#!/usr/bin/env python3
"""Onset of the cross term Cr_X at the clock points (ordinal_prime_cutoff_v13, Section 9).

Usage:  python3 opc_resonance_v13.py DATA_DIR [OUT_DIR]

Top window of ordinals (10^6, K].  (1) Cr_X = <S_X(tau_k)^2> - v_X with full local factors, and the same for the
prime part S^(1) alone, for a grid of cutoffs X.  (2) For the prime part S^(1)(t) = sum_{p<=1999} a_p sin(t log p), a_p = -1/(pi sqrt p), the cross
term Cr^(1) = sum_{p,q} a_p a_q (<sin(tau log p) sin(tau log q)> - [p=q]/2) is split into the ordered pairs with
p q in [tau_min/2pi, tau_max/2pi] (resonant) and the others; the stationary-phase value
sum_{resonant ordered pairs} log(pq) / (2 pi^2 #I) is printed for comparison (heuristic).
Output: OUT_DIR/table_I_cross_term_onset.csv, table_I_resonance.json.  No parameter is fitted.
"""
import csv
import json
import os
import sys

import numpy as np

DATA = sys.argv[1] if len(sys.argv) > 1 else "data"
OUT = sys.argv[2] if len(sys.argv) > 2 else "outputs"
os.makedirs(OUT, exist_ok=True)
tau = np.fromfile(os.path.join(DATA, "zLamb.bin"), "<f8")
K = len(tau)
tt = tau[10 ** 6:]                      # indices k = 10^6+1, ..., K
nI = len(tt)


def primes(n):
    sv = np.ones(n + 1, bool)
    sv[:2] = False
    for p in range(2, int(n ** 0.5) + 1):
        if sv[p]:
            sv[p * p::p] = False
    return np.flatnonzero(sv)


P = primes(1999)
grid = [100, 200, 250, 300, 316, 350, 400, 500, 700, 907, 1200, 1999]
S = np.zeros(nI)
S1 = np.zeros(nI)
v = 0.0
v1 = 0.0
rows = []
gi = 0
for idx, p in enumerate(P):
    lp = np.log(p)
    m = 1
    while p ** (-m / 2) > 1e-17:
        a = -1.0 / (np.pi * m * p ** (m / 2))
        term = a * np.sin(m * lp * tt)
        S += term
        v += 0.5 * a * a
        if m == 1:
            S1 += term
            v1 += 0.5 * a * a
        m += 1
    nxt = P[idx + 1] if idx + 1 < len(P) else np.inf
    while gi < len(grid) and grid[gi] < nxt:
        rows.append(dict(X=grid[gi], n_primes=int(np.sum(P <= grid[gi])), mean_S2=f"{np.mean(S * S):.6f}",
                         v_X=f"{v:.6f}", Cr_X=f"{np.mean(S * S) - v:.6f}",
                         Cr1_X_primes_only=f"{np.mean(S1 * S1) - v1:.6f}"))
        gi += 1
with open(os.path.join(OUT, "table_I_cross_term_onset.csv"), "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)
for r in rows:
    print(r)

# (2) prime part, pair decomposition through the Gram matrix of the sine vectors
lp = np.log(P.astype(float))
G = np.zeros((len(P), len(P)))
step = 50000
for i0 in range(0, nI, step):
    blk = np.sin(np.outer(lp, tt[i0:i0 + step]))
    G += blk @ blk.T
G /= nI
a = -1.0 / (np.pi * np.sqrt(P.astype(float)))
M = np.outer(a, a) * (G - 0.5 * np.eye(len(P)))
U1, U2 = tt.min() / (2 * np.pi), tt.max() / (2 * np.pi)
PQ = np.outer(P.astype(float), P.astype(float))
res = (PQ >= U1) & (PQ <= U2)
pred = float(np.sum(np.log(PQ[res])) / (2 * np.pi ** 2 * nI))
out = dict(window="(10^6, K]", n_indices=nI, tau_over_2pi_range=[float(U1), float(U2)], X=1999, n_primes=len(P),
           Cr1_total=float(M.sum()), Cr1_resonant_pairs=float(M[res].sum()), Cr1_nonresonant=float(M[~res].sum()),
           n_resonant_ordered_pairs=int(res.sum()), n_nonresonant_ordered_pairs=int((~res).sum()),
           stationary_phase_value_heuristic=pred, sqrt_tau_min_over_2pi=float(np.sqrt(U1)))
with open(os.path.join(OUT, "table_I_resonance.json"), "w") as fh:
    json.dump(out, fh, indent=1)
print(json.dumps(out, indent=1))
