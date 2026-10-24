#!/usr/bin/env python3
import csv
from pathlib import Path
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
CSV=ROOT/'outputs/logarithmic_mesoscopic_m2_X10000000.csv'
FIG=ROOT/'figures/logarithmic_mesoscopic_m2_X10000000.png'
with CSV.open(newline='') as f: rows=list(csv.DictReader(f))
theta=[float(r['theta']) for r in rows]
# lambda(2)=-1, so the theorem controls -C_log from below.
signed=[-float(r['C_log_HX']) for r in rows]
lower=[float(r['signed_majority_lower_limit']) for r in rows]
fig,ax=plt.subplots(figsize=(7.4,4.5))
ax.plot(theta,signed,marker='o',label='lambda(2) C_log')
ax.plot(theta,lower,linestyle='--',label='theorem lower bound')
ax.axvline(0.5,linestyle=':',linewidth=1,label='majority threshold exponent 1/2')
ax.set_xlabel('theta')
ax.set_ylabel('signed logarithmic correlation')
ax.set_title('Logarithmic mesoscopic majority, m=2, X=1e7')
ax.grid(alpha=.2)
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig(FIG,dpi=220,bbox_inches='tight')
plt.close(fig)
print(f'wrote {FIG}')
