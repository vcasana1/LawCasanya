# Phases exp(i*t*log p) (and exp(i*t), i.e. "p = e") at the midpoints of close pairs of true zeros,
# versus all gaps. Gamma read only to evaluate; blocks k < 1 400 737 (same blocks as gaps_eval).
import os, glob, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(HERE, 'opc_gaps_eval.py')).read().split("files = sorted")[0])
files = sorted(f for f in glob.glob(os.path.join(HERE, 'outputs', 'tauc_k*_c1.30.npy')) if '_n300_' not in f)
MID, SG = [], []
for f in files:
    idx = np.load(f)[0].astype(int); tau, gam = tau_all[idx], gam_all[idx]
    SG.append(clock_diff(gam[1:], tau[:-1]) - clock_diff(gam[:-1], tau[:-1]))
    MID.append(0.5 * (gam[1:] + gam[:-1]))
sg, mid = np.concatenate(SG), np.concatenate(MID)
bases = [('e', 1.0)] + [(str(p), np.log(p)) for p in (2, 3, 5, 7, 11, 13, 17, 19, 23)]
out = []
for lab, cut in [('all gaps', np.inf), ('s<0.30', .30), ('s<0.15', .15), ('s<0.10', .10), ('s<0.05', .05)]:
    m = sg < cut
    row = [f"{lab:9s} n={m.sum():6d}"]
    for name, L in bases:
        z = np.exp(1j * mid[m] * L)
        row.append(f"{name}:{z.real.mean():+.2f}")
    out.append("  ".join(row))
out.append("")
out.append("entries = mean of cos(t_mid * log p); |mean| for uniform phases ~ 1/sqrt(n)")
# also resultant length and mean angle for p=2,3 at s<0.10
m = sg < .10
for name, L in bases[:4]:
    z = np.exp(1j * mid[m] * L).mean()
    out.append(f"s<0.10  {name}: |mean e^(i t log p)| = {abs(z):.3f}, mean angle/pi = {np.angle(z)/np.pi:+.3f}")
txt = "\n".join(out); print(txt)
open(os.path.join(HERE, 'outputs', 'phases_close.txt'), 'w').write(txt + "\n")
