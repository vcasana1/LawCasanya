#!/usr/bin/env python3
"""Shared binary/NumPy loaders used by every numerical appendix."""

from __future__ import annotations

from pathlib import Path

import numpy as np


def load_float64(path: Path) -> np.ndarray:
    """Load a one-dimensional float64 array.

    Raw ``.bin`` files are little-endian IEEE-754 float64 with no header.
    NumPy ``.npy`` files are retained as provenance copies and are accepted
    for independent cross-checks.
    """
    path = Path(path)
    if path.suffix.lower() == ".bin":
        values = np.fromfile(path, dtype="<f8")
    elif path.suffix.lower() == ".npy":
        values = np.load(path, allow_pickle=False)
    else:
        raise ValueError(f"unsupported array format: {path}")
    values = np.asarray(values, dtype=np.float64)
    if values.ndim != 1 or values.size == 0:
        raise ValueError(f"expected a nonempty one-dimensional array: {path}")
    if not np.all(np.isfinite(values)):
        raise ValueError(f"array contains nonfinite entries: {path}")
    return values

