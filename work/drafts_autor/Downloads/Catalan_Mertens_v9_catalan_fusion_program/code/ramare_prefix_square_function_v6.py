#!/usr/bin/env python3
"""Finite exact audit of the prime-coloured Ramare prefix decomposition.

This is a falsification tool for Version 6, not evidence for an asymptotic
bound.  The default prime band is deliberately computational and is not
claimed to reproduce the optimized band in Matomaki--Teravainen.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def mobius_and_spf(limit: int) -> tuple[np.ndarray, np.ndarray]:
    mu = np.ones(limit + 1, dtype=np.int8)
    spf = np.zeros(limit + 1, dtype=np.int32)
    primes: list[int] = []
    mu[0] = 0
    for n in range(2, limit + 1):
        if spf[n] == 0:
            spf[n] = n
            primes.append(n)
            mu[n] = -1
        for p in primes:
            value = p * n
            if value > limit:
                break
            spf[value] = p
            if n % p == 0:
                mu[value] = 0
                break
            mu[value] = -mu[n]
    return mu, spf


def distinct_factors(n: int, spf: np.ndarray) -> list[int]:
    factors: list[int] = []
    while n > 1:
        p = int(spf[n])
        factors.append(p)
        while n % p == 0:
            n //= p
    return factors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--x", type=int, default=100_000)
    parser.add_argument("--theta", type=float, default=0.56)
    parser.add_argument("--P", type=int, default=3)
    parser.add_argument("--Q", type=int, default=97)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()

    h = max(2, int(round(args.x ** args.theta)))
    limit = args.x + h
    mu, spf = mobius_and_spf(limit)

    block_increments: dict[int, np.ndarray] = {}
    remainder_increment = np.zeros(h, dtype=float)
    direct_increment = mu[args.x + 1 : args.x + h + 1].astype(float)

    for offset, n in enumerate(range(args.x + 1, args.x + h + 1)):
        if mu[n] == 0:
            continue
        eligible = [p for p in distinct_factors(n, spf) if args.P < p <= args.Q]
        if not eligible:
            remainder_increment[offset] = float(mu[n])
            continue
        weight = 1.0 / len(eligible)
        for p in eligible:
            block = int(math.floor(math.log2(p)))
            block_increments.setdefault(block, np.zeros(h, dtype=float))
            # -mu(n/p)/nu_P(n) = mu(n)/nu_P(n) for squarefree n.
            block_increments[block][offset] += -float(mu[n // p]) * weight

    block_prefix = {
        block: np.cumsum(increments) for block, increments in block_increments.items()
    }
    remainder_prefix = np.cumsum(remainder_increment)
    direct_prefix = np.cumsum(direct_increment)
    reconstructed = remainder_prefix.copy()
    for values in block_prefix.values():
        reconstructed += values

    reconstruction_error = float(np.max(np.abs(reconstructed - direct_prefix)))
    diagonal = float(sum(np.dot(v, v) for v in block_prefix.values()))
    blocks = sorted(block_prefix)
    signed_off_diagonal = 0.0
    absolute_off_diagonal = 0.0
    for i, left in enumerate(blocks):
        for right in blocks[i + 1 :]:
            inner = float(np.dot(block_prefix[left], block_prefix[right]))
            signed_off_diagonal += 2.0 * inner
            absolute_off_diagonal += 2.0 * abs(inner)
    remainder_energy = float(np.dot(remainder_prefix, remainder_prefix))
    projected_energy = float(np.dot(direct_prefix, direct_prefix))
    crsf_absolute_total = remainder_energy + diagonal + absolute_off_diagonal

    root = Path(__file__).resolve().parents[1]
    output_dir = root / "outputs"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = args.output or output_dir / "ramare_prefix_square_function_v6.json"

    result = {
        "finite_audit_only": True,
        "x": args.x,
        "H": h,
        "theta": args.theta,
        "prime_band": [args.P, args.Q],
        "dyadic_prime_blocks": blocks,
        "reconstruction_max_abs_error": reconstruction_error,
        "remainder_energy": remainder_energy,
        "diagonal_block_energy": diagonal,
        "signed_off_diagonal": signed_off_diagonal,
        "absolute_off_diagonal": absolute_off_diagonal,
        "crsf_absolute_total_over_H2": crsf_absolute_total / (h * h),
        "projected_prefix_energy_over_H2": projected_energy / (h * h),
        "maximum_prefix_height_over_sqrtH": float(
            np.max(np.abs(direct_prefix)) / math.sqrt(h)
        ),
    }
    output_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")

    fig, axes = plt.subplots(2, 1, figsize=(9.2, 6.4), constrained_layout=True)
    axes[0].plot(direct_prefix, color="#202060", label="direct Mertens prefix")
    axes[0].plot(reconstructed, "--", color="#d05432", label="Ramare reconstruction")
    axes[0].set_ylabel("prefix sum")
    axes[0].grid(alpha=0.25)
    axes[0].legend(frameon=False)
    for block in blocks:
        axes[1].plot(block_prefix[block], linewidth=1.0,
                     label=fr"$2^{block}\leq p<2^{block + 1}$")
    axes[1].plot(remainder_prefix, color="black", linewidth=1.2,
                 label="rough remainder")
    axes[1].set_xlabel("prefix length")
    axes[1].set_ylabel("coloured current")
    axes[1].grid(alpha=0.25)
    axes[1].legend(frameon=False, ncol=2, fontsize=8)
    png_path = output_dir / "ramare_prefix_square_function_v6.png"
    fig.savefig(png_path, dpi=220)
    plt.close(fig)

    result["png"] = str(png_path)
    output_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
