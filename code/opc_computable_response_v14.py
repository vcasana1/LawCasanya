#!/usr/bin/env python3
"""Computable and residual parts of the prime responses at the clock points (ordinal_prime_cutoff_v14, Section 11.4).

Usage:  python3 opc_computable_response_v14.py DATA_DIR [OUT_DIR]

Window T = 2^19 < gamma_k <= 2T.  For cutoff exponents (c_1, c_2, c_3) and the Newton points x^(m) of
opc_iteration_v14.py, and for primes p:
  R_tau   = -2 pi sqrt(p) < s_k sin(tau_k log p) >,                  s_k = L(tau_k)(tau_k - gamma_k);
  A_m     = -2 pi sqrt(p) < L(tau_k)(tau_k - x^(m)_k) sin(tau_k log p) >   (computable, no zeros);
  D_m     = -2 pi sqrt(p) < S_{X_m}(tau_k) sin(tau_k log p) >            (diagonal part);
  B_m     = A_m - D_m   (response of the transport S_{X_m}(x^(m-1)) - S_{X_m}(tau_k));
  E_m     = R_tau - A_m (response of the residual L(tau_k)(x^(m)_k - gamma_k)).
The column 'res' marks p X_m >= T/(2 pi), where the frequencies log(np), n <= X_m, reach the stationary band
of the clock (Proposition 8.15) and D_m is no longer small.  Output: OUT_DIR/table_L_computable_response.csv.
No parameter is fitted.
"""
import csv
import os
import sys

import numpy as np

DATA = sys.argv[1] if len(sys.argv) > 1 else "data"
OUT = sys.argv[2] if len(sys.argv) > 2 else "outputs"
os.makedirs(OUT, exist_ok=True)
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


T = 2.0 ** 19
sel = (g > T) & (g <= 2 * T)
gg, tt, kk = g[sel], tau[sel], k[sel]
M = len(gg)
LT = np.log(T / (2 * np.pi))
s = L(tt) * (tt - gg)
plist = [3, 7, 31, 101, 211, 1009, 2003, 10007, 20011, 50021, 100003, 131101]


def resp(v, p):
    return -2 * np.pi * np.sqrt(p) * np.mean(v * np.sin(tt * np.log(p)))


rows = []
for cs in ((1 / 10, 1 / 5, 1 / 3), (1 / 5, 1 / 3, 1 / 2), (1 / 3, 1 / 2, 1 / 2)):
    x = [tt.copy()]
    Xs, ph_tau = [], []
    for c in cs:
        X = int(T ** c)
        P = primes(X)
        Xs.append(X)
        ph_tau.append(phase(tt, P))
        xp = x[-1]
        x.append(xp - (N0(xp) + phase(xp, P) - (kk - 0.5)) / L(xp))
    Y = [L(tt) * (tt - x[m]) for m in (1, 2, 3)]
    for p in plist:
        row = dict(c1=f"{cs[0]:.4f}", c2=f"{cs[1]:.4f}", c3=f"{cs[2]:.4f}", X1=Xs[0], X2=Xs[1], X3=Xs[2],
                   p=p, theta=f"{np.log(p) / LT:.4f}", R_tau=f"{resp(s, p):.4f}")
        for m in (1, 2, 3):
            A = resp(Y[m - 1], p)
            D = resp(ph_tau[m - 1], p)
            row[f"A{m}"] = f"{A:.4f}"
            row[f"D{m}"] = f"{D:.4f}"
            row[f"B{m}"] = f"{A - D:.4f}"
            row[f"E{m}"] = f"{resp(s, p) - A:.4f}"
            row[f"res{m}"] = int(p * Xs[m - 1] >= T / (2 * np.pi))
        rows.append(row)
        print(row)
with open(os.path.join(OUT, "table_L_computable_response.csv"), "w", newline="") as fh:
    wr = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
    wr.writeheader()
    wr.writerows(rows)
