#!/usr/bin/env python3
"""Outward-rounded confirmation of the decimal bound in Theorem E.

Uses rational vertices and interval elementary functions, not zero data.
Parameters are fixed by the proof: 30 A-process steps, 80 decimal digits.
Run: python code/verify_envelope_intervals_v5.py [OUTPUT_DIRECTORY]
"""
from fractions import Fraction as Q
from pathlib import Path
import json
import sys
import mpmath as mp

mp.iv.dps = 80
iv = mp.iv

def rq(q):
    q = Q(q)
    return iv.mpf(q.numerator)/iv.mpf(q.denominator)

def vertices(steps):
    k, ell = Q(13,84), Q(55,84)
    result = [(ell-k,k)]
    for _ in range(steps):
        k, ell = k/(2*k+2), Q(1,2)+ell/(2*k+2)
        result.append((ell-k,k))
    return result+[(Q(1),Q(0))]

def primitive(alpha, beta, q):
    s, a, b = rq(q), rq(alpha), rq(beta)
    x = s-1
    arcsine = iv.atan2(x, iv.sqrt(1-x*x))
    return -a*iv.sqrt(s*(2-s))+(a+b)*arcsine

def integral(a, ea, b, eb):
    slope = (eb-ea)/(b-a)
    intercept = ea-slope*a
    return primitive(slope,intercept,b)-primitive(slope,intercept,a)

def coefficient(points):
    result=iv.mpf(0)
    for (a,ea),(b,eb) in zip(points,points[1:]):
        result += integral(a,ea,b,eb)
        sa,sb=1-b,1-a
        result += integral(sa,Q(1,2)-sa+eb,sb,Q(1,2)-sb+ea)
    return result/(2*iv.pi*iv.ln(2))

points=vertices(30)
c30=coefficient(points)
sigma,k=points[-2]
tail=3*rq(k)*iv.sqrt(1-rq(sigma))/(2*iv.pi*iv.ln(2))
c_inf=iv.mpf([(c30-tail).a,c30.b])
height=2*iv.pi*c_inf
assert tail < iv.mpf('5e-15')
assert iv.mpf('0.096815114279049') < c_inf
assert c_inf < iv.mpf('0.096815114279054')
assert iv.mpf('0.608307303550') < height
assert height < iv.mpf('0.608307303552')
assert height < iv.mpf('0.6083074')
result={
    'mpmath_version':mp.__version__, 'interval_decimal_precision':iv.dps,
    'A_process_steps':30, 'vertices':'exact rational arithmetic',
    'C_30_interval':str(c30), 'tail_bound_interval':str(tail),
    'C_infinity_enclosure':str(c_inf),
    'two_pi_C_infinity_enclosure':str(height),
    'proved_displayed_upper_bound':'0.6083074',
    'cited_Bellotti_Wong_implied_height_coefficient':str(2*iv.pi*iv.mpf('0.10076')),
    'cited_Trudgian_implied_height_coefficient':str(2*iv.pi*iv.mpf('0.1013')),
    'scope':'certifies arithmetic for the stated analytic inputs, not the external analytic theorems',
}
out=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parents[1]/'outputs'
out.mkdir(parents=True,exist_ok=True)
(out/'envelope_intervals_v5.json').write_text(json.dumps(result,indent=2)+'\n')
(out/'envelope_intervals_v5.txt').write_text('\n'.join(f'{k}: {v}' for k,v in result.items())+'\n')
print(json.dumps(result,indent=2))
