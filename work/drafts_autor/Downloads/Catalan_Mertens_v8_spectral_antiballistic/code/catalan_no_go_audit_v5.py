#!/usr/bin/env python3
"""Finite audit for the Catalan--Mertens v5 criterion/mechanism note."""

from __future__ import annotations

import json
import math
from pathlib import Path

def catalan(n: int) -> int:
    return math.comb(2 * n, n) // (n + 1)


def primitive_dyck_paths(semilength: int):
    length = 2 * semilength

    def rec(pos: int, height: int, word: list[int]):
        if pos == length:
            if height == 0:
                yield tuple(word)
            return
        for step in (1, -1):
            new_height = height + step
            if new_height < 0:
                continue
            if pos + 1 < length and new_height == 0:
                continue
            if pos + 1 == length and new_height != 0:
                continue
            word.append(step)
            yield from rec(pos + 1, new_height, word)
            word.pop()

    yield from rec(0, 0, [])


def heights(word):
    out = [0]
    for step in word:
        out.append(out[-1] + step)
    return out


def mobius_sieve(limit: int):
    mu = [1] * (limit + 1)
    prime = [True] * (limit + 1)
    prime[0:2] = [False, False]
    for p in range(2, limit + 1):
        if not prime[p]:
            continue
        for n in range(p, limit + 1, p):
            prime[n] = False if n != p else prime[n]
            mu[n] *= -1
        square = p * p
        for n in range(square, limit + 1, square):
            mu[n] = 0
    mu[0] = 0
    return mu


def prime_dilation_error(mu, limit: int):
    mertens = [0] * (limit + 1)
    for n in range(1, limit + 1):
        mertens[n] = mertens[n - 1] + mu[n]
    primes = [p for p in range(2, 50) if all(p % d for d in range(2, int(p**0.5) + 1))]
    maximum = 0
    for p in primes:
        ap = [0] * (limit + 1)
        for n in range(1, limit + 1):
            ap[n] = ap[n - 1] + (mu[n] if n % p else 0)
        for x in range(1, limit + 1):
            maximum = max(maximum, abs(mertens[x] - (ap[x] - ap[x // p])))
    return maximum


def main():
    root = Path(__file__).resolve().parents[1]
    output = root / "outputs"
    output.mkdir(parents=True, exist_ok=True)

    rows = []
    for n in range(1, 8):
        paths = list(primitive_dyck_paths(n))
        maxima = [max(heights(path)) for path in paths]
        rows.append(
            {
                "semilength": n,
                "enumerated_primitive_paths": len(paths),
                "expected_catalan": catalan(n - 1),
                "largest_possible_height": max(maxima),
            }
        )

    mu = mobius_sieve(5000)
    identity_error = prime_dilation_error(mu, 5000)
    report = {
        "purpose": "audit identities and demonstrate the Catalan-only obstruction",
        "primitive_excursions": rows,
        "prime_dilation_identity_max_abs_error": identity_error,
        "conclusion": (
            "Primitive Catalan structure permits mountain excursions of height L/2; "
            "the prime-dilation average reproduces M exactly and supplies no bound."
        ),
    }
    (output / "catalan_no_go_audit_v5.json").write_text(
        json.dumps(report, indent=2), encoding="utf-8"
    )

    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
