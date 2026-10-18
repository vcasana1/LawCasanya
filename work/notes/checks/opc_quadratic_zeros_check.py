"""Quadratic part of the walk drift for the ordinates versus the constructions (relative to the clock).
C(x)-C(tau) = sum_k w_k e^{i tau_k}(e^{-i y_k}-1),  y_k = tau_k - x_k;  linear -i y, quadratic -y^2/2.
x = gamma (zeros), zCasanya, and the one-step model y = S_X(tau)/L (X = dyadic third cutoff <= 512).
Slow-mode content: projection of the block trajectory of each quadratic part on that of the pair (71,193).
Run from work/v17/code (uses opc_common_v15)."""
import sys, numpy as np
sys.path.insert(0, '.')
from opc_common_v15 import *
tau = load('zLamb.bin'); gam = load('zeross.bin'); cas = load('zCasanya.bin')
N = tau.size; k = np.arange(1, N + 1.); w = (N - k + 1) / N; Lt = L(tau); E = w * np.exp(1j * tau)
X3 = dyadic_cut(tau, 512)
S1, _ = S_and_dS(tau, X3, need_d=False); y1 = S1 / Lt          # one-step model (N0(tau)=k-1/2)
def parts(y):
    return complex(np.sum(E * (np.exp(-1j * y) - 1))), complex(np.sum(E * (-1j * y))), complex(np.sum(E * (-y ** 2 / 2)))
a71, a193 = 1 / (np.pi * np.sqrt(71)), 1 / (np.pi * np.sqrt(193))
ups = 1 + np.log(71 / 193)
pair = -(a71 * a193 / 4) * w / Lt ** 2 * np.exp(1j * ups * tau) * (X3 >= 193)
edges = np.linspace(0, N, 201).astype(int)
def traj(h): return np.cumsum(np.add.reduceat(h, edges[:-1]))
P = traj(pair)
print('pair (71,193) total contribution: %.3f%+.3fi' % (pair.sum().real, pair.sum().imag))
for nm, y in (('zeros  (y = tau - gamma)', tau - gam), ('zCasanya (y = tau - x)', tau - cas), ('one-step model S_X/L', y1)):
    tot, lin, quad = parts(y)
    Q = traj(E * (-y ** 2 / 2))
    beta = np.vdot(P, Q) / np.vdot(P, P)      # least-squares coefficient of the (71,193) trajectory
    print(f'{nm:26s} total {tot.real:+8.3f}{tot.imag:+8.3f}i  linear {lin.real:+8.3f}{lin.imag:+8.3f}i  '
          f'quadratic {quad.real:+8.3f}{quad.imag:+8.3f}i  |  (71,193)-coefficient of quadratic trajectory {beta.real:+.3f}{beta.imag:+.3f}i')
print('mean of delta^2 * L^2 (zeros): %.4f ; of y^2 L^2 (zCasanya): %.4f' % (np.mean((Lt*(tau-gam))**2), np.mean((Lt*(tau-cas))**2)))
