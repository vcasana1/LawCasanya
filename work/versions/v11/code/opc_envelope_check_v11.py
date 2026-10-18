#!/usr/bin/env python3
"""Finite-height envelopes of delta_k = tau_k - gamma_k (ordinal_prime_cutoff_v11, Proposition 8.x).

Usage:  python3 opc_envelope_check_v11.py DATA_DIR [OUT_DIR]

For every index k:
  (i)  |s_k - varpi(gamma_k)/pi| <= max |S(gamma_k^+-)| - 1/2, and Bellotti-Wong (Cor. 1.5, eq. (1.2)) give
       |S(t)| <= B_S(t) for t >= e and |S(t)| <= 2.5167 for 0 <= t <= 30 610 046 000;
  (ii) -E/L(tau_k) <= delta_k <= E/L(gamma_k) with E = B - 1/2 + |varpi(gamma_k)|/pi.
varpi(t) = 1/(48 t) + 7/(5760 t^3) + O(t^-5) is evaluated by this expansion (|error| < 1e-12 for t > 14).
Output: OUT_DIR/check_envelope_S.csv.  No parameter is fitted.
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
N0 = g / (2 * np.pi) * np.log(g / (2 * np.pi * np.e)) + 7 / 8
s = k - 0.5 - N0
d = tau - g
Lg = np.log(g / (2 * np.pi)) / (2 * np.pi)
Lt = np.log(tau / (2 * np.pi)) / (2 * np.pi)
varpi = 1 / (48 * g) + 7 / (5760 * g ** 3)
BS = 0.10076 * np.log(g) + np.minimum(0.24460 * np.log(np.log(g)) + 7.20844, 1.68845 * np.log(np.log(g)) + 1.50956)
assert g[-1] <= 30610046000
BP = np.full(K, 2.5167)
BWN = 0.10076 * np.log(g) + 0.24460 * np.log(np.log(g)) + 8.08344
rows = []
for name, B in (("Platt range 2.5167", BP), ("Bellotti-Wong Cor 1.5", BS)):
    E = B - 0.5 + np.abs(varpi) / np.pi
    up, lo = E / Lg, -E / Lt
    ok_s = bool(np.all(np.abs(s - varpi / np.pi) <= B - 0.5))
    ok_d = bool(np.all((d <= up) & (d >= lo)))
    rows.append(dict(envelope=name, sandwich_ok=ok_s, displacement_ok=ok_d,
                     max_abs_s=f"{np.max(np.abs(s)):.6f}", max_ratio_abs_s_over_E=f"{np.max(np.abs(s) / E):.4f}",
                     max_delta_over_upper=f"{np.max(d / up):.4f}", max_minus_delta_over_lower=f"{np.max(d / lo):.4f}",
                     upper_at_k34=f"{up[33]:.4f}", lower_at_k34=f"{lo[33]:.4f}",
                     upper_at_K=f"{up[-1]:.4f}", lower_at_K=f"{lo[-1]:.4f}"))
old_up, old_lo = (BWN - 11 / 8) / Lg, -(BWN + 3 / 8) / Lt
rows.append(dict(envelope="v8 (N-bound) for comparison", sandwich_ok=bool(np.all((s >= -BWN - 3 / 8) & (s <= BWN - 11 / 8))),
                 displacement_ok=bool(np.all((d <= old_up) & (d >= old_lo))), max_abs_s=f"{np.max(np.abs(s)):.6f}",
                 max_ratio_abs_s_over_E="", max_delta_over_upper=f"{np.max(d / old_up):.4f}",
                 max_minus_delta_over_lower=f"{np.max(d / old_lo):.4f}", upper_at_k34=f"{old_up[33]:.4f}",
                 lower_at_k34=f"{old_lo[33]:.4f}", upper_at_K=f"{old_up[-1]:.4f}", lower_at_K=f"{old_lo[-1]:.4f}"))
with open(os.path.join(OUT, "check_envelope_S.csv"), "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)
for r in rows:
    print(r)
j = int(np.argmax(np.abs(s)))
print(f"max |s_k| = {abs(s[j]):.6f} at k = {j + 1}, gamma = {g[j]:.6f}, delta = {d[j]:.6f}")
