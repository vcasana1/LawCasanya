#!/usr/bin/env python3
import csv
from pathlib import Path
import numpy as np
from common import *
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"outputs"; lam=load_liouville()
m=2; X=10_000_000
cs=[0.10,0.25,0.49,0.50,0.60,0.75,0.90,0.99,1.00,1.50]
rows=[]
for c in cs:
    C,_=correlation_integer_layer(lam,X,m,c)
    alpha=np.longdouble(m)*np.expm1(np.longdouble(str(c))/np.longdouble(X))
    I0=min(X,int(np.ceil(np.longdouble(1)/alpha)-1))
    finite=max(0,2*I0-X)/X
    asymp=max(0.0,2*min(1.0,1/(m*c))-1)
    rows.append((c,C,abs(C)/X,I0,finite,asymp))
with (OUT/"natural_majority_m2_X10000000.csv").open("w",newline="") as f:
    w=csv.writer(f); w.writerow(["m","X","c","C","absC_over_X","I0","finite_lower_over_X","asymptotic_lower"])
    for row in rows:w.writerow([m,X,*row])
with (OUT/"natural_majority_m2_X10000000.txt").open("w") as f:
    f.write("UNCONDITIONAL NATURAL MAJORITY CHECK\n")
    f.write("m=2 X=10,000,000\n")
    f.write("c      |C|/X        I0          finite lower/X   asymptotic lower\n")
    for c,C,ratio,I0,finite,asymp in rows:
        f.write(f"{c:0.2f}   {ratio: .9f}  {I0:8d}    {finite: .9f}       {asymp: .9f}\n")
print((OUT/"natural_majority_m2_X10000000.txt").read_text())
