"""Stage 7: the relative size of the residual,  |E_mid| / |T|  ~ c sqrt(|M|)/n."""
import numpy as np, os
D=os.path.join(os.path.dirname(__file__),'..','data')
M=np.load(D+'/M.npy');T=np.load(D+'/T.npy');E_mid=np.load(D+'/E_mid.npy');Q=np.load(D+'/Q.npy');pr=np.load(D+'/pr.npy')
N=len(M);n=np.arange(1,N+1);h=np.abs(M).astype(int)
s=(h>=8)&(n>=10**3)
r=np.abs(E_mid[s])/np.abs(T[s])
print("median |E_mid|/|T| over n>=10^3, |M|>=8 : %.4e" % np.median(r))
print("median |E_mid|/|T| over all n>=100     : %.4e"
      % np.median((np.abs(E_mid)/np.abs(np.where(T==0,1,T)))[(n>=100)&(T!=0)]))
print("\npredicted law  |E_mid|/|T| ~ c sqrt(|M|)/n  with c = 0.155*pi^2/3 = %.4f" % (0.155*np.pi**2/3))
print(" n band                      median of (|E_mid|/|T|) * n / sqrt(|M|)")
for a,b in [(1e3,1e4),(1e4,1e5),(1e5,3.16e5),(3.16e5,1e6)]:
    ss=s&(n>=a)&(n<b)
    print("  [%.2e, %.2e)      %.4f" % (a,b,np.median(np.abs(E_mid[ss])/np.abs(T[ss])*n[ss]/np.sqrt(h[ss]))))
