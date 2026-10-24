#!/usr/bin/env python3
"""Exact finite-sum check of the twisted quadratic prime-polynomial bound."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def prime_power_terms(limit: int) -> tuple[np.ndarray, np.ndarray]:
    """Return log(n) and Lambda(n)/(sqrt(n) log(n)) for n<=limit."""
    if limit < 2:
        return np.empty(0), np.empty(0)
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for prime in range(2, int(limit**0.5) + 1):
        if sieve[prime]:
            sieve[prime * prime :: prime] = False
    primes = np.flatnonzero(sieve)
    entries: list[tuple[int, float]] = []
    for prime in primes:
        power = int(prime)
        exponent = 1
        while power <= limit:
            entries.append((power, 1.0 / (exponent * np.sqrt(power))))
            if power > limit // int(prime):
                break
            power *= int(prime)
            exponent += 1
    entries.sort()
    values = np.array([entry[0] for entry in entries], dtype=np.float64)
    coefficients = np.array([entry[1] for entry in entries], dtype=np.float64)
    return np.log(values), coefficients


def exponential_integral(frequency: np.ndarray, height: float) -> np.ndarray:
    result = np.empty(frequency.shape, dtype=np.complex128)
    small = np.abs(frequency) < 1e-12
    result[small] = height
    omega = frequency[~small]
    result[~small] = np.expm1(1j * omega * height) / (1j * omega)
    return result


def exact_twisted_square(height: float, alpha: float, theta: float) -> tuple[complex, int, int]:
    cutoff = max(2, int(np.floor(height**theta)))
    logarithms, coefficients = prime_power_terms(cutoff)
    a = alpha * np.log(height)
    plus = logarithms[:, None] + logarithms[None, :]
    minus = logarithms[:, None] - logarithms[None, :]
    kernel = 0.25 * (
        exponential_integral(a + minus, height)
        + exponential_integral(a - minus, height)
        - exponential_integral(a + plus, height)
        - exponential_integral(a - plus, height)
    )
    integral = np.sum((coefficients[:, None] * coefficients[None, :]) * kernel) / np.pi**2
    return complex(integral), cutoff, coefficients.size


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--figure", type=Path, default=root / "figures" / "prime_model_validation.png"
    )
    args = parser.parse_args()

    cases = [
        (0.50, 0.375, 0.10),
        (1.00, 0.750, 0.10),
        (1.50, 0.875, 0.05),
    ]
    heights = np.array([300.0, 800.0, 2000.0, 5000.0, 12000.0])
    records: dict[tuple[float, float], tuple[np.ndarray, np.ndarray]] = {}

    print("Twisted prime-polynomial finite-sum validation")
    print("P_Y(t)=-(1/pi) sum_{n<=Y} Lambda(n)/(sqrt(n)log(n))*sin(t log n)")
    print("integrals are evaluated algebraically from exponential antiderivatives")
    for alpha, theta, epsilon in cases:
        if not (alpha / 2.0 < theta < min(alpha, 1.0)):
            raise RuntimeError("invalid theta range")
        actual: list[float] = []
        normalized_bound: list[float] = []
        print()
        print(f"alpha={alpha:.2f}, theta={theta:.3f}, epsilon={epsilon:.3f}")
        print(f"theta-alpha/2 = {theta-alpha/2:.3f}; min(alpha,1)-theta = {min(alpha,1)-theta:.3f}")
        print("      T       Y     prime powers       |I(T)|/T       bound-shape/T      ratio")
        for height in heights:
            integral, cutoff, term_count = exact_twisted_square(height, alpha, theta)
            observed = abs(integral) / height
            shape = (
                height ** (1.0 - alpha / 2.0 + epsilon)
                + height ** (alpha / 2.0 + epsilon)
                + height ** (theta + epsilon)
            ) / height
            actual.append(observed)
            normalized_bound.append(shape)
            print(
                f"{height:8.0f}  {cutoff:6d}      {term_count:6d}       "
                f"{observed:12.5e}     {shape:12.5e}    {observed/shape:8.4f}"
            )
        records[(alpha, theta)] = (np.array(actual), np.array(normalized_bound))

    blue = "#0b6fa4"
    orange = "#c8681c"
    green = "#4a7c59"
    gray = "#8a8a8a"
    colors = [blue, orange, green]
    fig, axes = plt.subplots(1, 2, figsize=(11.8, 4.55), dpi=180)

    ax = axes[0]
    for (alpha, theta, _), color in zip(cases, colors):
        actual, _ = records[(alpha, theta)]
        ax.loglog(heights, actual, "o-", color=color, linewidth=1.1, markersize=3.8, label=rf"$\alpha={alpha:.1f},\ \theta={theta:.3f}$")
    ax.set_xlabel(r"$T$")
    ax.set_ylabel(r"$T^{-1}|\int_0^T e^{i\alpha\log T\,t}P_Y(t)^2\,dt|$")
    ax.set_title("Exact finite prime-polynomial integrals", loc="left")
    ax.legend(frameon=False, fontsize=8)

    ax = axes[1]
    for (alpha, theta, _), color in zip(cases, colors):
        actual, shape = records[(alpha, theta)]
        ax.semilogx(heights, actual / shape, "o-", color=color, linewidth=1.1, markersize=3.8, label=rf"$\alpha={alpha:.1f}$")
    ax.set_xlabel(r"$T$")
    ax.set_ylabel("observed / stated bound shape")
    ax.set_title("Compatibility with all three exponent terms", loc="left")
    ax.legend(frameon=False, fontsize=8)

    for ax in axes:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color(gray)
        ax.spines["bottom"].set_color(gray)
        ax.grid(color="#ececec", linewidth=0.55)
    fig.suptitle(
        "Twisted quadratic cancellation in the truncated Selberg prime model",
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
