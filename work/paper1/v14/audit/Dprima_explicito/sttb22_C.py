"""Constant C(eps,k,x0) of Theorem 5 of Simonic-Trudgian-Turnage-Butterbaugh,
Trans. AMS 375 (2022) [arXiv:2010.10675v1, eqs. (17)-(21)], evaluated in exact
closed form with mpmath. L = L0 = 642.86 (their Lemma 1)."""
from mpmath import mp, mpf, pi, e, sqrt, log, factorial
mp.dps = 40
a0 = mpf('1.5453'); L = mpf('642.86')
a1 = 13 + mpf(26)/(10*pi) + mpf(13)/(3*pi*e)
def a2(x0): return mpf(13)/2 + mpf(18)/(10*pi) + mpf(13)/(6*pi*e) + 2/log(x0)*(52 + mpf(124)/(10*pi) + mpf(52)/(3*pi*e))
def a3(x0): return 3*pi*a1/2 + mpf(139)/75 + 62*pi*a1/(75*log(x0))
def a4(x0, eps, k): return 1 + eps/k*(log(2)/log(x0) + a3(x0)/(pi*a2(x0)))
def C(eps, k, x0):
    A2, A4 = a2(x0), a4(x0, eps, k)
    q = 1 + 8*a0*L/eps
    R1 = 8*a0*L/eps*(8*eps)**(2*k)*factorial(2*k)/mpf(k)**(2*k-1) + (3*eps/(2*pi*A2*A4*sqrt(2*k)))**(2*k)*(13 + mpf(k)/18)
    R2 = sqrt(13)*((12*e)**2*a1*eps/(A2*A4*sqrt(k)))**(2*k)*sqrt(q*(8*eps/e)**(8*k)*factorial(8*k)/mpf(k)**(8*k-1))
    R3 = sqrt(13)*(24*e**2*eps/(pi*A2*A4*sqrt(k)))**(2*k)*sqrt(q*(8*eps/e**2)**(4*k)*factorial(4*k)/mpf(k)**(4*k-1))
    R4 = sqrt(13)*(6*a1*eps/(A2*A4*sqrt(k)))**(2*k)*(1 + 8*a0*L/eps*(8*eps)**(4*k)*factorial(4*k)/mpf(k)**(4*k-1))
    main = (12*A2*A4*k/eps)**(2*k)/6
    return main*(1+R1+R2+R3+R4), main, (R1, R2, R3, R4)
eps = mpf(1)/88
# check against their Corollary 2 (x0 = e^{20000}): C(1/88,1) < 1.44161e11, C(1/88,2) < 2.69927e21
for k in (1, 2):
    print('check x0=e^20000 k=%d: C=%s' % (k, mp.nstr(C(eps, k, e**20000)[0], 8)))
for k in (2, 3, 4):
    c, m, R = C(eps, k, e**16)
    print('x0=e^16 k=%d: C=%s  main=%s  T >= e^%d' % (k, mp.nstr(c, 6), mp.nstr(m, 6), 1408*k), ' R=', [mp.nstr(r, 3) for r in R])
