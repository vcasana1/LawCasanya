#!/usr/bin/env python3
"""Scan of the Backlund disc in Theorem E (floating point, not a certificate).

For a disc with centre sigma_o > 1 and radius rho > sigma_o (Bellotti-Wong, Lemma 2.1),
    a(sigma_o, rho) = 1/(2 pi log(rho/(sigma_o - 1/2))) * int_0^pi e*(sigma_o + rho cos th) dth,
with e* = profile on [1/2,1], 1/2 - s + e(1-s) on [0,1/2), 0 on [1,oo), 1/2 - s on (-oo,0).
The proof of Theorem E takes sigma_o -> 1, rho -> 1.  This program checks numerically that
the infimum over admissible discs is at that corner, for each profile.
Usage: python envelope_disc_scan_v9.py [M] [outdir]
"""
import os, sys
import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize

HERE = os.path.dirname(os.path.abspath(__file__))
argv = sys.argv[:]
sys.argv = [argv[0], argv[1] if len(argv) > 1 else '3000', '/tmp']
src = open(os.path.join(HERE, 'envelope_best_profile_v9.py')).read().split('out = {}')[0]
exec(src)   # defines cases (profiles as rational vertex lists), without printing

def make_e(v):
    xs = np.array([float(a) for a, b in v]); ys = np.array([float(b) for a, b in v])
    def e(s):
        if s >= 1: return 0.0
        if s >= 0.5: return float(np.interp(s, xs, ys))
        if s >= 0: return 0.5 - s + float(np.interp(1 - s, xs, ys))
        return 0.5 - s
    return e

def a(e, s0, r):
    if not (1 <= s0 <= r): return 9.0
    br = sorted(set([0.0, np.pi] + [float(np.arccos(min(1, max(-1, (x - s0) / r)))) for x in (0, 0.5, 1)]))
    I = sum(quad(lambda t: e(s0 + r * np.cos(t)), br[i], br[i + 1], limit=200)[0] for i in range(len(br) - 1))
    return I / (2 * np.pi * np.log(r / (s0 - 0.5)))

lines = []
for name, v in cases.items():
    e = make_e(v)
    lines.append(name)
    for r in [1, 1.05, 1.1, 1.2, 1.5, 2, 3]:
        lines.append('  sigma_o=1  rho=%.2f   2*pi*a = %.9f' % (r, 2 * np.pi * a(e, 1, r)))
    corner = a(e, 1, 1)
    best = None
    for start in ([1.0001, 1.2], [1.05, 1.1], [1.2, 1.5], [1.5, 2.5], [1.01, 1.02]):
        res = minimize(lambda p: a(e, p[0], p[1]), start, method='Nelder-Mead',
                       options={'xatol': 1e-9, 'fatol': 1e-13})
        if best is None or res.fun < best.fun: best = res
    lines.append('  corner (1,1): 2*pi*a = %.9f;  best of 5 Nelder-Mead runs: (%.6f, %.6f), 2*pi*a = %.9f;  below corner by more than 1e-7 (quadrature accuracy): %s'
                 % (2 * np.pi * corner, best.x[0], best.x[1], 2 * np.pi * best.fun, 2*np.pi*(corner - best.fun) > 1e-7))
text = '\n'.join(lines)
print(text)
out = argv[2] if len(argv) > 2 else '.'
open(os.path.join(out, 'envelope_disc_scan_v9.txt'), 'w').write(text + '\n')
