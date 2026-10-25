# "Landau-Gonek for pairs": test of the diagonal prediction
#   (1/N) sum_gamma cos(gamma log p) sum_{gamma' != gamma} h((gamma'-gamma) Lam)
#      ~ mean_k[ b_p(gamma_k) * ( int h + hhat(alpha_p(gamma_k)) ) ],
#   b_p(t) = -(log p/sqrt p)/log(t/2pi),  alpha_p(t) = log p / log(t/2pi),
# for h(x) = sinc^2(x/a) (hhat(xi) = a (1 - a|xi|)_+ , Fourier support 1/a). a >= 1: Montgomery range (theorem under RH
# up to lower-order terms); a < 1: beyond it. Also hard windows |x| < eps. Only k < 1 400 737.
import os, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(HERE, 'opc_gaps_eval.py')).read().split("files = sorted")[0])
K = TEST_FIRST_K - 1
g = gam_all[:K].astype(np.float64)
L = np.log(g / (2 * np.pi)); Lam = L / (2 * np.pi)
J = 60                                                       # neighbours on each side
def pairsum(hfun):
    acc = np.zeros(K)
    for j in range(1, J + 1):
        x = (g[j:] - g[:-j]) * Lam[:-j]                      # unfolded distance (local density at left point)
        v = hfun(x); acc[:-j] += v; acc[j:] += v
    return acc
out = ["p    window            measured     diagonal-pred   ratio meas/pred   (ratio to Landau bias: meas/b, pred/b)"]
primes = (2, 3, 5, 7, 11, 13)
cosp = {p: np.cos(g * np.log(p)) for p in primes}
bp = {p: -(np.log(p) / np.sqrt(p)) / L for p in primes}
for a in (3.0, 2.0, 1.5, 1.0, 0.7, 0.5, 0.3):
    h = lambda x, a=a: np.sinc(x / a) ** 2
    A = pairsum(h)
    for p in primes:
        meas = np.mean(cosp[p] * A)
        alpha = np.log(p) / L
        hh = a * np.clip(1 - a * alpha, 0, None)
        pred = np.mean(bp[p] * (a + hh))
        bm = np.mean(bp[p])
        out.append(f"{p:2d}  sinc^2 a={a:<4}       {meas:+.5f}     {pred:+.5f}        {meas/pred:6.3f}        ({meas/bm:6.3f}, {pred/bm:6.3f})")
    out.append("")
for eps in (1.0, 0.5, 0.3, 0.15):
    A = pairsum(lambda x, e=eps: (np.abs(x) < e).astype(float))
    for p in primes:
        meas = np.mean(cosp[p] * A); bm = np.mean(bp[p])
        out.append(f"{p:2d}  hard |x|<{eps:<5}      {meas:+.6f}   pair-mass {A.mean():.5f}   meas/b {meas/bm:7.3f}   conditional/b {meas/bm/A.mean():7.2f}")
    out.append("")
txt = "\n".join(out); print(txt)
open(os.path.join(HERE, 'outputs', 'pair_landau.txt'), 'w').write(txt + "\n")
