"""Task 1. Spectrum of the Newton residual E^(3) of zCasanya versus the ordinal residual r_k,
and the effect of solving the truncated equation exactly (true-derivative Newton from x^(3)).

E_k = N0(x_k) + S_X(x_k) - (k - 1/2),   X = dyadic cutoff of the third step (<= 512),
r_k = N0(gamma_k) - N0(x_k).
Writes outputs/task1_*.csv, outputs/task1_spectra.png and prints a report.
"""
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from opc_common import *

tau = load('zLamb.bin'); gam = load('zeross.bin'); cas = load('zCasanya.bin')
N = tau.size
k = np.arange(1, N + 1, dtype=float)
base = N0(tau) - (k - 0.5)
X3 = dyadic_cut(tau, 512)

S3, dS3 = S_and_dS(cas, X3)
E3 = base + clock_diff(cas, tau) + S3
r = clock_diff(gam, tau) - clock_diff(cas, tau)

# exact root of N0 + S_X = k - 1/2 from x^(3) with the true derivative
x = cas.copy()
ok = np.ones(N, bool)
for it in range(40):
    S, dS = S_and_dS(x, X3)
    res = base + clock_diff(x, tau) + S
    der = L(x) + dS
    bad = der <= 0.05 * L(x)
    ok &= ~bad
    step = np.where(bad, 0.0, res / np.where(bad, 1.0, der))
    step = np.clip(step, -0.25 / L(tau), 0.25 / L(tau))
    x = x - step
    conv = np.mean(np.abs(res[ok]) < 1e-9)
    print(f'iteration {it+1}: converged fraction {conv:.6f}, derivative failures {int((~ok).sum())}', flush=True)
    if conv > 0.99999 and it >= 5:
        break
S, dS = S_and_dS(x, X3)
res = base + clock_diff(x, tau) + S
ok &= (np.abs(res) < 1e-9) & (L(x) + dS > 0) & (np.abs(x - cas) < 0.5 / L(tau))
xs = np.where(ok, x, cas)
rs = clock_diff(gam, tau) - clock_diff(xs, tau)

def stats(name, xx, rr):
    g1 = rr[1:] - rr[:-1]; g2 = rr[2:] - rr[:-2]
    return dict(name=name, rms_height=float(np.sqrt(np.mean((xx - gam) ** 2))),
                rms_ordinal=float(np.sqrt(np.mean(rr ** 2))),
                gap_rms_h1=float(np.sqrt(np.mean(g1 ** 2))), gap_rms_h2=float(np.sqrt(np.mean(g2 ** 2))),
                acorr=acorr(rr), crossings=int(np.sum(np.diff(xx) <= 0)))

report = {'iterations': it + 1, 'exact_root_ok_fraction': float(ok.mean()),
          'E3_rms': float(np.sqrt(np.mean(E3 ** 2))), 'E3_acorr': acorr(E3),
          'R2_r_on_E3': float(np.corrcoef(r, E3)[0, 1] ** 2),
          'zCasanya': stats('zCasanya (8,8,512)', cas, r),
          'exact_root': stats('exact root, same cutoffs', xs, rs)}

blocks = [(2 ** 16, 2 ** 17), (2 ** 17, 2 ** 18), (2 ** 18, 2 ** 19), (2 ** 19, 2 ** 20), (2 ** 20, tau[-1] + 1)]
rows = []
fig, axs = plt.subplots(len(blocks), 1, figsize=(11, 13), sharex=True)
for ax, (lo, hi) in zip(axs, blocks):
    sel = (tau > lo) & (tau <= hi)
    tm = np.median(tau[sel]); ell = np.log(tm / TWO_PI)
    Xb = float(np.median(X3[sel])); edge = 1 - np.log(Xb) / ell
    row = dict(block=f'{lo}-{int(hi)}', n=int(sel.sum()), X3=Xb, edge_1_minus_c=edge)
    for nm, v in (('r', r[sel]), ('E3', E3[sel]), ('r_exact', rs[sel])):
        a, P, pk, band = periodogram_peak(v)
        row[f'peak_{nm}'] = pk; row[f'band_{nm}'] = band
        ax.semilogy(a, P, lw=0.8, label=f'{nm} (peak {pk:.3f})')
    row['corr_spectra_r_E3'] = float(np.corrcoef(*[np.log(periodogram_peak(v)[1][1:]) for v in (r[sel], E3[sel])])[0, 1])
    rows.append(row)
    ax.axvline(edge, color='k', ls=':', lw=1)
    for q in (2, 3, 4, 5, 7, 8):
        for sgn in (-1, 1):
            aq = edge + sgn * np.log(q) / ell
            if 0 < aq < 0.5:
                ax.axvline(aq, color='0.75', ls='--', lw=0.6)
    ax.set_title(f'tau in ({lo}, {int(hi)}], X3 = {Xb:.0f}, edge 1-c = {edge:.3f}')
    ax.legend(loc='lower left', fontsize=8); ax.grid(alpha=.3)
axs[-1].set_xlabel('ordinal frequency alpha')
fig.tight_layout(); fig.savefig('outputs/task1_spectra.png', dpi=130)

report['blocks'] = rows
json.dump(report, open('outputs/task1_report.json', 'w'), indent=2)
import csv
with open('outputs/task1_blocks.csv', 'w', newline='') as f:
    wr = csv.DictWriter(f, fieldnames=list(rows[0].keys())); wr.writeheader(); wr.writerows(rows)
print(json.dumps(report, indent=2))
