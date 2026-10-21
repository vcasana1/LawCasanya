#!/usr/bin/env python3
"""Identify existing zCasanya0 by declared candidate grid, without gamma access.
Compatibility at 1e-8 is not byte identity or proof of historical execution.
"""
import hashlib,importlib.util,json,sys,time
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent;OUT=HERE/'outputs'
spec=importlib.util.spec_from_file_location('pav',HERE/'sources/casanya_monotone_projection.py');P=importlib.util.module_from_spec(spec);spec.loader.exec_module(P)
def guard(ev,args):
    if ev=='open' and args and isinstance(args[0],(str,bytes)) and 'zeross' in str(args[0]).lower():raise PermissionError('Truth forbidden')
sys.addaudithook(guard)
DATA=Path('/Users/vcasana/Documents/·.· MATLAB/·.· bin_unicos');tau=np.fromfile(DATA/'zLamb.bin',dtype='<f8');existing=np.fromfile(DATA/'zCasanya0.bin',dtype='<f8');rows=[]
for X in [512,2048,8192]:
    raw=np.fromfile(OUT/f'Casanya_constant_X{X}.bin',dtype='<f8')
    for alpha in [.01,.05,.10,.20]:
        y=P.isotonic_project(raw,tau,alpha);d=y-existing
        r=dict(X=X,alpha=alpha,max_difference=float(np.max(np.abs(d))),rms_difference=float(np.sqrt(np.mean(d*d))),
               byte_identical=bool(np.array_equal(y,existing)),compatible_within_1e8=bool(np.max(np.abs(d))<1e-8))
        rows.append(r);print(r,flush=True)
        (OUT/'zCasanya0_configuration_compatibility.json').write_text(json.dumps(dict(existing_sha256=hashlib.sha256((DATA/'zCasanya0.bin').read_bytes()).hexdigest(),truth_used=False,tests=rows),indent=2))
