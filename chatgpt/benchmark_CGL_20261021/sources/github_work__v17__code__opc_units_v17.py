"""Root mean square of the errors x_k - gamma_k in height and in units of the mean spacing,
lL(tau_k) (x_k - gamma_k) with lL(t) = log(t/2pi)/(2pi), for the constructions of Tables tab:rule and
tab:beyond_nyquist.  The ordinates are read only to evaluate.  Writes ../outputs/units_v17.{json,txt}."""
import json, os
import numpy as np
from opc_common_v15 import *

HERE = os.path.dirname(os.path.abspath(__file__))
PREP = os.path.join(HERE, '../../v15_prep/outputs')
out = open(os.path.join(HERE, '../outputs/units_v17.txt'), 'w')


def say(s):
    print(s); out.write(s + '\n')


tau_all = load('zLamb.bin'); gam_all = load('zeross.bin'); cas_all = load('zCasanya.bin')
first = 1400736
pts3 = np.load(os.path.join(PREP, 'task3_points.npy'))
rows = []


def ev(setname, nm, idx, x):
    e = x - gam_all[idx]
    r = dict(set=setname, method=nm, rms_height=float(np.sqrt(np.mean(e ** 2))),
             rms_spacings=float(np.sqrt(np.mean((L(tau_all[idx]) * e) ** 2))),
             mean_spacing=float(np.mean(1 / L(tau_all[idx]))))
    rows.append(r)
    say(f"{setname:10s} {nm:22s} rms height {r['rms_height']:.5f}  rms in mean spacings {r['rms_spacings']:.5f}  mean spacing {r['mean_spacing']:.4f}")


test = np.arange(first, tau_all.size)
for nm, x in (('clock', tau_all[test]), ('zCasanya', cas_all[test]), ('Stage A', pts3[0]), ('R1', pts3[1]), ('R2', pts3[2])):
    ev('untouched', nm, test, x)
b3 = np.load(os.path.join(PREP, 'task4_points_c1.30_b3.npy'))[0].astype(int)
ev('block 3', 'clock', b3, tau_all[b3]); ev('block 3', 'zCasanya', b3, cas_all[b3]); ev('block 3', 'R2', b3, pts3[2][b3 - first])
for c in ('0.85', '1.00'):
    z = np.load(os.path.join(PREP, f'task4_points_c{c}.npy')); ii = z[0].astype(int)
    ev('block 3', f'c={c}', b3, z[1][np.searchsorted(ii, b3)])
for c in ('1.15', '1.30'):
    ev('block 3', f'c={c}', b3, np.load(os.path.join(PREP, f'task4_points_c{c}_b3.npy'))[1])
json.dump(rows, open(os.path.join(HERE, '../outputs/units_v17.json'), 'w'), indent=2)
out.close()
