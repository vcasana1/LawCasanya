"""Rebuild the comparison array zCasanya (three Newton steps of the clock equation with dyadic cutoffs
(8, 8, 512) on the prime powers n <= X) from the clock alone, and compare it with the delivered file.

x^(0)_k = tau_k,  x^(j)_k = x^(j-1)_k - (N0(x^(j-1)_k) + S_{X_j}(x^(j-1)_k) - (k - 1/2)) / L(x^(j-1)_k),
X_j = min(Xmax_j, max(8, floor(sqrt(2^floor(log2 tau_k))))),  (Xmax_1, Xmax_2, Xmax_3) = (8, 8, 512),
S_X(t) = -(1/pi) sum_{n = p^m <= X} sin(m t log p) / (m p^{m/2}).
No ordinate is read.  Two clock inputs are used: the certified clock data/zLamb.bin of the paper and the
clock file with which zCasanya.bin was delivered (they differ by at most 2.4e-10).
Writes ../outputs/rebuild_zcasanya_v15.json and .txt (same text as the console).
"""
import json, hashlib, os
import numpy as np
from opc_common_v15 import *

HERE = os.path.dirname(os.path.abspath(__file__))
out = open(os.path.join(HERE, '../outputs/rebuild_zcasanya_v15.txt'), 'w')


def say(s):
    print(s, flush=True)
    out.write(s + '\n')


def build(tau):
    k = np.arange(1, tau.size + 1, dtype=float)
    x = tau.copy()
    for xmax in (8, 8, 512):
        X = dyadic_cut(tau, xmax)
        S, _ = S_and_dS(x, X, need_d=False)
        x = x - (N0(x) - (k - 0.5) + S) / L(x)
    return x


cas = load('zCasanya.bin')
res = {'zCasanya_sha256': hashlib.sha256(cas.astype('<f8').tobytes()).hexdigest()}
for name in ('zLamb.bin', 'zLamb_clock_zCasanya_input.bin'):
    tau = load(name)
    x = build(tau)
    d = np.abs(x - cas)
    res[name] = dict(max_abs_difference=float(d.max()), indices_differing=int((d > 0).sum()),
                     max_relative_to_spacing=float(np.max(d * L(tau))),
                     crossings=int(np.sum(np.diff(x) <= 0)))
    say(f'clock {name}: max |rebuilt - zCasanya| = {d.max():.3e}, differing indices {int((d > 0).sum())}, '
        f'max in units of zeros {np.max(d * L(tau)):.3e}, crossings {int(np.sum(np.diff(x) <= 0))}')
json.dump(res, open(os.path.join(HERE, '../outputs/rebuild_zcasanya_v15.json'), 'w'), indent=2)
out.close()
