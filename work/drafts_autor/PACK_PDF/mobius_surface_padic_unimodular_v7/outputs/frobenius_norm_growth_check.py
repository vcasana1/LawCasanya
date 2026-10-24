"""
Non-circular candidate mechanism for the sqrt(N log N) scale:
D_N is built from K_N (Mobius/divisor incidence) and B_N^{-1} (congruence
differences). Row n of K_N has ~ d(n) nonzero entries (divisors of n),
so on average O(log N) nonzero entries per row (Dirichlet: sum d(n) ~ N log N).
If A_N=K_N B_N^{-1} inherits a similar O(log N)-nonzero-per-row sparsity
pattern with O(1)-bounded entries, then trivially
    ||D_N||_F^2  ~  (# nonzero entries) * O(1)  ~  N log N,
giving ||D_N||_F ~ sqrt(N log N) for FREE, with NO reference to zeta at all
-- pure divisor-counting (Dirichlet hyperbola). This only bounds
||D_N||_op <= ||D_N||_F from ABOVE at the right order; it does not by
itself explain why lambda_max actually SATURATES this bound (that is
the genuine open step, HP1).

Test: does ||D_N||_F^2 / (N log N) stabilize, matching this divisor-counting
heuristic exactly?
"""
import numpy as np
from scipy.sparse import coo_matrix

def mobius_sieve(N):
    lp = np.zeros(N + 1, dtype=np.int32)
    mu = np.zeros(N + 1, dtype=np.int8)
    mu[1] = 1
    primes = []
    for n in range(2, N + 1):
        if lp[n] == 0:
            lp[n] = n
            primes.append(n)
            mu[n] = -1
        for p in primes:
            m = p * n
            if p > lp[n] or m > N:
                break
            lp[m] = p
            mu[m] = 0 if p == lp[n] else -mu[n]
    return mu

def build_A(N):
    mu = mobius_sieve(N)
    kr, kc, kv = [], [], []
    for q in range(1, N + 1):
        mq = int(mu[q])
        amax = N // q
        if mq == 0 or amax < 2:
            continue
        a = np.arange(2, amax + 1, dtype=np.int32)
        n = q * a
        kr.extend((n - 2).tolist()); kc.extend((a - 2).tolist()); kv.extend([mq] * len(a))
    K = coo_matrix((np.asarray(kv, dtype=float), (kr, kc)), shape=(N - 1, N - 1)).tocsr()

    br, bc, bv = [], [], []
    for m in range(2, N + 1):
        v = np.arange(m, N + 1, m, dtype=np.int32)
        br.extend((v - 2).tolist()); bc.extend([m - 2] * len(v)); bv.extend([1.0] * len(v))
        v = np.arange(m, N, m, dtype=np.int32)
        br.extend((v - 1).tolist()); bc.extend([m - 2] * len(v)); bv.extend([-1.0] * len(v))
    Binv = coo_matrix((np.asarray(bv, dtype=float), (br, bc)), shape=(N - 1, N - 1)).tocsr()

    A = K @ Binv
    return A

for N in [8192, 16384, 32768, 65536, 131072]:
    A = build_A(N)
    Dmat = 0.5 * (A - A.T)   # this is i*D_N in our earlier convention; ||.||_F same as D_N's since D_N=-i*Dmat
    fro2 = (Dmat.multiply(Dmat)).sum()   # sum of squares (real matrix)
    nnz = Dmat.nnz
    print(f"N={N:7d}  ||D_N||_F^2={fro2:14.1f}  N*logN={N*np.log(N):14.1f}  "
          f"ratio={fro2/(N*np.log(N)):.5f}  nnz={nnz:9d}  nnz/N={nnz/N:.3f}")
