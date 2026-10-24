#!/usr/bin/env python3
"""Illustrate the exact Cesaro dephasing law for finite prime products.

The plot is numerical evidence only.  The limiting formula used for the
horizontal reference lines is proved algebraically in the accompanying paper.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


PRIMES = np.array([2, 3, 5, 7, 11, 13, 17, 19], dtype=np.float64)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tau-max", type=float, default=10_000.0)
    parser.add_argument("--points", type=int, default=200_001)
    parser.add_argument("--output-png", type=Path, default=Path("tau_dephasing.png"))
    parser.add_argument("--output-json", type=Path, default=Path("tau_dephasing.json"))
    return parser.parse_args()


def running_cesaro(values: np.ndarray) -> np.ndarray:
    return np.cumsum(values, dtype=np.float64) / np.arange(1, values.size + 1)


def main() -> None:
    args = parse_args()
    tau = np.linspace(0.0, args.tau_max, args.points)
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.2), constrained_layout=True)
    records = []

    for j, color in ((4, "#1967ad"), (6, "#c43c39"), (8, "#4b8f29")):
        normalized = np.prod(
            np.abs(np.sin(0.5 * tau[:, None] * np.log(PRIMES[:j])[None, :])),
            axis=1,
        )
        square_mean = running_cesaro(normalized * normalized)
        target = 2.0 ** (-j)
        axes[0].plot(tau[:4001], normalized[:4001], color=color, lw=0.8, label=f"j={j}")
        axes[1].plot(tau[1:], square_mean[1:], color=color, lw=1.0, label=f"j={j}")
        axes[1].axhline(target, color=color, ls="--", lw=0.8, alpha=0.8)
        records.append(
            {
                "j": j,
                "tau_max": args.tau_max,
                "sample_cesaro_square": float(square_mean[-1]),
                "exact_infinite_cesaro_square": target,
            }
        )

    axes[0].set_title("Normalized prime sine product")
    axes[0].set_xlabel(r"$\tau$ (initial window)")
    axes[0].set_ylabel(r"$2^{-j}|\widehat{dK_j}(\tau)|$")
    axes[0].legend(frameon=False)
    axes[0].grid(alpha=0.2)

    axes[1].set_title("Running Cesaro mean of the square")
    axes[1].set_xscale("log")
    axes[1].set_yscale("log")
    axes[1].set_xlabel(r"frequency cutoff $T$")
    axes[1].set_ylabel("running mean; dashed = exact limit")
    axes[1].legend(frameon=False)
    axes[1].grid(alpha=0.2, which="both")

    args.output_png.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output_png, dpi=220)
    plt.close(fig)
    result = {
        "records": records,
        "interpretation": "finite illustration; the limit is an exact theorem",
    }
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
