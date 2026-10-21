#!/usr/bin/env python3
"""Casanya c667 isotonic post-processing, without zeta zeros or extra primes.

Given the existing c667 ordinates x[k] and Lambert/RvM ordinates tau[k],
compute the unique Euclidean projection

  min_y sum_k (y[k]-x[k])**2
  subject to y[k+1]-y[k] >= alpha*(tau[k+1]-tau[k]).

Set u=x-alpha*tau, apply weighted pool-adjacent-violators (PAV) to make
u nondecreasing, then return y=u_projected+alpha*tau.

This is a separate post-processing method (M3-mono), NOT a new
prime-phase calculation and NOT the v17 continuation method.
No true zeros or zeta evaluation enter this script.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

import numpy as np


def load_f64(path: Path) -> np.ndarray:
    if not path.is_file():
        raise FileNotFoundError(path)
    if path.stat().st_size % 8:
        raise ValueError(f"{path} is not a float64 binary")
    return np.fromfile(path, dtype="<f8")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def isotonic_project(x: np.ndarray, tau: np.ndarray, alpha: float) -> np.ndarray:
    """Unweighted, full-array, O(n) PAV; no sorting or oracle access."""
    x = np.asarray(x, dtype=np.float64).reshape(-1)
    tau = np.asarray(tau, dtype=np.float64).reshape(-1)
    if len(x) != len(tau) or len(x) < 2:
        raise ValueError("Incompatible or short arrays")
    if not np.all(np.isfinite(x)) or not np.all(np.isfinite(tau)):
        raise ValueError("Non-finite ordinates")
    if not np.all(np.diff(tau) > 0):
        raise ValueError("Lambert clock must be strictly increasing")
    if not np.isfinite(alpha) or not (0 < alpha <= 1):
        raise ValueError("Alpha must be finite and in (0,1]")

    u = x - alpha * tau
    n = len(u)
    means = np.empty(n, dtype=np.float64)
    weights = np.empty(n, dtype=np.int64)
    starts = np.empty(n, dtype=np.int64)
    ends = np.empty(n, dtype=np.int64)
    count = 0
    for i in range(n):
        means[count] = u[i]
        weights[count] = 1
        starts[count] = i
        ends[count] = i + 1
        count += 1
        while count > 1 and means[count - 2] > means[count - 1]:
            left, right = count - 2, count - 1
            wl, wr = weights[left], weights[right]
            means[left] = (wl * means[left] + wr * means[right]) / (wl + wr)
            weights[left] = wl + wr
            ends[left] = ends[right]
            count -= 1
    projected_u = np.empty(n, dtype=np.float64)
    for j in range(count):
        projected_u[starts[j] : ends[j]] = means[j]
    return projected_u + alpha * tau


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--casanya", required=True, type=Path, help="Existing c667 binary")
    p.add_argument("--lambert", required=True, type=Path, help="RvM binary")
    p.add_argument("--output", required=True, type=Path, help="New binary output")
    p.add_argument("--alpha", type=float, default=0.10)
    args = p.parse_args()
    inp, taufile = args.casanya.resolve(), args.lambert.resolve()
    out = args.output.resolve()
    if out in (inp, taufile) or out.exists():
        raise FileExistsError(f"Refusing to overwrite {out}")
    x, tau = load_f64(inp), load_f64(taufile)
    y = isotonic_project(x, tau, args.alpha)
    delta_gap = np.diff(y)
    original_crossings = int(np.count_nonzero(np.diff(x) <= 0))
    crossings = int(np.count_nonzero(delta_gap <= 0))
    if crossings:
        raise AssertionError(f"Projection did not preserve strict order: {crossings} gaps")
    out.parent.mkdir(parents=True, exist_ok=True)
    y.astype("<f8", copy=False).tofile(out)
    report = dict(
        method="Casanya c667 + full-array PAV isotonic projection",
        alpha=args.alpha,
        n=int(len(y)),
        source=str(inp),
        source_sha256=sha256(inp),
        lambert=str(taufile),
        lambert_sha256=sha256(taufile),
        output=str(out),
        output_sha256=sha256(out),
        previous_nonpositive_gaps=original_crossings,
        nonpositive_gaps=crossings,
        min_gap=float(delta_gap.min()),
        rms_change_from_c667=float(np.sqrt(np.mean((y - x) ** 2))),
        max_change_from_c667=float(np.max(np.abs(y - x))),
        maximum_prime_count="unchanged from c667; report original budget separately",
        validation_truth_used=False,
    )
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
