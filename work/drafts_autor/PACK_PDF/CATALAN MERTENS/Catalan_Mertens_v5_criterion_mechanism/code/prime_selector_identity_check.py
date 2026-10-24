#!/usr/bin/env python3
"""Finite exact checks of the prime-shell, transfer, and Fourier identities."""

from __future__ import annotations

import argparse
import cmath
import json
import math
from pathlib import Path


def mobius_sieve(limit: int) -> list[int]:
    mu = [1] * (limit + 1)
    prime = [True] * (limit + 1)
    prime[0:2] = [False, False]
    primes: list[int] = []
    mu[0] = 0
    for n in range(2, limit + 1):
        if prime[n]:
            primes.append(n)
            mu[n] = -1
        for p in primes:
            if n * p > limit:
                break
            prime[n * p] = False
            if n % p == 0:
                mu[n * p] = 0
                break
            mu[n * p] = -mu[n]
    return mu


def primes_up_to(limit: int) -> list[int]:
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]
    for p in range(2, int(math.isqrt(limit)) + 1):
        if sieve[p]:
            for n in range(p * p, limit + 1, p):
                sieve[n] = False
    return [p for p in range(2, limit + 1) if sieve[p]]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=100_000)
    parser.add_argument("--kernel-x", type=int, default=30)
    parser.add_argument("--output", type=Path, default=Path("selector_check.json"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    mu = mobius_sieve(args.limit)
    mertens = [0] * (args.limit + 1)
    for n in range(1, args.limit + 1):
        mertens[n] = mertens[n - 1] + mu[n]

    test_primes = [p for p in (2, 3, 5, 7, 11, 97) if p <= args.limit]
    shell_failures = []
    for p in test_primes:
        filtered = [0] * (args.limit + 1)
        for n in range(1, args.limit + 1):
            filtered[n] = filtered[n - 1] + (mu[n] if n % p else 0)
        for x in range(1, args.limit + 1):
            shell = filtered[x] - filtered[x // p]
            if shell != mertens[x]:
                shell_failures.append({"p": p, "x": x})
                break

    kernel_primes = primes_up_to(args.kernel_x)
    atoms = [(1, 1)]
    for p in kernel_primes:
        atoms += [(product * p, -sign) for product, sign in atoms]
    atoms.sort()
    kernel_failures = []
    for x in range(1, args.kernel_x + 1):
        value = sum(sign for product, sign in atoms if product <= x)
        if value != mertens[x]:
            kernel_failures.append({"x": x, "K": value, "M": mertens[x]})

    convolution = {1: 1}
    for p in kernel_primes:
        updated = dict(convolution)
        for product, sign in convolution.items():
            updated[product * p] = updated.get(product * p, 0) - sign
        convolution = updated
    transfer_ok = sorted(convolution.items()) == atoms

    fourier_errors = []
    for tau in (0.125, 0.5, 1.0, 2.75):
        direct = sum(sign * cmath.exp(-1j * tau * math.log(product)) for product, sign in atoms)
        product = 1.0 + 0.0j
        for p in kernel_primes:
            product *= 1.0 - cmath.exp(-1j * tau * math.log(p))
        fourier_errors.append(abs(direct - product))

    result = {
        "limit": args.limit,
        "tested_shell_primes": test_primes,
        "shell_failures": shell_failures,
        "kernel_x": args.kernel_x,
        "kernel_primes": kernel_primes,
        "kernel_failures": kernel_failures,
        "transfer_factorization_ok": transfer_ok,
        "max_fourier_factorization_error": max(fourier_errors),
        "status": "PASS" if not shell_failures and not kernel_failures and transfer_ok else "FAIL",
        "interpretation": "finite verification of exact identities, not an RH test",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
