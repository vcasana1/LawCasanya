#!/usr/bin/env python3
import csv, math
from pathlib import Path
from common import *
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"outputs"; lam=load_liouville()
X=2_000_000; p,q=3,2
lpq=int(lambda_at(lam,[p*q])[0])
cs=[-0.5,-0.1,0.0,0.3,0.6,0.8,1.2,2.0]
rows=[]
for c in cs:
    C=correlation_rational_layer(lam,X,p,q,c)
    if c<0: pred=0.0
    elif c<=q/p: pred=lpq/q
    else: pred=lpq/(p*c)
    rows.append((c,C,C/X,pred,(C-X*pred)/math.sqrt(X)))
with (OUT/"rational_local_profile_3_over_2.csv").open("w",newline="") as f:
    w=csv.writer(f); w.writerow(["p","q","X","c","C","C_over_X","predicted_profile","residual_over_sqrtX"])
    for c,C,cx,pred,res in rows:
        w.writerow([p,q,X,c,C,f"{cx:.12f}",f"{pred:.12f}",f"{res:.12f}"])
with (OUT/"rational_local_profile_3_over_2.txt").open("w") as f:
    f.write("LOCAL PROFILE AROUND log(3/2), X=2,000,000\n")
    f.write("c       C/X            predicted        residual/sqrt(X)\n")
    for c,C,cx,pred,res in rows:
        f.write(f"{c:>4.1f}   {cx: .9f}   {pred: .9f}   {res: .6f}\n")
print((OUT/"rational_local_profile_3_over_2.txt").read_text())
