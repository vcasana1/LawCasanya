#!/usr/bin/env python3
"""Joint extremal problem: Lamzouri's certificate (arXiv:2609.02882, Prop. 2.1 + Lemma 3.1) with a kernel of support
(-lambda, lambda), lambda > 1/2 allowed, under the hypothesis H(b): int_1^inf F(alpha) alpha^-2 d alpha <= b (F >= 0),
compared with the defect certificate 4/3 - 4 Q_2 under the same b (Parseval heuristic Q_2 = a(log(1/c) + b), c = 1/2).

Lamzouri: N_0^s/N >= 2 - Phi(phi), phi = eta^2 >= 0 even, supp in (-lambda, lambda), int phi = 1, Q = phi * phi,
  Phi = Q(0) + 2 int_0^1 alpha Q + 2 int_1^{2 lambda} F Q  <=  Q(0) + 2 int_0^1 alpha Q + 2 b max_{[1,2lambda]} alpha^2 Q.
Check: lambda = 1/2 gives Montgomery-Taylor C_MT = 1.32750 (certificate 0.67250)."""
import json, math
import numpy as np
from scipy.optimize import minimize

def solve(lam, b, n=120):
    h = lam/n
    u = (np.arange(-n, n + 1))*h                       # grid for eta, 2n+1 points
    al = (np.arange(-2*n, 2*n + 1))*h                  # grid for Q
    i0 = 2*n
    sel01 = (al >= 0) & (al <= 1); w01 = np.where(np.isclose(al[sel01], 0) | np.isclose(al[sel01], 1), 0.5, 1.0)
    selT = al >= 1 - 1e-12
    def full(x):  # even extension, x = eta at u = 0..lam (n+1 values), last forced 0
        e = np.concatenate([x[:0:-1], x]); return e
    def Qof(x):
        phi = full(x)**2
        phi = phi/(phi.sum()*h)
        return np.convolve(phi, phi)*h
    def parts(x):
        Q = Qof(x)
        lin = Q[i0] + 2*np.sum(al[sel01]*Q[sel01]*w01)*h
        tail = np.max(al[selT]**2*Q[selT]) if selT.any() else 0.0
        return lin, tail
    def obj(z):
        lin, _ = parts(z[:-1]); return lin + 2*b*z[-1]
    cons = []
    if selT.any():
        cons.append({"type": "ineq", "fun": lambda z: z[-1] - al[selT]**2*Qof(z[:-1])[selT]})
    x0 = np.cos(math.sqrt(2)*np.minimum(np.arange(n + 1)*h, 0.5))**0.5*(np.arange(n + 1)*h < min(lam, 0.5))
    x0 = x0 + 1e-3
    z0 = np.concatenate([x0, [parts(x0)[1]]])
    bnds = [(None, None)]*n + [(0, 0)] + [(0, None)]  # eta(lam) = 0
    r = minimize(obj, z0, method="SLSQP", constraints=cons, bounds=bnds, options={"maxiter": 400, "ftol": 1e-10})
    lin, tail = parts(r.x[:-1])
    Phi = lin + 2*b*tail
    return {"lambda": lam, "b": b, "Phi": float(Phi), "certificate": float(2 - Phi), "Q0_plus_lin": float(lin),
            "tail_max_alpha2Q": float(tail), "ok": bool(r.success)}

a = 1/(2*math.pi**2)
check = solve(0.5, 0.0)
rows = []
for b in [0.5, 1.0, 1.5, 2.0, 2.597, 3.0]:
    best = max((solve(lam, b) for lam in [0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.25, 1.5]), key=lambda r: r["certificate"])
    ours = 4/3 - 4*a*(math.log(2) + b)
    rows.append({"b": b, "lamzouri_extended": best, "defect_certificate_c_half": ours})
json.dump({"MT_check": check, "rows": rows}, open("joint_extremal.json", "w"), indent=1)
lines = ["Check lambda = 1/2: Phi = %.5f (C_MT = 1.32750), certificate %.5f (0.67250)" % (check["Phi"], check["certificate"]), "",
         "   b     Lamzouri, best lambda   certificate     defect cert. (c=1/2)   max of the two"]
for r in rows:
    L = r["lamzouri_extended"]; d = r["defect_certificate_c_half"]
    lines.append(" %5.3f      %.2f              %.5f          %.5f               %.5f" % (r["b"], L["lambda"], L["certificate"], d, max(d, L["certificate"])))
txt = "\n".join(lines) + "\n"; open("joint_extremal.txt", "w").write(txt); print(txt)
