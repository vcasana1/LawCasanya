#!/usr/bin/env python3
"""Export provenance NumPy arrays as raw little-endian float64 binaries."""

from __future__ import annotations

import hashlib
from pathlib import Path

import numpy as np


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def export(source: Path, destination: Path) -> None:
    values = np.load(source, allow_pickle=False).astype("<f8", copy=False)
    if values.ndim != 1 or not np.all(np.isfinite(values)):
        raise ValueError(f"invalid ordinate array: {source}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    values.tofile(destination)
    restored = np.fromfile(destination, dtype="<f8")
    if not np.array_equal(values, restored):
        raise RuntimeError(f"binary round-trip failed: {destination}")
    print(f"source = data/{source.name}")
    print(f"source sha256 = {sha256(source)}")
    print(f"destination = data/{destination.name}")
    print(f"destination sha256 = {sha256(destination)}")
    print(f"count = {values.size}")
    print(f"dtype = little-endian IEEE-754 float64")
    print(f"byte count = {destination.stat().st_size}")
    print("round-trip exact = True")


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    print("Raw-binary data export")
    export(root / "data" / "g_hp.npy", root / "data" / "g_hp.bin")
    print()
    export(root / "data" / "gammas.npy", root / "data" / "gammas.bin")


if __name__ == "__main__":
    main()
