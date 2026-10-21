#!/usr/bin/env python3
"""Evaluate pre-existing arithmetic continuations without rerunning their construction."""
import csv,hashlib,json
from pathlib import Path
import numpy as np
from localgap_metrics import per_zero,summarize
HERE=Path(__file__).resolve().parent;OUT=HERE/'outputs';N=2001052
DATA=Path('/Users/vcasana/Documents/·.· MATLAB/·.· bin_unicos');g=np.memmap(DATA/'zeross.bin',dtype='<f8',mode='r')
BASE=Path('/Users/vcasana/Documents/ChatGPT/Möbius/LawCasanya/work/v15_prep/outputs')
pilot=np.load(HERE.parent/'results_v2/pilot_inputs.npz')['k'];halo=np.load(OUT/'v17_recovered_neighbor.npz')
points=np.load(BASE/'task3_points.npy',mmap_mode='r');rows=[];inventory=[]
for j,name in enumerate(['v17_StageA','v17_R1','v17_R2']):
    k=np.arange(1400736,N+1);x=np.r_[halo['values'][j,0],points[j]]
    d=per_zero(k,x,g[k-1],N)
    for region,mask in [('final600316_existing_variant',k>=1400737),('pilot_last300',np.isin(k,pilot[-300:])),('high_consecutive_last300',k>N-300)]:
        rows.append(summarize(d,mask,name,region,'per-index: see original cutoffs','existing arithmetic rule; R2 model is heuristic, continuation checks sampled'))
    bad=d['violated']|d['structural'];np.savez_compressed(OUT/(name+'_violations.npz'),k=k[bad],error=d['error'][bad],d=d['d'][bad],R=d['R'][bad])
    inventory.append(dict(method=name,path=str(BASE/'task3_points.npy'),sha256=hashlib.sha256((BASE/'task3_points.npy').read_bytes()).hexdigest(),row=j,full_final_coverage=True))
for name in ['task4_points_c0.85.npy','task4_points_c1.00.npy','task4_points_c1.15_b3.npy','task4_points_c1.30_b3.npy']:
    p=BASE/name;a=np.load(p);k=a[0].astype(np.int64)+1;x=a[1];d=per_zero(k,x,g[k-1],N)
    label=name.replace('task4_points_','').replace('.npy','');rows.append(summarize(d,np.ones(len(k),bool),label,'existing_contiguous_blocks','per-index','arithmetic continuation at fixed exponent; historical test exposure; no new fit'))
    if name.endswith('_b3.npy'):
        for tag,values,pr in [('c667',np.memmap(DATA/'zCasanya.bin',dtype='<f8',mode='r')[k-1],97),('c667_PAV',np.memmap(OUT/'c667_PAV_a010.bin',dtype='<f8',mode='r')[k-1],97),('v17_R2',points[2,k-1400737],'per-index')]:
            q=per_zero(k,values,g[k-1],N);rows.append(summarize(q,np.ones(len(k),bool),tag,'same_'+label+'_block',pr,'same exact indices; both external endpoints unavailable in this table'))
    inventory.append(dict(method=label,path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),point_count=len(k),missing_external_neighbors=int(np.sum(~d['covered']))))
fields=list(dict.fromkeys(k for r in rows for k in r))
with (OUT/'other_versions_summary.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
(OUT/'other_versions_inventory.json').write_text(json.dumps(inventory,indent=2))
for r in rows:print(r['method'],r['region'],'n',r['covered'],'RMS',r['rms'],'fail',r['all_failure_count'],'Rmax',r['max_R'],flush=True)
