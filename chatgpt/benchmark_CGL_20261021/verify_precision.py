#!/usr/bin/env python3
"""Independent mpmath check of formulas/derivatives/roots. No zeta evaluation."""
from pathlib import Path
import argparse,json
import mpmath as mp
import numpy as np
import constructors as C

HERE=Path(__file__).resolve().parent;OUT=HERE/'results'
mp.mp.dps=60

def main():
    global OUT
    ap=argparse.ArgumentParser();ap.add_argument('--output',default=str(OUT));a=ap.parse_args();OUT=Path(a.output)
    C.install_guard()
    pr=C.sieve(8192);checks=[]
    inp=np.load(OUT/'pilot_inputs.npz');k,tau=inp['k'],inp['tau']
    vals=np.load(OUT/'pilot_candidates.npz')
    for kind,support,X in [('euler',31,None),('euler',8191,None),('gonek',32,np.sqrt(32)),('gonek',8192,np.sqrt(8192)),('sharp',512,None)]:
        P=C.Phase(pr,support,kind,X)
        for t in tau[[0,400,700,999]]:
            mt=mp.mpf(float(t));s,ds=P(np.array([t]))
            if kind=='euler':
                # Sum of individual log factors; wrapping the whole product is forbidden.
                def f(u):return -mp.im(mp.fsum(mp.log(1-mp.power(int(p),-mp.mpf('.500001')-1j*u)) for p in P.p))/mp.pi
            else:
                def f(u):
                    terms=[]
                    for n,p,m in zip(P.n,P.p,P.m):
                        if kind=='gonek':
                            # formal X is the exact sqrt(support), not the rounded float.
                            wt=min(mp.mpf(1),2-mp.log(int(n))/(mp.log(support)/2))
                            wt=max(mp.mpf(0),wt)
                        else:wt=mp.mpf(1)
                        terms.append(-wt*mp.sin(int(m)*u*mp.log(int(p)))/(mp.pi*int(m)*mp.sqrt(int(n))))
                    return mp.fsum(terms)
            ss=f(mt);dd=mp.diff(f,mt)
            th=mp.im(mp.loggamma(mp.mpf('.25')+.5j*mt))-.5*mt*mp.log(mp.pi)
            checks.append(dict(kind=kind,support=support,t=float(t),phase_abs_error=float(abs(ss-s[0])),
                               derivative_abs_error=float(abs(dd-ds[0])),theta_abs_error=float(abs(th-C.theta(t)))))
    roots=[]
    for b in [7,31,127,511,2047,8191]:
        P=C.Phase(pr,b+1,'gonek',np.sqrt(b+1));x=vals[f'M2_Gonek_level_P{b}']
        for i in [0,400,700,999]:
            if not np.isfinite(x[i]):continue
            t=mp.mpf(float(x[i]));terms=[]
            for n,p,m in zip(P.n,P.p,P.m):
                w=max(mp.mpf(0),min(mp.mpf(1),2-mp.log(int(n))/(mp.log(b+1)/2)))
                terms.append(-w*mp.sin(int(m)*t*mp.log(int(p)))/(mp.pi*int(m)*mp.sqrt(int(n))))
            th=mp.im(mp.loggamma(mp.mpf('.25')+.5j*t))-.5*t*mp.log(mp.pi)
            res=1+th/mp.pi+mp.fsum(terms)-(int(k[i])-.5)
            roots.append(dict(method=f'Gonek_P{b}',k=int(k[i]),phase_residual_hp=float(abs(res))))
    # Stable clock difference versus independent arbitrary precision subtraction.
    cd=[]
    for t in tau[[0,400,700,999]]:
        y=float(t+.1);tt=mp.mpf(float(t));yy=mp.mpf(y)
        exact=(yy/(2*mp.pi)*(mp.log(yy/(2*mp.pi))-1)+mp.mpf('.875'))-(tt/(2*mp.pi)*(mp.log(tt/(2*mp.pi))-1)+mp.mpf('.875'))
        approx=C.clock_diff(np.array([y]),np.array([t]))[0]
        cd.append(float(abs(exact-approx)))
    assert max(r['phase_abs_error'] for r in checks)<1e-8
    assert max(r['derivative_abs_error'] for r in checks)<1e-7
    assert max(cd)<1e-14
    # k=1 correctly handles the negative, real principal Lambert-W argument.
    for kk in [1,2,3,1000,2001052]:
        from scipy.special import lambertw
        root=2*np.pi*(kk-1.375)/lambertw((kk-1.375)/np.e).real
        assert root>2*np.pi and abs(C.N0(root)-(kk-.5))<1e-8
    result=dict(digits=60,phase_checks=checks,root_checks=roots,clock_difference_errors=cd,
                maxima={name:max(r[name] for r in checks) for name in ['phase_abs_error','derivative_abs_error','theta_abs_error']},
                zeta_or_true_ordinate_used=False,pass_checks=True)
    (OUT/'high_precision_checks.json').write_text(json.dumps(result,indent=2))
    print(json.dumps({k:v for k,v in result.items() if k not in ['phase_checks','root_checks']},indent=2))

if __name__=='__main__':main()
