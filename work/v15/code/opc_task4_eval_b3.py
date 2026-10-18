"""Evaluate all constructions on sample block 3 (10 000 consecutive indices) against the true ordinates."""
import glob, json
import numpy as np
from opc_common import *
tau_all = load('zLamb.bin'); gam_all = load('zeross.bin'); cas_all = load('zCasanya.bin'); first = 1400736
pts3 = np.load('outputs/task3_points.npy')
b3 = np.load(sorted(glob.glob('outputs/task4_points_c*_b3.npy'))[0])[0].astype(int)
tau, gam = tau_all[b3], gam_all[b3]
M = {'RvM': tau, 'zCasanya': cas_all[b3], 'R2': pts3[2][b3 - first]}
for f in sorted(glob.glob('outputs/task4_points_c*.npy')):
    a = np.load(f); ii = a[0].astype(int); pos = np.searchsorted(ii, b3)
    if np.all(ii[pos] == b3):
        M['c=' + f.split('_c')[-1].replace('.npy', '')] = a[1][pos]
rows = []
for nm, x in M.items():
    e = x - gam; r = clock_diff(gam, tau) - clock_diff(x, tau)
    wk = np.cumsum(np.exp(1j * x) - np.exp(1j * gam))
    rows.append(dict(method=nm, rms=float(np.sqrt(np.mean(e**2))), p99=float(np.quantile(abs(e), .99)), max=float(abs(e).max()),
                     gap1=float(np.sqrt(np.mean(np.diff(r)**2))), acorr=acorr(r), cross=int(np.sum(np.diff(x) <= 0)),
                     walk_end=float(abs(wk[-1])), walk_max=float(abs(wk).max())))
    print(f"{nm:22s} rms {rows[-1]['rms']:.5f} p99 {rows[-1]['p99']:.4f} max {rows[-1]['max']:.3f} gap1 {rows[-1]['gap1']:.4f} "
          f"ac {rows[-1]['acorr'][0]:+.3f} {rows[-1]['acorr'][1]:+.3f} cross {rows[-1]['cross']} walk {rows[-1]['walk_end']:.3f}/{rows[-1]['walk_max']:.3f}")
json.dump(rows, open('outputs/task4_eval_b3.json', 'w'), indent=2)
