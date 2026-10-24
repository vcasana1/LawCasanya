# Reproducible spectral experiment for the v6 surface operator.
# Requires numpy and scipy only.  No zeta-zero data enter this script.

import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigsh
from scipy.optimize import linear_sum_assignment


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


def build_surface_dirac(N):
    """Build D_N=(A_N-A_N^*)/(2i), A_N=K_N B_N^{-1}."""
    mu = mobius_sieve(N)

    kr, kc, kv = [], [], []
    for q in range(1, N + 1):
        mq = int(mu[q])
        amax = N // q
        if mq == 0 or amax < 2:
            continue
        a = np.arange(2, amax + 1, dtype=np.int32)
        n = q * a
        kr.extend((n - 2).tolist())
        kc.extend((a - 2).tolist())
        kv.extend([mq] * len(a))
    K = coo_matrix(
        (np.asarray(kv, dtype=float), (kr, kc)),
        shape=(N - 1, N - 1),
    ).tocsr()

    br, bc, bv = [], [], []
    for m in range(2, N + 1):
        v = np.arange(m, N + 1, m, dtype=np.int32)
        br.extend((v - 2).tolist())
        bc.extend([m - 2] * len(v))
        bv.extend([1.0] * len(v))

        v = np.arange(m, N, m, dtype=np.int32)
        br.extend((v - 1).tolist())
        bc.extend([m - 2] * len(v))
        bv.extend([-1.0] * len(v))

    Binv = coo_matrix(
        (np.asarray(bv, dtype=float), (br, bc)),
        shape=(N - 1, N - 1),
    ).tocsr()

    A = K @ Binv
    S = 0.5 * (A - A.T)
    return (-1j) * S.astype(np.complex128)


def edge_spectrum(N, k=25):
    D = build_surface_dirac(N)
    vals, vecs = eigsh(
        D, k=k, which="LA", ncv=max(4 * k + 20, 120),
        tol=1e-10, maxiter=20000,
    )
    order = np.argsort(vals)[::-1]
    vals = vals[order]
    vecs = vecs[:, order]
    residual = np.linalg.norm(D @ vecs - vecs * vals, axis=0)
    if residual.max() > 1e-8:
        raise RuntimeError("ARPACK residual too large")
    return vals, vecs, residual


def match_branches(vecs_N, vecs_2N):
    """Maximum-weight overlap matching under zero-extension N -> 2N."""
    old_block = vecs_2N[:vecs_N.shape[0], :]
    overlap = np.abs(vecs_N.conj().T @ old_block) ** 2
    mass = np.sum(np.abs(old_block) ** 2, axis=0)
    alignment = overlap / mass[None, :]
    rows, cols = linear_sum_assignment(-overlap)
    mapping = np.full(vecs_N.shape[1], -1, dtype=int)
    mapping[rows] = cols
    return mapping, overlap, alignment


def main():
    Ns = [8192, 16384, 32768, 65536, 131072]
    k = 25
    spectra = {}

    # No zeta zeros are used in this loop.
    for N in Ns:
        vals, vecs, residual = edge_spectrum(N, k=k)
        spectra[N] = (vals, vecs)
        print(
            N,
            vals[0],
            vals[0] / np.sqrt(N * np.log(N)),
            residual.max(),
        )

    # Track identities from the N=8192 branches.
    branch_index = {Ns[0]: np.arange(k)}
    for N, M in zip(Ns[:-1], Ns[1:]):
        valsN, vecsN = spectra[N]
        valsM, vecsM = spectra[M]
        mapping, overlap, alignment = match_branches(vecsN, vecsM)
        branch_index[M] = np.array([
            mapping[i] for i in branch_index[N]
        ])
        print("match", N, M)
        for b in range(10):
            i = branch_index[N][b]
            j = mapping[i]
            print(
                b + 1, i + 1, j + 1,
                overlap[i, j], alignment[i, j]
            )


if __name__ == "__main__":
    main()
