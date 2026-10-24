"""
Appendix A.3 -- No-finite-jet perturbation confirmation (Proposition 14.1 / Remark 14.2).
Reproduces the 46.9 vs 49.0 comparison confirming the obstruction persists
after matching N=6 derivatives at the zero.
"""
import sympy as sp

qv = sp.Symbol('q')
qg = sp.Rational(1, 3)

# a concrete real-analytic F_beta with a simple zero at q=q_gamma
Fbeta = (qv - qg)*sp.sin(3*qv + 1) + (qv - qg)**2*sp.exp(qv)
# an unrelated reference F_{1/2,n}
Fhalf = sp.cos(2*qv) + qv**2

# best-fit C matching fourth derivatives at q_gamma
C_val = sp.diff(Fbeta, qv, 4).subs(qv, qg) / sp.diff(Fhalf, qv, 4).subs(qv, qg)
D4_original = sp.simplify(sp.diff(Fbeta - C_val*Fhalf, qv, 4))
probe_point = qg + sp.Rational(1, 10)
val_original = float(D4_original.subs(qv, probe_point))
print(f"D_q^4(F_beta - C*F_half) at probe point, BEFORE perturbation: {val_original}")

# perturb: agree with F_beta to order N=6 at q_gamma, arbitrary G elsewhere
G = sp.sin(5*qv) + 2
N = 6
Fbeta_tilde = Fbeta + (qv - qg)**(N+1)*G

print("\nDerivative agreement check (orders 0..N, must all be 0):")
for j in range(N+1):
    diff_j = sp.simplify(sp.diff(Fbeta_tilde - Fbeta, qv, j).subs(qv, qg))
    print(f"  order {j}: {diff_j}")

C_val_tilde = sp.diff(Fbeta_tilde, qv, 4).subs(qv, qg) / sp.diff(Fhalf, qv, 4).subs(qv, qg)
D4_tilde = sp.simplify(sp.diff(Fbeta_tilde - C_val_tilde*Fhalf, qv, 4))
val_tilde = float(D4_tilde.subs(qv, probe_point))
print(f"\nD_q^4(F_beta_tilde - C_tilde*F_half) at same point, AFTER perturbation: {val_tilde}")
print(f"Still generic/nonzero despite sharing 6 derivatives? {abs(val_tilde) > 1e-6}")
