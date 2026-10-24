from pathlib import Path
import numpy as np
ROOT = Path(__file__).resolve().parents[1]
EXPECTED_N = 2_001_052
gamma = np.fromfile(ROOT/"data"/"zeross.bin", dtype=np.float64)
tau = np.fromfile(ROOT/"data"/"zLamb.bin", dtype=np.float64)
if len(gamma) != EXPECTED_N or len(tau) != EXPECTED_N:
    raise ValueError(f"Expected {EXPECTED_N:,} float64 values in both zeross.bin and zLamb.bin; got {len(gamma):,} and {len(tau):,}")
u = np.array([1.0, np.sqrt(2.0), np.sqrt(3.0), np.sqrt(5.0)])
Delta = (np.exp(1j*u[0]*gamma)-np.exp(1j*u[1]*gamma)
         -np.exp(1j*u[2]*gamma)+np.exp(1j*u[3]*gamma))
R = np.abs(Delta)
with open(ROOT/"outputs"/"shark_fin_index_correlations.txt","w") as f:
    f.write("lag,corr_Rk_Rkpluslag\n")
    for j in range(1,21):
        c = np.corrcoef(R[:-j],R[j:])[0,1]
        f.write(f"{j},{c:.12f}\n")
