#!/usr/bin/env python3
"""Explicit constants of Selberg's mean-square approximation, after Hiary-Zhao (arXiv:2512.14907v1, 2025).
Step 1: reproduce their Theorem 1 constant (|E S(t,chi)| < 981.4 as kappa -> 1/8) from their formulas
        (Prop. 11: B1, B2; Lemma 13: C; Prop. 14: D, h(k)), to validate the transcription.
Step 2: zeta adaptation [ADAPT, not proved here]: conductor q -> T, log q(|t|+1)/log x -> 1/(delta kappa),
        mollifier length xi = T^kappa with kappa < 1/4 (twisted second moment of zeta for xi^2 < T^{1/2}).
        This gives (1/T) int_T^{2T} (S - S^pr_{x^3})^2 dt <= D_zeta, x = T^{delta kappa}.
Step 3: translate into B and into the certificate N_0^s/N >= 1 - 4<u^2>."""
import json, math
import mpmath as mp

def h(k):
    def val(D):
        g = ((2*D*D + 4*D + 3)*mp.e**(6*D) - 192*D**3 - 80*D**2 - 22*D - 3) / (8*D**4*mp.e**(6*D))
        return ((1 - mp.e**(-D))*mp.mpf(8.68)**(2*k) + mp.e**(-D)*g**(2*k))**(mp.mpf(1)/(2*k))
    best = min(((val(mp.mpf(d)/1000), d/1000) for d in range(50, 3000, 5)), key=lambda z: z[0])
    return best

def B1(eta, variant):
    a = 5*(1 + mp.e**(-eta))**2
    num = a + (5*mp.pi + 1)*6*eta**3*mp.e**eta
    den = (6*eta**3*mp.e**eta - a)*eta if variant == 0 else 6*eta**3*mp.e**eta - a*eta
    return num/den

def B2(eta, variant):
    a = 5*(1 + mp.e**(-eta))**2
    num = a*(1 + eta) + 30*mp.pi*eta**3*mp.e**eta
    den = (12*eta**3*mp.e**eta - 2*a)*eta if variant == 0 else 12*eta**3*mp.e**eta - 2*a*eta
    return num/den

def C(eta, delta, r, v):
    w = 2/delta - 2*r - 3
    assert w > 0
    pref = 2**(v + 1)*(4.79 + 4.12/(4*mp.e**(3*eta)/delta - 1.73))
    return ((2*eta)**v*mp.e**(2*eta*r)
            + pref*(eta**v*mp.e**(-w*eta)/delta
                    + v*mp.gammainc(v, eta*w)/(delta*w**v)
                    + 2*r*mp.gammainc(v + 1, eta*w)/(delta*w**(v + 1))))

def D(eta, delta, kappa, k, logfactor, variant):
    hk = h(k)[0]
    b1, b2 = B1(eta, variant), B2(eta, variant)
    c4 = C(eta, delta, 4*k, 4*k)**(mp.mpf(1)/(4*k))
    c2 = C(eta, delta, 0, 2*k)**(mp.mpf(1)/(2*k))
    s = ((b1 + mp.e**(-2*eta))*c4*mp.sqrt(hk) + 1.5*(1 + b1)*c2
         + b2*c2*logfactor/(delta*kappa) + mp.sqrt(0.12) + 0.53 + mp.sqrt(0.58))
    return s**(2*k)/mp.pi**(2*k)

out = {}
hk1, Dlt = h(1)
out["h1"] = [float(hk1), Dlt]
# Step 1: Hiary-Zhao Theorem 1 (eta=1.156, delta=0.16, kappa -> 1/8, eps=1/4: log factor 5/4-eps = 1)
for variant in (0, 1):
    out[f"HZ_thm1_sqrtD_variant{variant}"] = float(mp.sqrt(D(1.156, 0.16, 0.125, 1, 1.0, variant)))
print(json.dumps(out, indent=1))

# ---------------- Step 2-3: zeta adaptation [ADAPT] and translation ----------------
# F = N0 + S^(1)_X (primes only, X = x^3 = T^{3 delta kappa}); E = N - F = S - S^pr_{x^3} + varpi/pi.
# Theorem A: <u^2> = Q_2 - 1/12,  Q_2 = (1/M) int E^2 (L + S_X') dt  <=  <E^2>_t (1+o(1)) + c_X sqrt(<E^4>_t) (1+o(1)),
# using <S_X'^2>_t ~ (log X)^2/(4 pi^2) = (c_X L)^2 (Mertens) and Cauchy-Schwarz.
# <E^2> <= D(k=1), <E^4> <= 2 D(k=2) (factor k! = 2 for the zeta analogue of HZ Lemma 12; conservative).
a = 1/(2*math.pi**2)
res = {}
for kappa in (0.125, 0.25):
    best = None
    for delta in [i/1000 for i in range(40, 106, 5)]:
        d1 = min(float(D(eta/100, delta, kappa, 1, 1.0, 1)) for eta in range(80, 260, 4))
        d2 = min(float(D(eta/100, delta, kappa, 2, 1.0, 1)) for eta in range(80, 260, 4))
        cX = 3*delta*kappa
        Q2 = d1 + cX*math.sqrt(2*d2)
        u2 = Q2 - 1/12
        cand = {"kappa": kappa, "delta": delta, "c_X": cX, "D1": d1, "D2": d2, "Q2_bound": Q2,
                "u2_bound": u2, "B_bound": Q2/a - math.log(1/cX), "certificate": 1 - 4*u2}
        if best is None or Q2 < best["Q2_bound"]:
            best = cand
    res[f"kappa_{kappa}"] = best
needed = {"u2_for_positive_proportion": 0.25, "u2_for_record_0.6735": (1 - 0.6735)/4,
          "measured_u2_c_0.5": 0.01213, "measured_B_c_0.5": 1.19}
out.update({"zeta_adaptation": res, "targets": needed})
json.dump(out, open("explicit_B_hiary_zhao.json", "w"), indent=1)
lines = ["Hiary-Zhao transcription check: sqrt D(1.156, 0.16, 1/8, k=1) = %.4f (paper: 981.4)" % out["HZ_thm1_sqrtD_variant1"],
         "h(1) = %.4f at Delta = %.3f (paper: 6.390, 0.645)" % tuple(out["h1"]), ""]
for key, b in res.items():
    lines += [f"zeta adaptation, {key}: best delta = {b['delta']}, X = T^{b['c_X']:.4f}",
              "  D(k=1) = %.4e   D(k=2) = %.4e" % (b["D1"], b["D2"]),
              "  Q_2 <= %.4e   <u^2> <= %.4e   B <= %.4e   certificate 1-4<u^2> = %.4e" %
              (b["Q2_bound"], b["u2_bound"], b["B_bound"], b["certificate"]), ""]
lines += ["targets: <u^2> < 0.25 (positive proportion), < %.4f (record 0.6735); measured <u^2> = 0.01213 at c = 1/2, B = 1.19" %
          needed["u2_for_record_0.6735"]]
txt = "\n".join(lines) + "\n"
open("explicit_B_hiary_zhao.txt", "w").write(txt); print(txt)
