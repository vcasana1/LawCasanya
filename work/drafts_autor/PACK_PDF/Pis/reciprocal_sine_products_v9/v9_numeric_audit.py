"""
v9_numeric_audit.py
Reproduces the key numerical checks reported in Section 12 (Numerical
audit) of "Reciprocal Sine Products and Centered Euclidean Kernels" (v9).
Requires: numpy, scipy, sympy.

Run: python3 v9_numeric_audit.py
"""

import numpy as np
import sympy
from scipy import special, integrate


def psi1(t):
    return special.polygamma(1, 1 + t)


def F(t):
    return special.digamma(1 + t) - special.digamma(1)


# ---------------------------------------------------------------
# 12.1 -- the constant C, and J0, H0, log(pi)+J0+H0 = -C
# ---------------------------------------------------------------
def check_constants():
    print("=== 12.1-12.2: constants C, J0, H0 ===")
    C, _ = integrate.quad(lambda t: -np.log(np.sin(np.pi * t)) * psi1(t),
                           0, 1, limit=400)
    print(f"C = {C:.15f}")

    def h(u):
        if u < 1e-12:
            return 0.0
        return np.log(np.sin(np.pi * u) / (np.pi * u))

    J0, _ = integrate.quad(lambda u: np.log(u) * (psi1(u) + psi1(1 - u)),
                            1e-9, 0.5, limit=300)
    H0, _ = integrate.quad(lambda u: h(u) * (psi1(u) + psi1(1 - u)),
                            1e-9, 0.5, limit=300)
    print(f"J0 = {J0:.15f}")
    print(f"H0 = {H0:.15f}")
    print(f"log(pi)+J0+H0 = {np.log(np.pi)+J0+H0:.15f}   (-C = {-C:.15f})")
    print()


# ---------------------------------------------------------------
# 12.3: exact shifted-divisor count N_p(S), eq. (10.5)
# ---------------------------------------------------------------
def check_NpS(p, Svals):
    print(f"=== 12.3: N_p(S) identity, p={p} ===")
    k_all = np.arange(2, p)
    r_all = p % k_all
    s_all = np.minimum(r_all, k_all - r_all)

    for S in Svals:
        direct = int(np.sum(s_all <= S))
        total = S - 2
        for n in range(p - S, p + S + 1):
            if n > 0:
                total += int(sympy.divisor_count(n))
        for k in range(1, 2 * S + 1):
            total -= (p + S) // k - (p - S - 1) // k
        print(f"  S={S:3d}  direct={direct:5d}  formula={int(total):5d}  "
              f"diff={direct-int(total)}")
    print()


# ---------------------------------------------------------------
# 12.3: corrected gamma factorization for S_p = prod s_k
# ---------------------------------------------------------------
def check_gamma_factorization(p):
    print(f"=== 12.3: gamma factorization of S_p, p={p} ===")
    from math import lgamma
    k_all = np.arange(2, p)
    r_all = p % k_all
    s_all = np.minimum(r_all, k_all - r_all)
    logSp_direct = np.sum(np.log(s_all.astype(float)))

    def a_q(q):
        return p % q

    def branch_counts(q):
        a = a_q(q)
        Xm = (p - 1) // (2 * q + 1)
        Xp = (p - 1) // (2 * q - 1)
        nminus = max(0, 1 + (Xm - a) // q)
        nplus = max(0, 1 + (Xp - (q - a)) // q)
        return nminus, nplus, a

    log_q1 = lgamma(((p - 1) // 3) + 1)
    log_correct = log_q1   # correct: sin/pi, Gamma(n+alpha)Gamma(n+1-alpha)
    log_wrong = log_q1     # wrong:   pi/sin, inverted Pochhammer ratio

    for q in range(2, (p - 1) // 2 + 1):
        nminus, nplus, a = branch_counts(q)
        if nminus == 0 and nplus == 0:
            continue
        alpha = a / q
        term_gamma = lgamma(nminus + alpha) + lgamma(nplus + 1 - alpha)
        sin_val = np.sin(np.pi * alpha)
        common = (nminus + nplus) * np.log(q) + term_gamma
        log_correct += common + np.log(sin_val / np.pi)
        log_wrong += common + np.log(np.pi / sin_val)

    print(f"  log S_p direct        = {logSp_direct:.12f}")
    print(f"  via sin/pi (correct)  = {log_correct:.12f}   "
          f"diff={logSp_direct-log_correct:.3e}")
    print(f"  via pi/sin (wrong)    = {log_wrong:.12f}   "
          f"diff={logSp_direct-log_wrong:.3e}")
    print()


# ---------------------------------------------------------------
# 12.4: exact regular-grid identity for H_p(t), including the
# psi and boundary correction
# ---------------------------------------------------------------
def check_Hp_grid(p, tvals):
    print(f"=== 12.4: H_p(t) regular-grid identity, p={p} ===")
    k_all = np.arange(2, p)
    r_all = p % k_all
    frac = r_all / k_all.astype(float)

    def Ap(t):
        return float(np.sum(frac <= t))

    def Dp(t):
        return Ap(t) - p * F(t) + 2 * t

    def Hp_direct(t):
        return Dp(t) - Dp(1 - t)

    def Hp_grid(t):
        m = np.arange(1, p + 1)
        x1 = (p / (m + t)) % 1.0
        x2 = (p / (m + 1 - t)) % 1.0
        recip = np.sum(x1 - x2)
        psit = p * (special.digamma(p + 2 - t) - special.digamma(p + 1 + t))
        return recip + psit + (4 * t - 2)

    for t in tvals:
        a = Hp_direct(t)
        b = Hp_grid(t)
        print(f"  t={t:.6f}  H_p={a:14.6f}  grid_formula={b:14.6f}  "
              f"diff={a-b:.3e}")
    print()


# ---------------------------------------------------------------
# 12.5: exhaustive folded-discrepancy maxima
# ---------------------------------------------------------------
def exhaustive_Hp_max(p):
    k_all = np.arange(2, p)
    r_all = p % k_all
    frac = r_all / k_all.astype(float)
    ts_sorted = np.sort(np.unique(frac))
    ts_sorted = ts_sorted[(ts_sorted > 0) & (ts_sorted < 0.5)]
    frac_sorted = np.sort(frac)

    def Ap_vec(tv):
        return np.searchsorted(frac_sorted, tv, side='right').astype(float)

    eps = 1e-9
    best = 0.0
    for tv in [ts_sorted, ts_sorted - eps]:
        Ap_t = Ap_vec(tv)
        Ap_1mt = Ap_vec(1 - tv)
        Dp_t = Ap_t - p * F(tv) + 2 * tv
        Dp_1mt = Ap_1mt - p * F(1 - tv) + 2 * (1 - tv)
        Hp = np.abs(Dp_t - Dp_1mt)
        best = max(best, np.max(Hp))
    return best


def check_exhaustive_max(primes):
    print("=== 12.5: exhaustive |H_p| maxima ===")
    print(f"{'p':>8s} {'max|H_p|':>12s} {'/p^(1/3)':>10s} {'/p^(1/3)logp':>14s}")
    for p in primes:
        assert sympy.isprime(p)
        m = exhaustive_Hp_max(p)
        p13 = p ** (1 / 3)
        print(f"{p:8d} {m:12.6f} {m/p13:10.4f} {m/(p13*np.log(p)):14.5f}")
    print()


if __name__ == "__main__":
    check_constants()
    check_NpS(10007, [3, 7, 15, 30, 60])
    check_gamma_factorization(10007)
    check_Hp_grid(10007, [0.1234567, 0.3141592, 0.045])
    check_exhaustive_max([1009, 5003, 10007, 20011, 50021])
