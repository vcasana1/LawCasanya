from pathlib import Path
import numpy as np
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]
EXPECTED_N = 2_001_052
gamma = np.fromfile(ROOT/"data"/"zeross.bin", dtype=np.float64)
tau = np.fromfile(ROOT/"data"/"zLamb.bin", dtype=np.float64)
if len(gamma) != EXPECTED_N or len(tau) != EXPECTED_N:
    raise ValueError(f"Expected {EXPECTED_N:,} float64 values in both zeross.bin and zLamb.bin; got {len(gamma):,} and {len(tau):,}")
n=EXPECTED_N
k=np.arange(1,n+1,dtype=np.float64); q=k*np.log(k)
z=np.exp(1j*gamma*q); w=np.exp(1j*tau*q); start=2
R=np.abs((z[start+1:]-z[start:-1])-(w[start+1:]-w[start:-1]))
mean_exact=1.799092479842851
rows={"sample_count":len(R),"mean_radius_data":float(R.mean()),
"exact_shark_fin_mean":mean_exact,"mean_deviation":float(R.mean()-mean_exact),
"second_moment_data":float(np.mean(R*R)),"exact_second_moment":4.0,
"second_moment_deviation":float(np.mean(R*R)-4.0)}
pd.DataFrame([rows]).to_csv(ROOT/"outputs"/"lagged_qk_regenerated.csv",index=False)
stats_file=ROOT/'outputs'/'lagged_qk_sharkfin_moments.csv'
if not stats_file.exists():
    raise FileNotFoundError('Run scripts/make_all_results_v2.py first to generate the seeded reference KS diagnostic')
ks=float(pd.read_csv(stats_file).loc[0,'normalized_shape_approx_KS'])
table=f"""\\begin{{center}}
\\begin{{tabular}}{{@{{}}lr@{{}}}}
\\toprule
Quantity & Value\\\\
\\midrule
sample count & ${rows['sample_count']:,}$\\\\
mean radius, data & ${rows['mean_radius_data']:.11f}$\\\\
exact shark-fin mean & ${mean_exact:.12f}$\\\\
mean deviation & ${rows['mean_deviation']:.6e}$\\\\
second moment, data & ${rows['second_moment_data']:.9f}$\\\\
exact second moment & $4$\\\\
second-moment deviation & ${rows['second_moment_deviation']:.6e}$\\\\
normalized-shape KS diagnostic & ${ks:.2e}$\\\\
\\bottomrule
\\end{{tabular}}
\\end{{center}}
"""
(ROOT/"outputs"/"lagged_qk_table.tex").write_text(table,encoding="utf-8")
print(pd.DataFrame([rows]).to_string(index=False))
