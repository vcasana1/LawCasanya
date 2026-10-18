"""Tests of the finite-height and finite-window statements of ordinal_prime_cutoff_v13.

Usage: python3 opc_checks_v13.py DATA_DIR

Inputs : DATA_DIR/zeross.bin (ordinates gamma_k), DATA_DIR/zLamb.bin (clock tau_k), each exactly
         2,001,052 little-endian float64 values; ../outputs/table_F_direct_defects.csv and
         ../outputs/table_G_prime_responses.csv written by opc_extensions_v13.py.
Outputs: ../outputs/check_envelope.csv          finite-height envelope (Remark on Bellotti--Wong)
         ../outputs/check_accounting.csv        exact finite-window gain = diagonal - cross term
         ../outputs/check_response_bins.csv     grouped moving-prime responses (bin width 0.05, >= 5 primes)
         ../outputs/check_log.txt               everything printed
         ../figures/fig02_direct_defects.png    direct ordinal defects against the cutoff exponent
         ../figures/fig03_accounting.png        gain, diagonal part and cross term against the cutoff
         ../figures/fig07_response_law.png      grouped responses R^gamma against 1 - Phi(theta)
         ../figures/fig08_response_clock_vs_zero.png   R^tau against R^gamma

Notation (as in the paper): N_0(t) = t/(2 pi) log(t/(2 pi e)) + 7/8, L(t) = log(t/2pi)/(2pi),
s_k = k - 1/2 - N_0(gamma_k) (exact), delta_k = tau_k - gamma_k,
BW(t) = 0.10076 log t + 0.24460 log log t + 8.08344,
a_n = -Lambda(n)/(pi sqrt(n) log n), S_X(t) = sum over prime powers p^m, p <= X, of a_{p^m} sin(t log p^m),
v_X = (1/2) sum a_n^2, Cr_X = <S_X(tau_k)^2> - v_X, D_X = 2 <s_k S_X(tau_k)> - v_X.
No parameter is fitted.
"""
import csv
import os
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "data")
OUT = os.path.join(HERE, "..", "outputs")
FIG = os.path.join(HERE, "..", "figures")
os.makedirs(OUT, exist_ok=True)
os.makedirs(FIG, exist_ok=True)
LOG = open(os.path.join(OUT, "check_log.txt"), "w")
K = 2001052


def log(*a):
    s = " ".join(str(x) for x in a)
    print(s, flush=True)
    LOG.write(s + "\n")
    LOG.flush()


def load(name):
    path = os.path.join(DATA, name)
    if os.path.getsize(path) != 8 * K:
        raise ValueError("%s: expected exactly %d float64 values" % (path, K))
    x = np.fromfile(path, dtype="<f8")
    if not np.isfinite(x).all() or np.any(np.diff(x) < 0):
        raise ValueError("%s: values must be finite and nondecreasing" % path)
    return x


def primes_upto(n):
    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(n ** 0.5) + 1):
        if sieve[p]:
            sieve[p * p::p] = False
    return np.flatnonzero(sieve)


def Phi(th):
    th = np.asarray(th, dtype=float)
    return (1 + th) * np.log1p(th) + (1 - th) * np.log1p(-th)


gam = load("zeross.bin")
tau = load("zLamb.bin")
k = np.arange(1, K + 1, dtype=float)
N0g = gam / (2 * np.pi) * np.log(gam / (2 * np.pi * np.e)) + 7 / 8
s = k - 0.5 - N0g
delta = tau - gam
Lg = np.log(gam / (2 * np.pi)) / (2 * np.pi)
Lt = np.log(tau / (2 * np.pi)) / (2 * np.pi)
WINDOWS = [(0, 1000), (1000, 10000), (10000, 100000), (100000, 500000), (500000, 1000000), (1000000, K)]
LAB = ["(0,1e3]", "(1e3,1e4]", "(1e4,1e5]", "(1e5,5e5]", "(5e5,1e6]", "(1e6,K]"]

# ------------------------------------------------------------------ 1. finite-height envelope
BW = 0.10076 * np.log(gam) + 0.24460 * np.log(np.log(gam)) + 8.08344
upper = (BW - 11 / 8) / Lg
lower = -(BW + 3 / 8) / Lt
ok_s = bool(np.all((s >= -BW - 3 / 8) & (s <= BW - 11 / 8)))
ok_d = bool(np.all((delta >= lower) & (delta <= upper)))
log("envelope: ordinal sandwich holds for all k:", ok_s, "; displacement envelope holds for all k:", ok_d)
rows = []
for (a, b), lab in zip(WINDOWS, LAB):
    d, u, l = delta[a:b], upper[a:b], lower[a:b]
    rows.append((lab, b - a, float(gam[a]), float(gam[b - 1]), float(d.max()), float(d.min()),
                 float(u.min()), float(l.max()), float(np.max(d / u)), float(np.max(-d / np.abs(l)))))
    log("envelope %-10s max delta=%.6f min delta=%.6f  min upper=%.4f  max lower=%.4f  max delta/upper=%.4f  max(-delta)/|lower|=%.4f"
        % (lab, rows[-1][4], rows[-1][5], rows[-1][6], rows[-1][7], rows[-1][8], rows[-1][9]))
with open(os.path.join(OUT, "check_envelope.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(("window", "zero_count", "gamma_first", "gamma_last", "max_delta", "min_delta",
                "min_upper_envelope", "max_lower_envelope", "max_delta_over_upper", "max_minus_delta_over_abs_lower"))
    w.writerows(rows)
j = int(np.argmax(np.abs(delta)))
log("global max |delta_k| = %.6f at k = %d (gamma = %.6f)" % (abs(delta[j]), j + 1, gam[j]))

# ------------------------------------------------------------------ 2. exact finite-window accounting
PR = primes_upto(2000)
XS = [7, 61, 401, 907, 1999]
ACC_W = [1, 2, 3, 4, 5]                      # indices into WINDOWS: all windows above k = 1000
acc = []
for wi in ACC_W:
    a, b = WINDOWS[wi]
    t, sw = tau[a:b], s[a:b]
    S = np.zeros(b - a)
    vX = 0.0
    done = 0
    for X in XS:
        for p in PR[(PR > done) & (PR <= X)]:
            p = int(p)
            lp = np.log(p)
            m = 1
            while p ** (-m / 2) > 1e-17:
                S += -np.sin(m * lp * t) / (np.pi * m * p ** (m / 2))
                vX += 1 / (2 * np.pi ** 2 * m * m * p ** m)
                m += 1
        done = X
        gain = float(np.mean(sw * sw) - np.mean((sw - S) ** 2))
        D = float(2 * np.mean(sw * S) - vX)
        Cr = float(np.mean(S * S) - vX)
        acc.append((LAB[wi], X, b - a, float(np.mean(sw * sw)), gain, D, Cr, vX))
        log("accounting %-10s X=%5d  <s^2>=%.6f  gain=%.6f  D=%.6f  Cr=%.6f  D-Cr-gain=%.1e  v_X=%.6f"
            % (LAB[wi], X, float(np.mean(sw * sw)), gain, D, Cr, D - Cr - gain, vX))
with open(os.path.join(OUT, "check_accounting.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(("window", "X", "zero_count", "mean_s2", "gain", "diagonal_D_X", "cross_Cr_X", "v_X"))
    w.writerows(acc)

# ------------------------------------------------------------------ 3. grouped moving-prime responses
G = []
with open(os.path.join(OUT, "table_G_prime_responses.csv")) as f:
    for r in csv.DictReader(f):
        G.append((int(r["window"]), int(r["prime"]), float(r["theta_median"]), float(r["rho_gamma"]),
                  float(r["rho_tau"])))
G = np.array(G)
bins = []
edges = np.round(np.arange(0.0, 1.0001, 0.05), 2)
for wnd in range(1, 6):
    Gw = G[G[:, 0] == wnd]
    for lo, hi in zip(edges[:-1], edges[1:]):
        sel = Gw[(Gw[:, 2] >= lo) & (Gw[:, 2] < hi)]
        if len(sel) < 5:
            continue
        law = 1 - Phi(sel[:, 2])
        bins.append((wnd, lo, hi, len(sel), float(np.mean(sel[:, 2])), float(np.mean(sel[:, 3])),
                     float(np.mean(law)), float(np.mean(sel[:, 3]) - np.mean(law)),
                     float(np.std(sel[:, 3] - law) / np.sqrt(len(sel))), float(np.mean(sel[:, 4]))))
with open(os.path.join(OUT, "check_response_bins.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(("window", "theta_lo", "theta_hi", "prime_count", "mean_theta", "mean_R_gamma",
                "mean_law", "difference", "standard_error_of_difference", "mean_R_tau"))
    w.writerows(bins)
for r in bins:
    if r[0] == 5:
        log("bins top window [%.2f,%.2f) n=%4d  R^g=%.6f  law=%.6f  diff=%+.6f (se %.6f)  R^t=%.6f"
            % (r[1], r[2], r[3], r[5], r[6], r[7], r[8], r[9]))

# ------------------------------------------------------------------ figures
plt.rcParams.update({"font.size": 10, "figure.dpi": 200, "savefig.dpi": 200})
F = []
with open(os.path.join(OUT, "table_F_direct_defects.csv")) as f:
    for r in csv.DictReader(f):
        F.append((int(r["r"]), float(r["c"]), float(r["mean_u2"]), float(r["mean_one_step_r2"])))
F = np.array(F)
fig, ax = plt.subplots(figsize=(7, 4))
cols = {14: "tab:purple", 16: "tab:orange", 18: "tab:green", 19: "tab:blue"}
for r in (14, 16, 18, 19):
    sel = F[F[:, 0] == r]
    x = np.log(1 / sel[:, 1])
    ax.plot(x, sel[:, 2], "o-", color=cols[r], label=r"$\langle u_k(X)^2\rangle$, $T=2^{%d}$" % r)
    ax.plot(x, sel[:, 3], "s:", mfc="none", color=cols[r], label=r"$\langle r_k(X)^2\rangle$, $T=2^{%d}$" % r)
xx = np.linspace(0.6, 2.4, 50)
ax.plot(xx, xx / (2 * np.pi ** 2), "k--", label=r"$\frac{1}{2\pi^2}\log(1/c)$")
ax.set_xlabel(r"$\log(1/c)$, $X=T^c$")
ax.set_ylabel("mean over $T<\\gamma_k\\leq 2T$")
ax.set_title("Direct ordinal defects against the cutoff exponent")
ax.legend(fontsize=6.5, ncol=2)
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig02_direct_defects.png"))

fig, ax = plt.subplots(figsize=(7, 5.4))
wcols = {"(1e3,1e4]": "tab:purple", "(1e4,1e5]": "tab:orange", "(1e5,5e5]": "tab:green",
         "(5e5,1e6]": "tab:red", "(1e6,K]": "tab:blue"}
TEXW = {"(1e3,1e4]": r"$(10^3,10^4]$", "(1e4,1e5]": r"$(10^4,10^5]$", "(1e5,5e5]": r"$(10^5,5\cdot10^5]$",
        "(5e5,1e6]": r"$(5\cdot10^5,10^6]$", "(1e6,K]": r"$(10^6,K]$"}
for lab in wcols:
    rr = [x for x in acc if x[0] == lab]
    X = [x[1] for x in rr]
    ax.plot(X, [x[4] for x in rr], "o-", color=wcols[lab], label=r"gain, $k\in$" + TEXW[lab])
    ax.plot(X, [x[6] for x in rr], "s:", mfc="none", color=wcols[lab], label=r"$\mathrm{Cr}_X$, $k\in$" + TEXW[lab])
ax.plot(XS, [acc[i][7] for i in range(len(XS))], "k--", label=r"$v_X$")
ax.set_xscale("log")
ax.set_xlabel("cutoff $X$ (primes $p\\leq X$, full local factors)")
ax.set_ylabel("mean square")
ax.set_title("Exact finite-window accounting of the one-step gain")
ax.legend(fontsize=7, ncol=3, loc="upper center", bbox_to_anchor=(0.5, -0.17))
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig03_accounting.png"))

B = np.array([b for b in bins])
fig, ax = plt.subplots(figsize=(7, 4))
th = np.linspace(0, 0.97, 200)
ax.plot(th, 1 - Phi(th), "k-", label=r"$1-\Phi(\theta)$")
ax.plot(th, 1 - th ** 2, color="gray", ls="--", label=r"$1-\theta^2$")
wl = {1: r"$(10^3,10^4]$", 2: r"$(10^4,10^5]$", 3: r"$(10^5,5\cdot10^5]$", 4: r"$(5\cdot10^5,10^6]$", 5: r"$(10^6,K]$"}
wc = {1: "tab:purple", 2: "tab:orange", 3: "tab:green", 4: "tab:red", 5: "tab:blue"}
for wnd in range(1, 6):
    sel = B[B[:, 0] == wnd]
    ax.errorbar(sel[:, 4], sel[:, 5], yerr=sel[:, 8], fmt="o", ms=3.5, color=wc[wnd], label=r"$k\in$" + wl[wnd])
ax.set_xlabel(r"$\theta=\log p/\mathrm{median}\,\log(\tau_k/2\pi)$")
ax.set_ylabel(r"bin mean of $\mathcal{R}^{\gamma}_p$")
ax.set_title(r"Prime responses of $s_k$ at the zeros (bins of width 0.05 in $\theta$)")
ax.legend(fontsize=7)
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig07_response_law.png"))

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(th, 1 - Phi(th), "k-", lw=1, label=r"$1-\Phi(\theta)$")
for wnd in (2, 3, 5):
    sel = B[B[:, 0] == wnd]
    ax.plot(sel[:, 4], sel[:, 9], "s-", color=wc[wnd], label=r"$\mathcal{R}^{\tau}_p$, $k\in$" + wl[wnd])
    ax.plot(sel[:, 4], sel[:, 5], "o:", color=wc[wnd], label=r"$\mathcal{R}^{\gamma}_p$, $k\in$" + wl[wnd])
ax.set_xlabel(r"$\theta$")
ax.set_ylabel("bin mean of the response")
ax.set_title("Response at the clock point against response at the zero")
ax.legend(fontsize=7)
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig08_response_clock_vs_zero.png"))
log("done")
LOG.close()
