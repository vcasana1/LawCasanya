#!/usr/bin/env python3
"""Blockwise audit of compressed-time Mertens moments and excursion budgets.

Input format: one signed int8 value mu(n) for each n=1,...,N.
The program never materializes the entire Mertens walk in memory.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np


def odd_double_factorial(k: int) -> int:
    value = 1
    for j in range(1, k + 1):
        value *= 2 * j - 1
    return value


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=Path)
    parser.add_argument("--block", type=int, default=5_000_000)
    parser.add_argument("--max-k", type=int, default=6)
    parser.add_argument("--output", type=Path, default=Path("moment_audit.json"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.max_k < 1:
        raise ValueError("--max-k must be positive")

    size = args.filename.stat().st_size
    data = np.memmap(args.filename, dtype=np.int8, mode="r", shape=(size,))
    moments = np.zeros(args.max_k, dtype=np.float64)
    length_budgets = [0] * args.max_k

    mertens = 0
    compressed = 0
    previous_zero = 0
    returns = 0
    max_abs = 0

    for lo in range(0, size, args.block):
        hi = min(lo + args.block, size)
        block = np.asarray(data[lo:hi])
        nz = np.flatnonzero(block)
        if nz.size == 0:
            continue

        steps = block[nz].astype(np.int64, copy=False)
        walk = np.cumsum(steps, dtype=np.int64)
        walk += mertens
        absolute = np.abs(walk).astype(np.float64, copy=False)
        max_abs = max(max_abs, int(absolute.max(initial=0.0)))

        power = absolute * absolute
        for k in range(1, args.max_k + 1):
            if k > 1:
                power = power * absolute * absolute
            moments[k - 1] += float(np.sum(power, dtype=np.float64))

        hits = np.flatnonzero(walk == 0)
        for hit in hits:
            zero = compressed + int(hit) + 1
            gap = zero - previous_zero
            for k in range(1, args.max_k + 1):
                length_budgets[k - 1] += gap ** (k + 1)
            previous_zero = zero
            returns += 1

        mertens = int(walk[-1])
        compressed += int(nz.size)

    tail = compressed - previous_zero
    records = []
    for k in range(1, args.max_k + 1):
        budget = length_budgets[k - 1] + tail ** (k + 1)
        iid_leading = (
            odd_double_factorial(k) / (k + 1) * float(compressed) ** (k + 1)
        )
        records.append(
            {
                "k": k,
                "B_k": float(moments[k - 1]),
                "Lambda_k": str(budget),
                "B_k_over_Lambda_k": float(moments[k - 1] / budget),
                "B_k_over_iid_leading": float(moments[k - 1] / iid_leading),
            }
        )

    result = {
        "input": str(args.filename.resolve()),
        "N": size,
        "compressed_steps": compressed,
        "M_N": mertens,
        "returns_to_zero": returns,
        "last_zero_compressed": previous_zero,
        "open_tail_compressed": tail,
        "max_abs_M": max_abs,
        "moments": records,
        "interpretation": "finite computation only; no asymptotic inference",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
