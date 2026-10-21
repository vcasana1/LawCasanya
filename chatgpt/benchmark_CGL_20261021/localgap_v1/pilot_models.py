#!/usr/bin/env python3
"""Continue existing predictions, adding actual neighbours and consecutive windows.
No true ordinates; published equations unchanged. Do not sort roots or match gamma.
"""
import hashlib,json,sys,time
from pathlib import Path
import numpy as np
from scipy.optimize import brentq

HERE=Path(__file__).resolve().parent;OLD=HERE.parent;OUT=HERE/'outputs';OUT.mkdir(exist_ok=True)
sys.path.insert(0,str(OLD));import constructors as C
DATA=Path('/Users/vcasana/Documents/·.· MATLAB/·.· bin_unicos')
def guard(event,args):
    if event=='open' and args and isinstance(args[0],(str,bytes)) and 'zeross' in str(args[0]).lower():raise PermissionError('Truth forbidden')
sys.addaudithook(guard)
tauall=np.fromfile(DATA/'zLamb.bin',dtype='<f8');N=len(tauall)
previous=np.load(OLD/'results_v2/pilot_inputs.npz');oldk=previous['k'];old=np.load(OLD/'results_v2/pilot_candidates.npz')
targets=np.unique(np.r_[np.arange(1,1001),oldk,np.arange(N-299,N+1)])
k=np.unique(np.r_[targets,targets[targets>1]-1,targets[targets<N]+1]);tau=tauall[k-1]
pr=C.sieve(8192);configs=[]
for tier in [512,2048,8192]:
    for method in ['Gonek','LeClair','Casanya_root']:
        configs.append(dict(method=method,tier=tier,prime_count=int(np.sum(pr<=tier)),
                            root_policy='fixed target level k, warm Newton plus unique positive bracket fallback; report multiple roots',
                            ordinal_enumeration='pending_global_count'))
config=dict(configs=configs,alpha=.1,indices=k.tolist(),targets=targets.tolist(),old_pilot=oldk.tolist(),
            no_true_zero_access=True,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(OUT/'pilot_config_frozen.json').write_text(json.dumps(config,indent=2))
np.savez(OUT/'pilot_index_sets.npz',k=k,targets=targets,old_pilot=oldk,first1000=np.arange(1,1001),pilot_last300=oldk[-300:],high_consecutive_last300=np.arange(N-299,N+1),tau=tau)

class Model:
    def __init__(self,kind,tier):
        self.kind=kind;self.tier=tier
        self.P=C.Phase(pr,tier,'gonek',np.sqrt(tier)) if kind=='Gonek' else C.Phase(pr,tier,'euler' if kind=='LeClair' else 'sharp')
    def smooth(self,t):
        if self.kind=='Gonek':return 1+C.theta(t)/np.pi
        return C.N0(t)+(1/(48*np.pi*t) if self.kind=='LeClair' else 0)
    def slope(self,t):
        if self.kind=='Gonek':return C.theta_d(t)/np.pi
        return C.L(t)-(1/(48*np.pi*t*t) if self.kind=='LeClair' else 0)
    def f(self,t,kk,der=True):
        s,ds=self.P(t,derivative=der);return self.smooth(t)+s-(kk-.5),self.slope(t)+ds
    def solve(self,tau,kk):
        x=tau.copy();tol=np.maximum(1e-10,16*np.spacing(kk.astype(float)))
        for _ in range(40):
            r,d=self.f(x,kk);done=np.abs(r)<=tol
            if done.all():break
            step=np.clip(r/np.where(np.abs(d)>1e-12,d,np.nan),-.25/C.L(tau),.25/C.L(tau))
            y=x-step;good=np.isfinite(y)&(y>2*np.pi)&~done;x[good]=y[good]
        r,d=self.f(x,kk);bad=np.abs(r)>np.maximum(1e-9,32*np.spacing(kk.astype(float)))
        failed_before=int(bad.sum());recovered=0
        for i in np.flatnonzero(bad):
            fun=lambda t:self.f(t,np.full(len(t),kk[i]),False)[0]
            root,count=C.bracket_fallback(fun,tau[i],1/C.L(tau[i]))
            if np.isfinite(root):x[i]=root;bad[i]=False;recovered+=1
        x[bad]=np.nan
        return x,dict(newton_failures=failed_before,unique_bracket_recovered=recovered,missing=int(bad.sum()))

def prefix_enumeration(model):
    # Include the near-axis region as an explicit diagnostic, rather than silently dropping it.
    stop=float(tauall[1000]+1);counts=[];last=None;seconds=[]
    for step in [.04,.02]:
        st=time.perf_counter();ts=np.linspace(.01,stop,int((stop-.01)/step)+2)
        h=model.smooth(ts)+model.P(ts,derivative=False)[0];levels=np.floor(h+.5).astype(np.int64)
        delta=np.diff(levels);cells=np.flatnonzero(delta!=0);out=[]
        for i in cells:
            for kk in range(min(levels[i],levels[i+1])+1,max(levels[i],levels[i+1])+1):
                out.append((ts[i],ts[i+1],kk,int(np.sign(delta[i]))))
        counts.append(len(out));last=np.array(out);seconds.append(time.perf_counter()-st)
    return last,dict(prefix_stop=stop,prefix_counts=counts,stable_counts=counts[0]==counts[1],
                     prefix_downcrossings=int(np.sum(last[:,3]<0)),near_axis_events=int(np.sum(last[:,0]<6.3)),
                     mesh_seconds=seconds,global_ordinal_validated=False)

def main():
    meta={};result={}
    for conf in configs:
        kind,tier=conf['method'],conf['tier'];name=f'{kind}_X{tier}';m=Model(kind,tier);st=time.perf_counter()
        cache_name=f'M2_Gonek_level_P{tier-1}' if kind=='Gonek' else f'M1_LeClair_P{tier-1}'
        x=np.full(len(k),np.nan);cached=np.isin(k,oldk) if kind!='Casanya_root' else np.zeros(len(k),bool)
        if cached.any():x[cached]=old[cache_name][np.searchsorted(oldk,k[cached])]
        new=~cached;xx,diag=m.solve(tau[new],k[new]);x[new]=xx
        res=np.full(len(k),np.nan);finite=np.isfinite(x);res[finite]=m.f(x[finite],k[finite],False)[0]
        assert np.all(np.abs(res[finite])<=np.maximum(2e-8,64*np.spacing(k[finite].astype(float))))
        elapsed=time.perf_counter()-st;budget=m.P.budget()
        # Local root multiplicity on real k±1 context, with a refined grid.
        mults=[]
        for ng in [65,129]:
            mult=np.zeros(len(k),int);offset=np.linspace(-2,2,ng)
            for lo in range(0,len(k),40):
                hi=min(lo+40,len(k));tt=np.maximum(2*np.pi+1e-6,tau[lo:hi,None]+offset[None,:]/C.L(tau[lo:hi,None]))
                vals=m.f(tt.ravel(),np.repeat(k[lo:hi],ng),False)[0].reshape(tt.shape)
                mult[lo:hi]=np.sum(vals[:,:-1]*vals[:,1:]<0,axis=1)
            mults.append(mult)
        audit={}
        if kind in ['Gonek','LeClair']:
            prefix,audit=prefix_enumeration(m);np.savez_compressed(OUT/(name+'_prefix_enumeration.npz'),cells=prefix)
        result[name]=x;result[name+'_root_count']=mults[-1];result[name+'_phase_residual']=res
        meta[name]=dict(conf|diag|budget,seconds=elapsed,cached_points=int(cached.sum()),new_points=int(new.sum()),
                        local_multiple=int(np.sum(mults[-1]>1)),local_missing=int(np.sum(mults[-1]==0)),
                        multiplicity_mesh_changes=int(np.sum(mults[0]!=mults[1])),**audit)
        np.savez(OUT/'pilot_models.npz',**result)
        (OUT/'pilot_constructor_metadata.json').write_text(json.dumps(meta,indent=2))
        print(name,meta[name],flush=True)
    (OUT/'pilot_constructor_complete.json').write_text(json.dumps(dict(complete=True,truth_free=True,n=len(k)),indent=2))

if __name__=='__main__':main()
