"""Corrected Gram law and local separation of the ordinates for the zero-free constructions.

For points x_k (computed from the clock and the primes only) let m_k = (x_k + x_{k+1})/2.
  law at k:          the interval (m_{k-1}, m_k] contains an odd number of ordinates;
                     since all zeros of the table are simple and on the critical line (verified far beyond
                     this height), this is the sign change Z(m_{k-1}) Z(m_k) < 0;
  one zero at k:     the interval contains exactly one ordinate;
  separation G(eta): |e_j| < eta / L(tau_k) for j = k-1, k, k+1 and x_k - x_{k-1}, x_{k+1} - x_k > 2 eta / L(tau_k),
                     e_j = x_j - gamma_j  (sufficient for 'one zero at k', Proposition prop:local_separation);
  gap(eta):          L(tau_k) * min(x_k - x_{k-1}, x_{k+1} - x_k) <= 2 eta  (computable without zeros).
The bare clock gives the clock midpoints, which are within O(1/tau) of Gram points (Gram's law).
The ordinates are read only to evaluate.  Writes ../outputs/separation_v15.{json,csv,txt}.
"""
import json, csv, os
import numpy as np
from opc_common_v15 import *

HERE = os.path.dirname(os.path.abspath(__file__))
PREP = os.path.join(HERE, '../../v15_prep/outputs')
out = open(os.path.join(HERE, '../outputs/separation_v15.txt'), 'w')


def say(s=''):
    print(s, flush=True)
    out.write(s + '\n')


tau_all = load('zLamb.bin'); gam_all = load('zeross.bin'); cas_all = load('zCasanya.bin')
N = tau_all.size
first = 1400736                       # 0-based start of the untouched test set k = 1 400 737 ... 2 001 052
ETAS = (0.10, 0.15, 0.20, 0.25, 0.30)


def evaluate(idx, x):
    """idx: 0-based consecutive indices, x: points; statistics over the interior indices."""
    tau, gam = tau_all[idx], gam_all[idx]
    m = 0.5 * (x[1:] + x[:-1])                        # m_k between k and k+1
    cnt = np.searchsorted(gam_all, m[1:], side='right') - np.searchsorted(gam_all, m[:-1], side='right')
    Lk = L(tau[1:-1])
    e = x - gam
    ae = np.abs(e)
    g_lo = x[1:-1] - x[:-2]; g_hi = x[2:] - x[1:-1]
    row = dict(n=int(idx.size - 2), law=float(np.mean(cnt % 2 == 1)), one_zero=float(np.mean(cnt == 1)),
               crossings=int(np.sum(np.diff(x) <= 0)))
    for eta in ETAS:
        h = eta / Lk
        sep = (ae[:-2] < h) & (ae[1:-1] < h) & (ae[2:] < h) & (g_lo > 2 * h) & (g_hi > 2 * h)
        assert np.all(cnt[sep] == 1)                 # Proposition prop:local_separation
        row[f'sep_{eta:.2f}'] = float(np.mean(sep))
        row[f'gap_{eta:.2f}'] = float(np.mean(Lk * np.minimum(g_lo, g_hi) <= 2 * eta))
    return row


rows = []
test = np.arange(first, N)
pts3 = np.load(os.path.join(PREP, 'task3_points.npy'))
methods = [('bare clock (Gram midpoints)', tau_all[test]), ('zCasanya (8,8,512)', cas_all[test]),
           ('Stage A: monotone root X=16', pts3[0]), ('rule N: continuation to (tau/2pi)^(1/2)', pts3[1]),
           ('rule G: continuation to (tau/2pi)^c_G', pts3[2])]
for nm, x in methods:
    r = evaluate(test, x); r.update(method=nm, set='test k=1400737..2001052'); rows.append(r)
allk = np.arange(N)
for nm, x in (('bare clock (Gram midpoints)', tau_all), ('zCasanya (8,8,512)', cas_all)):
    r = evaluate(allk, x); r.update(method=nm, set='all k=1..2001052'); rows.append(r)
b3 = np.load(os.path.join(PREP, 'task4_points_c1.30_b3.npy'))[0].astype(int)
for nm, x in (('bare clock (Gram midpoints)', tau_all[b3]), ('zCasanya (8,8,512)', cas_all[b3]),
              ('rule G', pts3[2][b3 - first])):
    r = evaluate(b3, x); r.update(method=nm, set='block 3'); rows.append(r)
for c in ('0.85', '1.00'):
    z = np.load(os.path.join(PREP, f'task4_points_c{c}.npy')); ii = z[0].astype(int)
    r = evaluate(b3, z[1][np.searchsorted(ii, b3)]); r.update(method=f'continuation c={c}', set='block 3'); rows.append(r)
for c in ('1.15', '1.30'):
    z = np.load(os.path.join(PREP, f'task4_points_c{c}_b3.npy'))
    r = evaluate(b3, z[1]); r.update(method=f'continuation c={c}', set='block 3'); rows.append(r)

say('Corrected Gram law and local separation (fractions of interior indices)')
say(f"{'set':26s} {'method':42s} {'law':>8s} {'one':>8s} " + ' '.join(f'sep{e:.2f}' for e in ETAS)
    + ' ' + ' '.join(f'gap{e:.2f}' for e in ETAS) + ' cross')
for r in rows:
    say(f"{r['set']:26s} {r['method']:42s} {r['law']:8.5f} {r['one_zero']:8.5f} "
        + ' '.join(f"{r[f'sep_{e:.2f}']:7.4f}" for e in ETAS) + ' '
        + ' '.join(f"{r[f'gap_{e:.2f}']:7.4f}" for e in ETAS) + f" {r['crossings']:5d}")
json.dump(rows, open(os.path.join(HERE, '../outputs/separation_v15.json'), 'w'), indent=2)
keys = ['set', 'method', 'n', 'law', 'one_zero', 'crossings'] + [f'sep_{e:.2f}' for e in ETAS] + [f'gap_{e:.2f}' for e in ETAS]
with open(os.path.join(HERE, '../outputs/separation_v15.csv'), 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=keys); w.writeheader(); w.writerows(rows)
out.close()
