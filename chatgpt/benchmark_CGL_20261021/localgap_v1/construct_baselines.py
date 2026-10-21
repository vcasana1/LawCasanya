#!/usr/bin/env python3
"""Truth-free fixed-parameter Casanya cutoffs and GLOBAL PAV. Originals immutable."""
import hashlib,importlib.util,json,os,sys,time
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent;OLD=HERE.parent;OUT=HERE/'outputs';OUT.mkdir(exist_ok=True)
sys.path.insert(0,str(OLD));import constructors as C
spec=importlib.util.spec_from_file_location('pav_source',HERE/'sources/casanya_monotone_projection.py')
PAV=importlib.util.module_from_spec(spec);spec.loader.exec_module(PAV)
DATA=Path('/Users/vcasana/Documents/·.· MATLAB/·.· bin_unicos')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def guard(event,args):
    if event=='open' and args and isinstance(args[0],(str,bytes)) and 'zeross' in str(args[0]).lower():raise PermissionError('Reference truth forbidden')
sys.addaudithook(guard)
tau=np.fromfile(DATA/'zLamb.bin',dtype='<f8');raw=np.fromfile(DATA/'zCasanya.bin',dtype='<f8');n=len(tau)
assert n==len(raw)==2001052
pr=C.sieve(32768);indices=np.arange(1,n+1);config=dict(alpha=.10,cutoffs=[512,2048,8192],
  policy='constant sharp prime-power [8,8,X], separately labelled from dyadic c667',
  index_selection='all indices in original order',true_zeros_used=False,
  source_c667_sha256=sha(DATA/'zCasanya.bin'),source_tau_sha256=sha(DATA/'zLamb.bin'))
(OUT/'baseline_config_frozen.json').write_text(json.dumps(config,indent=2))
meta={}
def save(name,a,seconds,kind,primes):
    path=OUT/(name+'.bin');assert not path.exists();a.astype('<f8').tofile(path)
    meta[name]=dict(path=str(path),sha256=sha(path),seconds=seconds,provenance=kind,prime_count=primes,
                    nonpositive_gaps=int(np.sum(np.diff(a)<=0)),min_gap=float(np.min(np.diff(a))))
    (OUT/'baseline_constructor_metadata.json').write_text(json.dumps(meta,indent=2))
    print(name,meta[name],flush=True)
st=time.perf_counter();mono=PAV.isotonic_project(raw,tau,.10);save('c667_PAV_a010',mono,time.perf_counter()-st,'fixed PAV of frozen validated c667; no extra primes',97)
np.savez_compressed(OUT/'c667_projection_change.npz',changed_k=np.flatnonzero(mono!=raw)+1,delta=(mono-raw)[mono!=raw])
del mono
# New raw arithmetic variants: pilot stability first, no truth-based selection.
def build(tau,k,X):
    x=tau.copy();base=C.N0(tau)-(k-.5)
    for cut in [8,8,X]:
        s=np.zeros_like(x)
        for p in pr[pr<=cut]:
            q,m=int(p),1
            while q<=cut:
                s-=np.sin((m*np.log(float(p)))*x)/(np.pi*m*np.sqrt(float(q)))
                q*=int(p);m+=1
        x-=(base+C.clock_diff(x,tau)+s)/C.L(x)
        if not np.all(np.isfinite(x)&(x>C.TP)):raise ValueError('Invalid domain, no clipping or true-zero repair')
    return x
for X in config['cutoffs']:
    st=time.perf_counter();pilot=build(tau[:1000],indices[:1000],X)
    print('arithmetic pilot stable',X,'seconds',time.perf_counter()-st,flush=True)
    st=time.perf_counter();x=build(tau,indices,X);elapsed=time.perf_counter()-st
    save(f'Casanya_constant_X{X}',x,elapsed,'fixed arithmetic constant cutoff; not selected with truth',int(np.sum(pr<=X)))
    st=time.perf_counter();y=PAV.isotonic_project(x,tau,.10)
    save(f'Casanya_constant_X{X}_PAV_a010',y,elapsed+time.perf_counter()-st,'same arithmetic + global PAV alpha0.10',int(np.sum(pr<=X)))
    del x,y
(OUT/'baseline_constructor_complete.json').write_text(json.dumps(dict(complete=True,truth_access_blocked=True,n=n),indent=2))
