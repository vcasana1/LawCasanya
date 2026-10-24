"""Exact finite checks for the v12 chapter; not a numerical proof of RH.

Inputs are the retained v11 arrays. Identities are checked with integers
or rational numbers. Explicit B/P_delta Laurent coefficients are evaluated
numerically; these calculations do not continue the full delta function.
"""
from pathlib import Path
from itertools import combinations
from fractions import Fraction
import json
import time
import numpy as np
import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)


def walk(signs):
    R = [0]
    a, b = [], []
    for q, e in enumerate(signs, 1):
        R.append(R[-1] + e)
        (a if e == 1 else b).append(q)
    return R, a, b


def finite_words():
    count = cut_checks = rational_checks = 0
    primes = [0, 2, 3, 5, 7, 11, 13, 17, 19]
    for J in range(1, 9):
        Q = 2 * J
        for plus in combinations(range(Q), J):
            eps = [-1] * Q
            for q in plus:
                eps[q] = 1
            R, a, b = walk(eps)
            d = [y - x for x, y in zip(a, b)]
            assert d == [R[x] + R[y] for x, y in zip(a, b)]
            V = [sum(max(abs(x) - r, 0) for x in d)
                 for r in range(Q + 1)]
            H = max(map(abs, R))
            assert V[0] == sum(map(abs, R[:-1])) >= J
            for r in range(Q + 1):
                twoC = [max(abs(R[q] + R[q + r]) - r, 0)
                        for q in range(Q - r)]
                assert 2 * V[r] == sum(twoC)
                assert V[r] >= H * max(H - r, 0)
                for q, cr in enumerate(twoC):
                    assert abs(cr - max(2 * abs(R[q]) - r, 0)) \
                        <= abs(R[q + r] - R[q])
                cut_checks += len(twoC)
            # Phi(1/2), multiplied by 2**Q: every operation is integral.
            lhs = sum(1 << (Q - abs(x)) for x in d)
            rhs = (J << Q) - (V[0] << (Q - 1))
            rhs += sum(V[r] << (Q - r - 1) for r in range(1, Q))
            assert lhs == rhs
            if count % 997 == 0:
                # A nonuniform physical clock tests the distinction d/Delta.
                clock = [0] + [q*q + 2*q for q in range(1, Q + 1)]
                f = [Fraction(0)] + [Fraction(1, n*n) for n in clock[1:]]
                w = [primes[j] - j for j in range(J + 1)]
                Dw = [0]
                for wj in w[1:]:
                    Dw.append(Dw[-1] + wj)
                paired = sum((w[j] * (f[a[j-1]] - f[b[j-1]])
                              for j in range(1, J + 1)), Fraction(0))
                unit = sum(((Dw[(q+R[q])//2]-Dw[(q-R[q])//2]) *
                            (f[q]-f[q+1]) for q in range(1, Q)),
                           Fraction(0))
                assert paired == unit
                for cutoff in range(1, Q + 1):
                    np_, nm_ = (cutoff+R[cutoff])//2, (cutoff-R[cutoff])//2
                    original = sum((w[j] * f[a[j-1]]
                                    for j in range(1, np_+1)), Fraction(0))
                    original -= sum((w[j] * f[b[j-1]]
                                     for j in range(1, nm_+1)), Fraction(0))
                    complete = sum((w[j] * (f[a[j-1]]-f[b[j-1]])
                                    for j in range(1, min(np_, nm_)+1)),
                                   Fraction(0))
                    boundary = sum((w[j]*f[a[j-1]]
                                    for j in range(nm_+1, np_+1)), Fraction(0))
                    boundary -= sum((w[j]*f[b[j-1]]
                                     for j in range(np_+1, nm_+1)), Fraction(0))
                    assert original == complete + boundary
                    rational_checks += 1
            count += 1
    examples = {}
    for name, word in [("I", "++-+--+-"), ("II", "++--++--")]:
        R, a, b = walk([1 if e == "+" else -1 for e in word])
        ds = [y-x for x, y in zip(a, b)]
        examples[name] = {"word": word, "R": R[1:], "d": ds,
                          "V2": sum(max(abs(d)-2, 0) for d in ds),
                          "quadratic_energy": sum(d*d for d in ds)}
    return {"balanced_words": count, "two_time_point_checks": cut_checks,
            "rational_cutoff_checks": rational_checks, "examples": examples}


def bareiss(matrix):
    """Fraction-free determinant with pivoting, independent of Schur formula."""
    A = [list(map(int, row)) for row in matrix]
    n, prev, sign = len(A), 1, 1
    if n == 0:
        return 1
    for k in range(n - 1):
        if A[k][k] == 0:
            pivot = next((i for i in range(k+1, n) if A[i][k]), None)
            if pivot is None:
                return 0
            A[k], A[pivot] = A[pivot], A[k]
            sign = -sign
        p = A[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                num = A[i][j]*p - A[i][k]*A[k][j]
                assert num % prev == 0
                A[i][j] = num // prev
            A[i][k] = 0
        prev = p
    return sign * A[-1][-1]


def border_matrix(terms, zero_row=None):
    m = len(terms)
    A = [[0] * (2*m+1) for _ in range(2*m+1)]
    for i, t in enumerate(terms):
        k = 2*i
        A[k][k], A[k][k+1] = 2, 3
        A[k+1][k], A[k+1][k+1] = 3, 5
        if zero_row is not None and zero_row[i]:
            u, v = (5, 7), (-2, -7)
        else:
            u, v = (int(t), 0), (-2, -3)
        A[k][-1], A[k+1][-1] = u
        A[-1][k], A[-1][k+1] = v
    return A


def array_and_matrix_checks():
    names = ["mu", "M", "Q", "Np", "Nm", "S", "SS", "T", "pr"]
    arr = {n: np.load(ROOT / "data" / (n+".npy")) for n in names}
    mu, Np, Nm, pr = (arr[k] for k in ("mu", "Np", "Nm", "pr"))
    j = np.where(mu == 1, Np, Nm)
    coeff = mu.astype(np.int64) * (pr[j] - j)
    W = np.cumsum(coeff)
    w = pr - np.arange(len(pr), dtype=np.int64)
    Dw = np.cumsum(w)
    assert np.array_equal(W, Dw[Np] - Dw[Nm])
    assert np.array_equal(2*(arr["T"]-W), arr["M"]*(arr["Q"]+1))
    assert np.array_equal(arr["SS"], np.cumsum(arr["S"]))
    N = len(mu)
    nbal = int(np.flatnonzero(arr["M"] == 0)[-1]) + 1
    sf = np.flatnonzero(mu[:nbal]) + 1
    eps = mu[sf-1]
    R = np.concatenate(([0], np.cumsum(eps, dtype=np.int64)))
    a, b = np.flatnonzero(eps == 1)+1, np.flatnonzero(eps == -1)+1
    d = b - a
    Q, J = len(eps), len(a)
    assert Q == 2*J and R[-1] == 0
    V = {}
    for r in range(65):
        direct = int(np.maximum(np.abs(d)-r, 0).sum())
        two = int(np.maximum(np.abs(R[:Q-r]+R[r:Q])-r, 0).sum())
        assert two == 2*direct
        V[str(r)] = direct
    delta_phys = sf[b-1] - sf[a-1]
    phys_area = int(np.dot(w[1:J+1], np.abs(delta_phys)))
    assert phys_area == int(np.abs(W[:nbal]).sum())
    ordinal_area = int(np.dot(w[1:J+1], np.abs(d)))
    assert ordinal_area == int(np.abs(W[sf-1]).sum())
    prime_set = set(map(int, pr[1:200]))
    matrix_rows = []
    matrix_example = None
    for n in range(1, 41):
        MT = border_matrix(arr["S"][:n][mu[:n] != 0])
        MSS = border_matrix(arr["S"][:n], mu[:n] == 0)
        for mat in [MT, MSS]:
            assert all(x == 0 or abs(x) in prime_set for row in mat for x in row)
        detT, detSS = bareiss(MT), bareiss(MSS)
        assert detT == int(arr["T"][n-1])
        assert detSS == int(arr["SS"][n-1])
        red = [[int(jj == 1 or jj % ii == 0)
                for jj in range(1, n+1)] for ii in range(1, n+1)]
        assert bareiss(red) == int(arr["M"][n-1])
        matrix_rows.append({"n": n, "dim_T": len(MT), "dim_SS": len(MSS),
                            "det_T": detT, "det_SS": detSS})
        if n == 4:
            matrix_example = {"T_matrix": MT, "SS_matrix": MSS}
    return {"integer_prefixes": N, "balanced_physical_endpoint": nbal,
            "balanced_Q": Q, "J": J, "V_by_duration_cutoff": V,
            "prime_weighted_physical_area": phys_area,
            "prime_weighted_ordinal_area": ordinal_area,
            "matrix_checks": matrix_rows, "matrix_example_n4": matrix_example}


def explicit_poles():
    mp.mp.dps = 60
    c0 = 3 / mp.pi**2
    def B(s):
        return c0*s / ((s-1)*mp.zeta(s-1))
    def Pd(s):
        z = s-1
        zz, dz = mp.zeta(z), mp.diff(mp.zeta, z)
        return c0*s*(zz+z*dz)/(z*z*zz*zz)
    def string_complex(z):
        return {"real": mp.nstr(mp.re(z), 40), "imag": mp.nstr(mp.im(z), 40)}
    rows = []
    h = mp.mpf("1e-12")
    for k in range(1, 6):
        rho = mp.zetazero(k)
        s0 = 1+rho
        res = c0*s0/(rho*mp.diff(mp.zeta, rho))
        err_b = abs(h*B(s0+h)-res)
        err_d = abs(h*h*Pd(s0+h)-res)
        err_simple = abs(h*(Pd(s0+h)-res/(h*h))-res/s0)
        assert max(err_b, err_d, err_simple) < mp.mpf("1e-9")
        assert abs(Pd(s0+mp.mpf(".1")) -
                   (B(s0+mp.mpf(".1"))/(s0+mp.mpf(".1"))
                    - mp.diff(B, s0+mp.mpf(".1")))) < mp.mpf("1e-45")
        rows.append({"index": k, "rho": string_complex(rho),
                     "B_residue_and_Pdelta_double_coefficient": string_complex(res),
                     "Pdelta_simple_coefficient": string_complex(res/s0),
                     "Laurent_limit_absolute_errors": {
                         "B": mp.nstr(err_b, 12),
                         "Pdelta_double": mp.nstr(err_d, 12),
                         "Pdelta_simple": mp.nstr(err_simple, 12)}})
    z = mp.mpf(".3") + mp.mpf(".2")*1j
    numeric_integral = mp.quad(lambda u: mp.exp(-z*u)*(u+mp.log(u)), [1, mp.inf])
    branch_formula = mp.exp(-z)*(1+z)/(z*z) + mp.e1(z)/z
    assert abs(numeric_integral-branch_formula) < mp.mpf("1e-45")
    return {"precision_decimal_digits": mp.mp.dps,
            "scope": "Explicit B and P_delta only; not poles proved for full delta.",
            "not_interval_certified": True, "rows": rows,
            "branch_model_integral_error": mp.nstr(abs(numeric_integral-branch_formula), 12)}


def main():
    start = time.monotonic()
    result = {"finite_words": finite_words()}
    print("Finite balanced words:", result["finite_words"]["balanced_words"], flush=True)
    result["arrays_and_matrices"] = array_and_matrix_checks()
    print("One million prefix identities; 40 exact T/SS/Redheffer determinants checked.",
          flush=True)
    result["explicit_poles"] = explicit_poles()
    result["elapsed_seconds"] = round(time.monotonic()-start, 3)
    result["all_checks_passed"] = True
    (OUT / "v12_alpha_program_audit.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print("Laurent coefficients: five B poles and five explicit P_delta candidates.", flush=True)
    print("All finite checks passed. No numerical assertion of RH or full delta meromorphy.")
    print("Elapsed seconds:", result["elapsed_seconds"])


if __name__ == "__main__":
    main()
