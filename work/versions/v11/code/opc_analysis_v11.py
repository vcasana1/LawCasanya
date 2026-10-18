"""Ordinal-dependent prime cutoffs for Riemann zeta zero ordinates.

Numerical companion of the manuscript on ordinal prime cutoffs.

Data (not included in the repository, see README):
  data/zeross.bin : ordinates gamma_k of the zeros of zeta, k = 1..2,001,052 (little-endian float64)
  data/zLamb.bin  : Lambert clock tau_k = 2*pi*(k-11/8)/W((k-11/8)/e), same length (little-endian float64)

Notation (as in the manuscript):
  delta_k   = tau_k - gamma_k                     (displacement of the clock)
  T'(k)     = 2*pi / log(tau_k/(2*pi))            (derivative of the clock in the ordinal)
  S_P(t)    = -(1/pi) sum_{p in P} arg(1 - p^{-1/2-it})     (Euler phase, full local factors)
  tau_k^P   = tau_k - T'(k) S_P(tau_k)            (one-step prime-corrected clock)
  delta_k^P = tau_k^P - gamma_k = delta_k - T'(k) S_P(tau_k)
  saturation with level B: the correction T'(k) S_P(tau_k) is replaced by sgn(.) min(|.|, B).

Outputs: ../outputs/*.csv, *.txt, *.tex and ../figures/*.png
Usage:   python3 opc_analysis_v11.py [path_to_data_dir]
"""
import os
import sys
import time
import hashlib
import json
import csv
import platform
import scipy

import numpy as np
import matplotlib
import matplotlib.ticker
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mpmath as mp
from scipy.special import lambertw

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "data")
OUT = os.path.join(HERE, "..", "outputs")
FIG = os.path.join(HERE, "..", "figures")
os.makedirs(OUT, exist_ok=True)
os.makedirs(FIG, exist_ok=True)
LOG = open(os.path.join(OUT, "opc_analysis_log.txt"), "w")


def log(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.write(s + "\n")
    LOG.flush()


# ----------------------------------------------------------------------------- data
tau = np.fromfile(os.path.join(DATA, "zLamb.bin"), dtype="<f8")
gam = np.fromfile(os.path.join(DATA, "zeross.bin"), dtype="<f8")
K = 2001052
if len(tau) != K or len(gam) != K:
    raise ValueError("Expected exactly 2,001,052 values in each input; no truncation is allowed")
if not np.isfinite(tau).all() or not np.isfinite(gam).all():
    raise ValueError("Input contains a non-finite ordinate")
if np.any(np.diff(tau) <= 0) or np.any(np.diff(gam) < 0):
    raise ValueError("Clock must be increasing and ordinates nondecreasing")
metadata = {"python": platform.python_version(), "numpy": np.__version__,
            "scipy": scipy.__version__, "matplotlib": matplotlib.__version__,
            "mpmath": mp.__version__, "files": {}}
for filename in ("zeross.bin", "zLamb.bin"):
    path = os.path.join(DATA, filename)
    h = hashlib.sha256()
    with open(path, "rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    metadata["files"][filename] = {"size_bytes": os.path.getsize(path), "sha256": h.hexdigest()}
with open(os.path.join(OUT, "analysis_metadata.json"), "w") as stream:
    json.dump(metadata, stream, indent=2)

k = np.arange(1, K + 1, dtype=float)
Lk = np.log(tau / (2 * np.pi))          # log(tau_k / 2pi) = 1 + W_k
Tp = 2 * np.pi / Lk                     # T'(k)
delta = tau - gam                       # delta_k = tau_k - gamma_k
s_ord = delta / Tp                      # ordinal-normalized displacement
log("K =", K, " tau_K =", tau[-1], " gamma_K =", gam[-1])

# check of the clock formula on a sample of indices
idx = np.array([0, 1, 9, 99, 999, 99999, K - 1])
a = idx + 1 - 11.0 / 8.0
Wv = np.real(lambertw(a / np.e))
tau_chk = 2 * np.pi * a / Wv
log("clock formula check, max |tau_file - 2pi(k-11/8)/W((k-11/8)/e)| on sample:",
    float(np.max(np.abs(tau_chk - tau[idx]))))

EDGES = [0, 1000, 10**4, 10**5, 5 * 10**5, 10**6, K]
WIN = list(zip(EDGES[:-1], EDGES[1:]))
WLAB = ["(0,1e3]", "(1e3,1e4]", "(1e4,1e5]", "(1e5,5e5]", "(5e5,1e6]", "(1e6,%d]" % K]
WTEX = [r"$(0,10^3]$", r"$(10^3,10^4]$", r"$(10^4,10^5]$", r"$(10^5,5\cdot10^5]$", r"$(5\cdot10^5,10^6]$",
        r"$(10^6,K]$"]   # display labels used in the figures


def rms(x):
    return float(np.sqrt(np.mean(x * x)))


def primes_upto(n):
    sv = np.ones(n + 1, bool)
    sv[:2] = False
    for q in range(2, int(n ** 0.5) + 1):
        if sv[q]:
            sv[q * q::q] = False
    return np.nonzero(sv)[0]


def euler_term(p, t):
    """-(1/pi) arg(1 - p^{-1/2-it}): contribution of the prime p to S_P(t), all powers p^m"""
    return -np.angle(1.0 - p ** -0.5 * np.exp(-1j * t * np.log(p))) / np.pi


def saturate(c, B):
    return np.sign(c) * np.minimum(np.abs(c), B) if B is not None else c


def li2(x, terms=200):
    m = np.arange(1, terms + 1)
    return float(np.sum(x ** m / m ** 2))


def cP(plist):
    """(1/2pi^2) sum_{p in P} Li_2(1/p): asymptotic mean-square gain of the full Euler phase over P"""
    return sum(li2(1.0 / p) for p in plist) / (2 * np.pi ** 2)


PR = primes_upto(2000)
LADDER = [p for p in PR if p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 43, 53, 61, 71, 83, 97, 113, 131,
                                 151, 173, 199, 229, 263, 307, 353, 401, 461, 523, 601, 701, 809, 907, 1009, 1201,
                                 1409, 1601, 1801, 1999)]
SCAN = [p for p in PR if 11 <= p <= 71]
THETA = 0.57                                       # variable rule X_k = max(7, (tau_k/2pi)^THETA)
Xvar = np.maximum(7.0, (tau / (2 * np.pi)) ** THETA)
B0 = 0.6
parameters = {"ordinal_windows": WIN, "window_labels": WLAB,
              "prime_max": 2000, "cutoff_ladder": [int(p) for p in LADDER],
              "saturation_scan": [int(p) for p in SCAN],
              "variable_exponent": THETA, "variable_minimum_cutoff": 7,
              "method_saturation": B0, "saturation_levels": [0.5, 0.6, 0.7]}
with open(os.path.join(OUT, "analysis_parameters.json"), "w") as stream:
    json.dump(parameters, stream, indent=2)

# ----------------------------------------------------------------------------- one pass over the primes
S = np.zeros(K)          # S_P(tau_k) with P = primes <= current p
Svar = np.zeros(K)       # variable cutoff: prime p used for k with X_k >= p
snap = {}
rms_ladder = {}          # p -> list of RMS per window (no saturation)
max_ladder = {}
scan_rows = []
for p in PR:
    tp = euler_term(p, tau)
    S += tp
    a0 = int(np.searchsorted(Xvar >= p, True)) if Xvar[-1] >= p else K
    if a0 < K:
        Svar[a0:] += tp[a0:]
    if p in LADDER:
        r = delta - Tp * S
        rms_ladder[p] = [rms(r[a:b]) for a, b in WIN]
        max_ladder[p] = [float(np.max(np.abs(r[a:b]))) for a, b in WIN]
    if p in SCAN:
        for B in (0.5, 0.6, 0.7):
            r = delta - saturate(Tp * S, B)
            ar = np.abs(r)
            j = int(np.argmax(ar))
            scan_rows.append((p, B, float(ar[j]), j + 1, int(np.sum(ar >= 0.5)), rms(r), float(r[258317])))
    if p in (7, 61, 1999):
        snap[p] = S.copy()
log("prime loop done, %.0f s" % (time.time() - T0))

# ----------------------------------------------------------------------------- Table A: methods by window
methods = [("bare clock", np.zeros(K), None),
           ("P={2,3,5,7}, B=0.6", Tp * snap[7], B0),
           ("P={p<=61}, B=0.6", Tp * snap[61], B0),
           ("P={p<=1999} (fixed)", Tp * snap[1999], None),
           ("X_k=max(7,(tau_k/2pi)^0.57), B=0.6", Tp * Svar, B0)]
resid = {}
with open(os.path.join(OUT, "table_A_methods_by_window.csv"), "w") as f:
    f.write("method,window,RMS,max_abs,count_ge_half\n")
    for name, c, B in methods:
        r = delta - saturate(c, B)
        resid[name] = r
        for (a, b), wl in zip(WIN, WLAB):
            f.write('"%s","%s",%.6f,%.6f,%d\n' % (name, wl, rms(r[a:b]), np.max(np.abs(r[a:b])),
                                                 np.sum(np.abs(r[a:b]) >= 0.5)))
        j = int(np.argmax(np.abs(r)))
        log("A| %-38s global RMS %.6f  max %.6f at k=%d  #>=1/2: %d" %
            (name, rms(r), abs(r[j]), j + 1, int(np.sum(np.abs(r) >= 0.5))))
        log("   per-window RMS:", " ".join("%.4f" % rms(r[a:b]) for a, b in WIN))
        log("   per-window max:", " ".join("%.4f" % np.max(np.abs(r[a:b])) for a, b in WIN))

# ----------------------------------------------------------------------------- Table B: RMS against the cutoff
with open(os.path.join(OUT, "table_B_rms_vs_cutoff.csv"), "w") as f:
    csv.writer(f).writerow(["X"] + ["RMS_"+w for w in WLAB] + ["max_"+w for w in WLAB])
    for p in LADDER:
        f.write("%d," % p + ",".join("%.6f" % v for v in rms_ladder[p]) + "," +
                ",".join("%.6f" % v for v in max_ladder[p]) + "\n")
opt = []
for j, ((a, b), wl) in enumerate(zip(WIN, WLAB)):
    pbest = min(LADDER, key=lambda p: rms_ladder[p][j])
    Lmed = float(np.median(Lk[a:b]))
    opt.append((wl, pbest, rms_ladder[pbest][j], Lmed, rms(delta[a:b])))
    log("B| window %-16s optimal X = %5d  RMS = %.4f   median log(tau/2pi) = %.3f  bare RMS = %.4f" %
        (wl, pbest, rms_ladder[pbest][j], Lmed, rms(delta[a:b])))
xs = np.array([o[3] for o in opt[1:]])
ys = np.log(np.array([o[1] for o in opt[1:]], float))
theta_fit = float(np.sum(xs * ys) / np.sum(xs * xs))
log("B| least-squares fit log X_opt = theta * log(tau/2pi) on windows 2-6: theta = %.4f" % theta_fit)
with open(os.path.join(OUT, "table_B_optimal_cutoff.csv"), "w") as f:
    f.write("window,X_opt,RMS_at_opt,median_log_tau_over_2pi,bare_RMS\n")
    for o in opt:
        f.write('"%s",%d,%.6f,%.4f,%.6f\n' % o)
    f.write("theta_fit,%.6f\n" % theta_fit)

# ----------------------------------------------------------------------------- Table C: fixed cutoff and saturation, global
with open(os.path.join(OUT, "table_C_fixed_cutoff_saturation.csv"), "w") as f:
    f.write("X,B,global_max,k_at_max,count_ge_half,RMS,residual_at_k258318\n")
    for row in scan_rows:
        f.write("%d,%.1f,%.6f,%d,%d,%.6f,%.6f\n" % row)
for row in scan_rows:
    if row[0] in (11, 13, 31, 61, 71):
        log("C| X=%3d B=%.1f  max %.4f at k=%8d  #>=1/2 %d  RMS %.4f  r(258318) %+.4f" % row)

# ----------------------------------------------------------------------------- Table D: measured mean-square gain against theory
PP = {7: [2, 3, 5, 7], 61: [int(p) for p in PR if p <= 61], 1999: [int(p) for p in PR if p <= 1999]}
with open(os.path.join(OUT, "table_D_gain_vs_theory.csv"), "w") as f:
    f.write("window,mean_s2,gain_P7,c_P7,gain_P61,c_P61\n")
    for (a, b), wl in zip(WIN, WLAB):
        s2 = float(np.mean(s_ord[a:b] ** 2))
        g7 = s2 - float(np.mean((s_ord[a:b] - snap[7][a:b]) ** 2))
        g61 = s2 - float(np.mean((s_ord[a:b] - snap[61][a:b]) ** 2))
        f.write('"%s",%.6f,%.6f,%.6f,%.6f,%.6f\n' % (wl, s2, g7, cP(PP[7]), g61, cP(PP[61])))
        log("D| %-16s <s^2> %.4f  gain P7 %.4f (c=%.4f)  gain P61 %.4f (c=%.4f)" %
            (wl, s2, g7, cP(PP[7]), g61, cP(PP[61])))

# ----------------------------------------------------------------------------- Table E: projection coefficients
a, b = 10**6, K
def Lambda(n):
    for p in PR:
        if p > n:
            break
        if n % p == 0:
            m = n
            while m % p == 0:
                m //= p
            return float(np.log(p)) if m == 1 else 0.0
    return 0.0

Lmed_top = float(np.median(Lk[a:b]))


def factor(n):
    out = {}
    for p in PR:
        if p > n:
            break
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
    return out


def second_order(n):
    """second-order prediction log(n)/(a*b*log(tau/2pi)) for n = p^a q^b with two distinct primes, else nan"""
    fz = factor(n)
    if len(fz) != 2:
        return float("nan")
    e = list(fz.values())
    return float(np.log(n)) / (e[0] * e[1] * Lmed_top)


rows_E = []
for n in range(2, 65):
    proj = float(np.mean(s_ord[a:b] * np.sin(tau[a:b] * np.log(n))))
    rho = -2 * np.pi * np.sqrt(n) * proj
    theo = Lambda(n) / np.log(n)
    rows_E.append((n, proj, rho, theo, second_order(n)))
with open(os.path.join(OUT, "table_E_projection_coefficients.csv"), "w") as f:
    f.write("n,projection,rho_n=-2pi*sqrt(n)*projection,Lambda(n)/log(n),second_order_log(n)/(ab*L)\n")
    for r_ in rows_E:
        f.write("%d,%.6e,%.6f,%.6f,%.6f\n" % r_)
so_err = [abs(r_[2] - r_[4]) for r_ in rows_E if r_[4] == r_[4]]
log("E| median log(tau/2pi) in the window: %.4f ; max |rho_n - log n/(ab L)| over n = p^a q^b <= 64: %.4f" %
    (Lmed_top, max(so_err)))
log("E| n, rho_n, first-order, second-order:", " ".join("%d:%.3f/%.3f/%.3f" % (r_[0], r_[2], r_[3], r_[4])
                                                         for r_ in rows_E))
pp_err = [abs(r_[2] - r_[3]) for r_ in rows_E if r_[3] > 0]
np_err = [abs(r_[2]) for r_ in rows_E if r_[3] == 0]
log("E| window k in (1e6, K]: max |rho_n - Lambda(n)/log n| over prime powers n<=64: %.4f ; max |rho_n| over"
    " non-prime-powers: %.4f" % (max(pp_err), max(np_err)))
log("E| rho_2..rho_12:", " ".join("%d:%.3f" % (r_[0], r_[2]) for r_ in rows_E[:11]))

# ----------------------------------------------------------------------------- the extreme residual: a close pair
kk = 258318
i0 = kk - 1
ng = (gam[1:] - gam[:-1]) * np.log(gam[:-1] / (2 * np.pi)) / (2 * np.pi)
rank = int(np.sum(ng < ng[i0 - 1])) + 1
mp.mp.dps = 25
with open(os.path.join(OUT, "close_pair_k258318.txt"), "w") as f:
    f.write("k, gamma_k (zeross.bin), tau_k, delta_k=tau-gamma, gap to next, normalized gap to next\n")
    for j in range(i0 - 3, i0 + 4):
        f.write("%d %.9f %.9f %+.4f %.4f %.4f\n" % (j + 1, gam[j], tau[j], delta[j], gam[j + 1] - gam[j], ng[j]))
    for n in (kk - 1, kk, kk + 1):
        z = mp.zetazero(n)
        f.write("mpmath zetazero(%d) = %s ; difference with zeross.bin = %.3e\n" %
                (n, mp.nstr(z.imag, 18), float(z.imag) - gam[n - 1]))
    f.write("normalized gap (k-1,k) = %.4f, rank %d among %d gaps\n" % (ng[i0 - 1], rank, len(ng)))
    for n in (1, 1000, 100000, 1000000, K):
        z = mp.zetazero(n)
        f.write("data check: mpmath zetazero(%d) - zeross.bin = %.3e\n" % (n, float(z.imag) - gam[n - 1]))
    f.write("S(gamma_k) (midpoint) = %s\n" % mp.nstr(kk - mp.mpf(1) / 2 - mp.siegeltheta(mp.mpf(gam[i0])) / mp.pi - 1, 10))
    for name in resid:
        f.write("residual %-38s %+.4f\n" % (name, resid[name][i0]))
log(open(os.path.join(OUT, "close_pair_k258318.txt")).read())

# ----------------------------------------------------------------------------- figures
plt.rcParams.update({"font.size": 10, "figure.dpi": 200, "savefig.dpi": 200})
C0, C1, C2, C3, C4 = "#1f4e79", "#c0504d", "#4f9a3a", "#8064a2", "#e08a1e"
# display labels in the notation of the paper (calligraphic P = finite set of primes)
DISP = {"bare clock": r"bare clock $\tau_k$",
        "P={2,3,5,7}, B=0.6": r"$\mathcal{P}=\{2,3,5,7\}$, $B=0.6$",
        "P={p<=61}, B=0.6": r"$\mathcal{P}=\{p\leq 61\}$, $B=0.6$",
        "P={p<=1999} (fixed)": r"$\mathcal{P}=\{p\leq 1999\}$, no saturation",
        "X_k=max(7,(tau_k/2pi)^0.57), B=0.6": r"$X_k=\max(7,(\tau_k/2\pi)^{0.57})$, $B=0.6$"}

# figure: displacement for k <= 2000
fig, ax = plt.subplots(figsize=(7.2, 3.6))
n0 = 2000
ax.plot(k[:n0], delta[:n0], ".", ms=2.2, color=C0, label=r"$\delta_k=\tau_k-\gamma_k$")
ax.plot(k[:n0], resid["P={2,3,5,7}, B=0.6"][:n0], ".", ms=2.2, color=C1,
        label=r"one-step residual, $\mathcal{P}=\{2,3,5,7\}$, $B=0.6$")
ax.axhline(0, color="k", lw=0.5)
ax.set_xlabel("ordinal $k$")
ax.set_ylabel("displacement")
ax.legend(loc="upper right", fontsize=8)
ax.set_title("Clock displacement and one-step Euler correction, $k\\leq 2000$")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig01_displacement_first2000.png"))

# figure: binned RMS against log10 k
bins = np.unique(np.round(np.logspace(1, np.log10(K), 36)).astype(int))
mid, curves = [], {nm: [] for nm in resid}
for a_, b_ in zip(bins[:-1], bins[1:]):
    mid.append(np.sqrt(a_ * b_))
    for nm in resid:
        curves[nm].append(rms(resid[nm][a_:b_]))
fig, ax = plt.subplots(figsize=(7.2, 4.0))
for (nm, col) in zip(resid, (C0, C1, C2, C3, C4)):
    ax.plot(mid, curves[nm], "-o", ms=2.5, lw=1.2, color=col, label=DISP[nm])
ax.set_xscale("log")
ax.set_xlabel("ordinal $k$ (log scale)")
ax.set_ylabel("RMS of the residual in the bin")
ax.legend(fontsize=7.5)
ax.set_title("Root mean square of the residual, logarithmic bins of $k$")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "figS1_rms_by_height.png"))

# figure: RMS against the cutoff, per window
fig, ax = plt.subplots(figsize=(7.2, 4.0))
cols = (C0, C1, C2, C3, C4, "#555555")
for j, wl in enumerate(WTEX):
    yv = [rms_ladder[p][j] for p in LADDER]
    ax.plot(LADDER, yv, "-", lw=1.2, color=cols[j], label="$k\\in$" + wl)
    pb = opt[j][1]
    ax.plot([pb], [opt[j][2]], "o", color=cols[j], ms=5)
ax.set_xscale("log")
ax.set_xlabel("prime cutoff $X$ (primes $p\\leq X$, full local factors)")
ax.set_ylabel("RMS of $\\tau_k^X-\\gamma_k$")
ax.legend(fontsize=7.5)
ax.set_title("RMS against the cutoff; dots mark the optimum of each window")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig04_rms_vs_cutoff.png"))

# figure: optimal cutoff against log(tau/2pi)
fig, ax = plt.subplots(figsize=(6.0, 4.0))
xo = np.array([o[3] for o in opt])
yo = np.log(np.array([o[1] for o in opt], float))
ax.plot(xo, yo, "o", color=C0, label="RMS-optimal $\\log X$ per window")
xx = np.linspace(4, 12.5, 50)
ax.plot(xx, theta_fit * xx, "-", color=C1, label="$\\log X=%.3f\\,\\log(\\tau/2\\pi)$" % theta_fit)
ax.set_xlabel("median of $\\log(\\tau_k/2\\pi)$ in the window")
ax.set_ylabel("$\\log X_{\\rm opt}$")
ax.legend(fontsize=8)
ax.set_title("The optimal prime cutoff grows with the height")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "figS2_optimal_cutoff.png"))

# figure: close pair
fig, ax = plt.subplots(figsize=(7.2, 2.8))
js = np.arange(i0 - 4, i0 + 5)
ax.plot(gam[js], np.zeros_like(js), "o", color="k", ms=6, label="$\\gamma_k$ (zeros)")
ax.plot(tau[js], 0.6 * np.ones_like(js), "s", color=C0, ms=5, label="$\\tau_k$ (clock)")
ax.plot(tau[js] - (Tp * snap[7])[js], 1.2 * np.ones_like(js), "^", color=C1, ms=5, label="$\\tau_k^{\\mathcal{P}}$, $\\mathcal{P}=\\{2,3,5,7\\}$")
ax.plot(tau[js] - (Tp * snap[61])[js], 1.8 * np.ones_like(js), "v", color=C2, ms=5, label="$\\tau_k^{\\mathcal{P}}$, $\\mathcal{P}=\\{p\\leq61\\}$")
for j in js:
    ax.plot([gam[j], tau[j]], [0, 0.6], "-", color="#999999", lw=0.6)
ax.annotate("$k=258317,258318$", xy=(gam[i0 - 1], 0), xytext=(gam[i0 - 1] - 1.2, -0.5), fontsize=8,
            arrowprops=dict(arrowstyle="->", lw=0.6))
ax.set_yticks([])
ax.set_ylim(-0.8, 2.3)
ax.set_xlabel("$t$")
ax.legend(fontsize=7, ncol=4, loc="upper center")
ax.set_title("The extreme residual: a close pair of zeros followed by a large gap")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "figS3_close_pair.png"))

# figure: measured gain against theory
g7s, g61s, s2s = [], [], []
for a_, b_ in WIN:
    s2 = float(np.mean(s_ord[a_:b_] ** 2))
    s2s.append(s2)
    g7s.append(s2 - float(np.mean((s_ord[a_:b_] - snap[7][a_:b_]) ** 2)))
    g61s.append(s2 - float(np.mean((s_ord[a_:b_] - snap[61][a_:b_]) ** 2)))
fig, ax = plt.subplots(figsize=(7.2, 3.8))
xw = np.arange(len(WLAB))
ax.plot(xw, g7s, "o-", color=C1, label="measured gain, $\\mathcal{P}=\\{2,3,5,7\\}$")
ax.axhline(cP(PP[7]), color=C1, ls="--", lw=1, label="$v_{\\mathcal{P}}=%.5f$" % cP(PP[7]))
ax.plot(xw, g61s, "s-", color=C2, label="measured gain, $\\mathcal{P}=\\{p\\leq 61\\}$")
ax.axhline(cP(PP[61]), color=C2, ls="--", lw=1, label="$v_{\\mathcal{P}}=%.5f$" % cP(PP[61]))
ax.set_xticks(xw)
ax.set_xticklabels(WTEX, fontsize=8)
ax.set_xlabel("window of ordinals")
ax.set_ylabel("$\\langle s_k^2\\rangle-\\langle (s_k-S_{\\mathcal{P}}(\\tau_k))^2\\rangle$")
ax.legend(fontsize=7.5)
ax.set_title("Mean-square gain of a fixed prime set against $v_{\\mathcal{P}}$")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig06_gain_fixed_sets.png"))

# figure: maximum per window
fig, ax = plt.subplots(figsize=(7.2, 3.8))
for (nm, col, mk) in zip(resid, (C0, C1, C2, C3, C4), "osd^v"):
    ax.plot(xw, [np.max(np.abs(resid[nm][a_:b_])) for a_, b_ in WIN], "-" + mk, color=col, ms=4, label=DISP[nm])
ax.axhline(0.5, color="k", lw=0.6, ls=":")
ax.set_xticks(xw)
ax.set_xticklabels(WTEX, fontsize=8)
ax.set_ylabel("max $|$residual$|$ in the window")
ax.set_yscale("log")
ax.set_ylim(0.3, 4.0)
ax.set_yticks([0.3, 0.5, 1.0, 2.0, 3.0])
ax.set_yticklabels(["0.3", "0.5", "1", "2", "3"])
ax.yaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
ax.legend(fontsize=7)
ax.set_title("Maximum of the residual per window")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig05_max_by_window.png"))

log("total time %.0f s" % (time.time() - T0))
LOG.close()
