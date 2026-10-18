"""Centroids of the phase walks P_j(x) = sum_{k<=j} e^{i x_k} over all K = 2 001 052 indices,
C_K(x) = (1/K) sum_{j<=K} P_j(x) = sum_{k<=K} (K-k+1)/K e^{i x_k},
for the ordinates, the clock and zCasanya, and the exact angular/radial split of C_K(x) - C_K(gamma):
  C_K(x) - C_K(gamma) = i A + B,  A = sum_k w_k e^{i gamma_k} sin(eps_k),  B = sum_k w_k e^{i gamma_k} (cos(eps_k) - 1),
  eps_k = x_k - gamma_k,  w_k = (K-k+1)/K.
Writes ../outputs/walk_centroids_v15.{json,txt} (same text as the console).
"""
import json, os
import numpy as np
from opc_common_v15 import *

HERE = os.path.dirname(os.path.abspath(__file__))
out = open(os.path.join(HERE, '../outputs/walk_centroids_v15.txt'), 'w')


def say(s=''):
    print(s, flush=True)
    out.write(s + '\n')


def c(z):
    return [float(z.real), float(z.imag)]


gam = load('zeross.bin'); tau = load('zLamb.bin'); cas = load('zCasanya.bin')
K = gam.size
w = (K - np.arange(K)) / K
C = {nm: complex(np.sum(w * np.exp(1j * x))) for nm, x in (('zeros', gam), ('clock', tau), ('zCasanya', cas))}
res = {'centroids': {k: c(v) for k, v in C.items()}}
for nm, x in (('clock', tau), ('zCasanya', cas)):
    eps = x - gam
    A = complex(np.sum(w * np.exp(1j * gam) * np.sin(eps)))
    B = complex(np.sum(w * np.exp(1j * gam) * (np.cos(eps) - 1)))
    closure = abs(1j * A + B - (C[nm] - C['zeros']))
    res[nm] = dict(iA=c(1j * A), B=c(B), difference=c(C[nm] - C['zeros']), closure=closure,
                   abs_difference=abs(C[nm] - C['zeros']))
    say(f'{nm}: C(x)-C(gamma) = {C[nm]-C["zeros"]:.6f}, iA = {1j*A:.6f}, B = {B:.6f}, closure {closure:.1e}')
for k, v in C.items():
    say(f'centroid {k}: {v:.6f}')
say(f'|C(zCasanya)-C(clock)| = {abs(C["zCasanya"]-C["clock"]):.4f}')
json.dump(res, open(os.path.join(HERE, '../outputs/walk_centroids_v15.json'), 'w'), indent=2)
out.close()
