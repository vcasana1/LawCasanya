#!/usr/bin/env python3
import csv
from pathlib import Path
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
CSV=ROOT/"outputs/rational_local_profile_3_over_2.csv"
FIG=ROOT/"figures/rational_local_profile_3_over_2.png"
with CSV.open(newline="") as f: rows=list(csv.DictReader(f))
c=[float(r["c"]) for r in rows]
y=[float(r["C_over_X"]) for r in rows]
p=[float(r["predicted_profile"]) for r in rows]
fig,ax=plt.subplots(figsize=(7.4,4.5))
ax.plot(c,y,marker="o",label="measured")
ax.plot(c,p,marker="x",label="conditional profile")
ax.set_xlabel("c"); ax.set_ylabel("C_X / X")
ax.set_title("Microscopic profile around log(3/2)")
ax.grid(alpha=.2); ax.legend(frameon=False)
fig.tight_layout(); fig.savefig(FIG,dpi=220,bbox_inches="tight"); plt.close(fig)
print(f"wrote {FIG}")
