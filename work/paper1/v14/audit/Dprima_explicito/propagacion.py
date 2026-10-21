"""Order-of-magnitude propagation of explicit constants through the proof of
Theorem D' (v14), using the exact STTB22 constants of sttb22_C.py.
Only the dominant terms are kept (all neglected terms are smaller by many
orders of magnitude); the output is an estimate of the final constant, not a
certified bound."""
from mpmath import mp, mpf, pi, log, zeta
import importlib.util, sys, os
spec = importlib.util.spec_from_file_location('s', os.path.join(os.path.dirname(__file__), 'sttb22_C.py'))
mp.dps = 30
eps = mpf(1)/88
from mpmath import e
exec(open(os.path.join(os.path.dirname(__file__), 'sttb22_C.py')).read().split('eps = mpf(1)/88')[0])
C2 = C(eps, 2, e**16)[0]; C3 = C(eps, 3, e**16)[0]; C4 = C(eps, 4, e**16)[0]
# Lemma block_fourth: three dyadic blocks, ||S-S_X||_4^4 ~ C2 per block (prime-sum part O(1))
block = 3*C2
# Lemma slope_envelope as written (8th moments, k=4): int Z_j^8 <= 2*int (dS)^8, ||dS||_8 <= 2 C4^{1/8} T^{1/8} + O(sqrt log)
dS8 = (2*C4**(mpf(1)/8))**8
slope8 = 2048*zeta(4)*2*dS8*3           # 2048 sum j^-4 * 2 * (3 dyadic blocks)
# variant with 6th moments (k=3): (z-j/4)_+^4 <= 16 z^6/j^2
dS6 = (2*C3**(mpf(1)/6))**6
slope6 = 8*16*zeta(2)*2*dS6*3
for name, slope, k in (('as written (8th moments)', slope8, 4), ('6th-moment variant', slope6, 3)):
    Cr = (slope**(mpf(1)/4) + 2*block**(mpf(1)/4))**4
    u4 = 2*Cr*2                          # <u^4> <= 2 Lambda Cr T / #I, #I ~ T Lambda / 2 (dyadic window)
    spacings = 2*u4**(mpf(1)/4)          # |x-gamma| <= 2|u|/Lambda, spacing = 1/Lambda
    logT_break = spacings/mpf('0.6331')*2*pi/(2*pi)  # trivial: |delta_k|*Lambda <= 0.6331*log T/(2 pi)
    print(name, ': T0 >= e^%d' % (1408*k), ' C_r ~ %s' % mp.nstr(Cr, 3),
          ' <u^4> <= %s' % mp.nstr(u4, 3), ' L^4-error <= %s mean spacings' % mp.nstr(spacings, 3),
          ' beats trivial clock bound only if log T > %s' % mp.nstr(spacings*2*pi/mpf('0.6331'), 3))
