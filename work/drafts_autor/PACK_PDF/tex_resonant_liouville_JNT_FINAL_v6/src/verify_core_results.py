#!/usr/bin/env python3
import csv, math, hashlib, platform
from pathlib import Path
import numpy as np
import mpmath as mp
from common import *

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"outputs"; OUT.mkdir(exist_ok=True)
lam=load_liouville()

rows=[]

# Boundary c=1/m.
mp.mp.dps=80
m=2; X=1_000_000; c=mp.mpf("0.5")
alpha=mp.mpf(m)*mp.expm1(c/X)
C_boundary,_=correlation_integer_layer(lam,X,m,float(c))
rows.append(("boundary_m2_X1e6_c0.5",C_boundary))

# Exact left c-independence.
Xleft=10_000_000
left=[]
for cc in [-0.01,-0.40]:
    C,r=correlation_integer_layer(lam,Xleft,2,cc)
    left.append((cc,C,C/Xleft,int(r.min()),int(r.max())))

# Rational fixed resonances.
Xrat=2_000_000
rats=[(3,2),(5,2),(7,2),(2,3),(5,3),(4,3),(5,4)]
rrows=[]
for p,q in rats:
    C=correlation_rational(lam,Xrat,p,q)
    lpq=int(lambda_at(lam,[p*q])[0])
    pred=lpq/q
    resid=(C-Xrat*pred)/math.sqrt(Xrat)
    rrows.append((p,q,C,C/Xrat,pred,resid))

with (OUT/"rational_resonances_X2000000.csv").open("w",newline="") as f:
    w=csv.writer(f); w.writerow(["p","q","X","C","C_over_X","lambda_pq_over_q","residual_over_sqrtX"])
    for p,q,C,cx,pred,resid in rrows:
        w.writerow([p,q,Xrat,C,f"{cx:.12f}",f"{pred:.12f}",f"{resid:.12f}"])

with (OUT/"core_verification.txt").open("w") as f:
    f.write("CORE NUMERICAL VERIFICATION\n")
    f.write(f"Python: {platform.python_version()}\n")
    f.write(f"Binary SHA256: {hashlib.sha256((ROOT/'data/liouville_int8_N21000000.bin').read_bytes()).hexdigest()}\n\n")
    f.write("Endpoint c=1/m\n")
    f.write(f"m=2 X=1000000 c=0.5\n")
    f.write(f"X*alpha_X={mp.nstr(alpha*X,40)}\n")
    f.write(f"C_X={C_boundary}\n\n")
    f.write("Exact left c-independence, m=2, X=10^7\n")
    for cc,C,cx,rmin,rmax in left:
        f.write(f"c={cc:+.2f} C={C} C/X={cx:.9f} offsets={rmin}..{rmax}\n")
    f.write("\nRational resonances, X=2*10^6\n")
    f.write("p/q       C/X             lambda(pq)/q     residual/sqrt(X)\n")
    for p,q,C,cx,pred,resid in rrows:
        f.write(f"{p}/{q:<2}   {cx: .9f}      {pred: .9f}       {resid: .6f}\n")

print((OUT/"core_verification.txt").read_text())
