#!/usr/bin/env python3
"""Generate the exact Lambert--RVM clock used by carrier computations."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

import numpy as np
from scipy.special import lambertw


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
    parser.add_argument("--count", type=int, default=2_001_052)
    parser.add_argument(
        "--output", type=Path, default=root / "data" / "rvm_tau_2001052.bin"
    )
    args = parser.parse_args()
    if args.count < 2:
        raise ValueError("count must be at least two")

    ordinal = np.arange(1, args.count + 1, dtype=np.float64)
    shifted = ordinal - 11.0 / 8.0
    argument = shifted / np.e
    tau = TWOPI * shifted / np.real(lambertw(argument, 0))

    # Newton refinement is performed in extended precision.  M is strictly
    # increasing on the generated range because tau_1 > 2*pi and
    # M'(t)=log(t/(2*pi))/(2*pi)>0 there.
    tau_long = tau.astype(np.longdouble)
    target = ordinal.astype(np.longdouble) - np.longdouble(0.5)
    two_pi = np.longdouble(2.0) * np.longdouble(np.pi)
    for _ in range(5):
        value = (
            (tau_long / two_pi) * np.log(tau_long / (two_pi * np.e))
            + np.longdouble(7.0 / 8.0)
            - target
        )
        derivative = np.log(tau_long / two_pi) / two_pi
        tau_long -= value / derivative

    tau64 = tau_long.astype("<f8")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    tau64.tofile(args.output)
    restored = np.fromfile(args.output, dtype="<f8")
    if not np.array_equal(tau64, restored):
        raise RuntimeError("RVM binary round-trip failed")
    residual = (
        (tau_long / two_pi) * np.log(tau_long / (two_pi * np.e))
        + np.longdouble(7.0 / 8.0)
        - target
    )
    print("Lambert--RVM binary generation")
    print(f"count = {args.count}")
    print(f"output = data/{args.output.name}")
    print(f"output sha256 = {sha256(args.output)}")
    print(f"dtype = little-endian IEEE-754 float64")
    print(f"byte count = {args.output.stat().st_size}")
    print(f"tau_1 = {tau64[0]:.15f}")
    print(f"tau_N = {tau64[-1]:.12f}")
    print(f"strictly increasing = {bool(np.all(np.diff(tau64) > 0.0))}")
    print(f"max extended-precision |M(tau_k)-(k-1/2)| = {np.max(np.abs(residual)):.3e}")


if __name__ == "__main__":
    main()
