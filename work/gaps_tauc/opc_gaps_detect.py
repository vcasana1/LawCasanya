# Precision/recall of small tauc gaps as detector of small true gaps (close pairs).
# Uses only already-built tauc outputs; gamma read only to evaluate. Blocks k < 1 400 737.
import os, glob, numpy as np, json
HERE = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(HERE, 'opc_gaps_eval.py')).read().split("files = sorted")[0])  # reuse loaders/paths
files = sorted(f for f in glob.glob(os.path.join(HERE, 'outputs', 'tauc_k*_c1.30.npy')) if '_n300_' not in f)
ST, SG = [], []
for f in files:
    a = np.load(f); idx = a[0].astype(int); x = a[1]
    tau, gam = tau_all[idx], gam_all[idx]
    unf = lambda y: clock_diff(y[1:], tau[:-1]) - clock_diff(y[:-1], tau[:-1])
    ST.append(unf(x)); SG.append(unf(gam))
st, sg = np.concatenate(ST), np.concatenate(SG); n = len(st)
out = [f"total gaps {n}", "", "PRECISION: among tauc gaps below thr, fraction of true gaps below g"]
out.append("thr_tauc  count   g<0.10  g<0.15  g<0.20  g<0.30   (base rate g<0.10 / g<0.15: %.4f / %.4f)" % ((sg<0.1).mean(), (sg<0.15).mean()))
res = {}
for t in [0.19, 0.20, 0.21, 0.22, 0.25, 0.30]:
    m = st < t; c = m.sum()
    row = [((sg[m] < g).mean() if c else 0) for g in (0.10, 0.15, 0.20, 0.30)]
    out.append(f"  {t:.2f}   {c:6d}   " + "  ".join(f"{r:.3f}" for r in row)); res[f"prec_{t}"] = [int(c)] + row
out += ["", "RECALL: among true gaps below g, fraction with tauc gap below thr"]
out.append("g_true   count   t<0.20  t<0.22  t<0.25  t<0.30")
for g in [0.05, 0.075, 0.10, 0.15]:
    m = sg < g; c = m.sum()
    row = [((st[m] < t).mean() if c else 0) for t in (0.20, 0.22, 0.25, 0.30)]
    out.append(f"  {g:.3f}  {c:6d}   " + "  ".join(f"{r:.3f}" for r in row)); res[f"rec_{g}"] = [int(c)] + row
r = np.corrcoef(st[sg < 0.4], sg[sg < 0.4])[0, 1]
out += ["", f"Spearman-like check: Pearson corr(s_tauc, s_gamma | s_gamma<0.4) = {r:.3f}"]
txt = "\n".join(out); print(txt)
open(os.path.join(HERE, 'outputs', 'gaps_detect.txt'), 'w').write(txt + "\n")
json.dump(res, open(os.path.join(HERE, 'outputs', 'gaps_detect.json'), 'w'), indent=1)
