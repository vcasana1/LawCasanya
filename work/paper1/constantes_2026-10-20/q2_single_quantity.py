#!/usr/bin/env python3
"""Q_2 = (1/M) int_T^{2T} (N - F_X)^2 dF_X as one quantity, F_X = N0 + S_X, dF_X = (L + S_X') dt.
Measures on a t-grid (training heights only, T = 100 000, window (T, 2T]):
  V_L = (1/M) int E^2 L dt,  C_X = (1/M) int E^2 S_X' dt  (Q_2 = V_L + C_X),  and the zero-side value <u^2> + 1/12.
E = N - N0 - S_X (varpi/pi < 1e-6 omitted). Zeros are read only to evaluate N(t) and u_k."""
import json, math, sys
import numpy as np
g_all = np.fromfile(sys.argv[1] if len(sys.argv) > 1 else "../../../data/zeross.bin", dtype="<f8")[:1_400_736]
T = 100000.0; H = 0.01
N0 = lambda t: (0.5*t*np.log(t/(2*np.pi*np.e)) - np.pi/8)/np.pi + 1.0
LL = lambda t: np.log(t/(2*np.pi))/(2*np.pi)
def primes_upto(n):
    s = np.ones(n + 1, bool); s[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if s[i]: s[i*i::i] = False
    return np.nonzero(s)[0].astype(float)
def SX_and_d(t, X, chunk=20000):
    ps = primes_upto(int(X)); lp, amp = np.log(ps), ps**-0.5
    S, dS = np.empty_like(t), np.empty_like(t)
    for i in range(0, t.size, chunk):
        z = amp[None, :]*np.exp(-1j*t[i:i+chunk, None]*lp[None, :])
        S[i:i+chunk] = -np.angle(1 - z).sum(1)/np.pi
        dS[i:i+chunk] = -np.imag(1j*lp[None, :]*z/(1 - z)).sum(1)/np.pi
    return S, dS
t = np.arange(T + H/2, 2*T, H)
Nt = np.searchsorted(g_all, t, side="right").astype(float)
sel = (g_all > T) & (g_all <= 2*T); g = g_all[sel]; k = np.nonzero(sel)[0] + 1.0; M = g.size
rows = []
for c in (0.5, 0.25):
    X = T**c
    S, dS = SX_and_d(t, X)
    E = Nt - N0(t) - S
    VL = float((E**2*LL(t)).sum()*H/M); CX = float((E**2*dS).sum()*H/M)
    Sg, _ = SX_and_d(g, X); u = (k - 0.5) - N0(g) - Sg
    rows.append({"c": c, "X": X, "M": int(M), "V_L": VL, "C_X": CX, "Q2_t_side": VL + CX,
                 "Q2_zero_side": float((u**2).mean() + 1/12), "mean_E2_t": float((E**2).mean()),
                 "corr_E2_dS": float(np.corrcoef(E**2, dS)[0, 1])})
json.dump(rows, open("q2_single_quantity.json", "w"), indent=1)
lines = ["T = 100000, grid step 0.01, window (T,2T]",
         "    c     V_L=(1/M)int E^2 L   C_X=(1/M)int E^2 S_X'   Q_2 (t-side)   Q_2=<u^2>+1/12 (zeros)   corr(E^2,S_X')"]
for r in rows:
    lines.append("  %.2f     %.5f              %+.5f              %.5f        %.5f                  %+.4f" %
                 (r["c"], r["V_L"], r["C_X"], r["Q2_t_side"], r["Q2_zero_side"], r["corr_E2_dS"]))
txt = "\n".join(lines) + "\n"; open("q2_single_quantity.txt", "w").write(txt); print(txt)
