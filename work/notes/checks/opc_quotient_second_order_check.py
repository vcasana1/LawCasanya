"""Explicit point from tau only (test set, dyadic cutoff 512 as zCasanya's third step):
  x1 = tau - S/L                                (Lagrange order 1)
  x2 = x1 + S S'/L^2 - L' S^2/(2 L^3)           (Lagrange order 2, full)
  xq = x1 + Q/L^2 - L' S^2/(2 L^3),  Q = quotient part of S S' = sum_{i,j} c_i c_j f_j/2 sin((f_i - f_j) t)
       (second-order term without the product modes, which the clock sampling aliases at n1 n2 ~ t/(2 pi e)).
Usage: python3 opc_quotient_second_order_check.py [first0 [last0]] (0-based slice; default = test set).
Walk split relative to the clock and RMS vs gamma in mean spacings; zeros read only to evaluate."""
import sys, numpy as np
sys.path.insert(0, '.')
from opc_common_v15 import *
first = int(sys.argv[1]) if len(sys.argv) > 1 else 1400736; last = int(sys.argv[2]) if len(sys.argv) > 2 else None
tau = load('zLamb.bin')[first:last]; gam = load('zeross.bin')[first:last]; cas = load('zCasanya.bin')[first:last]
n = tau.size; w = (n - np.arange(n)) / n; Ew = w * np.exp(1j * tau); Lt = L(tau); Lp = 1 / (TWO_PI * tau)
Y = dyadic_cut(tau, 512)
S, dS = S_and_dS(tau, Y)
J = int(np.searchsorted(PP_N, 512, side='right'))
# quotient part: S S' = sum_ij c_i c_j f_j sin(f_i t) cos(f_j t) = sum_ij c_i c_j f_j/2 [sin((f_i+f_j)t) + sin((f_i-f_j)t)]
Q = np.zeros(n); P = np.zeros(n)
for i in range(J):
    mi = Y >= PP_N[i]
    for j in range(J):
        m = mi & (Y >= PP_N[j])
        cc = PP_COEF[i] * PP_COEF[j] * PP_FREQ[j] / 2
        Q += np.where(m, cc * np.sin((PP_FREQ[i] - PP_FREQ[j]) * tau), 0.0)
        P += np.where(m, cc * np.sin((PP_FREQ[i] + PP_FREQ[j]) * tau), 0.0)
print(f'check S S\' = Q + P: max error {np.max(np.abs(S*dS - Q - P)):.2e}')
x1 = tau - S / Lt
curv = -Lp * S ** 2 / (2 * Lt ** 3)
pts = {'zeros': gam, 'zCasanya': cas, 'order 1': x1, 'order 2 (full)': x1 + S * dS / Lt ** 2 + curv,
       'order 1 + quotient part': x1 + Q / Lt ** 2 + curv}
for nm, x in pts.items():
    y = tau - x
    tot = np.sum(Ew * (np.exp(-1j * y) - 1)); lin = np.sum(Ew * (-1j * y)); quad = np.sum(Ew * (-y ** 2 / 2))
    rms = np.sqrt(np.mean((Lt * (x - gam)) ** 2)); cr = int(np.sum(np.diff(x) <= 0))
    print(f'{nm:26s} rms {rms:.4f} sp  crossings {cr:5d} | total {tot.real:+7.3f}{tot.imag:+7.3f}i  '
          f'|total - zeros| {abs(tot - (np.sum(Ew*(np.exp(1j*(gam-tau))-1)))):6.3f} | linear {lin.real:+8.3f}{lin.imag:+8.3f}i  quadratic {quad.real:+8.3f}{quad.imag:+8.3f}i')
