#!/usr/bin/env python3
"""Independent finite-range validation of the log(N)/N centroid rate."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from data_io import load_float64


LIMIT = 0.77689426079325358 + 0.767855668864547j
FULL_COUNT = 2_001_052
FULL_OBSERVED = 8.7162e-6


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=root / "data" / "g_hp.bin")
    parser.add_argument(
        "--figure",
        type=Path,
        default=root / "figures" / "centroid_rate_validation.png",
    )
    args = parser.parse_args()

    gamma = load_float64(args.input)
    phase = np.exp(1j * gamma)
    prefix = np.concatenate(([0.0j], np.cumsum(phase)))
    weighted_prefix = np.concatenate(
        ([0.0j], np.cumsum(np.arange(gamma.size, dtype=np.float64) * phase))
    )

    def centroid(size: int) -> complex:
        return prefix[size] - weighted_prefix[size] / size

    sizes = np.unique(
        np.round(np.logspace(np.log10(300), np.log10(gamma.size), 60)).astype(int)
    )
    error = np.array([abs(centroid(int(size)) - LIMIT) for size in sizes])
    compensated = error * sizes / np.log(sizes)
    coefficient = float(np.mean(compensated))
    coefficient_sd = float(np.std(compensated))
    prediction = coefficient * np.log(FULL_COUNT) / FULL_COUNT

    print("Independent centroid-rate validation")
    print(f"input = data/{args.input.name}")
    print(f"input sha256 = {file_sha256(args.input)}")
    print(f"ordinates = {gamma.size}")
    print(f"conditional limit = {LIMIT.real:.17f} {LIMIT.imag:+.15f}i")
    print(f"mean of |C_N-L|*N/log(N) = {coefficient:.6f}")
    print(f"standard deviation = {coefficient_sd:.6f}")
    print(f"minimum = {np.min(compensated):.6f}")
    print(f"maximum = {np.max(compensated):.6f}")
    print(f"prediction at N={FULL_COUNT} = {prediction:.8e}")
    print(f"full-table observed discrepancy = {FULL_OBSERVED:.8e}")
    print(f"observed/predicted = {FULL_OBSERVED / prediction:.6f}")

    blue = "#0b6fa4"
    orange = "#c8681c"
    green = "#4a7c59"
    gray = "#8a8a8a"
    fig, axes = plt.subplots(1, 2, figsize=(11.6, 4.5), dpi=180)

    ax = axes[0]
    ax.loglog(sizes, error, color=blue, linewidth=1.25, label=r"$|C_N-L|$")
    ax.loglog(
        sizes,
        coefficient * np.log(sizes) / sizes,
        color=orange,
        linewidth=1.6,
        linestyle="--",
        label=rf"${coefficient:.3f}\log N/N$",
    )
    root_coefficient = float(np.mean(error * np.sqrt(sizes)))
    ax.loglog(
        sizes,
        root_coefficient / np.sqrt(sizes),
        color=green,
        linewidth=1.2,
        linestyle=":",
        label=r"best $N^{-1/2}$ comparison",
    )
    ax.set_xlabel(r"$N$")
    ax.set_ylabel(r"$|C_N-L|$")
    ax.set_title("Independent low-height ordinate table", loc="left")
    ax.legend(frameon=False, fontsize=8.3)

    ax = axes[1]
    ax.semilogx(sizes, compensated, color=orange, linewidth=1.1)
    ax.axhline(coefficient, color=gray, linewidth=0.8, linestyle="--")
    ax.scatter(
        [FULL_COUNT],
        [FULL_OBSERVED * FULL_COUNT / np.log(FULL_COUNT)],
        color=blue,
        s=35,
        zorder=5,
        label=r"independent full-table check, $N=2{,}001{,}052$",
    )
    ax.set_xlabel(r"$N$")
    ax.set_ylabel(r"$|C_N-L|N/\log N$")
    ax.set_title("Compensated rate and 90-fold extrapolation", loc="left")
    ax.legend(frameon=False, fontsize=8.2)

    for ax in axes:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color(gray)
        ax.spines["bottom"].set_color(gray)
        ax.grid(color="#ececec", linewidth=0.6)

    fig.suptitle(
        r"Observed exponential-centroid rate: $|C_N-L|\asymp \log N/N$",
        x=0.01,
        y=1.02,
        ha="left",
        fontsize=12.2,
    )
    fig.tight_layout()
    args.figure.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.figure, bbox_inches="tight", facecolor="white")
    print(f"figure = figures/{args.figure.name}")


if __name__ == "__main__":
    main()
