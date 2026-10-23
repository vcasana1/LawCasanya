"""Independent Arb/FLINT audit template for the two Casanya pair discs.

Python >=3.10, python-flint with acb_series.gamma() and acb_series.zeta().
No genuine ordinates, zeross.bin or reference zero list are used.

The certificate is valid only if this program completes with a strict PASS for
both cases and its interval enclosures are retained. NOT EXECUTED in the
ChatGPT container on 2026-10-23: python-flint was unavailable there.

Run: python audit_pairs_arb.py --case 1283 --arcs 4096
     python audit_pairs_arb.py --case 1290 --arcs 4096

Algorithm: finite interval arcs cover the *entire boundary circle* of the
radius 3*h/2. Each interval third derivative is enclosed via the coefficient
of w**3 in a Taylor series of F(z+w); maximum modulus covers the disk.
The Taylor coefficients of the real entire function Xi(1/2+i*z) are enclosed
by ball evaluation at exact decimal input b and a positive scaling constant.
No assumed global bounding constant or FFT tail estimate is used.
"""
import argparse
import json
import platform
import time
from flint import acb, arb, acb_series, ctx

CASES = {
    1283: {"b": "1283.159048033", "h": "0.164715498", "scale": "1e433"},
    1290: {"b": "1290.255802206", "h": "0.154422788", "scale": "1e435"},
}

def scaled_xi_jet(zball, scale):
    """Taylor coefficients through 3, each a complex ball.

    Parameter zball may be an acb box; if so the coefficient j encloses
    F^(j)(z)/j! for every z in that box.
    """
    x = acb_series([zball, acb(1)], prec=4)
    s = acb("0.5") + acb(0, 1) * x
    gamma_factor = (s / 2).gamma()
    completed = (s * (s - 1) / 2) * ((-s / 2) * arb.pi().log()).exp()
    z = acb(scale) * completed * gamma_factor * s.zeta()
    coeff = z.coeffs()
    if len(coeff) < 4:
        coeff.extend([acb(0)] * (4 - len(coeff)))
    return coeff[:4]

def interval_arc(j, n):
    """Outward-rounded angle interval covering [2*pi*j/n,2*pi*(j+1)/n]."""
    pi = arb.pi()
    mid = pi * arb(2 * j + 1) / n
    half_width = (pi / n).upper()
    radius = half_width + mid.rad()
    return arb(mid.mid(), radius)

def audit(case, arcs, bits):
    ctx.prec = bits
    ctx.cap = 16
    cfg = CASES[case]
    b, h, scale = arb(cfg["b"]), arb(cfg["h"]), arb(cfg["scale"])
    radius = arb("1.5") * h
    start = time.time()
    central = scaled_xi_jet(acb(b), scale)
    f0, f1, f2 = central[0], central[1], 2 * central[2]
    # Strict realness of Xi along R is known analytically. The absolute
    # complex ball bounds are safe even if a tiny imaginary radius survives.
    f2abs = abs(f2)
    f2low = f2abs.lower()
    if not (f2low > 0):
        raise ArithmeticError("f'' lower bound does not exclude zero")
    bound = arb(0)
    for j in range(arcs):
        theta = interval_arc(j, arcs)
        zarc = acb(b + radius * theta.cos(), radius * theta.sin())
        j3 = scaled_xi_jet(zarc, scale)[3]
        upper = abs(6 * j3).upper()
        if upper > bound:
            bound = upper
        if j % max(1, arcs // 16) == 0:
            print("case", case, "arc", j, "/", arcs, "M3upper", bound, flush=True)
    # Holomorphy of xi implies |f'''(z)| <= max_boundary |f'''|.
    M3 = bound
    residual = abs(f0 + f2 * h * h / 2)
    H = h.upper()
    # Bounds computed monotonically with directed interval endpoints.
    small_left = residual.upper() + (arb(5) * H / 4) * abs(f1).upper() + arb(125) * M3 * H**3 / 384
    small_right = arb(7) * f2low * h.lower()**2 / 32
    outer_left = residual.upper() + (arb(3) * H / 2) * abs(f1).upper() + arb(9) * M3 * H**3 / 16
    outer_right = arb(5) * f2low * h.lower()**2 / 8
    eta = H * M3 / f2low
    small_ok = bool(small_left.upper() < small_right.lower())
    outer_ok = bool(outer_left.upper() < outer_right.lower())
    status = "PASS" if small_ok and outer_ok else "INCONCLUSIVE"
    obj = dict(
        status=status, case=case, input=cfg, arcs=arcs, bits=bits,
        M3_upper=str(M3), f2_abs_lower=str(f2low),
        small_left_upper=str(small_left.upper()), small_right_lower=str(small_right.lower()),
        outer_left_upper=str(outer_left.upper()), outer_right_lower=str(outer_right.lower()),
        eta_upper=str(eta.upper()),
        central_coefficients=[str(x) for x in central],
        elapsed_s=round(time.time() - start, 2),
        python=platform.python_version(),
    )
    print(json.dumps(obj, indent=2), flush=True)
    with open(f"pair_{case}_arb_audit.json", "w") as o:
        json.dump(obj, o, indent=2)
    if status != "PASS":
        raise RuntimeError("No certificate: increase precision/arcs or improve the interval bounds")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--case", type=int, choices=[1283, 1290], required=True)
    ap.add_argument("--arcs", type=int, default=4096)
    ap.add_argument("--bits", type=int, default=256)
    args = ap.parse_args()
    audit(args.case, args.arcs, args.bits)
