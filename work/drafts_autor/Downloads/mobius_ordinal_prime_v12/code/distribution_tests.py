"""Stage 4: distributional tests on the standardised residual, plus the effective sample size."""
import numpy as np, os
from scipy import stats
D = os.path.join(os.path.dirname(__file__), '..', 'data')
M=np.load(D+'/M.npy'); Q=np.load(D+'/Q.npy'); pr=np.load(D+'/pr.npy')
E_mid=np.load(D+'/E_mid.npy'); sd_i=np.load(D+'/sd_indep.npy'); sd_c=np.load(D+'/sd_corr.npy')
N=len(M); n=np.arange(1,N+1); h=np.abs(M).astype(int)

print("=== A. the h^{3/2} log n normalisation ===")
Z32 = np.where(h>0, E_mid/np.maximum(h,1)**1.5/np.log(np.maximum(n,3)), 0.0)
sel = (h>=8)&(n>=10**3)
print(" |M| bucket        count    median |Z_3/2|")
for a,b in [(8,12),(12,19),(19,31),(31,51),(51,84),(84,138),(138,225),(225,400)]:
    s = sel&(h>=a)&(h<b)
    print("  [%4d,%4d)  %9d       %.4f" % (a,b,s.sum(),np.median(np.abs(Z32[s]))))
print("\n n band                       count   RMS Z_3/2   median|Z_3/2|")
ed=[1e5,1.58e5,2.51e5,3.98e5,6.31e5,1e6]
for a,b in zip(ed[:-1],ed[1:]):
    s=sel&(n>=a)&(n<b)
    print("  [%.2e, %.2e)  %9d     %.4f        %.4f" % (a,b,s.sum(),np.sqrt((Z32[s]**2).mean()),np.median(np.abs(Z32[s]))))

print("\n=== B. standardised residual Z = E_mid / sd_pred (covariance-corrected) ===")
def moments(x):
    return (x.mean(), x.std(), stats.skew(x), stats.kurtosis(x), np.median(np.abs(x)))
print(" n band                       count      mean       sd      skew    exkurt  median|Z|   KS vs N(0,1)   p")
for a,b in [(1e4,1e5),(1e5,3.16e5),(3.16e5,1e6)]:
    s=(n>=a)&(n<b)&(h>=12)
    Z=E_mid[s]/sd_c[s]
    ks=stats.kstest(Z,'norm')
    print("  [%.2e, %.2e)  %9d  %+.4f  %.4f  %+.4f  %+.4f    %.4f     %.4f   %.1e"
          % (a,b,s.sum(),*moments(Z)[:4],moments(Z)[4],ks.statistic,ks.pvalue))
print("\n |M| bucket        count      mean       sd      skew    exkurt  median|Z|")
for a,b in [(12,19),(19,31),(31,51),(51,84),(84,138),(138,225),(225,400)]:
    s=(n>=10**4)&(h>=a)&(h<b)
    Z=E_mid[s]/sd_c[s]
    print("  [%4d,%4d)  %9d  %+.4f  %.4f  %+.4f  %+.4f    %.4f" % (a,b,s.sum(),*moments(Z)))

s=(n>=10**4)&(h>=12); Z=E_mid[s]/sd_c[s]
print("\nquantiles of Z (all n >= 10^4, |M| >= 12, %d points):" % s.sum())
qs=[1,5,25,50,75,95,99]
print("   level   ", "  ".join("%6d%%" % q for q in qs))
print("   observed", "  ".join("%+7.3f" % v for v in np.percentile(Z,qs)))
print("   N(0,1)  ", "  ".join("%+7.3f" % v for v in stats.norm.ppf(np.array(qs)/100)))

print("\n=== C. effective sample size (the points are NOT independent) ===")
Zf=E_mid[s]/sd_c[s]; idx=np.where(s)[0]
Zc=Zf-Zf.mean(); v=Zc.var()
ac=[float(np.dot(Zc[:-d],Zc[d:])/((len(Zc)-d)*v)) for d in [1,10,100,1000,3000,10000,30000]]
print("autocorrelation of Z in n at lag  1,10,100,1000,3000,10000,30000:")
print("   " + "  ".join("%+.4f" % a for a in ac))
d=1; tau=1.0
while d < 200000:
    r=float(np.dot(Zc[:-d],Zc[d:])/((len(Zc)-d)*v))
    if r<=0.05: break
    d*=2
print("first lag with autocorrelation <= 0.05 : %d" % d)
print("integrated autocorrelation time (lags <= 20000, Geyer cut) : ", end="")
tot=1.0
for dd in range(1,20001):
    r=float(np.dot(Zc[:-dd],Zc[dd:])/((len(Zc)-dd)*v))
    if r<=0: break
    tot+=2*r
print("%.0f" % tot)
print("=> effective sample size ~ %d / %.0f ~ %d" % (len(Zf),tot,int(len(Zf)/tot)))
