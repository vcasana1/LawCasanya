#!/usr/bin/env python3
"""Recover only the missing predecessor of the existing final v17 arrays.
Check three overlap points before using the recovered synthetic neighbour.
Truth-free; use original six-level/ten-step/five-point v17 rule.
"""
import importlib.util,json,sys
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent;OUT=HERE/'outputs';sys.path.insert(0,str(HERE.parent));import constructors as C
def guard(ev,args):
    if ev=='open' and args and isinstance(args[0],(str,bytes)) and 'zeross' in str(args[0]).lower():raise PermissionError('Truth forbidden')
sys.addaudithook(guard)
DATA=Path('/Users/vcasana/Documents/·.· MATLAB/·.· bin_unicos');tauall=np.fromfile(DATA/'zLamb.bin',dtype='<f8')
k=np.arange(1400736,1400740);tau=tauall[k-1];P=C.Phase(C.sieve(200000),200000,'sharp')
xA,cut,valid=C.stage_a(tau,k,P);assert valid.all()
r1,c1,m1=C.v17_continuation(tau,k,P,xA,cut,'R1');r2,c2,m2=C.v17_continuation(tau,k,P,xA,cut,'R2')
old=np.load('/Users/vcasana/Documents/ChatGPT/Möbius/LawCasanya/work/v15_prep/outputs/task3_points.npy',mmap_mode='r')
values=np.vstack([xA,r1,r2]);diff=np.max(np.abs(values[:,1:]-old[:3,:3]),axis=1)
assert np.all(diff<1e-8)
np.savez(OUT/'v17_recovered_neighbor.npz',k=k,values=values)
(OUT/'v17_neighbor_check.json').write_text(json.dumps(dict(k=k.tolist(),max_overlap_differences=diff.tolist(),only_new_index=1400736,truth_used=False),indent=2))
print('v17 predecessor recovered; overlap differences',diff)
