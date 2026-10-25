# Effect of close pairs on the ordinate centroid C_N(1) = sum_{k<=N} (1-(k-1)/N) e^{i gamma_k}.
# Experiment: spread every close pair (unfolded gap s<S0) symmetrically about its midpoint to unfolded gap 1
# (clipped so the order with the neighbours is kept), all other zeros unchanged; compare C_N and the partial sums.
# Also: Landau-Gonek check of the unconditional phase bias. Only k < 1 400 737 (test set untouched).
import os, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(HERE, 'opc_gaps_eval.py')).read().split("files = sorted")[0])
K = TEST_FIRST_K - 1
g = gam_all[:K].astype(np.float64); t = tau_all[:K]
s = clock_diff(g[1:], t[:-1]) - clock_diff(g[:-1], t[:-1])          # unfolded gaps
Lam = np.log(g / (2 * np.pi)) / (2 * np.pi)                          # density
def centroid(x, N):
    w = 1 - np.arange(N) / N
    return np.sum(w * np.exp(1j * x[:N]))
def partial(x):
    return np.cumsum(np.exp(1j * x))
out = []
C0 = {N: centroid(g, N) for N in (10**4, 10**5, 10**6, K)}
out.append("RH limit e^{-1/2}V_+(1) = 0.77689426079 + 0.76785566886 i")
for S0 in (0.15, 0.30):
    h = g.copy(); idx = np.where(s < S0)[0]
    idx = idx[np.diff(np.r_[-2, idx]) > 1]                           # disjoint pairs only
    for k in idx:
        m = 0.5 * (g[k] + g[k + 1]); half = 0.5 / Lam[k]
        lo = g[k - 1] if k > 0 else -np.inf; hi = g[k + 2] if k + 2 < K else np.inf
        h[k] = max(m - half, 0.5 * (lo + m)); h[k + 1] = min(m + half, 0.5 * (m + hi))
    out.append(f"\nspread pairs s<{S0}: {len(idx)} pairs moved")
    for N in (10**4, 10**5, 10**6, K):
        c1 = centroid(h, N); out.append(f"  N={N:8d}  C(gamma)={C0[N].real:+.5f}{C0[N].imag:+.5f}i   C(spread)={c1.real:+.5f}{c1.imag:+.5f}i   |diff|={abs(c1-C0[N]):.4f}")
    P0, P1 = partial(g), partial(h)
    out.append(f"  max|partial sum| up to K: gamma {np.abs(P0).max():.3f}   spread {np.abs(P1).max():.3f}   final |S_K|: {abs(P0[-1]):.3f} vs {abs(P1[-1]):.3f}")
# Landau-Gonek prediction of unconditional bias E[cos(gamma log p)] = -(log p/sqrt p)/log(T/2pi) (heuristic per-zero normalisation)
out.append("\nLandau-Gonek check on k<K: mean cos(gamma log p) vs -(log p/sqrt p) * (T/2pi)/N(T) over window")
T1, T0 = g[-1], g[0]
for p in (2, 3, 5, 7, 11, 13):
    meas = np.cos(g * np.log(p)).mean()
    pred = -(np.log(p) / np.sqrt(p)) * ((T1 - T0) / (2 * np.pi)) / K
    out.append(f"  p={p:2d}  measured {meas:+.4f}   predicted {pred:+.4f}")
txt = "\n".join(out); print(txt)
open(os.path.join(HERE, 'outputs', 'centroid_pairs.txt'), 'w').write(txt + "\n")
