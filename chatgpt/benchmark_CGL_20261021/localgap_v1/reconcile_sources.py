#!/usr/bin/env python3
"""Arithmetic reconstruction of specific documented clock/rounding variants.
No fitting or reference zeros: compare exact bytes to issue #1 attachment hashes.
"""
import hashlib,importlib.util,json,sys,time
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent;OUT=HERE/'outputs';OLD=HERE.parent
sys.path.insert(0,str(OLD));import constructors as C
spec=importlib.util.spec_from_file_location('pavsource',HERE/'sources/casanya_monotone_projection.py');pav=importlib.util.module_from_spec(spec);spec.loader.exec_module(pav)
def guard(ev,args):
    if ev=='open' and args and isinstance(args[0],(str,bytes)) and 'zeross' in str(args[0]).lower():raise PermissionError('Truth forbidden')
sys.addaudithook(guard)
DATA=Path('/Users/vcasana/Documents/·.· MATLAB/·.· bin_unicos')
raw=np.fromfile(DATA/'zCasanya.bin',dtype='<f8');pr=C.sieve(512);rows=[]
def sha(a):return hashlib.sha256(a.astype('<f8').tobytes()).hexdigest()
for clockpath in [DATA/'zLamb.bin',Path('/Users/vcasana/Documents/ChatGPT/Möbius/LawCasanya/data/zLamb.bin')]:
    tau=np.fromfile(clockpath,dtype='<f8');k=np.arange(1,len(tau)+1)
    for mode in ['stable_frozen','v15_direct_clock_sorted_powers']:
        st=time.perf_counter()
        if mode=='stable_frozen':x,_=C.c667(tau,k,pr)
        else:
            x=tau.copy()
            for ceiling in [8,8,512]:
                cut=np.minimum(ceiling,np.maximum(8,np.floor(np.sqrt(np.exp2(np.floor(np.log2(tau)))))))
                s=np.zeros_like(x)
                n,p,m=C.powers(pr,ceiling)
                for nn,pp,mm in zip(n,p,m):
                    mask=cut>=nn;s-=np.where(mask,np.sin((mm*np.log(float(pp)))*x)/(np.pi*mm*np.sqrt(float(nn))),0)
                x-=(C.N0(x)-(k-.5)+s)/C.L(x)
        h=sha(x);y=pav.isotonic_project(x,tau,.1);hy=sha(y)
        row=dict(clock_path=str(clockpath),clock_sha256=hashlib.sha256(clockpath.read_bytes()).hexdigest(),arithmetic=mode,
                 c667_sha256=h,PAV_sha256=hy,max_difference_from_original=float(np.max(np.abs(x-raw))),seconds=time.perf_counter()-st,
                 matches_shared_c667=h=='dc8d4be907366056825da86ed4ebe2371d5c071c2dbf2bc64fc36501fe38e607',
                 matches_shared_PAV=hy=='2857d9e8c85c4197ebeab052df16ea8defb82650ce3078ba37fb918dfbfb60ef')
        if row['matches_shared_c667'] or row['matches_shared_PAV']:
            path=OUT/(f'reconciled_{h[:12]}.bin');x.astype('<f8').tofile(path)
            y.astype('<f8').tofile(OUT/(f'reconciled_PAV_{hy[:12]}.bin'))
        rows.append(row);print(row,flush=True)
        (OUT/'hash_reconciliation.json').write_text(json.dumps(rows,indent=2))
    del tau,x,y
