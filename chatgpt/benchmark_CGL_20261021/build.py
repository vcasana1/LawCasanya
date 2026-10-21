#!/usr/bin/env python3
"""Construct and audit pilot candidates in a process barred from reference zeros."""
import argparse, hashlib, json, os, resource, time
from pathlib import Path
import numpy as np
from scipy.special import lambertw
from scipy.optimize import brentq
import constructors as C

HERE=Path(__file__).resolve().parent
DATA=Path('/Users/vcasana/Documents/·.· MATLAB/·.· bin_unicos')
BUDGETS=[7,31,127,511,2047,8191]

def dump(path,value):
    tmp=path.with_suffix(path.suffix+'.tmp');tmp.write_text(json.dumps(value,indent=2,allow_nan=False));os.replace(tmp,path)

def sample_indices():
    groups=[]
    for lo,hi,n in [(1,800420,400),(800421,1400736,300),(1400737,2001052,300)]:
        windows=np.r_[np.arange(lo,lo+64),np.arange((lo+hi)//2,(lo+hi)//2+64),np.arange(hi-63,hi+1)]
        isolated=np.linspace(lo+128,hi-128,n-len(windows)).astype(int)
        out=np.unique(np.r_[windows,isolated]);assert len(out)==n
        groups.append(out)
    return np.concatenate(groups)

def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(8*1024**2),b''):h.update(b)
    return h.hexdigest()

def audit_model(P,k,tau,budget,outdir):
    """Two-grid critical root enumeration on [6.3,tau_1000+spacing].
    Mesh convergence is measured, not interval certification. Independently
    report sampled target-level multiplicity near each clock point.
    """
    start=time.perf_counter()
    stop=float(2*np.pi*(1000-1.375)/lambertw((1000-1.375)/np.e).real+2)
    counts=[];roots_final=[]
    for dt in [.04,.02]:
        ts=np.linspace(6.3,stop,int(np.ceil((stop-6.3)/dt))+1)
        h=1+C.theta(ts)/np.pi+P(ts,derivative=False)[0]
        lev=np.floor(h+.5).astype(int)
        cells=np.flatnonzero(lev[1:]!=lev[:-1]);roots=[]
        for i in cells:
            for label in range(min(lev[i],lev[i+1])+1,max(lev[i],lev[i+1])+1):
                target=label-.5
                fun=lambda t:float(1+C.theta(t)/np.pi+P(np.array([t]),derivative=False)[0][0]-target)
                rt=brentq(fun,ts[i],ts[i+1],xtol=1e-11)
                roots.append((rt,label,int(np.sign(h[i+1]-h[i]))))
        counts.append(len(roots));roots_final=roots
    # Sampled local root multiplicities at the requested label, never matching gamma.
    offsets=np.linspace(-2,2,65)
    mult=np.zeros(len(k),int)
    for lo in range(0,len(k),50):
        hi=min(lo+50,len(k));tt=tau[lo:hi,None]+offsets[None,:]/C.L(tau[lo:hi,None])
        tt=np.maximum(tt,6.3)
        h=1+C.theta(tt)/np.pi+P(tt.ravel(),derivative=False)[0].reshape(tt.shape)-(k[lo:hi,None]-.5)
        mult[lo:hi]=np.sum(h[:,:-1]*h[:,1:]<0,axis=1)
    np.savetxt(outdir/f'gonek_roots_prefix_P{budget}.csv',np.array(roots_final),delimiter=',',header='root,phase_label,direction',comments='')
    return dict(prefix_start=6.3,prefix_stop=stop,prefix_mesh_counts=counts,
                prefix_mesh_count_stable=counts[0]==counts[1],
                prefix_extra_downcrossings=sum(r[2]<0 for r in roots_final),
                local_multiple_target_roots=int(np.sum(mult>1)),local_no_target_root=int(np.sum(mult==0)),
                global_enumeration_to_sample_max=False,interval_certified=False,
                root_enumeration_seconds=time.perf_counter()-start),mult

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',default=str(HERE/'results'));a=ap.parse_args()
    out=Path(a.output);out.mkdir(parents=True,exist_ok=True)
    C.install_guard()
    denied=[]
    for name in ['zeross.bin','zCasanya.bin']:
        try:open(DATA/name,'rb')
        except PermissionError:denied.append(name)
    assert len(denied)==2
    tauall=np.fromfile(DATA/'zLamb.bin',dtype='<f8');assert len(tauall)==2001052
    primes=np.fromfile(DATA/'primoss.bin',dtype='<u8',count=148934).astype(np.int64)
    assert np.array_equal(primes[:-1],C.sieve(2000000)) and primes[-1]==2000003
    k=sample_indices();tau=tauall[k-1]
    config=dict(code_sha256={n:sha(HERE/n) for n in ['constructors.py','build.py']},
                indices=k.tolist(),budgets=BUDGETS,construction_allowlist=['zLamb.bin','primoss.bin'],
                denied_files_verified=denied,precision='float64',lc_delta=1e-6,
                lc_root_selection='prime-by-prime warm start; max12 clipped Newton; positive bracket fallback only when unique; failures sticky',
                gonek_root_selection='phase level k; max40 local Newton; positive unique bracket fallback; ordinal index NOT assumed',
                lc_reference='LeClair arXiv:1601.00914v1 pp18-19 eq49, Stirling eq48, delta TableI',
                gonek_reference='Gonek TAMS 364 (2012) pp2162-2163 eq3.4-3.5; pp2170-2172 eq5.2,7.4',
                github_commit='24d9d84862bced814fea8b9a8cae8bf97ac4b5a7',
                v17_reference='v17 code common + work/v15_prep/opc_task3_analytic_rule.py',
                stop_rule='No full M1-M2 benchmark unless complete coverage and ordinal enumeration validated; no gamma tuning')
    config['configuration_sha256']=hashlib.sha256(json.dumps(config,sort_keys=True).encode()).hexdigest()
    dump(out/'config_frozen.json',config) # before any evaluator runs
    np.savez(out/'pilot_inputs.npz',k=k,tau=tau)
    meta={};vals={'M0_Lambert':tau};failures=[]
    st=time.perf_counter();full,m=C.c667(tauall,np.arange(1,len(tauall)+1),primes)
    m['seconds']=time.perf_counter()-st;meta['M3_c667']=m
    full.astype('<f8').tofile(out/'c667_reconstructed.bin');vals['M3_c667']=full[k-1]
    print('c667 full reconstruction',m,flush=True)
    st=time.perf_counter();lc=C.lc_continuation(tau,k,primes,BUDGETS)
    for b,(x,m,issues) in lc.items():
        key=f'M1_LeClair_P{b}';vals[key]=x;meta[key]=m
        failures.extend(dict(method=key,k=i,type=t,prime=p) for i,t,p in issues)
        print(key,'seconds',m['seconds'],'coverage',np.isfinite(x).mean(),flush=True)
    for b in BUDGETS:
        key=f'M2_Gonek_level_P{b}';P=C.Phase(primes,b+1,'gonek',np.sqrt(b+1))
        x,m=C.solve_level(tau,k,P);vals[key]=x;meta[key]=m
        audit,mult=audit_model(P,k,tau,b,out);meta[key]|=audit
        vals[key+'_multiplicity']=mult
        print(key,'seconds',m['seconds'],'coverage',np.isfinite(x).mean(),'audit',audit,flush=True)
    P=C.Phase(primes,200000,'sharp')
    st=time.perf_counter();xA,Xmon,valid=C.stage_a(tau,k,P)
    vals['M4_v17_StageA']=xA;vals['M4_v17_Xmon']=Xmon
    meta['M4_v17_StageA']=P.budget()|dict(seconds=time.perf_counter()-st,analytic_monotonicity_checked=True)
    for rule in ['R1','R2']:
        P.calls=P.work=P.derivative_work=P.raw_work=0;P.max_requested=0
        st=time.perf_counter();x,cut,m=C.v17_continuation(tau,k,P,xA,Xmon,rule)
        key=f'M4_v17_{rule}';vals[key]=x;vals[key+'_cut']=cut
        meta[key]=P.budget()|m|dict(seconds=time.perf_counter()-st,actual_max_cut=float(cut.max()))
        print(key,'seconds',meta[key]['seconds'],'coverage',np.isfinite(x).mean(),flush=True)
    np.savez(out/'pilot_candidates.npz',**vals)
    dump(out/'constructor_metadata.json',meta);dump(out/'constructor_failures.json',failures)
    dump(out/'constructor_complete.json',dict(complete=True,maxrss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                                             note='macOS ru_maxrss bytes; includes full c667 reconstruction'))

if __name__=='__main__':main()
