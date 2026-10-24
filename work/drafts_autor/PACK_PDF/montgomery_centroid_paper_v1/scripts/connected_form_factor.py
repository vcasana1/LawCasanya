#!/usr/bin/env python3
"""Connected Montgomery form factor from the supplied zeta ordinates.

The diagonal contribution is exactly one.  The off-diagonal part is computed
from a weighted histogram of normalized positive pair gaps and then cosine
transformed.  This avoids storing an N by N pair matrix while retaining the
Montgomery weight w(u)=4/(4+u^2).
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
        default=root / "figures" / "connected_form_factor.png",
    )
    parser.add_argument("--max-lag", type=int, default=500)
    parser.add_argument("--gap-bin", type=float, default=0.01)
    parser.add_argument("--alpha-step", type=float, default=0.01)
    args = parser.parse_args()

    gamma = load_float64(args.input)
    count = gamma.size
    height = float(gamma[-1])
    local_log = float(np.log(height / TWOPI))
    max_gap = args.max_lag + 8.0
    edges = np.arange(0.0, max_gap + args.gap_bin, args.gap_bin)
    weighted_histogram = np.zeros(edges.size - 1, dtype=np.float64)

    for lag in range(1, args.max_lag + 1):
        delta = gamma[lag:] - gamma[:-lag]
        normalized = local_log * delta / TWOPI
        weight = 4.0 / (4.0 + delta * delta)
        weighted_histogram += np.histogram(normalized, bins=edges, weights=weight)[0]

    centers = 0.5 * (edges[:-1] + edges[1:])
    alphas = np.arange(0.02, 4.0 + args.alpha_step * 0.5, args.alpha_step)
    off = np.empty_like(alphas)
    chunk = 40
    coefficient = 2.0 / count
    for left in range(0, alphas.size, chunk):
        right = min(left + chunk, alphas.size)
        cosine = np.cos(TWOPI * np.outer(alphas[left:right], centers))
        off[left:right] = coefficient * (cosine @ weighted_histogram)

    plateau = alphas >= 1.0
    plateau_rms = float(np.sqrt(np.mean(off[plateau] ** 2)))
    root_scale = float(local_log / np.sqrt(count))
    fitted_constant = plateau_rms / root_scale
    finite_target = np.where(
        alphas <= 1.0,
        np.exp(-2.0 * alphas * local_log) * local_log + alphas,
        1.0,
    )
    ramp_mask = (alphas >= 0.20) & (alphas <= 1.0)
    ramp_rmse = float(np.sqrt(np.mean(((1.0 + off[ramp_mask]) - finite_target[ramp_mask]) ** 2)))

    scaling_rows: list[tuple[int, float, float, float]] = []
    scale_alphas = np.arange(1.0, 4.001, 0.02)
    for fraction in (0.125, 0.25, 0.5, 1.0):
        sub_count = int(round(count * fraction))
        sub_gamma = gamma[:sub_count]
        sub_height = float(sub_gamma[-1])
        sub_log = float(np.log(sub_height / TWOPI))
        sub_edges = np.arange(0.0, args.max_lag + 8.0 + args.gap_bin, args.gap_bin)
        sub_hist = np.zeros(sub_edges.size - 1, dtype=np.float64)
        for lag in range(1, min(args.max_lag, sub_count - 1) + 1):
            delta = sub_gamma[lag:] - sub_gamma[:-lag]
            normalized = sub_log * delta / TWOPI
            weight = 4.0 / (4.0 + delta * delta)
            sub_hist += np.histogram(normalized, bins=sub_edges, weights=weight)[0]
        sub_centers = 0.5 * (sub_edges[:-1] + sub_edges[1:])
        sub_off = np.empty_like(scale_alphas)
        for left in range(0, scale_alphas.size, chunk):
            right = min(left + chunk, scale_alphas.size)
            cosine = np.cos(TWOPI * np.outer(scale_alphas[left:right], sub_centers))
            sub_off[left:right] = (2.0 / sub_count) * (cosine @ sub_hist)
        sub_rms = float(np.sqrt(np.mean(sub_off**2)))
        scaling_rows.append((sub_count, sub_log, sub_rms, sub_rms * np.sqrt(sub_count) / sub_log))

    print("Connected Montgomery form factor")
    print(f"input = data/{args.input.name}")
    print(f"input sha256 = {file_sha256(args.input)}")
    print(f"ordinates = {count}")
    print(f"terminal height = {height:.12f}")
    print(f"log(T/(2*pi)) = {local_log:.9f}")
    print(f"max ordinal lag = {args.max_lag}")
    print(f"normalized-gap bin width = {args.gap_bin:.4f}")
    print(f"plateau RMS of Off(alpha), 1<=alpha<=4 = {plateau_rms:.6f}")
    print(f"log(T/(2*pi))/sqrt(N) = {root_scale:.6f}")
    print(f"plateau RMS coefficient = {fitted_constant:.4f}")
    print(f"finite-ramp RMSE, 0.2<=alpha<=1 = {ramp_rmse:.6f}")
    print("selected values:")
    print("  alpha        Off(alpha)       F(alpha)")
    for alpha in (0.10, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 2.00, 3.00, 4.00):
        index = int(np.argmin(np.abs(alphas - alpha)))
        print(f"  {alpha:4.2f}        {off[index]:+10.6f}      {1.0 + off[index]:10.6f}")
    print("plateau scaling over prefix tables:")
    print("  N        log(T/(2*pi))      RMS Off       RMS*sqrt(N)/log")
    for sub_count, sub_log, sub_rms, coefficient_row in scaling_rows:
        print(f"  {sub_count:6d}       {sub_log:10.6f}      {sub_rms:9.6f}          {coefficient_row:8.4f}")

    blue = "#0b6fa4"
    orange = "#c8681c"
    gray = "#8a8a8a"
    fig, axes = plt.subplots(1, 3, figsize=(14.4, 4.7), dpi=180)

    ax = axes[0]
    ax.plot(alphas, 1.0 + off, color=blue, linewidth=1.25, label="computed $F_T$")
    ax.plot(alphas, finite_target, color=orange, linewidth=1.25, linestyle="--", label="ramp / plateau target")
    ax.axvline(1.0, color=orange, linewidth=1.0, linestyle="--")
    ax.text(1.03, 0.80 * np.max(1.0 + off), r"$\alpha=1$", color=orange, fontsize=9)
    ax.set_xlim(0.0, 4.05)
    ax.set_xlabel(r"$\alpha$")
    ax.set_ylabel(r"$F_T(\alpha)$")
    ax.set_title("Ramp and plateau on one scale", loc="left")
    ax.legend(frameon=False, fontsize=7.8)

    ax = axes[1]
    ax.plot(alphas[plateau], off[plateau], color=blue, linewidth=1.25, label=r"$\mathrm{Off}(\alpha)$")
    envelope = fitted_constant * root_scale
    ax.axhline(envelope, color=orange, linewidth=1.0, linestyle="--")
    ax.axhline(-envelope, color=orange, linewidth=1.0, linestyle="--", label=rf"$\pm {fitted_constant:.2f}L_T/\sqrt{{N}}$")
    ax.axhline(0.0, color=gray, linewidth=0.8)
    ax.set_xlim(1.0, 4.05)
    bound = max(0.09, 1.15 * float(np.max(np.abs(off[plateau]))))
    ax.set_ylim(-bound, bound)
    ax.set_xlabel(r"$\alpha$")
    ax.set_title("Expanded plateau: root-scale fluctuations", loc="left")
    ax.legend(frameon=False, fontsize=8.5)

    ax = axes[2]
    scale_n = np.array([row[0] for row in scaling_rows], dtype=float)
    scale_coeff = np.array([row[3] for row in scaling_rows])
    ax.semilogx(scale_n, scale_coeff, "o-", color=blue, linewidth=1.15, markersize=4)
    ax.axhline(np.mean(scale_coeff), color=orange, linewidth=1.0, linestyle="--")
    ax.set_xlabel(r"prefix size $N$")
    ax.set_ylabel(r"RMS$(\mathrm{Off})\sqrt{N}/L_T$")
    ax.set_title("Finite-height root-scale check", loc="left")

    for ax in axes:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color(gray)
        ax.spines["bottom"].set_color(gray)
        ax.grid(color="#ececec", linewidth=0.6)

    fig.suptitle(
        f"Connected form factor from {count:,} zeta ordinates: diagonal = 1 exactly",
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
