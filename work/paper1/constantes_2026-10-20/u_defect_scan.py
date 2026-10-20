#!/usr/bin/env python3
"""Empirical size of the ordinal defect u_k(X) and of the zeta-free corrected clocks
at the heights of Odlyzko's table (training indices only, k <= 1 400 736).

Definitions as in prime_corrected_clock_v11.tex:
  N0(t) = Theta0(t)/pi + 1,  Theta0(t) = (t/2) log(t/(2 pi e)) - pi/8,  L(t) = log(t/2pi)/(2pi)
  tau_k : N0(tau_k) = k - 1/2  (Lambert W, solved here by Newton on N0)
  S_X(t) = -(1/pi) sum_{p<=X} arg(1 - p^{-1/2-it})   (principal arg of each factor)
  u_k(X) = k - 1/2 - N0(gamma_k) - S_X(gamma_k)        (ordinal defect at the ordinate)
  x^(j)  = x^(j-1) - (N0(x^(j-1)) + S_X(x^(j-1)) - (k-1/2)) / L(x^(j-1)),  x^(0)=tau_k
The zeros gamma_k are read only to evaluate errors; no construction uses them.
Window: I_T = {k : T < gamma_k <= 2T} with 2T <= gamma_{1400736}.
"""
import json, math, sys
import numpy as np

ZEROS = sys.argv[1] if len(sys.argv) > 1 else "../../../data/zeross.bin"
KMAX_TRAIN = 1_400_736
g_all = np.fromfile(ZEROS, dtype="<f8")
assert g_all.size == 2_001_052
g_tr = g_all[:KMAX_TRAIN]
T = math.floor(g_tr[-1] / 2.0)
k_all = np.arange(1, g_all.size + 1, dtype=np.float64)
sel = (g_tr > T) & (g_tr <= 2 * T)
g = g_tr[sel]
k = k_all[:KMAX_TRAIN][sel]
M = g.size
logT = math.log(T)
LL = lambda t: np.log(t / (2 * np.pi)) / (2 * np.pi)
Theta0 = lambda t: 0.5 * t * np.log(t / (2 * np.pi * np.e)) - np.pi / 8
N0 = lambda t: Theta0(t) / np.pi + 1.0

def primes_upto(n):
    s = np.ones(n + 1, dtype=bool); s[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]: s[i * i::i] = False
    return np.nonzero(s)[0]

def S_X(t, X, chunk=40000):
    ps = primes_upto(int(math.floor(X)))
    lp = np.log(ps.astype(np.float64)); amp = ps.astype(np.float64) ** -0.5
    out = np.empty_like(t)
    for a in range(0, t.size, chunk):
        tt = t[a:a + chunk, None]
        z = 1.0 - amp[None, :] * np.exp(-1j * tt * lp[None, :])
        out[a:a + chunk] = -np.angle(z).sum(axis=1) / np.pi
    return out, ps.size

# RvM clock: Newton on N0 (N0 is increasing and convex for t > 2pi)
tau = 2 * np.pi * np.exp(1.0) * np.ones(M)
x = (k - 11 / 8)
tau = 2 * np.pi * x / np.log(x / np.e)          # first-order Lambert start
for _ in range(8):
    tau = tau - (N0(tau) - (k - 0.5)) / LL(tau)
assert np.max(np.abs(N0(tau) - (k - 0.5))) < 1e-8

Lg = LL(g)
spacing = 1.0  # index units
res = {"T": T, "logT": logT, "loglogT": math.log(logT), "M": int(M),
       "k_first": int(k[0]), "k_last": int(k[-1]), "a": 1 / (2 * math.pi ** 2)}

def stats(v):
    return {"mean": float(v.mean()), "m2": float((v ** 2).mean()), "m4": float((v ** 4).mean()),
            "frac_abs_ge_half": float((np.abs(v) >= 0.5).mean()), "max_abs": float(np.abs(v).max())}

# 1. defect of the plain clock (X < 2): s_k
s = (k - 0.5) - N0(g)
res["s_k"] = stats(s)
res["s_k"]["pred_m2"] = res["a"] * math.log(logT)

# 2. defect u_k(X) at X = T^c
res["u"] = []
for c in [1 / 2, 1 / 3, 1 / 4, 1 / 6, 1 / 8]:
    X = T ** c
    SXg, npr = S_X(g, X)
    u = s - SXg
    st = stats(u); st.update({"c": c, "X": X, "n_primes": npr,
                              "main": res["a"] * math.log(1 / c)})
    st["K_emp"] = st["m2"] - st["main"]
    res["u"].append(st)

# 3. zeta-free corrected clocks: Newton steps with fixed X = T^c from tau_k
def nearest_is_own(xk):
    idx = np.searchsorted(g_all, xk)            # neighbours in the full table (evaluation only)
    idx = np.clip(idx, 1, g_all.size - 1)
    left, right = g_all[idx - 1], g_all[idx]
    nearest = np.where(np.abs(xk - left) <= np.abs(right - xk), idx - 1, idx) + 1
    return float((nearest == k).mean())

res["clock"] = []
for c in [1 / 2, 1 / 4]:
    X = T ** c
    xk = tau.copy()
    eps_prev = Lg * (xk - g)
    rows = [{"step": 0, "m2_index": float((eps_prev ** 2).mean()),
             "frac_nearest_own": nearest_is_own(xk)}]
    for j in range(1, 7):
        SXx, _ = S_X(xk, X)
        xk = xk - (N0(xk) + SXx - (k - 0.5)) / LL(xk)
        eps = Lg * (xk - g)
        rows.append({"step": j, "m2_index": float((eps ** 2).mean()),
                     "m4_index": float((eps ** 4).mean()),
                     "frac_abs_ge_half": float((np.abs(eps) >= 0.5).mean()),
                     "frac_nearest_own": nearest_is_own(xk),
                     "rms_height": float(np.sqrt(((xk - g) ** 2).mean()))})
        eps_prev = eps
    res["clock"].append({"c": c, "X": X, "rows": rows})

out = json.dumps(res, indent=1)
open("u_defect_scan.json", "w").write(out)
lines = [f"T = {T}  log T = {logT:.4f}  loglog T = {math.log(logT):.4f}  #I_T = {M}  k in [{int(k[0])}, {int(k[-1])}]",
         f"a = 1/(2 pi^2) = {res['a']:.6f}", "",
         "plain clock defect s_k: <s^2> = %.5f  (a loglogT = %.5f)  frac|s|>=1/2 = %.4f" %
         (res['s_k']['m2'], res['s_k']['pred_m2'], res['s_k']['frac_abs_ge_half']), "",
         "  c       X      #p   <u^2>    a log(1/c)   K_emp    <u^4>/<u^2>^2  frac|u|>=1/2  max|u|"]
for st in res["u"]:
    lines.append("%6.4f %8.1f %5d  %.5f   %.5f    %+.5f   %.3f          %.5f       %.3f" %
                 (st['c'], st['X'], st['n_primes'], st['m2'], st['main'], st['K_emp'],
                  st['m4'] / st['m2'] ** 2, st['frac_abs_ge_half'], st['max_abs']))
for cl in res["clock"]:
    lines += ["", "Newton steps from tau_k with fixed X = T^%.4f = %.1f (zeta-free):" % (cl['c'], cl['X']),
              " step  <eps^2> (index units)  frac|eps|>=1/2  frac nearest zero = own  rms height"]
    for r in cl["rows"]:
        lines.append(" %3d   %.5f               %s        %.5f                   %s" %
                     (r['step'], r['m2_index'],
                      ("%.5f" % r['frac_abs_ge_half']) if 'frac_abs_ge_half' in r else "   -   ",
                      r['frac_nearest_own'], ("%.5f" % r['rms_height']) if 'rms_height' in r else "  -"))
txt = "\n".join(lines) + "\n"
open("u_defect_scan.txt", "w").write(txt)
print(txt)
