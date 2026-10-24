#!/usr/bin/env python3
"""Finite verification of the Lambert-centroid/Dirac-comb counterexample."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from data_io import load_float64


TWOPI = 2.0 * np.pi


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input", type=Path, default=root / "data" / "rvm_tau_2001052.bin"
    )
    parser.add_argument(
        "--figure",
        type=Path,
        default=root / "figures" / "rvm_counterexample_validation.png",
    )
    args = parser.parse_args()
    tau = load_float64(args.input)
    count = tau.size
    phase = np.exp(1j * tau)
    prefix = np.cumsum(phase)
    weighted = np.cumsum(np.arange(count, dtype=np.float64) * phase)

    def centroid(size: int) -> complex:
        return prefix[size - 1] - weighted[size - 1] / size

    base_sizes = np.unique(
        np.round(np.logspace(np.log10(1000), np.log10(count // 2), 64)).astype(int)
    )
    increments = np.array([abs(centroid(2 * n) - centroid(n)) for n in base_sizes])
    compensated = increments * base_sizes / np.log(base_sizes) ** 2

    ordinal = np.arange(1, count + 1, dtype=np.float64)
    clock_residual = (
        (tau / TWOPI) * np.log(tau / (TWOPI * np.e))
        + 7.0 / 8.0
        - (ordinal - 0.5)
    )

    print("Lambert centroid and lattice-pair counterexample")
    print(f"input = data/{args.input.name}")
    print(f"input sha256 = {sha256(args.input)}")
    print(f"levels = {count}")
    print(f"max float64 |M(tau_k)-(k-1/2)| = {np.max(np.abs(clock_residual)):.3e}")
    print(f"C_N^M = {centroid(count).real:+.12f} {centroid(count).imag:+.12f}i")
    print("successive-doubling convergence check")
    print(f"mean |C_(2N)-C_N|*N/log(N)^2 = {np.mean(compensated):.9f}")
    print(f"sd = {np.std(compensated):.9f}")
    print(f"min = {np.min(compensated):.9f}")
    print(f"max = {np.max(compensated):.9f}")
    print("unfolded pair locations = positive integers exactly in the defining clock")
    print("comparison process = continuous 1-sinc(s)^2 density")

    blue = "#0b6fa4"
    orange = "#c8681c"
    green = "#4a7c59"
    gray = "#8a8a8a"
    fig, axes = plt.subplots(1, 2, figsize=(11.8, 4.55), dpi=180)

    ax = axes[0]
    ax.loglog(base_sizes, increments, color=blue, linewidth=1.15, label=r"$|C_{2N}^M-C_N^M|$")
    coefficient = float(np.median(compensated))
    ax.loglog(
        base_sizes,
        coefficient * np.log(base_sizes) ** 2 / base_sizes,
        color=orange,
        linewidth=1.3,
        linestyle="--",
        label=rf"${coefficient:.3f}\log^2N/N$",
    )
    ax.set_xlabel(r"$N$")
    ax.set_ylabel("successive-doubling difference")
    ax.set_title("Lambert centroid: convergence-scale check", loc="left")
    ax.legend(frameon=False, fontsize=8.2)

    ax = axes[1]
    block = 200
    integer = np.arange(1, 9, dtype=np.float64)
    lattice_mass = 1.0 - integer / block
    ax.bar(integer, lattice_mass, width=0.16, color=blue, alpha=0.78, label="RVM pair atoms")
    continuum = np.linspace(0.02, 8.5, 1200)
    ax.plot(
        continuum,
        1.0 - np.sinc(continuum) ** 2,
        color=green,
        linewidth=1.65,
        label="GUE sine density",
    )
    ax.set_xlim(0.0, 8.5)
    ax.set_ylim(0.0, 1.12)
    ax.set_xlabel("positive unfolded separation")
    ax.set_ylabel("atom mass / comparison density")
    ax.set_title("Exact obstruction: Dirac comb, not sine law", loc="left")
    ax.legend(frameon=False, fontsize=8.2)

    for ax in axes:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color(gray)
        ax.spines["bottom"].set_color(gray)
        ax.grid(color="#ececec", linewidth=0.55)
    fig.suptitle(
        "The Lambert clock separates centroid convergence from pair correlation",
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
