"""Common definitions for the three pre-version computations (clock, prime phases, statistics).

Conventions follow ordinal_prime_cutoff and zCasanya_build.py:
  N0(t) = t/(2pi) (log(t/2pi) - 1) + 7/8,  L(t) = log(t/2pi)/(2pi),
  S_X(t) = -(1/pi) sum_{p^m <= X} sin(m t log p) / (m p^{m/2})   (power_sharp window).
The true ordinates are used only for evaluation, never for construction.
"""
import numpy as np

TWO_PI = 2 * np.pi
N_REC = 2001052


def load(name):
    a = np.fromfile(name, dtype='<f8')
    assert a.size == N_REC and np.all(np.isfinite(a))
    return a


def L(t):
    return np.log(t / TWO_PI) / TWO_PI


def N0(t):
    return t / TWO_PI * (np.log(t / TWO_PI) - 1) + 0.875


def clock_diff(t, tau):
    """N0(t) - N0(tau) without cancellation (Taylor remainder for |u| < 0.01)."""
    d = t - tau
    u = d / tau
    h = np.empty_like(u)
    small = np.abs(u) < .01
    v = u[small]
    poly = np.full_like(v, 1 / (14 * 13))
    for n in range(13, 1, -1):
        poly = (-1.) ** n / (n * (n - 1)) + v * poly
    h[small] = v * v * poly
    v = u[~small]
    h[~small] = (1 + v) * np.log1p(v) - v
    return L(tau) * d + tau / TWO_PI * h


def primes_upto(n):
    s = np.ones(n + 1, bool)
    s[:2] = False
    for i in range(2, int(n ** .5) + 1):
        if s[i]:
            s[i * i::i] = False
    return np.flatnonzero(s)


def prime_powers(nmax):
    """Arrays (n, p, m) of prime powers n = p^m <= nmax, sorted by n."""
    out = []
    for p in primes_upto(nmax):
        q, m = int(p), 1
        while q <= nmax:
            out.append((q, int(p), m))
            q *= int(p)
            m += 1
    out.sort()
    a = np.array(out, dtype=np.int64)
    return a[:, 0], a[:, 1], a[:, 2]


PP_N, PP_P, PP_M = prime_powers(7000000)
PP_LOGP = np.log(PP_P.astype(float))
PP_FREQ = PP_M * PP_LOGP                       # m log p = log n
PP_COEF = 1.0 / (np.pi * PP_M * np.sqrt(PP_N.astype(float)))   # a_q
PP_DCOEF = PP_LOGP / (np.pi * np.sqrt(PP_N.astype(float)))      # derivative weight
PP_LAMBDA_SQRT = PP_LOGP / np.sqrt(PP_N.astype(float))          # Lambda(n)/sqrt(n)
PP_B = np.cumsum(PP_LAMBDA_SQRT)                                 # B(n) = sum_{n'<=n} Lambda/sqrt
PP_W = 1.0 / (PP_M.astype(float) ** 2 * PP_N.astype(float))     # w_n = Lambda^2/(n log^2 n)


def S_and_dS(t, X, need_d=True, block=65536):
    """S_X(t) and S_X'(t) with a per-point cutoff X (array or scalar)."""
    t = np.asarray(t, float)
    X = np.broadcast_to(np.asarray(X, float), t.shape)
    nt = int(np.searchsorted(PP_N, X.max(), side='right'))
    S = np.zeros_like(t)
    dS = np.zeros_like(t) if need_d else None
    for lo in range(0, t.size, block):
        hi = min(t.size, lo + block)
        tt, xx = t[lo:hi], X[lo:hi]
        s = np.zeros_like(tt)
        ds = np.zeros_like(tt) if need_d else None
        for j in range(nt):
            mask = xx >= PP_N[j]
            if not mask.any():
                continue
            ang = PP_FREQ[j] * tt
            if mask.all():
                s -= PP_COEF[j] * np.sin(ang)
                if need_d:
                    ds -= PP_DCOEF[j] * np.cos(ang)
            else:
                s -= np.where(mask, PP_COEF[j] * np.sin(ang), 0.0)
                if need_d:
                    ds -= np.where(mask, PP_DCOEF[j] * np.cos(ang), 0.0)
        S[lo:hi] = s
        if need_d:
            dS[lo:hi] = ds
    return S, dS


def dyadic_cut(tau, xmax):
    h = np.exp2(np.floor(np.log2(tau)))
    return np.minimum(xmax, np.maximum(8, np.floor(np.sqrt(h))))


def acorr(r, lags=(1, 2, 3)):
    r = r - r.mean()
    v = np.mean(r * r)
    return [float(np.mean(r[:-h] * r[h:]) / v) for h in lags]


def periodogram_peak(r, lo_frac=0.0):
    """Hann periodogram; returns (alpha grid, power, peak alpha, fraction of power in [0.4,0.5])."""
    x = r - r.mean()
    n = 2 ** int(np.floor(np.log2(x.size)))
    x = x[:n] * np.hanning(n)
    P = np.abs(np.fft.rfft(x)) ** 2 / n
    a = np.arange(P.size) / n
    # smooth with a running mean of width ~0.004 in alpha for a stable peak
    w = max(1, int(0.004 * n))
    Ps = np.convolve(P, np.ones(w) / w, mode='same')
    sel = a > 0.02
    peak = float(a[sel][np.argmax(Ps[sel])])
    band = float(P[(a >= 0.4) & (a <= 0.5)].sum() / P[a > 0].sum())
    return a, Ps, peak, band


def walk_defect(x, gam, w):
    """Weighted centroid difference sum w_k (e^{i x_k} - e^{i gamma_k})."""
    return complex(np.sum(w * (np.exp(1j * x) - np.exp(1j * gam))))
