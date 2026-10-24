#!/usr/bin/env python3
"""Generate the numerical figures used in the centroid manuscript.

The finite zeta tables below are transcribed from the full-data
MATLAB output for N=2,001,052 zeros. The Lambert-RVM Abel approximants are
transcribed from rvm_centroid_output.txt. The RH defect sensitivity curve is
an analytic illustration of the positive imaginary-frequency criterion.
"""
from __future__ import annotations

from pathlib import Path
import csv
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "figures"
DATA = ROOT / "data"
FIG.mkdir(parents=True, exist_ok=True)
DATA.mkdir(parents=True, exist_ok=True)

# Tail-centroid table.
removed = np.array([0, 10, 100, 1000, 10000, 100000, 200100, 500260,
          1000500, 1500800, 1800900], dtype=float)
abs_zeta = np.array([1.0923, 1.5972, 0.60399, 1.3495, 2.0882, 2.4476,
           0.60171, 0.92554, 1.3558, 2.4596, 1.3232])
abs_rvm = np.array([1.7580, 0.50157, 0.65664, 0.91298, 1.2078, 1.5221,
          1.6194, 1.7491, 1.8482, 1.9064, 1.9327])
abs_diff = np.array([1.2330, 1.1960, 1.2492, 1.1667, 1.4259, 1.0192,
           1.4994, 1.0034, 0.58972, 1.4196, 0.65554])

with (DATA / "tail_centroid_table.csv").open("w", newline="") as f:
  w = csv.writer(f)
  w.writerow(["removed_prefix", "abs_C_zeta", "abs_C_RVM", "abs_difference"])
  w.writerows(zip(removed.astype(int), abs_zeta, abs_rvm, abs_diff))

fig, ax = plt.subplots(figsize=(7.0, 4.4))
ax.plot(removed, abs_zeta, marker="o", label=r"$|C_\zeta|$")
ax.plot(removed, abs_rvm, marker="s", label=r"$|C_{\rm RVM}|$")
ax.plot(removed, abs_diff, marker="^", label=r"$|C_\zeta-C_{\rm RVM}|$")
ax.set_xscale("symlog", linthresh=10)
ax.set_xlabel("Removed prefix length")
ax.set_ylabel("Centroid modulus")
ax.set_title("Tail-centroid stability test")
ax.grid(True, alpha=0.25)
ax.legend()
fig.tight_layout()
fig.savefig(FIG / "tail_centroid_stability.pdf")
fig.savefig(FIG / "tail_centroid_stability.png", dpi=220)
plt.close(fig)

# Empirical standard-deviation profile against Selberg scale.
gamma = np.array([1421.8, 5449.7, 9879.3, 12399.9, 18048.1, 40435.1,
         74922.2, 201091.6, 600270.7, 1132490.7])
sigma_emp = np.array([0.28310, 0.28880, 0.29921, 0.30184, 0.30601,
           0.31372, 0.31907, 0.32669, 0.33476, 0.33850])
sigma_selberg = np.array([0.31690, 0.33020, 0.33529, 0.33712, 0.34005,
             0.34589, 0.35000, 0.35605, 0.36210, 0.36535])
with (DATA / "S_argument_variance_profile.csv").open("w", newline="") as f:
  w = csv.writer(f)
  w.writerow(["gamma", "sigma_empirical", "sigma_Selberg"])
  w.writerows(zip(gamma, sigma_emp, sigma_selberg))

fig, ax = plt.subplots(figsize=(7.0, 4.4))
ax.plot(gamma, sigma_emp, marker="o", label="Empirical local standard deviation")
ax.plot(gamma, sigma_selberg, marker="s", label="Selberg scale")
ax.set_xscale("log")
ax.set_xlabel(r"Zero ordinate $\gamma$")
ax.set_ylabel("Standard deviation")
ax.set_title(r"Argument fluctuation scale along the zero sequence")
ax.grid(True, alpha=0.25)
ax.legend()
fig.tight_layout()
fig.savefig(FIG / "argument_variance_profile.pdf")
fig.savefig(FIG / "argument_variance_profile.png", dpi=220)
plt.close(fig)

# Lambert-RVM Abel-series approximants.
J = np.array([10000, 100000, 500000, 1000000, 2001052], dtype=float)
re = np.array([0.041580072865611, 0.041570891195329, 0.041569346208409,
        0.041569178431353, 0.041568808323635])
im = np.array([1.757554793733856, 1.757542207523970, 1.757541422824472,
        1.757540990615438, 1.757541025528465])
ref = re[-1] + 1j * im[-1]
err = np.abs(re + 1j * im - ref)
with (DATA / "rvm_abel_approximants.csv").open("w", newline="") as f:
  w = csv.writer(f)
  w.writerow(["J", "real", "imag", "distance_to_last_approximant"])
  w.writerows(zip(J.astype(int), re, im, err))

fig, ax = plt.subplots(figsize=(7.0, 4.4))
ax.plot(J[:-1], err[:-1], marker="o")
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel("Abel-series cutoff J")
ax.set_ylabel("Distance to the J=2,001,052 approximant")
ax.set_title("Lambert-RVM Abel-series convergence")
ax.grid(True, alpha=0.25)
fig.tight_layout()
fig.savefig(FIG / "rvm_abel_convergence.pdf")
fig.savefig(FIG / "rvm_abel_convergence.png", dpi=220)
plt.close(fig)

# Positive defect sensitivity on the imaginary frequency axis.
gamma1 = 14.134725142
horizontal_delta = 0.05
y = np.logspace(-2.3, 0.15, 600)
defect = 2.0 * (1.0 - np.cos(y * horizontal_delta)) * np.exp(-y * gamma1)
y_opt = 2.0 / gamma1
with (DATA / "rh_positive_defect_curve.csv").open("w", newline="") as f:
  w = csv.writer(f)
  w.writerow(["y", "pair_defect_delta_0.05_gamma1"])
  w.writerows(zip(y, defect))

fig, ax = plt.subplots(figsize=(7.0, 4.4))
ax.plot(y, defect)
ax.axvline(y_opt, linestyle="--", label=r"$2/\gamma_1$")
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel(r"Imaginary frequency parameter $y$")
ax.set_ylabel("Positive paired defect")
ax.set_title(r"Sensitivity of $2(1-\cos(y\delta))e^{-y\gamma}$ for $\delta=0.05$")
ax.grid(True, alpha=0.25)
ax.legend()
fig.tight_layout()
fig.savefig(FIG / "rh_positive_defect_sensitivity.pdf")
fig.savefig(FIG / "rh_positive_defect_sensitivity.png", dpi=220)
plt.close(fig)

# Complex-plane numerical landmarks.
points = {
  "Zeta centroid": 0.776907119554635 + 0.767844590760710j,
  "Conditional analytic limit": 0.776894260793165 + 0.767855668864548j,
  "Smooth term B": 0.381782018323631 + 0.146163101528591j,
  "Arithmetic term P": 0.395112242469534 + 0.621692567335957j,
  "Lambert centroid": 0.041570219277352 + 1.757541749592316j,
}
with (DATA / "complex_landmarks.csv").open("w", newline="") as f:
  w = csv.writer(f)
  w.writerow(["label", "real", "imag"])
  for label, z in points.items():
    w.writerow([label, z.real, z.imag])

fig, ax = plt.subplots(figsize=(6.5, 5.4))
offsets = {
  "Zeta centroid": (8, 8),
  "Conditional analytic limit": (8, -10),
  "Smooth term B": (8, 8),
  "Arithmetic term P": (8, 8),
  "Lambert centroid": (8, 8),
}
for label, z in points.items():
  ax.scatter([z.real], [z.imag], s=40)
  dx, dy = offsets.get(label, (6, 6))
  ax.annotate(label, (z.real, z.imag), xytext=(dx, dy), textcoords="offset points", fontsize=8)
ax.axhline(0, linewidth=0.8)
ax.axvline(0, linewidth=0.8)
ax.set_xlabel("Real part")
ax.set_ylabel("Imaginary part")
ax.set_title("Numerical centroid landmarks")
ax.grid(True, alpha=0.25)
fig.tight_layout()
fig.savefig(FIG / "centroid_complex_landmarks.pdf")
fig.savefig(FIG / "centroid_complex_landmarks.png", dpi=220)
plt.close(fig)

print("ARTICLE FIGURE GENERATION")
print(f"output directory: {FIG}")
for p in sorted(FIG.glob("*.*")):
  if p.suffix.lower() in {".png", ".pdf"}:
    print(f"figure: {p.name}")
for p in sorted(DATA.glob("*.csv")):
  print(f"data:  {p.name}")
print(f"y_opt = 2/gamma_1 = {y_opt:.12f}")
