#!/usr/bin/env python3
"""Extrae longitudes, alturas y areas de las excursiones de Mertens.

El fichero de entrada contiene mu(1),...,mu(N) como int8. Las posiciones
mu(n)=0 se eliminan y el paseo comprimido tiene pasos +/-1.
"""

from __future__ import annotations

import argparse
import csv
import math
import time
from pathlib import Path

import numpy as np


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=Path)
    parser.add_argument("--block", type=int, default=5_000_000)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("mertens_excursiones_alturas.csv"),
    )
    return parser.parse_args()


def catalan_height_upper_tail(length: int, height: int) -> float:
    """P(maximo >= height) en la excursion uniforme de longitud ``length``.

    Se quitan el primer paso ascendente y el ultimo descendente. Queda un
    Dyck path de longitud 2*n=length-2 y altura maxima height-1. El conteo
    acotado se obtiene del espectro del grafo camino de alturas 0,...,a.
    """
    if length == 2:
        return 1.0
    n = length // 2 - 1
    a = height - 2
    if a < 0:
        return 1.0
    j = np.arange(1, a + 2, dtype=np.float64)
    theta = math.pi * j / (a + 2)
    eigen_abs = np.abs(2.0 * np.cos(theta))
    with np.errstate(divide="ignore"):
        terms = (
            math.log(2.0 / (a + 2))
            + 2.0 * np.log(np.sin(theta))
            + 2.0 * n * np.log(eigen_abs)
        )
    peak = float(np.max(terms))
    log_bounded = peak + math.log(float(np.exp(terms - peak).sum()))
    log_catalan = (
        math.lgamma(2 * n + 1) - math.lgamma(n + 1) - math.lgamma(n + 2)
    )
    log_cdf = min(0.0, log_bounded - log_catalan)
    return min(1.0, max(0.0, -math.expm1(log_cdf)))


def main() -> None:
    args = parse_args()
    size = args.filename.stat().st_size
    data = np.memmap(args.filename, dtype=np.int8, mode="r", shape=(size,))

    rows: list[tuple[int, int, int, int, int, int, int, int, int, float]] = []
    mertens = 0
    compressed = 0
    previous_zero_n = 0
    previous_zero_m = 0
    open_height = 0
    open_area = 0
    open_sign = 0
    started = time.monotonic()

    for lo in range(0, size, args.block):
        hi = min(lo + args.block, size)
        block = np.asarray(data[lo:hi])
        nz = np.flatnonzero(block)
        if nz.size:
            steps = block[nz].astype(np.int64, copy=False)
            walk = np.cumsum(steps, dtype=np.int64)
            walk += mertens
            hits = np.flatnonzero(walk == 0)

            start = 0
            for hit in hits:
                segment = walk[start : hit + 1]
                if segment.size:
                    if open_sign == 0:
                        open_sign = int(np.sign(segment[0]))
                    open_height = max(open_height, int(np.max(np.abs(segment))))
                    open_area += int(np.sum(np.abs(segment), dtype=np.int64))

                end_m = compressed + int(hit) + 1
                end_n = lo + int(nz[hit]) + 1
                length = end_m - previous_zero_m
                rows.append(
                    (
                        len(rows) + 1,
                        previous_zero_n,
                        end_n,
                        previous_zero_m,
                        end_m,
                        length,
                        open_sign,
                        open_height,
                        open_area,
                        open_height / math.sqrt(length),
                    )
                )
                previous_zero_n = end_n
                previous_zero_m = end_m
                open_height = 0
                open_area = 0
                open_sign = 0
                start = int(hit) + 1

            if start < walk.size:
                segment = walk[start:]
                if open_sign == 0:
                    open_sign = int(np.sign(segment[0]))
                open_height = max(open_height, int(np.max(np.abs(segment))))
                open_area += int(np.sum(np.abs(segment), dtype=np.int64))

            mertens = int(walk[-1])
            compressed += int(nz.size)

        block_number = lo // args.block + 1
        if block_number % 10 == 0 or hi == size:
            elapsed = time.monotonic() - started
            print(
                f"bloque={block_number:3d} n={hi:12d} m={compressed:12d} "
                f"M={mertens:7d} retornos={len(rows):7d} t={elapsed:7.1f}s",
                flush=True,
            )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    columns = (
        "Return",
        "Start_n",
        "End_n",
        "Start_m",
        "End_m",
        "Gap",
        "ExcursionSign",
        "MaxHeight",
        "Area",
        "HeightOverSqrtGap",
        "ReducedHeightOverSqrtLength",
        "CatalanHeightUpperTailExact",
        "HeightFreeEnergyNats",
        "HeightFreeEnergyBits",
    )
    with args.output.open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(columns)
        for row in rows:
            length = row[5]
            height = row[7]
            reduced_scaled = (
                (height - 1) / math.sqrt(length - 2) if length > 2 else 0.0
            )
            upper_tail = catalan_height_upper_tail(length, height)
            free_nats = -math.log(upper_tail)
            writer.writerow(
                row
                + (
                    reduced_scaled,
                    upper_tail,
                    free_nats,
                    free_nats / math.log(2.0),
                )
            )

    gaps = np.fromiter((row[5] for row in rows), dtype=np.int64)
    heights = np.fromiter((row[7] for row in rows), dtype=np.int64)
    scaled = heights / np.sqrt(gaps)
    print("\nRESUMEN")
    print(f"N={size}")
    print(f"m={compressed}")
    print(f"M(N)={mertens}")
    print(f"retornos={len(rows)}")
    print(f"ultimo_retorno_n={previous_zero_n}")
    print(f"ultimo_retorno_m={previous_zero_m}")
    print(f"cola_m={compressed-previous_zero_m}")
    print(f"gap_max={int(gaps.max())}")
    print(f"altura_max_absoluta={int(heights.max())}")
    print(f"max_altura_sobre_raiz_gap={float(scaled.max()):.12g}")
    for q in (0.5, 0.9, 0.95, 0.99, 0.999):
        print(f"q{q:g}_altura_sobre_raiz_gap={np.quantile(scaled, q):.12g}")
    print(f"csv={args.output.resolve()}")


if __name__ == "__main__":
    main()
