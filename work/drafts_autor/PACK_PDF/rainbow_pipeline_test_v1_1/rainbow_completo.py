import mpmath as mp
import numpy as np
from numpy.polynomial import legendre as Leg

mp.mp.dps = 20

print("="*70)
print("PASO 1: elegir el lobulo n=8 (mismo de siempre en este hilo)")
print("="*70)
g8 = mp.mpf('43.327073281'); g9 = mp.mpf('48.005150881')
print(f"gamma_8={float(g8)}  gamma_9={float(g9)}")

print()
print("="*70)
print("PASO 2: Omega_n = theta(gamma_9)-theta(gamma_8), theta'>0 en el rango")
print("="*70)
theta_g8 = mp.siegeltheta(g8); theta_g9 = mp.siegeltheta(g9)
Omega = theta_g9 - theta_g8
thetap_mid = mp.mpf('0.5')*mp.log((g8+g9)/2/(2*mp.pi))
print(f"Omega_8={float(Omega):.6f}   theta'(punto medio)={float(thetap_mid):.6f} (>0, confirmado)")

print()
print("="*70)
print("PASO 3: coordenada de fase t_n(q), theta(t_n(q))=theta(g8)+Omega*q")
print("="*70)
def t_of_q(q):
    target = theta_g8 + Omega*mp.mpf(q)
    t = g8 + q*(g9-g8)
    for _ in range(6):
        f = mp.siegeltheta(t) - target
        fp = mp.mpf('0.5')*mp.log(t/(2*mp.pi))
        t = t - f/fp
    return t
for q in [0.0, 0.25, 0.5, 0.75, 1.0]:
    print(f"  q={q}:  t_n(q)={float(t_of_q(q)):.6f}")

print()
print("="*70)
print("PASO 4: arco critico rotado, Z_hat_0(q)=r_n(q)*e^(-i*Omega*q), verificacion directa")
print("="*70)
Z0 = mp.siegelz(g8+mp.mpf('1e-6'))  # signo de Z justo despues de g8
eps_n = 1 if Z0 > 0 else -1
def Zhat0(q):
    t = t_of_q(q)
    return eps_n*mp.e**(1j*theta_g8)*mp.zeta(mp.mpf('0.5')+1j*t)
q_test = mp.mpf('0.37')
lhs = Zhat0(q_test)
r_n = abs(mp.siegelz(t_of_q(q_test)))
rhs = r_n*mp.e**(-1j*Omega*q_test)
print(f"  q=0.37:  Z_hat_0(q) directo = {complex(lhs)}")
print(f"           r_n(q)*e^(-iOmega q) = {complex(rhs)}")
print(f"           diferencia = {float(abs(lhs-rhs)):.2e}")

print()
print("="*70)
print("PASO 5: familia Rainbow W_sigma(q)=zeta(sigma+it_n(q)), sigma=1/2..1")
print("="*70)
NQ = 61
qs = [mp.mpf(i)/(NQ-1) for i in range(NQ)]
ts_grid = [t_of_q(q) for q in qs]
sigmas = np.linspace(0.5, 1.0, 26)

def W(sigma):
    return np.array([complex(mp.zeta(mp.mpf(sigma)+1j*t)) for t in ts_grid])

W_cache = {s: W(s) for s in sigmas}
print(f"  calculada para {len(sigmas)} valores de sigma, {NQ} puntos de q cada una")

print()
print("="*70)
print("PASO 6: proyeccion Q_perp (base de Legendre, quitar grado <=3)")
print("="*70)
qf = np.array([float(q) for q in qs])
def legendre_shifted(m, x):
    c = np.zeros(m+1); c[m]=1.0
    return Leg.legval(2*x-1, c)*np.sqrt(2*m+1)
phi03 = np.array([legendre_shifted(m, qf) for m in range(4)])

def Qperp(vals):
    coefs = [np.trapezoid(vals*phi03[m], qf) for m in range(4)]
    proj = sum(c*phi03[m] for m,c in enumerate(coefs))
    return vals - proj

u_cache = {s: Qperp(W_cache[s]) for s in sigmas}
print(f"  u_{{1/2}} tiene norma {np.sqrt(np.trapezoid(np.abs(u_cache[0.5])**2, qf).real):.6f}")

print()
print("="*70)
print("PASO 7: M_n(sigma) = 1 - |<u_{1/2},u_sigma>|^2 / (||u_{1/2}||^2 ||u_sigma||^2)")
print("="*70)
u_half = u_cache[0.5]
norm_half2 = np.trapezoid(np.abs(u_half)**2, qf).real

Mvals = []
for s in sigmas:
    us = u_cache[s]
    inner = np.trapezoid(np.conj(u_half)*us, qf)
    norm_s2 = np.trapezoid(np.abs(us)**2, qf).real
    M = 1 - abs(inner)**2/(norm_half2*norm_s2)
    Mvals.append(M)
Mvals = np.array(Mvals)

print(f"{'sigma':>8} {'M_n(sigma)':>14}")
for s, M in zip(sigmas[::3], Mvals[::3]):
    print(f'{s:8.3f} {M:14.8f}')

print()
print("="*70)
print("PASO 8: verificacion No-Exit -- M_n(1/2)=0 y M_n(sigma)>0 para sigma>1/2 ?")
print("="*70)
print(f"  M_n(1/2) = {Mvals[0]:.2e}  (debe ser 0 exacto)")
print(f"  minimo de M_n(sigma) para sigma>1/2 = {Mvals[1:].min():.8f}")
print(f"  todos estrictamente positivos? {np.all(Mvals[1:]>0)}")

print()
print("="*70)
print("PASO 9: monotonia -- M_n'(sigma)>=0 en todo el rango, para ESTE lobulo?")
print("="*70)
dM = np.gradient(Mvals, sigmas)
print(f"  minimo de M_n'(sigma) = {dM.min():.6f}")
print(f"  algun valor negativo? {np.any(dM<0)}")
if np.any(dM<0):
    idx = np.where(dM<0)[0]
    print(f"  sigma donde M_n' es negativa: {sigmas[idx]}")

np.save('Mvals_rainbow_completo.npy', Mvals)
np.save('sigmas_rainbow_completo.npy', sigmas)
