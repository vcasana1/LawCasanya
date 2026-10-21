#!/usr/bin/env python3
"""Arithmetic-only diagnostic: SAME LeClair equation, different solver.
Also counts target-level sign crossings locally. Does not invent a new method.
"""
import hashlib,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import brentq
import constructors as C

HERE=Path(__file__).resolve().parent;OUT=HERE/'results_v2'

def main():
    C.install_guard()
    data=np.load(OUT/'pilot_inputs.npz');k,tau=data['k'],data['tau'];pr=C.sieve(8192)
    old=np.load(OUT/'pilot_candidates.npz');out={};meta={};checks=[]
    conf=dict(equation='LeClair2016 eq49 delta1e-6, unchanged',solver='direct Newton, max40; unique positive bracket fallback',
              sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),true_zeros_available=False)
    (OUT/'solver_config_frozen.json').write_text(json.dumps(conf,indent=2))
    smooth=lambda t:C.N0(t)+1/(48*np.pi*t)
    smooth_d=lambda t:C.L(t)-1/(48*np.pi*t*t)
    for b in [7,31,127,511,2047,8191]:
        key=f'M1_direct_same_equation_P{b}';P=C.Phase(pr,b,'euler');start=time.perf_counter();x=tau.copy()
        for _ in range(40):
            s,ds=P(x);res=smooth(x)+s-(k-.5);der=smooth_d(x)+ds
            done=np.abs(res)<np.maximum(1e-10,16*np.spacing(k.astype(float)))
            if np.all(done):break
            step=np.clip(res/np.where(np.abs(der)>1e-12,der,np.nan),-.25/C.L(tau),.25/C.L(tau))
            xx=x-step;x=np.where(done|~np.isfinite(xx)|(xx<=2*np.pi),x,xx)
        s,ds=P(x);res=smooth(x)+s-(k-.5);bad=np.abs(res)>np.maximum(1e-9,32*np.spacing(k.astype(float)))
        recovered=0
        for z in np.flatnonzero(bad):
            fun=lambda tt:smooth(tt)+P(tt,derivative=False)[0]-(k[z]-.5)
            xx,nroots=C.bracket_fallback(fun,tau[z],1/C.L(tau[z]))
            if np.isfinite(xx):x[z]=xx;bad[z]=False;recovered+=1
        x[bad]=np.nan;elapsed=time.perf_counter()-start
        out[key]=x;meta[key]=P.budget()|dict(seconds=elapsed,newton_failures=int(bad.sum()+recovered),bracket_recoveries=recovered,
                                            same_published_equation=True,prime_by_prime_continuation=False)
        previous=old[f'M1_LeClair_P{b}'];good=np.isfinite(x)&np.isfinite(previous)
        # Count local roots on two grids, to expose ambiguity instead of picking against gamma.
        multiplicities=[]
        for width in [65,129]:
            mult=np.zeros(len(k),int);off=np.linspace(-2,2,width)
            for lo in range(0,len(k),50):
                hi=min(lo+50,len(k));tt=np.maximum(2*np.pi+1e-6,tau[lo:hi,None]+off[None,:]/C.L(tau[lo:hi,None]))
                h=smooth(tt)+P(tt.ravel(),derivative=False)[0].reshape(tt.shape)-(k[lo:hi,None]-.5)
                mult[lo:hi]=np.sum(h[:,:-1]*h[:,1:]<0,axis=1)
            multiplicities.append(mult)
        out[key+'_multiplicity']=multiplicities[-1]
        check=dict(cutoff=b,prime_count=meta[key]['prime_count'],n=len(k),direct_coverage=float(np.isfinite(x).mean()),
                   max_difference_on_common=float(np.max(np.abs(x[good]-previous[good]))),
                   differences_over_1e7=int(np.sum(np.abs(x[good]-previous[good])>1e-7)),
                   local_multiple_roots=int(np.sum(multiplicities[-1]>1)),local_no_roots=int(np.sum(multiplicities[-1]==0)),
                   refined_mesh_changes=int(np.sum(multiplicities[0]!=multiplicities[1])),direct_seconds=elapsed,
                   prime_continuation_seconds=json.loads((OUT/'constructor_metadata.json').read_text())[f'M1_LeClair_P{b}']['seconds'])
        checks.append(check);print(check,flush=True)
    np.savez(OUT/'solver_candidates.npz',**out)
    (OUT/'solver_metadata.json').write_text(json.dumps(meta,indent=2))
    (OUT/'same_equation_checks.json').write_text(json.dumps(checks,indent=2))

if __name__=='__main__':main()
