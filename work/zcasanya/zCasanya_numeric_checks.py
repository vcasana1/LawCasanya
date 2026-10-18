#!/usr/bin/env python3
"""Numerical checks without true-zero input; high precision uses only elementary functions."""
import json
from pathlib import Path
import sys
import mpmath as mp
import numpy as np
from zCasanya_build import clock_difference, clock, slope, phase, guard


def main():
    sys.addaudithook(guard)
    out = Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parent
    tau = np.fromfile(out / 'inputs' / 'zLamb.bin', dtype='<f8')
    primes = np.fromfile(out / 'inputs' / 'primoss.bin', dtype='<u8')
    mp.mp.dps = 70
    def f(t):
        return t/(2*mp.pi)*(mp.log(t/(2*mp.pi))-1)+mp.mpf(7)/8
    ids = np.unique(np.r_[np.arange(20), np.linspace(0,len(tau)-1,70).astype(int)])
    diff_errors, base_errors, formula_errors = [], [], []
    for k in ids:
        a = float(tau[k])
        base_errors.append(abs(float(mp.mpf(float(clock(np.array([a]))[0]))-f(mp.mpf(a)))))
        for d in [-1., -.01, 0., .01, 1.]:
            b = a+d
            truth = f(mp.mpf(b))-f(mp.mpf(a))
            actual = clock_difference(np.array([b]), np.array([a]))[0]
            diff_errors.append(abs(float(mp.mpf(float(actual))-truth)))
            u = mp.mpf(b-a)/mp.mpf(a)
            proposed = mp.log(mp.mpf(a)/(2*mp.pi))/(2*mp.pi)*(b-a)
            if u:
                proposed += (b-a)/(2*mp.pi)*(mp.log1p(u)/u-1)*u
            formula_errors.append(abs(float(proposed-truth)))
    sample = tau[ids[::10]]
    phase_errors = {}
    for window in ['euler_v10','power_sharp']:
        for cutoff in [8,128,8192]:
            actual = phase(sample,primes,cutoff,window)
            errors=[]
            for t, got in zip(sample,actual):
                total=mp.mpf(0)
                for p in primes[primes<=cutoff]:
                    p=int(p); angle=mp.mpf(float(t))*mp.log(p)
                    if window=='euler_v10':
                        r=1/mp.sqrt(p)
                        total-=mp.atan2(r*mp.sin(angle),1-r*mp.cos(angle))/mp.pi
                    else:
                        q,m=p,1
                        while q<=cutoff:
                            total-=mp.sin(m*angle)/(mp.pi*m*mp.sqrt(q))
                            q,m=q*p,m+1
                errors.append(abs(float(mp.mpf(float(got))-total)))
            phase_errors[window+'_'+str(cutoff)] = max(errors)
    # Independently compare infinite-power series with the closed local factor.
    series_errors=[]
    for p in [2,3,127]:
        for t in [14.5,1000.,1132490.7]:
            angle=mp.mpf(t)*mp.log(p); r=1/mp.sqrt(p)
            series=sum(mp.sin(m*angle)*r**m/m for m in range(1,501))
            closed=mp.atan2(r*mp.sin(angle),1-r*mp.cos(angle))
            series_errors.append(abs(float(series-closed)))
    result={'precision_decimal_digits':70,
            'clock_difference_max_error':max(diff_errors),
            'direct_clock_max_roundoff_vs_high_precision':max(base_errors),
            'pasted_stable_formula_max_error':max(formula_errors),
            'phase_max_errors':phase_errors,
            'local_factor_vs_500_powers_max_error':max(series_errors),
            'longdouble_epsilon':float(np.finfo(np.longdouble).eps),
            'tested_height_range':[float(tau[ids[0]]),float(tau[ids[-1]])]}
    assert result['clock_difference_max_error']<1e-13
    assert result['direct_clock_max_roundoff_vs_high_precision']<2e-9
    assert max(phase_errors.values())<5e-9
    assert max(series_errors)<1e-60
    blocked=False
    try:
        open(out/'zeross_DO_NOT_READ.bin','rb')
    except PermissionError:
        blocked=True
    assert blocked
    result['true_zero_access_guard_test_passed']=blocked
    (out/'numeric_checks.json').write_text(json.dumps(result,indent=2))
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
