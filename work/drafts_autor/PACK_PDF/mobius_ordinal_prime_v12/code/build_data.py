"""Stage 1: sieve mu, build M, Q, prime table, T, E, E_mid.  Saves .npy to ../data/"""
import numpy as np, os, time
from sympy import primerange, prime
N = 10**6
OUT = os.path.join(os.path.dirname(__file__), '..', 'data')
os.makedirs(OUT, exist_ok=True)

def mobius_sieve(n):
    mu = np.ones(n+1, dtype=np.int8); is_c = np.zeros(n+1, dtype=bool); primes = []
    mu[0] = 0
    for i in range(2, n+1):
        if not is_c[i]:
            primes.append(i); mu[i] = -1
        for p in primes:
            if i*p > n: break
            is_c[i*p] = True
            if i % p == 0:
                mu[i*p] = 0; break
            mu[i*p] = -mu[i]
    return mu

t0 = time.time()
mu = mobius_sieve(N); mu[1] = 1
M = np.cumsum(mu[1:N+1].astype(np.int64))
Q = np.cumsum((mu[1:N+1]**2).astype(np.int64))
print("N = %d   M(N) = %d   Q(N) = %d" % (N, M[-1], Q[-1]))
need_transform = int((Q[-1] + abs(M[-1]))//2) + 4
# Keep the prime-prefix table long enough not only for the transform itself,
# but also for the Version 9 recovery audit, whose formal inversion domain can
# reach index Q(N).
need = max(need_transform, int(Q[-1]) + 4)
prime_upper = int(prime(need + 8)) + 1
pl = np.array(list(primerange(2, prime_upper)), dtype=np.int64)
assert len(pl) > need
pr = np.zeros(len(pl)+1, dtype=np.int64); pr[1:] = pl          # pr[m] = p_m
P  = np.zeros(len(pl)+1, dtype=np.int64); P[1:]  = np.cumsum(pl)  # P[m] = sum_{j<=m} p_j
print("max ordinal-prime index required = %d   (p = %d)" % ((Q[-1]+M[-1])//2, pr[(Q[-1]+M[-1])//2]))

Np = (Q + M)//2; Nm = (Q - M)//2
assert ((Q - M) % 2 == 0).all(), "parity lemma violated"
T = P[Np] - P[Nm]
SS = T + np.arange(1, N+1) - Q

# centre of the window is the half-integer (Q+1)/2 ; p_star = linear interpolation there
c_lo = (Q+1)//2; c_hi = (Q+2)//2
p_star = 0.5*(pr[c_lo].astype(float) + pr[c_hi].astype(float))
E     = T - M*pr[Q//2]
E_mid = T - M*p_star

for name, arr in [('mu',mu[1:N+1]),('M',M),('Q',Q),('Np',Np),('Nm',Nm),('T',T),('SS',SS),('E',E),('E_mid',E_mid),
                  ('pr',pr),('P',P),('p_star',p_star)]:
    np.save(os.path.join(OUT, name + '.npy'), arr)
print("elapsed %.1f s" % (time.time()-t0))

# --- direct check of the closed form against brute-force summation of S ---
S = np.zeros(N, dtype=np.int64)
m1 = mu[1:N+1]
S[m1 == -1] = -pr[Nm[m1 == -1]]
S[m1 ==  1] =  pr[Np[m1 ==  1]]
S[m1 ==  0] = 1
np.save(os.path.join(OUT, 'S.npy'), S)
print("closed form SS == cumsum(S) everywhere :", np.array_equal(np.cumsum(S), SS))
print("sgn T == sgn M everywhere              :", np.array_equal(np.sign(T), np.sign(M)))
print("T == 0  iff  M == 0                    :", np.array_equal(T == 0, M == 0))
lo = np.where(M != 0, np.abs(M)*pr[(Q-np.abs(M))//2 + 1], 0)
hi = np.where(M != 0, np.abs(M)*pr[(Q+np.abs(M))//2], 0)
print("block bounds hold everywhere           :", bool(np.all(lo <= np.abs(T)) and np.all(np.abs(T) <= hi)))
print("#{n <= 10^6 : M(n) = 0}                =", int((M == 0).sum()))
