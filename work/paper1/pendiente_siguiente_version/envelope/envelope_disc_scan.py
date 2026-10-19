import sys, os; sys.argv=["x","3000"]; os.chdir(os.path.dirname(os.path.abspath(__file__)))
exec(open('envelope_best_profile.py').read().split("out = {}")[0])
import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize
def mk(v):
    xs=np.array([float(a) for a,b in v]); ys=np.array([float(b) for a,b in v])
    def mu(s): return float(np.interp(s,xs,ys))
    def e(s):
        if s>=1: return 0.0
        if s>=0.5: return mu(s)
        if s>=0: return 0.5-s+mu(1-s)
        return 0.5-s
    return e
def a(e,s0,r):
    if not (1<=s0<=r): return 9
    br=sorted(set([0,np.pi]+[np.arccos(min(1,max(-1,(x-s0)/r))) for x in (0,0.5,1)]))
    I=sum(quad(lambda t:e(s0+r*np.cos(t)),br[i],br[i+1],limit=200)[0] for i in range(len(br)-1))
    return I/(2*np.pi*np.log(r/(s0-0.5)))
for name in ['v7: Bourgain + A-process, J=30','TY23 hull + TTY25 new pairs','Lindelof hypothesis (e = 0 on [1/2,1]), ceiling of the method']:
    e=mk(cases[name])
    print(name)
    for r in [1,1.05,1.1,1.2,1.3,1.5,2,3]:
        print('  s0=1 rho=%.2f  2pi*a=%.6f'%(r,2*np.pi*a(e,1,r)))
    res=minimize(lambda p:a(e,p[0],p[1]),[1.0001,1.2],method='Nelder-Mead',options={'xatol':1e-7,'fatol':1e-10})
    print('  opt',res.x,2*np.pi*res.fun)
