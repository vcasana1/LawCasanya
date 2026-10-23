"""Rouche + indexed Turing/Arb one-zero verifier (corrected validation logic).

Requires python-flint, numpy; no zeross.bin or true zeros in construction.
Usage: python rouche_one_zero_v4.py CENTERS.bin K0 COUNT OUT_PREFIX

This program has been syntax checked but *not* run in the ChatGPT environment
because python-flint is unavailable. All comparisons use Arb ball bounds.
It uses acb.zeta_zero(k) only after a purely local Rouche disk is validated.
"""
import sys
import json
import time
import numpy as np
from flint import acb, arb, acb_series, ctx

ctx.prec = 160
ctx.cap = 16
PI = arb.pi()
K = 7
RMAX = arb("0.2")
TRIES = ("1.5", "2", "3", "5")

def jet(b):
    """Hardy Z Taylor coefficients of degrees 0 through K at a ball b."""
    x = acb_series([acb(b), acb(1)], prec=K + 2)
    s = acb_series([acb("0.5") + acb(0, 1) * acb(b), acb(0, 1)], prec=K+2)
    u = acb_series([acb("0.25") + acb(0, 1) * acb(b) / 2, acb(0, 1) / 2], prec=K+2)
    uc = acb_series([acb("0.25") - acb(0, 1) * acb(b) / 2, acb(0, -1) / 2], prec=K+2)
    theta = (u.lgamma() - uc.lgamma()) / acb(0, 2) - x * (PI.log() / 2)
    values = ((theta * acb(0, 1)).exp() * s.zeta()).coeffs()
    if len(values) < K + 1:
        values.extend([acb(0)] * (K + 1 - len(values)))
    return values

def local_disc(center):
    """Return a disk certified by Rouche, or None.

    CENTER is an exact dyadic/input Arb real ball; outward interval bounds
    are used for all decisive comparisons.
    """
    z = jet(center)
    a, c = abs(z[0]), abs(z[1])
    if not (c.lower() > 0):
        return None
    r0 = a / c
    for m in TRIES:
        radius = (arb(m) * r0).upper() + arb("1e-12")
        if not (radius.upper() < RMAX.lower()):
            continue
        # This complex rectangle contains the whole circle |z-center|<=radius.
        box = acb(arb(center, radius), arb(0, radius))
        zK = abs(jet(box)[K]).upper()
        high_r = radius.upper()
        remainder = sum((abs(z[j]).upper() * high_r**j for j in range(2, K)), arb(0))
        remainder += zK * high_r**K
        lhs = a.upper() + remainder.upper()
        rhs = c.lower() * radius.lower()
        if bool(lhs < rhs):
            return dict(center=center, radius=radius, lhs=lhs, rhs=rhs,
                        multiplier=m, f0_abs=a, f1_abs=c, rem=remainder)
    return None

def certify_index(k, certified):
    """Verify inclusion of the Arb Turing indexed zero in THE certified disk."""
    gamma_ball = acb.zeta_zero(k)
    center = certified["center"]
    radius = certified["radius"]
    zeta_s_center = acb(arb("0.5"), center)
    upper_distance = abs(gamma_ball - zeta_s_center).upper()
    return bool(upper_distance < radius.lower()), gamma_ball, upper_distance

def run(path, k0, count, prefix):
    xs = np.fromfile(path, dtype="<f8")
    records = []
    start = time.time()
    for k in range(k0, k0 + count):
        x = float(xs[k-1])
        xb = arb(x)  # the binary64 input is only a proposed, prime-only center
        trial = local_disc(xb)
        method = "original"
        if trial is None:
            v = jet(xb)
            if not (abs(v[1]).lower() > 0):
                records.append({"k":k,"status":"fail_derivative"})
                continue
            # Proposal only: round the Newton correction, then fully recertify.
            correction = (v[0]/v[1]).real.mid()
            bnew = arb(float(x - float(correction)))
            trial = local_disc(bnew)
            method = "newton"
        if trial is None:
            records.append({"k":k,"status":"fail_rouche"})
            continue
        ok, ball, distance = certify_index(k, trial)
        effective_bound = trial["radius"].upper() + abs(trial["center"]-xb).upper()
        records.append(dict(
            k=k, input_center=repr(x), certified_center=str(trial["center"]),
            actual_radius=str(trial["radius"]), bound_about_input=str(effective_bound),
            rouche_margin=str(trial["rhs"].lower() - trial["lhs"].upper()),
            ball_k=str(ball), ball_to_cert_center_upper=str(distance),
            status="indexed_certified" if ok else "index_not_proved", method=method))
        if (k-k0+1) % 10 == 0:
            print("processed", k-k0+1, "of", count, flush=True)
    summary = dict(input=path,k0=k0,count=count,
        indexed_certified=sum(r["status"] == "indexed_certified" for r in records),
        fail_rouche=sum(r["status"] == "fail_rouche" for r in records),
        index_not_proved=sum(r["status"] == "index_not_proved" for r in records),
        time_s=round(time.time()-start,2))
    with open(prefix+".json", "w") as out:
        json.dump(dict(summary=summary, records=records), out, indent=2)
    print(json.dumps(summary,indent=2))

if __name__ == "__main__":
    if len(sys.argv)!=5:
        raise SystemExit("Usage: rouche_one_zero_v4.py CENTERS.bin K0 COUNT OUT_PREFIX")
    run(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),sys.argv[4])
