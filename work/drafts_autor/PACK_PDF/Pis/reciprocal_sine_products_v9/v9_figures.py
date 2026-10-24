"""
v9_figures.py
Regenerates the auxiliary figures of "Reciprocal Sine Products and
Centered Euclidean Kernels" (v9). All text in English. P(n) is displayed
against its genuine continuous envelope x -> e^{-Cx}, with data shown as
clean scatter points, never as bars/histograms.

Run: python3 v9_figures.py
"""

import numpy as np
import sympy
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import special

C = 0.7437948618394004


def logabsP(n):
    k = np.arange(2, n)
    r = n % k
    if np.any(r == 0):
        return -np.inf
    return np.sum(np.log(np.abs(np.sin(np.pi * (r / k)))))


def logPtilde(n):
    k = np.arange(2, n)
    r = n % k
    mask = r != 0
    return np.sum(np.log(np.abs(np.sin(np.pi * (r[mask] / k[mask])))))


def make_figure_Pvs_Ptilde(path="fig_P_vs_Ptilde.png"):
    Nmax = 300
    ns = np.arange(3, Nmax)
    logP_vals = np.array([logabsP(n) for n in ns])
    logPt_vals = np.array([logPtilde(n) for n in ns])
    is_prime = np.array([sympy.isprime(int(n)) for n in ns])

    fig, axes = plt.subplots(1, 2, figsize=(13, 5), sharey=True)

    ax = axes[0]
    ax.plot(ns[is_prime], logP_vals[is_prime], 'o', ms=3, color='#2563eb',
            label='n prime (P!=0)')
    ax.scatter(ns[~is_prime], np.full(np.sum(~is_prime), logP_vals[is_prime].min() - 5),
               marker='|', color='#dc2626', s=40,
               label='n composite (P=0 exactly, off scale)')
    ax.plot(ns, -C * ns, '--', color='gray', lw=1.2, label=r'$-Cn$')
    ax.set_title(r'$P(n)$: exact zero on composites')
    ax.set_xlabel('n'); ax.set_ylabel(r'$\log|P(n)|$')
    ax.legend(fontsize=8)

    ax = axes[1]
    ax.plot(ns[is_prime], logPt_vals[is_prime], 'o', ms=3, color='#2563eb', label='n prime')
    ax.plot(ns[~is_prime], logPt_vals[~is_prime], 'o', ms=3, color='#16a34a',
            label='n composite (zero factors omitted)')
    ax.plot(ns, -C * ns, '--', color='gray', lw=1.2, label=r'$-Cn$ (same $C$)')
    ax.set_title(r'$\widetilde P(n)$: zero factors treated as 1')
    ax.set_xlabel('n')
    ax.legend(fontsize=8)

    plt.tight_layout()
    plt.savefig(path, dpi=150)
    plt.close(fig)


def make_figure_dashboard(path="fig_dashboard.png", p=100003):
    def F(t): return special.digamma(1 + t) - special.digamma(1)
    def rho(t): return special.polygamma(1, 1 + t)

    k = np.arange(2, p)
    r = p % k
    frac = r / k.astype(float)
    frac_sorted = np.sort(frac)

    def Ap(tv):
        return np.searchsorted(frac_sorted, tv, side='right').astype(float)

    ts = np.linspace(1e-4, 1 - 1e-4, 6000)
    Dp = Ap(ts) - p * F(ts) + 2 * ts
    ts_half = np.linspace(1e-4, 0.5, 4000)
    Hp = (Ap(ts_half) - p * F(ts_half) + 2 * ts_half) - \
         (Ap(1 - ts_half) - p * F(1 - ts_half) + 2 * (1 - ts_half))

    fig, axes = plt.subplots(2, 3, figsize=(16, 9))

    t_dense = np.linspace(0.001, 0.999, 2000)
    ax = axes[0, 0]
    ax.plot(t_dense, rho(t_dense), color='#2563eb')
    ax.set_title(r'$\rho(t)=\psi_1(1+t)$' + '\nlimiting density of {n/k} (nonuniform)')
    ax.set_xlabel('t'); ax.set_ylabel(r'$\rho(t)$')
    ax.axhline(np.pi**2 / 6, ls=':', color='gray', lw=0.8)
    ax.text(0.02, np.pi**2 / 6 + 0.05, r'$\rho(0)=\pi^2/6$', fontsize=8)

    ax = axes[0, 1]
    t2 = np.linspace(0.001, 0.999, 2000)
    ell = np.log(2 * np.sin(np.pi * t2))
    ax.plot(t2, ell, color='#dc2626')
    ax.set_title(r'$\ell(t)=\log(2\sin\pi t)$' + '\nkernel whose mean against rho gives the constant C')
    ax.set_xlabel('t'); ax.set_ylabel(r'$\ell(t)$')
    ax.axvline(0.5, ls=':', color='gray', lw=0.8)

    ax = axes[0, 2]
    J = 8
    t3 = np.linspace(0.001, 0.999, 3000)
    KJ = (np.sin((2 * J + 1) * np.pi * t3) / np.sin(np.pi * t3) - 1) / 2
    ax.plot(t3, KJ, color='#16a34a')
    ax.set_title(r'$K_J(t)=\sum_{j=1}^{J}\cos(2\pi jt)$, J=8' + '\nDirichlet kernel: quadrature defect of B_J(p)')
    ax.set_xlabel('t'); ax.set_ylabel(r'$K_J(t)$')

    ax = axes[1, 0]
    ax.plot(ts, Dp, lw=0.6, color='#7c3aed')
    ax.axhline(0, color='gray', lw=0.6)
    ax.set_title('one-sided discrepancy D_p(t)' + f'\n(count of k with {{p/k}}<=t, minus density), p={p}')
    ax.set_xlabel('t'); ax.set_ylabel(r'$D_p(t)$')

    ax = axes[1, 1]
    ax.plot(ts_half, Hp, lw=0.6, color='#ea580c')
    ax.axhline(0, color='gray', lw=0.6)
    ax.set_title('folded discrepancy H_p(t)=D_p(t)-D_p(1-t)' + '\nthe only part that sees log|P(p)|')
    ax.set_xlabel('t'); ax.set_ylabel(r'$H_p(t)$')

    ax = axes[1, 2]
    ax.plot(ts_half, np.abs(Dp[:len(ts_half)]), lw=0.6, color='#7c3aed', alpha=0.6, label=r'$|D_p(t)|$')
    ax.plot(ts_half, np.abs(Hp), lw=0.6, color='#ea580c', alpha=0.8, label=r'$|H_p(t)|$')
    ax.axhline(p**(1 / 3), ls='--', color='k', lw=1, label=r'$p^{1/3}$')
    ax.set_title('Scale comparison\n(open question: is H_p << p^(1/3) with no log?)')
    ax.set_xlabel('t'); ax.legend(fontsize=8)

    plt.tight_layout()
    plt.savefig(path, dpi=145)
    plt.close(fig)


def make_figure_other_functions(path="fig_otras_funciones.png"):
    def ell(x):
        return np.log(np.sin(np.pi * x))

    def Vk(u, k):
        total = np.zeros_like(u)
        for r in range(1, k // 2):
            if np.gcd(r, k) == 1:
                w = -ell(r / k)
                total = total + 2 * w * (1 - np.cos((k / 2 - r) * u))
        return total

    def Cl2(theta, J=400):
        j = np.arange(1, J + 1)
        theta = np.asarray(theta)
        return np.sum(np.sin(np.outer(theta, j)) / j**2, axis=1)

    def h_smooth(u):
        u = np.asarray(u, dtype=float)
        out = np.zeros_like(u)
        mask = u > 1e-9
        out[mask] = np.log(np.sin(np.pi * u[mask]) / (np.pi * u[mask]))
        return out

    fig, axes = plt.subplots(1, 3, figsize=(15, 4.3))

    ax = axes[0]
    u = np.linspace(-3 * np.pi, 3 * np.pi, 2000)
    for k, c in zip([7, 11, 17], ['#2563eb', '#16a34a', '#dc2626']):
        ax.plot(u, Vk(u, k), color=c, label=f'k={k}', lw=1.3)
    ax.axhline(0, color='gray', lw=0.6)
    ax.set_title(r'$V_k(u)$: centered kernel (Theorem 8.2)' + '\nreal, even, nonnegative -- negative type under $V_k(u_i-u_j)$')
    ax.set_xlabel('u'); ax.legend(fontsize=8)

    ax = axes[1]
    th = np.linspace(0, 2 * np.pi, 2000)
    ax.plot(th, Cl2(th), color='#7c3aed')
    ax.axhline(0, color='gray', lw=0.6)
    ax.set_title(r'$\mathrm{Cl}_2(\theta)=\sum_j \sin(j\theta)/j^2$' + '\nClausen function (Sec. 9, incomplete sums)')
    ax.set_xlabel(r'$\theta$')

    ax = axes[2]
    uu = np.linspace(0, 0.5, 2000)
    ax.plot(uu, h_smooth(uu), color='#ea580c')
    ax.set_title(r'$h(u)=\log(\sin\pi u/\pi u)$' + '\nsmooth part (Prop. 6.1); all the singularity\nis confined to $\\log(s_k/k)$')
    ax.set_xlabel('u')

    plt.tight_layout()
    plt.savefig(path, dpi=150)
    plt.close(fig)


def make_figure_convergence(path="fig_convergencia_C.png"):
    Nmax = 4000
    primes = list(sympy.primerange(3, Nmax))
    ratio = [-logabsP(p) / p for p in primes]

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(primes, ratio, '.', ms=3, color='#2563eb', alpha=0.7,
            label=r'$-\log|P(p)|/p$')
    ax.axhline(C, color='#dc2626', lw=1.5, ls='--', label=f'C = {C:.4f}')
    ax.set_xlabel('p (prime)')
    ax.set_ylabel(r'$-\log|P(p)|/p$')
    ax.set_title('Direct convergence of P(x) as a function of x:\n' +
                 r'$-\log|P(p)|/p \to C$ (Theorem 3.5 / 3.2)')
    ax.legend(fontsize=9)
    ax.set_ylim(C - 0.15, C + 0.5)
    plt.tight_layout()
    plt.savefig(path, dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    make_figure_Pvs_Ptilde()
    make_figure_dashboard()
    make_figure_other_functions()
    make_figure_convergence()
    print("Figures written.")
