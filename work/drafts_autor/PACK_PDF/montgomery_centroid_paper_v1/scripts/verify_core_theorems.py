#!/usr/bin/env python3
"""Finite-data compatibility checks for the paper's core exact results.

The script distinguishes algebraic identities (reported with floating-point
closure errors) from asymptotic statements (reported with compensated finite
statistics).  It does not use numerical agreement as a proof.
"""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import loggamma

from data_io import load_float64


TWOPI = 2.0 * np.pi
LIMIT = 0.77689426079325358 + 0.767855668864547j


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def rsiemann_clock(gamma: np.ndarray) -> np.ndarray:
    theta = np.imag(loggamma(0.25 + 0.5j * gamma)) - 0.5 * gamma * np.log(np.pi)
    return 1.0 + theta / np.pi


def montgomery_identity_check(gamma: np.ndarray, alpha: float = 0.65) -> tuple[float, float, float]:
    """Compare the pair sum with its exponentially smoothed trace integral."""
    sample = gamma[:192]
    height = sample[-1]
    frequency = alpha * np.log(height)
    difference = sample[:, None] - sample[None, :]
    direct = np.sum(
        np.exp(1j * frequency * difference) * 4.0 / (4.0 + difference * difference)
    ).real

    grid = np.linspace(-12.0, 12.0, 24001)
    integral_values = np.empty_like(grid)
    for left in range(0, grid.size, 1200):
        right = min(left + 1200, grid.size)
        trace = np.exp(1j * np.outer(frequency + grid[left:right], sample)).sum(axis=1)
        integral_values[left:right] = np.exp(-2.0 * np.abs(grid[left:right])) * np.abs(trace) ** 2
    integrated = float(np.trapezoid(integral_values, grid))
    return float(direct), integrated, abs(float(direct) - integrated)


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=root / "data" / "g_hp.bin")
    parser.add_argument(
        "--figure",
        type=Path,
        default=root / "figures" / "core_theorem_compatibility.png",
    )
    args = parser.parse_args()

    gamma = load_float64(args.input)
    count = gamma.size
    ordinal = np.arange(1, count + 1, dtype=np.float64)
    zero_based = ordinal - 1.0
    phase = np.exp(1j * gamma)
    walk = np.cumsum(phase)
    walk_energy_prefix = np.cumsum(np.abs(walk) ** 2)
    phase_prefix = np.cumsum(phase)
    ordinal_phase_prefix = np.cumsum(zero_based * phase)
    clock = rsiemann_clock(gamma)
    clock_phase_prefix = np.cumsum(clock * phase)

    sizes = np.unique(
        np.round(np.logspace(np.log10(300), np.log10(count), 72)).astype(int)
    )
    centroids = phase_prefix[sizes - 1] - ordinal_phase_prefix[sizes - 1] / sizes
    exact_clock = (
        phase_prefix[sizes - 1]
        + (0.5 * phase_prefix[sizes - 1] - clock_phase_prefix[sizes - 1]) / sizes
    )
    level_gap = np.abs(centroids - exact_clock)
    limit_gap = np.abs(centroids - LIMIT)
    energy = walk_energy_prefix[sizes - 1] / sizes
    trajectory_compensated = energy / np.log(sizes) ** 2
    triangular_remainder = np.abs(
        np.abs(centroids) ** 2 - abs(LIMIT) ** 2 - 1.0 / (6.0 * sizes)
    )

    inversion_errors: list[float] = []
    for frequency in (0.25, 0.5, 1.0, np.log(2.0), 2.0):
        current_phase = np.exp(1j * frequency * gamma)
        current_walk = np.cumsum(current_phase)
        current_A = np.cumsum(current_walk)
        first = np.diff(np.concatenate(([0.0j], current_A)))
        second = np.diff(np.concatenate(([0.0j], first)))
        inversion_errors.append(
            max(
                float(np.max(np.abs(first - current_walk))),
                float(np.max(np.abs(second - current_phase))),
            )
        )

    direct_size = 512
    weights = 1.0 - np.arange(direct_size, dtype=np.float64) / direct_size
    small_phase = phase[:direct_size]
    triangular_direct = 0.0
    trajectory_direct = 0.0
    for j in range(direct_size - 1):
        cosines = np.cos(gamma[j] - gamma[j + 1 : direct_size])
        triangular_direct += 2.0 * weights[j] * np.dot(weights[j + 1 :], cosines)
        trajectory_direct += 2.0 * np.dot(weights[j + 1 :], cosines)
    triangular_identity = abs(np.dot(weights, small_phase)) ** 2 - np.dot(weights, weights)
    small_walk = np.cumsum(small_phase)
    trajectory_energy = float(np.mean(np.abs(small_walk) ** 2))
    trajectory_identity = trajectory_energy - (direct_size + 1.0) / 2.0
    triangular_closure = abs(triangular_direct - triangular_identity)
    trajectory_closure = abs(trajectory_direct - trajectory_identity)

    pair_value, integral_value, montgomery_error = montgomery_identity_check(gamma)

    final_centroid = centroids[-1]
    final_clock = exact_clock[-1]
    print("Core theorem compatibility checks")
    print(f"input = data/{args.input.name}")
    print(f"input sha256 = {sha256(args.input)}")
    print(f"ordinates = {count}")
    print(f"ordinate range = [{gamma[0]:.12f}, {gamma[-1]:.12f}]")
    print()
    print("Level-one exact-clock reduction")
    print(f"C_N = {final_centroid.real:+.12f} {final_centroid.imag:+.12f}i")
    print(f"Q_N^(H) = {final_clock.real:+.12f} {final_clock.imag:+.12f}i")
    print(f"|C_N-Q_N^(H)| = {level_gap[-1]:.12e}")
    print(f"midpoint clock-defect sd = {np.std(ordinal - 0.5 - clock):.9f}")
    print()
    print("Conditional complex centroid limit")
    print(f"L = {LIMIT.real:+.15f} {LIMIT.imag:+.15f}i")
    print(f"|C_N-L| = {limit_gap[-1]:.12e}")
    print(f"Re(C_N-L) = {(final_centroid-LIMIT).real:+.12e}")
    print(f"Im(C_N-L) = {(final_centroid-LIMIT).imag:+.12e}")
    print()
    print("Pair identities at N=512 (direct O(N^2) sum versus closed form)")
    print(f"triangular pair closure error = {triangular_closure:.3e}")
    print(f"trajectory pair closure error = {trajectory_closure:.3e}")
    print(f"full-N triangular asymptotic remainder = {triangular_remainder[-1]:.9e}")
    print(f"full-N trajectory energy E_N = {energy[-1]:.9f}")
    print(f"full-N E_N/log(N)^2 = {trajectory_compensated[-1]:.9f}")
    print(f"full-N max_(n<=N)|S_n|/log(N) = {np.max(np.abs(walk))/np.log(count):.9f}")
    print()
    print("Centroid inversion finite-difference closure")
    for frequency, error in zip((0.25, 0.5, 1.0, np.log(2.0), 2.0), inversion_errors):
        print(f"u={frequency:.12f}: max closure error = {error:.3e}")
    print()
    print("Montgomery identity, N=192, alpha=0.65")
    print(f"direct weighted pair sum = {pair_value:.12f}")
    print(f"smoothed trace integral = {integral_value:.12f}")
    print(f"absolute quadrature discrepancy = {montgomery_error:.3e}")

    blue = "#0b6fa4"
    orange = "#c8681c"
    green = "#4a7c59"
    gray = "#8a8a8a"
    fig, axes = plt.subplots(2, 3, figsize=(13.0, 7.7), dpi=180)

    ax = axes[0, 0]
    ax.loglog(sizes, level_gap, color=blue, linewidth=1.2)
    ax.set_title("Level-one clock replacement", loc="left")
    ax.set_xlabel(r"$N$")
    ax.set_ylabel(r"$|C_N-Q_N^{(H)}|$")

    ax = axes[0, 1]
    ax.semilogx(sizes, centroids.real, color=blue, linewidth=1.1, label=r"$\Re C_N$")
    ax.semilogx(sizes, centroids.imag, color=green, linewidth=1.1, label=r"$\Im C_N$")
    ax.axhline(LIMIT.real, color=orange, linewidth=1.0, linestyle="--")
    ax.axhline(LIMIT.imag, color=orange, linewidth=1.0, linestyle="--")
    ax.set_title("Both centroid coordinates", loc="left")
    ax.set_xlabel(r"$N$")
    ax.legend(frameon=False, fontsize=8)

    ax = axes[0, 2]
    ax.loglog(sizes, triangular_remainder, color=blue, linewidth=1.1, label="triangular-pair remainder")
    ax.loglog(sizes, limit_gap, color=orange, linewidth=1.1, linestyle="--", label=r"$|C_N-L|$")
    ax.set_title("Pair cancellation forced by $C_N$", loc="left")
    ax.set_xlabel(r"$N$")
    ax.legend(frameon=False, fontsize=7.6)

    ax = axes[1, 0]
    ax.semilogx(sizes, energy, color=blue, linewidth=1.1, label=r"$\mathcal{E}_N$")
    ax.semilogx(sizes, np.log(sizes) ** 2, color=orange, linewidth=1.1, linestyle="--", label=r"$\log^2N$")
    ax.set_title("Trajectory-energy scale", loc="left")
    ax.set_xlabel(r"$N$")
    ax.legend(frameon=False, fontsize=8)

    ax = axes[1, 1]
    frequencies = np.array((0.25, 0.5, 1.0, np.log(2.0), 2.0))
    ax.semilogy(frequencies, np.maximum(inversion_errors, 1e-18), "o", color=blue)
    ax.set_title("Exact centroid inversion", loc="left")
    ax.set_xlabel(r"frequency $u$")
    ax.set_ylabel("max finite-difference error")

    ax = axes[1, 2]
    ax.bar([0, 1], [pair_value, integral_value], color=[blue, green], width=0.62)
    ax.set_xticks([0, 1], ["pair sum", "trace integral"])
    ax.set_title("Montgomery identity ($N=192$)", loc="left")
    ax.text(0.5, 0.04, f"$|\\Delta|={montgomery_error:.1e}$", transform=ax.transAxes, ha="center", fontsize=8)

    for ax in axes.ravel():
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color(gray)
        ax.spines["bottom"].set_color(gray)
        ax.grid(color="#ececec", linewidth=0.55)
        ax.tick_params(labelsize=8)

    fig.suptitle(
        "Numerical compatibility checks: exact closures and finite-height asymptotics",
        x=0.01,
        y=1.01,
        ha="left",
        fontsize=12.4,
    )
    fig.tight_layout()
    args.figure.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.figure, bbox_inches="tight", facecolor="white")
    print(f"figure = figures/{args.figure.name}")


if __name__ == "__main__":
    main()
