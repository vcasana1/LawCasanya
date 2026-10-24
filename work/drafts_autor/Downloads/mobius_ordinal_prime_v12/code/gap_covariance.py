"""Stage 3: replace the independent-gap model by the measured local gap covariance.
   Var(E_mid | h) = w^T Sigma_g w  with the antisymmetric signs inside w."""
import numpy as np, os
D = os.path.join(os.path.dirname(__file__), '..', 'data')
M=np.load(D+'/M.npy'); Q=np.load(D+'/Q.npy'); pr=np.load(D+'/pr.npy')
E_mid=np.load(D+'/E_mid.npy'); g=np.load(D+'/gaps.npy')
N=len(M); n=np.arange(1,N+1)
from weights_identity import weights, w2_closed

LO, HI = 50_000, 305_000                      # prime-index band covering n in [1e5,1e6]
seg = g[LO:HI]
mu_g = seg.mean(); var_g = seg.var()
print("=== local gap statistics, prime index band [%d, %d) ===" % (LO,HI))
print("mean gap                 = %.4f" % mu_g)
print("log p at band centre     = %.4f" % np.log(pr[(LO+HI)//2]))
print("Var(g)                   = %.4f" % var_g)
print("Var(g) / log^2 p         = %.4f   (Cramer/Poisson model predicts 1)" % (var_g/np.log(pr[(LO+HI)//2])**2))

DMAX = 420
c = seg - mu_g
rho = np.array([1.0] + [float(np.dot(c[:-d], c[d:])/((len(c)-d)*var_g)) for d in range(1, DMAX+1)])
print("\ngap autocorrelation rho(d), d = 1..10:")
print("  " + "  ".join("%.4f" % r for r in rho[1:11]))
print("sum_{d>=1} rho(d) over d<=420 = %.4f" % rho[1:].sum())

# kappa(h) = w^T R w / w^T w  ; R_{ab} = rho(|i_a - i_b|)
HMAX = int(np.abs(M).max())
print("\nmax |M(n)| for n <= 10^6 =", HMAX)
kappa = np.ones(HMAX+1)
for h in range(1, HMAX+1):
    idx, w = weights(h, 10**5)
    if len(w) == 0: kappa[h] = 1.0; continue
    d = np.abs(idx[:,None]-idx[None,:])
    d[d > DMAX] = DMAX
    kappa[h] = float(w @ rho[d] @ w) / float(w @ w)
print("kappa(h) = w^T R w / w^T w  (1 under independence):")
for h in [3,5,10,20,40,80,160,320,HMAX]:
    print("   h = %4d   kappa = %.4f   sqrt(kappa) = %.4f" % (h, kappa[h], np.sqrt(max(kappa[h],0))))

# local gap sd at the window centre, from a running window of 2001 gaps
W = 2001
csum = np.concatenate([[0.], np.cumsum(g)]); csq = np.concatenate([[0.], np.cumsum(g**2)])
def local_sd(i):
    a = np.clip(i-W//2, 0, len(g)-W); b = a+W
    m1 = (csum[b]-csum[a])/W; m2 = (csq[b]-csq[a])/W
    return np.sqrt(np.maximum(m2-m1**2, 0))
ctr = (Q//2).astype(int)
sd_g = local_sd(ctr)
h_arr = np.abs(M).astype(int)
sum_w2 = np.where(h_arr % 2 == 1, h_arr*(h_arr**2-1)/12.0, h_arr*(h_arr-1)*(h_arr-2)/12.0)
sd_indep = sd_g*np.sqrt(sum_w2)                       # independent-gap prediction
sd_corr  = sd_g*np.sqrt(sum_w2*np.clip(kappa[np.clip(h_arr,0,HMAX)],0,None))  # covariance-corrected
np.save(D+'/sd_indep.npy', sd_indep); np.save(D+'/sd_corr.npy', sd_corr); np.save(D+'/kappa.npy', kappa)

sel = (n >= 10**4) & (h_arr >= 12)
print("\n=== test on %d values of n (n >= 10^4, |M| >= 12) ===" % sel.sum())
for name, sd in [("independent-gap model", sd_indep), ("covariance-corrected  ", sd_corr)]:
    Z = E_mid[sel]/sd[sel]
    print("%s : RMS(E_mid)/RMS(sd_pred) = %.4f   RMS Z = %.5f   mean Z = %+.3e   median|Z| = %.5f   corr(|E_mid|,sd) = %.4f"
          % (name, np.sqrt((E_mid[sel]**2).mean())/np.sqrt((sd[sel]**2).mean()),
             np.sqrt((Z**2).mean()), Z.mean(), np.median(np.abs(Z)),
             np.corrcoef(np.abs(E_mid[sel]), sd[sel])[0,1]))
