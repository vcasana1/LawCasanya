"""Direct ordinal defects and finite-window prime responses; no fitted parameters.

Usage: python opc_extensions_v10.py DATA_DIR [--skip-responses]
Writes tables and diagnostics beside the original companion outputs.
"""
import argparse
import csv
import hashlib
import json
import platform
import sys
from pathlib import Path

import numpy as np
import scipy


def primes_upto(n):
    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            sieve[p*p::p] = False
    return np.flatnonzero(sieve)


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(1024*1024), b''):
            h.update(block)
    return h.hexdigest()


def phase(p, t):
    return -np.angle(1 - p**(-0.5)*np.exp(-1j*t*np.log(p)))/np.pi


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_dir', type=Path)
    parser.add_argument('--skip-responses', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    out = root/'outputs'
    out.mkdir(exist_ok=True)
    expected = 2001052
    arrays = {}
    metadata = {'python': platform.python_version(), 'numpy': np.__version__,
                'scipy': scipy.__version__, 'files': {}}
    for name in ('zeross.bin', 'zLamb.bin'):
        path = args.data_dir/name
        if not path.is_file() or path.stat().st_size != 8*expected:
            raise ValueError(f'{path}: expected exactly {expected} little-endian float64 values')
        values = np.fromfile(path, dtype='<f8')
        if not np.isfinite(values).all() or np.any(np.diff(values) < 0):
            raise ValueError(f'{path}: values must be finite and nondecreasing')
        arrays[name] = values
        metadata['files'][name] = {'size_bytes': path.stat().st_size, 'sha256': digest(path)}
    gam, tau = arrays['zeross.bin'], arrays['zLamb.bin']
    k = np.arange(1, expected+1, dtype=float)
    Ltau = np.log(tau/(2*np.pi))/(2*np.pi)
    N0gam = gam/(2*np.pi)*np.log(gam/(2*np.pi*np.e)) + 7/8
    s = k - 0.5 - N0gam
    q = Ltau*(tau-gam)
    metadata['max_clock_equation_error'] = float(np.max(np.abs(
        tau/(2*np.pi)*np.log(tau/(2*np.pi*np.e))+7/8-k+0.5)))
    metadata['max_abs_q_minus_s'] = float(np.max(np.abs(q-s)))
    PR = primes_upto(20000)
    C = (1/160, 1/80, 1/40, 1/20, 1/10, 1/5, 1/3, 1/2)
    metadata['parameters'] = {'expected_count':expected, 'prime_max':20000,
        'defect_dyadic_exponents':[14,16,18,19], 'defect_exponents':list(C),
        'defect_cutoff_is_constant_on_each_height_window':True,
        'cutoffs_below_two':'excluded', 'Euler_phase':'full local factors',
        'prime_response_ordinal_windows':[[1000,10000],[10000,100000],
            [100000,500000],[500000,1000000],[1000000,expected]],
        'response_target':'exact s_k=k-1/2-N0(gamma_k)',
        'theta':'log(p)/median(log(tau_k/(2*pi)))',
        'response_bin_width':0.05, 'minimum_primes_per_bin':5}
    defect_rows = []
    for r in (14, 16, 18, 19):
        T = float(2**r)
        mask = (gam > T) & (gam <= 2*T)
        t, z, st = gam[mask], tau[mask], s[mask]
        for c in C:
            X = T**c
            if X < 2:
                continue
            P = PR[PR <= X]
            Sg = np.zeros(len(t))
            St = np.zeros(len(t))
            for p in P:
                Sg += phase(int(p), t)
                St += phase(int(p), z)
            u = st-Sg
            # Exact ordinal residual of the one-step clock, without saturation.
            rk = q[mask]-St
            lead = np.log(1/c)/(2*np.pi**2)
            defect_rows.append((r, int(T), len(t), c, X, len(P),
                                float(np.mean(u*u)), lead,
                                float(np.mean(u*u))-lead,
                                float(np.mean(rk*rk))))
        print(f'direct defects: T=2^{r}, zeros={len(t)}', flush=True)
    with (out/'table_F_direct_defects.csv').open('w', newline='') as f:
        w=csv.writer(f)
        w.writerow(('r','T','zero_count','c','X','prime_count','mean_u2',
                    'log_1_over_c_over_2pi2','difference','mean_one_step_r2'))
        w.writerows(defect_rows)

    if not args.skip_responses:
        windows = [(1000,10000),(10000,100000),(100000,500000),
                   (500000,1000000),(1000000,expected)]
        medians = [float(np.median(np.log(tau[a:b]/(2*np.pi)))) for a,b in windows]
        rows = []
        for ip,p0 in enumerate(PR):
            p = int(p0)
            lg = np.log(p)
            sn_g = np.sin(gam*lg)
            sn_t = np.sin(tau*lg)
            for j,((a,b),L) in enumerate(zip(windows,medians)):
                rg = -2*np.pi*np.sqrt(p)*np.mean(s[a:b]*sn_g[a:b])
                rt = -2*np.pi*np.sqrt(p)*np.mean(s[a:b]*sn_t[a:b])
                th = lg/L
                law = (1-(1+th)*np.log1p(th)-(1-th)*np.log1p(-th)
                       if 0 < th < 1 else float('nan'))
                rows.append((j+1,a,b,p,th,float(rg),float(rt),float(law)))
            if ip % 200 == 0:
                print(f'prime responses: {ip+1}/{len(PR)} (p={p})',flush=True)
        with (out/'table_G_prime_responses.csv').open('w',newline='') as f:
            w=csv.writer(f)
            w.writerow(('window','k_lower_exclusive','k_upper_inclusive','prime',
                        'theta_median','rho_gamma','rho_tau','sine_response_prediction'))
            w.writerows(rows)
        diagnostics=[]
        rr=np.array(rows)
        for j in range(1,6):
            selected=rr[(rr[:,0]==j)&(rr[:,4]>0)&(rr[:,4]<1)]
            central=selected[(selected[:,4]>=0.1)&(selected[:,4]<=0.8)]
            diagnostics.append({'window':j,'prime_count_total':len(PR),
              'prime_count_theta_below_one':len(selected),
              'max_abs_gamma_minus_prediction':float(np.max(np.abs(selected[:,5]-selected[:,7]))),
              'rms_gamma_minus_prediction':float(np.sqrt(np.mean((selected[:,5]-selected[:,7])**2))),
              'prime_count_theta_01_to_08':len(central),
              'max_abs_gamma_minus_prediction_theta_01_to_08':float(np.max(np.abs(central[:,5]-central[:,7])))})
        metadata['prime_response_diagnostics']=diagnostics
    (out/'extension_metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
    print(json.dumps(metadata,indent=2),flush=True)


if __name__ == '__main__':
    main()
