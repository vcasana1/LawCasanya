"""Task 4. Self-consistent cutoff: continuation from the monotone root up to Y = (tau/2pi)^{c_target}.

Zero-free calibration (task 3 outputs): kappa_s = <(L (x_A - x_R2))^2> / model sum_{16<n<=Y_R2} w_n/(2pi^2) = 0.886.
With sigma^2(c) = kappa_s/(2pi^2) sum_{(tau/2pi)^c < n <= tau/2pi} w_n the gain rule c = 0.1874/sigma(c)
has no fixed point below c = 1 at these heights (c_phi > 1 for every c in [0.5, 1)), so the rule asks for all
prime powers up to tau/2pi.  c_target = 1.0 is the rule; c_target = 0.85 is run as a diagnostic.
Evaluated on 6 contiguous blocks of 10 000 indices inside the untouched test range.
Usage: python3 opc_task4_selfconsistent_cutoff.py C_TARGET
"""
import sys, json, time
import numpy as np
from opc_common import *

c_target = float(sys.argv[1])
nblocks = int(sys.argv[2]) if len(sys.argv) > 2 else 6
t0 = time.time()
tau_all = load('zLamb.bin')
N = tau_all.size
first = 1400736
starts = np.linspace(first, N - 10000, 6).astype(int)
starts = starts if nblocks == 6 else starts[[2]]
idx = np.concatenate([np.arange(s, s + 10000) for s in starts])
tau = tau_all[idx]
k = idx + 1.0
base = N0(tau) - (k - 0.5)
xA_all = np.load('outputs/task3_points.npy')[0]
xA = xA_all[idx - first]
Xmon = np.full(tau.size, 16.0)
Ymax = (tau / TWO_PI) ** c_target
LEVELS = 8


def S_dS_matrix(t, Y, need_S=True, chunk=None):
    """S_Y and S_Y' with per-point cutoff, vectorised by chunks (terms sorted by n)."""
    J = np.searchsorted(PP_N, Y, side='right')
    nt = int(J.max())
    fr, co, dc = PP_FREQ[:nt], PP_COEF[:nt], PP_DCOEF[:nt]
    S = np.zeros(t.size); dS = np.zeros(t.size)
    jj = np.arange(nt)
    chunk = chunk or max(20, int(1.5e7 / nt))
    for lo in range(0, t.size, chunk):
        hi = min(t.size, lo + chunk)
        ang = np.outer(t[lo:hi], fr)
        mask = jj[None, :] < J[lo:hi, None]
        if need_S:
            S[lo:hi] = -np.sum(np.where(mask, np.sin(ang), 0.0) * co, axis=1)
        dS[lo:hi] = -np.sum(np.where(mask, np.cos(ang), 0.0) * dc, axis=1)
    return S, dS


x = xA.copy(); Ycur = Xmon.copy(); active = np.ones(tau.size, bool); acc = []
for lev in range(1, LEVELS + 1):
    Ynew = np.maximum(np.floor(Xmon * (Ymax / Xmon) ** (lev / LEVELS)), Ycur)
    a = np.flatnonzero(active & (Ynew > Ycur))
    ta, ba, xa, Ya, Yp = tau[a], base[a], x[a].copy(), Ynew[a], Ycur[a]
    Lt = L(ta); good = np.ones(a.size, bool)
    for it in range(7):
        S, dS = S_dS_matrix(xa, Ya)
        res = ba + clock_diff(xa, ta) + S
        der = L(xa) + dS
        bad = der <= 0.1 * L(xa); good &= ~bad
        xa = xa - np.clip(np.where(bad, 0, res / np.where(bad, 1, der)), -0.25 / Lt, 0.25 / Lt)
    S, dS = S_dS_matrix(xa, Ya)
    good &= np.abs(ba + clock_diff(xa, ta) + S) < 1e-9
    for s in (0.0, 0.5, 1.0):
        pt = x[a] + s * (xa - x[a])
        _, d1 = S_dS_matrix(pt, Ya, need_S=False); _, d0 = S_dS_matrix(pt, Yp, need_S=False)
        good &= (L(pt) + d1 > 0.1 * L(pt)) & (L(pt) + d0 > 0.1 * L(pt))
    x[a[good]] = xa[good]; Ycur[a[good]] = Ya[good]; active[a[~good]] = False
    acc.append(float(good.mean()))
    print(f'c={c_target} level {lev}: tried {a.size}, accepted {good.mean():.4f}, median Y {np.median(Ya):.0f}, '
          f'{time.time()-t0:.0f}s', flush=True)
np.save(f'outputs/task4_points_c{c_target:.2f}' + ('' if nblocks == 6 else '_b3') + '.npy', np.vstack([idx.astype(float), x, Ycur]))
json.dump(dict(c_target=c_target, accepted=acc, kappa_s=0.8857, seconds=time.time() - t0,
               final_c_median=float(np.median(np.log(Ycur) / np.log(tau / TWO_PI))),
               final_c_quantiles=[float(q) for q in np.quantile(np.log(Ycur) / np.log(tau / TWO_PI), [.01, .1, .5])]),
          open(f'outputs/task4_info_c{c_target:.2f}' + ('' if nblocks == 6 else '_b3') + '.json', 'w'), indent=2)
print('done', time.time() - t0)
