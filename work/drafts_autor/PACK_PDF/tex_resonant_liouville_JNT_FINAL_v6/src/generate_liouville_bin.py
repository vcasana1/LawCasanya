#!/usr/bin/env python3
"""Generate lambda(1),...,lambda(N) as raw signed int8."""
from __future__ import annotations
import argparse, hashlib
from pathlib import Path
import numpy as np

def generate(N: int) -> np.ndarray:
    is_prime = np.ones(N+1,dtype=np.bool_)
    is_prime[:2] = False
    limit = int(N**0.5)
    for p in range(2,limit+1):
        if is_prime[p]:
            is_prime[p*p:N+1:p] = False
    primes = np.flatnonzero(is_prime)
    parity = np.zeros(N+1,dtype=np.uint8)
    for p0 in primes:
        p = int(p0); q = p
        while q <= N:
            parity[q:N+1:q] ^= 1
            if q > N//p:
                break
            q *= p
    return (1-2*parity[1:]).astype(np.int8)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--N",type=int,default=21_000_000)
    ap.add_argument("--out",default="data/liouville_int8_N21000000_regenerated.bin")
    args=ap.parse_args()
    lam=generate(args.N)
    out=Path(args.out); out.parent.mkdir(parents=True,exist_ok=True)
    lam.tofile(out)
    print(f"N={args.N}")
    print(f"bytes={out.stat().st_size}")
    print(f"sha256={hashlib.sha256(out.read_bytes()).hexdigest()}")

if __name__=="__main__":
    main()
