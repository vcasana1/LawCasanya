#!/usr/bin/env python3
"""Envelope constant of Theorem E with the best published exponent-pair profiles.

C(e) = 1/(2 pi log 2) * int_0^1 e(s)/sqrt(s(2-s)) ds,  e(s) = 1/2 - s + e(1-s) for s < 1/2,
for e piecewise linear through finitely many points (sigma, mu) with mu(sigma) <= mu proved,
ending at (1, 0).  Each linear piece is integrated in closed form (s = 1 - cos th):
    int (a + b s)/sqrt(s(2-s)) ds = [(a+b) th - b sin th],
evaluated in interval arithmetic (mpmath.iv), so the printed upper ends are certified.

Inputs (exponent pairs (k,l) give mu(l-k) <= k, Ivic (7.57); chords are valid by convexity of mu):
  P0  Bourgain 2017: (13/84, 55/84)
  P1  Trudgian-Yang (arXiv:2306.05599, Lemma 1.1): (4742/38463, 35731/51284), (18/199, 593/796),
      (2779/38033, 58699/76066), (715/10238, 7955/10238)
  A   van der Corput A-process images A^j of all the above (j <= 25)
  HB  Heath-Brown 2017, Thm 2 (Proc. Steklov Inst. Math. 296, 88-103): (2/((m-1)^2(m+2)), 1-(3m-2)/(m(m-1)(m+2))), 3 <= m <= M
  P2  Tao-Trudgian-Yang (arXiv:2501.16779, Thm 20): (89/1282, 997/1282),
      (652397/9713986, 7599781/9713986), (10769/351096, 609317/702192), (89/3478, 15327/17390)
"""
from fractions import Fraction as F
import json, sys
from mpmath import iv, mp
iv.dps = 50; mp.dps = 50

def A(k, l): return (k/(2*k+2), F(1, 2) + l/(2*k+2))
def pt(k, l): return (l-k, k)
def achain(k, l, J):
    out = [pt(k, l)]
    for _ in range(J):
        k, l = A(k, l); out.append(pt(k, l))
    return out
def hb(M): return [(1-F(3*m*m-3*m+2, m*(m-1)**2*(m+2)), F(2, (m-1)**2*(m+2))) for m in range(3, M+1)]
def hull(points):
    pts = sorted(set(points)); h = []
    for p in pts:
        while len(h) >= 2:
            (x1, y1), (x2, y2) = h[-2], h[-1]
            if (y2-y1)*(p[0]-x1) >= (p[1]-y1)*(x2-x1): h.pop()
            else: break
        h.append(p)
    return h
def fi(x): x = F(x); return iv.mpf(x.numerator)/iv.mpf(x.denominator)
def th(s):  # arccos(1-s) = atan2(sqrt(s(2-s)), 1-s), s in [0,1]
    s = fi(s); return iv.atan2(iv.sqrt(s*(2-s)), 1-s)
def piece(s0, s1, a, b):
    t0, t1 = th(s0), th(s1)
    return (a+b)*(t1-t0) - b*(iv.sin(t1)-iv.sin(t0))
def C(verts):
    assert verts[-1] == (F(1), F(0)) and verts[0][0] == F(1, 2)
    tot = iv.mpf(0)
    for (x0, y0), (x1, y1) in zip(verts, verts[1:]):
        b = (y1-y0)/(x1-x0); a = y0-b*x0
        tot += piece(x0, x1, fi(a), fi(b))
        tot += piece(1-x1, 1-x0, fi(F(1, 2)+a+b), fi(-(1+b)))
    return tot/(2*iv.pi*iv.log(2))

B0 = (F(13, 84), F(55, 84))
TY = [B0, (F(4742, 38463), F(35731, 51284)), (F(18, 199), F(593, 796)),
      (F(2779, 38033), F(58699, 76066)), (F(715, 10238), F(7955, 10238))]
TTY = [(F(89, 1282), F(997, 1282)), (F(652397, 9713986), F(7599781, 9713986)),
       (F(10769, 351096), F(609317, 702192)), (F(89, 3478), F(15327, 17390))]
END = [(F(1), F(0))]
M = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
OUT = sys.argv[2] if len(sys.argv) > 2 else '.'
HBA = [q for (sg, mu) in hb(M) for q in achain(mu, sg+mu, 25)]
def Bp(k, l): return (l-F(1, 2), k+F(1, 2))
def ABA(Mb, J):
    """A-images (j<=J) of B-images of A-images (j<=J) of Bourgain's and Heath-Brown's pairs, m<=Mb."""
    base = [B0]+[(mu, sg+mu) for (sg, mu) in hb(Mb)]
    pairs = set()
    for p in base:
        k, l = p
        for _ in range(J+1):
            pairs.add((k, l)); k, l = A(k, l)
    for p in list(pairs):
        b = Bp(*p)
        if b[1]-b[0] >= F(1, 2) and b[0] >= 0:
            k, l = b
            for _ in range(J+1):
                pairs.add((k, l)); k, l = A(k, l)
    return [pt(*p) for p in pairs if p[1]-p[0] >= F(1, 2)]
cases = {
 'v7: Bourgain + A-process, J=30': hull(achain(*B0, 30)+END),
 'published: Bourgain 2017 + Heath-Brown 2017 chain + A-images': hull([q for q in achain(*B0, 25)]+[q for (sg, mu) in hb(M) for q in achain(mu, sg+mu, 25)]+END),
 'published + A-images of B-images of A-images (m <= 300, j <= 10)': hull(ABA(300, 10)+END),
 'TY23 hull: Bourgain + TY23 pairs + Heath-Brown chain, all with A-images': hull([q for p in TY for q in achain(*p, 25)]+HBA+END),
 'TY23 hull + TTY25 new pairs, all with A-images': hull([q for p in TY+TTY for q in achain(*p, 25)]+HBA+END),
 'Lindelof profile (e = 0 on [1/2,1]): floor of the one-disc method': [(F(1, 2), F(0))]+END,
}
out = {}
for name, v in cases.items():
    c = C(v); twopi = 2*iv.pi*c
    lo, hi = mp.mpf(c.a.a), mp.mpf(c.b.b); tlo, thi = mp.mpf(twopi.a.a), mp.mpf(twopi.b.b)
    out[name] = {'vertices': len(v), 'C_lower': mp.nstr(lo, 25), 'C_upper': mp.nstr(hi, 25),
                 '2piC_lower': mp.nstr(tlo, 15), '2piC_upper': mp.nstr(thi, 15)}
    print(f"{name}\n   vertices={len(v)}  C in [{mp.nstr(lo,16)}, {mp.nstr(hi,16)}]   2*pi*C in [{mp.nstr(tlo,12)}, {mp.nstr(thi,12)}]")
json.dump({'M_heath_brown': M, 'interval_dps': iv.dps, 'results': out}, open(OUT+'/envelope_best_profile_v9.json', 'w'), indent=1)
