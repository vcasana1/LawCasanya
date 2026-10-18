"""Linear and quadratic parts of the walk drift relative to the clock on the untouched indices,
for the zeros, zCasanya, Stage A and R2 (points from work/v15_prep/outputs/task3_points.npy)."""
import sys, numpy as np
sys.path.insert(0, '.')
from opc_common_v15 import *
tau = load('zLamb.bin')[1400736:]; gam = load('zeross.bin')[1400736:]; cas = load('zCasanya.bin')[1400736:]
p = np.load('../../v15_prep/outputs/task3_points.npy')
n = tau.size; w = (n - np.arange(n)) / n; E = w * np.exp(1j * tau)
for nm, x in (('zeros', gam), ('zCasanya', cas), ('Stage A', p[0]), ('R1', p[1]), ('R2', p[2])):
    y = tau - x
    tot = np.sum(E * (np.exp(-1j * y) - 1)); lin = np.sum(E * (-1j * y)); quad = np.sum(E * (-y ** 2 / 2))
    print(f'{nm:9s} total {tot.real:+8.3f}{tot.imag:+8.3f}i  linear {lin.real:+8.3f}{lin.imag:+8.3f}i  quadratic {quad.real:+8.3f}{quad.imag:+8.3f}i')
