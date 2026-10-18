#!/usr/bin/env python3
"""Iterated Newton steps and the local deformation of the second clock (ordinal_prime_cutoff_v13, Section 8).

Usage:  python3 opc_iteration_v13.py DATA_DIR [OUT_DIR]

Window T = 2^19 < gamma_k <= 2T.  For cutoff exponents (c_1, c_2, c_3) the points x^(0) = tau_k,
x^(j) = x^(j-1) - (N_0(x^(j-1)) + S_{X_j}(x^(j-1)) - (k - 1/2)) / L(x^(j-1)), X_j = T^{c_j}, full local factors,
and the errors e_j = x^(j) - gamma_k.  Printed: <(L e_j)^2> for j = 0..3; the fourth moment of the relative
deformation (d_{2,k} - d_{0,k}) / d_{0,k}, d_{j,k} = x^(j)_{k+1} - x^(j)_k; the proportion of inversions d_{2,k} <= 0;
the multiplicity integral  int n~_j(u)^2 du / (b M)  for j = 1, 2 with b = 2 pi / log(3T).
The asymptotic cutoffs c_j = H_{j-1}^{-1/2} are not reachable at this height (c_2 > 1); the rows are illustrations.
Output: OUT_DIR/table_K_iteration.csv.  No parameter is fitted.
"""
import csv
import os
import sys

import numpy as np

DATA = sys.argv[1] if len(sys.argv) > 1 else "data"
OUT = sys.argv[2] if len(sys.argv) > 2 else "outputs"
g = np.fromfile(os.path.join(DATA, "zeross.bin"), "<f8")
tau = np.fromfile(os.path.join(DATA, "zLamb.bin"), "<f8")
K = len(g)
k = np.arange(1, K + 1, dtype=float)
N0 = lambda x: x / (2 * np.pi) * np.log(x / (2 * np.pi * np.e)) + 7 / 8
L = lambda x: np.log(x / (2 * np.pi)) / (2 * np.pi)


def primes(n):
    sv = np.ones(n + 1, bool)
    sv[:2] = False
    for p in range(2, int(n ** 0.5) + 1):
        if sv[p]:
            sv[p * p::p] = False
    return np.flatnonzero(sv)


def phase(x, P):
    out = np.zeros_like(x)
    for p in P:
        lp = np.log(p)
        m = 1
        while p ** (-m / 2) > 1e-17:
            out += -np.sin(m * lp * x) / (np.pi * m * p ** (m / 2))
            m += 1
    return out


def multiplicity(x, b):
    """int n~(u)^2 du / (b M) with n~(u) = #{k : u-b <= x_k <= u} = sum_{j,k} (b - |x_j - x_k|)_+ / (b M)."""
    xs = np.sort(x)
    tot = 0.0
    i = 0
    for j in range(len(xs)):
        while xs[j] - xs[i] > b:
            i += 1
        d = xs[j] - xs[i:j]
        tot += b + 2 * np.sum(b - d)
    return tot / (b * len(xs))


T = 2.0 ** 19
sel = (g > T) & (g <= 2 * T)
gg, tt, kk = g[sel], tau[sel], k[sel]
M = len(gg)
b = 2 * np.pi / np.log(3 * T)
rows = []
for cs in ((1 / 5, 1 / 3, 1 / 2), (1 / 3, 1 / 2, 1 / 2), (1 / 10, 1 / 5, 1 / 3)):
    x = [tt.copy()]
    for c in cs:
        P = primes(int(T ** c))
        xp = x[-1]
        x.append(xp - (N0(xp) + phase(xp, P) - (kk - 0.5)) / L(xp))
    e = [xx - gg for xx in x]
    ms = [float(np.mean((L(tt) * ee) ** 2)) for ee in e]
    d0 = np.diff(x[0])
    d2 = np.diff(x[2])
    rel = (d2 - d0) / d0
    row = dict(c1=f"{cs[0]:.4f}", c2=f"{cs[1]:.4f}", c3=f"{cs[2]:.4f}",
               X1=int(T ** cs[0]), X2=int(T ** cs[1]), X3=int(T ** cs[2]),
               ms_Le0=f"{ms[0]:.5f}", ms_Le1=f"{ms[1]:.5f}", ms_Le2=f"{ms[2]:.5f}", ms_Le3=f"{ms[3]:.5f}",
               deformation_4th_moment=f"{np.mean(rel ** 4):.3e}", deformation_rms=f"{np.sqrt(np.mean(rel ** 2)):.4f}",
               frac_inversions_d2=f"{np.mean(d2 <= 0):.5f}", frac_inversions_d1=f"{np.mean(np.diff(x[1]) <= 0):.5f}",
               mult_x1=f"{multiplicity(x[1], b):.4f}", mult_x2=f"{multiplicity(x[2], b):.4f}", mult_tau=f"{multiplicity(x[0], b):.4f}")
    rows.append(row)
    print(row)
with open(os.path.join(OUT, "table_K_iteration.csv"), "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)
