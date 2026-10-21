#!/usr/bin/env python3
"""Common final600316 comparison, only for complete index-gated pairs.
Optional competitor PAV is REGIONAL with explicit halos, not full-array PAV.
"""
import csv,gzip,importlib.util,json
from pathlib import Path
import numpy as np
from localgap_metrics import per_zero,summarize
HERE=Path(__file__).resolve().parent;OUT=HERE/'outputs';N=2001052
DATA=Path('/Users/vcasana/Documents/·.· MATLAB/·.· bin_unicos');truth=np.memmap(DATA/'zeross.bin',dtype='<f8',mode='r');tau=np.memmap(DATA/'zLamb.bin',dtype='<f8',mode='r')
spec=importlib.util.spec_from_file_location('pav',HERE/'sources/casanya_monotone_projection.py');pav=importlib.util.module_from_spec(spec);spec.loader.exec_module(pav)
pilot=np.load(HERE.parent/'results_v2/pilot_inputs.npz')['k'];rows=[];windows=[];checks=[]
baseline_meta=json.loads((OUT/'baseline_constructor_metadata.json').read_text())
def export(k,x,name,tier,pr,provenance,save_perzero=True):
    d=per_zero(k,x,truth[k-1],N)
    for region,mask in [('final600316',k>=1400737),('pilot_last300',np.isin(k,pilot[-300:])),('high_consecutive_last300',k>N-300)]:
        row=summarize(d,mask,name,region,pr,provenance);row['tier']=tier;rows.append(row)
    for lo in range(1400737,N+1,10000):
        mask=(k>=lo)&(k<min(lo+10000,N+1));r=summarize(d,mask,name,f'k{lo}_{min(lo+9999,N)}',pr,provenance);r['tier']=tier;windows.append(r)
    tail=k>=1400737;bad=tail&(d['violated']|d['directional_violated']|d['structural'])
    fields=['k','model','truth','error','abs_error','left_gap','right_gap','d','R','structural','directional_gap','directional_R','directional_passed','directional_violated']
    with gzip.open(OUT/(name+'_final_violations.csv.gz'),'wt',newline='') as f:
        w=csv.writer(f);w.writerow(fields)
        for i in np.flatnonzero(bad):w.writerow([d[a][i] for a in fields])
    if save_perzero:
        np.savez_compressed(OUT/(name+'_final_metrics.npz'),first_k=1400737,error=d['error'][tail],d=d['d'][tail],R=d['R'][tail],left_gap=d['left_gap'][tail],right_gap=d['right_gap'][tail],directional_R=d['directional_R'][tail],structural=d['structural'][tail])
    return d
complete=[]
for tier in [512,2048,8192]:
    if not all((OUT/f'{m}_X{tier}_final_constructor.json').exists() for m in ['Gonek','LeClair']):continue
    complete.append(tier);pr={512:97,2048:309,8192:1028}[tier]
    for method in ['Gonek','LeClair']:
        name=f'{method}_X{tier}';z=np.load(OUT/(name+'_final_with_halo.npz'));k=z['k'];x=z['model']
        constructor=json.loads((OUT/(name+'_final_constructor.json')).read_text())
        branch_note=('; ambiguous level selected by original prime-by-prime constructor, direct Newton disagrees'
                     if constructor.get('explicit_phase_index_selection_gate_passed') else '; unique ascending level crossing on both meshes')
        export(k,x,name,tier,pr,'fixed phase indices k; numerical regular family t>=6.3; not ordinal enumeration of every model root'+branch_note)
        y=pav.isotonic_project(x,tau[k-1],.1)
        i512=np.searchsorted(k,1400737-512);y512=pav.isotonic_project(x[i512:],tau[k[i512:]-1],.1)
        main=k>=1400737;agree=float(np.max(np.abs(y[main]-y512[k[i512:]>=1400737])))
        checks.append(dict(method=name,alpha=.1,halo1024_vs512_maxdiff=agree,max_postprocessing_change=float(np.max(np.abs(y-x))),
                           scope='regional PAV on final region plus halo, not global2million PAV'))
        export(k,y,name+'_regional_PAV_a010',tier,pr,'optional regional PAV alpha0.1 with halo1024; check halo512; distinct from original method',False)
    # Same exact k and synthetic neighbours for all arithmetic variants.
    for name in [f'Casanya_constant_X{tier}',f'Casanya_constant_X{tier}_PAV_a010']:
        x=np.memmap(baseline_meta[name]['path'],dtype='<f8',mode='r')[k-1]
        export(k,x,name,tier,pr,baseline_meta[name]['provenance'],False)
    if tier==512:
        for name,path,prov in [('c667_original',DATA/'zCasanya.bin','frozen historical validation-selected c667'),('c667_PAV_a010',OUT/'c667_PAV_a010.bin','full-array PAV of frozen c667, fixed alpha.10'),('zCasanya0_existing',DATA/'zCasanya0.bin','compatible with constant X512 alpha.20; source script selects hyperparameters with validation truth; bytes differ by rounding')]:
            export(k,np.memmap(path,dtype='<f8',mode='r')[k-1],name,tier,97,prov,False)
for name,data in [('full_localgap_summary.csv',rows),('full_localgap_by_height.csv',windows)]:
    if data:
        fields=list(dict.fromkeys(k for r in data for k in r))
        with (OUT/name).open('w',newline='') as f:
            w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(data)
(OUT/'optional_PAV_halo_checks.json').write_text(json.dumps(checks,indent=2))
(OUT/'final_evaluation_status.json').write_text(json.dumps(dict(complete_tiers=complete,all_required_tiers_complete=len(complete)==3,
  regular_index_scope='numerical regular-family indexing t>=6.3, two meshes; near-axis exceptions retained, no interval proof',
  criterion='primary: -right_gap/2 < error < left_gap/2; outer endpoint cells unbounded; legacy symmetric minimum retained'),indent=2))
for r in rows:
    if r['region']=='final600316':print(r['method'],r['rms'],r['all_failure_count'],r['max_R'],r['max_R_k'],flush=True)
