#!/usr/bin/env python3
import csv, platform
from pathlib import Path
from common import *
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"outputs"; lam=load_liouville()
m=2; X=10_000_000
thetas=[0.0,0.2,0.4,0.45,0.5,0.8]
rows=[]
for theta in thetas:
    c=float(X**theta)
    measured=logarithmic_integer_layer(lam,X,m,c)
    B,n0=resonant_harmonic_mass_integer(X,m,c)
    lower=1-2*theta
    rows.append((theta,c,measured,B,n0,lower))
with (OUT/"logarithmic_mesoscopic_m2_X10000000.csv").open("w",newline="") as f:
    w=csv.writer(f); w.writerow(["X","m","theta","c_X","C_log_HX","resonant_mass","n0","signed_majority_lower_limit"])
    for theta,c,measured,B,n0,lower in rows:
        w.writerow([X,m,theta,f"{c:.12g}",f"{measured:.12f}",f"{B:.12f}",n0,f"{lower:.12f}"])
with (OUT/"logarithmic_mesoscopic_m2_X10000000.txt").open("w") as f:
    f.write("LOGARITHMIC MESOSCOPIC CHECK (H_X NORMALIZATION)\n")
    f.write(f"Python: {platform.python_version()}\n")
    f.write("m=2 X=10,000,000\n")
    f.write("theta      c_X          C_log           resonant mass     1-2theta\n")
    for theta,c,measured,B,n0,lower in rows:
        f.write(f"{theta:>4.2f}  {c:>12.5g}  {measured: .9f}    {B: .9f}     {lower: .9f}\n")
print((OUT/"logarithmic_mesoscopic_m2_X10000000.txt").read_text())
