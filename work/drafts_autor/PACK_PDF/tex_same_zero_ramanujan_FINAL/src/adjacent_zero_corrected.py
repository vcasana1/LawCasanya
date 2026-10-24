from pathlib import Path
import numpy as np
import pandas as pd

BASE = Path(__file__).resolve().parents[1]
OUT = BASE / "outputs"
OUT.mkdir(exist_ok=True)

V_GUE = 3*np.pi/8 - 1
V_GOE = 4/np.pi - 1
EXPECTED_N = 2_001_052

def rho_pred(T, x2=1.0):
    return 1 - np.pi**2 * V_GUE / (x2*np.log(np.log(T)))

print("V_GUE_Wigner =", V_GUE)
print("V_GOE_Wigner =", V_GOE)
for T in [1e6,1e12,1e30]:
    print("T =", T, "rho(X2=1) =", rho_pred(T,1.0),
          "rho(X2=0.848888) =", rho_pred(T,0.848888))

gamma_file = BASE / "data" / "zeross.bin"
tau_file = BASE / "data" / "zLamb.bin"
if gamma_file.exists() and tau_file.exists():
    gamma = np.memmap(gamma_file, dtype=np.float64, mode="r")
    tau = np.memmap(tau_file, dtype=np.float64, mode="r")
    if len(gamma) != EXPECTED_N or len(tau) != EXPECTED_N:
        raise ValueError(f"Expected {EXPECTED_N:,} float64 values in both zeross.bin and zLamb.bin; got {len(gamma):,} and {len(tau):,}")
    gamma = np.asarray(gamma)
    tau = np.asarray(tau)
    sigma = np.sqrt(2*np.log(np.log(tau))) / np.log(tau/(2*np.pi))
    X = (gamma-tau)/sigma
    x0, x1 = X[:-1], X[1:]
    rho_emp = np.corrcoef(x0,x1)[0,1]
    D = np.sqrt(np.log(np.log(tau[:-1]))) * (x1-x0)
    L = np.log(tau[:-1]/(2*np.pi))
    gap = (gamma[1:]-gamma[:-1]) / (2*np.pi/L)
    res = pd.DataFrame([{
        "pairs": len(x0),
        "mean_X2_full_prefix": np.mean(X*X),
        "rho_empirical": rho_emp,
        "var_D": np.var(D),
        "mean_D": np.mean(D),
        "min_D": np.min(D),
        "var_normalized_gap": np.var(gap),
        "mean_normalized_gap": np.mean(gap),
        "algebraic_rhs_using_empirical_X2":
            np.mean(X*X)*np.mean(np.log(np.log(tau[:-1])))/np.pi**2*(1-rho_emp),
    }])
    res.to_csv(OUT/"adjacent_zero_empirical.csv", index=False)
    print(res.to_string(index=False))
else:
    print("Data files not present. Put zeross.bin and zLamb.bin in data/ to run empirical adjacent-zero calculations.")
