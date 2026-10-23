"""One-zero Rouche certificate for the corrected centres x_k, with the zero index
fixed by Arb's Turing-certified count (acb.zeta_zero).

For every k in the block:
  Z(t) = exp(i theta(t)) zeta(1/2+it), analytic and real on the real axis near b = x_k.
  a = Z(b), c = Z'(b), S(r) = sum_{2<=j<K}|z_j| r^j + sup_disc|z_K| r^K  (Taylor, ball over the disc for z_K).
  If |a| + S(r) < |c| r  (R)  then Z has exactly one zero in |z-b|<r; it is real, simple.
The centres x_k are read from the input file; zeross.bin is NOT read.
Index: acb.zeta_zero(k) (rigorous index, Turing's method inside Arb) must lie in the disc.
Usage: python3 rouche_one_zero.py INPUT.bin K0 COUNT OUT_PREFIX
"""
import sys, json, time
import numpy as np
from flint import acb, arb, acb_series, ctx

ctx.prec = 120
ctx.cap = 16
PI = arb.pi()

RMAX = 0.2   # radius cap (mean zero spacing ~0.55 at t~6e5); larger discs are not attempted
K = 7   # Taylor order: Z(b+w) = sum_{j<K} z_j w^j + R_K,  |R_K| <= sup_disc |z_K| r^K

def z_jet(b):
    """Taylor coefficients z_0..z_K of Z at b (acb ball: a point, or a disc for the remainder)."""
    x = acb_series([b, acb(1)], prec=K + 2)
    s = acb_series([acb(0.5) + acb(0, 1) * b, acb(0, 1)], prec=K + 2)
    u = acb_series([acb(0.25) + acb(0, 1) * b / 2, acb(0, 1) / 2], prec=K + 2)
    uc = acb_series([acb(0.25) - acb(0, 1) * b / 2, acb(0, -1) / 2], prec=K + 2)
    theta = (u.lgamma() - uc.lgamma()) / acb(0, 2) - x * (PI.log() / 2)
    Z = (theta * acb(0, 1)).exp() * s.zeta()
    return Z.coeffs()

def certify_at(b_float, tries=(1.5, 2, 3, 5)):
    b = acb(arb(b_float))
    z = z_jet(b)
    a, c = abs(z[0]), abs(z[1])
    r0 = a / c
    for m in tries:
        r = r0 * m + arb("1e-12")
        rr = r.upper()
        if rr > RMAX:
            break
        disc = acb(arb(b_float, rr), arb(0, rr))
        zK = abs(z_jet(disc)[K]).upper()
        S = sum((abs(z[j]) * rr**j for j in range(2, K)), arb(0)) + zK * rr**K
        if (a + S < c * rr):
            return float(rr), float(a.mid()), float(c.mid()), float(S.upper()), m
    return None, float(a.mid()), float(c.mid()), None, None

def certify(x):
    """Try the disc centred at x; if (R) fails, re-centre at the Newton point b1 = x - Z/Z'
    (computed from the same jet) and add |b1 - x| to the radius: |gamma - x| <= r1 + |b1 - x|."""
    out = certify_at(x)
    if out[0] is not None:
        return out + ("x",)
    z = z_jet(acb(arb(x)))
    b1 = x - float((z[0] / z[1]).real.mid())
    r1, a, c, S, m = certify_at(b1)
    if r1 is None:
        return None, a, c, None, None, "newton"
    return r1 + abs(b1 - x), a, c, S, m, "newton"

def main():
    inp, k0, cnt, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    xs = np.fromfile(inp, dtype="<f8")
    rows, t0 = [], time.time()
    for k in range(k0, k0 + cnt):
        x = float(xs[k - 1])
        r, a, c, M2, m, centre = certify(x)
        status, inside = "fail_R", None
        if r is not None:
            g = acb.zeta_zero(k)               # Turing-certified index
            gm, gr = float(g.imag.mid()), float(g.imag.rad())
            inside = abs(gm - x) + gr < r and abs(float(g.real.mid()) - 0.5) < 1e-9
            status = "ok" if inside else "index_mismatch"
        rows.append((k, x, r, a, c, M2, m, status, centre))
    rows_ok = [q for q in rows if q[7] == "ok"]
    # disjointness of consecutive discs
    overlap = sum(1 for p, q in zip(rows, rows[1:])
                  if p[2] is not None and q[2] is not None and p[1] + p[2] >= q[1] - q[2])
    with open(out + ".csv", "w") as fh:
        fh.write("k,x_k,r_k,Z_b,Zp_b,S,mult,status,centre\n")
        for q in rows:
            fh.write(",".join("" if v is None else repr(v) for v in q) + "\n")
    summ = dict(input=inp, k0=k0, count=cnt, ok=len(rows_ok),
                fail_R=sum(1 for q in rows if q[7] == "fail_R"),
                index_mismatch=sum(1 for q in rows if q[7] == "index_mismatch"),
                overlapping_consecutive_discs=overlap,
                max_r=max((q[2] for q in rows_ok), default=None),
                mean_r=float(np.mean([q[2] for q in rows_ok])) if rows_ok else None,
                seconds=round(time.time() - t0, 1))
    json.dump(summ, open(out + ".json", "w"), indent=1)
    print(json.dumps(summ, indent=1))

if __name__ == "__main__":
    main()
