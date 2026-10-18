#!/usr/bin/env python3
"""Transport identity in a prime frequency (ordinal_prime_cutoff_v12, Section on the twisted integral).

Usage:  python3 opc_twist_v12.py DATA_DIR [OUT_DIR]

Window T = 2^19 < t <= 2T.  For primes p and w = log p:
  I      = (1/T) int_T^{2T} exp(i w t + i w G(t)/L(t)) dt, computed exactly on every gap of consecutive
           ordinates (G = N - N_0 is k - N_0(t) on the gap (gamma_k, gamma_{k+1}); the integrand is a smooth
           function there and is integrated by adaptive Simpson to relative accuracy 1e-10);
  D      = (2i/T) sum_{k in I_T} sin(w/(2 L(tau_k))) delta_k p^{i tau_k}   (delta_k = tau_k - gamma_k);
  J      = (1/T) sum_k (tau_{k+1} - tau_k) exp(i w v_k), v_k = N_0^{-1}(k) = tau_{k+1/2}  (clock sum, no zeros);
  Rtau   = -2 pi sqrt(p) <s_k sin(tau_k log p)>_{I_T};
  Rw     = weighted response: -2 pi sqrt(p) <b_k s_k sin(tau_k log p)>, b_k = (M/(T L(tau_k))) sin(w/(2L(tau_k)))/sin(pi theta).
Output: OUT_DIR/table_J_twist.csv and twist_log.txt.  No parameter is fitted.
"""
import csv
import os
import sys

import numpy as np
from scipy.special import lambertw

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
T = 2.0 ** 19
i0, i1 = int(np.searchsorted(g, T)), int(np.searchsorted(g, 2 * T))   # gamma[i0] > T, gamma[i1-1] <= 2T
LT = np.log(T / (2 * np.pi))
sel = slice(i0, i1)
M = i1 - i0


def tau_x(x):
    y = x - 11 / 8
    return 2 * np.pi * y / lambertw(y / np.e).real


def gap_integral(a, b, Nv, w):
    """int_a^b exp(i(w t + w (Nv - N0(t))/L(t))) dt on each gap, Simpson with 9 nodes (the phase varies by O(1/T))."""
    nodes = np.linspace(0, 1, 9)
    wts = np.array([1, 4, 2, 4, 2, 4, 2, 4, 1], dtype=float) / 24
    tot = np.zeros(len(a), dtype=complex)
    for u, wt in zip(nodes, wts):
        t = a + (b - a) * u
        tot += wt * np.exp(1j * (w * t + w * (Nv - N0(t)) / L(t)))
    return (b - a) * tot


rows = []
lines = [f"T=2^19, M=#I_T={M}, gaps used {i1 - 1 - i0}"]
a, b = g[i0:i1 - 1], g[i0 + 1:i1]
Nv = np.arange(i0 + 1, i1, dtype=float)             # N(t) on the gap (gamma_{i0+1} ... ) : index i -> N = i+1 (1-based)
vk = tau_x(Nv + 0.5)                                 # v_k = N_0^{-1}(k) = tau_{k+1/2}
for p in (3, 101, 1009, 10007, 100003, 131101):
    w = np.log(p)
    th = w / LT
    I = gap_integral(a, b, Nv, w).sum() / T
    D = 2j * np.sum(np.sin(w / (2 * L(tau[sel]))) * d[sel] * np.exp(1j * w * tau[sel])) / T
    J = np.sum((tau[i0 + 1:i1] - tau[i0:i1 - 1]) * np.exp(1j * w * vk)) / T
    Rt = -2 * np.pi * np.sqrt(p) * np.mean(s[sel] * np.sin(w * tau[sel]))
    bk = (M / (T * L(tau[sel]))) * np.sin(w / (2 * L(tau[sel]))) / np.sin(np.pi * th) if th < 1 else np.full(M, np.nan)
    Rw = -2 * np.pi * np.sqrt(p) * np.mean(bk * s[sel] * np.sin(w * tau[sel]))
    res = 2 * np.pi * np.sqrt(p) / T if T / (2 * np.pi) <= p <= T / np.pi else 0.0
    row = dict(p=p, theta=f"{th:.4f}", Re_I=f"{I.real:+.6e}", Im_I=f"{I.imag:+.6e}", Re_D=f"{D.real:+.6e}", Im_D=f"{D.imag:+.6e}",
               Re_J_clock=f"{J.real:+.6e}", Im_J_clock=f"{J.imag:+.6e}", resonance_2pi_sqrtp_over_T=f"{res:.6e}",
               I_minus_D_minus_J=f"{abs(I - D - J):.2e}", R_tau=f"{Rt:.4f}", R_tau_weighted=f"{Rw:.4f}",
               sin_pi_theta_Rw_over_pi_sqrtp=f"{np.sin(np.pi * th) * Rw / (np.pi * np.sqrt(p)):+.6e}")
    rows.append(row)
    lines.append(str(row))
with open(os.path.join(OUT, "table_J_twist.csv"), "w", newline="") as fh:
    wr = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
    wr.writeheader()
    wr.writerows(rows)
with open(os.path.join(OUT, "twist_log.txt"), "w") as fh:
    fh.write("\n".join(lines) + "\n")
print("\n".join(lines))
