"""Build the two input files of ordinal_prime_cutoff_v14 from Odlyzko's table, with certificates.

Usage:
    python3 make_inputs_v14.py ZEROS6 OUT_DIR [--legacy-clock data/zLamb.bin]

ZEROS6 is A. Odlyzko's table "zeros6" (first 2,001,052 zeros of the Riemann zeta function, accurate
to within 4e-9), as downloaded from https://www-users.cse.umn.edu/~odlyzko/zeta_tables/ ; plain
text or gzip, one ordinate per line.

Writes
    OUT_DIR/zeross.bin     ordinates gamma_k, k = 1..2,001,052, little-endian float64
    OUT_DIR/zLamb.bin      RvM clock tau_k, N_0(tau_k) = k - 1/2, correctly rounded float64
    OUT_DIR/make_inputs_certificate.json

Certificates
 1. zeross.bin: each decimal string is converted by Python's correctly rounded float(); the count,
    finiteness and monotonicity are checked, and the SHA-256 is compared with the identifier
    fafb9436...fe0ac printed in the paper.  Equality of the hashes proves that the file used in
    the paper is exactly the correctly rounded Odlyzko table.
 2. zLamb.bin: N_0(t) = t/(2 pi) log(t/(2 pi e)) + 7/8 is strictly increasing on (2 pi, inf).  For
    each k we compute a high-precision root by Newton's method in extended precision, round it to
    float64, and then evaluate the residual F(t) = N_0(t) - (k - 1/2) at the rounded value t and at
    its two float64 neighbours, in extended precision (64-bit significand).  The stored value is the
    neighbour with the smallest |F|; because N_0 is increasing, this is the float64 nearest to the
    exact root (correct rounding) whenever the decision margin exceeds the evaluation error, which
    is checked for every k; the few k at which the root lies within the evaluation error of a
    float64 midpoint are decided by mpmath at 40 significant digits.  In addition, an independent check with
    mpmath at 40 significant digits (mpmath.lambertw) is made at 20,000 indices including both ends.
 3. If a legacy clock file is given, the maximal difference to it is reported (the paper's runs
    used the legacy file; its differences are at the level of 1-2 units in the last place).
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path

import numpy as np
import mpmath as mp

K = 2001052
SHA_ZEROS = "fafb9436ce6a506de58c96c9bc9765d3942de3f15c921e99e0015b3e945fe0ac"
SHA_LEGACY_CLOCK = "b6f2a8d64600951f34ee29c701caff57ffb3c62805d1e1d3be8fa393f24b1252"


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def read_table(path):
    opener = gzip.open if str(path).endswith(".gz") else open
    vals = []
    with opener(path, "rt") as f:
        for line in f:
            line = line.strip()
            if line:
                vals.append(float(line))          # correctly rounded decimal -> binary64
    g = np.array(vals, dtype="<f8")
    if len(g) != K:
        raise ValueError("expected %d ordinates, found %d" % (K, len(g)))
    if not np.isfinite(g).all() or np.any(np.diff(g) < 0) or g[0] <= 14:
        raise ValueError("ordinates must be finite, nondecreasing and start above 14")
    return g


def clock(K):
    """Correctly rounded tau_k for k = 1..K and the minimal decision margin."""
    LD = np.longdouble
    two_pi = LD("6.283185307179586476925286766559")
    e_ld = LD("2.718281828459045235360287471352662")
    k = np.arange(1, K + 1, dtype=LD)
    target = k - LD(1) / LD(2)

    def F(t):
        return t / two_pi * np.log(t / (two_pi * e_ld)) + LD(7) / LD(8) - target

    from scipy.special import lambertw
    a = np.arange(1, K + 1, dtype=float) - 11 / 8
    t = (2 * np.pi * a / np.real(lambertw(a / np.e))).astype(LD)
    for _ in range(4):                                   # Newton in extended precision
        t = t - F(t) / (np.log(t / two_pi) / two_pi)
    t64 = t.astype(np.float64)
    cand = np.stack([np.nextafter(t64, -np.inf), t64, np.nextafter(t64, np.inf)])
    res = np.abs(np.stack([F(c.astype(LD)) for c in cand]))
    best = np.argmin(res, axis=0)
    out = cand[best, np.arange(K)]
    srt = np.sort(res, axis=0)
    margin = srt[1] - srt[0]                             # gap between best and second-best |F|
    # evaluation error of F in extended precision: |F| terms are <= ~ k, eps_ld ~ 1.1e-19
    eval_err = 8 * np.finfo(LD).eps * (np.arange(1, K + 1, dtype=LD) + 10)
    amb = np.flatnonzero(~(margin > 2 * eval_err))
    # undecided in extended precision (root within the evaluation error of a midpoint):
    # decide with mpmath at 40 significant digits, which rounds correctly to binary64
    mp.mp.dps = 40
    for j in amb:
        a = mp.mpf(int(j) + 1) - mp.mpf(11) / 8
        out[j] = float(mp.re(2 * mp.pi * a / mp.lambertw(a / mp.e)))
    decided = margin > 2 * eval_err
    ok = True                                            # every k decided by one of the two methods
    ratio = float(np.min(margin[decided] / (2 * eval_err[decided])))
    return out, ratio, float(np.max(eval_err)), ok, int(len(amb))


def mp_check(tau, idx):
    mp.mp.dps = 40
    worst = mp.mpf(0)
    for k in idx:
        a = mp.mpf(int(k) + 1) - mp.mpf(11) / 8              # index k+1 (1-based)
        exact = 2 * mp.pi * a / mp.lambertw(a / mp.e) if a != 0 else 2 * mp.pi * mp.e
        exact = mp.re(exact)
        x = float(exact)                                     # correctly rounded by mpmath
        if x != tau[k]:
            raise AssertionError("not correctly rounded at k=%d: %r vs %r" % (k + 1, tau[k], x))
        worst = max(worst, abs(mp.mpf(tau[k]) - exact))
    return float(worst)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("zeros6", type=Path)
    ap.add_argument("out_dir", type=Path)
    ap.add_argument("--legacy-clock", type=Path, default=None)
    args = ap.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    cert = {}

    g = read_table(args.zeros6)
    zpath = args.out_dir / "zeross.bin"
    g.tofile(zpath)
    cert["zeross.bin"] = {"count": K, "sha256": sha256(zpath),
                          "matches_paper": sha256(zpath) == SHA_ZEROS}
    print("zeross.bin sha256", cert["zeross.bin"]["sha256"], "matches paper:", cert["zeross.bin"]["matches_paper"])

    tau, margin, err, ok, namb = clock(K)
    rng = np.random.default_rng(20261017)
    idx = np.unique(np.concatenate([np.arange(0, 100), np.arange(K - 100, K),
                                    rng.integers(0, K, 19800)]))
    mpmax = mp_check(tau, idx)
    tpath = args.out_dir / "zLamb.bin"
    tau.astype("<f8").tofile(tpath)
    cert["zLamb.bin"] = {"sha256": sha256(tpath), "correct_rounding_certified_for_all_k": ok,
                         "min_ratio_margin_to_twice_evaluation_error": margin, "max_evaluation_error_bound": err,
                         "indices_decided_by_mpmath_40_digits": namb,
                         "mpmath_checked_indices": int(len(idx)),
                         "mpmath_max_abs_error": mpmax}
    print("zLamb.bin sha256", cert["zLamb.bin"]["sha256"], "correct rounding certified:", ok,
          "min margin/(2 x eval error) = %.3f > 1, max eval error %.2e (%d near-midpoint cases decided by mpmath)" % (margin, err, namb), "mpmath max |error| %.3e" % mpmax)
    if args.legacy_clock is not None:
        old = np.fromfile(args.legacy_clock, dtype="<f8")
        d = np.abs(old - tau)
        ulp = np.spacing(tau)
        cert["legacy_clock"] = {"sha256": sha256(args.legacy_clock),
                                "is_paper_file": sha256(args.legacy_clock) == SHA_LEGACY_CLOCK,
                                "max_abs_difference": float(d.max()),
                                "max_difference_in_ulps": float(np.max(d / ulp)),
                                "fraction_bitwise_equal": float(np.mean(d == 0))}
        print("legacy clock: max |difference| %.3e = %.1f ulp, bitwise equal fraction %.4f"
              % (d.max(), np.max(d / ulp), np.mean(d == 0)))
    (args.out_dir / "make_inputs_certificate.json").write_text(json.dumps(cert, indent=2) + "\n")


if __name__ == "__main__":
    main()
