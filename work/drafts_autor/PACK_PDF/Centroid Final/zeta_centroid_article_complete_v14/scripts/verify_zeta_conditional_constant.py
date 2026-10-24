#!/usr/bin/env python3
"""Reproduce the conditional one-sided analytic centroid constant.

This script evaluates the explicit quantities B(x0) and P(x0) used in the
manuscript at x0=1 and sigma=1/2. It does not use a table of zeta zeros.

The mathematical identification of B+P with the ordinal triangular centroid
is a theorem only under the manuscript's stated boundary-interchange/Riesz
compatibility hypothesis (and RH for the pure ordinate phase).
"""
from __future__ import annotations

import mpmath as mp

mp.mp.dps = 70

x0 = mp.mpf(1)
sigma = mp.mpf('0.5')
U = mp.mpf(20)


def theta(t: mp.mpf) -> mp.mpf:
  z = mp.mpf('0.25') + 0.5j*t
  # Continuous branch near positive t; for x0=1 principal loggamma is valid.
  return mp.im(mp.loggamma(z)) - mp.mpf('0.5')*t*mp.log(mp.pi)


def H(t: mp.mpf) -> mp.mpf:
  return 1 + theta(t)/mp.pi


def Hp(t: mp.mpf) -> mp.mpf:
  z = mp.mpf('0.25') + 0.5j*t
  return (mp.mpf('0.5')*mp.re(mp.digamma(z)) - mp.mpf('0.5')*mp.log(mp.pi))/mp.pi


def Hpp(t: mp.mpf) -> mp.mpf:
  z = mp.mpf('0.25') + 0.5j*t
  return -mp.im(mp.polygamma(1, z))/(4*mp.pi)


def continuous_log_zeta(s: mp.mpc) -> mp.mpc:
  # At Im(s)=+/-1 and Re(s)>=1/2 the horizontal ray contains no zeta zero
  # or pole; the principal value agrees with continuation from Re(s)>>1
  # for this numerical evaluation.
  return mp.log(mp.zeta(s))


def primes_upto(n: int) -> list[int]:
  sieve = bytearray(b'\x01')*(n+1)
  sieve[0:2] = b'\x00\x00'
  p = 2
  while p*p <= n:
    if sieve[p]:
      sieve[p*p:n+1:p] = b'\x00' * (((n-p*p)//p)+1)
    p += 1
  return [i for i in range(2,n+1) if sieve[i]]


def euler_product_tail_i2(U: mp.mpf, prime_max: int = 1000, m_max: int = 30) -> mp.mpc:
  """Tail U..infinity of e^u[Log zeta(sigma+u+ix0)-2^{-s}]du.

  For u>=U use the absolutely convergent Euler expansion
   Log zeta(s) = sum_p sum_{m>=1} p^{-ms}/m.
  The (p,m)=(2,1) term is subtracted in the integrand.
  """
  total = mp.mpc(0)
  for p in primes_upto(prime_max):
    lp = mp.log(p)
    for m in range(1, m_max+1):
      if p == 2 and m == 1:
        continue
      rate = m*lp - 1
      coeff = (mp.power(p, -m*(sigma + 1j*x0)) / m)
      term = coeff * mp.e**(-rate*U) / rate
      total += term
      if abs(term) < mp.mpf('1e-75'):
        break
  return total


# Smooth (Gamma/Riemann-Siegel) contribution.
# We integrate H'' exactly on [x0,x_cut] and use the standard asymptotic
# expansion of theta(t) for the oscillatory tail. This avoids a very slow
# infinite-interval quadrature while keeping the computation transparent.
x_cut = mp.mpf(30)
finite_osc = mp.quad(lambda t: mp.e**(1j*t)*Hpp(t), [x0, 2, 4, 8, 16, x_cut])


def oscillatory_power_tail(p: int, x: mp.mpf, extra_steps: int = 45) -> mp.mpc:
  """J_p(x)=int_x^inf exp(i t)t^{-p}dt by downward recurrence."""
  # Repeated integration by parts gives
  # J_p = i e^{ix} x^{-p} - i p J_{p+1}.
  top = p + extra_steps
  J = mp.mpc(0)
  for q in range(top-1, p-1, -1):
    J = 1j*mp.e**(1j*x)*x**(-q) - 1j*q*J
  return J


tail_osc = oscillatory_power_tail(1, x_cut)/(2*mp.pi)
# theta(t) = main + sum_{n>=1} c_n t^{-(2n-1)}.
# Hence H'' adds c_n(2n-1)(2n)/(pi t^{2n+1}).
for n in range(1, 13):
  c_n = ((-1)**n * mp.bernpoly(2*n, mp.mpf('0.5'))
      / (4*n*(2*n-1)))
  p = 2*n + 1
  coeff = c_n*(2*n-1)*(2*n)/mp.pi
  tail_osc += coeff*oscillatory_power_tail(p, x_cut)

osc = finite_osc + tail_osc
B = mp.e**(1j*x0)*(H(x0) + 1j*Hp(x0)) + 1j*osc

# Arithmetic one-sided contribution.
I1 = mp.quad(lambda u: mp.e**(-u)*continuous_log_zeta(sigma+u-1j*x0), [0, 1, 2, 4, 8, 16, 32, 64])
I2_head = mp.quad(
  lambda u: mp.e**u*(continuous_log_zeta(sigma+u+1j*x0) - mp.power(2, -(sigma+u+1j*x0))),
  [0, 1, 2, 4, 8, 12, 16, U]
)
I2_tail = euler_product_tail_i2(U)
I2 = I2_head + I2_tail
sub = mp.power(2, -(sigma+1j*x0))/(1-mp.log(2))
P = 1j*mp.e**(1j*x0)/(2*mp.pi)*(I1 + I2 - sub)
Cstar = B + P
real_closed = (mp.e - 1/(mp.e**2-1))/(2*mp.sqrt(mp.e))

fmt = lambda z: mp.nstr(z, 50)
print('ZETA CONDITIONAL CENTROID CONSTANT REPRODUCTION')
print('x0         =', fmt(x0))
print('sigma        =', fmt(sigma))
print('Euler-tail split U =', fmt(U))
print('theta-tail x_cut   =', fmt(x_cut))
print('')
print('B(x0)        =', fmt(B))
print('I1          =', fmt(I1))
print('I2 head       =', fmt(I2_head))
print('I2 Euler tail    =', fmt(I2_tail))
print('I2 total       =', fmt(I2))
print('P(x0)        =', fmt(P))
print('C_infty_zeta        =', fmt(Cstar))
print('closed Re(C_infty_zeta)  =', fmt(real_closed))
print('Re difference    =', fmt(mp.re(Cstar)-real_closed))
print('')
print('C_infty_zeta Re      =', mp.nstr(mp.re(Cstar), 30))
print('C_infty_zeta Im      =', mp.nstr(mp.im(Cstar), 30))
