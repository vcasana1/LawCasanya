#!/usr/bin/env python3
"""
Generate the two figures used in the manuscript.

Outputs in the current directory:
    mobius_heatmap_N80.png
    mobius_surface_3d_N200.png
    mobius_surface_interactive_N200.html

The arithmetic surface is
    F(n,r) = sum_{a|n, a>r} mu(n/a),
for integers n >= 1 and r >= 0.
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

try:
    import plotly.graph_objects as go
except Exception:
    go = None


def mobius_sieve(N: int) -> np.ndarray:
    """Return mu[0..N]."""
    mu = np.ones(N + 1, dtype=int)
    mu[0] = 0
    is_prime = np.ones(N + 1, dtype=bool)
    is_prime[:2] = False
    for p in range(2, int(N ** 0.5) + 1):
        if is_prime[p]:
            is_prime[p * p:N + 1:p] = False
    for p in np.where(is_prime)[0]:
        mu[p::p] *= -1
        p2 = p * p
        if p2 <= N:
            mu[p2::p2] = 0
    return mu


def divisors(n: int) -> list[int]:
    ds = []
    for a in range(1, int(n ** 0.5) + 1):
        if n % a == 0:
            ds.append(a)
            if a * a != n:
                ds.append(n // a)
    ds.sort()
    return ds


def surface_F(N: int) -> np.ndarray:
    """Return array Z[r,n-1] = F(n,r), with 0 <= r <= N."""
    mu = mobius_sieve(N)
    Z = np.zeros((N + 1, N), dtype=int)
    for n in range(1, N + 1):
        ds = divisors(n)
        for r in range(0, N + 1):
            Z[r, n - 1] = sum(mu[n // a] for a in ds if a > r)
    return Z


def make_heatmap() -> None:
    N = 80
    Z = surface_F(N)[1:N + 1, :]
    out = Path("mobius_heatmap_N80.png")
    fig, ax = plt.subplots(figsize=(13, 8.5))
    im = ax.imshow(
        Z,
        origin="lower",
        aspect="auto",
        interpolation="nearest",
        extent=[1, N, 1, N],
        vmin=-1,
        vmax=1,
        cmap="coolwarm",
    )
    ax.set_xlabel("r")
    ax.set_ylabel("n")
    ax.set_title(r"Superficie $F(n,r)=\sum_{a\mid n,\ a>r}\mu(n/a)$, $1\le n,r\le 80$")
    cbar = fig.colorbar(im, ax=ax)
    cbar.set_label("F(n,r) recortado en [-1,1]")
    ax.set_xticks([1, 10, 20, 40, 60, 80])
    ax.set_yticks([1, 10, 20, 40, 60, 80])
    ax.grid(color="white", linewidth=0.8, alpha=0.6)
    fig.tight_layout()
    fig.savefig(out, dpi=180)
    plt.close(fig)


def make_3d_and_html() -> None:
    N = 200
    Z = surface_F(N)
    cols = np.arange(1, N + 1)
    rows = np.arange(0, N + 1)
    X, Y = np.meshgrid(cols, rows)

    fig = plt.figure(figsize=(14, 10))
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(X, Y, Z, rstride=2, cstride=2, linewidth=0, antialiased=True)
    ax.set_xlabel("Numero de columna n")
    ax.set_ylabel("Filas omitidas r")
    ax.set_zlabel("F(n,r)")
    ax.set_title("Superficie 3D de las sumas de columna de la matriz de Mobius truncada")
    ax.view_init(elev=28, azim=-135)
    fig.savefig("mobius_surface_3d_N200.png", dpi=180, bbox_inches="tight")
    plt.close(fig)

    if go is not None:
        fig_html = go.Figure(
            data=[go.Surface(
                x=cols,
                y=rows,
                z=Z,
                showscale=True,
                hovertemplate="n=%{x}<br>r=%{y}<br>F(n,r)=%{z}<extra></extra>",
            )]
        )
        fig_html.update_layout(
            title="Superficie 3D de F(n,r): columnas de la matriz de Mobius con filas omitidas",
            scene=dict(
                xaxis_title="Numero de columna n",
                yaxis_title="Filas omitidas r",
                zaxis_title="F(n,r)",
                camera=dict(eye=dict(x=1.55, y=-1.65, z=0.9)),
            ),
            margin=dict(l=0, r=0, b=0, t=60),
        )
        fig_html.write_html("mobius_surface_interactive_N200.html", include_plotlyjs=True, full_html=True)


if __name__ == "__main__":
    make_heatmap()
    make_3d_and_html()
