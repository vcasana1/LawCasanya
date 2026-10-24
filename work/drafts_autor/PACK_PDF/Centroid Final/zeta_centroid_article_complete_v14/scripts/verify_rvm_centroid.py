#!/usr/bin/env python3
"""Reproduce the Lambert Riemann-von Mangoldt exponential centroid.

The script constructs the inverse smooth clock
  M(x)=x/(2*pi)*log(x/(2*pi*e))+7/8,
by its exact Lambert-W formula, computes the finite triangular centroid, and
checks the discrete Abel decomposition used in the analytic proof.
"""
from __future__ import annotations

import numpy as np
from scipy.special import lambertw

N = 2_001_052
pi = np.pi
k = np.arange(1, N+2, dtype=np.float64)
x = k - 11.0/8.0
tau = 2*pi*x / lambertw(x/np.e).real
z = np.exp(1j*tau)

# Direct triangular centroid for k=1,...,N.
w = (N - np.arange(1, N+1) + 1)/N
C_direct = np.sum(w*z[:N], dtype=np.complex128)

# Gap/Abel coefficients.
gap = np.diff(tau)            # g_k=tau_{k+1}-tau_k
d = 1.0/(np.exp(1j*gap)-1.0)      # d_k
Dd = np.diff(d)             # d_{k+1}-d_k

first_term = -d[0]*z[0]
raw_series_trunc = first_term - np.sum(Dd*z[1:N], dtype=np.complex128)
boundary_average = np.sum(d[:N]*z[1:N+1], dtype=np.complex128)/N
weighted_series = -np.sum((1.0-np.arange(1,N)/N)*Dd*z[1:N], dtype=np.complex128)
C_abel = first_term + boundary_average + weighted_series

# Verify the inverse clock numerically.
M_tau = tau[:N]/(2*pi)*np.log(tau[:N]/(2*pi*np.e)) + 7.0/8.0
clock_err = M_tau - (np.arange(1,N+1)-0.5)

# Coarse tail diagnostics for the convergent Abel series.
cutoffs = np.array([10_000, 100_000, 500_000, 1_000_000, N], dtype=int)
partials = []
for J in cutoffs:
  ps = first_term - np.sum(Dd[:J-1]*z[1:J], dtype=np.complex128)
  partials.append(ps)

print('LAMBERT RVM EXPONENTIAL CENTROID REPRODUCTION')
print(f'N              = {N}')
print(f'tau_1            = {tau[0]:.15f}')
print(f'tau_N            = {tau[N-1]:.15f}')
print(f'max |M(tau_k)-(k-1/2)|    = {np.max(np.abs(clock_err)):.12e}')
print('')
print(f'C_N direct          = {C_direct.real:+.15f} {C_direct.imag:+.15f}i')
print(f'-d_1 exp(i tau_1)      = {first_term.real:+.15f} {first_term.imag:+.15f}i')
print(f'boundary average       = {boundary_average.real:+.15e} {boundary_average.imag:+.15e}i')
print(f'weighted Abel series     = {weighted_series.real:+.15f} {weighted_series.imag:+.15f}i')
print(f'C_N from Abel identity    = {C_abel.real:+.15f} {C_abel.imag:+.15f}i')
print(f'|direct-Abel|        = {abs(C_direct-C_abel):.12e}')
print('')
print(f'infinite-series truncation N = {raw_series_trunc.real:+.15f} {raw_series_trunc.imag:+.15f}i')
print('partial Abel-series approximants:')
for J, ps in zip(cutoffs, partials):
  print(f' J={J:8d}: {ps.real:+.15f} {ps.imag:+.15f}i')
print('')
print('The analytic theorem in the manuscript proves convergence of the')
print('unweighted Abel series and an O(log J / J) tail at the smooth-clock scale.')
