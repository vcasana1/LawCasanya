"""
Appendix A.2 -- g(s)=s-s0 exact zero and transport-equation verification.
Reproduces eq:g-numerical-parameters, eq:g-numerical-zero,
and the h=1e-8 finite-difference check of the transport identity.
"""
import mpmath as mp
mp.mp.dps = 25

g1 = mp.im(mp.zetazero(1))
g2 = mp.im(mp.zetazero(2))
theta_g1 = mp.siegeltheta(g1)
theta_g2 = mp.siegeltheta(g2)
Omega1 = theta_g2 - theta_g1

def t_of_q(q):
    target = theta_g1 + Omega1*mp.mpf(q)
    t = g1 + q*(g2 - g1)
    for _ in range(8):
        f = mp.siegeltheta(t) - target
        fp = mp.mpf('0.5')*mp.log(t/(2*mp.pi))
        t = t - f/fp
    return t

def a_of_q(q):
    t = t_of_q(q)
    thetap = mp.mpf('0.5')*mp.log(t/(2*mp.pi))
    return thetap/Omega1

beta0 = mp.mpf('0.7')
q0 = mp.mpf('0.5')
s0 = beta0 + 1j*t_of_q(q0)
print(f"gamma_1={g1}, gamma_2={g2}, Omega_1={Omega1}")
print(f"s0 = {s0}")

def g(s):
    return s - s0

def G(beta, q):
    return g(beta + 1j*t_of_q(q))

print(f"g(0.7+i*t_1(1/2)) = {G(beta0, q0)}   (must be exactly 0)")

h = mp.mpf('1e-8')
dG_dbeta = (G(beta0+h, q0) - G(beta0-h, q0)) / (2*h)
dG_dq = (G(beta0, q0+h) - G(beta0, q0-h)) / (2*h)
lhs = -1j*a_of_q(q0)*dG_dq
print(f"dG/dbeta                = {complex(dG_dbeta)}")
print(f"-i*a(q)*dG/dq            = {complex(lhs)}")
print(f"residual (discretization only) = {complex(dG_dbeta - lhs)}")
