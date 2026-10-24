#!/usr/bin/env python3
"""Complete reproducibility script for VIOLET_THREAD_V3.

This single script regenerates every numerical CSV/TeX output and all twenty
PNG figures in the archive from data/zeross.bin and data/zLamb.bin.
It uses all 2,001,052 ordinates for the global RVM/phase diagnostics and
recomputes the detailed first-49 zeta lobe geometry and Euclidean arc lengths.
"""
from pathlib import Path
import numpy as np
import pandas as pd
import mpmath as mp
from scipy.optimize import minimize_scalar
from scipy.special import ellipe
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "outputs"
FIG = ROOT / "figures"
OUT.mkdir(exist_ok=True)
FIG.mkdir(exist_ok=True)

GAMMA = np.fromfile(DATA / "zeross.bin", dtype=np.float64)
TAU = np.fromfile(DATA / "zLamb.bin", dtype=np.float64)
if len(GAMMA) != 2_001_052 or len(TAU) != 2_001_052:
    raise RuntimeError("Expected 2,001,052 ordinates in each binary file.")

mp.mp.dps = 28


def theta_asym(t):
    t = np.asarray(t, dtype=np.float64)
    return (
        0.5*t*np.log(t/(2*np.pi)) - 0.5*t - np.pi/8
        + 1/(48*t) + 7/(5760*t**3) + 31/(80640*t**5)
    )


def theta_exact(t):
    return float(mp.siegeltheta(float(t)))


def theta_prime_asym(t):
    t = float(t)
    return (
        0.5*np.log(t/(2*np.pi))
        - 1/(48*t**2)
        - 21/(5760*t**4)
        - 155/(80640*t**6)
    )


def theta0(z):
    z = np.asarray(z, dtype=np.complex128)
    return 0.5*z*np.log(z/(2*np.pi*np.e)) - np.pi/8


def zeta_line(t):
    return complex(mp.zeta(0.5 + 1j*float(t)))


def zeta_abs(t):
    return float(abs(mp.zeta(0.5 + 1j*float(t))))


def arc_speed(t):
    s = 0.5 + 1j*t
    zp = mp.diff(lambda z: mp.zeta(z), s)
    return mp.sqrt(1 + abs(zp)**2)


# -----------------------------------------------------------------------------
# 1. Full 2,001,052-ordinate RVM/phase diagnostics.
# -----------------------------------------------------------------------------
theta_g = theta_asym(GAMMA)
s_full = np.diff(theta_g)/np.pi
delta_rvm = GAMMA - TAU

full_summary = pd.DataFrame({
    "quantity": [
        "number_of_ordinates", "number_of_zero_intervals",
        "gamma_1", "gamma_N", "tau_1", "tau_N",
        "mean_gamma_minus_tau", "std_gamma_minus_tau",
        "rms_gamma_minus_tau", "max_abs_gamma_minus_tau",
        "mean_phase_spacing_s", "std_phase_spacing_s",
        "min_phase_spacing_s", "max_phase_spacing_s",
        "q01_phase_spacing_s", "q99_phase_spacing_s",
    ],
    "value": [
        len(GAMMA), len(GAMMA)-1,
        GAMMA[0], GAMMA[-1], TAU[0], TAU[-1],
        delta_rvm.mean(), delta_rvm.std(ddof=1),
        np.sqrt(np.mean(delta_rvm**2)), np.max(np.abs(delta_rvm)),
        s_full.mean(), s_full.std(ddof=1), s_full.min(), s_full.max(),
        np.quantile(s_full, 0.01), np.quantile(s_full, 0.99),
    ],
})
full_summary.to_csv(OUT / "full_dataset_summary.csv", index=False)

idx = np.unique(np.r_[np.arange(100), np.linspace(0, len(GAMMA)-1, 2000).astype(int)])
pd.DataFrame({
    "n": idx+1,
    "gamma_n": GAMMA[idx],
    "tau_n": TAU[idx],
    "gamma_minus_tau": delta_rvm[idx],
}).to_csv(OUT / "full_dataset_sampled_ordinates.csv", index=False)

# -----------------------------------------------------------------------------
# 2. Recompute first-49 Euclidean arc observables from the raw zero ordinates.
# -----------------------------------------------------------------------------
arc_rows = []
for j in range(49):
    a = float(GAMMA[j]); b = float(GAMMA[j+1]); gap = b-a
    L = float(mp.quad(arc_speed, [a, b]))
    R = L/gap
    opt = minimize_scalar(
        lambda x: -zeta_abs(x), bounds=(a, b), method="bounded",
        options={"xatol": 1e-11, "maxiter": 300},
    )
    A = -float(opt.fun)
    Omega = theta_exact(b) - theta_exact(a)
    s_phase = Omega/np.pi
    mid = 0.5*(a+b)
    aa = np.pi*A/gap
    bb = A*theta_prime_asym(mid)
    mpar = (aa*aa-bb*bb)/(1+aa*aa)
    Rarch = (2/np.pi)*np.sqrt(1+aa*aa)*ellipe(mpar)
    arc_rows.append({
        "n": j+1,
        "gamma_n": a,
        "gamma_n_plus_1": b,
        "gap": gap,
        "L_n": L,
        "R_n": R,
        "s_n_phase": s_phase,
        "A_n_max_abs_Z": A,
        "R_n_sine_arch": Rarch,
        "R_n_minus_sine_arch": R-Rarch,
    })

arc = pd.DataFrame(arc_rows)
arc.to_csv(OUT / "first_49_arc_metrics_recomputed.csv", index=False)
arc_summary = pd.DataFrame({
    "quantity": ["corr_R_gap", "corr_R_s", "corr_R_A", "corr_L_A", "corr_R_arch", "rmse_arch"],
    "value": [
        np.corrcoef(arc["R_n"], arc["gap"])[0,1],
        np.corrcoef(arc["R_n"], arc["s_n_phase"])[0,1],
        np.corrcoef(arc["R_n"], arc["A_n_max_abs_Z"])[0,1],
        np.corrcoef(arc["L_n"], arc["A_n_max_abs_Z"])[0,1],
        np.corrcoef(arc["R_n"], arc["R_n_sine_arch"])[0,1],
        np.sqrt(np.mean(arc["R_n_minus_sine_arch"]**2)),
    ],
})
arc_summary.to_csv(OUT / "arc_recomputed_summary.csv", index=False)

# -----------------------------------------------------------------------------
# 3. Eccentric lobe geometry in uniform phase coordinate.
# -----------------------------------------------------------------------------
lobe_rows = []
lobe_curves = {}
for j in range(49):
    a, b = float(GAMMA[j]), float(GAMMA[j+1])
    tha, thb = theta_exact(a), theta_exact(b)
    Omega = thb-tha
    q = np.linspace(0.0, 1.0, 321)

    tdense = np.linspace(a, b, 1601)
    thdense = np.array([theta_exact(x) for x in tdense])
    tq = np.interp(tha + q*Omega, thdense, tdense)
    w = np.array([zeta_line(x) for x in tq])
    thq = np.array([theta_exact(x) for x in tq])
    Zq = np.real(w*np.exp(1j*thq))
    eps = np.sign(Zq[len(Zq)//2]) or 1.0

    what = eps*np.exp(1j*tha)*w
    A = float(arc.loc[j, "A_n_max_abs_Z"])
    C = np.trapezoid(what, q)
    E = 2*np.abs(C)/A
    D = np.sqrt(np.trapezoid((np.abs(what-C)-np.abs(C))**2, q))/A

    s = Omega/np.pi
    if abs(1-s*s) < 1e-10:
        cmodel = -0.5j
    else:
        cmodel = (1 + np.exp(-1j*np.pi*s))/(np.pi*(1-s*s))
    Epred = 2*abs(cmodel)

    arch = A*np.sin(np.pi*q)*np.exp(-1j*Omega*q)
    shape_rmse = np.sqrt(np.trapezoid(np.abs(what-arch)**2, q))/A
    centroid_error = np.abs(C/A-cmodel)

    lobe_rows.append({
        "n": j+1, "gamma_n": a, "gamma_n_plus_1": b,
        "Omega_n": Omega, "s_n": s, "A_n": A,
        "C_n_real": C.real, "C_n_imag": C.imag, "C_n_abs": abs(C),
        "E_n_2absC_over_A": E,
        "D_n_normalized_circle_tangency_defect": D,
        "model_centroid_real_over_A": cmodel.real,
        "model_centroid_imag_over_A": cmodel.imag,
        "centroid_model_error": centroid_error,
        "normalized_arch_shape_rmse": shape_rmse,
        "E_n_arch_prediction": Epred,
        "E_n_minus_arch_prediction": E-Epred,
    })
    lobe_curves[j+1] = (q, what/A, arch/A, C/A)

lobes = pd.DataFrame(lobe_rows)
lobes.to_csv(OUT / "first_49_eccentric_lobe_metrics.csv", index=False)
lobe_summary = pd.DataFrame({
    "quantity": [
        "mean_E_n", "std_E_n", "median_E_n", "mean_D_n", "median_D_n",
        "mean_centroid_model_error", "mean_normalized_arch_shape_rmse",
        "corr_E_with_s", "corr_D_with_abs_s_minus_1",
        "corr_actual_vs_arch_E", "rmse_actual_vs_arch_E", "mae_actual_vs_arch_E",
    ],
    "value": [
        lobes["E_n_2absC_over_A"].mean(),
        lobes["E_n_2absC_over_A"].std(ddof=1),
        lobes["E_n_2absC_over_A"].median(),
        lobes["D_n_normalized_circle_tangency_defect"].mean(),
        lobes["D_n_normalized_circle_tangency_defect"].median(),
        lobes["centroid_model_error"].mean(),
        lobes["normalized_arch_shape_rmse"].mean(),
        np.corrcoef(lobes["E_n_2absC_over_A"], lobes["s_n"])[0,1],
        np.corrcoef(lobes["D_n_normalized_circle_tangency_defect"], np.abs(lobes["s_n"]-1))[0,1],
        np.corrcoef(lobes["E_n_2absC_over_A"], lobes["E_n_arch_prediction"])[0,1],
        np.sqrt(np.mean(lobes["E_n_minus_arch_prediction"]**2)),
        np.mean(np.abs(lobes["E_n_minus_arch_prediction"])),
    ],
})
lobe_summary.to_csv(OUT / "eccentric_lobe_summary.csv", index=False)

# -----------------------------------------------------------------------------
# 4. TeX appendix tables.
# -----------------------------------------------------------------------------
with open(OUT / "arc_metrics_table.tex", "w") as f:
    for _, r in arc.iterrows():
        f.write(
            f"{int(r.n)} & {r.gamma_n:.9f} & {r.gamma_n_plus_1:.9f} & "
            f"{r.gap:.6f} & {r.L_n:.6f} & {r.R_n:.6f} & {r.s_n_phase:.6f} \\\\\n"
        )
with open(OUT / "eccentric_lobe_table.tex", "w") as f:
    for _, r in lobes.iterrows():
        f.write(
            f"{int(r.n)} & {r.s_n:.6f} & {r.A_n:.6f} & {r.C_n_real:.6f} & "
            f"{r.C_n_imag:.6f} & {r.E_n_2absC_over_A:.6f} & "
            f"{r.D_n_normalized_circle_tangency_defect:.6f} & {r.E_n_arch_prediction:.6f} \\\\\n"
        )

# -----------------------------------------------------------------------------
# 5. PNG figures.
# -----------------------------------------------------------------------------
tgrid = np.linspace(GAMMA[0], GAMMA[49], 3000)
wgrid = np.array([zeta_line(x) for x in tgrid])

fig = plt.figure(figsize=(11,7))
ax = fig.add_subplot(111, projection="3d")
ax.plot(tgrid, wgrid.real, wgrid.imag, lw=1.15)
ax.plot([GAMMA[0], GAMMA[49]], [0,0], [0,0], lw=0.9)
ax.scatter(GAMMA[:50], np.zeros(50), np.zeros(50), s=18)
ax.set_xlabel(r"$t$"); ax.set_ylabel(r"$\Re\,\zeta(1/2+it)$"); ax.set_zlabel(r"$\Im\,\zeta(1/2+it)$")
ax.set_title("Euclidean zeta thread over the first 50 zeros")
ax.view_init(elev=22, azim=-61)
fig.tight_layout(); fig.savefig(FIG/"fig01_euclidean_zeta_thread.png", dpi=220, bbox_inches="tight"); plt.close(fig)

fig, ax = plt.subplots(figsize=(8,8))
ax.plot(wgrid.real, wgrid.imag, lw=0.9); ax.scatter([0],[0],s=35)
ax.axhline(0,lw=0.6); ax.axvline(0,lw=0.6); ax.set_aspect("equal", adjustable="datalim")
ax.set_xlabel(r"$\Re\,\zeta(1/2+it)$"); ax.set_ylabel(r"$\Im\,\zeta(1/2+it)$")
ax.set_title("Transverse projection: zeros are pinch points, not lobe centers")
ax.grid(True,alpha=0.2); fig.tight_layout(); fig.savefig(FIG/"fig02_transverse_eccentric_lobes.png",dpi=220,bbox_inches="tight"); plt.close(fig)

fig, ax = plt.subplots(figsize=(8,8))
for n in [8,14,25,33,46]:
    q, actual, model, c = lobe_curves[n]
    ax.plot(actual.real, actual.imag, lw=1.1, label=f"lobe {n}")
ax.scatter([0],[0],s=28); ax.set_aspect("equal",adjustable="datalim")
ax.set_xlabel("normalized rotated real part"); ax.set_ylabel("normalized rotated imaginary part")
ax.set_title("Five actual lobes after phase rotation and amplitude normalization")
ax.grid(True,alpha=0.2); ax.legend(fontsize=8); fig.tight_layout(); fig.savefig(FIG/"fig03_normalized_actual_lobes.png",dpi=220,bbox_inches="tight"); plt.close(fig)

phi=np.linspace(0,np.pi,500); A=1.0; lam=1.0
fig, ax = plt.subplots(figsize=(8,8))
for delta in [-0.35,0.0,0.25,0.6]:
    z=-0.5j*A+0.5j*A*np.exp(-2*lam*delta)*np.exp(-2j*phi)
    ax.plot(z.real,z.imag,lw=1.3,label=rf"$\delta={delta}$")
ax.scatter([0],[0],s=35); ax.set_aspect("equal",adjustable="box")
ax.set_xlabel("real part"); ax.set_ylabel("imaginary part")
ax.set_title("Exact no-exit of the eccentric circular lobe under the first-order flow")
ax.grid(True,alpha=0.2); ax.legend(); fig.tight_layout(); fig.savefig(FIG/"fig04_circular_lobe_first_order_no_exit.png",dpi=220,bbox_inches="tight"); plt.close(fig)

fig, ax = plt.subplots(figsize=(9.5,5.5))
ax.plot(lobes["n"],lobes["E_n_2absC_over_A"],marker="o",ms=3,lw=1.0,label=r"$E_n=2|C_n|/A_n$")
ax.axhline(1,lw=0.9,ls="--",label="tangent-circle value")
ax.set_xlabel(r"$n$"); ax.set_ylabel(r"$E_n$"); ax.set_title("Normalized lobe eccentricity for the first 49 intervals")
ax.grid(True,alpha=0.2); ax.legend(); fig.tight_layout(); fig.savefig(FIG/"fig05_eccentricity_En.png",dpi=220,bbox_inches="tight"); plt.close(fig)

fig, ax = plt.subplots(figsize=(9.5,5.5))
ax.plot(lobes["n"],lobes["D_n_normalized_circle_tangency_defect"],marker="o",ms=3,lw=1.0)
ax.set_xlabel(r"$n$"); ax.set_ylabel(r"$D_n$")
ax.set_title("Normalized defect from a circle centered at the lobe centroid and tangent to the origin")
ax.grid(True,alpha=0.2); fig.tight_layout(); fig.savefig(FIG/"fig06_circle_tangency_defect_Dn.png",dpi=220,bbox_inches="tight"); plt.close(fig)

fig, ax = plt.subplots(figsize=(9.5,5.5))
ax.hist(s_full,bins=180,density=True); ax.axvline(1,lw=1.0,ls="--"); ax.set_xlim(0,3.35)
ax.set_xlabel(r"$s_n=[\vartheta(\gamma_{n+1})-\vartheta(\gamma_n)]/\pi$"); ax.set_ylabel("density")
ax.set_title("Phase-unfolded lobe sweep: all 2,001,051 intervals")
fig.tight_layout(); fig.savefig(FIG/"fig07_full_phase_spacing_histogram.png",dpi=220,bbox_inches="tight"); plt.close(fig)

fig, ax = plt.subplots(figsize=(10,5.5)); stride=500
ax.plot(np.arange(1,len(GAMMA)+1,stride),delta_rvm[::stride],lw=0.7); ax.axhline(0,lw=0.8)
ax.set_xlabel(r"$n$ (every 500th ordinate shown)"); ax.set_ylabel(r"$\gamma_n-\tau_n$")
ax.set_title("Zeta minus RVM/Lambert ordinates across all 2,001,052 entries")
ax.grid(True,alpha=0.15); fig.tight_layout(); fig.savefig(FIG/"fig08_full_zeta_minus_rvm_lambert.png",dpi=220,bbox_inches="tight"); plt.close(fig)

fig, ax = plt.subplots(figsize=(7.3,6.0))
ax.scatter(lobes["s_n"],lobes["E_n_2absC_over_A"],s=36); ax.axhline(1,lw=0.8,ls="--")
ax.set_xlabel(r"$s_n=\Omega_n/\pi$"); ax.set_ylabel(r"$E_n=2|C_n|/A_n$")
ax.set_title("Eccentricity versus RVM-phase lobe sweep")
ax.grid(True,alpha=0.2); fig.tight_layout(); fig.savefig(FIG/"fig09_eccentricity_vs_phase_sweep.png",dpi=220,bbox_inches="tight"); plt.close(fig)

fig, ax = plt.subplots(figsize=(9.5,5.4)); ax.plot(arc["n"],arc["L_n"],marker="o",ms=3,lw=1.0)
ax.set_xlabel(r"$n$"); ax.set_ylabel(r"$L_n$"); ax.set_title("Zero-to-zero Euclidean arc length: first 49 intervals")
ax.grid(True,alpha=0.2); fig.tight_layout(); fig.savefig(FIG/"fig10_arc_length_Ln.png",dpi=220,bbox_inches="tight"); plt.close(fig)

fig, ax = plt.subplots(figsize=(9.5,5.4)); ax.plot(arc["n"],arc["R_n"],marker="o",ms=3,lw=1.0)
ax.set_xlabel(r"$n$"); ax.set_ylabel(r"$R_n$"); ax.set_title("Arc-length inflation ratio: first 49 intervals")
ax.grid(True,alpha=0.2); fig.tight_layout(); fig.savefig(FIG/"fig11_arc_ratio_Rn.png",dpi=220,bbox_inches="tight"); plt.close(fig)

fig, ax = plt.subplots(figsize=(6.5,6.0)); ax.scatter(arc["R_n_sine_arch"],arc["R_n"],s=34)
lo=min(arc["R_n_sine_arch"].min(),arc["R_n"].min()); hi=max(arc["R_n_sine_arch"].max(),arc["R_n"].max())
ax.plot([lo,hi],[lo,hi],ls="--",lw=1.0); ax.set_xlabel(r"$R_n^{(\mathrm{arch})}$"); ax.set_ylabel(r"$R_n$")
ax.set_title("One-arch elliptic reduction of the recomputed arc ratio")
ax.grid(True,alpha=0.2); fig.tight_layout(); fig.savefig(FIG/"fig12_elliptic_arch_prediction.png",dpi=220,bbox_inches="tight"); plt.close(fig)

tr=np.linspace(TAU[0],TAU[49],3500); th0=theta0(tr).real; m=np.cos(th0)*np.exp(-1j*th0)
fig=plt.figure(figsize=(11,7)); ax=fig.add_subplot(111,projection="3d")
ax.plot(tr,m.real,m.imag,lw=1.15); ax.plot([TAU[0],TAU[49]],[0,0],[0,0],lw=0.9); ax.scatter(TAU[:50],np.zeros(50),np.zeros(50),s=18)
ax.set_xlabel(r"$t$"); ax.set_ylabel(r"$\Re\,M_0(t)$"); ax.set_zlabel(r"$\Im\,M_0(t)$")
ax.set_title("RVM/Lambert phase skeleton: exact eccentric tangent-circle lobes"); ax.view_init(elev=22,azim=-61)
fig.tight_layout(); fig.savefig(FIG/"fig13_rvm_tangent_circle_thread.png",dpi=220,bbox_inches="tight"); plt.close(fig)

fig, ax=plt.subplots(figsize=(6.5,6.0)); ax.scatter(lobes["E_n_arch_prediction"],lobes["E_n_2absC_over_A"],s=36)
lo=min(lobes["E_n_arch_prediction"].min(),lobes["E_n_2absC_over_A"].min()); hi=max(lobes["E_n_arch_prediction"].max(),lobes["E_n_2absC_over_A"].max())
ax.plot([lo,hi],[lo,hi],ls="--",lw=1.0); ax.set_xlabel(r"one-arch prediction $E_n^{(\mathrm{arch})}$"); ax.set_ylabel(r"measured $E_n$")
ax.set_title("Measured eccentricity versus RVM-phase one-arch prediction")
ax.grid(True,alpha=0.2); fig.tight_layout(); fig.savefig(FIG/"fig14_eccentricity_model_vs_actual.png",dpi=220,bbox_inches="tight"); plt.close(fig)

D=np.linspace(-0.49,0.49,600); fig,ax=plt.subplots(figsize=(9,5.5))
for tt in [20,50,100,1000]:
    bound=0.5*np.abs((tt/(2*np.pi))**(-D)-1); ax.plot(D,bound,lw=1.1,label=rf"$t={tt}$")
ax.set_xlabel(r"$\delta$"); ax.set_ylabel("rigorous lower bound for the RVM model modulus")
ax.set_title("RVM tangent-circle no-exit barrier"); ax.grid(True,alpha=0.2); ax.legend()
fig.tight_layout(); fig.savefig(FIG/"fig15_rvm_no_exit_barrier.png",dpi=220,bbox_inches="tight"); plt.close(fig)

print(full_summary.to_string(index=False))
print(arc_summary.to_string(index=False))
print(lobe_summary.to_string(index=False))

# -----------------------------------------------------------------------------
# 6. Additional Version 3 geometry figures (16--20).
# -----------------------------------------------------------------------------
# Overlay
tz = np.linspace(float(GAMMA[0]), float(GAMMA[49]), 2600)
wz = np.array([zeta_line(x) for x in tz])
tr = np.linspace(float(TAU[0]), float(TAU[49]), 2600)
th0 = theta0(tr).real
wr = np.cos(th0)*np.exp(-1j*th0)
fig = plt.figure(figsize=(12, 7.5))
ax = fig.add_subplot(111, projection="3d")
ax.plot(tz, wz.real, wz.imag, lw=1.05, label="zeta thread")
ax.plot(tr, wr.real, wr.imag, lw=1.15, label="RVM tangent-circle skeleton")
ax.scatter(GAMMA[:50], np.zeros(50), np.zeros(50), s=12)
ax.scatter(TAU[:50], np.zeros(50), np.zeros(50), s=12)
ax.set_xlabel(r"$t$")
ax.set_ylabel("real part")
ax.set_zlabel("imaginary part")
ax.set_title("Actual zeta lobes and the RVM/Lambert tangent-circle skeleton")
ax.view_init(elev=21, azim=-62)
ax.legend(fontsize=8)
fig.tight_layout()
fig.savefig(FIG/"fig16_zeta_rvm_overlay_3d.png", dpi=220, bbox_inches="tight")
plt.close(fig)

# Representative lobe
n = 8
a, b = float(GAMMA[n-1]), float(GAMMA[n])
th_a, th_b = theta_exact(a), theta_exact(b)
Omega = th_b-th_a
q = np.linspace(0, 1, 601)
tdense = np.linspace(a, b, 2601)
thdense = np.array([theta_exact(x) for x in tdense])
tq = np.interp(th_a + q*Omega, thdense, tdense)
w = np.array([zeta_line(x) for x in tq])
thq = np.array([theta_exact(x) for x in tq])
Zq = np.real(w*np.exp(1j*thq))
eps = np.sign(Zq[len(Zq)//2]) or 1.0
what = eps*np.exp(1j*th_a)*w
A = np.max(np.abs(what))
model = A*np.sin(np.pi*q)*np.exp(-1j*Omega*q)
C = np.trapezoid(what, q)

fig, ax = plt.subplots(figsize=(8,8))
ax.plot(what.real/A, what.imag/A, lw=1.4, label="actual rotated lobe")
ax.plot(model.real/A, model.imag/A, lw=1.2, ls="--", label="one-arch phase model")
ax.scatter([0],[0],s=34,label="zero-axis contact")
ax.scatter([C.real/A],[C.imag/A],s=34,label="phase centroid")
ax.set_aspect("equal", adjustable="datalim")
ax.set_xlabel("normalized rotated real part")
ax.set_ylabel("normalized rotated imaginary part")
ax.set_title(f"Lobe {n}: eccentric geometry in uniform phase coordinate")
ax.grid(True, alpha=0.2)
ax.legend(fontsize=8)
fig.tight_layout()
fig.savefig(FIG/"fig17_single_lobe_phase_geometry.png", dpi=220, bbox_inches="tight")
plt.close(fig)

# Quarter-turn vectors
dw = np.gradient(what, tq)
sel = np.linspace(25, len(q)-26, 11, dtype=int)
scale = 0.16*A/np.max(np.abs(dw[sel]))
fig, ax = plt.subplots(figsize=(8,8))
ax.plot(what.real/A, what.imag/A, lw=1.2)
for k in sel:
    p = what[k]/A
    tang = dw[k]*scale/A
    norm = -1j*dw[k]*scale/A
    ax.arrow(p.real,p.imag,tang.real,tang.imag,width=0.002,head_width=0.025,length_includes_head=True)
    ax.arrow(p.real,p.imag,norm.real,norm.imag,width=0.002,head_width=0.025,length_includes_head=True)
ax.scatter([0],[0],s=30)
ax.set_aspect("equal", adjustable="datalim")
ax.set_xlabel("normalized rotated real part")
ax.set_ylabel("normalized rotated imaginary part")
ax.set_title("Longitudinal tangent and exact 90-degree transverse direction")
ax.grid(True, alpha=0.2)
fig.tight_layout()
fig.savefig(FIG/"fig18_quarter_turn_vector_field.png", dpi=220, bbox_inches="tight")
plt.close(fig)

# Eccentricity law
s = lobes["s_n"].to_numpy()
Ea = lobes["E_n_2absC_over_A"].to_numpy()
Ep = lobes["E_n_arch_prediction"].to_numpy()
order = np.argsort(s)
fig, ax = plt.subplots(figsize=(8.5,6))
ax.scatter(s,Ea,s=28,label="actual zeta lobes")
ax.plot(s[order],Ep[order],lw=1.25,label="one-arch phase prediction")
ax.set_xlabel(r"$s_n=\Omega_n/\pi$")
ax.set_ylabel(r"$E_n$")
ax.set_title("Lobe eccentricity is controlled by phase sweep")
ax.grid(True, alpha=0.2)
ax.legend()
fig.tight_layout()
fig.savefig(FIG/"fig19_eccentricity_phase_law.png", dpi=220, bbox_inches="tight")
plt.close(fig)

# Exact tangent-circle identity
phi = np.linspace(0,np.pi,600)
fig, ax = plt.subplots(figsize=(8,8))
for shift in [0.0,0.65,1.30]:
    z = np.sin(phi)*np.exp(-1j*(phi+shift))
    ax.plot(z.real,z.imag,lw=1.2)
ax.scatter([0],[0],s=32)
ax.set_aspect("equal", adjustable="box")
ax.set_xlabel("real part")
ax.set_ylabel("imaginary part")
ax.set_title("The unit-sweep arch is an eccentric circle tangent to the origin")
ax.grid(True, alpha=0.2)
fig.tight_layout()
fig.savefig(FIG/"fig20_tangent_circle_identity.png", dpi=220, bbox_inches="tight")
plt.close(fig)

# -----------------------------------------------------------------------------
# V4 analytic obstruction figures (no corpus-dependent inputs)
# -----------------------------------------------------------------------------

m = np.arange(1, 151)
d = 4 * (1 - (-1.0)**m) / (np.pi**3 * m**3)
fig, ax = plt.subplots(figsize=(8.4, 5.6))
odd = (m % 2 == 1)
ax.loglog(m[odd], np.abs(d[odd]), marker="o", markersize=3, linewidth=1,
          label=r"$|d_m|$ for $f(x)=x(1-x)$")
ax.loglog(m[odd], 8/(np.pi**3*m[odd]**3), linestyle="--", linewidth=1,
          label=r"$8/(\pi^3m^3)$")
ax.set_xlabel(r"$m$")
ax.set_ylabel(r"$|d_m|$")
ax.set_title("Analyticity does not imply exponential sine-series decay")
ax.grid(True, which="both", alpha=0.22)
ax.legend()
fig.tight_layout()
fig.savefig(FIG/"fig21_sine_series_endpoint_obstruction.png", dpi=220, bbox_inches="tight")
plt.close(fig)

M = np.arange(5, 501)
fig, ax = plt.subplots(figsize=(8.4, 5.6))
for c in [0.1, 1.0, 10.0]:
    eps = c / M**2
    y = np.arcsinh(1/np.sqrt(eps)) / (np.pi*M)
    ax.loglog(M, y, linewidth=1.2, label=rf"$c={c}$")
ax.set_xlabel(r"$M$")
ax.set_ylabel(r"nearest zero distance $|\Im x|$")
ax.set_title("Real-axis closeness does not prevent nearby complex zeros")
ax.grid(True, which="both", alpha=0.22)
ax.legend()
fig.tight_layout()
fig.savefig(FIG/"fig22_hidden_complex_zeros_counterexample.png", dpi=220, bbox_inches="tight")
plt.close(fig)
