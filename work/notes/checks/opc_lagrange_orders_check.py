"""Explicit Lagrange-Buermann points of orders 1..M (input tau_k only, fixed cutoff Y per index) and the
walk drift they produce, on the untouched indices k = 1 400 737 ... 2 001 052.
Equation: N0(x) + S_Y(x) = k - 1/2, S_Y(t) = -sum_{n<=Y} c_n sin(t log n), c_n = 1/(pi m p^{m/2}).
x(a) solves N0(x) + a S_Y(x) = k - 1/2; the order-n point is the Taylor polynomial of x(a) of degree n at a = 1
(= the Lagrange-Buermann partial sum).  Computed with truncated power-series arithmetic per index.
Cutoffs: Y = 16 (Stage A cutoff) and Y = dyadic third cutoff (512 on this range, as zCasanya).
Reference: exact root of the same equation (Newton with true derivative from the order-M point).
Ordinates are read only to evaluate.  Run from work/v17/code."""
import sys, numpy as np
sys.path.insert(0, '.')
from opc_common_v15 import *
M = 6
first = 1400736
tau = load('zLamb.bin')[first:]; gam = load('zeross.bin')[first:]
n = tau.size; k = np.arange(first + 1, first + n + 1, dtype=float)
w = (n - np.arange(n)) / n; Ew = w * np.exp(1j * tau)

def mul(A, B):                       # truncated product of series (N, M+1)
    C = np.zeros_like(A)
    for i in range(M + 1):
        C[:, i:] += A[:, [i]] * B[:, :M + 1 - i]
    return C

def compose(der, D):                 # f(x0 + D(a)), der[:, j] = f^{(j)}(x0), D has zero constant term
    R = np.zeros_like(D); P = np.zeros_like(D); P[:, 0] = 1.0; fact = 1.0
    for j in range(M + 1):
        if j > 0:
            P = mul(P, D); fact *= j
        R += der[:, [j]] * P / fact
    return R

# derivatives of N0 at tau: N0' = L, N0^{(j)} = (-1)^j (j-2)!/(2 pi tau^{j-1}) for j >= 2
dN0 = np.zeros((n, M + 1)); dN0[:, 1] = L(tau)
for j in range(2, M + 1):
    dN0[:, j] = (-1) ** j * np.math.factorial(j - 2) / (TWO_PI * tau ** (j - 1)) if hasattr(np, 'math') else 0
import math
for j in range(2, M + 1):
    dN0[:, j] = (-1) ** j * math.factorial(j - 2) / (TWO_PI * tau ** (j - 1))

def S_derivs(t, Y):
    D = np.zeros((t.size, M + 1))
    J = int(np.searchsorted(PP_N, Y.max(), side='right'))
    for jj in range(J):
        mask = Y >= PP_N[jj]
        if not mask.any(): continue
        ang = PP_FREQ[jj] * t
        for d in range(M + 1):
            D[:, d] -= np.where(mask, PP_COEF[jj] * PP_FREQ[jj] ** d * np.sin(ang + d * np.pi / 2), 0.0)
    return D

def lagrange_points(Y):
    dS = S_derivs(tau, Y)
    # solve N0(tau + V(a)) + a S(tau + V(a)) = N0(tau)  for the series V(a) = x(a) - tau
    V = np.zeros((n, M + 1))
    for it in range(M + 1):
        N0V = compose(dN0, V) ; N0V[:, 0] = 0.0          # N0(tau+V) - N0(tau)
        SV = compose(dS, V)
        aSV = np.zeros_like(SV); aSV[:, 1:] = SV[:, :-1]   # a * S(tau+V)
        resid = N0V + aSV
        V = V - resid / dN0[:, [1]]                       # Newton-type update on the series coefficients
        V[:, 0] = 0.0
    pts = [tau + np.sum(V[:, :m + 1], axis=1) for m in range(1, M + 1)]
    return pts

def exact_root(x, Y):
    base = N0(tau) - (k - 0.5)
    for _ in range(30):
        S, dS = S_and_dS(x, Y)
        x = x - (base + clock_diff(x, tau) + S) / (L(x) + dS)
    S, _ = S_and_dS(x, Y)
    ok = np.abs(base + clock_diff(x, tau) + S) < 1e-9
    return x, ok

def report(name, x):
    y = tau - x
    tot = np.sum(Ew * (np.exp(-1j * y) - 1)); lin = np.sum(Ew * (-1j * y)); quad = np.sum(Ew * (-y ** 2 / 2))
    rms = np.sqrt(np.mean((L(tau) * (x - gam)) ** 2))
    print(f'{name:30s} rms {rms:.4f} sp | total {tot.real:+7.3f}{tot.imag:+7.3f}i |{tot:7.3f}| '
          f'linear {lin.real:+7.3f}{lin.imag:+7.3f}i  quadratic {quad.real:+7.3f}{quad.imag:+7.3f}i')

report('zeros (reference)', gam)
for label, Y in (('Y=16', np.full(n, 16.0)), ('Y=dyadic (512)', dyadic_cut(tau, 512))):
    pts = lagrange_points(Y)
    for m, x in enumerate(pts, 1):
        report(f'{label} Lagrange order {m}', x)
    xr, ok = exact_root(pts[-1].copy(), Y)
    print(f'  exact root converged at {ok.mean():.6f}; max |order-{M} - root| on converged = {np.max(np.abs(pts[-1]-xr)[ok]):.3e}')
    report(f'{label} exact root', np.where(ok, xr, pts[-1]))
