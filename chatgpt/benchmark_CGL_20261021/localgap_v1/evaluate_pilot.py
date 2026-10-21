#!/usr/bin/env python3
"""All pilot methods, same actual k, same immediate-neighbour criterion."""
import csv,gzip,json,sys
from pathlib import Path
import numpy as np
from localgap_metrics import per_zero,summarize,self_check
HERE=Path(__file__).resolve().parent;OLD=HERE.parent;OUT=HERE/'outputs';sys.path.insert(0,str(OLD));import constructors as C
DATA=Path('/Users/vcasana/Documents/·.· MATLAB/·.· bin_unicos')
self_check();sets=np.load(OUT/'pilot_index_sets.npz');k=sets['k'];N=2001052
g=np.memmap(DATA/'zeross.bin',dtype='<f8',mode='r');tau=np.memmap(DATA/'zLamb.bin',dtype='<f8',mode='r')
pred=np.load(OUT/'pilot_models.npz');meta=json.loads((OUT/'pilot_constructor_metadata.json').read_text())
regions={name:np.isin(k,sets[name]) for name in ['first1000','old_pilot','pilot_last300','high_consecutive_last300']}
regions['fixed_pilot1000']=regions.pop('old_pilot')
rows=[]
def export(name,x,prime_count,origin,root_count=None,residual=None):
    d=per_zero(k,x,g[k-1],N)
    for region,mask in regions.items():
        r=summarize(d,mask,name,region,prime_count,origin)
        r['root_index_status']='phase_labels_numerically_checked; global_enumeration_pending' if root_count is not None else 'input_index_preserved'
        if root_count is not None:r['local_multiple_root_labels']=int(np.sum(mask&(root_count>1)))
        rows.append(r)
    fields=['k','model','truth','error','abs_error','left_gap','right_gap','d','R','covered','structural','passed','violated','directional_gap','directional_R','directional_passed','directional_violated']
    with gzip.open(OUT/(name+'_pilot_per_zero.csv.gz'),'wt',newline='') as f:
        w=csv.writer(f);w.writerow(fields+(['local_target_root_count','phase_residual'] if root_count is not None else []))
        for i in range(len(k)):
            a=[d[q][i] for q in fields]
            if root_count is not None:a.extend([root_count[i],residual[i]])
            w.writerow(a)
    return d
export('Lambert',tau[k-1],0,'input baseline')
for name in meta:
    export(name,pred[name],meta[name]['prime_count'],'published equation, same frozen k; no sorting or nearest-zero selection',pred[name+'_root_count'],pred[name+'_phase_residual'])
baseline_meta=json.loads((OUT/'baseline_constructor_metadata.json').read_text())
baseline_meta['c667_original']=dict(path=str(DATA/'zCasanya.bin'),prime_count=97,provenance='frozen historically validation-selected c667')
for name,m in baseline_meta.items():
    x=np.memmap(m['path'],dtype='<f8',mode='r')[k-1];export(name,x,m['prime_count'],m['provenance'])
fields=list(dict.fromkeys(a for row in rows for a in row))
with (OUT/'pilot_localgap_summary.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
# Root-solver diagnostic on the EXACT same sharp cutoff equation as the arithmetic clocks.
diagnostics=[];pr=C.sieve(8192)
for tier in [512,2048,8192]:
    P=C.Phase(pr,tier,'sharp')
    for tag in [f'Casanya_constant_X{tier}',f'Casanya_constant_X{tier}_PAV_a010',f'Casanya_root_X{tier}']:
        x=pred[tag] if tag in pred.files else np.memmap(baseline_meta[tag]['path'],dtype='<f8',mode='r')[k-1]
        res=C.N0(x)+P(x,derivative=False)[0]-(k-.5)
        for region,mask in regions.items():diagnostics.append(dict(method=tag,tier=tier,region=region,
          phase_residual_rms=float(np.sqrt(np.mean(res[mask]**2))),max_abs_phase_residual=float(np.max(np.abs(res[mask])))))
with (OUT/'same_equation_solver_diagnostic.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(diagnostics[0]));w.writeheader();w.writerows(diagnostics)
(OUT/'pilot_evaluation_complete.json').write_text(json.dumps(dict(complete=True,n_computed_context=len(k),requested_sets={n:int(q.sum()) for n,q in regions.items()},no_mean_spacing_criterion=True),indent=2))
for r in rows:
    if r['region']=='pilot_last300':print(r['method'],'rms',r['rms'],'maxabs',r['max_abs'],'Rmax',r['max_R'],'fail',r['all_failure_count'],'kR',r['max_R_k'],flush=True)
