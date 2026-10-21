"""Arithmetic checks independent of reference zeros."""
import construct as c
import numpy as np,json
from scipy.integrate import quad
from scipy.optimize import minimize,LinearConstraint
T=32;L=np.log(T)/(2*np.pi);M=int(np.ceil(2.5*T*L));h=2.5*T/M;t=T/2+h*np.arange(M+1);pp=c.primes(np.sqrt(T/2));d,_=c.load(t,h,pp)
def target(s):
    phase=sum(np.angle(1-p**(-.5)*np.exp(-1j*s*np.log(p))) for p in pp)
    return c.n0(s)-np.interp(s,t,c.n0(t))-phase/np.pi
err=[]
for i in [0,1,M//2,M]:
    val=0
    if i:val+=quad(lambda s:(s-t[i-1])/h*target(s),t[i-1],t[i],epsabs=1e-11)[0]/h
    if i<M:val+=quad(lambda s:(t[i+1]-s)/h*target(s),t[i],t[i+1],epsabs=1e-11)[0]/h
    err.append(abs(val-d[i]))
b=np.load(c.OUT/'block_32.npz');cp=c.OUT/'verification_solver'
# Reconstruct ADMM directly for comparison with independent SLSQP.
A=np.diag(np.r_[1/3,np.full(M-1,2/3),1/3])+np.diag(np.full(M,1/6),1)+np.diag(np.full(M,1/6),-1)
D=np.diff(np.eye(M+1),axis=0);lo=L*h/2-np.diff(c.n0(t));hi=2*L*h-np.diff(c.n0(t));y=np.zeros(M+1);z=np.clip(D@y,lo,hi);u=np.zeros(M)
for it in range(3000):
    y=np.linalg.solve(A+.5*D.T@D,d+.5*D.T@(z-u));dy=D@y;z=np.clip(dy+u,lo,hi);u+=dy-z
r=minimize(lambda v:.5*v@A@v-d@v,y,jac=lambda v:A@v-d,constraints=[LinearConstraint(D,lo,hi)],method='SLSQP',options={'ftol':1e-13,'maxiter':1000})
result=dict(max_load_error=max(err),slsqp_success=bool(r.success),max_solution_difference=float(np.max(abs(r.x-y))),reference_zeros_used=False)
assert max(err)<1e-10 and r.success and result['max_solution_difference']<1e-6
(c.OUT/'verification.json').write_text(json.dumps(result,indent=2));print(result)
