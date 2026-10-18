"""Block-3 comparison of all constructions against the true ordinates, and fit of e^2(c) for the continuation runs.
Writes outputs/task4_fit_b3.txt and outputs/task4_fit_b3.json (the console output is the same text)."""
import json, sys
import numpy as np
from opc_common import *
out = open('outputs/task4_fit_b3.txt', 'w')
def say(s=''):
    print(s); out.write(s + '\n')
tau_all = load('zLamb.bin'); gam_all = load('zeross.bin'); cas_all = load('zCasanya.bin'); first = 1400736
pts3 = np.load('outputs/task3_points.npy')
a130 = np.load('outputs/task4_points_c1.30_b3.npy'); b3 = a130[0].astype(int)
tau, gam = tau_all[b3], gam_all[b3]
M = {'RvM clock': tau, 'zCasanya (8,8,512)': cas_all[b3], 'R2 (c_phi model)': pts3[2][b3 - first]}
for c in ('0.85', '1.00'):
    z = np.load(f'outputs/task4_points_c{c}.npy'); ii = z[0].astype(int); M['c=' + c] = z[1][np.searchsorted(ii, b3)]
M['c=1.15'] = np.load('outputs/task4_points_c1.15_b3.npy')[1]; M['c=1.30'] = a130[1]
say(f'Block 3: k = {b3[0]+1} ... {b3[-1]+1} (10 000 consecutive indices of the untouched test set); errors against gamma_k')
say(f"{'method':20s} {'rms':>8s} {'e2':>10s} {'p99':>7s} {'max':>6s} {'gap1':>7s} {'ac1':>7s} {'ac2':>7s} {'cross':>5s} {'walk_end':>8s} {'walk_max':>8s}")
rows = []; cs = []; es = []
for nm, x in M.items():
    e = x - gam; r = clock_diff(gam, tau) - clock_diff(x, tau); wk = np.cumsum(np.exp(1j * x) - np.exp(1j * gam))
    rms = float(np.sqrt(np.mean(e ** 2))); ac = acorr(r)
    row = dict(method=nm, rms=rms, e2=rms ** 2, p99=float(np.quantile(abs(e), .99)), max=float(abs(e).max()),
               gap1=float(np.sqrt(np.mean(np.diff(r) ** 2))), acorr1=ac[0], acorr2=ac[1],
               crossings=int(np.sum(np.diff(x) <= 0)), walk_end=float(abs(wk[-1])), walk_max=float(abs(wk).max()))
    rows.append(row)
    say(f"{nm:20s} {rms:8.5f} {rms**2:10.3e} {row['p99']:7.4f} {row['max']:6.3f} {row['gap1']:7.4f} {ac[0]:+7.3f} {ac[1]:+7.3f} {row['crossings']:5d} {row['walk_end']:8.3f} {row['walk_max']:8.3f}")
    if nm.startswith('c='):
        cs.append(float(nm[2:])); es.append(rms ** 2)
lc = np.log(cs); es = np.array(es)
p1 = np.polyfit(lc, es, 1); p2 = np.polyfit(lc, es, 2)
slopes = np.diff(es) / np.diff(lc)
say('')
say('Fit of e^2 against log c over c = ' + ', '.join(f'{c:.2f}' for c in cs))
say(f'local slopes d(e^2)/d(log c): ' + ', '.join(f'{s:.3e}' for s in slopes))
say(f'linear fit: e^2 = {p1[1]:.3e} + ({p1[0]:.3e}) log c, zero at c = {np.exp(-p1[1]/p1[0]):.3f}')
say(f'quadratic fit: minimum e^2 = {np.polyval(p2, -p2[1]/(2*p2[0])):.3e} (rms {np.sqrt(max(np.polyval(p2, -p2[1]/(2*p2[0])),0)):.4f}) at c = {np.exp(-p2[1]/(2*p2[0])):.3f}  [4-point estimate]')
pred = es[2] + slopes[1] * np.log(1.30 / 1.15)
say(f'straight-line prediction for c = 1.30 from c = 1.00, 1.15: e^2 = {pred:.3e}; observed {es[3]:.3e}')
json.dump(dict(block=[int(b3[0] + 1), int(b3[-1] + 1)], rows=rows, c=cs, e2=es.tolist(), slopes=slopes.tolist(),
               linear_fit=p1.tolist(), quadratic_fit=p2.tolist()), open('outputs/task4_fit_b3.json', 'w'), indent=2)
out.close()
