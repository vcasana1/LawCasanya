"""Prime phase of the displacement of the Riemann zeros: numerical part of ordinal_prime_cutoff_v2.

For a prime p, ell = log p, and a window of ordinals (a, b], with s_k = L(tau_k) (tau_k - gamma_k),
L(t) = log(t/2pi)/(2pi) and a_p = -1/(pi sqrt p), the script computes

  Pi^gamma_p = (2/a_p) <s_k sin(ell gamma_k)>     (phase at the zero)
  Pi^tau_p   = (2/a_p) <s_k sin(ell tau_k)>       (phase at the clock point)
  Pi^cos_p   = (2/a_p) <s_k cos(ell gamma_k)>     (cosine projection)
  theta_p    = ell / median log(tau_k/2pi)        (scale of the prime relative to the height)

for all primes p <= 20000 in five windows, the binned law against the conjectured function
  Pi_*(theta) = 1 - (1+theta) log(1+theta) - (1-theta) log(1-theta),
the segment function Pi_p(nu) = (2/a_p) <s_k sin(ell (gamma_k + nu delta_k))>, nu in [0,1],
and the exact accounting of the one-step clock: gain G_X = D_X - C_X, where
  D_X = 2 <s S_X(tau)> - v_X,  C_X = <S_X(tau)^2> - v_X,  v_X = sum_{p<=X} sum_m 1/(2 pi^2 m^2 p^m).

Data (not included in the repository): data/zeross.bin (ordinates), data/zLamb.bin (clock),
2,001,052 little-endian float64 values each.
Outputs: ../outputs/phase_*.csv, phase_law_log.txt; ../figures/fig09-fig11.
Usage: python3 opc_phase_law.py [data_dir]
"""
import hashlib
import os
import sys
import time

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "data")
OUT = os.path.join(HERE, "..", "outputs")
FIG = os.path.join(HERE, "..", "figures")
os.makedirs(OUT, exist_ok=True)
os.makedirs(FIG, exist_ok=True)
LOG = open(os.path.join(OUT, "phase_law_log.txt"), "w")
K_EXPECTED = 2001052


def log(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.write(s + "\n")
    LOG.flush()


def load(name):
    path = os.path.join(DATA, name)
    if not os.path.exists(path):
        sys.exit("missing data file %s (see README: data files are not included in the repository)" % path)
    raw = open(path, "rb").read()
    x = np.frombuffer(raw, dtype="<f8")
    if len(x) != K_EXPECTED:
        sys.exit("%s has %d values, expected %d" % (name, len(x), K_EXPECTED))
    log("%s  sha256 %s  n=%d" % (name, hashlib.sha256(raw).hexdigest(), len(x)))
    return x


log("python", sys.version.split()[0], " numpy", np.__version__, " matplotlib", matplotlib.__version__)
gam = load("zeross.bin")
tau = load("zLamb.bin")
K = K_EXPECTED
Lk = np.log(tau / (2 * np.pi))
s = Lk / (2 * np.pi) * (tau - gam)          # s_k = L(tau_k) delta_k
delta = tau - gam

WIN = [(10**3, 10**4), (10**4, 10**5), (10**5, 5 * 10**5), (5 * 10**5, 10**6), (10**6, K)]
WLAB = ["(1e3,1e4]", "(1e4,1e5]", "(1e5,5e5]", "(5e5,1e6]", "(1e6,%d]" % K]
LMED = [float(np.median(Lk[a:b])) for a, b in WIN]


def primes_upto(n):
    sv = np.ones(n + 1, bool)
    sv[:2] = False
    for q in range(2, int(n ** 0.5) + 1):
        if sv[q]:
            sv[q * q::q] = False
    return np.nonzero(sv)[0]


def Pi_star(th):
    th = np.asarray(th, float)
    return 1 - (1 + th) * np.log1p(th) - np.where(th < 1, (1 - th) * np.log1p(-np.minimum(th, 0.999999999)), 0.0)


PMAX = 20000
P = primes_upto(PMAX)
log("primes up to %d: %d" % (PMAX, len(P)))

# ------------------------------------------------------------------ per-prime projections
rows = []
for p in P:
    ell = np.log(p)
    ap = -1.0 / (np.pi * np.sqrt(p))
    sg = np.sin(gam * ell)
    st = np.sin(tau * ell)
    cg = np.cos(gam * ell)
    for j, (a, b) in enumerate(WIN):
        ss = s[a:b]
        n = b - a
        pg = np.mean(ss * sg[a:b]) / (ap / 2)
        pt = np.mean(ss * st[a:b]) / (ap / 2)
        pc = np.mean(ss * cg[a:b]) / (ap / 2)
        err = np.sqrt(np.mean(ss ** 2) / 2 / n) / abs(ap / 2)
        rows.append((p, j, ell / LMED[j], pg, pt, pc, err))
R = np.array(rows)
np.savetxt(os.path.join(OUT, "phase_projections_primes_to_20000.csv"), R, delimiter=",", fmt="%.8g",
           header="p,window_index,theta,Pi_gamma,Pi_tau,Pi_cos,stat_error_per_prime", comments="")
log("per-prime projections done, %.0f s" % (time.time() - T0))

# ------------------------------------------------------------------ binned law
edges = np.round(np.arange(0.1, 1.001, 0.1), 2)
bin_rows = []
for j in range(len(WIN)):
    r = R[R[:, 1] == j]
    for lo, hi in zip(edges[:-1], edges[1:]):
        m = (r[:, 2] >= lo) & (r[:, 2] < hi)
        if m.sum() < 3:
            continue
        th = r[m, 2]
        th2 = float(np.mean(th ** 2))
        y = float(np.mean(1 - r[m, 3]))
        se = float(np.sqrt(np.mean(r[m, 6] ** 2) / m.sum()))
        model = float(np.mean(1 - Pi_star(th)))
        bin_rows.append((j, lo, hi, int(m.sum()), th2, y, y / th2, se / th2, model / th2,
                         float(np.mean(1 - r[m, 4])), float(np.mean(r[m, 5]))))
with open(os.path.join(OUT, "phase_law_binned.csv"), "w") as f:
    f.write("window_index,theta_lo,theta_hi,n_primes,mean_theta2,mean_1_minus_Pi_gamma,ratio_to_theta2,"
            "ratio_stat_error,model_ratio,mean_1_minus_Pi_tau,mean_Pi_cos\n")
    for b_ in bin_rows:
        f.write("%d,%.1f,%.1f,%d,%.6f,%.6f,%.6f,%.6f,%.6f,%.6f,%.6f\n" % b_)
log("window  theta-bin   n_p   ratio(1-Pi_g)/theta^2  +-     model   1-Pi_tau   Pi_cos")
for b_ in bin_rows:
    log("%-12s [%.1f,%.1f) %5d   %.4f   %.4f   %.4f   %.4f   %+.4f" %
        (WLAB[b_[0]], b_[1], b_[2], b_[3], b_[6], b_[7], b_[8], b_[9], b_[10]))

# ------------------------------------------------------------------ fits on 0.2 <= theta < 0.8
fit_rows = []
for j in range(len(WIN)):
    r = R[R[:, 1] == j]
    m = (r[:, 2] >= 0.2) & (r[:, 2] < 0.8) & (r[:, 3] < 0.98)
    th, y, w = r[m, 2], 1 - r[m, 3], 1 / r[m, 6] ** 2
    A = np.vstack([np.log(th), np.ones_like(th)]).T * np.sqrt(w)[:, None]
    alpha, logc = np.linalg.lstsq(A, np.log(y) * np.sqrt(w), rcond=None)[0]
    c2 = np.sum(w * y * th ** 2) / np.sum(w * th ** 4)
    chi_q = np.sum(w * (y - c2 * th ** 2) ** 2) / (m.sum() - 1)
    chi_m = np.sum(w * (y - (1 - Pi_star(th))) ** 2) / m.sum()
    fit_rows.append((j, int(m.sum()), alpha, np.exp(logc), c2, chi_q, chi_m))
    log("%-12s n=%4d  power fit alpha=%.3f c=%.3f | alpha=2 fixed: c=%.3f chi2/dof=%.3f | model chi2/n=%.3f" %
        ((WLAB[j],) + fit_rows[-1][1:]))
with open(os.path.join(OUT, "phase_law_fits.csv"), "w") as f:
    f.write("window_index,n_primes,alpha_free,c_free,c_alpha2,chi2_per_dof_alpha2,chi2_per_n_model\n")
    for r_ in fit_rows:
        f.write("%d,%d,%.6f,%.6f,%.6f,%.6f,%.6f\n" % r_)

# ------------------------------------------------------------------ segment function Pi_p(nu), top window
a, b = WIN[-1]
NU = np.linspace(0, 1, 9)
seg_rows = []
for p in (61, 401, 907, 2003, 5003):
    ell = np.log(p)
    ap = -1.0 / (np.pi * np.sqrt(p))
    vals = [float(np.mean(s[a:b] * np.sin(ell * (gam[a:b] + nu * delta[a:b]))) / (ap / 2)) for nu in NU]
    integ = float(np.trapezoid(vals, NU)) if hasattr(np, "trapezoid") else float(np.trapz(vals, NU))
    seg_rows.append([p, ell / LMED[-1]] + vals + [integ])
    log("segment p=%5d theta=%.3f  Pi(nu) at nu=0,0.5,1: %.4f %.4f %.4f  max %.4f  integral %.4f" %
        (p, ell / LMED[-1], vals[0], vals[4], vals[-1], max(vals), integ))
with open(os.path.join(OUT, "phase_segment_top_window.csv"), "w") as f:
    f.write("p,theta," + ",".join("nu=%.3f" % v for v in NU) + ",integral_trapezoid\n")
    for r_ in seg_rows:
        f.write(",".join("%.6f" % v for v in r_) + "\n")

# ------------------------------------------------------------------ exact accounting of the one-step clock
LADDER = [7, 61, 401, 907, 1999]
acc_rows = []
for wi in (1, 2, 4):
    a, b = WIN[wi]
    t6, s6 = tau[a:b], s[a:b]
    S = np.zeros(b - a)
    vX = 0.0
    for p in P[P <= 2000]:
        S += -np.angle(1.0 - p ** -0.5 * np.exp(-1j * t6 * np.log(p))) / np.pi
        vX += sum(1.0 / (2 * np.pi ** 2 * m * m * float(p) ** m) for m in range(1, 60))
        if p in LADDER:
            G = float(np.mean(s6 ** 2) - np.mean((s6 - S) ** 2))
            D = float(2 * np.mean(s6 * S) - vX)
            C = float(np.mean(S ** 2) - vX)
            acc_rows.append((wi, int(p), b - a, G, D, C, vX))
            log("accounting %-12s X=%5d N=%7d  gain=%.5f  D=%.5f  C=%.5f  D-C=%.5f  v_X=%.5f" %
                (WLAB[wi], p, b - a, G, D, C, D - C, vX))
with open(os.path.join(OUT, "phase_accounting.csv"), "w") as f:
    f.write("window_index,X,N_zeros,gain,D_X,C_X,v_X\n")
    for r_ in acc_rows:
        f.write("%d,%d,%d,%.6f,%.6f,%.6f,%.6f\n" % r_)

# ------------------------------------------------------------------ figures
plt.rcParams.update({"font.size": 10, "figure.dpi": 200, "savefig.dpi": 200})
COL = ["#8064a2", "#e08a1e", "#4f9a3a", "#c0504d", "#1f4e79"]
xx = np.linspace(0.0, 0.95, 200)

fig, ax = plt.subplots(figsize=(7.2, 4.2))
for j in range(len(WIN)):
    br = [b_ for b_ in bin_rows if b_[0] == j]
    thm = [np.sqrt(b_[4]) for b_ in br]
    ax.errorbar(thm, [1 - b_[5] for b_ in br], yerr=[b_[7] * b_[4] for b_ in br], fmt="o", ms=3.5,
                color=COL[j], label="$k\\in$" + WLAB[j])
ax.plot(xx, Pi_star(xx), "-", color="k", lw=1.3, label="$\\Pi_*(\\theta)$")
ax.plot(xx, 1 - xx ** 2, "--", color="#777777", lw=1.0, label="$1-\\theta^2$")
ax.set_xlabel("$\\theta=\\log p/\\log(\\tau_k/2\\pi)$")
ax.set_ylabel("$\\Pi^\\gamma$ (binned)")
ax.legend(fontsize=7.5)
ax.set_title("Prime phase of the displacement at the zeros")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig09_phase_law.png"))

fig, ax = plt.subplots(figsize=(7.2, 4.2))
for j in range(len(WIN)):
    br = [b_ for b_ in bin_rows if b_[0] == j]
    ax.errorbar([np.sqrt(b_[4]) for b_ in br], [b_[6] for b_ in br], yerr=[b_[7] for b_ in br], fmt="o",
                ms=3.5, color=COL[j], label="$k\\in$" + WLAB[j])
xr = np.linspace(0.05, 0.95, 200)
ax.plot(xr, (1 - Pi_star(xr)) / xr ** 2, "-", color="k", lw=1.3, label="$(1-\\Pi_*(\\theta))/\\theta^2$")
ax.axhline(1, color="#777777", ls="--", lw=1.0)
ax.set_ylim(0.6, 1.5)
ax.set_xlabel("$\\theta$")
ax.set_ylabel("$(1-\\Pi^\\gamma)/\\theta^2$")
ax.legend(fontsize=7.5)
ax.set_title("Ratio to $\\theta^2$: data and the conjectured law")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig10_phase_law_ratio.png"))

fig, ax = plt.subplots(figsize=(7.2, 4.2))
for j in (1, 2, 4):
    br = [b_ for b_ in bin_rows if b_[0] == j]
    ax.plot([np.sqrt(b_[4]) for b_ in br], [1 - b_[9] for b_ in br], "s-", ms=3.5, color=COL[j],
            label="$\\Pi^\\tau$, $k\\in$" + WLAB[j])
    ax.plot([np.sqrt(b_[4]) for b_ in br], [1 - b_[5] for b_ in br], "o:", ms=3, color=COL[j],
            label="$\\Pi^\\gamma$, $k\\in$" + WLAB[j])
ax.plot(xx, Pi_star(xx), "-", color="k", lw=1.0, label="$\\Pi_*(\\theta)$")
ax.set_xlabel("$\\theta$")
ax.set_ylabel("binned projection")
ax.legend(fontsize=7)
ax.set_title("Phase at the clock point against phase at the zero")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig11_phase_clock_vs_zero.png"))

log("total time %.0f s" % (time.time() - T0))
LOG.close()
