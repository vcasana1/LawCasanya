#!/usr/bin/env python3
"""Independent true-zero evaluation of existing and newly constructed Casanya variants."""
import csv,gzip,hashlib,importlib.util,json,sys
from pathlib import Path
import numpy as np
from localgap_metrics import per_zero,summarize,self_check

HERE=Path(__file__).resolve().parent;OUT=HERE/'outputs';OLD=HERE.parent
DATA=Path('/Users/vcasana/Documents/·.· MATLAB/·.· bin_unicos');N=2001052
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def csvout(name,rows):
    fields=list(dict.fromkeys(k for r in rows for k in r))
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)

def main():
    self_check();truth=np.fromfile(DATA/'zeross.bin',dtype='<f8');tau=np.fromfile(DATA/'zLamb.bin',dtype='<f8')
    k=np.arange(1,N+1);oldk=np.load(OLD/'results_v2/pilot_inputs.npz')['k'];regions={
      'first1000':k<=1000,'fixed_pilot1000':np.isin(k,oldk),'pilot_last300':np.isin(k,oldk[-300:]),
      'high_consecutive_last300':k>N-300,'final600316_baseline_only':k>=1400737,'all2001052_baseline_only':np.ones(N,bool)}
    meta=json.loads((OUT/'baseline_constructor_metadata.json').read_text())
    methods={'c667_original':dict(path=str(DATA/'zCasanya.bin'),prime_count=97,provenance='frozen c667, validation-selected historical parameters'),
             'zCasanya_matlab_existing':dict(path=str(DATA/'zCasanya_matlab.bin'),prime_count=97,provenance='historical MATLAB replication; rounding differs'),
             'zCasanya0_existing':dict(path=str(DATA/'zCasanya0.bin'),prime_count='unknown',provenance='existing optimized file; truth-selected cutoff/alpha possible; configuration not identified')}
    methods.update(meta);rows=[];inventory=[];windowrows=[]
    for name,m in methods.items():
        p=Path(m['path']);x=np.fromfile(p,dtype='<f8');assert len(x)==N
        d=per_zero(k,x,truth,N)
        for reg,mask in regions.items():rows.append(summarize(d,mask,name,reg,m['prime_count'],m['provenance']))
        for lo in range(0,N,50000):
            hi=min(lo+50000,N);mask=(k>lo)&(k<=hi)
            windowrows.append(summarize(d,mask,name,f'window_{lo+1}_{hi}',m['prime_count'],m['provenance']))
        inventory.append(dict(method=name,path=str(p),bytes=p.stat().st_size,sha256=sha(p),**{a:m[a] for a in ['prime_count','provenance']}))
        # Small human-readable table: requested pilot sets, with true k±1 synthetic neighbours.
        pick=regions['first1000']|regions['fixed_pilot1000']|regions['high_consecutive_last300']
        fields=['k','model','truth','error','abs_error','left_gap','right_gap','d','R','covered','structural','passed','violated','directional_gap','directional_R','directional_passed','directional_violated']
        with gzip.open(OUT/(name+'_pilot_per_zero.csv.gz'),'wt',newline='') as f:
            w=csv.writer(f);w.writerow(fields)
            for i in np.flatnonzero(pick):w.writerow([d[a][i] for a in fields])
        # Complete violation locations, sufficient to reproduce counts and inspect every offender.
        bad=d['violated']|d['directional_violated']|d['structural'];np.savez_compressed(OUT/(name+'_violations.npz'),k=k[bad],error=d['error'][bad],d=d['d'][bad],R=d['R'][bad],directional_R=d['directional_R'][bad],structural=d['structural'][bad])
        # Binary per-zero table for the final region: arithmetic rows, not a validated cross-model leaderboard.
        tail=regions['final600316_baseline_only'];np.savez_compressed(OUT/(name+'_final_per_zero.npz'),k=k[tail],model=x[tail],error=d['error'][tail],d=d['d'][tail],R=d['R'][tail],left_gap=d['left_gap'][tail],right_gap=d['right_gap'][tail],directional_R=d['directional_R'][tail])
        q=rows[-1];print(name,'RMS',q['rms'],'Rmax',q['max_R'],'violations',q['all_failure_count'],'structural',q['structural_failure_count'],flush=True)
    # Existing v17 arrays already cover the final region: evaluate, do not reconstruct.
    path=Path('/Users/vcasana/Documents/ChatGPT/Möbius/LawCasanya/work/v15_prep/outputs/task3_points.npy')
    points=np.load(path,mmap_mode='r');kk=np.arange(1400737,N+1)
    for i,label in enumerate(['v17_StageA_existing','v17_R1_existing','v17_R2_existing']):
        d=per_zero(kk,points[i],truth[kk-1],N)
        # First point needs its predecessor outside the supplied file. Mark missing, do not invent it.
        for reg,mask in [('final600316_existing_variant_only',np.ones(len(kk),bool)),('pilot_last300',np.isin(kk,oldk[-300:])),('high_consecutive_last300',kk>N-300)]:
            rows.append(summarize(d,mask,label,reg,'per-index','existing arithmetic continuation; five-point segment checks, not interval certificate'))
        inventory.append(dict(method=label,path=str(path),sha256=sha(path),row=i,provenance='arithmetic construction, error evaluated later; rule R2 heuristic prime-tail sigma'))
    csvout('casanya_localgap_summary.csv',rows);csvout('casanya_by_height.csv',windowrows)
    (OUT/'candidate_inventory.json').write_text(json.dumps(inventory,indent=2))
    (OUT/'baseline_evaluation_complete.json').write_text(json.dumps(dict(complete=True,convention='e=model-truth; primary directional synthetic midpoint cell, outer endpoints unbounded; legacy symmetric minimum also reported',full_comparison_M1_M2_complete=False),indent=2))

if __name__=='__main__':main()
