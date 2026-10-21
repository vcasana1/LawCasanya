"""Task 3. Construction with the analytic per-index cutoff rule and comparison with zCasanya (8,8,512)
on the untouched final 30% of the indices (k = 1 400 737 ... 2 001 052).

Stage A (certified monotone root): X_mon(k) = largest prime power n with
    B(n) = sum_{n'<=n} Lambda(n')/sqrt(n') <= (1-eta)/2 * log((tau_k - 1)/2pi),  eta = 0.1,
  so that F_X' >= eta L > 0 on [tau_k - 1, oo); the unique root of N0 + S_X = k - 1/2 is found by bisection.
Stage B (continuation): geometric ladder of 6 cutoffs from X_mon(k) to Y_max(k); at each level Newton with the
  true derivative from the previous root; the level is accepted only if F_Y' > 0.1 L and F_prev' > 0.1 L at 5
  points of the segment between the two roots (sampled check, not interval arithmetic); otherwise the index
  stays at its last accepted cutoff.
  Rule R1: Y_max = sqrt(tau/2pi) (Nyquist).
  Rule R2: Y_max = (tau/2pi)^{c_phi},  c_phi = sqrt(2 log 2)/(2 pi sigma),  sigma^2 = (1/2pi^2) sum_{X_mon < n <= tau/2pi} w_n
  (Gaussian model, no zero used).
The true ordinates are read only to evaluate.
"""
import json, csv, time
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from opc_common import *

t0 = time.time()
tau_all = load('zLamb.bin'); gam_all = load('zeross.bin'); cas_all = load('zCasanya.bin')
N = tau_all.size
first = 1400736
idx = np.arange(first, N)
tau = tau_all[idx]; gam = gam_all[idx]; cas = cas_all[idx]
k = idx + 1.0
base = N0(tau) - (k - 0.5)
ETA = 0.1
LEVELS = 6

# ---------- Stage A
thr = (1 - ETA) / 2 * np.log((tau - 1) / TWO_PI)
jm = np.searchsorted(PP_B, thr, side='right') - 1
Xmon = np.where(jm >= 0, PP_N[np.maximum(jm, 0)], 1).astype(float)
Abound = np.cumsum(PP_COEF)[np.maximum(jm, 0)] * (jm >= 0)
Bmon = PP_B[np.maximum(jm, 0)] * (jm >= 0)
h = 1.1 * (Abound + np.abs(base)) / (L(tau - 1) - Bmon / np.pi) + 1e-9
lo = tau - h; hi = tau + h
g = lambda x, X: base + clock_diff(x, tau) + S_and_dS(x, X, need_d=False)[0]
glo, ghi = g(lo, Xmon), g(hi, Xmon)
bracket_ok = (glo < 0) & (ghi > 0)
for _ in range(55):
    mid = 0.5 * (lo + hi)
    gm = g(mid, Xmon)
    neg = gm < 0
    lo = np.where(neg, mid, lo); hi = np.where(neg, hi, mid)
xA = 0.5 * (lo + hi)
print(f'Stage A: X_mon values {np.unique(Xmon)}, bracket ok {bracket_ok.mean():.6f}, {time.time()-t0:.0f}s', flush=True)

# model sigma
Wc = np.concatenate([[0.0], np.cumsum(PP_W)])
iT = np.searchsorted(PP_N, tau / TWO_PI, side='right')
iX = np.searchsorted(PP_N, Xmon, side='right')
sigma_model = np.sqrt((Wc[iT] - Wc[iX]) / (2 * np.pi ** 2))
c_phi = np.sqrt(2 * np.log(2)) / (2 * np.pi * sigma_model)


def continuation(Ymax, label):
    x = xA.copy(); Ycur = Xmon.copy()
    active = np.ones(tau.size, bool)
    accepted = []
    for lev in range(1, LEVELS + 1):
        Ynew = np.floor(Xmon * (Ymax / Xmon) ** (lev / LEVELS))
        Ynew = np.maximum(Ynew, Ycur)
        a = np.flatnonzero(active & (Ynew > Ycur))
        if a.size == 0:
            accepted.append(0.0); continue
        ta, ba, xa, Ya, Yp = tau[a], base[a], x[a].copy(), Ynew[a], Ycur[a]
        Lt = L(ta)
        good = np.ones(a.size, bool)
        for it in range(10):
            S, dS = S_and_dS(xa, Ya)
            res = ba + clock_diff(xa, ta) + S
            der = L(xa) + dS
            bad = der <= 0.1 * L(xa)
            good &= ~bad
            step = np.clip(np.where(bad, 0, res / np.where(bad, 1, der)), -0.25 / Lt, 0.25 / Lt)
            xa = xa - step
        S, dS = S_and_dS(xa, Ya)
        res = ba + clock_diff(xa, ta) + S
        good &= (np.abs(res) < 1e-9)
        for s in (0.0, 0.25, 0.5, 0.75, 1.0):
            pt = x[a] + s * (xa - x[a])
            _, d1 = S_and_dS(pt, Ya); _, d0 = S_and_dS(pt, Yp)
            good &= (L(pt) + d1 > 0.1 * L(pt)) & (L(pt) + d0 > 0.1 * L(pt))
        x[a[good]] = xa[good]; Ycur[a[good]] = Ya[good]
        active[a[~good]] = False
        accepted.append(float(good.mean()))
        print(f'{label} level {lev}: tried {a.size}, accepted {good.mean():.4f}, '
              f'median Y {np.median(Ya):.0f}, {time.time()-t0:.0f}s', flush=True)
    return x, Ycur, accepted


xR1, YR1, accR1 = continuation(np.sqrt(tau / TWO_PI), 'R1')
xR2, YR2, accR2 = continuation((tau / TWO_PI) ** np.minimum(c_phi, 0.95), 'R2')

# ---------- evaluation
w = (tau.size - np.arange(tau.size)) / tau.size
def metrics(name, x):
    e = x - gam
    r = clock_diff(gam, tau) - clock_diff(x, tau)
    g1 = r[1:] - r[:-1]; g2 = r[2:] - r[:-2]
    _, _, pk, band = periodogram_peak(r)
    walk = np.cumsum(np.exp(1j * x) - np.exp(1j * gam))
    return dict(method=name, rms=float(np.sqrt(np.mean(e ** 2))), mae=float(np.mean(np.abs(e))),
                max_abs=float(np.max(np.abs(e))), p99=float(np.quantile(np.abs(e), .99)),
                improved_vs_RvM=float(np.mean(np.abs(e) < np.abs(tau - gam))),
                rms_ordinal=float(np.sqrt(np.mean(r ** 2))),
                gap_rms_h1=float(np.sqrt(np.mean(g1 ** 2))), gap_rms_h2=float(np.sqrt(np.mean(g2 ** 2))),
                acorr1=acorr(r)[0], acorr2=acorr(r)[1], acorr3=acorr(r)[2],
                crossings=int(np.sum(np.diff(x) <= 0)), spectral_peak=pk, band_04_05=band,
                walk_centroid_defect=float(abs(np.sum(w * (np.exp(1j * x) - np.exp(1j * gam))))),
                walk_max_defect=float(np.max(np.abs(walk))))

rows = [metrics('RvM clock', tau), metrics('zCasanya (8,8,512)', cas), metrics('Stage A: monotone root', xA),
        metrics('R1: continuation to sqrt(tau/2pi)', xR1), metrics('R2: continuation to (tau/2pi)^c_phi', xR2)]
ell = np.log(tau / TWO_PI)
info = dict(test_first_k=int(first + 1), test_last_k=int(N), n=int(tau.size),
            Xmon_values=[int(v) for v in np.unique(Xmon)], bracket_ok=float(bracket_ok.mean()),
            sigma_model_median=float(np.median(sigma_model)),
            sigma_actual_after_A=float(np.sqrt(np.mean((L(tau) * (xA - gam)) ** 2))),
            c_phi_median=float(np.median(c_phi)), accepted_R1=accR1, accepted_R2=accR2,
            final_c_R1_median=float(np.median(np.log(YR1) / ell)), final_c_R2_median=float(np.median(np.log(YR2) / ell)),
            final_c_R2_quartiles=[float(q) for q in np.quantile(np.log(YR2) / ell, [.1, .25, .5, .75, .9])],
            fraction_R2_beyond_nyquist=float(np.mean(YR2 > np.sqrt(tau / TWO_PI))),
            seconds=time.time() - t0)
json.dump(dict(info=info, methods=rows), open('outputs/task3_report.json', 'w'), indent=2)
with open('outputs/task3_methods.csv', 'w', newline='') as f:
    wr = csv.DictWriter(f, fieldnames=list(rows[0].keys())); wr.writeheader(); wr.writerows(rows)
np.save('outputs/task3_points.npy', np.vstack([xA, xR1, xR2, YR1, YR2]))

fig, axs = plt.subplots(1, 2, figsize=(13, 5))
for nm, x in (('zCasanya', cas), ('Stage A', xA), ('R1', xR1), ('R2', xR2)):
    r = clock_diff(gam, tau) - clock_diff(x, tau)
    a, P, pk, _ = periodogram_peak(r)
    axs[0].semilogy(a, P, lw=.8, label=f'{nm} (peak {pk:.3f})')
    axs[1].plot(np.arange(tau.size)[::50], np.abs(np.cumsum(np.exp(1j * x) - np.exp(1j * gam)))[::50], lw=.8, label=nm)
axs[0].set_xlabel('ordinal frequency alpha'); axs[0].set_title('periodogram of the ordinal residual (test set)')
axs[1].set_xlabel('index in test set'); axs[1].set_title('|walk(x) - walk(gamma)| on the test set')
[a.legend(fontsize=8) for a in axs]; [a.grid(alpha=.3) for a in axs]
fig.tight_layout(); fig.savefig('outputs/task3_comparison.png', dpi=130)
print(json.dumps(dict(info=info, methods=rows), indent=2))
