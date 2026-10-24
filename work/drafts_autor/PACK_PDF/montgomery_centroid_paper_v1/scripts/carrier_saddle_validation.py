#!/usr/bin/env python3
"""Numerically verify the localized archimedean stationary-phase law."""

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


def carrier_amplitude(tau: np.ndarray, alpha: float, logarithm: float) -> float:
    phase = np.longdouble(alpha * logarithm) * tau.astype(np.longdouble)
    two_pi = np.longdouble(2.0) * np.longdouble(np.pi)
    phase -= two_pi * np.floor(phase / two_pi)
    return float(abs(np.sum(np.exp(1j * phase.astype(np.float64)))))


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input", type=Path, default=root / "data" / "rvm_tau_2001052.bin"
    )
    parser.add_argument(
        "--figure",
        type=Path,
        default=root / "figures" / "carrier_saddle_validation.png",
    )
    args = parser.parse_args()
    tau = load_float64(args.input)
    count = tau.size
    height = float(tau[-1])
    logarithm = float(np.log(height / TWOPI))

    # The full binary contains 2,001,052 phases.  A 13-point grid in each
    # nonintegral band keeps the validation reproducible without replacing the
    # actual sum by a subsample.
    intervals = [
        np.linspace(0.22, 0.94, 13),
        np.linspace(1.06, 1.94, 13),
        np.linspace(2.06, 2.94, 13),
    ]
    alphas = np.concatenate(intervals)
    measured = np.array([carrier_amplitude(tau, float(a), logarithm) for a in alphas])
    mode = np.ceil(alphas).astype(int)
    time = alphas * logarithm
    predicted = time * np.exp(time / (2.0 * mode)) / mode ** 1.5
    ratio = measured / predicted

    selected = np.array([0.30, 0.50, 0.70, 0.90, 1.20, 1.40, 1.80, 2.20, 2.60, 2.90])
    selected_measured = np.array([
        measured[int(np.argmin(np.abs(alphas - a)))]
        if np.min(np.abs(alphas - a)) < 1e-12
        else carrier_amplitude(tau, float(a), logarithm)
        for a in selected
    ])
    selected_mode = np.ceil(selected).astype(int)
    selected_time = selected * logarithm
    selected_predicted = (
        selected_time * np.exp(selected_time / (2.0 * selected_mode)) / selected_mode ** 1.5
    )

    print("Archimedean carrier saddle validation")
    print(f"input = data/{args.input.name}")
    print(f"input sha256 = {sha256(args.input)}")
    print(f"count = {count}")
    print(f"tau_N = {height:.12f}")
    print(f"log(tau_N/(2*pi)) = {logarithm:.9f}")
    print("stationary phase: tau_n^*=2*pi*exp(t/n)")
    print("leading magnitude: t*exp(t/(2*n))/n^(3/2), n=ceil(alpha)")
    print("  alpha   mode      measured      predicted      ratio")
    for alpha, nmode, actual, estimate in zip(
        selected, selected_mode, selected_measured, selected_predicted
    ):
        print(f"  {alpha:5.2f}    {nmode:2d}    {actual:11.3f}    {estimate:11.3f}    {actual/estimate:8.4f}")
    interior = np.minimum(alphas - np.floor(alphas), np.ceil(alphas) - alphas) >= 0.08
    print(f"median measured/predicted away from integer endpoints = {np.median(ratio[interior]):.6f}")
    print(f"RMS relative error away from integer endpoints = {np.sqrt(np.mean((ratio[interior]-1.0)**2)):.6f}")

    blue = "#0b6fa4"
    orange = "#c8681c"
    gray = "#8a8a8a"
    fig, axes = plt.subplots(1, 2, figsize=(11.8, 4.55), dpi=180)
    ax = axes[0]
    ax.semilogy(alphas, measured, color=blue, linewidth=1.05, label="measured carrier sum")
    ax.semilogy(alphas, predicted, color=orange, linewidth=1.25, linestyle="--", label="localized saddle magnitude")
    for endpoint in (1.0, 2.0, 3.0):
        ax.axvline(endpoint, color=gray, linewidth=0.7, linestyle=":")
    ax.set_xlabel(r"$\alpha$, with $t=\alpha\log(T/2\pi)$")
    ax.set_ylabel(r"magnitude")
    ax.set_title("Closed carrier spectrum between endpoints", loc="left")
    ax.legend(frameon=False, fontsize=8.2)

    ax = axes[1]
    ax.plot(alphas, ratio, color=blue, linewidth=1.05)
    ax.axhline(1.0, color=orange, linewidth=1.0, linestyle="--")
    for endpoint in (1.0, 2.0, 3.0):
        ax.axvline(endpoint, color=gray, linewidth=0.7, linestyle=":")
    ax.set_ylim(0.55, 1.45)
    ax.set_xlabel(r"$\alpha$")
    ax.set_ylabel("measured / leading saddle")
    ax.set_title("Finite-$N$ compatibility of the amplitude", loc="left")

    for ax in axes:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color(gray)
        ax.spines["bottom"].set_color(gray)
        ax.grid(color="#ececec", linewidth=0.55)
    fig.suptitle(
        f"Lambert--RVM archimedean saddles, N={count:,}",
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
