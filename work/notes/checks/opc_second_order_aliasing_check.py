"""Where the non-slow part of the second-order term B = sum w e^{i tau}(i S S'/L^2) comes from (test set, dyadic 512).
Sampling at the clock is exact Poisson: sum_k g(tau_k) = int g dN0 + sum_{m != 0} int g e^{2 pi i m N0} dN0, so a
mode e^{i(1+F)t} of e^{it} S S' resonates at m = 1 when 1 + F = 2 pi L(t) = log(t/2pi), i.e. for product modes
F = log(n1 n2) with n1 n2 ~ t/(2 pi e).  Computes A and B restricted to these product modes (band: stationary point
inside the window, +-delta).  Run from work/v17/code."""
import sys, numpy as np
sys.path.insert(0, '.')
from opc_common_v15 import *
first = 1400736
tau = load('zLamb.bin')[first:]; n = tau.size
w = (n - np.arange(n)) / n; Ew = w * np.exp(1j * tau); Lt = L(tau)
Y = dyadic_cut(tau, 512)
lo, hi = TWO_PI * Lt.min(), TWO_PI * Lt.max()
print(f'tau range {tau[0]:.0f}..{tau[-1]:.0f}; 2 pi L in [{lo:.4f}, {hi:.4f}]; t/(2 pi e) in [{tau[0]/TWO_PI/np.e:.0f}, {tau[-1]/TWO_PI/np.e:.0f}]')
J = int(np.searchsorted(PP_N, 512, side='right'))
for delta in (0.02, 0.1, 0.3):
    Ap = 0j; Bp = 0j; npairs = 0
    for i in range(J):
        for j in range(J):
            F = PP_FREQ[i] + PP_FREQ[j]
            if lo - delta < 1 + F < hi + delta:
                npairs += 1
                m = (Y >= PP_N[i]) & (Y >= PP_N[j])
                ci, cj = PP_COEF[i], PP_COEF[j]
                s2 = np.where(m, -ci * cj / 2 * np.cos(F * tau), 0.0)      # product part of S^2 (ordered pair share)
                ss = np.where(m, ci * cj * PP_FREQ[j] / 2 * np.sin(F * tau), 0.0)  # product part of S S'
                Ap += np.sum(Ew * (-s2 / (2 * Lt ** 2))); Bp += np.sum(Ew * (1j * ss / Lt ** 2))
    print(f'delta {delta}: ordered pairs {npairs}: A_prod={Ap:.3f}  B_prod={Bp:.3f}')
