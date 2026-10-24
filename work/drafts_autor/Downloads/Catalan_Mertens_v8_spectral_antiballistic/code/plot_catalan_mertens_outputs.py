#!/usr/bin/env python3
"""Create publication PNGs from the archived moment and excursion outputs."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--moments", type=Path, required=True)
    parser.add_argument("--excursions", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    moment_data = json.loads(args.moments.read_text(encoding="utf-8"))
    records = moment_data["moments"]
    k = np.array([row["k"] for row in records])
    iid = np.array([row["B_k_over_iid_leading"] for row in records])
    budget = np.array([row["B_k_over_Lambda_k"] for row in records])

    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.0), constrained_layout=True)
    axes[0].semilogy(k, iid, "o-", color="#1967ad")
    axes[0].set_xlabel("moment order k")
    axes[0].set_ylabel(r"$\mathcal{B}_k^{\#}$/simple-walk leading moment")
    axes[0].set_title("Compressed Mertens moment ratios")
    axes[0].grid(alpha=0.25, which="both")
    axes[1].plot(k, budget, "o-", color="#c43c39")
    axes[1].set_xlabel("moment order k")
    axes[1].set_ylabel(r"$\mathcal{B}_k^{\#}/\Lambda_k$")
    axes[1].set_ylim(0.0, max(0.45, 1.08 * budget.max()))
    axes[1].set_title("Observed excursion-budget ratio")
    axes[1].grid(alpha=0.25)
    fig.savefig(args.output_dir / "moment_ratios.png", dpi=220)
    plt.close(fig)

    gaps: list[int] = []
    scaled: list[float] = []
    with args.excursions.open(newline="") as handle:
        for row in csv.DictReader(handle):
            gaps.append(int(row["Gap"]))
            scaled.append(float(row["HeightOverSqrtGap"]))
    gap = np.asarray(gaps, dtype=np.float64)
    height_scaled = np.asarray(scaled, dtype=np.float64)
    ordered = np.sort(gap)
    ccdf = (ordered.size - np.arange(ordered.size)) / ordered.size

    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.0), constrained_layout=True)
    axes[0].scatter(gap, height_scaled, s=5, alpha=0.18, color="#1967ad", edgecolors="none")
    axes[0].set_xscale("log")
    axes[0].set_xlabel("compressed excursion length L")
    axes[0].set_ylabel(r"$H/\sqrt{L}$")
    axes[0].set_title("Height across excursion scales")
    axes[0].grid(alpha=0.2, which="both")
    axes[1].loglog(ordered, ccdf, color="#c43c39", lw=1.2)
    axes[1].set_xlabel("compressed gap L")
    axes[1].set_ylabel(r"empirical $\Pr(\mathrm{Gap}\geq L)$")
    axes[1].set_title("Heavy-tailed return gaps")
    axes[1].grid(alpha=0.2, which="both")
    fig.savefig(args.output_dir / "excursion_geometry.png", dpi=220)
    plt.close(fig)

    print(args.output_dir / "moment_ratios.png")
    print(args.output_dir / "excursion_geometry.png")


if __name__ == "__main__":
    main()
