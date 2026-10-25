# Which rearrangements of close pairs does the centroid "see"?  Only k < 1 400 737.
# A: merge close pairs into double zeros (both at the midpoint).  B: reflect sub-spacing gaps s -> S0 - s.
# C: spread close pairs to unfolded gap 1 (contrast; large-scale change).  Centroid C_N(u) and max partial sums.
import os, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(HERE, 'opc_gaps_eval.py')).read().split("files = sorted")[0])
K = TEST_FIRST_K - 1
g = gam_all[:K].astype(np.float64); t = tau_all[:K]
s = clock_diff(g[1:], t[:-1]) - clock_diff(g[:-1], t[:-1])
Lam = np.log(g / (2 * np.pi)) / (2 * np.pi)
def pairs(S0):
    idx = np.where(s < S0)[0]; return idx[np.diff(np.r_[-2, idx]) > 1]
def modify(kind, S0):
    h = g.copy(); idx = pairs(S0)
    for k in idx:
        m = 0.5 * (g[k] + g[k + 1])
        if kind == 'merge':   new = 0.0
        elif kind == 'reflect': new = (S0 - s[k]) / Lam[k]
        else:                 new = 1.0 / Lam[k]
        lo = g[k - 1] if k > 0 else -np.inf; hi = g[k + 2] if k + 2 < K else np.inf
        h[k] = max(m - new / 2, 0.5 * (lo + m)); h[k + 1] = min(m + new / 2, 0.5 * (m + hi))
    return h, len(idx)
def cen(x, u, N=K):
    w = 1 - np.arange(N) / N; return np.sum(w * np.exp(1j * u * x[:N]))
U = (0.8, 1.0, np.log(2.5))
out = ["u-values: " + ", ".join(f"{u:.4f}" for u in U)]
ref = {u: cen(g, u) for u in U}
out.append("gamma         " + "  ".join(f"C({u:.3f})={ref[u].real:+.4f}{ref[u].imag:+.4f}i" for u in U) +
           f"   max|S|={np.abs(np.cumsum(np.exp(1j*g))).max():.2f}")
for kind, S0 in (('merge', 0.15), ('merge', 0.30), ('merge', 0.50), ('reflect', 0.30), ('reflect', 0.50), ('spread', 0.15)):
    h, n = modify(kind, S0)
    cs = {u: cen(h, u) for u in U}
    out.append(f"{kind:7s} s<{S0:.2f} ({n:6d} pairs)  " + "  ".join(f"|dC({u:.3f})|={abs(cs[u]-ref[u]):.4f}" for u in U) +
               f"   max|S|={np.abs(np.cumsum(np.exp(1j*h))).max():.2f}")
txt = "\n".join(out); print(txt)
open(os.path.join(HERE, 'outputs', 'centroid_subspacing.txt'), 'w').write(txt + "\n")
