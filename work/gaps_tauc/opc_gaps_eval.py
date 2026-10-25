"""Nearest-neighbour gap test: best zero-free tauc construction (c = 1.30) against the true ordinates,
on blocks OUTSIDE the untouched test set (k < 1 400 737).  zCasanya (8,8,512) is shown on the same blocks
for reference.  The true ordinates (data/zeross.bin) are read only here, to evaluate.

Unfolded gap of a list y: s_k = N0(y_{k+1}) - N0(y_k) (exact clock unfolding, computed without cancellation).
GUE reference: Wigner surmise beta = 2, CDF  erf(2x/sqrt(pi)) - (4x/pi) exp(-4x^2/pi).
Writes outputs/gaps_eval.json, outputs/gaps_eval.txt (same text as the console) and outputs/gaps_hist.png.
"""
import sys, os, glob, json
import numpy as np
from math import erf
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(REPO, 'work', 'v15_prep'))
from opc_common import *

TEST_FIRST_K = 1400737
tau_all = load(os.path.join(REPO, 'data', 'zLamb.bin'))
gam_all = load(os.path.join(REPO, 'data', 'zeross.bin'))
cas_all = load(os.path.join(REPO, 'work', 'data', 'zCasanya.bin'))
files = sorted(f for f in glob.glob(os.path.join(HERE, 'outputs', 'tauc_k*_c1.30.npy')) if '_n300_' not in f)
out = open(os.path.join(HERE, 'outputs', 'gaps_eval.txt'), 'w')
def say(s=''):
    print(s); out.write(s + '\n')

def gue_cdf(x):
    return np.array([erf(2 * v / np.sqrt(np.pi)) for v in np.atleast_1d(x)]) - 4 * x / np.pi * np.exp(-4 * x ** 2 / np.pi)

TH = np.array([0.025, 0.05, 0.075, 0.1, 0.15, 0.2, 0.3, 0.5])
report = dict(blocks=[], thresholds=TH.tolist())
allg, allt, allc = [], [], []
for f in files:
    a = np.load(f); idx = a[0].astype(int); x = a[1]
    assert idx.max() + 1 < TEST_FIRST_K
    tau, gam, cas = tau_all[idx], gam_all[idx], cas_all[idx]
    unf = lambda y: clock_diff(y[1:], tau[:-1]) - clock_diff(y[:-1], tau[:-1])
    sg, st, sc = unf(gam), unf(x), unf(cas)
    e = (clock_diff(x, tau) - clock_diff(gam, tau))             # ordinal error of tauc, units of zeros
    ec = (clock_diff(cas, tau) - clock_diff(gam, tau))
    blk = dict(file=os.path.basename(f), k_first=int(idx[0] + 1), k_last=int(idx[-1] + 1), n_gaps=int(sg.size),
               height=[float(gam[0]), float(gam[-1])],
               rms_err_tauc=float(np.sqrt(np.mean(e ** 2))), rms_err_zCasanya=float(np.sqrt(np.mean(ec ** 2))),
               rms_gapdiff_tauc=float(np.sqrt(np.mean((st - sg) ** 2))),
               rms_gapdiff_zCasanya=float(np.sqrt(np.mean((sc - sg) ** 2))),
               max_gapdiff_tauc=float(np.max(np.abs(st - sg))),
               var_gap=dict(gamma=float(sg.var()), tauc=float(st.var()), zCasanya=float(sc.var())),
               inversions=dict(tauc=int(np.sum(st <= 0)), zCasanya=int(np.sum(sc <= 0))),
               counts={lab: [int(np.sum(v < t)) for t in TH] for lab, v in (('gamma', sg), ('tauc', st), ('zCasanya', sc))},
               gue_expected=[float(sg.size * g) for g in gue_cdf(TH)])
    report['blocks'].append(blk); allg.append(sg); allt.append(st); allc.append(sc)
    say(f"Block k = {blk['k_first']} ... {blk['k_last']}  (gamma in [{gam[0]:.0f}, {gam[-1]:.0f}]), {sg.size} gaps")
    say(f"  ordinal RMS error (units of zeros): tauc {blk['rms_err_tauc']:.4f}   zCasanya {blk['rms_err_zCasanya']:.4f}")
    say(f"  RMS(s_tauc - s_gamma) {blk['rms_gapdiff_tauc']:.4f}  max {blk['max_gapdiff_tauc']:.4f}   RMS(s_zCas - s_gamma) {blk['rms_gapdiff_zCasanya']:.4f}")
    say(f"  gap variance: gamma {sg.var():.4f}  tauc {st.var():.4f}  zCasanya {sc.var():.4f}   (GUE surmise 0.1781)")
    say(f"  inversions (s <= 0): tauc {blk['inversions']['tauc']}  zCasanya {blk['inversions']['zCasanya']}")
    say('  ' + 'threshold'.ljust(10) + ''.join(f'{t:>8.3f}' for t in TH))
    for lab in ('gamma', 'tauc', 'zCasanya'):
        say('  ' + ('#' + lab).ljust(10) + ''.join(f'{c:>8d}' for c in blk['counts'][lab]))
    say('  ' + 'GUE exp.'.ljust(10) + ''.join(f'{c:>8.1f}' for c in blk['gue_expected']))
    say()

sg, st, sc = np.concatenate(allg), np.concatenate(allt), np.concatenate(allc)
# joint behaviour on the smallest true gaps
order = np.argsort(sg)[:25]
say('25 smallest true gaps (all blocks): s_gamma -> s_tauc')
say('  ' + '  '.join(f'{sg[i]:.3f}->{st[i]:.3f}' for i in order[:13]))
say('  ' + '  '.join(f'{sg[i]:.3f}->{st[i]:.3f}' for i in order[13:]))
small = sg < 0.15
say(f'gaps with s_gamma < 0.15: {small.sum()};  RMS(s_tauc - s_gamma) there {np.sqrt(np.mean((st[small]-sg[small])**2)):.4f}; '
    f'mean ratio s_tauc/s_gamma {np.mean(st[small]/sg[small]):.3f}')
# two-sample KS on the whole distribution and on s < 0.5
def ks(a, b):
    z = np.sort(np.concatenate([a, b]))
    return float(np.max(np.abs(np.searchsorted(np.sort(a), z, 'right') / a.size - np.searchsorted(np.sort(b), z, 'right') / b.size)))
ksall = ks(sg, st); kscas = ks(sg, sc)
say(f'two-sample KS distance gamma vs tauc {ksall:.4f}; gamma vs zCasanya {kscas:.4f}; '
    f'5% critical value for these sizes ~ {1.36*np.sqrt(2/sg.size):.4f}')
# small-s exponent: slope of log CDF vs log s on [0.05, 0.3]
grid = np.geomspace(0.05, 0.3, 12)
def slope(v):
    F = np.array([np.mean(v < g) for g in grid]); ok = F > 0
    return float(np.polyfit(np.log(grid[ok]), np.log(F[ok]), 1)[0])
say(f'log-log slope of the empirical CDF on [0.05, 0.3] (GUE: 3): gamma {slope(sg):.3f}  tauc {slope(st):.3f}  zCasanya {slope(sc):.3f}')
report.update(ks_gamma_tauc=ksall, ks_gamma_zCasanya=kscas, slope_cdf=dict(gamma=slope(sg), tauc=slope(st), zCasanya=slope(sc)),
              smallest=[[float(sg[i]), float(st[i]), float(sc[i])] for i in order],
              n_small_015=int(small.sum()))
json.dump(report, open(os.path.join(HERE, 'outputs', 'gaps_eval.json'), 'w'), indent=2)
out.close()

fig, axs = plt.subplots(1, 3, figsize=(16, 4.8))
bins = np.linspace(0, 3, 121); xs = np.linspace(0, 3, 400)
for v, lab, ls in ((sg, 'gamma (zeros)', '-'), (st, 'tauc c=1.30', '--'), (sc, 'zCasanya', ':')):
    axs[0].hist(v, bins=bins, density=True, histtype='step', lw=1.3, ls=ls, label=lab)
axs[0].plot(xs, 32 / np.pi ** 2 * xs ** 2 * np.exp(-4 * xs ** 2 / np.pi), 'k', lw=.8, label='GUE surmise')
axs[0].set_xlabel('unfolded gap s'); axs[0].set_title('nearest-neighbour gaps'); axs[0].legend(fontsize=8)
g2 = np.geomspace(0.01, 1, 60)
for v, lab, ls in ((sg, 'gamma', '-'), (st, 'tauc c=1.30', '--'), (sc, 'zCasanya', ':')):
    axs[1].loglog(g2, [max(np.mean(v < g), 1e-7) for g in g2], ls=ls, label=lab)
axs[1].loglog(g2, gue_cdf(g2), 'k', lw=.8, label='GUE surmise')
axs[1].set_xlabel('s'); axs[1].set_ylabel('P(gap < s)'); axs[1].set_title('small gaps (CDF, log-log)'); axs[1].legend(fontsize=8)
axs[2].plot(sg, st, ',', alpha=.4); axs[2].plot([0, 3], [0, 3], 'k', lw=.6)
axs[2].set_xlim(0, 0.6); axs[2].set_ylim(-0.05, 0.6); axs[2].set_xlabel('s_gamma'); axs[2].set_ylabel('s_tauc')
axs[2].set_title('same index: tauc gap vs true gap (s<0.6)')
[a.grid(alpha=.3) for a in axs]
fig.tight_layout(); fig.savefig(os.path.join(HERE, 'outputs', 'gaps_hist.png'), dpi=130)
