# Merge close pairs into double zeros AND compensate by tiny real shifts of neighbouring zeros, so that the
# ordinate centroid is preserved.  Merge pair (g_k, g_k+1) -> double zero at the midpoint m (gap Delta in t).
# Change of sum_j e^{i u gamma_j}:  D(u) = 2 e^{i u m} (1 - cos(u Delta/2)).
# Compensation: shift neighbours g_j (j = k-2, k-1, k+2, k+3) by eps_j, d_j = g_j - m.  To first order in eps:
#   i u e^{i u m} sum_j eps_j e^{i u d_j} = -D(u)  for all u  <=>  moments  M_r = sum_j eps_j d_j^r :
#   M0 = 0, M1 = Delta^2/4, M2 = 0, M3 = Delta^4/32   (Taylor matching in u, exact through u^3, error O(u^5 ...)).
# Only k < 1 400 737.  Reports centroid change at several u and partial sums.
import os, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(HERE, 'opc_gaps_eval.py')).read().split("files = sorted")[0])
K = TEST_FIRST_K - 1
g = gam_all[:K].astype(np.float64); t = tau_all[:K]
s = clock_diff(g[1:], t[:-1]) - clock_diff(g[:-1], t[:-1])
Lam = np.log(g / (2 * np.pi)) / (2 * np.pi)
def cen(x, u, N=K):
    w = 1 - np.arange(N) / N; return np.sum(w * np.exp(1j * u * x[:N]))
U = (0.7, 0.8, 0.9163, 1.0, 1.05, 1.5, 2.0)
ref = {u: cen(g, u) for u in U}
out = []
for S0 in (0.15, 0.30):
    idx = np.where(s < S0)[0]; idx = idx[np.diff(np.r_[-10, idx]) > 5]        # pairs with untouched neighbours
    idx = idx[(idx >= 2) & (idx + 3 < K)]
    merged = g.copy(); comp = g.copy(); maxshift = 0.0
    for k in idx:
        m = 0.5 * (g[k] + g[k + 1]); D = g[k + 1] - g[k]
        merged[k] = merged[k + 1] = m; comp[k] = comp[k + 1] = m
        J = np.array([k - 2, k - 1, k + 2, k + 3]); d = g[J] - m
        A = np.vstack([d ** r for r in range(4)]); b = np.array([0.0, D ** 2 / 4, 0.0, D ** 4 / 32])
        eps = np.linalg.solve(A, b); comp[J] += eps
        maxshift = max(maxshift, np.max(np.abs(eps)) * Lam[k])
    out.append(f"merge s<{S0:.2f}: {len(idx)} pairs -> double zeros;  max neighbour shift = {maxshift:.2e} spacings")
    for u in U:
        cm, cc = cen(merged, u), cen(comp, u)
        out.append(f"   u={u:.4f}   C(gamma)={ref[u].real:+.6f}{ref[u].imag:+.6f}i   |dC| merged {abs(cm-ref[u]):.2e}   merged+compensated {abs(cc-ref[u]):.2e}")
    for name, x in (('gamma', g), ('merged', merged), ('merged+comp', comp)):
        S = np.cumsum(np.exp(1j * x)); out.append(f"   max|S_n| {name:12s} {np.abs(S).max():.3f}   |S_K| {abs(S[-1]):.3f}")
    out.append("")
txt = "\n".join(out); print(txt)
open(os.path.join(HERE, 'outputs', 'centroid_compensate.txt'), 'w').write(txt + "\n")
