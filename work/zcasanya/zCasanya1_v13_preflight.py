#!/usr/bin/env python3
"""Finite-height preflight for Theorem 8.10; never reads true-zero data."""

from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parent
N_EXPECTED = 2_001_052


def guard(event, args):
    if event == "open" and args and "zeross" in str(args[0]).lower():
        raise PermissionError("The v13 preflight must not open true-zero data")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(8 * 1024**2), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    sys.addaudithook(guard)
    clock_path = ROOT / "inputs" / "zLamb.bin"
    prime_path = ROOT / "inputs" / "primoss.bin"
    tex_path = ROOT / "source" / "ordinal_prime_cutoff_v13.tex"
    zip_path = ROOT / "source" / "ordinal_prime_cutoff_v13.zip"

    tau = np.fromfile(clock_path, dtype="<f8")
    if len(tau) != N_EXPECTED or not np.all(np.isfinite(tau)) or not np.all(np.diff(tau) > 0):
        raise ValueError("Unexpected zLamb.bin")

    block_exponents = np.floor(np.log2(tau)).astype(int)
    blocks = []
    for exponent in np.unique(block_exponents):
        height = 2.0 ** int(exponent)
        h0 = math.log(math.log(height))
        h1 = math.log(h0) if h0 > 0 else math.nan
        c1 = h0 ** -0.5 if h0 > 0 else math.nan
        c2 = h1 ** -0.5 if h1 > 0 else math.nan
        blocks.append(
            {
                "T": height,
                "records_by_tau_block": int(np.sum(block_exponents == exponent)),
                "H0": h0,
                "H1": h1 if math.isfinite(h1) else None,
                "c1": c1 if math.isfinite(c1) else None,
                "c2": c2 if math.isfinite(c2) else None,
                "T_to_1_over_160": height ** (1 / 160),
                "higher_moment_cutoff_interval_nonempty_r1": height ** (1 / 160) >= 2,
                "theorem_8_9_c1_at_most_half": c1 <= 0.5,
                "theorem_8_9_c2_at_most_half": bool(math.isfinite(c2) and c2 <= 0.5),
            }
        )

    hstar_lower = 160**2 * 4
    result = {
        "construction_inputs_opened": ["zLamb.bin", "primoss.bin"],
        "true_zero_input_opened": False,
        "records": len(tau),
        "tau_first": float(tau[0]),
        "tau_last": float(tau[-1]),
        "hashes": {
            "zLamb.bin": sha256(clock_path),
            "primoss.bin": sha256(prime_path),
            "ordinal_prime_cutoff_v13.tex": sha256(tex_path),
            "ordinal_prime_cutoff_v13.zip": sha256(zip_path),
        },
        "literal_conditions": {
            "higher_moment_range": "2 <= X <= T^(1/(160 r))",
            "minimum_T_for_nonempty_range_at_r_1": "2^160",
            "minimum_T_for_c1_at_most_half": "exp(exp(4))",
            "Hstar_proved_lower_bound": hstar_lower,
            "minimum_T_for_one_nonempty_uniform_iteration_from_Hstar": "exp(exp(Hstar))",
            "log10_log10_of_that_minimum_using_Hstar_102400": hstar_lower / math.log(10) - math.log10(math.log(10)),
        },
        "observed_maxima": {
            "max_H0": max(row["H0"] for row in blocks),
            "max_T_to_1_over_160": max(row["T_to_1_over_160"] for row in blocks),
            "all_higher_moment_ranges_empty_at_r1": all(not row["higher_moment_cutoff_interval_nonempty_r1"] for row in blocks),
            "all_c1_exceed_half": all(not row["theorem_8_9_c1_at_most_half"] for row in blocks),
            "all_c2_invalid_or_exceed_half": all(not row["theorem_8_9_c2_at_most_half"] for row in blocks),
        },
        "dyadic_blocks_based_only_on_tau_for_diagnostic_purposes": blocks,
        "conclusion": "Theorem 8.10 has no nontrivial numerically admissible step on this height range, and its constants do not determine a unique finite-height extension.",
    }
    destination = ROOT / "zCasanya1_v13_preflight.json"
    destination.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps(result["observed_maxima"], indent=2))
    print(destination)


if __name__ == "__main__":
    main()
