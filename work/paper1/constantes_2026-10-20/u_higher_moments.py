#!/usr/bin/env python3
"""Moments <(2u)^{2j}>, j = 1..4, of the ordinal defect u_k(T^c) on I_T, T = 408 392 (training indices only),
and the certificates 1 - <(2u)^{2j}> (lemma: N_0^s >= N - 4^j sum u_k^{2j}). Same definitions as u_defect_scan.py."""
import json, math, sys
import numpy as np
g_all = np.fromfile(sys.argv[1] if len(sys.argv) > 1 else "../../../data/zeross.bin", dtype="<f8")[:1_400_736]
T = math.floor(g_all[-1]/2); sel = (g_all > T) & (g_all <= 2*T); g = g_all[sel]; k = np.nonzero(sel)[0] + 1.0
N0 = lambda t: (0.5*t*np.log(t/(2*np.pi*np.e)) - np.pi/8)/np.pi + 1.0
def primes_upto(n):
    s = np.ones(n + 1, bool); s[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if s[i]: s[i*i::i] = False
    return np.nonzero(s)[0].astype(float)
def S_X(t, X, chunk=40000):
    ps = primes_upto(int(X)); lp, amp = np.log(ps), ps**-0.5; out = np.empty_like(t)
    for i in range(0, t.size, chunk):
        out[i:i+chunk] = -np.angle(1 - amp[None, :]*np.exp(-1j*t[i:i+chunk, None]*lp[None, :])).sum(1)/np.pi
    return out
rows = []
for c in (0.5, 0.25):
    u = (k - 0.5) - N0(g) - S_X(g, T**c)
    for j in (1, 2, 3, 4):
        m = float(((2*u)**(2*j)).mean())
        rows.append({"c": c, "j": j, "moment_(2u)^2j": m, "certificate": 1 - m})
    rows.append({"c": c, "j": "inf", "frac_|u|>=1/2": float((np.abs(u) >= 0.5).mean())})
json.dump({"T": T, "M": int(g.size), "rows": rows}, open("u_higher_moments.json", "w"), indent=1)
lines = [f"T = {T}, #I_T = {g.size}", "   c    j    <(2u)^(2j)>    certificate 1 - <(2u)^(2j)>"]
for r in rows:
    if r["j"] == "inf": lines.append("  %.2f  inf  frac |u|>=1/2 = %.5f" % (r["c"], r["frac_|u|>=1/2"]))
    else: lines.append("  %.2f   %d    %.6f       %.5f" % (r["c"], r["j"], r["moment_(2u)^2j"], r["certificate"]))
txt = "\n".join(lines) + "\n"; open("u_higher_moments.txt", "w").write(txt); print(txt)
