#!/usr/bin/env python3
"""Exact RVM-residual encoding of unfolded zeta-zero pair statistics.

The script uses the independently generated ordinate table supplied in the
``rvm_portador_residuo`` package.  It verifies the exact identity

    M(gamma_{k+h}) - M(gamma_k)
      = h + eta_{k+h} - eta_k,

where eta_k = M(gamma_k) - (k - 1/2), estimates the positive pair density from
the residual increments, and compares it with the GUE sine-kernel density.  It
also computes a block-averaged unfolded form factor.  The numerical comparison
is descriptive; the algebraic residual identity is exact up to floating-point
roundoff.
"""

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


def rvm_clock(t: np.ndarray) -> np.ndarray:
    """Leading Riemann--von Mangoldt clock used for exact unfolding."""
    return (t / TWOPI) * np.log(t / (TWOPI * np.e)) + 7.0 / 8.0


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def positive_pair_density(
    unfolded: np.ndarray,
    residual: np.ndarray,
    start: int,
    xmax: float,
    bin_width: float,
    max_lag: int,
) -> tuple[np.ndarray, np.ndarray, float, int]:
    """Estimate the positive two-point density from exact residual increments."""
    edges = np.arange(0.0, xmax + bin_width * 0.5, bin_width)
    counts = np.zeros(edges.size - 1, dtype=np.float64)
    population = unfolded.size - start
    reconstruction_error = 0.0

    for lag in range(1, max_lag + 1):
        direct = unfolded[start + lag :] - unfolded[start:-lag]
        reconstructed = lag + residual[start + lag :] - residual[start:-lag]
        reconstruction_error = max(
            reconstruction_error,
            float(np.max(np.abs(direct - reconstructed))),
        )
        counts += np.histogram(reconstructed, bins=edges)[0]

    centers = 0.5 * (edges[:-1] + edges[1:])
    density = counts / (population * bin_width)
    return centers, density, reconstruction_error, population


def windowed_connected_form_factor(
    centers: np.ndarray,
    density: np.ndarray,
    reference_density: np.ndarray,
    bin_width: float,
    xmax: float,
    alphas: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    """Cosine transform of the connected pair density with a Hann gap window.

    A compact gap window is essential here.  The raw finite trace contains
    coherent arithmetic/clock spikes and is not a pointwise estimator of the
    GUE form factor.  Applying the same window to the data and the sine-kernel
    reference gives a like-for-like connected statistic.
    """
    window = 0.5 * (1.0 + np.cos(np.pi * centers / xmax))
    cosine = np.cos(TWOPI * np.outer(alphas, centers))
    measured = 1.0 + 2.0 * bin_width * (cosine @ (window * (density - 1.0)))
    reference = 1.0 + 2.0 * bin_width * (
        cosine @ (window * (reference_density - 1.0))
    )
    return measured, reference


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    default_input = root / "data" / "g_hp.bin"
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=default_input)
    parser.add_argument(
        "--figure",
        type=Path,
        default=root / "figures" / "unfolded_residual_pair_law.png",
    )
    parser.add_argument("--burn", type=int, default=1200)
    parser.add_argument("--xmax", type=float, default=8.0)
    parser.add_argument("--bin-width", type=float, default=0.08)
    parser.add_argument("--max-lag", type=int, default=16)
    args = parser.parse_args()

    gammas = load_float64(args.input)
    ordinal = np.arange(1, gammas.size + 1, dtype=np.float64)
    unfolded = rvm_clock(gammas)
    residual = unfolded - (ordinal - 0.5)

    centers, density, identity_error, population = positive_pair_density(
        unfolded,
        residual,
        args.burn,
        args.xmax,
        args.bin_width,
        args.max_lag,
    )
    sine_density = 1.0 - np.sinc(centers) ** 2
    comparison = (centers >= 0.2) & (centers <= 6.0)
    pair_rmse = float(np.sqrt(np.mean((density[comparison] - sine_density[comparison]) ** 2)))

    alpha_grid = np.unique(
        np.concatenate(
            [
                np.linspace(0.05, 2.0, 391),
                np.array([0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 2.00]),
            ]
        )
    )
    form_factor, windowed_gue = windowed_connected_form_factor(
        centers,
        density,
        sine_density,
        args.bin_width,
        args.xmax,
        alpha_grid,
    )
    form_mask = (alpha_grid >= 0.10) & (alpha_grid <= 1.80)
    form_rmse = float(
        np.sqrt(np.mean((form_factor[form_mask] - windowed_gue[form_mask]) ** 2))
    )

    tail_residual = residual[args.burn :]
    tail_size = tail_residual.size
    integer_rows: list[tuple[int, float, float]] = []
    for mode in (1, 2, 3):
        residual_sum = abs(np.sum(np.exp(1j * TWOPI * mode * tail_residual)))
        integer_rows.append((mode, residual_sum, residual_sum / np.sqrt(tail_size)))

    try:
        displayed_input = args.input.resolve().relative_to(root.resolve())
    except ValueError:
        displayed_input = args.input
    try:
        displayed_figure = args.figure.resolve().relative_to(root.resolve())
    except ValueError:
        displayed_figure = args.figure

    print("Exact unfolded RVM-residual pair analysis")
    print(f"input = {displayed_input}")
    print(f"input sha256 = {sha256(args.input)}")
    print(f"ordinates = {gammas.size}")
    print(f"ordinate range = [{gammas[0]:.12f}, {gammas[-1]:.12f}]")
    print(f"analysis tail starts at ordinal = {args.burn + 1}")
    print(
        "eta statistics: "
        f"mean={np.mean(tail_residual):+.6e}, "
        f"sd={np.std(tail_residual):.6f}, "
        f"min={np.min(tail_residual):+.6f}, "
        f"max={np.max(tail_residual):+.6f}"
    )
    print(
        "max reconstruction error in "
        "M(gamma[k+h])-M(gamma[k]) = h+eta[k+h]-eta[k]: "
        f"{identity_error:.3e}"
    )
    print(
        f"positive pair density: population={population}, max_lag={args.max_lag}, "
        f"bin_width={args.bin_width:.3f}, RMSE on 0.2<=s<=6 = {pair_rmse:.4f}"
    )
    print(
        "Hann-windowed connected form factor: "
        f"gap cutoff={args.xmax:.1f}, RMSE on 0.1<=alpha<=1.8 = {form_rmse:.4f}"
    )
    print("integer residual modes (the unfolded ordinal carrier is constant):")
    print("  m       |sum exp(2*pi*i*m*eta_k)|      /sqrt(H)")
    for mode, magnitude, normalized in integer_rows:
        print(f"  {mode:d}       {magnitude:18.6f}      {normalized:10.6f}")
    print("selected windowed connected form-factor values:")
    print("  alpha        measured      windowed GUE")
    for alpha in (0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 2.00):
        index = int(np.argmin(np.abs(alpha_grid - alpha)))
        print(
            f"  {alpha:4.2f}        {form_factor[index]:8.4f}        "
            f"{windowed_gue[index]:8.4f}"
        )

    ink = "#202020"
    blue = "#0b6fa4"
    orange = "#c8681c"
    green = "#4a7c59"
    gray = "#8a8a8a"
    fig, axes = plt.subplots(1, 2, figsize=(12.0, 4.7), dpi=180)

    ax = axes[0]
    ax.plot(centers, density, color=blue, linewidth=1.25, label="residual-increment estimate")
    ax.plot(
        centers,
        sine_density,
        color=orange,
        linewidth=1.8,
        linestyle="--",
        label=r"$1-[\sin(\pi s)/(\pi s)]^2$",
    )
    ax.set_xlim(0.0, args.xmax)
    ax.set_ylim(0.0, 1.35)
    ax.set_xlabel(r"unfolded positive separation $s$")
    ax.set_ylabel(r"pair density $R_2(s)$")
    ax.set_title("The sine law is encoded by RVM-residual increments", loc="left")
    ax.legend(frameon=False, fontsize=8.5)

    ax = axes[1]
    ax.plot(
        alpha_grid,
        form_factor,
        color=blue,
        linewidth=1.2,
        label="residual-increment transform",
    )
    ax.plot(
        alpha_grid,
        windowed_gue,
        color=green,
        linewidth=1.8,
        linestyle="--",
        label="same transform of the sine law",
    )
    ax.axvline(1.0, color=gray, linewidth=0.8, linestyle=":")
    ax.set_xlim(0.05, 2.0)
    ax.set_ylim(0.0, max(1.4, float(np.quantile(form_factor, 0.99)) * 1.1))
    ax.set_xlabel(r"unfolded frequency $\alpha$")
    ax.set_ylabel("windowed connected form factor")
    ax.set_title("Fourier-dual check after gap smoothing", loc="left")
    ax.legend(frameon=False, fontsize=8.5)

    for ax in axes:
        ax.tick_params(labelsize=8.5)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color(gray)
        ax.spines["bottom"].set_color(gray)
        ax.grid(color="#ececec", linewidth=0.6, zorder=0)

    fig.suptitle(
        "Exact residual unfolding of 22,491 computed zeta ordinates",
        x=0.01,
        y=1.02,
        ha="left",
        color=ink,
        fontsize=12.0,
    )
    fig.tight_layout()
    args.figure.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.figure, bbox_inches="tight", facecolor="white")
    print(f"figure = {displayed_figure}")


if __name__ == "__main__":
    main()
