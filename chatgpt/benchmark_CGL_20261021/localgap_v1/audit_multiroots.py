#!/usr/bin/env python3
"""Localize enumerated multi-root levels, without opening true ordinates."""
import json
import numpy as np
import mpmath as mp
from scipy.optimize import brentq
from pilot_models import Model,C,tauall,N,OUT,pr

def main():
    rows=[]
    for tier in [512,2048,8192]:
        p=OUT/'global_index'/f'LeClair_X{tier}_enumeration.json'
        if not p.exists():continue
        state=np.load(p.with_name(f'LeClair_X{tier}_step0.04_checkpoint.npz'))
        labels=np.flatnonzero(state['counts'][1:N+1]>1)+1
        if not len(labels):continue
        model=Model('LeClair',tier)
        # Match the existing published prime-by-prime construction, no truth.
        ks=np.unique(np.r_[labels-1,labels,labels+1]);ks=ks[(ks>=1)&(ks<=N)]
        continuation=C.lc_continuation(tauall[ks-1],ks,pr,[tier])[tier]
        for k in labels:
            center=float(tauall[k-1]);space=1/C.L(center)
            grid=np.linspace(center-2*space,center+2*space,8193)
            vals=model.f(grid,np.full(len(grid),k),False)[0]
            ii=np.flatnonzero(vals[:-1]*vals[1:]<0)
            roots=[brentq(lambda t:float(model.f(np.array([t]),np.array([k]),False)[0][0]),grid[i],grid[i+1],xtol=1e-10) for i in ii]
            mp.mp.dps=55;pp=[mp.mpf(int(q)) for q in pr[pr<=tier]]
            def high(t):
                smooth=t/(2*mp.pi)*mp.log(t/(2*mp.pi))-t/(2*mp.pi)+mp.mpf(7)/8+1/(48*mp.pi*t)
                phase=-mp.fsum(mp.atan2(q**(-mp.mpf('.500001'))*mp.sin(t*mp.log(q)),1-q**(-mp.mpf('.500001'))*mp.cos(t*mp.log(q))) for q in pp)/mp.pi
                return smooth+phase-(int(k)-mp.mpf('.5'))
            exact=[mp.findroot(high,(mp.mpf(str(t))-.00001,mp.mpf(str(t))+.00001)) for t in roots]
            selected=float(continuation[0][np.searchsorted(ks,k)])
            direct=model.solve(np.array([center]),np.array([k]))[0][0]
            row=dict(tier=tier,k=int(k),enumerated_count=int(state['counts'][k]),roots_float=roots,
                     roots_55digits=[mp.nstr(t,48) for t in exact],max_float_highprec_difference=max(abs(t-float(u)) for t,u in zip(roots,exact)),
                     crossing_slopes=[float(model.f(np.array([t]),np.array([k]))[1][0]) for t in roots],
                     published_prime_by_prime_root=selected,direct_warm_root=float(direct),
                     continuation_root_number=1+int(np.argmin(np.abs(np.array(roots)-selected))) if np.isfinite(selected) else None,
                     continuation_issues=continuation[2],no_true_zero_access=True)
            rows.append(row);print(row,flush=True)
    (OUT/'multiroot_audit.json').write_text(json.dumps(rows,indent=2))
    for tier in sorted(set(r['tier'] for r in rows)):
        rr=[r for r in rows if r['tier']==tier]
        state=np.load(OUT/'global_index'/f'LeClair_X{tier}_step0.04_checkpoint.npz')
        coarse=np.load(OUT/'global_index'/f'LeClair_X{tier}_step0.08_checkpoint.npz')
        meshes_agree=bool(np.array_equal(state['counts'][1:N+1],coarse['counts'][1:N+1])
                          and np.array_equal(state['downs'][1:N+1],coarse['downs'][1:N+1]))
        checks=[]
        for r in rr:
            k=r['k'];x=r['published_prime_by_prime_root']
            checks.append(bool(np.isfinite(x) and r['continuation_issues']==[]
                               and len(r['roots_float'])==r['enumerated_count']
                               and abs(x-r['roots_float'][r['continuation_root_number']-1])<1e-7
                               and state['right'][k-1]<x<state['left'][k+1]))
        missing=int(np.sum(state['counts'][1:N+1]==0))
        gate=dict(method='LeClair',tier=tier,complete=True,
                  phase_index_selection_gate_passed=all(checks) and missing==0 and meshes_agree,
                  two_mesh_counts_agree=meshes_agree,
                  policy='unique regular root for unique levels; existing prime-by-prime constructor at ambiguous levels; no truth access',
                  no_all_root_ordinal_claim=True,interval_certified=False,
                  ambiguous_labels=[r['k'] for r in rr],
                  selected_roots={str(r['k']):r['published_prime_by_prime_root'] for r in rr},
                  selected_between_neighboring_label_brackets=checks,
                  missing_labels=missing)
        (OUT/'global_index'/f'LeClair_X{tier}_selection_gate.json').write_text(json.dumps(gate,indent=2))

if __name__=='__main__':main()
