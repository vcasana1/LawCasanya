#!/usr/bin/env python3
"""Refine final-region roots ONLY after the numerical regular-branch index gate.
No sorting/matching to true zeros. The same label k fixes each target level.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from pilot_models import Model,C,tauall,N,OUT

def main():
    ap=argparse.ArgumentParser();ap.add_argument('method',choices=['Gonek','LeClair']);ap.add_argument('tier',type=int);args=ap.parse_args()
    name=f'{args.method}_X{args.tier}';gd=OUT/'global_index';gate=json.loads((gd/(name+'_enumeration.json')).read_text())
    selection=None
    if not gate['numerical_regular_index_gate_passed']:
        selected_path=gd/(name+'_selection_gate.json')
        if selected_path.exists():selection=json.loads(selected_path.read_text())
        if selection is None or not selection['phase_index_selection_gate_passed']:
            raise RuntimeError('Regular-family unique-level gate failed; validated explicit branch selection is required')
    z=np.load(gd/f'{name}_step0.04_checkpoint.npz');k=np.arange(1400737-1024,N+1)
    lo=z['left'][k].copy();hi=z['right'][k].copy();assert np.all(np.isfinite(lo)&(lo<hi))
    if selection is not None:
        # Keep original target k. Use the previously published constructor to
        # select the branch; never choose the root with smallest true error.
        for label,value in selection['selected_roots'].items():
            pick=k==int(label);lo[pick]=value-1e-6;hi[pick]=value+1e-6
    m=Model(args.method,args.tier);t0=time.perf_counter();out=np.empty(len(k));resout=np.empty(len(k));iterations=[]
    for start in range(0,len(k),8000):
        end=min(start+8000,len(k));kk=k[start:end];a=lo[start:end].copy();b=hi[start:end].copy()
        fa,_=m.f(a,kk,False);fb,_=m.f(b,kk,False);assert np.all((fa<=0)&(fb>=0))
        x=a-fa*(b-a)/(fb-fa);done=np.zeros(len(kk),bool);tol=np.maximum(1e-10,16*np.spacing(kk.astype(float)))
        for it in range(45):
            r,der=m.f(x,kk);newdone=(np.abs(r)<=tol)|((b-a)<=5e-10);done|=newdone
            if done.all():break
            neg=r<0;a=np.where(~done&neg,x,a);b=np.where(~done&~neg,x,b)
            step=x-r/np.where(np.abs(der)>1e-12,der,np.nan)
            inside=np.isfinite(step)&(step>a)&(step<b)
            proposal=np.where(inside,step,.5*(a+b));x=np.where(done,x,proposal)
        r,_=m.f(x,kk,False)
        assert np.all(np.abs(r)<=np.maximum(2e-8,64*np.spacing(kk.astype(float))))
        out[start:end]=x;resout[start:end]=r;iterations.append(it+1)
        if start%80000==0 or end==len(k):print(name,'refined',end,'/',len(k),'seconds',time.perf_counter()-t0,flush=True)
    assert np.all(np.diff(out)>0)
    path=OUT/(name+'_final_with_halo.npz');np.savez_compressed(path,k=k,model=out,phase_residual=resout)
    result=dict(complete=True,method=args.method,tier=args.tier,n_final=600316,halo=1024,
      numerical_regular_index_gate_passed=gate['numerical_regular_index_gate_passed'],
      explicit_phase_index_selection_gate_passed=selection is not None,
      branch_policy='unique level root; ambiguous levels use existing prime-by-prime construction',
      all_positive_model_root_indexing_claimed=False,
      regular_family_start=6.3,interval_certified=False,seconds=time.perf_counter()-t0,
      max_phase_residual=float(np.max(np.abs(resout))),min_synthetic_gap=float(np.min(np.diff(out))),
      max_iterations=max(iterations),prime_budget=m.P.budget())
    (OUT/(name+'_final_constructor.json')).write_text(json.dumps(result,indent=2));print(result,flush=True)

if __name__=='__main__':main()
