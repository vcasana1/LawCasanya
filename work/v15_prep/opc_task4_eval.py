"""Evaluate task-4 constructions against the true ordinates on the 6 sample blocks (10 000 consecutive indices each)."""
import json, glob
import numpy as np
from opc_common import *

tau_all = load('zLamb.bin'); gam_all = load('zeross.bin'); cas_all = load('zCasanya.bin')
first = 1400736
pts3 = np.load('outputs/task3_points.npy')
runs = {}
for f in sorted(glob.glob('outputs/task4_points_c*.npy')):
    a = np.load(f); runs[f.split('_c')[-1][:-4]] = a
idx = runs[next(iter(runs))][0].astype(int)
tau, gam = tau_all[idx], gam_all[idx]
methods = {'RvM clock': tau, 'zCasanya (8,8,512)': cas_all[idx], 'Stage A (X=16)': pts3[0][idx - first],
           'R2 (c_phi model)': pts3[2][idx - first]}
for c, a in runs.items():
    methods[f'self-consistent c={c}'] = a[1]
nb = 6
rows = []
for nm, x in methods.items():
    e = x - gam
    r = clock_diff(gam, tau) - clock_diff(x, tau)
    g1, g2, ac, cr, wd, wm = [], [], [], [], [], []
    for b in range(nb):
        s = slice(b * 10000, (b + 1) * 10000)
        rb, xb, gb = r[s], x[s], gam[s]
        g1.append(np.mean((rb[1:] - rb[:-1]) ** 2)); g2.append(np.mean((rb[2:] - rb[:-2]) ** 2))
        ac.append(acorr(rb)); cr.append(int(np.sum(np.diff(xb) <= 0)))
        wk = np.cumsum(np.exp(1j * xb) - np.exp(1j * gb)); wd.append(abs(wk[-1])); wm.append(np.max(np.abs(wk)))
    ac = np.mean(np.array(ac), axis=0)
    rows.append(dict(method=nm, rms=float(np.sqrt(np.mean(e ** 2))), p99=float(np.quantile(np.abs(e), .99)),
                     max_abs=float(np.max(np.abs(e))), rms_ordinal=float(np.sqrt(np.mean(r ** 2))),
                     gap_h1=float(np.sqrt(np.mean(g1))), gap_h2=float(np.sqrt(np.mean(g2))),
                     acorr1=float(ac[0]), acorr2=float(ac[1]), acorr3=float(ac[2]), crossings=int(sum(cr)),
                     walk_block_end_mean=float(np.mean(wd)), walk_block_max_mean=float(np.mean(wm))))
json.dump(rows, open('outputs/task4_eval.json', 'w'), indent=2)
for r_ in rows:
    print(f"{r_['method']:28s} rms {r_['rms']:.5f} p99 {r_['p99']:.4f} max {r_['max_abs']:.3f} ord {r_['rms_ordinal']:.4f} "
          f"gap1 {r_['gap_h1']:.4f} gap2 {r_['gap_h2']:.4f} ac {r_['acorr1']:+.3f} {r_['acorr2']:+.3f} {r_['acorr3']:+.3f} "
          f"cross {r_['crossings']} walk_end {r_['walk_block_end_mean']:.3f} walk_max {r_['walk_block_max_mean']:.3f}")
