"""Walk contributions of the second-order Lagrange terms, evaluated separately at tau_k (test set,
k = 1 400 737 ... 2 001 052), cutoff = dyadic third cutoff (512) of zCasanya and Y=16.
A = sum w e^{i tau} (-S^2/(2L^2)),  B = sum w e^{i tau} (i S S'/L^2),  C = sum w e^{i tau} (-i L' S^2/(2 L^3)).
Continuous prediction: a mode b e^{i d t} of S^2 gives A+B -> -(1+d) b/2 /L^2, i.e. A multiplied by 1+d.
Also: distribution of |S'|/L (the Lagrange series in the parameter a converges at a=1 only if this is < 1 in the
relevant sense), and the same sums restricted to the slow band |1+d| < 0.05 of S^2 built from pair products.
Run from work/v17/code."""
import sys, numpy as np
sys.path.insert(0, '.')
from opc_common_v15 import *
first = 1400736
tau = load('zLamb.bin')[first:]; n = tau.size
w = (n - np.arange(n)) / n; Ew = w * np.exp(1j * tau)
Lt = L(tau); Lp = 1 / (TWO_PI * tau)
for label, Y in (('Y=16', np.full(n, 16.0)), ('Y=dyadic(512)', dyadic_cut(tau, 512))):
    S, dS = S_and_dS(tau, Y)
    A = np.sum(Ew * (-S ** 2 / (2 * Lt ** 2))); B = np.sum(Ew * (1j * S * dS / Lt ** 2))
    C = np.sum(Ew * (-1j * Lp * S ** 2 / (2 * Lt ** 3)))
    r = np.abs(dS) / Lt
    print(f'{label}: A={A:.3f} B={B:.3f} A+B={A+B:.3f} C={C:.2e} | |S\'|/L: median {np.median(r):.3f} '
          f'p99 {np.quantile(r,.99):.3f} max {r.max():.3f} frac>1 {np.mean(r>1):.4f}')
    # slow band of S^2: products of two prime-power terms with |1 + log(n1/n2)| < 0.05 (quotient modes)
    J = int(np.searchsorted(PP_N, Y.max(), side='right'))
    As = 0j; Bs = 0j
    for i in range(J):
        for j in range(J):
            d = PP_FREQ[i] - PP_FREQ[j]
            if abs(1 + d) < 0.05:
                m = (Y >= PP_N[i]) & (Y >= PP_N[j])
                # S = -sum c sin(f t); S^2 contains c_i c_j/2 * cos((f_i - f_j) t) summed over ordered pairs
                ci, cj = PP_COEF[i], PP_COEF[j]
                s2 = np.where(m, ci * cj / 2 * np.cos(d * tau), 0.0)          # ordered pair (i,j) share
                ds2 = np.where(m, -ci * cj / 2 * d * np.sin(d * tau), 0.0)    # its derivative
                As += np.sum(Ew * (-s2 / (2 * Lt ** 2))); Bs += np.sum(Ew * (1j * ds2 / 2 / Lt ** 2))
    print(f'   slow band |1+d|<0.05: A_slow={As:.3f}  B_slow={Bs:.3f}  A_slow+B_slow={As+Bs:.3f}  ratio |A+B|/|A|={abs(As+Bs)/abs(As):.3f}')
