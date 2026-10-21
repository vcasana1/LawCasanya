#!/usr/bin/env python3
"""Arithmetic identity checks only. No zero file, fit, or predictive experiment."""
import json,hashlib,sys
from pathlib import Path
import mpmath as mp
HERE=Path(__file__).resolve().parent
def guard(event,args):
    if event=='open' and args and isinstance(args[0],(str,bytes)) and 'zeross' in str(args[0]).lower():
        raise PermissionError('True-zero data forbidden')
sys.addaudithook(guard)
mp.mp.dps=70
pr=[mp.mpf(p) for p in [2,3,5,7,11,13]]
def phase(t):
    return -mp.fsum(mp.atan2(mp.sin(t*mp.log(p))/mp.sqrt(p),1-mp.cos(t*mp.log(p))/mp.sqrt(p)) for p in pr)/mp.pi
def V(t):
    return mp.fsum(mp.im(mp.polylog(3,mp.exp(1j*t*mp.log(p))/mp.sqrt(p)))/mp.log(p)**2 for p in pr)/mp.pi
def N0(t):return t/(2*mp.pi)*(mp.log(t/(2*mp.pi))-1)+mp.mpf(7)/8
def A0(t):return t*t/(4*mp.pi)*mp.log(t/(2*mp.pi))-3*t*t/(8*mp.pi)+7*t/8
def A1(t):return t**3/(6*mp.pi)*mp.log(t/(2*mp.pi))-2*t**3/(9*mp.pi)+7*t*t/16
t=mp.mpf(30);h=mp.mpf('.3');left=t-h;right=t+h
direct=mp.quad(lambda u:(u-left)/h*phase(u),[left,t])+mp.quad(lambda u:(right-u)/h*phase(u),[t,right])
closed=(V(left)-2*V(t)+V(right))/h
leftload=mp.quad(lambda u:(t+h-u)/h*phase(u),[t,t+h])
leftclosed=-mp.diff(V,t)+(V(t+h)-V(t))/h
rightload=mp.quad(lambda u:(u-(t-h))/h*phase(u),[t-h,t])
rightclosed=mp.diff(V,t)-(V(t)-V(t-h))/h
smooth=mp.quad(lambda u:(u-left)/h*N0(u),[left,t])+mp.quad(lambda u:(right-u)/h*N0(u),[t,right])
smoothclosed=((A1(t)-left*A0(t))-(A1(left)-left*A0(left))+(right*A0(right)-A1(right))-(right*A0(t)-A1(t)))/h
errors=dict(V_second_derivative=abs(mp.diff(V,t,2)-phase(t)),
    interior_hat_load=abs(direct-closed),left_endpoint_hat_load=abs(leftload-leftclosed),
    right_endpoint_hat_load=abs(rightload-rightclosed),smooth_hat_load=abs(smooth-smoothclosed),
    smooth_primitive=abs(mp.diff(A0,t)-N0(t)),weighted_smooth_primitive=abs(mp.diff(A1,t)-t*N0(t)))
assert all(e<mp.mpf('1e-55') for e in errors.values())
source=Path('/Users/vcasana/Downloads/prime_corrected_clock_v14.tex')
manifest=dict(source_path=str(source),source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
    source_bytes=source.stat().st_size,precision_decimal_digits=mp.mp.dps,
    verification_scope='independent high-precision evaluations of analytic identities, not a benchmark or a proof audit of the whole v14',
    true_zero_data_accessed=False,fitted_parameters=False,
    errors={k:mp.nstr(v,12) for k,v in errors.items()},all_identity_checks_passed=True)
(HERE/'verification.json').write_text(json.dumps(manifest,indent=2));print(json.dumps(manifest,indent=2))
