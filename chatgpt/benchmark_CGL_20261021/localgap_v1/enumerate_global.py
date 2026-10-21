#!/usr/bin/env python3
"""Numerical enumeration of the regular root family, from t=6.3 to final k.

This is an explicit branch audit, NOT enumeration of every near-axis artefact
of a high-t approximation. The pilot preserves these extra near-axis roots.
No truth input. A gate requires exactly one ascending crossing of every level
k-1/2, k=1..N, on TWO uniform meshes. Mesh agreement is numerical evidence,
not an interval-arithmetic proof or a claim about actual zeta root indices.
"""
import argparse,json,os,time
from pathlib import Path
import numpy as np
from pilot_models import Model,C,tauall,N,OUT

def atomic(path,data):
    temp=path.with_suffix('.tmp');temp.write_text(json.dumps(data,indent=2));os.replace(temp,path)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('method',choices=['Gonek','LeClair']);ap.add_argument('--fast',action='store_true');args=ap.parse_args()
    if args.fast:from fastphase import evaluate as fast_evaluate
    method=args.method;start_t=6.3;stop=float(tauall[-1]+4/C.L(tauall[-1]));outdir=OUT/'global_index';outdir.mkdir(exist_ok=True)
    tiers=[512,2048,8192];config=dict(method=method,tiers=tiers,start_t=start_t,stop_t=stop,steps=[.08,.04],
      family='regular critical roots above6.3, same target k and original Lambert-warm branch; near-axis roots separately reported',
      definition_warning='not every positive root of the high-height equation; no near-axis root is relabelled into k=1',truth_access=False,
      resumed_backend='optional validated vForce, same formula' if args.fast else 'NumPy')
    atomic(outdir/(method+'_config.json'),config)
    for tier in tiers:
        destination=outdir/f'{method}_X{tier}_enumeration.json'
        if destination.exists() and json.loads(destination.read_text()).get('complete'):continue
        model=Model(method,tier);records=[];allcounts=[]
        for step in config['steps']:
            statepath=outdir/f'{method}_X{tier}_step{step}_checkpoint.npz'
            last_i=0;counts=np.zeros(N+64,np.uint16);downs=np.zeros(N+64,np.uint16)
            left=np.full(N+64,np.nan);right=np.full(N+64,np.nan)
            elapsed_old=0
            if statepath.exists():
                z=np.load(statepath);last_i=int(z['last_i']);counts=z['counts'];downs=z['downs'];left=z['left'];right=z['right'];elapsed_old=float(z['elapsed'])
            total=int(np.ceil((stop-start_t)/step));st=time.perf_counter();chunk=50000
            hprev=None
            for i in range(last_i,total,chunk):
                j=min(i+chunk,total);tt=start_t+np.arange(i,j+1)*step;tt[-1]=min(tt[-1],stop)
                phase=fast_evaluate(model.P,tt) if args.fast else model.P(tt,derivative=False)[0]
                h=model.smooth(tt)+phase
                lev=np.floor(h+.5).astype(np.int64);delta=np.diff(lev);cross=np.flatnonzero(delta)
                for direction in [1,-1]:
                    at=cross[np.sign(delta[cross])==direction]
                    if not len(at):continue
                    if np.all(np.abs(delta[at])==1):
                        labels=np.maximum(lev[at],lev[at+1])
                        good=(labels>=1)&(labels<=N+63);labs=labels[good];aa=at[good]
                        np.add.at(counts,labs,1)
                        if direction<0:np.add.at(downs,labs,1)
                        left[labs]=tt[aa];right[labs]=tt[aa+1]
                    else:
                        for cell in at:
                            for label in range(min(lev[cell],lev[cell+1])+1,max(lev[cell],lev[cell+1])+1):
                                if 1<=label<len(counts):
                                    counts[label]+=1;downs[label]+=direction<0;left[label]=tt[cell];right[label]=tt[cell+1]
                elapsed=elapsed_old+time.perf_counter()-st
                if (i//chunk)%20==0 or j==total:
                    with statepath.with_suffix('.tmp').open('wb') as f:np.savez_compressed(f,last_i=j,counts=counts,downs=downs,left=left,right=right,elapsed=elapsed)
                    os.replace(statepath.with_suffix('.tmp'),statepath)
                    atomic(outdir/f'{method}_progress.json',dict(method=method,tier=tier,step=step,completed_points=j,total_points=total,percent=100*j/total,seconds=elapsed))
                    print(method,tier,step,f'{100*j/total:.1f}%',f'{elapsed:.1f}s',flush=True)
            required=counts[1:N+1];down=downs[1:N+1]
            r=dict(step=step,seconds=elapsed_old+time.perf_counter()-st,n_required=N,
                   missing_labels=int(np.sum(required==0)),multiple_labels=int(np.sum(required>1)),
                   descending_events=int(down.sum()),total_events_required=int(required.sum()),
                   exactly_one_ascending_per_k=bool(np.all(required==1)&np.all(down==0)))
            records.append(r);allcounts.append(required.copy())
        gate=all(r['exactly_one_ascending_per_k'] for r in records) and np.array_equal(*allcounts)
        atomic(destination,dict(complete=True,method=method,tier=tier,regular_family_start=start_t,
                               numerical_regular_index_gate_passed=gate,interval_certified=False,meshes=records,
                               all_positive_model_zeros_indexed=False,near_axis_exceptions_preserved_in_pilot=True))
        print('GATE',method,tier,gate,records,flush=True)

if __name__=='__main__':main()
