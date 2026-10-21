#!/usr/bin/env python3
"""Truth-free local stability diagnostic of the original smooth denominator."""
import sys,json
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent;OLD=HERE.parent
sys.path.insert(0,str(OLD));import constructors as C
C.install_guard()
z=np.load(OLD/'localgap_v1/outputs/pilot_models.npz')
s=np.load(OLD/'localgap_v1/outputs/pilot_index_sets.npz');k=s['k'];pr=C.sieve(8192)
rows=[]
for X in [512,2048,8192]:
    x=z[f'Casanya_root_X{X}'];P=C.Phase(pr,X,'sharp');phase,der=P(x)
    factor=np.abs(der/C.L(x))
    for region in ['first1000','pilot_last300','high_consecutive_last300']:
        mask=np.isin(k,s[region]);rows.append(dict(cutoff=X,region=region,n=int(mask.sum()),
            smooth_denominator_local_factor_gt1=int(np.sum(factor[mask]>1)),
            max_factor=float(factor[mask].max()),
            min_full_phase_derivative_at_sampled_roots=float(np.min((C.L(x)+der)[mask]))))
result=dict(truth_access_forbidden=True,
    equation='F_X(t;k)=N0(t)+S_X(t)-(k-1/2)',
    original_iteration='G(t)=t-F_X(t;k)/N0_prime(t)',
    derivative_at_exact_root='G_prime(r)=-S_X_prime(r)/N0_prime(r)',
    qualification='evaluated at numerical pilot roots; local instability of a repeatedly fixed-cutoff iteration, not a proof that every finite three-step result is worse',
    rows=rows)
(HERE/'diagnosis.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
