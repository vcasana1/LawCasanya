#!/usr/bin/env python3
"""Finite audit of the gentle-mountain construction in Version 6."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def gentle_mountain(r: int, blocks: int) -> np.ndarray:
    """Return the heights of W followed by the path retracing W."""
    up_block = np.r_[np.ones(r + 1, dtype=int), -np.ones(r, dtype=int)]
    first_half = np.tile(up_block, blocks)
    second_half = -first_half[::-1]
    steps = np.r_[first_half, second_half]
    return np.r_[0, np.cumsum(steps)]


def chord_profile(height: np.ndarray) -> np.ndarray:
    """Maximum absolute increment among all chords of each length."""
    length = height.size - 1
    profile = np.zeros(length + 1, dtype=int)
    for span in range(1, length + 1):
        profile[span] = np.max(np.abs(height[span:] - height[:-span]))
    return profile


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    output_dir = root / "outputs"
    output_dir.mkdir(parents=True, exist_ok=True)

    r = 12
    blocks = 80
    height = gentle_mountain(r, blocks)
    profile = chord_profile(height)
    length = height.size - 1
    delta = 1.0 / (2 * r + 1)
    spans = np.arange(length + 1)
    deterministic_envelope = delta * spans + 4 * r

    assert height[0] == 0 and height[-1] == 0
    assert np.all(height[1:-1] > 0)
    assert np.all(profile <= deterministic_envelope + 1e-12)

    fig, axes = plt.subplots(2, 1, figsize=(9.2, 6.4), constrained_layout=True)
    axes[0].plot(height, color="#243b72", linewidth=1.25)
    axes[0].set_title("Primitive Catalan gentle mountain")
    axes[0].set_xlabel("compressed step")
    axes[0].set_ylabel("height")
    axes[0].grid(alpha=0.25)

    axes[1].plot(spans[1:], profile[1:] / spans[1:], color="#b33a3a",
                 label="maximum chord slope")
    axes[1].plot(spans[1:], deterministic_envelope[1:] / spans[1:],
                 color="#202020", linestyle="--",
                 label=r"$\delta+4r/s$")
    axes[1].axhline(delta, color="#238b57", linestyle=":",
                    label=r"block drift $\delta$")
    axes[1].set_xscale("log")
    axes[1].set_xlabel("chord length s")
    axes[1].set_ylabel("maximum |increment| / s")
    axes[1].set_ylim(0, 1.05)
    axes[1].grid(alpha=0.25)
    axes[1].legend(frameon=False)

    png_path = output_dir / "mt_catalan_gentle_mountain_v6.png"
    fig.savefig(png_path, dpi=220)
    plt.close(fig)

    audit = {
        "r": r,
        "blocks": blocks,
        "length": int(length),
        "maximum_height": int(height.max()),
        "block_drift_delta": delta,
        "primitive": bool(np.all(height[1:-1] > 0) and height[-1] == 0),
        "envelope_verified": bool(np.all(profile <= deterministic_envelope + 1e-12)),
        "png": str(png_path),
    }
    json_path = output_dir / "mt_catalan_gentle_mountain_v6.json"
    json_path.write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(audit, indent=2))


if __name__ == "__main__":
    main()
