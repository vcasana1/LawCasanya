#!/usr/bin/env python3
"""Exact exponent audit for the Version 7 Catalan-energy hierarchy.

This program visualizes algebraic consequences of the proposed bounds.
It is not numerical evidence that any Catalan-energy estimate holds for
the Mobius function.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

import matplotlib.pyplot as plt


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    out_dir = root / "outputs"
    out_dir.mkdir(parents=True, exist_ok=True)

    theta = Fraction(11, 20)
    rows = []
    for q in range(1, 41):
        dyadic = Fraction(q + 1, 2 * q + 1)
        mesoscopic = Fraction(1, 1) - theta * Fraction(q, 2 * q + 1)
        rows.append(
            {
                "q": q,
                "dyadic_fraction": str(dyadic),
                "dyadic_decimal": float(dyadic),
                "critical_block_fraction": str(mesoscopic),
                "critical_block_decimal": float(mesoscopic),
            }
        )

    payload = {
        "status": "exact_formula_audit_not_arithmetic_evidence",
        "theta": str(theta),
        "dyadic_formula": "(q+1)/(2q+1)",
        "dyadic_limit": "1/2",
        "critical_block_formula": "1-theta*q/(2q+1)",
        "critical_block_limit": "29/40",
        "rows": rows,
    }
    json_path = out_dir / "catalan_energy_ladder_v7.json"
    json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    q_values = [row["q"] for row in rows]
    dyadic_values = [row["dyadic_decimal"] for row in rows]
    mesoscopic_values = [row["critical_block_decimal"] for row in rows]

    fig, ax = plt.subplots(figsize=(9.2, 5.2))
    ax.plot(q_values, dyadic_values, "o-", lw=2, ms=4,
            label=r"dyadic: $(q+1)/(2q+1)$")
    ax.plot(q_values, mesoscopic_values, "s-", lw=2, ms=3,
            label=r"critical blocks: $1-\frac{11}{20}\frac{q}{2q+1}$")
    ax.axhline(0.5, color="tab:blue", ls="--", alpha=0.7,
               label=r"dyadic limit $1/2$")
    ax.axhline(29 / 40, color="tab:orange", ls="--", alpha=0.7,
               label=r"critical-block limit $29/40$")
    ax.set_xlabel(r"fixed moment index $q$")
    ax.set_ylabel("global exponent forced by the energy bound")
    ax.set_title("Catalan occupation-energy exponent ladder (exact algebra)")
    ax.grid(alpha=0.25)
    ax.legend(loc="best")
    fig.tight_layout()

    png_path = out_dir / "catalan_energy_ladder_v7.png"
    fig.savefig(png_path, dpi=220)
    plt.close(fig)

    print(f"Wrote {json_path}")
    print(f"Wrote {png_path}")


if __name__ == "__main__":
    main()
