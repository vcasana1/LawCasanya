#!/usr/bin/env python3
"""T-dependence of <u_k(T^c)^2> on dyadic windows I_T = {T < gamma_k <= 2T}, training indices only
(k <= 1 400 736). Same definitions as u_defect_scan.py. Prints <u^2>, a log(1/c), K_emp = difference,
and <u^2> + 1/12 (the weighted mean square of N - F_X over t given by Theorem A with g(y)=y^2)."""
import json, math, sys
import numpy as np
ZEROS = sys.argv[1] if len(sys.argv) > 1 else "../../../data/zeross.bin"
g_all = np.fromfile(ZEROS, dtype="<f8")[:1_400_736]
k_all = np.arange(1, g_all.size + 1, dtype=np.float64)
a = 1 / (2 * math.pi ** 2)
N0 = lambda t: (0.5 * t * np.log(t / (2 * np.pi * np.e)) - np.pi / 8) / np.pi + 1.0
def primes_upto(n):
    s = np.ones(n + 1, dtype=bool); s[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]: s[i * i::i] = False
    return np.nonzero(s)[0]
def S_X(t, X, chunk=40000):
    ps = primes_upto(int(math.floor(X))).astype(np.float64)
    lp, amp = np.log(ps), ps ** -0.5
    out = np.empty_like(t)
    for i in range(0, t.size, chunk):
        z = 1.0 - amp[None, :] * np.exp(-1j * t[i:i + chunk, None] * lp[None, :])
        out[i:i + chunk] = -np.angle(z).sum(axis=1) / np.pi
    return out
rows = []
for T in [12500, 25000, 50000, 100000, 200000, 408392]:
    sel = (g_all > T) & (g_all <= 2 * T)
    g, k = g_all[sel], k_all[sel]
    s = (k - 0.5) - N0(g)
    for c in [0.5, 0.25]:
        u = s - S_X(g, T ** c)
        m2 = float((u ** 2).mean())
        rows.append({"T": T, "loglogT": math.log(math.log(T)), "M": int(g.size), "c": c,
                     "m2": m2, "main": a * math.log(1 / c), "K_emp": m2 - a * math.log(1 / c),
                     "m2_plus_1_12": m2 + 1 / 12, "frac_ge_half": float((np.abs(u) >= 0.5).mean())})
json.dump(rows, open("u_defect_T_dependence.json", "w"), indent=1)
lines = ["      T   loglogT       M     c    <u^2>    a log(1/c)   K_emp    <u^2>+1/12   frac|u|>=1/2"]
for r in rows:
    lines.append("%7d   %.4f  %7d  %.2f  %.5f   %.5f    %+.5f   %.5f      %.5f" %
                 (r["T"], r["loglogT"], r["M"], r["c"], r["m2"], r["main"], r["K_emp"], r["m2_plus_1_12"], r["frac_ge_half"]))
txt = "\n".join(lines) + "\n"
open("u_defect_T_dependence.txt", "w").write(txt); print(txt)
