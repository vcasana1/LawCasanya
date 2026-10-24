"""Stage 5: KS test on a thinned, effectively independent subsample."""
import numpy as np, os
from scipy import stats
D=os.path.join(os.path.dirname(__file__),'..','data')
M=np.load(D+'/M.npy'); E_mid=np.load(D+'/E_mid.npy'); sd_c=np.load(D+'/sd_corr.npy')
N=len(M); n=np.arange(1,N+1); h=np.abs(M).astype(int)
s=(n>=10**4)&(h>=12); Z=E_mid[s]/sd_c[s]
print("full sample: %d points, integrated autocorrelation time ~51" % len(Z))
print("\nthin   count      mean       sd      skew    exkurt    KS      p-value")
for step in [1,51,128,256,512]:
    Zt=Z[::step]
    ks=stats.kstest(Zt,'norm')
    print("%4d %8d   %+.4f  %.4f  %+.4f  %+.4f  %.5f  %.3e"
          % (step,len(Zt),Zt.mean(),Zt.std(),stats.skew(Zt),stats.kurtosis(Zt),ks.statistic,ks.pvalue))
print("\nexcess kurtosis of Z by |M| (n >= 10^4) - test of the CLT approach:")
for a,b in [(12,19),(19,31),(31,51),(51,84),(84,138),(138,225),(225,400)]:
    ss=(n>=10**4)&(h>=a)&(h<b); Zb=E_mid[ss]/sd_c[ss]
    print("   |M| in [%4d,%4d):  excess kurtosis = %+.4f   (thinned: %+.4f)"
          % (a,b,stats.kurtosis(Zb),stats.kurtosis(Zb[::51])))
