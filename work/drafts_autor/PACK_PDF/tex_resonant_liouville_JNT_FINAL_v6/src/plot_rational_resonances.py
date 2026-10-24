#!/usr/bin/env python3
import csv
from pathlib import Path
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
CSV=ROOT/"outputs/rational_resonances_X2000000.csv"
FIG=ROOT/"figures/rational_resonances_X2000000.png"
with CSV.open(newline="") as f: rows=list(csv.DictReader(f))
x=[f"{r['p']}/{r['q']}" for r in rows]
y=[float(r["C_over_X"]) for r in rows]
p=[float(r["lambda_pq_over_q"]) for r in rows]
fig,ax=plt.subplots(figsize=(7.4,4.5))
ax.plot(x,y,marker="o",label="measured")
ax.plot(x,p,marker="x",label="conditional main term")
ax.set_xlabel("p/q"); ax.set_ylabel("normalized correlation")
ax.set_title("Rational Liouville resonances, X=2e6")
ax.grid(alpha=.2); ax.legend(frameon=False)
fig.tight_layout(); fig.savefig(FIG,dpi=220,bbox_inches="tight"); plt.close(fig)
print(f"wrote {FIG}")
