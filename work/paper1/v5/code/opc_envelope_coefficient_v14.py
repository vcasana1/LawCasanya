#!/usr/bin/env python3
"""Coefficient of the asymptotic envelope limsup |S(t)|/log t (Theorem E of ordinal_prime_cutoff_v14).

Usage:  python3 opc_envelope_coefficient_v14.py OUT_DIR

For an exponent profile e(sigma) on [0,1] (zeta(sigma+it) << |t|^{e(sigma)+eps} uniformly), the
Backlund-Jensen bound of Bellotti-Wong (Lemmas 2.1 and 2.3 of arXiv:2412.15470), with the disc centred
at b and radius rho tending to (1,1), gives

    limsup |S(t)|/log t <= C(e) = 1/(2 pi log 2) * int_0^1 e(sigma) / sqrt(sigma (2 - sigma)) d sigma .

The script evaluates C(e) for four profiles, with 40-digit quadrature on each linear piece:
  (a) the profile of Bellotti-Wong: 27/164 at sigma=1/2, Yang's lines sigma_k=1-k/(2^k-2) (k=4..9) with
      exponent 1/(2^k-2), 0 at sigma=1, linear interpolation between 0 and 1/2 (no reflection);
  (b) the same right-hand profile, reflected to [0,1/2] by the functional equation;
  (c) Bourgain's exponent pair (13/84,55/84) and its images A^j (j=1..7) under van der Corput's
      A-process, lower convex hull, reflected to [0,1/2];
  (d) the Lindelof profile (floor of the method).
It also evaluates the general disc (b, rho) for profile (a) as a check against 0.10076.
No data are read.
"""
import json
import sys
from fractions import Fraction as Fr

import mpmath as mp

mp.mp.dps = 40


def lower_hull(points):
    pts = sorted(set(points))
    hull = []
    for p in pts:
        while len(hull) >= 2:
            (x1, y1), (x2, y2) = hull[-2], hull[-1]
            if (y2 - y1) * (p[0] - x1) >= (p[1] - y1) * (x2 - x1):
                hull.pop()
            else:
                break
        hull.append(p)
    return hull


def piecewise(points):
    xs = [mp.mpf(x.numerator) / x.denominator if isinstance(x, Fr) else mp.mpf(x) for x, _ in points]
    ys = [mp.mpf(y.numerator) / y.denominator if isinstance(y, Fr) else mp.mpf(y) for _, y in points]

    def f(s):
        for i in range(len(xs) - 1):
            if xs[i] <= s <= xs[i + 1]:
                return ys[i] + (ys[i + 1] - ys[i]) * (s - xs[i]) / (xs[i + 1] - xs[i])
        raise ValueError(s)
    return f, xs


def profile(right_points, reflect, left_value_at_half=None):
    """Return e(sigma) on [0,1] and the list of breakpoints."""
    right, xs = piecewise(right_points)
    half = mp.mpf(1) / 2

    def e(s):
        if s >= 1:
            return mp.mpf(0)
        if s >= half:
            return right(s)
        if reflect:
            return half - s + right(1 - s)
        # linear interpolation between e(0)=1/2 and e(1/2)
        return (1 - 2 * s) * half + 2 * s * left_value_at_half
    bps = sorted(set([mp.mpf(0), half, mp.mpf(1)] + xs + ([1 - x for x in xs] if reflect else [])))
    return e, bps


def coefficient(e, bps):
    w = lambda s: e(s) / mp.sqrt(s * (2 - s))
    total = mp.mpf(0)
    for a, b in zip(bps[:-1], bps[1:]):
        if b > a:
            total += mp.quad(w, [a, b])
    return total / (2 * mp.pi * mp.log(2))


def disc_coefficient(e, b, rho):
    """(1/pi) int_0^pi e(b + rho cos th) dth / (2 log(rho/(b-1/2))), e = 0 for sigma >= 1."""
    g = lambda th: e(min(max(b + rho * mp.cos(th), mp.mpf(0)), mp.mpf(1))) if b + rho * mp.cos(th) >= 0 else mp.mpf(1) / 2 - (b + rho * mp.cos(th))
    val = mp.quad(g, mp.linspace(0, mp.pi, 64)) / mp.pi
    return val / (2 * mp.log(rho / (b - mp.mpf(1) / 2)))


def main(out_dir):
    half = Fr(1, 2)
    yang = [(Fr(1) - Fr(k, 2 ** k - 2), Fr(1, 2 ** k - 2)) for k in range(4, 10)]
    bw_right = lower_hull([(half, Fr(27, 164))] + yang + [(Fr(1), Fr(0))])
    e_a, b_a = profile(bw_right, reflect=False, left_value_at_half=mp.mpf(27) / 164)
    e_b, b_b = profile(bw_right, reflect=True)

    pairs = []
    k, l = Fr(13, 84), Fr(55, 84)
    pairs.append((k, l))
    for _ in range(7):
        k, l = k / (2 * k + 2), half + l / (2 * k + 2)
        pairs.append((k, l))
    bourgain_points = [(l - k, k) for k, l in pairs] + [(Fr(1), Fr(0))]
    bourgain_right = lower_hull(bourgain_points)
    e_c, b_c = profile(bourgain_right, reflect=True)

    lindelof_right = [(half, Fr(0)), (Fr(1), Fr(0))]
    e_d, b_d = profile(lindelof_right, reflect=True)

    res = {
        "formula": "C(e) = (1/(2 pi log 2)) * int_0^1 e(sigma)/sqrt(sigma(2-sigma)) dsigma",
        "a_BellottiWong_profile_no_reflection": float(coefficient(e_a, b_a)),
        "b_same_profile_with_reflection": float(coefficient(e_b, b_b)),
        "c_Bourgain_Aimages_with_reflection": float(coefficient(e_c, b_c)),
        "d_Lindelof_floor": float(coefficient(e_d, b_d)),
        "check_disc_b1.0001_rho1.0002_profile_a": float(disc_coefficient(e_a, mp.mpf("1.0001"), mp.mpf("1.0002"))),
        "Bourgain_hull_points": [[str(x), str(y), float(x), float(y)] for x, y in bourgain_right],
        "BW_hull_points": [[str(x), str(y), float(x), float(y)] for x, y in bw_right],
        "exponent_pairs_used": [[str(k), str(l)] for k, l in pairs],
    }
    for key in ("a_BellottiWong_profile_no_reflection", "b_same_profile_with_reflection",
                "c_Bourgain_Aimages_with_reflection", "d_Lindelof_floor"):
        res[key + "_times_2pi"] = float(2 * mp.pi * res[key])
    res["c_exact_40_digits"] = mp.nstr(coefficient(e_c, b_c), 30)
    res["c_times_2pi_40_digits"] = mp.nstr(2 * mp.pi * coefficient(e_c, b_c), 30)
    with open(f"{out_dir}/envelope_coefficient.json", "w") as fh:
        json.dump(res, fh, indent=1)
    for key, val in res.items():
        if not isinstance(val, list):
            print(f"{key}: {val}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "outputs")
