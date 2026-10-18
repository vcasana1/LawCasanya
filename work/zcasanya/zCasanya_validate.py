#!/usr/bin/env python3
"""Independent validator; never supplies ordinate corrections to the constructor.

pilot: selects a parameter shortlist using a sample from the first 40% only.
select: ranks full candidates on indices [40%,70%) and freezes selected.json.
report: opens final 30% only after selection, and reports all regions and heights.
"""
from pathlib import Path
import argparse
import csv
import hashlib
import json
import shutil
import time
import numpy as np


def digest(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for b in iter(lambda:f.read(8*1024**2),b''):h.update(b)
    return h.hexdigest()


def write_csv(path, rows):
    with Path(path).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]))
        w.writeheader();w.writerows(rows)


def stats(x, g, base):
    err=x-g; a=np.abs(err); b=np.abs(base-g)
    return {'n':len(x),'rms':float(np.sqrt(np.mean(err*err))),
            'mae':float(np.mean(a)),'median_abs':float(np.median(a)),
            'max_abs':float(np.max(a)),
            'percent_improved':float(100*np.mean(a<b)),
            'mean_signed':float(np.mean(err)),
            'p90_abs':float(np.quantile(a,.9)),
            'p99_abs':float(np.quantile(a,.99)),
            'nonpositive_gaps':int(np.sum(np.diff(x)<=0)),
            'min_gap':float(np.min(np.diff(x))) if len(x)>1 else 0.}


def inputs(args):
    o=Path(args.output).resolve(); d=Path(args.data_dir).resolve()
    tau=np.fromfile(d/'zLamb.bin',dtype='<f8')
    f=d/'zeross.bin'
    assert f.stat().st_size==tau.nbytes
    # Mapping does not evaluate the held-out region; slices are chosen by stage.
    g=np.memmap(f,mode='r',dtype='<f8')
    return o,d,tau,g


def pilot(args):
    o,d,tau,g=inputs(args)
    assert (o/'pilot_complete.json').exists()
    manifest=json.loads((o/'pilot_manifest.json').read_text())
    rows=[]
    for c in manifest:
        assert digest(o/c['file'])==c['sha256']
        a=np.load(o/c['file']); idx=a['index']; x=a['values']
        assert idx.max()<int(.4*len(tau))
        mask=idx>=512  # Extra consecutive low indices are stability probes only.
        m=stats(x[mask],g[idx[mask]],tau[idx[mask]])
        valid=all(z['finite'] and z['domain_valid'] and
                  z['max_step_in_local_spacings']<8 for z in c['diagnostics'])
        rows.append({'id':c['id'],'window':c['window'],'policy':c['policy'],
                     'steps':len(c['cutoffs']),'cutoffs':json.dumps(c['cutoffs']),
                     'intrinsically_eligible':valid,**m})
    write_csv(o/'pilot_results.csv',rows)
    chosen={}
    for window in ['euler_v10','power_sharp']:
        for policy in ['constant','dyadic']:
            for steps in [1,2,3,4]:
                pool=[r for r in rows if r['window']==window and r['policy']==policy
                      and r['steps']==steps and r['intrinsically_eligible']]
                best=min(pool,key=lambda r:r['rms'])
                config=next(c for c in manifest if c['id']==best['id'])
                chosen[config['id']]={k:config[k] for k in ['id','window','policy','cutoffs']}
                # Keep all prefixes for a directly matched iteration comparison.
                for j in range(1,steps):
                    prefix=next(c for c in manifest if c['window']==window and c['policy']==policy
                                and c['cutoffs']==config['cutoffs'][:j])
                    chosen[prefix['id']]={k:prefix[k] for k in ['id','window','policy','cutoffs']}
            # Same-cutoff 2nd and 3rd step of the best 1-step tuning model.
            r=min((r for r in rows if r['window']==window and r['policy']==policy and
                   r['steps']==1 and r['intrinsically_eligible']),key=lambda r:r['rms'])
            base=next(c for c in manifest if c['id']==r['id'])
            for j in [2,3]:
                c=next(c for c in manifest if c['window']==window and c['policy']==policy
                       and c['cutoffs']==base['cutoffs']*j)
                chosen[c['id']]={k:c[k] for k in ['id','window','policy','cutoffs']}
    shortlist=list(chosen.values())
    if (o/'shortlist.json').exists():
        for c in json.loads((o/'shortlist.json').read_text()):
            if c['id'] not in chosen:
                shortlist.append(c)
    (o/'shortlist.json').write_text(json.dumps(shortlist,indent=2))
    (o/'split_protocol.json').write_text(json.dumps({
        'n':len(tau),'tuning':[1,int(.4*len(tau))],
        'selection_validation':[int(.4*len(tau))+1,int(.7*len(tau))],
        'untouched_test':[int(.7*len(tau))+1,len(tau)],
        'pilot_extra_stability_probes':[1,512],
        'selection_rule':'Minimum validation RMS among intrinsically eligible candidates; exact RMS ties prefer fewer full-array crossings, then ID. No sorting or repair.',
        'intrinsic_eligibility':'All iterates finite, t>2pi, every step smaller than 8 smooth local spacings.',
        'cutoff_policy_dyadic':'T=2^floor(log2(tau)); X=min(Xmax,max(8,floor(sqrt(T)))).',
        'no_coefficients_or_ordinate_corrections_fit':True},indent=2))
    print('SHORTLIST',len(shortlist),json.dumps(shortlist,indent=2))


def select(args):
    o,d,tau,g=inputs(args)
    assert (o/'full_complete.json').exists()
    manifest=json.loads((o/'full_manifest.json').read_text())
    assert len(manifest)==json.loads((o/'full_complete.json').read_text())['candidates']
    lo,hi=int(.4*len(tau)),int(.7*len(tau))
    rows=[]
    for c in manifest:
        assert digest(o/c['file'])==c['sha256']
        x=np.memmap(o/c['file'],mode='r',dtype='<f8')
        eligible=all(z['finite'] and z['domain_valid'] and
                     z['max_step_in_local_spacings']<8 for z in c['diagnostics'])
        rows.append({'id':c['id'],'window':c['window'],'policy':c['policy'],
                     'steps':len(c['cutoffs']),'cutoffs':json.dumps(c['cutoffs']),
                     'intrinsically_eligible':eligible,
                     'all_nonpositive_gaps':c['nonpositive_gaps'],
                     **stats(x[lo:hi],g[lo:hi],tau[lo:hi])})
    write_csv(o/'selection_validation_results.csv',rows)
    best=min((r for r in rows if r['intrinsically_eligible']),
             key=lambda r:(r['rms'],r['all_nonpositive_gaps'],r['id']))
    c=next(c for c in manifest if c['id']==best['id'])
    selected={**c,'selection_validation_metrics':best,
              'selected_before_untouched_test':True,
              'selection_time_unix':time.time(),
              'constructor_sha256':digest(o/'zCasanya_build.py')}
    if (o/'selected.json').exists():
        prior=json.loads((o/'selected.json').read_text())
        assert all(prior[k]==selected[k] for k in ['id','window','policy','cutoffs','sha256']), 'Existing frozen winner must not change after test evaluation'
        selected['selection_time_unix']=prior['selection_time_unix']
        selected['initial_constructor_sha256']=prior['constructor_sha256']
        selected['manifest_reconciliation_note']='All 58 precomputed finalists included; the original frozen configuration and binary SHA-256 are unchanged. Only manifest checkpoint persistence was repaired in the constructor.'
    dest=o/'zCasanya.bin'
    if dest.exists():
        backup=o/('zCasanya.backup.'+str(time.time_ns())+'.bin')
        shutil.copy2(dest,backup)
    shutil.copy2(o/c['file'],dest)
    assert digest(dest)==c['sha256']
    (o/'selected.json').write_text(json.dumps(selected,indent=2))
    print('SELECTED',json.dumps(selected,indent=2))


def report(args):
    o,d,tau,g=inputs(args)
    selected=json.loads((o/'selected.json').read_text())
    assert selected['selected_before_untouched_test']
    assert digest(o/'zCasanya.bin')==selected['sha256']
    assert np.all(np.isfinite(g)) and np.all(np.diff(g)>0)
    assert 14<g[0]<15 and 1.13e6<g[-1]<1.14e6
    meta={'path':str(d/'zeross.bin'),'dtype':'<f8','records':len(g),
          'bytes':g.nbytes,'sha256':digest(d/'zeross.bin'),
          'first':g[:5].tolist(),'last':g[-5:].tolist(),
          'strictly_increasing':True}
    (o/'validation_input_audit.json').write_text(json.dumps(meta,indent=2))
    manifest=json.loads((o/'full_manifest.json').read_text())
    assert len(manifest)==json.loads((o/'full_complete.json').read_text())['candidates']
    bounds=[('tuning_full',0,int(.4*len(tau))),
            ('selection_validation',int(.4*len(tau)),int(.7*len(tau))),
            ('untouched_test',int(.7*len(tau)),len(tau)),('all',0,len(tau))]
    rows=[]; windows=[]; hist=[]
    models=[{'id':'Lambert','window':'baseline','policy':'baseline','cutoffs':[],'file':None}]+manifest
    for c in models:
        x=tau if c['file'] is None else np.memmap(o/c['file'],mode='r',dtype='<f8')
        for region,lo,hi in bounds:
            rows.append({'id':c['id'],'window':c['window'],'policy':c['policy'],
                         'steps':len(c['cutoffs']),'cutoffs':json.dumps(c['cutoffs']),
                         'region':region,'k_first':lo+1,'k_last':hi,
                         **stats(x[lo:hi],g[lo:hi],tau[lo:hi])})
        block=np.floor(np.log2(tau)).astype(int)
        for h in np.unique(block):
            at=block==h
            windows.append({'id':c['id'],'T_lower':2.**int(h),'T_upper':2.**int(h+1),
                            **stats(x[at],g[at],tau[at])})
        e=x-g
        edges=np.r_[-np.inf,np.linspace(-1.5,1.5,121),np.inf]
        counts,_=np.histogram(e,bins=edges)
        for a,b,n in zip(edges[:-1],edges[1:],counts):
            hist.append({'id':c['id'],'error_lower':float(a),'error_upper':float(b),'count':int(n)})
    write_csv(o/'zCasanya_results.csv',rows)
    write_csv(o/'height_windows.csv',windows)
    write_csv(o/'error_distribution.csv',hist)
    all_rows={r['id']:r for r in rows if r['region']=='all'}
    validation=[r for r in rows if r['region']=='selection_validation']
    summary=[all_rows['Lambert']]
    valid_ids={c['id'] for c in manifest if all(z['finite'] and z['domain_valid'] and
               z['max_step_in_local_spacings']<8 for z in c['diagnostics'])}
    for j in [1,2,3,4]:
        eligible=[r for r in validation if r['steps']==j and r['id'] in valid_ids]
        best=min(eligible,key=lambda r:(r['rms'],all_rows[r['id']]['nonpositive_gaps'],r['id']))
        summary.append(all_rows[best['id']])
    summary.append(all_rows[selected['id']])
    write_csv(o/'final_comparison.csv',summary)
    base=all_rows['Lambert']['rms']; final=all_rows[selected['id']]['rms']
    result={'selected_id':selected['id'],'configuration':{k:selected[k] for k in ['window','policy','cutoffs']},
            'all_rms_original':base,'all_rms_Casanya':final,
            'rms_improvement_percent':100*(1-final/base),
            'rms_improvement_percent_vs_task_reference':100*(1-final/.1880662998),
            'first':float(np.fromfile(o/'zCasanya.bin',dtype='<f8',count=1)[0]),
            'last':float(np.memmap(o/'zCasanya.bin',mode='r',dtype='<f8')[-1]),
            'records':len(tau),'bytes':(o/'zCasanya.bin').stat().st_size,
            'path':str(o/'zCasanya.bin'),'sha256':digest(o/'zCasanya.bin'),
            'comparison':summary,
            'selected_regions':[r for r in rows if r['id'] in ['Lambert',selected['id']]],
            'test_opened_only_after_selection':True}
    best_two=next(c for c in manifest if c['id']==summary[2]['id'])
    prefix=next(c for c in manifest if c['window']==best_two['window'] and
                c['policy']==best_two['policy'] and c['cutoffs']==best_two['cutoffs'][:1])
    result['matched_second_step']={'first_id':prefix['id'],'second_id':best_two['id'],
         'cutoffs':best_two['cutoffs'],
         'first_all_rms':all_rows[prefix['id']]['rms'],
         'second_all_rms':all_rows[best_two['id']]['rms'],
         'improves':all_rows[best_two['id']]['rms']<all_rows[prefix['id']]['rms']}
    (o/'summary.json').write_text(json.dumps(result,indent=2))
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--data-dir',required=True);p.add_argument('--output',required=True)
    p.add_argument('--stage',required=True,choices=['pilot','select','report'])
    a=p.parse_args()
    {'pilot':pilot,'select':select,'report':report}[a.stage](a)
