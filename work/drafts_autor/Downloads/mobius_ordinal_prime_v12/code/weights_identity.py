"""Stage 2: exact antisymmetric gap representation of E_mid and the weight-norm formula."""
import numpy as np, os
D = os.path.join(os.path.dirname(__file__), '..', 'data')
M=np.load(D+'/M.npy'); Q=np.load(D+'/Q.npy'); pr=np.load(D+'/pr.npy'); E_mid=np.load(D+'/E_mid.npy')
N=len(M); n=np.arange(1,N+1)

def weights(h, m):
    """Return (indices, weights) of the gaps g_i = p_{i+1}-p_i in the exact expansion
       E_mid = sgn(M) * sum_i w_i g_i ,  m = floor((Q+1)/2)."""
    if h == 0: return np.array([],int), np.array([],float)
    if h % 2 == 0:
        k = np.arange(1, h//2)
        idx = np.concatenate([m+k, m-k]); w = np.concatenate([h/2-k, -(h/2-k)])
    else:
        k1 = np.arange(0, (h-1)//2); k2 = np.arange(1, (h+1)//2)
        idx = np.concatenate([m+k1, m-k2])
        w   = np.concatenate([(h-1)/2-k1, -((h+1)/2-k2)])
    return idx, w

def w2_closed(h):
    return h*(h*h-1)/12.0 if h % 2 == 1 else h*(h-1)*(h-2)/12.0

g = np.diff(pr[1:].astype(float))          # g[i-1] = p_{i+1} - p_i
print("=== exact antisymmetric gap identity ===")
rng = np.random.default_rng(0)
sample = rng.choice(np.arange(1000, N), size=4000, replace=False)
bad = 0; maxerr = 0.0
for i in sample:
    h = int(abs(M[i])); m = int((Q[i]+1)//2)
    idx, w = weights(h, m)
    val = np.sign(M[i]) * float(np.dot(w, g[idx-1]))
    err = abs(val - E_mid[i]); maxerr = max(maxerr, err)
    if err > 1e-6: bad += 1
print("random n tested            : %d" % len(sample))
print("mismatches                 : %d" % bad)
print("max absolute error         : %.3e" % maxerr)

print("\n=== weight-norm formula  sum w^2 ===")
ok = True
for h in list(range(1, 60)) + [100, 101, 300, 301, 370]:
    _, w = weights(h, 10**5)
    if abs((w**2).sum() - w2_closed(h)) > 1e-9: ok = False; print("FAIL h =", h)
print("sum w^2 = h(h^2-1)/12  (h odd),  h(h-1)(h-2)/12  (h even) :", ok)
print("check   : h=7 -> %.1f (closed %.1f) ; h=8 -> %.1f (closed %.1f)"
      % ((weights(7,10**5)[1]**2).sum(), w2_closed(7),
         (weights(8,10**5)[1]**2).sum(), w2_closed(8)))
print("asymptotics: sum w^2 / (h^3/12) at h=370 : %.6f" % (w2_closed(370)/(370**3/12)))
np.save(D+'/gaps.npy', g)
