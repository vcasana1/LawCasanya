#!/usr/bin/env python3
"""Exact finite audit for the Version 9 Catalan-fusion example.

The script enumerates Dyck paths of semilength 6 and verifies that two
additional weak restrictions can have a genuinely joint effect on the
maximum height after a baseline restriction has created several maximizers.
It writes a machine-readable JSON certificate and a publication PNG.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt


def dyck_words(n: int) -> list[tuple[int, ...]]:
    words: list[tuple[int, ...]] = []

    def extend(word: tuple[int, ...], height: int, up: int, down: int) -> None:
        if up == n and down == n:
            words.append(word)
            return
        if up < n:
            extend(word + (1,), height + 1, up + 1, down)
        if down < n and height > 0:
            extend(word + (-1,), height - 1, up, down + 1)

    extend((), 0, 0, 0)
    return words


def height(word: tuple[int, ...]) -> int:
    level = 0
    maximum = 0
    for step in word:
        level += step
        maximum = max(maximum, level)
    return maximum


def select(words: list[tuple[int, ...]], forced: dict[int, int]) -> list[tuple[int, ...]]:
    # Positions are 1-based, as in the paper.
    return [w for w in words if all(w[position - 1] == step for position, step in forced.items())]


def summarize(words: list[tuple[int, ...]]) -> dict[str, object]:
    distribution = Counter(height(w) for w in words)
    h_star = max(distribution) if distribution else None
    high_count = distribution[h_star] if h_star is not None else 0
    return {
        "total": len(words),
        "maximum_height": h_star,
        "maximizer_count": high_count,
        "height_distribution": {str(h): distribution.get(h, 0) for h in range(1, 7)},
    }


def prefix_rank_formula(words: list[tuple[int, ...]]) -> list[int]:
    """Return max_t height from the exact prefix rank profile.

    For each prefix I_t, the rank-like quantity is the maximum number of up
    steps in I_t among the surviving paths. Thus 2*r(I_t)-t is exactly the
    largest compatible height at time t.
    """
    profile = []
    for t in range(1, 13):
        rank = max(sum(1 for step in w[:t] if step == 1) for w in words)
        profile.append(2 * rank - t)
    return profile


def bounded_dyck_count(n: int, forced: dict[int, int], ceiling: int) -> int:
    states = {0: 1}
    for position in range(1, 2 * n + 1):
        allowed = (forced[position],) if position in forced else (-1, 1)
        updated: dict[int, int] = {}
        for old_height, count in states.items():
            for step in allowed:
                new_height = old_height + step
                if 0 <= new_height <= ceiling:
                    updated[new_height] = updated.get(new_height, 0) + count
        states = updated
    return states.get(0, 0)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", default="../outputs/catalan_fusion_v9.json")
    parser.add_argument("--png", default="../outputs/catalan_fusion_v9.png")
    args = parser.parse_args()

    all_words = dyck_words(6)
    constraints = {
        "baseline": {6: -1},
        "A": {6: -1, 7: 1},
        "B": {6: -1, 8: 1},
        "A_union_B": {6: -1, 7: 1, 8: 1},
    }
    classes = {name: select(all_words, forced) for name, forced in constraints.items()}
    summaries = {name: summarize(words) for name, words in classes.items()}

    baseline_height = summaries["baseline"]["maximum_height"]
    assert len(all_words) == 132
    assert summaries["baseline"]["total"] == 66
    assert [summaries[key]["total"] for key in ("A", "B", "A_union_B")] == [42, 32, 19]
    assert [summaries[key]["maximum_height"] for key in ("baseline", "A", "B", "A_union_B")] == [5, 5, 5, 4]
    assert [summaries[key]["maximizer_count"] for key in ("baseline", "A", "B", "A_union_B")] == [5, 1, 1, 4]

    # Exact prefix-rank identity for each nonempty restricted class.
    rank_profiles = {name: prefix_rank_formula(words) for name, words in classes.items()}
    for name, profile in rank_profiles.items():
        assert max(profile) == summaries[name]["maximum_height"]

    bounded_dp = {
        name: {
            str(ceiling): bounded_dyck_count(6, constraints[name], ceiling)
            for ceiling in range(1, 7)
        }
        for name in classes
    }
    for name in classes:
        cumulative = 0
        for ceiling in range(1, 7):
            cumulative += summaries[name]["height_distribution"][str(ceiling)]
            assert bounded_dp[name][str(ceiling)] == cumulative

    base_total = summaries["baseline"]["total"]
    base_high = summaries["baseline"]["maximizer_count"]
    sector_xi: dict[str, float | None] = {}
    for name in ("A", "B", "A_union_B"):
        total = summaries[name]["total"]
        high = sum(height(w) >= baseline_height for w in classes[name])
        if high == 0:
            sector_xi[name] = None
        else:
            sector_xi[name] = math.log((base_high / base_total) / (high / total))

    sector_interactions: dict[str, object] = {}
    for threshold in range(2, baseline_height + 1):
        counts = {
            name: sum(height(w) >= threshold for w in classes[name])
            for name in classes
        }
        p0 = counts["baseline"] / summaries["baseline"]["total"]
        p_a = counts["A"] / summaries["A"]["total"]
        p_b = counts["B"] / summaries["B"]["total"]
        p_ab = counts["A_union_B"] / summaries["A_union_B"]["total"]
        if p_ab == 0:
            interaction = "infinity"
        else:
            interaction = math.log((p_a * p_b) / (p0 * p_ab))
        sector_interactions[str(threshold)] = {
            "high_counts": counts,
            "delta_sec_A_B": interaction,
        }

    height_drop = {
        name: baseline_height - summaries[name]["maximum_height"]
        for name in ("A", "B", "A_union_B")
    }
    synergy = height_drop["A_union_B"] - height_drop["A"] - height_drop["B"]
    assert synergy == 1

    certificate = {
        "semilength": 6,
        "unrestricted_dyck_count": len(all_words),
        "constraints_1_based": constraints,
        "classes": summaries,
        "prefix_rank_height_profiles": rank_profiles,
        "bounded_height_dp_counts": bounded_dp,
        "sector_threshold": baseline_height,
        "sector_xi": sector_xi,
        "sector_interactions_by_threshold": sector_interactions,
        "sector_annihilated_by_union": sum(height(w) >= baseline_height for w in classes["A_union_B"]) == 0,
        "height_synergy": synergy,
    }

    json_path = Path(args.json)
    png_path = Path(args.png)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    png_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    labels = ["Baseline", "A", "B", "A union B"]
    keys = ["baseline", "A", "B", "A_union_B"]
    totals = [summaries[k]["total"] for k in keys]
    high = [sum(height(w) >= baseline_height for w in classes[k]) for k in keys]
    distributions = [[summaries[k]["height_distribution"][str(h)] for h in range(1, 7)] for k in keys]

    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.2), constrained_layout=True)
    x = range(len(keys))
    axes[0].bar([i - 0.18 for i in x], totals, width=0.36, label="all paths", color="#4C78A8")
    axes[0].bar([i + 0.18 for i in x], high, width=0.36, label="height >= 5", color="#E45756")
    axes[0].set_xticks(list(x), labels)
    axes[0].set_ylabel("exact number of Dyck paths")
    axes[0].set_title("Sector annihilation is a joint effect")
    axes[0].legend(frameon=False)

    colors = ["#4C78A8", "#F58518", "#54A24B", "#B279A2"]
    for key, label, color, values in zip(keys, labels, colors, distributions):
        axes[1].plot(range(1, 7), values, marker="o", linewidth=2, label=label, color=color)
    axes[1].set_xlabel("maximum height")
    axes[1].set_ylabel("number of paths")
    axes[1].set_title("Exact height spectra, semilength 6")
    axes[1].set_xticks(range(1, 7))
    axes[1].legend(frameon=False)

    fig.savefig(png_path, dpi=220)
    print(json.dumps(certificate, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
