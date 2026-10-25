"""Build the best zero-free tauc construction (AGENTS.md section 5) on a block of indices OUTSIDE the untouched
test set, for the nearest-neighbour gap test against the true ordinates.

Construction (identical to work/v15_prep/opc_task3_analytic_rule.py Stage A + opc_task4_selfconsistent_cutoff.py):
  Stage A: certified monotone root of N0 + S_Xmon = k - 1/2, X_mon(k) = largest prime power n with
           B(n) = sum_{n'<=n} Lambda(n')/sqrt(n') <= (1-eta)/2 log((tau_k-1)/2pi), eta = 0.1; bisection.
  Continuation: geometric ladder of 8 cutoffs from X_mon to Y_max = (tau_k/2pi)^c; Newton with the true derivative
           at each level; a level is accepted only if F' > 0.1 L at sampled points of the segment, otherwise the
           index keeps its last accepted cutoff.
Only tau_k (data/zLamb.bin) and primes enter; the true ordinates are NOT read by this program.
Usage: python3 opc_gaps_build_tauc.py K_FIRST COUNT C
  K_FIRST is the 1-based index of the first zero of the block; the block must end before k = 1 400 737.
"""
import sys, os, json, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(REPO, 'work', 'v15_prep'))
from opc_common import *

k_first, count, c_target = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
TEST_FIRST_K = 1400737
assert k_first >= 2 and k_first + count - 1 < TEST_FIRST_K, 'block touches the untouched test set'
t0 = time.time()
tau_all = load(os.path.join(REPO, 'data', 'zLamb.bin'))
idx = np.arange(k_first - 1, k_first - 1 + count)          # 0-based
tau = tau_all[idx]
k = idx + 1.0
base = N0(tau) - (k - 0.5)
ETA = 0.1
LEVELS = 8

# ---------- Stage A (certified monotone root)
thr = (1 - ETA) / 2 * np.log((tau - 1) / TWO_PI)
jm = np.searchsorted(PP_B, thr, side='right') - 1
Xmon = np.where(jm >= 0, PP_N[np.maximum(jm, 0)], 1).astype(float)
Abound = np.cumsum(PP_COEF)[np.maximum(jm, 0)] * (jm >= 0)
Bmon = PP_B[np.maximum(jm, 0)] * (jm >= 0)
h = 1.1 * (Abound + np.abs(base)) / (L(tau - 1) - Bmon / np.pi) + 1e-9
lo = tau - h; hi = tau + h
g = lambda x, X: base + clock_diff(x, tau) + S_and_dS(x, X, need_d=False)[0]
bracket_ok = (g(lo, Xmon) < 0) & (g(hi, Xmon) > 0)
for _ in range(55):
    mid = 0.5 * (lo + hi)
    neg = g(mid, Xmon) < 0
    lo = np.where(neg, mid, lo); hi = np.where(neg, hi, mid)
xA = 0.5 * (lo + hi)
print(f'Stage A: X_mon {np.unique(Xmon)}, bracket ok {bracket_ok.mean():.6f}, {time.time()-t0:.0f}s', flush=True)

Ymax = (tau / TWO_PI) ** c_target


def S_dS_matrix(t, Y, need_S=True, chunk=None):
    J = np.searchsorted(PP_N, Y, side='right')
    nt = int(J.max())
    fr, co, dc = PP_FREQ[:nt], PP_COEF[:nt], PP_DCOEF[:nt]
    S = np.zeros(t.size); dS = np.zeros(t.size)
    jj = np.arange(nt)
    chunk = chunk or max(20, int(1.5e7 / nt))
    for a0 in range(0, t.size, chunk):
        a1 = min(t.size, a0 + chunk)
        ang = np.outer(t[a0:a1], fr)
        mask = jj[None, :] < J[a0:a1, None]
        if need_S:
            S[a0:a1] = -np.sum(np.where(mask, np.sin(ang), 0.0) * co, axis=1)
        dS[a0:a1] = -np.sum(np.where(mask, np.cos(ang), 0.0) * dc, axis=1)
    return S, dS


x = xA.copy(); Ycur = Xmon.copy(); active = np.ones(tau.size, bool); acc = []
for lev in range(1, LEVELS + 1):
    Ynew = np.maximum(np.floor(Xmon * (Ymax / Xmon) ** (lev / LEVELS)), Ycur)
    a = np.flatnonzero(active & (Ynew > Ycur))
    if a.size == 0:
        acc.append(0.0); continue
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

tag = f'k{k_first}_n{count}_c{c_target:.2f}'
np.save(os.path.join(HERE, 'outputs', f'tauc_{tag}.npy'), np.vstack([idx.astype(float), x, Ycur]))
json.dump(dict(k_first=k_first, count=count, c_target=c_target, Xmon_values=[float(v) for v in np.unique(Xmon)],
               bracket_ok=float(bracket_ok.mean()), accepted=acc, seconds=time.time() - t0,
               final_c_quantiles=[float(q) for q in np.quantile(np.log(Ycur) / np.log(tau / TWO_PI), [.01, .1, .5])]),
          open(os.path.join(HERE, 'outputs', f'tauc_{tag}.json'), 'w'), indent=2)
print('done', time.time() - t0)
