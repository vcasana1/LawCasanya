"""V5 exact extensions: prime-counting identity and linear kappa transform.

This script verifies the exact algebraic statements included in v5.  The follow-up
MS variance ratios and cross-coupling numbers in the manuscript were supplied
as external stage-9 measurements and are recorded separately in outputs/.
"""
import os, sys, numpy as np
D=os.path.join(os.path.dirname(__file__),'..','data')
M=np.load(D+'/M.npy'); Q=np.load(D+'/Q.npy'); E=np.load(D+'/E_mid.npy')
pr=np.load(D+'/pr.npy'); pstar=np.load(D+'/p_star.npy'); kap=np.load(D+'/kappa.npy')
g=np.load(D+'/gaps.npy')
sys.path.insert(0,os.path.dirname(__file__))
from weights_identity import weights

# Exact prime-counting integral identity, evaluated as its gap sum.
rng=np.random.default_rng(4)
ix=rng.choice(len(M),size=5000,replace=False)
err=[]
for z in ix:
    m=int(M[z]); h=abs(m)
    if h==0:
        rhs=0.0
    else:
        a=int((Q[z]-h)//2); b=a+h
        # integral_{p_a}^{p_b} (b-pi(t))dt = sum_{j=a}^{b-1}(b-j)g_j
        # gaps.npy convention: g[j-1]=p_{j+1}-p_j
        integ=0.0
        for j in range(a,b):
            integ += (b-j)*(pr[j+1]-pr[j])
        rhs=np.sign(m)*(integ-h*(pstar[z]-pr[a]))
    err.append(abs(rhs-E[z]))
print('=== Proposition: prime-counting integral form ===')
print('random n tested        :',len(ix))
print('max absolute error     : %.3e'%max(err))

# kappa(h) = c0^{-1} sum_d c_d rho(d)
LO,HI=50000,305000
seg=g[LO:HI].astype(float); var=seg.var(); cen=seg-seg.mean(); DMAX=420
rho=np.array([1.0]+[float(np.dot(cen[:-d],cen[d:])/((len(cen)-d)*var)) for d in range(1,DMAX+1)])
errs=[]
for h in range(3,len(kap)):
    idx,w=weights(h,100000)
    c0=float(w@w); val=c0
    # ordered pairs |i-j|=d
    diff=np.abs(idx[:,None]-idx[None,:]); ww=w[:,None]*w[None,:]
    for d in range(1,min(DMAX,int(diff.max()))+1):
        val += rho[d]*float(ww[diff==d].sum())
    errs.append(abs(kap[h]-val/c0))
print('\n=== kappa as a linear transform of rho ===')
print('h tested               : 3..%d'%(len(kap)-1))
print('max |direct-linear|    : %.3e'%max(errs))
print('rho(1..8)              :',' '.join('%+.4f'%x for x in rho[1:9]))
