#!/usr/bin/env python3
"""Finite audits for the exact Version 8 identities.

This program checks algebraic/combinatorial statements only.  It does not
test the open arithmetic power-saving conjecture and it uses no Mobius data.
"""

from __future__ import annotations

import argparse
import csv
import itertools
import json
import math
from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def occupation_kernel(h: int) -> tuple[np.ndarray, np.ndarray]:
    j = np.tril(np.ones((h, h), dtype=float))
    return j, j.T @ j


def closed_spectrum(h: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    k = np.arange(1, h + 1, dtype=float)
    theta = (2 * k - 1) * np.pi / (2 * h + 1)
    eigenvalues = 1.0 / (4.0 * np.sin(theta / 2.0) ** 2)
    n = np.arange(1, h + 1, dtype=float)[:, None]
    vectors = 2.0 / np.sqrt(2 * h + 1) * np.sin((h + 1 - n) * theta)
    return theta, eigenvalues, vectors


def spectrum_audit(h_values: list[int]) -> dict:
    records = []
    for h in h_values:
        j, kernel = occupation_kernel(h)
        theta, lam, vectors = closed_spectrum(h)
        numerical = np.linalg.eigvalsh(kernel)[::-1]
        rng = np.random.default_rng(1701 + h)
        a = rng.choice([-1.0, 0.0, 1.0], size=h)
        energy_direct = float(np.dot(j @ a, j @ a))
        coeff = vectors.T @ a
        energy_spectral = float(np.sum(lam * coeff**2))

        n = np.arange(1, h + 1, dtype=float)
        twists = np.array(
            [np.sum(a * np.exp(-1j * th * n)) for th in theta],
            dtype=complex,
        )
        coeff_from_twist = 2.0 / np.sqrt(2 * h + 1) * np.imag(
            np.exp(1j * (h + 1) * theta) * twists
        )
        finite_twist_rhs = (
            2.0 * h * (h + 1) / (2 * h + 1) * np.max(np.abs(twists)) ** 2
        )
        records.append(
            {
                "H": h,
                "kernel_formula_error": float(
                    np.max(
                        np.abs(
                            kernel
                            - np.fromfunction(
                                lambda r, s: h - np.maximum(r, s), (h, h)
                            )
                        )
                    )
                ),
                "orthonormality_error": float(
                    np.max(np.abs(vectors.T @ vectors - np.eye(h)))
                ),
                "eigen_equation_error": float(
                    np.max(np.abs(kernel @ vectors - vectors * lam))
                ),
                "eigenvalue_error": float(np.max(np.abs(numerical - lam))),
                "energy_reconstruction_error": abs(
                    energy_direct - energy_spectral
                ),
                "twist_coefficient_error": float(
                    np.max(np.abs(coeff - coeff_from_twist))
                ),
                "energy_over_finite_twist_bound": (
                    energy_direct / finite_twist_rhs if finite_twist_rhs else 0.0
                ),
            }
        )
    return {"records": records}


def shifted_dilation_audit() -> dict:
    rng = np.random.default_rng(8128)
    records = []
    for p in [2, 3, 5, 11, 17]:
        for length in [3, 8, 15]:
            for residue in range(min(p, 4)):
                ell = 1 + ((3 * length + residue) % p)
                b = rng.choice([-1.0, 1.0], size=length)
                h = residue + p * (length - 1) + ell
                lifted = np.zeros(h)
                lifted[residue + p * np.arange(length)] = b
                lhs = float(np.sum(np.cumsum(lifted) ** 2))
                child = float(np.sum(np.cumsum(b) ** 2))
                endpoint = float(np.sum(b) ** 2)
                rhs = p * child - (p - ell) * endpoint
                records.append(abs(lhs - rhs))
    return {
        "cases": len(records),
        "maximum_identity_error": float(max(records)),
    }


def high_mode_audit(h: int = 128) -> dict:
    rng = np.random.default_rng(314159)
    _, lam, vectors = closed_spectrum(h)
    worst_ratio = 0.0
    cases = 0
    for _ in range(40):
        a = rng.choice([-1.0, 1.0], size=h)
        coeff = vectors.T @ a
        norm2 = float(np.dot(a, a))
        for cutoff in [2, 4, 8, 16, 32, 64]:
            tail = float(np.sum(lam[cutoff:] * coeff[cutoff:] ** 2))
            exact_bound = float(lam[cutoff] * norm2)
            worst_ratio = max(worst_ratio, tail / exact_bound)
            cases += 1
    return {
        "H": h,
        "cases": cases,
        "maximum_tail_over_lambda_Kplus1_norm2": worst_ratio,
    }


def abstract_frame_counterexample(h: int = 24000) -> dict:
    r_values = [2, 4, 8, 16, 32, 48]
    ratios = []
    d0 = 170
    n = np.arange(1, h + 1)
    for channels in r_values:
        lifted = []
        for d in range(d0, d0 + channels):
            lifted.append(np.cumsum((n % d == 0).astype(float)))
        matrix = np.vstack(lifted)
        numerator = float(np.sum(np.sum(matrix, axis=0) ** 2))
        denominator = float(np.sum(matrix**2))
        ratios.append(numerator / denominator)
    return {"H": h, "channels": r_values, "ratios": ratios}


def narayana(n: int, k: int) -> int:
    if not (1 <= k <= n):
        return 0
    return math.comb(n, k) * math.comb(n, k - 1) // n


def dyck_paths(n: int):
    for up_positions in itertools.combinations(range(2 * n), n):
        up = set(up_positions)
        steps = tuple(1 if j in up else -1 for j in range(2 * n))
        heights = np.cumsum(steps)
        if np.min(heights) >= 0 and heights[-1] == 0:
            yield steps, heights


def narayana_audit(max_n: int = 8) -> dict:
    records = []
    max_identity_error = 0.0
    for n in range(1, max_n + 1):
        all_counts: dict[int, int] = {}
        primitive_counts: dict[int, int] = {}
        for steps, heights in dyck_paths(n):
            peaks = sum(
                steps[j] == 1 and steps[j + 1] == -1
                for j in range(2 * n - 1)
            )
            local_formula = (
                2 * n + 1
                - sum(steps[j] * steps[j + 1] for j in range(2 * n - 1))
            ) / 4
            max_identity_error = max(max_identity_error, abs(peaks - local_formula))
            all_counts[peaks] = all_counts.get(peaks, 0) + 1
            if n == 1 or np.min(heights[:-1]) > 0:
                primitive_counts[peaks] = primitive_counts.get(peaks, 0) + 1
        expected_all = {k: narayana(n, k) for k in range(1, n + 1)}
        if n == 1:
            expected_primitive = {1: 1}
        else:
            expected_primitive = {
                k: narayana(n - 1, k) for k in range(1, n)
            }
        records.append(
            {
                "n": n,
                "all_counts": all_counts,
                "expected_all": expected_all,
                "primitive_counts": primitive_counts,
                "expected_primitive": expected_primitive,
                "all_distribution_pass": all_counts == expected_all,
                "primitive_distribution_pass": (
                    primitive_counts == expected_primitive
                ),
            }
        )
    return {
        "maximum_peak_identity_error": max_identity_error,
        "records": records,
    }


def return_local_time_audit(excursions_csv: Path, moment_json: Path) -> dict:
    end_m = []
    return_index = []
    gaps = []
    signs = []
    with excursions_csv.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            return_index.append(int(row["Return"]))
            end_m.append(int(row["End_m"]))
            gaps.append(int(row["Gap"]))
            signs.append(int(row["ExcursionSign"]))
    moment = json.loads(moment_json.read_text(encoding="utf-8"))
    total_m = int(moment["compressed_steps"])
    total_returns = int(moment["returns_to_zero"])
    iid_constant = math.sqrt(2.0 / math.pi)
    ratio = total_returns / math.sqrt(total_m)
    factor = ratio / iid_constant
    asymptotic_half_normal_tail = math.erfc(ratio / math.sqrt(2.0))
    flips = sum(signs[j] != signs[j - 1] for j in range(1, len(signs)))
    targets = [
        10**3,
        10**4,
        10**5,
        10**6,
        10**7,
        5 * 10**7,
        10**8,
        2 * 10**8,
        total_m,
    ]
    scale_table = []
    cursor = 0
    for target in targets:
        while cursor < len(end_m) and end_m[cursor] <= target:
            cursor += 1
        returns = cursor
        local_ratio = returns / math.sqrt(target)
        scale_table.append(
            {
                "m": target,
                "returns": returns,
                "R_over_sqrt_m": local_ratio,
                "factor_over_iid_mean": local_ratio / iid_constant,
            }
        )
    gap_survival_table = []
    for threshold in [2, 10, 100, 1000, 10_000, 100_000, 1_000_000, 10_000_000]:
        empirical = sum(gap > threshold for gap in gaps) / len(gaps)
        iid_asymptotic = math.sqrt(2.0 / (math.pi * threshold))
        gap_survival_table.append(
            {
                "threshold": threshold,
                "empirical_survival": empirical,
                "iid_asymptotic": iid_asymptotic,
                "ratio": empirical / iid_asymptotic,
            }
        )
    return {
        "compressed_steps": total_m,
        "returns": total_returns,
        "last_return_compressed": end_m[-1],
        "R_over_sqrt_m": ratio,
        "iid_mean_constant": iid_constant,
        "factor_over_iid_mean": factor,
        "half_normal_limit_tail_at_observed_ratio": asymptotic_half_normal_tail,
        "gap_2_count": sum(gap == 2 for gap in gaps),
        "gap_2_fraction": sum(gap == 2 for gap in gaps) / len(gaps),
        "gap_at_most_20_fraction": sum(gap <= 20 for gap in gaps) / len(gaps),
        "sign_flips": flips,
        "sign_flip_fraction": flips / (len(signs) - 1),
        "scale_table": scale_table,
        "gap_survival_table": gap_survival_table,
        "return_end_m": end_m,
        "return_index": return_index,
    }


def make_figure(report: dict, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(2, 2, figsize=(12.8, 9.0))
    axes = axes.ravel()

    h = 96
    _, lam, _ = closed_spectrum(h)
    _, kernel = occupation_kernel(h)
    numerical = np.linalg.eigvalsh(kernel)[::-1]
    axes[0].loglog(range(1, h + 1), lam, lw=2.2, label="closed form")
    axes[0].scatter(range(1, h + 1), numerical, s=10, label="numeric")
    axes[0].set_title(r"Exact spectrum of $J^*J$")
    axes[0].set_xlabel("mode k")
    axes[0].set_ylabel(r"$\lambda_k$")
    axes[0].legend(frameon=False)

    counter = report["abstract_frame_counterexample"]
    axes[1].plot(counter["channels"], counter["ratios"], "o-", lw=2.2)
    axes[1].plot(counter["channels"], counter["channels"], "--", alpha=0.6)
    axes[1].set_title("Abstract frame obstruction")
    axes[1].set_xlabel("number of positive channels R")
    axes[1].set_ylabel("combined / diagonal energy")

    record = report["narayana"]["records"][6]
    ks = sorted(int(k) for k in record["all_counts"])
    observed = [record["all_counts"][str(k)] for k in ks]
    expected = [record["expected_all"][str(k)] for k in ks]
    axes[2].bar(np.array(ks) - 0.17, observed, width=0.34, label="enumerated")
    axes[2].bar(np.array(ks) + 0.17, expected, width=0.34, label="Narayana")
    axes[2].set_title("Dyck peaks, semilength 7")
    axes[2].set_xlabel("number of peaks")
    axes[2].set_ylabel("paths")
    axes[2].legend(frameon=False)

    local = report["return_local_time"]
    end_m = np.asarray(local["return_end_m"], dtype=float)
    return_index = np.asarray(local["return_index"], dtype=float)
    factor_curve = return_index / np.sqrt(end_m) / local["iid_mean_constant"]
    axes[3].semilogx(end_m, factor_curve, lw=1.25, color="#7137a8")
    axes[3].axhline(1.0, color="black", ls="--", lw=1.2, label="iid mean")
    axes[3].scatter(
        [local["compressed_steps"]],
        [local["factor_over_iid_mean"]],
        color="#d24b40",
        zorder=5,
        label="full cutoff",
    )
    axes[3].set_title("Catalan return local time")
    axes[3].set_xlabel("compressed time m")
    axes[3].set_ylabel(r"$R(m)/\sqrt{2m/\pi}$")
    axes[3].legend(frameon=False)

    fig.suptitle("Version 8 finite identity audit (not arithmetic evidence)")
    fig.tight_layout()
    fig.savefig(output, dpi=190, bbox_inches="tight")
    plt.close(fig)


def make_local_time_figure(report: dict, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    local = report["return_local_time"]
    end_m = np.asarray(local["return_end_m"], dtype=float)
    return_index = np.asarray(local["return_index"], dtype=float)
    factor_curve = return_index / np.sqrt(end_m) / local["iid_mean_constant"]
    fig, ax = plt.subplots(figsize=(9.4, 5.2))
    ax.semilogx(end_m, factor_curve, lw=1.45, color="#7137a8")
    ax.axhline(1.0, color="black", ls="--", lw=1.2, label="iid mean")
    ax.scatter(
        [local["compressed_steps"]],
        [local["factor_over_iid_mean"]],
        s=58,
        color="#d24b40",
        zorder=5,
        label=f"full cutoff: {local['factor_over_iid_mean']:.4f}",
    )
    ax.set_title("Compressed Mertens return local time")
    ax.set_xlabel("compressed time m")
    ax.set_ylabel(r"$R(m)/\sqrt{2m/\pi}$")
    ax.legend(frameon=False)
    ax.grid(alpha=0.18)
    fig.tight_layout()
    fig.savefig(output, dpi=200, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output-json",
        type=Path,
        default=Path("outputs/jstarj_antiballistic_audit_v8.json"),
    )
    parser.add_argument(
        "--output-png",
        type=Path,
        default=Path("outputs/jstarj_antiballistic_audit_v8.png"),
    )
    parser.add_argument(
        "--excursions-csv",
        type=Path,
        default=Path("outputs/mertens_excursiones_alturas.csv"),
    )
    parser.add_argument(
        "--moment-json",
        type=Path,
        default=Path("outputs/moment_audit.json"),
    )
    parser.add_argument(
        "--output-localtime-png",
        type=Path,
        default=Path("outputs/catalan_return_factor4_v8.png"),
    )
    args = parser.parse_args()

    report = {
        "scope": (
            "Finite checks of exact identities only; no test of the open "
            "Mobius power-saving estimate."
        ),
        "spectrum": spectrum_audit([3, 8, 17, 41, 96]),
        "shifted_dilation": shifted_dilation_audit(),
        "high_mode_tail": high_mode_audit(),
        "abstract_frame_counterexample": abstract_frame_counterexample(),
        "narayana": narayana_audit(),
        "return_local_time": return_local_time_audit(
            args.excursions_csv, args.moment_json
        ),
    }
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(report, indent=2), encoding="utf-8")
    # Reloading normalizes integer dictionary keys to strings for plotting.
    normalized = json.loads(args.output_json.read_text(encoding="utf-8"))
    make_figure(normalized, args.output_png)
    make_local_time_figure(normalized, args.output_localtime_png)

    spectrum_records = report["spectrum"]["records"]
    print("V8 exact-identity audit")
    print("max eigenvalue error:", max(r["eigenvalue_error"] for r in spectrum_records))
    print("max dilation error:", report["shifted_dilation"]["maximum_identity_error"])
    print("high-mode inequality ratio:", report["high_mode_tail"]["maximum_tail_over_lambda_Kplus1_norm2"])
    print("Narayana identities pass:", all(r["all_distribution_pass"] and r["primitive_distribution_pass"] for r in report["narayana"]["records"]))
    print("return factor over iid mean:", report["return_local_time"]["factor_over_iid_mean"])
    print("wrote", args.output_json)
    print("wrote", args.output_png)
    print("wrote", args.output_localtime_png)


if __name__ == "__main__":
    main()
