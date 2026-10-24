"""
v9_Px_funcion.py
P(n) shown explicitly as a real-valued function: the genuine continuous
envelope x -> e^{-Cx} (and x -> -Cx on a log scale) drawn as a curve,
with P(n) itself shown as clean scatter points. No bars, no histogram.

Run: python3 v9_Px_funcion.py
Produces: fig_Pn_original.png, fig_Px_funcion_de_x.png
"""

import numpy as np
import sympy
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

C = 0.7437948618394004


def P_direct(n):
    val = 1.0
    for k in range(2, n):
        val *= np.sin(np.pi * n / k)
    return val


def logabsP(n):
    k = np.arange(2, n)
    r = n % k
    if np.any(r == 0):
        return np.nan
    return np.sum(np.log(np.abs(np.sin(np.pi * (r / k)))))


def make_figure_Pn_original(path="fig_Pn_original.png"):
    """P(n) with sign, small n, as a scatter plot -- not bars."""
    Nmax = 36
    ns = np.arange(2, Nmax)
    Pvals = np.array([P_direct(int(n)) for n in ns])
    is_prime = np.array([sympy.isprime(int(n)) for n in ns])

    fig, ax = plt.subplots(figsize=(11, 5))
    ax.axhline(0, color='black', lw=0.8)
    ax.vlines(ns[is_prime], 0, Pvals[is_prime], color='#93c5fd', lw=1, zorder=1)
    ax.plot(ns[is_prime], Pvals[is_prime], 'o', ms=7, color='#2563eb',
            zorder=3, label='n prime ($P\\neq0$)')
    ax.plot(ns[~is_prime], np.zeros(np.sum(~is_prime)), 'o', ms=7,
            color='#dc2626', zorder=3, label='n composite ($P=0$ exactly)')

    for n, v, isp in zip(ns, Pvals, is_prime):
        if isp:
            ax.annotate(f'{n}', (n, v), textcoords="offset points",
                        xytext=(0, 8 if v >= 0 else -14), ha='center',
                        fontsize=7, color='#1e3a8a')

    ax.set_xlabel('n')
    ax.set_ylabel('P(n)')
    ax.set_title(r'$P(n)=\prod_{k=2}^{n-1}\sin(\pi n/k)$ — the original product')
    ax.legend(fontsize=9, loc='lower left')
    plt.tight_layout()
    plt.savefig(path, dpi=150)
    plt.close(fig)


def make_figure_Px_envelope(path="fig_Px_funcion_de_x.png"):
    """P(x) as a function of a real variable x, against its continuous
    envelope, shown with scatter points only -- never bars."""
    Nmax = 45
    ns = np.arange(2, Nmax)
    Pvals = np.array([P_direct(int(n)) for n in ns])
    is_prime = np.array([sympy.isprime(int(n)) for n in ns])

    x_cont = np.linspace(2, Nmax, 2000)
    envelope_up = np.exp(-C * x_cont)
    envelope_dn = -np.exp(-C * x_cont)

    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))

    ax = axes[0]
    ax.plot(x_cont, envelope_up, '-', color='#dc2626', lw=1.8,
            label=r'$x\mapsto e^{-Cx}$ (continuous real function)')
    ax.plot(x_cont, envelope_dn, '-', color='#dc2626', lw=1.8)
    ax.fill_between(x_cont, envelope_dn, envelope_up, color='#dc2626', alpha=0.08)
    ax.plot(ns[is_prime], Pvals[is_prime], 'o', ms=6, color='#2563eb',
            zorder=5, label='P(n), n prime')
    ax.plot(ns[~is_prime], np.zeros(np.sum(~is_prime)), 'o', ms=6,
            color='#16a34a', zorder=5, label='P(n)=0, n composite')
    ax.axhline(0, color='gray', lw=0.5)
    ax.set_xlabel('x')
    ax.set_ylabel('P(x)  /  envelope')
    ax.set_title(r'$P(x)$ as a function of $x$, with its continuous envelope $\pm e^{-Cx}$' +
                 '\n(linear scale, x=2..45)')
    ax.legend(fontsize=9, loc='upper right')

    Nmax2 = 150
    ns2 = np.arange(2, Nmax2)
    logP2 = np.array([logabsP(n) for n in ns2])
    is_prime2 = np.array([sympy.isprime(int(n)) for n in ns2])
    x_cont2 = np.linspace(2, Nmax2, 500)

    ax = axes[1]
    ax.plot(x_cont2, -C * x_cont2, '-', color='#dc2626', lw=1.8,
            label=r'$x\mapsto -Cx$ (continuous real function)')
    ax.plot(ns2[is_prime2], logP2[is_prime2], 'o', ms=4, color='#2563eb',
            label='log|P(n)|, n prime')
    ax.set_xlabel('x')
    ax.set_ylabel('log|P(x)|  /  -Cx')
    ax.set_title(r'Same object on a log scale: $\log|P(x)|$ against the continuous line $-Cx$' +
                 '\n(x=2..150)')
    ax.legend(fontsize=9)

    plt.tight_layout()
    plt.savefig(path, dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    make_figure_Pn_original()
    make_figure_Px_envelope()
    print("Figures written.")
