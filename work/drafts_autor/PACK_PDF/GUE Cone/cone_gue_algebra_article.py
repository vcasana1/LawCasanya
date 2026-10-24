#!/usr/bin/env python3
"""Cone quotient algebra and GUE-spacing figures.

The empirical zeta-zero checks read ``zeross.bin`` from the same directory as
this script. The no-zero experiment is self-contained. Output files are written
beside the script, matching the filenames used by the accompanying LaTeX file.
"""
from __future__ import annotations

import csv
import math
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
OUT = ROOT
ZEROS_FILE = ROOT / "zeross.bin"
NMAX_ZERO: int | None = None
NMODEL = 2_000_000
FIG_W = 1600
FIG_H = 950


def load_font(size: int) -> ImageFont.ImageFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "/Library/Fonts/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except Exception:
            pass
    return ImageFont.load_default()


FONT_BIG = load_font(34)
FONT = load_font(26)
FONT_SMALL = load_font(21)


def erf_approx(x: np.ndarray) -> np.ndarray:
    sign = np.sign(x)
    ax = np.abs(x)
    p = 0.3275911
    a1 = 0.254829592
    a2 = -0.284496736
    a3 = 1.421413741
    a4 = -1.453152027
    a5 = 1.061405429
    t = 1.0 / (1.0 + p * ax)
    y = 1.0 - (((((a5 * t + a4) * t + a3) * t + a2) * t + a1) * t) * np.exp(-(ax * ax))
    return sign * y


def gue_pdf(s: np.ndarray) -> np.ndarray:
    y = np.zeros_like(s, dtype=np.float64)
    idx = s >= 0
    y[idx] = (32.0 / math.pi**2) * s[idx] ** 2 * np.exp(-4.0 * s[idx] ** 2 / math.pi)
    return y


def gue_cdf(s: np.ndarray) -> np.ndarray:
    y = np.zeros_like(s, dtype=np.float64)
    idx = s >= 0
    x = s[idx]
    y[idx] = erf_approx(2.0 * x / math.sqrt(math.pi)) - (4.0 * x / math.pi) * np.exp(
        -4.0 * x * x / math.pi
    )
    y[s > 20] = 1.0
    return y


def rvm_inverse_vector(n: np.ndarray) -> np.ndarray:
    two_pi = 2.0 * math.pi
    t = two_pi * (n + 1.0) / np.log(n + 10.0)
    t[t < 14.0] = 14.0
    for _ in range(30):
        f = t / two_pi * np.log(t / two_pi) - t / two_pi + 7.0 / 8.0
        df = (1.0 / two_pi) * np.log(t / two_pi)
        step = (f - n) / df
        step[~np.isfinite(step)] = 0.0
        t = t - step
        t[t <= two_pi] = two_pi + 1.0
    return t


def cone_fm_nu_from_y(
    y: np.ndarray, height: np.ndarray, alpha: float
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    q = (y[1:] - 1.0) / y[:-1]
    h = -np.angle(q) / alpha
    period = 2.0 * math.pi / alpha
    h = np.mod(h, period)
    h[h > period / 2.0] -= period
    h[h < 0.0] += period
    h0 = 2.0 * math.pi / np.log(height[1:] / (2.0 * math.pi))
    nu = h / h0
    eta = nu - 1.0
    return nu, eta, h


def compare_gue(x: np.ndarray, xmax: float = 3.8) -> dict[str, float]:
    x = x[np.isfinite(x)]
    edges = np.linspace(0.0, xmax, 220)
    centers = 0.5 * (edges[:-1] + edges[1:])
    dx = centers[1] - centers[0]
    hist, _ = np.histogram(x, bins=edges, density=True)
    pdf = gue_pdf(centers)
    xs = np.sort(x)
    emp = np.arange(1, xs.size + 1, dtype=np.float64) / xs.size
    ks = float(np.max(np.abs(emp - gue_cdf(xs))))
    return {
        "mean": float(np.mean(x)),
        "std": float(np.std(x, ddof=1)),
        "min": float(np.min(x)),
        "max": float(np.max(x)),
        "L1": float(np.sum(np.abs(hist - pdf)) * dx),
        "L2": float(math.sqrt(np.sum((hist - pdf) ** 2) * dx)),
        "KS": ks,
    }


def corr(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.corrcoef(a, b)[0, 1])


def polyline(
    draw: ImageDraw.ImageDraw,
    points: list[tuple[int, int]],
    color: tuple[int, int, int],
    width: int,
) -> None:
    if len(points) >= 2:
        draw.line(points, fill=color, width=width, joint="curve")


def project_3d(x: np.ndarray, y: np.ndarray, z: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    x = (x - np.mean(x)) / (np.std(x) + 1e-12)
    y = (y - np.mean(y)) / (np.std(y) + 1e-12)
    z = (z - np.min(z)) / (np.max(z) - np.min(z) + 1e-12)
    z = 3.0 * (z - 0.5)
    xr = 0.90 * x - 0.35 * y
    yr = 0.20 * x + 0.55 * y - 0.85 * z
    px = 130 + (xr - np.min(xr)) / (np.max(xr) - np.min(xr) + 1e-12) * (FIG_W - 230)
    py = 110 + (1.0 - (yr - np.min(yr)) / (np.max(yr) - np.min(yr) + 1e-12)) * (FIG_H - 230)
    return px, py


def draw_3d_path(
    path: Path,
    title: str,
    series: list[tuple[np.ndarray, np.ndarray, np.ndarray, str, tuple[int, int, int], int]],
) -> None:
    img = Image.new("RGB", (FIG_W, FIG_H), "white")
    draw = ImageDraw.Draw(img)
    draw.text((80, 35), title, fill=(0, 0, 0), font=FONT_BIG)
    draw.rectangle([80, 100, FIG_W - 60, FIG_H - 95], outline=(35, 35, 35), width=2)
    for x, y, z, _label, color, width in series:
        px, py = project_3d(x, y, z)
        pts = [(int(a), int(b)) for a, b in zip(px, py)]
        polyline(draw, pts, color, width)
    lx = 105
    ly = FIG_H - 70
    for _, _, _, label, color, width in series:
        draw.line([lx, ly, lx + 55, ly], fill=color, width=max(4, width))
        draw.text((lx + 70, ly - 14), label, fill=(0, 0, 0), font=FONT_SMALL)
        lx += 390
    draw.text(
        (95, FIG_H - 35),
        "orthographic projection of (Re S_N, Im S_N, height)",
        fill=(70, 70, 70),
        font=FONT_SMALL,
    )
    img.save(path)


def draw_hist(
    path: Path,
    title: str,
    datasets: list[tuple[np.ndarray, str, tuple[int, int, int], str]],
    xmax: float = 3.8,
) -> None:
    img = Image.new("RGB", (FIG_W, FIG_H), "white")
    draw = ImageDraw.Draw(img)
    left, top, right, bottom = 115, 105, 65, 120
    pw = FIG_W - left - right
    ph = FIG_H - top - bottom
    edges = np.linspace(0.0, xmax, 220)
    centers = 0.5 * (edges[:-1] + edges[1:])
    hists = [np.histogram(data[np.isfinite(data)], bins=edges, density=True)[0] for data, _, _, _ in datasets]
    pdf = gue_pdf(centers)
    ymax = float(max([np.max(pdf)] + [np.max(h) for h in hists]) * 1.14)

    def xy(xv: float, yv: float) -> tuple[int, int]:
        return left + int((xv / xmax) * pw), top + ph - int((yv / ymax) * ph)

    draw.text((80, 35), title, fill=(0, 0, 0), font=FONT_BIG)
    draw.rectangle([left, top, left + pw, top + ph], outline=(35, 35, 35), width=2)
    for tick in np.arange(0.0, xmax + 1e-9, 0.5):
        x, _ = xy(float(tick), 0.0)
        draw.line([x, top, x, top + ph], fill=(230, 230, 230))
        draw.text((x - 16, top + ph + 12), f"{tick:g}", fill=(0, 0, 0), font=FONT_SMALL)
    for tick in np.linspace(0.0, ymax, 6):
        _, y = xy(0.0, float(tick))
        draw.line([left, y, left + pw, y], fill=(230, 230, 230))
        draw.text((20, y - 12), f"{tick:.2f}", fill=(0, 0, 0), font=FONT_SMALL)
    for hist, (_, _label, color, mode) in zip(hists, datasets):
        if mode == "bars":
            for i, val in enumerate(hist):
                x0, y0 = xy(float(edges[i]), float(val))
                x1, y1 = xy(float(edges[i + 1]), 0.0)
                draw.rectangle([x0, y0, max(x0 + 1, x1), y1], fill=color)
        else:
            pts = [xy(float(c), float(v)) for c, v in zip(centers, hist)]
            polyline(draw, pts, color, 4)
    gue_pts = [xy(float(c), float(v)) for c, v in zip(centers, pdf)]
    polyline(draw, gue_pts, (0, 0, 0), 5)
    draw.text((left + pw // 2 - 35, FIG_H - 58), "nu_N", fill=(0, 0, 0), font=FONT)
    draw.text((20, top + ph // 2 - 20), "pdf", fill=(0, 0, 0), font=FONT)
    lx = left + pw - 315
    ly = top + 30
    draw.rectangle([lx - 15, ly - 15, lx + 285, ly + 105], fill=(255, 255, 255), outline=(70, 70, 70))
    legend = datasets + [(pdf, "Wigner-GUE", (0, 0, 0), "line")]
    for j, (_, label, color, mode) in enumerate(legend):
        yy = ly + 32 * j
        if mode == "bars":
            draw.rectangle([lx, yy - 10, lx + 45, yy + 10], fill=color)
        else:
            draw.line([lx, yy, lx + 45, yy], fill=color, width=5)
        draw.text((lx + 60, yy - 13), label, fill=(0, 0, 0), font=FONT_SMALL)
    img.save(path)


def draw_scatter(
    path: Path,
    title: str,
    x: np.ndarray,
    y: np.ndarray,
    xlabel: str,
    ylabel: str,
) -> None:
    img = Image.new("RGB", (FIG_W, FIG_H), "white")
    draw = ImageDraw.Draw(img)
    left, top, right, bottom = 125, 105, 65, 125
    pw = FIG_W - left - right
    ph = FIG_H - top - bottom
    xlo, xhi = np.quantile(x, [0.001, 0.999])
    ylo, yhi = np.quantile(y, [0.001, 0.999])
    pad_x = 0.08 * (xhi - xlo)
    pad_y = 0.08 * (yhi - ylo)
    xlo -= pad_x
    xhi += pad_x
    ylo -= pad_y
    yhi += pad_y

    def xy(xv: float, yv: float) -> tuple[int, int]:
        return (
            left + int((xv - xlo) / (xhi - xlo) * pw),
            top + ph - int((yv - ylo) / (yhi - ylo) * ph),
        )

    draw.text((80, 35), title, fill=(0, 0, 0), font=FONT_BIG)
    draw.rectangle([left, top, left + pw, top + ph], outline=(35, 35, 35), width=2)
    for tick in np.linspace(xlo, xhi, 7):
        px, _ = xy(float(tick), ylo)
        draw.line([px, top, px, top + ph], fill=(232, 232, 232))
        draw.text((px - 35, top + ph + 12), f"{tick:.2f}", fill=(0, 0, 0), font=FONT_SMALL)
    for tick in np.linspace(ylo, yhi, 7):
        _, py = xy(xlo, float(tick))
        draw.line([left, py, left + pw, py], fill=(232, 232, 232))
        draw.text((20, py - 12), f"{tick:.2f}", fill=(0, 0, 0), font=FONT_SMALL)
    for xv, yv in zip(x, y):
        px, py = xy(float(xv), float(yv))
        if left <= px <= left + pw and top <= py <= top + ph:
            draw.ellipse([px - 2, py - 2, px + 2, py + 2], fill=(35, 90, 185))
    line_pts = [xy(float(t), float(t)) for t in np.linspace(max(xlo, ylo), min(xhi, yhi), 400)]
    polyline(draw, line_pts, (215, 70, 35), 4)
    draw.text((left + pw // 2 - 90, FIG_H - 58), xlabel, fill=(0, 0, 0), font=FONT)
    draw.text((left - 92, top - 44), ylabel, fill=(0, 0, 0), font=FONT)
    img.save(path)


def gue_quantile_lattice(m: int) -> np.ndarray:
    s_grid = np.linspace(0.0, 4.5, 300_000)
    f_grid = np.maximum.accumulate(gue_cdf(s_grid))
    keep = np.concatenate(([True], np.diff(f_grid) > 0.0))
    s_grid = s_grid[keep]
    f_grid = f_grid[keep]
    phi = (math.sqrt(5.0) - 1.0) / 2.0
    u = ((np.arange(m, dtype=np.float64) + 0.5) * phi) % 1.0
    u = np.clip(u, np.finfo(np.float64).eps, 1.0 - np.finfo(np.float64).eps)
    return np.interp(u, f_grid, s_grid)


def bounded_increment_rearrangement(d: np.ndarray) -> np.ndarray:
    pos = np.sort(d[d >= 0.0])[::-1]
    neg = np.sort(d[d < 0.0])
    out = np.empty_like(d)
    ip = 0
    ineg = 0
    x = 0.0
    for k in range(d.size):
        if x >= 0.0 and ineg < neg.size:
            val = neg[ineg]
            ineg += 1
        elif x < 0.0 and ip < pos.size:
            val = pos[ip]
            ip += 1
        elif ineg < neg.size:
            val = neg[ineg]
            ineg += 1
        else:
            val = pos[ip]
            ip += 1
        out[k] = val
        x += float(val)
    return out


def no_zero_gmodel(alpha: float, n_model: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    n = np.arange(1, n_model + 1, dtype=np.float64)
    height = rvm_inverse_vector(n)
    a = 0.5 + 1.0 / (2.0 * math.pi * alpha * alpha * height) - 1j / (2.0 * math.pi * alpha) * np.log(
        height / (2.0 * math.pi)
    )
    s = gue_quantile_lattice(n_model - 1)
    d_re = 1.0 - s
    d_re -= np.mean(d_re)
    d_re = bounded_increment_rearrangement(d_re)
    real_g = np.empty(n_model, dtype=np.float64)
    real_g[0] = 0.0
    real_g[1:] = np.cumsum(d_re)
    phi = (math.sqrt(5.0) - 1.0) / 2.0
    sigma_im = 0.010862192738467039
    phase = 2.0 * math.pi * ((np.arange(n_model, dtype=np.float64) * phi + 0.1732050807568877) % 1.0)
    g = real_g + 1j * sigma_im * np.sin(phase)
    y = a + g
    nu_cone, _, _ = cone_fm_nu_from_y(y, height, alpha)
    nu_red = 1.0 - np.real(np.diff(g))
    return nu_cone, nu_red, height


def write_summary(rows: list[dict[str, object]]) -> None:
    fields = ["case", "N", "mean", "std", "min", "max", "L1", "L2", "KS", "extra"]
    with (OUT / "CONE_GUE_ARTICLE_SUMMARY.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def main() -> None:
    if not ZEROS_FILE.exists():
        raise FileNotFoundError(
            f"Missing {ZEROS_FILE.name}. Place zeross.bin beside this script to regenerate the zero-data figures."
        )

    circle_length = 3.0**math.pi * math.sqrt(math.exp(math.pi))
    alpha = 2.0 * math.pi / circle_length
    k_const = complex(-5.161990134502993, 2.9872973089668946)

    gamma = np.fromfile(ZEROS_FILE, dtype=np.float64)
    if NMAX_ZERO is not None:
        gamma = gamma[:NMAX_ZERO]
    gamma = gamma[np.isfinite(gamma)]
    n = gamma.size
    h = np.diff(gamma)
    h0 = 2.0 * math.pi / np.log(gamma[1:] / (2.0 * math.pi))
    nu_direct = h / h0

    r = np.exp(1j * alpha * gamma)
    s_walk = np.cumsum(r)
    a = 0.5 + 1.0 / (2.0 * math.pi * alpha * alpha * gamma) - 1j / (2.0 * math.pi * alpha) * np.log(
        gamma / (2.0 * math.pi)
    )
    y = np.exp(-1j * alpha * gamma) * (s_walk - k_const)
    g = y - a
    nu_cone, _, h_cone = cone_fm_nu_from_y(y, gamma, alpha)
    dreg_law = 1.0 - np.real(np.diff(g))

    step = max(1, n // 7000)
    idx = np.arange(0, n, step)
    idx_gap = np.arange(0, n - 1, step)
    smooth_s = k_const + r * a

    draw_3d_path(
        OUT / "FIG01_CONE_WALK_3D.png",
        "Cone walk from Odlyzko zeros",
        [(np.real(s_walk[idx]), np.imag(s_walk[idx]), gamma[idx], "S_N=sum exp(i alpha gamma_N)", (40, 95, 190), 2)],
    )
    draw_3d_path(
        OUT / "FIG02_CONE_SMOOTH_FIT_3D.png",
        "Cone decomposition: walk and smooth cone term",
        [
            (np.real(s_walk[idx]), np.imag(s_walk[idx]), gamma[idx], "actual walk", (35, 100, 195), 2),
            (np.real(smooth_s[idx]), np.imag(smooth_s[idx]), gamma[idx], "K+R_N A_N", (220, 80, 35), 3),
        ],
    )
    draw_hist(
        OUT / "FIG03_ZEROS_DIRECT_CONE_GUE.png",
        "Zeta zero spacings: direct gaps and cone quotient",
        [
            (nu_direct, "direct gaps", (75, 125, 210), "bars"),
            (nu_cone, "cone quotient", (220, 80, 35), "line"),
        ],
    )
    draw_scatter(
        OUT / "FIG04_ZEROS_REDUCED_LAW.png",
        "Reduced cone law on Odlyzko zeros",
        dreg_law[idx_gap],
        nu_direct[idx_gap],
        "1-Re(dG)",
        "nu_N",
    )

    nu_model, nu_model_red, _height_model = no_zero_gmodel(alpha, NMODEL)
    draw_hist(
        OUT / "FIG05_NO_ZERO_TRANSDUCER_GUE.png",
        "No-zero GUE driver through the cone quotient",
        [
            (nu_model, "cone output", (75, 125, 210), "bars"),
            (nu_model_red, "1-Re(dG)", (220, 80, 35), "line"),
        ],
    )

    metrics: list[dict[str, object]] = []
    cases = [
        ("zeros_direct", nu_direct, ""),
        ("zeros_cone_quotient", nu_cone, f"max_abs_h_error={np.max(np.abs(h_cone - h)):.17g}"),
        ("zeros_reduced_1_minus_Re_dG", dreg_law, f"corr_with_nu={corr(dreg_law, nu_direct):.17g}"),
        ("no_zero_gmodel_cone", nu_model, f"corr_with_reduced={corr(nu_model, nu_model_red):.17g}"),
        ("no_zero_gmodel_reduced", nu_model_red, ""),
    ]
    for case, arr, extra in cases:
        row: dict[str, object] = {"case": case, "N": arr.size, "extra": extra}
        row.update(compare_gue(arr))
        metrics.append(row)
    write_summary(metrics)

    report_lines = [
        "Cone GUE algebra article diagnostics",
        "====================================",
        f"zeross.bin values: {n}",
        f"gamma_1: {gamma[0]:.17g}",
        f"gamma_N: {gamma[-1]:.17g}",
        f"circleLength: {circle_length:.17g}",
        f"alpha: {alpha:.17g}",
        f"K: {k_const.real:.17g} {k_const.imag:+.17g}i",
        f"max |h_cone-h|: {np.max(np.abs(h_cone - h)):.17g}",
        f"mean |h_cone-h|: {np.mean(np.abs(h_cone - h)):.17g}",
        f"rms |h_cone-h|: {math.sqrt(np.mean((h_cone - h) ** 2)):.17g}",
        f"corr(nu, 1-Re(dG)): {corr(nu_direct, dreg_law):.17g}",
        f"mean |nu-(1-Re(dG))|: {np.mean(np.abs(nu_direct - dreg_law)):.17g}",
        f"rms |nu-(1-Re(dG))|: {math.sqrt(np.mean((nu_direct - dreg_law) ** 2)):.17g}",
        "",
    ]
    for row in metrics:
        report_lines.append(
            f"{row['case']}: mean={row['mean']:.17g}, std={row['std']:.17g}, "
            f"L1={row['L1']:.17g}, L2={row['L2']:.17g}, KS={row['KS']:.17g}, {row['extra']}"
        )
    (OUT / "CONE_GUE_ARTICLE_REPORT.txt").write_text("\n".join(report_lines) + "\n")
    print("\n".join(report_lines))


if __name__ == "__main__":
    main()
