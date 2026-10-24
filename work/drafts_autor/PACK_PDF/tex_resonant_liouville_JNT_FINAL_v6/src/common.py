#!/usr/bin/env python3
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BIN = ROOT / "data" / "liouville_int8_N21000000.bin"

def load_liouville(path=DEFAULT_BIN):
    path = Path(path)
    return np.memmap(path, dtype=np.int8, mode="r")

def lambda_at(lam, n):
    n = np.asarray(n, dtype=np.int64)
    if np.any(n < 1) or np.any(n > len(lam)):
        raise ValueError("Liouville index outside the available binary range.")
    return lam[n - 1]

def harmonic_number(N):
    n = np.arange(1, N+1, dtype=np.float64)
    return float(np.sum(1.0/n))

def correlation_rational(lam, X, p, q):
    n = np.arange(1, X + 1, dtype=np.int64)
    idx = (p*n)//q
    mask = idx >= 1
    vals = lambda_at(lam,n[mask]).astype(np.int16)*lambda_at(lam,idx[mask]).astype(np.int16)
    return int(vals.sum())

def correlation_integer_layer(lam, X, m, c):
    n = np.arange(1, X + 1, dtype=np.int64)
    Xld = np.longdouble(X)
    cld = np.longdouble(str(c))
    if c >= 0:
        alpha = np.longdouble(m)*np.expm1(cld/Xld)
        r = np.floor(alpha*n.astype(np.longdouble)).astype(np.int64)
        idx = m*n+r
    else:
        beta = np.longdouble(m)*(1-np.exp(cld/Xld))
        r = np.ceil(beta*n.astype(np.longdouble)).astype(np.int64)
        idx = m*n-r
    vals = lambda_at(lam,n).astype(np.int16)*lambda_at(lam,idx).astype(np.int16)
    return int(vals.sum()), r

def correlation_rational_layer(lam, X, p, q, c):
    n = np.arange(1, X+1, dtype=np.int64)
    a = (np.longdouble(p)/np.longdouble(q))*np.exp(np.longdouble(str(c))/np.longdouble(X))
    idx = np.floor(a*n.astype(np.longdouble)).astype(np.int64)
    mask = idx >= 1
    vals = lambda_at(lam,n[mask]).astype(np.int16)*lambda_at(lam,idx[mask]).astype(np.int16)
    return int(vals.sum())

def logarithmic_integer_layer(lam, X, m, c):
    n = np.arange(1, X+1, dtype=np.int64)
    a = np.longdouble(m)*np.exp(np.longdouble(str(c))/np.longdouble(X))
    idx = np.floor(a*n.astype(np.longdouble)).astype(np.int64)
    mask = idx >= 1
    vals = lambda_at(lam,n[mask]).astype(np.float64)*lambda_at(lam,idx[mask]).astype(np.float64)
    weights = 1.0/n[mask].astype(np.float64)
    H = np.sum(1.0/n.astype(np.float64))
    return float(np.sum(weights*vals)/H)

def resonant_harmonic_mass_integer(X, m, c):
    a = np.longdouble(m)*np.expm1(np.longdouble(str(c))/np.longdouble(X))
    if a <= 0:
        return 0.0, 0
    n0 = min(X, int(np.ceil(np.longdouble(1)/a)-1))
    n = np.arange(1, X+1, dtype=np.float64)
    H = float(np.sum(1.0/n))
    if n0 < 1:
        return 0.0, n0
    B = float(np.sum(1.0/np.arange(1,n0+1,dtype=np.float64))/H)
    return B, n0
