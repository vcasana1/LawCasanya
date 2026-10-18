#!/usr/bin/env python3
"""Transport term and Newton second-order term of the one-step clock (ordinal_prime_cutoff_v11, Section 7).

Usage:  python3 opc_transport_v11.py DATA_DIR [OUT_DIR]

Window: T = 2^19, indices with T < gamma_k <= 2T.  For X = T^c, c in {1/5, 1/3, 1/2}, full local factors:
  u_k        = s_k - S_X(gamma_k)                        (ordinal defect)
  t_k        = S_X(gamma_k) - S_X(tau_k)                 (transport term)
  chi_k      = L(tau_k) delta_k - s_k                    (exact second-order term, >= 0)
  r_k        = L(tau_k) (tau_k^X - gamma_k) = u_k + t_k + chi_k
  newton_k   = S_X(tau_k) S_X'(tau_k) / L(tau_k)         (second-order Newton term)
Output: OUT_DIR/table_H_transport.csv and transport_log.txt.  No parameter is fitted.
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
s = k - 0.5 - N0(g)
d = tau - g


def primes(n):
    sv = np.ones(n + 1, bool)
    sv[:2] = False
    for p in range(2, int(n ** 0.5) + 1):
        if sv[p]:
            sv[p * p::p] = False
    return np.flatnonzero(sv)


def phase(x, P, deriv=0):
    out = np.zeros_like(x)
    for p in P:
        lp = np.log(p)
        m = 1
        while p ** (-m / 2) > 1e-17:
            if deriv == 0:
                out += -np.sin(m * lp * x) / (np.pi * m * p ** (m / 2))
            else:
                out += -lp * np.cos(m * lp * x) / (np.pi * p ** (m / 2))
            m += 1
    return out


T = 2.0 ** 19
sel = (g > T) & (g <= 2 * T)
gg, tt, ss, dd = g[sel], tau[sel], s[sel], d[sel]
Lt = L(tt)
rows = []
lines = [f"T=2^19, window size {sel.sum()}"]
for c in (1 / 5, 1 / 3, 1 / 2):
    X = T ** c
    P = primes(int(X))
    Sg, St, Spt = phase(gg, P), phase(tt, P), phase(tt, P, 1)
    u = ss - Sg
    tr = Sg - St
    chi = Lt * dd - ss
    r = Lt * dd - St
    newton = St * Spt / Lt
    ms = lambda v: float(np.mean(v * v))
    row = dict(c=f"{c:.6f}", X=f"{X:.2f}", n_primes=len(P), ms_u=f"{ms(u):.6f}", ms_transport=f"{ms(tr):.6f}",
               corr_u_transport=f"{np.corrcoef(u, tr)[0, 1]:+.4f}", ms_r=f"{ms(r):.6f}",
               max_chi=f"{chi.max():.3e}", min_chi=f"{chi.min():.3e}",
               rms_SXprime_over_L=f"{np.sqrt(ms(Spt / Lt)):.4f}", frac_FXprime_negative=f"{np.mean(Lt + Spt < 0):.5f}",
               ms_newton=f"{ms(newton):.6f}", corr_transport_minus_newton=f"{np.corrcoef(tr, -newton)[0, 1]:+.4f}",
               check_identity_max_abs=f"{np.max(np.abs(r - (u + tr + chi))):.2e}")
    rows.append(row)
    lines.append(str(row))
with open(os.path.join(OUT, "table_H_transport.csv"), "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)
with open(os.path.join(OUT, "transport_log.txt"), "w") as fh:
    fh.write("\n".join(lines) + "\n")
print("\n".join(lines))
