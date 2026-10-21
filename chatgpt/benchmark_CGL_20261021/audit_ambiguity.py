#!/usr/bin/env python3
"""Reproduce the two local k=1 LeClair roots without any true ordinate."""
import json
from pathlib import Path
import numpy as np
import mpmath as mp
from scipy.optimize import brentq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import constructors as C

HERE=Path(__file__).resolve().parent;OUT=HERE/'results_v2'
C.install_guard();mp.mp.dps=60
pr=C.sieve(8191);P=C.Phase(pr,8191,'euler')
inp=np.load(OUT/'pilot_inputs.npz');vals=np.load(OUT/'pilot_candidates.npz')
tau=float(inp['tau'][0]);x=np.linspace(2*np.pi+1e-6,tau+2/C.L(tau),10001)
def fun(t):return C.N0(t)+1/(48*np.pi*t)+P(t,derivative=False)[0]-.5
y=fun(x);js=np.flatnonzero(y[:-1]*y[1:]<0)
roots=[]
for j in js:
    rr=brentq(lambda t:float(fun(np.array([t]))[0]),x[j],x[j+1],xtol=1e-12)
    t=mp.mpf(rr)
    def hp(u):
        s=-mp.im(mp.fsum(mp.log(1-mp.power(int(p),-mp.mpf('.500001')-1j*u)) for p in pr))/mp.pi
        return u/(2*mp.pi)*(mp.log(u/(2*mp.pi))-1)+mp.mpf('.875')+1/(48*mp.pi*u)+s-mp.mpf('.5')
    root_hp=mp.findroot(hp,(mp.mpf(rr)-mp.mpf('1e-4'),mp.mpf(rr)+mp.mpf('1e-4')))
    roots.append(dict(root_float=rr,root_hp=mp.nstr(root_hp,55),residual_hp_at_float=float(abs(hp(t))),
                      slope_hp=float(mp.diff(hp,root_hp))))
chosen=float(vals['M1_LeClair_P8191'][0])
out=dict(k=1,cutoff=8191,prime_count=len(pr),delta=1e-6,search_interval=[float(x[0]),float(x[-1])],
         root_count=len(roots),roots=roots,prime_continuation_selected=chosen,
         conclusion='The published finite phase equation has two solutions for this label in the tested interval. Continuation picks one; the label is not a global ordinal enumeration.',
         no_true_zero_or_zeta_access=True)
(OUT/'ambiguity_k1.json').write_text(json.dumps(out,indent=2))
fig,ax=plt.subplots(figsize=(8,4));ax.plot(x,y,label='LeClair eq49, k=1, 1028 primes');ax.axhline(0,color='k',lw=.7)
for r in roots:ax.plot(r['root_float'],0,'ro');ax.annotate(f"{r['root_float']:.6f}",(r['root_float'],0),xytext=(0,16),textcoords='offset points',ha='center')
ax.axvline(chosen,ls='--',color='green',label='root selected by prime continuation')
ax.set_xlabel('t');ax.set_ylabel('phase equation residual');ax.legend(fontsize=8);ax.grid(alpha=.3)
fig.tight_layout();fig.savefig(OUT/'phase_ambiguity_k1.png',dpi=160)
print(json.dumps(out,indent=2))
