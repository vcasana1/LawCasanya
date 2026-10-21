#!/usr/bin/env python3
"""Independent evaluator. Only this program reads zeross.bin and frozen c667."""
import argparse, csv, hashlib, json, os, platform, resource, sys, time
from pathlib import Path
import numpy as np
import scipy
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE=Path(__file__).resolve().parent;OUT=HERE/'results'
DATA=Path('/Users/vcasana/Documents/·.· MATLAB/·.· bin_unicos')

def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(8*1024**2),b''):h.update(b)
    return h.hexdigest()

def dump(name,value):
    p=OUT/name;t=p.with_suffix(p.suffix+'.tmp');t.write_text(json.dumps(value,indent=2,allow_nan=False));os.replace(t,p)

def csvout(name,rows):
    if not rows:return
    fields=list(dict.fromkeys(k for row in rows for k in row))
    with (OUT/name).open('w',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=fields);wr.writeheader();wr.writerows(rows)

def region(k):return np.where(k<=800420,'training',np.where(k<=1400736,'validation','test'))

def metrics(method,k,x,g,tau,scope,reg,meta=None,mult=None):
    meta=meta or {};good=np.isfinite(x);e=x[good]-g[good];ab=np.abs(e)
    orig=np.abs(tau[good]-g[good]);adj=(np.diff(k)==1)&good[:-1]&good[1:]
    gaps=np.diff(x)[adj]
    row=dict(method=method,scope=scope,region=reg,n_requested=len(k),n_covered=int(good.sum()),
             coverage=float(good.mean()),missing_roots=int((~good).sum()),
             consecutive_pairs=int(adj.sum()),nonpositive_gaps=int(np.sum(gaps<=0)),
             rms=float(np.sqrt(np.mean(e*e))) if len(e) else None,
             mae=float(ab.mean()) if len(e) else None,median_abs=float(np.median(ab)) if len(e) else None,
             p95_abs=float(np.quantile(ab,.95)) if len(e) else None,p99_abs=float(np.quantile(ab,.99)) if len(e) else None,
             max_abs=float(ab.max()) if len(e) else None,
             rms_spacings=float(np.sqrt(np.mean((e*np.log(g[good]/(2*np.pi))/(2*np.pi))**2))) if len(e) else None,
             percent_improved=float(100*np.mean(ab<orig)) if len(e) else None,
             percent_worsened=float(100*np.mean(ab>orig)) if len(e) else None,
             model_ordinal_index_errors='unmeasured_global_enumeration_pending' if method.startswith(('M1','M2')) else 'not_applicable_assigned_clock_outputs',
             input_index_preserved=True,model_root_ordinal_validated=False if method.startswith(('M1','M2','M4')) else 'not_applicable_clock_outputs',
             comparison_status='complete_index_assigned' if good.all() else 'NO_COMPARABLE_partial_coverage')
    if method.startswith(('M1','M2')):
        row['comparison_status']='NO_COMPARABLE_global_root_ordinal_unverified'
    if method.startswith('M4'):
        row['comparison_status']='complete_algorithm_outputs_sampled_continuation' if good.all() else 'NO_COMPARABLE_partial_coverage'
    if mult is not None:row['sampled_multi_root_labels']=int(np.sum(mult>1))
    return row

def main():
    global OUT
    ap=argparse.ArgumentParser();ap.add_argument('--output',default=str(OUT));a=ap.parse_args();OUT=Path(a.output)
    start=time.perf_counter();audits=[]
    arrays={}
    for name in ['zLamb.bin','zeross.bin','zCasanya.bin']:
        p=DATA/name;assert p.stat().st_size==16008416
        a=np.fromfile(p,dtype='<f8');assert len(a)==2001052 and np.isfinite(a).all()
        arrays[name]=a
        audits.append(dict(name=name,path=str(p),dtype='<f8',bytes=p.stat().st_size,records=len(a),
                           first=a[:5].tolist(),last=a[-5:].tolist(),sha256=sha(p),
                           nonpositive_gaps=int(np.sum(np.diff(a)<=0))))
    p=DATA/'primoss.bin';prefix=np.fromfile(p,dtype='<u8',count=148934)
    previous=-1;count=0;mono=True
    with p.open('rb') as f:
        while True:
            a=np.fromfile(f,dtype='<u8',count=1000000)
            if not len(a):break
            mono&=int(a[0])>previous and bool(np.all(a[1:]>a[:-1]));previous=int(a[-1]);count+=len(a)
    audits.append(dict(name=p.name,path=str(p),dtype='<u8',bytes=p.stat().st_size,records=count,
                       sha256=sha(p),first=prefix[:8].tolist(),last_value=previous,
                       all_records_strictly_increasing=mono,verified_prime_prefix_records=148933,
                       verified_prefix_max=1999993,next_record=int(prefix[-1]),
                       whole_file_primality_checked=False))
    for pat in ['122_*','211_*','104_*','105_*','107_*']:
        p=next(Path('/Users/vcasana/Documents/LIBRARY TOTAL').glob(pat))
        audits.append(dict(name=p.name,path=str(p),bytes=p.stat().st_size,sha256=sha(p)))
    for p in (HERE/'sources').glob('*'):
        audits.append(dict(name=p.name,path=str(p),bytes=p.stat().st_size,sha256=sha(p)))
    dump('inventory.json',audits)
    tau=arrays['zLamb.bin'];g=arrays['zeross.bin'];cas=arrays['zCasanya.bin'];kall=np.arange(1,len(g)+1)
    rebuild=np.fromfile(OUT/'c667_reconstructed.bin',dtype='<f8')
    delta=np.max(np.abs(rebuild-cas))
    dump('c667_reproduction.json',dict(frozen_sha256=sha(DATA/'zCasanya.bin'),rebuild_sha256=sha(OUT/'c667_reconstructed.bin'),
                                     byte_identical=sha(DATA/'zCasanya.bin')==sha(OUT/'c667_reconstructed.bin'),max_abs_difference=float(delta)))
    assert delta<1e-8
    meta=json.loads((OUT/'constructor_metadata.json').read_text());rows=[];windows=[];failures=[];cost=[]
    if (OUT/'solver_metadata.json').exists():meta.update(json.loads((OUT/'solver_metadata.json').read_text()))
    full={'M0_Lambert':tau,'M3_c667':cas}
    for name,x in full.items():
        for reg,at in [('all',np.ones(len(g),bool))]+[(r,region(kall)==r) for r in ['training','validation','test']]:
            rows.append(metrics(name,kall[at],x[at],g[at],tau[at],'full',reg))
        for lo in range(0,len(g),50000):
            hi=min(lo+50000,len(g));row=metrics(name,kall[lo:hi],x[lo:hi],g[lo:hi],tau[lo:hi],'full_window','all')
            row|=dict(first_k=lo+1,last_k=hi);windows.append(row)
        for i in np.flatnonzero(np.diff(x)<=0):
            failures.append(dict(method=name,k=int(i+1),next_k=int(i+2),type='nonpositive_gap',gap=float(x[i+1]-x[i])))
    assert abs(rows[0]['rms']-.1880662998)<1e-9
    assert abs(rows[4]['rms']-.0439885472)<1e-9
    assert rows[4]['nonpositive_gaps']==962
    inputs=np.load(OUT/'pilot_inputs.npz');k=inputs['k'];pt=inputs['tau'];pg=g[k-1]
    archive=np.load(OUT/'pilot_candidates.npz');candidates={n:archive[n] for n in archive.files}
    if (OUT/'solver_candidates.npz').exists():
        extra=np.load(OUT/'solver_candidates.npz');candidates.update({n:extra[n] for n in extra.files})
    methods=[n for n in candidates if not n.endswith(('_multiplicity','_cut','_Xmon'))]
    for name in methods:
        x=candidates[name];mult=candidates[name+'_multiplicity'] if name+'_multiplicity' in candidates else None
        if name.startswith(('M1','M2')):failures.append(dict(method=name,type='global_model_root_ordinal_not_validated',count='unknown'))
        for reg,at in [('all',np.ones(len(k),bool))]+[(r,region(k)==r) for r in ['training','validation','test']]:
            row=metrics(name,k[at],x[at],pg[at],pt[at],'pilot1000',reg,meta.get(name),mult[at] if mult is not None else None)
            rows.append(row)
            windows.append(row|dict(first_k=int(k[at][0]),last_k=int(k[at][-1])))
        for i in np.flatnonzero(~np.isfinite(x)):
            failures.append(dict(method=name,k=int(k[i]),type='missing_or_nonconverged_root'))
        for i in np.flatnonzero((np.diff(k)==1)&(np.diff(x)<=0)):
            failures.append(dict(method=name,k=int(k[i]),next_k=int(k[i+1]),type='nonpositive_gap',gap=float(x[i+1]-x[i])))
        if mult is not None:
            for i in np.flatnonzero(mult!=1):failures.append(dict(method=name,k=int(k[i]),type='sampled_target_level_root_count',count=int(mult[i])))
        if name in meta:
            m=meta[name].copy()
            if name=='M3_c667':m['memory_peak_process_bytes']=json.loads((OUT/'constructor_complete.json').read_text())['maxrss_bytes']
            else:m['memory_peak_process_bytes']='not_isolated_by_method; constructor process peak in constructor_complete.json'
            m['shared_StageA_seconds']=meta['M4_v17_StageA']['seconds'] if name in ['M4_v17_R1','M4_v17_R2'] else 0
            m['seconds_including_shared_stage']=m['seconds']+m['shared_StageA_seconds']
            m['n_cost']=2001052 if name=='M3_c667' else 1000
            m['estimate_full_seconds']=m['seconds_including_shared_stage']*2001052/m['n_cost']
            m['estimate_note']='linear pilot extrapolation; NOT a measured full runtime; excludes enumeration and evaluation'
            cost.append(dict(method=name,**m))
    for f in json.loads((OUT/'constructor_failures.json').read_text()):failures.append(f)
    budgetrows=[]
    for row in rows:
        if row['scope']=='pilot1000':
            m=meta.get(row['method'],{})
            budgetrows.append({**row,**{q:m.get(q) for q in ['prime_count','max_prime','formal_X','support','power_terms']}})
    csvout('benchmark_resumen.csv',rows);csvout('benchmark_por_altura.csv',windows)
    csvout('benchmark_presupuesto.csv',budgetrows);csvout('benchmark_coste.csv',cost);csvout('benchmark_fallos.csv',failures)
    # Targets report attained metrics without claiming an unvalidated indexed win.
    targets=[]
    for target in [.10,.075,.050,.044,.040]:
        for method in ['M1','M2','M3','M4']:
            rr=[r for r in rows if r['scope']=='pilot1000' and r['region']=='test' and r['method'].startswith(method)]
            hit=[r for r in rr if r['coverage']==1 and r['rms']<=target]
            targets.append(dict(method=method,target=target,scope='pilot_test300',attained_in_pilot=bool(hit),
                                configurations=';'.join(r['method'] for r in hit),
                                indexed_comparable=method=='M3',full_precision_target_demonstrated=False))
        r=rows[4]
        targets.append(dict(method='M3_c667',target=target,scope='full_all2001052',attained_in_pilot=False,
                            configurations='M3_c667' if r['rms']<=target else '',indexed_comparable=True,
                            full_precision_target_demonstrated=r['rms']<=target))
    csvout('precision_targets.csv',targets)
    plt.rcParams.update({'font.size':9})
    pilot=[r for r in rows if r['scope']=='pilot1000' and r['region']=='test']
    fig,axs=plt.subplots(1,2,figsize=(11,4))
    for prefix,label in [('M1_LeClair','LeClair: primo a primo'),('M1_direct','Misma ecuación LeClair: solver directo'),('M2','Gonek: nivel, ordinal pendiente')]:
        rr=[r for r in pilot if r['method'].startswith(prefix)]
        pp=[meta[r['method']]['prime_count'] for r in rr];rms=[r['rms'] for r in rr]
        axs[0].plot(pp,rms,'o-',label=label)
        axs[1].plot([meta[r['method']]['seconds'] for r in rr],rms,'o-',label=label)
    for ax in axs:
        ax.axhline(next(r['rms'] for r in pilot if r['method']=='M3_c667'),color='k',ls='--',label='c667 congelada (97 primos max)')
        ax.set_ylabel('RMS altura (test piloto; ver cobertura)');ax.legend(fontsize=7);ax.grid(alpha=.3)
    axs[0].set_xscale('log');axs[0].set_xlabel('primos distintos');axs[1].set_xlabel('segundos de construcción, piloto 1000')
    fig.suptitle('Test del piloto: 300 índices; enumeración ordinal global de M1/M2 pendiente',fontsize=10)
    fig.tight_layout();fig.savefig(OUT/'rms_primes_time.png',dpi=150)
    fig,axs=plt.subplots(1,3,figsize=(13,4))
    for name,x in full.items():
        w=[r for r in windows if r['method']==name and r['scope']=='full_window']
        axs[0].plot([r['last_k'] for r in w],[r['rms'] for r in w],label=name)
        axs[1].hist(x-g,bins=180,range=(-.7,.7),histtype='step',density=True,label=name)
    where=np.flatnonzero(np.diff(cas)<=0)
    axs[2].hist(where+1,bins=40);axs[2].set_title('962 saltos no positivos de c667')
    axs[0].set_xlabel('k');axs[0].set_ylabel('RMS altura');axs[1].set_xlabel('error altura');axs[2].set_xlabel('k')
    for ax in axs[:2]:ax.legend();ax.grid(alpha=.3)
    fig.tight_layout();fig.savefig(OUT/'height_distribution_failures.png',dpi=150)
    dump('evaluation_complete.json',dict(complete=True,seconds=time.perf_counter()-start,
                                        python=sys.version,numpy=np.__version__,scipy=scipy.__version__,platform=platform.platform(),
                                        maxrss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
    print('FULL REFERENCE CHECKS')
    for r in rows[:8]:print(r['method'],r['region'],r['rms'],r['nonpositive_gaps'])
    print('PILOT TEST')
    for r in pilot:print(r['method'],r['rms'],r['coverage'],r['comparison_status'])

if __name__=='__main__':main()
