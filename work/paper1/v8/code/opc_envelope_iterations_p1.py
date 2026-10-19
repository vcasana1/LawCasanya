#!/usr/bin/env python3
"""Envelope coefficient C_J of Theorem E for the profile built from Bourgain's exponent pair (13/84, 55/84)
by J applications of van der Corput's A-process, A(k,l) = (k/(2k+2), 1/2 + l/(2k+2)), the points
(l_j - k_j, k_j), j = 0..J, joined linearly to (1,0) and reflected by the functional equation:
   C(e) = (1/(2 pi log 2)) int_0^1 e(sigma) / sqrt(sigma (2 - sigma)) d sigma,
   e(sigma) = 1/2 - sigma + e(1 - sigma) on [0, 1/2).
Exact rational vertices; each linear piece integrated in closed form with mpmath at 50 digits:
   int (alpha s + beta) / sqrt(s(2-s)) ds = -alpha sqrt(s(2-s)) + (alpha + beta) arcsin(s - 1).
For every J the bound a <= C_J holds (Theorem E); C_J decreases with J.  Also checks that each new vertex lies
below the chord from the previous vertex to (1,0).  No data are read.
Usage: python3 opc_envelope_iterations_p1.py [OUT_DIR]   (writes envelope_iterations_p1.{json,txt})
"""
import json, os, sys
from fractions import Fraction as Fr
import mpmath as mp

def realq(value):
    """Convert exact rational vertices without relying on mpf(Fraction)."""
    if isinstance(value, Fr):
        return mp.mpf(value.numerator) / mp.mpf(value.denominator)
    return mp.mpf(value)


mp.mp.dps = 50
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), '../outputs')


def vertices(J):
    k, l = Fr(13, 84), Fr(55, 84)
    P = [(l - k, k)]
    for _ in range(J):
        k, l = k / (2 * k + 2), Fr(1, 2) + l / (2 * k + 2)
        P.append((l - k, k))
    P.append((Fr(1), Fr(0)))
    return P


def prim(alpha, beta, s):
    s = realq(s)
    return -alpha * mp.sqrt(s * (2 - s)) + (alpha + beta) * mp.asin(s - 1)


def piece_integral(a, ea, b, eb):
    alpha = realq(eb - ea) / realq(b - a)
    beta = realq(ea) - alpha * realq(a)
    return prim(alpha, beta, b) - prim(alpha, beta, a)


def coefficient(P):
    total = realq(0)
    for (a, ea), (b, eb) in zip(P, P[1:]):          # right half [1/2, 1]
        total += piece_integral(a, ea, b, eb)
    # left half: e(s) = 1/2 - s + e(1-s); vertices reflected: s' = 1 - a, value 1/2 - s' + ea (linear in s')
    for (a, ea), (b, eb) in zip(P, P[1:]):
        sa, sb = 1 - b, 1 - a                       # interval [1-b, 1-a] in [0, 1/2]
        va, vb = Fr(1, 2) - sa + eb, Fr(1, 2) - sb + ea
        total += piece_integral(sa, va, sb, vb)
    return total / (2 * mp.pi * mp.log(2))


rows, lines = [], []
prev = None
for J in range(0, 31):
    P = vertices(J)
    below = None
    if J >= 1:
        (s0, k0), (s1, k1) = P[-3], P[-2]
        below = bool(k1 < k0 * (1 - s1) / (1 - s0))
    c = coefficient(P)
    sJ, kJ = P[-2]
    tail = 3 * realq(kJ) * mp.sqrt(1 - realq(sJ)) / (2 * mp.pi * mp.log(2))   # bound for C_J - C_inf (Theorem E, 'The limit')
    rows.append(dict(J=J, last_vertex=[str(P[-2][0]), str(P[-2][1])], below_chord=below,
                     C_J=mp.nstr(c, 20), two_pi_C_J=mp.nstr(2 * mp.pi * c, 20), bound_CJ_minus_Cinf=mp.nstr(tail, 6),
                     decrease=None if prev is None else mp.nstr(prev - c, 6)))
    lines.append(f"J={J:2d}  sigma_J={float(P[-2][0]):.8f}  below_chord={below}  C_J={mp.nstr(c, 16)}  "
                 f"2pi*C_J={mp.nstr(2 * mp.pi * c, 12)}  C_J-C_inf<={mp.nstr(tail, 4)}" + ("" if prev is None else f"  decrease={mp.nstr(prev - c, 4)}"))
    prev = c
os.makedirs(OUT, exist_ok=True)
json.dump(rows, open(os.path.join(OUT, 'envelope_iterations_p1.json'), 'w'), indent=1)
open(os.path.join(OUT, 'envelope_iterations_p1.txt'), 'w').write('\n'.join(lines) + '\n')
print('\n'.join(lines))
