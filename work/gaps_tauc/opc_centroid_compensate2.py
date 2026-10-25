# Same as opc_centroid_compensate.py but with a nonlinear (Gauss-Newton) compensation: for each merged pair, the six
# nearest other zeros are shifted by real eps_j so that, after factoring e^{iu m},
#   R(u) = sum_j (e^{iu(d_j+eps_j)} - e^{iu d_j}) + 2(1 - cos(u Delta/2)) = 0
# in least squares on a grid u in [0.6, 2.0] (contains the window (log2, log3)).  Only k < 1 400 737.
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
ug = np.linspace(0.6, 2.0, 15)
ref = {u: cen(g, u) for u in U}
out = []
for S0 in (0.15, 0.30):
    idx = np.where(s < S0)[0]; idx = idx[np.diff(np.r_[-10, idx]) > 7]
    idx = idx[(idx >= 3) & (idx + 4 < K)]
    comp = g.copy(); maxshift = 0.0; worst = 0.0
    for k in idx:
        m = 0.5 * (g[k] + g[k + 1]); D = g[k + 1] - g[k]
        comp[k] = comp[k + 1] = m
        J = np.array([k - 3, k - 2, k - 1, k + 2, k + 3, k + 4]); d = g[J] - m
        tgt = -2 * (1 - np.cos(ug * D / 2))
        eps = np.zeros(6)
        for _ in range(8):
            E = np.exp(1j * np.outer(ug, d + eps))
            R = (E - np.exp(1j * np.outer(ug, d))).sum(1) - tgt
            Jm = 1j * ug[:, None] * E
            A = np.vstack([Jm.real, Jm.imag]); b = -np.r_[R.real, R.imag]
            eps += np.linalg.lstsq(A, b, rcond=None)[0]
        comp[J] += eps
        maxshift = max(maxshift, np.max(np.abs(eps)) * Lam[k]); worst = max(worst, np.abs(R).max())
    out.append(f"merge s<{S0:.2f}: {len(idx)} pairs -> double zeros + nonlinear compensation (6 neighbours); "
               f"max shift {maxshift:.2e} spacings; max per-pair residual on grid {worst:.1e}")
    for u in U:
        cc = cen(comp, u); out.append(f"   u={u:.4f}   |dC| merged+compensated {abs(cc-ref[u]):.2e}")
    S = np.cumsum(np.exp(1j * comp)); S0g = np.cumsum(np.exp(1j * g))
    out.append(f"   max|S_n|  gamma {np.abs(S0g).max():.4f}   merged+comp {np.abs(S).max():.4f};   max_n |S_n(comp)-S_n(gamma)| {np.abs(S-S0g).max():.2e}")
    out.append("")
txt = "\n".join(out); print(txt)
open(os.path.join(HERE, 'outputs', 'centroid_compensate2.txt'), 'w').write(txt + "\n")
