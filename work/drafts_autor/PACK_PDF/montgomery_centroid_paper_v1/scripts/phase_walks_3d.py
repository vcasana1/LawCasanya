#!/usr/bin/env python3
"""Same-scale 3D point clouds for zeta/RVM walks and two residual walks."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import lambertw

from data_io import load_float64


TWOPI = 2.0 * np.pi


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def lambert_levels(count: int) -> np.ndarray:
    ordinal = np.arange(1, count + 1, dtype=np.float64)
    argument = (ordinal - 11.0 / 8.0) / np.e
    tau = TWOPI * (ordinal - 11.0 / 8.0) / np.real(lambertw(argument, 0))
    tau = tau.astype(np.longdouble)
    target = ordinal.astype(np.longdouble) - np.longdouble(0.5)
    two_pi = np.longdouble(2.0) * np.longdouble(np.pi)
    for _ in range(5):
        value = (
            (tau / two_pi) * np.log(tau / (two_pi * np.e))
            + np.longdouble(7.0 / 8.0)
            - target
        )
        derivative = np.log(tau / two_pi) / two_pi
        tau -= value / derivative
    return tau.astype(np.float64)


def common_limits(first: np.ndarray, second: np.ndarray, padding: float = 0.06) -> tuple[float, float, float, float]:
    real_min = float(min(np.min(first.real), np.min(second.real)))
    real_max = float(max(np.max(first.real), np.max(second.real)))
    imag_min = float(min(np.min(first.imag), np.min(second.imag)))
    imag_max = float(max(np.max(first.imag), np.max(second.imag)))
    real_pad = padding * max(real_max - real_min, 1.0)
    imag_pad = padding * max(imag_max - imag_min, 1.0)
    return real_min - real_pad, real_max + real_pad, imag_min - imag_pad, imag_max + imag_pad


def plot_pair(
    first: np.ndarray,
    second: np.ndarray,
    first_title: str,
    second_title: str,
    suptitle: str,
    output: Path,
    sample: np.ndarray,
) -> tuple[float, float, float, float]:
    limits = common_limits(first, second)
    colors = np.linspace(0.0, 1.0, sample.size)
    x_axis = (sample + 1) / first.size
    fig = plt.figure(figsize=(12.0, 5.2), dpi=180)
    axes = [fig.add_subplot(1, 2, 1, projection="3d"), fig.add_subplot(1, 2, 2, projection="3d")]

    for axis, values, title in zip(axes, (first, second), (first_title, second_title)):
        axis.scatter(
            x_axis,
            values.real[sample],
            values.imag[sample],
            c=colors,
            cmap="viridis",
            s=2.3,
            alpha=0.72,
            linewidths=0,
            rasterized=True,
        )
        centroid = np.mean(values)
        axis.scatter(
            [0.5],
            [centroid.real],
            [centroid.imag],
            color="#c8681c",
            marker="X",
            s=55,
            depthshade=False,
        )
        axis.set_xlim(0.0, 1.0)
        axis.set_ylim(limits[0], limits[1])
        axis.set_zlim(limits[2], limits[3])
        axis.set_xlabel(r"ordinal fraction $n/N$", labelpad=7)
        axis.set_ylabel(r"$\Re$ cumulative walk", labelpad=7)
        axis.set_zlabel(r"$\Im$ cumulative walk", labelpad=7)
        axis.set_title(title, loc="left", pad=10)
        axis.view_init(elev=24, azim=-57)
        axis.grid(True, linewidth=0.35, alpha=0.5)

    fig.suptitle(suptitle, x=0.02, y=1.01, ha="left", fontsize=12.2)
    fig.tight_layout()
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return limits


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=root / "data" / "g_hp.bin")
    parser.add_argument("--points", type=int, default=4500)
    args = parser.parse_args()

    gamma = load_float64(args.input)
    tau = lambert_levels(gamma.size)
    zeta_phase = np.exp(1j * gamma)
    rvm_phase = np.exp(1j * tau)
    epsilon = gamma - tau

    zeta_walk = np.cumsum(zeta_phase)
    rvm_walk = np.cumsum(rvm_phase)
    paired_walk = np.cumsum(zeta_phase - rvm_phase)
    intrinsic_walk = np.cumsum(np.exp(1j * epsilon) - 1.0)

    sample = np.unique(
        np.round(np.linspace(0, gamma.size - 1, min(args.points, gamma.size))).astype(int)
    )
    walk_output = root / "figures" / "zeta_rvm_walks_3d_same_scale.png"
    residual_output = root / "figures" / "residual_walks_3d_same_scale.png"
    walk_limits = plot_pair(
        zeta_walk,
        rvm_walk,
        "Zeta-zero exponential walk",
        "Lambert--RVM carrier walk",
        "Zeta and RVM cumulative phase clouds on identical axes",
        walk_output,
        sample,
    )
    residual_limits = plot_pair(
        paired_walk,
        intrinsic_walk,
        r"Paired phase residual $e^{i\gamma_k}-e^{i\tau_k}$",
        r"Intrinsic residual $e^{i(\gamma_k-\tau_k)}-1$",
        "Two residual cumulative clouds on identical axes",
        residual_output,
        sample,
    )

    rvm_residual = (
        (tau / TWOPI) * np.log(tau / (TWOPI * np.e))
        + 7.0 / 8.0
        - (np.arange(1, gamma.size + 1) - 0.5)
    )
    print("Same-scale 3D phase-walk clouds")
    print(f"input = data/{args.input.name}")
    print(f"input sha256 = {file_sha256(args.input)}")
    print(f"ordinates = {gamma.size}")
    print(f"sampled points per panel = {sample.size}")
    print(f"max |M(tau_k)-(k-1/2)| = {np.max(np.abs(rvm_residual)):.3e}")
    print(f"zeta walk centroid = {np.mean(zeta_walk).real:+.12f} {np.mean(zeta_walk).imag:+.12f}i")
    print(f"RVM walk centroid = {np.mean(rvm_walk).real:+.12f} {np.mean(rvm_walk).imag:+.12f}i")
    print(f"paired-residual walk centroid = {np.mean(paired_walk).real:+.12f} {np.mean(paired_walk).imag:+.12f}i")
    print(f"intrinsic-residual walk centroid = {np.mean(intrinsic_walk).real:+.12f} {np.mean(intrinsic_walk).imag:+.12f}i")
    print(
        "walk common limits (Re_min, Re_max, Im_min, Im_max) = "
        + " ".join(f"{value:+.6f}" for value in walk_limits)
    )
    print(
        "residual common limits (Re_min, Re_max, Im_min, Im_max) = "
        + " ".join(f"{value:+.6f}" for value in residual_limits)
    )
    print(f"figure = figures/{walk_output.name}")
    print(f"figure = figures/{residual_output.name}")


if __name__ == "__main__":
    main()
