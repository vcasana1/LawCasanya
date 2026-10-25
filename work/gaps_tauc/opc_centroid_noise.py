# Centroid C_N(u) after adding random +-h to every ordinate (independent signs), h = 0.1, 0.01, 0.001. k < 1 400 737.
import os, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(HERE, 'opc_gaps_eval.py')).read().split("files = sorted")[0])
K = TEST_FIRST_K - 1
g = gam_all[:K].astype(np.float64)
w = 1 - np.arange(K) / K
rng = np.random.default_rng(12345)
out = []
for u in (1.0, 0.8):
    c0 = np.sum(w * np.exp(1j * u * g)); out.append(f"u={u}: C(gamma) = {c0.real:+.6f}{c0.imag:+.6f}i")
    for h in (0.1, 0.01, 0.001):
        for rep in range(3):
            x = g + h * rng.choice([-1.0, 1.0], K)
            c = np.sum(w * np.exp(1j * u * x))
            out.append(f"   h=+-{h:<6} rep {rep}:  C = {c.real:+.6f}{c.imag:+.6f}i   |dC| = {abs(c-c0):.4f}   max|S_n| = {np.abs(np.cumsum(np.exp(1j*u*x))).max():.2f}")
txt = "\n".join(out); print(txt)
open(os.path.join(HERE, 'outputs', 'centroid_noise.txt'), 'w').write(txt + "\n")
