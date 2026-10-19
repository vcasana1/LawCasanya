#!/usr/bin/env python3
"""v11 = v10 + (1) Theorem D'' : the one-step clock from tau_k with a fixed cutoff exponent has
mean-square error << (1+log log log T)/log^2 T (author's proof with an auxiliary cutoff);
(2) the author's review of v10: Fujii's (alpha') restricted to 0<h<=1, F/mathsf F in the sampling
lemma, t_flat/t_sharp, notation table, mesh step renamed mathsf h_T, disc wording;
(3) the ChatGPT hand-off for v11 (chatgpt/notes/regularized_clock_for_v11_20261019): range
2<=X<=sqrt(T/2) in Theorem D', moments and tails on the clock window I_T^tau, transport there,
certified tolerance of the convex program; (4) the open-problems subsection removed; the sentence
on uncomputed constants kept once.

Run on a copy of ../v10/manuscript/prime_corrected_clock_v10.tex saved as the v11 file name.
Every replacement must match exactly once.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
TEX = ROOT / 'manuscript' / 'prime_corrected_clock_v11.tex'
src = TEX.read_text()
head, sep, body = src.partition('\\begin{document}')
assert sep


def rep(old, new, count=1):
    global body
    n = body.count(old)
    if n != count:
        sys.exit(f'expected {count} match(es), found {n}:\n{old[:300]}')
    body = body.replace(old, new)


# ================================================================ (2) Fujii (alpha'): h <= 1
rep(r"""There are absolute constants $A$ and $T_0$ such that for every integer $k\ge1$, $T\ge T_0$ and $h>0$,
\[
\int_T^{2T}\bigl(S(t+h)-S(t)\bigr)^{2k}dt\ll(Ak)^kT\Bigl(\log\bigl(((h\wedge1)\log T+3)\,e^k\bigr)\Bigr)^k,\qquad h\wedge1=\min\{h,1\},
\]""",
    r"""There are absolute constants $A$ and $T_0$ such that for every integer $k\ge1$, $T\ge T_0$ and $0<h\le1$,
\[
\int_T^{2T}\bigl(S(t+h)-S(t)\bigr)^{2k}dt\ll(Ak)^kT\Bigl(\log\bigl((h\log T+3)\,e^k\bigr)\Bigr)^k,
\]""")
rep(r"""there with $0\le h\le\frac12T$, whereas \cite[\S5-1]{Fujii1981} requires $h$ to be bounded in the asymptotic formula.""",
    r"""there with $0\le h\le\frac12T$, whereas \cite[\S5-1]{Fujii1981} requires $h$ to be bounded in the asymptotic formula ($\alpha$) from which ($\alpha'$) is derived; ($\alpha'$) is printed with $h\wedge1=\min\{h,1\}$ in place of $h$ and without an explicit bound on $h$, but for unbounded $h$ its right side would be independent of $h$, and with $k=1$ that would bound $\int_H^{2H}S^2$ by $O_T(H)$ for every $H$, against Theorem~\CGref{thm:known_selberg_moments}; so it is stated here for $0<h\le1$ only.""")

# ================================================================ (2) sampling lemma: F -> mathsf F
rep(r"""\frac1b\int_{u-b}^uF+\int_{u-b}^u|\mathsf F'|$. Averaging ov""",
    r"""\frac1b\int_{u-b}^u\mathsf F+\int_{u-b}^u|\mathsf F'|$. Averaging ov""")
rep(r"""\frac1b\int_{u-b}^uF+\int_{u-b}^u|\mathsf F'|\Bigr)du\le\fra""",
    r"""\frac1b\int_{u-b}^u\mathsf F+\int_{u-b}^u|\mathsf F'|\Bigr)du\le\fra""")
rep(r"""\sum_kF(\mathsf x_k)\le17\,b^{-1}""", r"""\sum_k\mathsf F(\mathsf x_k)\le17\,b^{-1}""")

# ================================================================ (2) heights
rep(r"""with $|\widehat F(t_i)-N(t_i)|\le K$.""",
    r"""with $|\widehat F(t_\flat)-N(t_\flat)|\le K$ and $|\widehat F(t_\sharp)-N(t_\sharp)|\le K$.""")

# ================================================================ (2) mesh step renamed, notation table
body = body.replace(r'\varsigma_T', r'\mathsf h_T')
rep(r"""$\Lambda_T$, $\mathsf J_T$, $\mathcal K_T$ & $\frac{\log T}{2\pi}$; the block $[\frac T2,3T]$; piecewise linear functions with slopes in $[\frac12\Lambda_T,2\Lambda_T]$ (Section~\CGref{sec:regularized})\\
$\widehat F$, $\widehat x_k$, $\widehat u_k$ & regularized counting model, its level points, its defect at $\gamma_k$ (Section~\CGref{sec:regularized})\\""",
    r"""$\Lambda_T$, $\mathsf J_T$, $\mathsf L_T$, $\mathsf h_T$, $\mathsf t_i$ & $\frac{\log T}{2\pi}$; the block $[\frac T2,3T]$; number of mesh cells, mesh step $\le\Lambda_T^{-1}$, nodes (Section~\CGref{sec:regularized})\\
$\mathcal K_T$, $\mathcal I_T^\tau$ & piecewise linear functions on the mesh with slopes in $[\frac12\Lambda_T,2\Lambda_T]$; the clock window $\{k:T\le\tau_k<2T\}$\\
$\widehat F$, $\widehat x_k$, $\widehat u_k$, $t_\flat$, $t_\sharp$ & regularized counting model, its level points, its defect at $\gamma_k$, the two good heights of its proof (Section~\CGref{sec:regularized})\\
$E$, $E_*$, $\eta_{\rm reg}$, $B_{\rm reg}$ & objective of the convex program, its minimum, tolerance, dual lower bound (Proposition~\CGref{prop:tolerance})\\""")

# ================================================================ (2) discs
rep(r"""with the disc of the proof, and numerically with any single disc, Backlund's method cannot go below $0.4940$.""",
    r"""with the disc of the proof, and numerically among the discs examined, Backlund's method cannot go below $0.4940$.""")

# ================================================================ (1) Theorem D'': fixed cutoff exponent for the one-step clock
rep(r"""\begin{corollary}[A cutoff read off the clock]\label{cor:local_clock}""",
    r"""\begin{theorem}[Theorem D$''$: the one-step clock with a fixed cutoff exponent]\label{thm:fixed_cutoff_step}
There are absolute constants $T_0$ and $C$ such that for $T\ge T_0$ and $(\log\log T)^{-1/2}\le c\le\frac12$, with $X=T^c$,
\begin{equation}
\bigl\langle r_k(X)^2\bigr\rangle_{\IT}\le C(1+\log\log\log T),\qquad
\bigl\langle\mathfrak t_k(X)^2\bigr\rangle_{\IT}\le C(1+\log\log\log T),\qquad
\frac1{\#\IT}\sum_{k\in\IT}\bigl(\tau_k^X-\gamma_k\bigr)^2\le\frac{C(1+\log\log\log T)}{\log^2T}.
\label{eq:fixed_cutoff_step}
\end{equation}
In particular, for every fixed $0<c\le\frac12$ the one-step clock $\tau_k^{T^c}$ has mean-square error $\ll(1+\log\log\log T)/\log^2T$ in height, where Lemma~\CGref{lem:transport} alone gives $\ll(1+c^2\log\log T)/\log^2T$.
\end{theorem}

\begin{proof}
\emph{An auxiliary cutoff.} Let $Y=T^{c_Y}$ with $c_Y=(\log\log T)^{-1/2}$, so that $2\le Y\le X\le T^{1/2}$ for $T\ge T_0$. Corollary~\CGref{cor:computable_clock} gives $\langle r_k(Y)^2\rangle_{\IT}\ll1+\log\log\log T$. The cutoff $Y$ appears only in this proof.

\emph{The exact relation between the two residuals.} By \CGeqref{eq:one_step_clock}, $r_k(X)=\lL(\tau_k)(\tau_k-\gamma_k)-S_X(\tau_k)$, so
\[
r_k(X)=r_k(Y)-\mathfrak D(\tau_k),\qquad\mathfrak D=S_X-S_Y .
\]

\emph{Moments of $\mathfrak D$.} The function $\mathfrak D$ is the part of $S_X$ with primes $Y<p\le X$. Writing it as in Section~\CGref{subsec:euler_phase}, its terms $m=1$ are $\frac1\pi\sum_{Y<p\le X}p^{-1/2}\sin(t\log p)$; Lemma~\CGref{lem:trig_MV} on $[T-1,2T-2]$ and on $[T+1,2T+2]$, whose union contains $[T-1,2T+2]$, with $z_p=\frac1{\pi\sqrt p}$ gives
\[
\int_{T-1}^{2T+2}\Bigl(\frac1\pi\sum_{Y<p\le X}\frac{\sin(t\log p)}{\sqrt p}\Bigr)^2dt\ll T\sum_{Y<p\le X}\frac1p+X+\Bigl(\sum_{p\le X}p^{-1/2}\Bigr)^2\ll T\Bigl(1+\log\frac{\log X}{\log Y}\Bigr),
\]
by Theorem~\CGref{thm:known_mertens} and $X\le T^{1/2}$; the terms $m=2$ contribute $\ll T$ as in the proof of Lemma~\CGref{lem:D_moments}, and the terms $m\ge3$ are bounded. Hence $\int_{T-1}^{2T+2}\mathfrak D^2\ll T(1+\log(c/c_Y))=T(1+\log(c\sqrt{\log\log T}))$. Likewise $\mathfrak D'=S_X'-S_Y'$ and \CGeqref{eq:SX_derivative} on the same two intervals give $\int_{T-1}^{2T+2}\mathfrak D'^2\ll T(1+\log X)^2$.

\emph{Sampling at the clock points.} The intervals $\mathcal U_k=[\tau_k,\tau_k+\mathfrak b_T]$, $k\in\IT$, are disjoint and contained in $[T-1,2T+2]$ (proof of Lemma~\CGref{lem:transport}). For $x\in\mathcal U_k$ and $y\in\mathcal U_k$, $\mathfrak D(x)=\mathfrak D(y)+\int_y^x\mathfrak D'$; averaging over $y$ and using Cauchy--Schwarz, $\mathfrak D(\tau_k)^2\le\frac2{\mathfrak b_T}\int_{\mathcal U_k}\mathfrak D^2+2\mathfrak b_T\int_{\mathcal U_k}\mathfrak D'^2$. Summing over $k\in\IT$ and dividing by $\#\IT\gg T\log T$, with $\mathfrak b_T\asymp1/\log T$,
\[
\bigl\langle\mathfrak D(\tau_k)^2\bigr\rangle_{\IT}\ll\frac1T\int_{T-1}^{2T+2}\mathfrak D^2+\frac1{T\log^2T}\int_{T-1}^{2T+2}\mathfrak D'^2\ll1+\log\bigl(c\sqrt{\log\log T}\bigr)+\frac{(1+\log X)^2}{\log^2T}\ll1+\log\log\log T,
\]
since $c\le\frac12$ and $X\le T^{1/2}$.

\emph{Conclusion.} $\langle r_k(X)^2\rangle\le2\langle r_k(Y)^2\rangle+2\langle\mathfrak D(\tau_k)^2\rangle\ll1+\log\log\log T$, the first bound. By \CGeqref{eq:r_decomposition}, $\mathfrak t_k(X)=r_k(X)-u_k(X)-\chi_k$, with $\langle u_k(X)^2\rangle\ll1+\log(1/c)\le1+\frac12\log\log\log T$ (Theorem~\CGref{thm:main}) and $0\le\chi_k\le1/T$ (Theorem~\CGref{thm:accounting}(a)); this gives the second bound. The third follows from the first as in the proof of Corollary~\CGref{cor:computable_clock}.
\end{proof}

\begin{remark}[What is not proved for a fixed cutoff exponent]\label{rem:fixed_cutoff_heuristic}
Theorem~\CGref{thm:fixed_cutoff_step} improves the factor $c^2\log\log T$ of Lemma~\CGref{lem:transport} to $1+\log\log\log T$, but it does not give $\langle r_k(T^c)^2\rangle_{\IT}=O_c(1)$, which by Remark~\CGref{rem:newton} is equivalent to bounded mean-square transport from $\tau_k$. The following heuristic suggests that the factor cannot be removed. For a fixed displacement $h$, Lemma~\CGref{lem:trig_MV} gives $\frac1T\int_T^{2T}(S_X(t+h)-S_X(t))^2dt\approx\frac1{\pi^2}\sum_{p\le X}\frac{1-\cos(h\log p)}p\approx\frac1{\pi^2}\log(h\log X)$ when $h\log X\gg1$. The transport is such an increment with $h=|\delta_k|$, and $|\delta_k|\log T$ is of order $\sqrt{\log\log T}$ for most $k$ (Remark~\CGref{rem:korolev}(a)), so $h\log X\approx c\sqrt{\log\log T}$; the primes that drive the increment are those between $\exp(\log T/\sqrt{\log\log T})$ and $X$, while $\delta_k$ is governed mainly by the small primes. If the displacement $\delta_k$ and these large-prime phases could be treated as independent, the transport would have mean square $\approx\frac1{2\pi^2}\log(c^2\log\log T)$, of the order of the upper bound \CGeqref{eq:fixed_cutoff_step}. The step from the fixed displacement to $\delta_k$, which depends on the same phases and is sampled at the ordinates, is not justified; no lower bound for the transport is proved here. For the same reason the scale $c\asymp(\log\log T)^{-1/2}$ of Corollary~\CGref{cor:computable_clock} is the one allowed by the available estimates, not a proved minimizer of the true error. The regularized points of Theorem~\CGref{thm:regularized_clock} avoid the transport from $\tau_k$ altogether.
\end{remark}

\begin{corollary}[A cutoff read off the clock]\label{cor:local_clock}""")

# ================================================================ rem:newton: no heuristic contradicted by Theorem D''; no Question
rep(r"""Lemma~\CGref{lem:transport} gives only the upper bound $\langle\mathfrak t_k(X)^2\rangle_{\IT}\ll c^2\log\log T$, and whether the transport is bounded for fixed $c$ is open (Question~\CGref{q:fixed_c}). A heuristic count, treating $S_X(\tau_k)$ and $S_X'(\xi^X_k)$ as uncorrelated with $\langle S_X^2\rangle\approx\frac1{2\pi^2}\log\log X$ and $\langle S_X'^2\rangle/\lL(T)^2\approx c^2$, would give the Newton term a mean square of order $c^2\log\log T$; this is not proved, and it is not a lower bound for the transport.""",
    r"""Lemma~\CGref{lem:transport} gives the upper bound $\langle\mathfrak t_k(X)^2\rangle_{\IT}\ll c^2\log\log T$, and Theorem~\CGref{thm:fixed_cutoff_step} below improves it to $\ll1+\log\log\log T$ for $c\ge(\log\log T)^{-1/2}$; whether the transport is bounded for fixed $c$ is not decided here (Remark~\CGref{rem:fixed_cutoff_heuristic}).""")

# ================================================================ (3) Theorem D': range sqrt(T/2), clock window, tails
rep(r"""\begin{lemma}[The prime model on the block]\label{lem:block_fourth}
There are absolute constants $T_0$ and $C$ such that for $T\ge T_0$ and $2\le X\le T^{1/3}$, with $c=\log X/\log T$,""",
    r"""\begin{lemma}[The prime model on the block]\label{lem:block_fourth}
There are absolute constants $T_0$ and $C$ such that for $T\ge T_0$ and $2\le X\le\sqrt{T/2}$, with $c=\log X/\log T$,""")
rep(r"""which cover $\mathsf J_T$: for $T\ge T_0$, $2\le X\le T^{1/3}\le T'^{1/2}$, and by Lemma~\CGref{lem:V_size}""",
    r"""which cover $\mathsf J_T$: for $T\ge T_0$, $2\le X\le(T/2)^{1/2}\le T'^{1/2}$, and by Lemma~\CGref{lem:V_size}""")
rep(r"""There are absolute constants $T_0$ and $C$ such that for $T\ge T_0$ and $2\le X\le T^{1/3}$, with $c=\log X/\log T$ and $\widehat F$, $\widehat x_k$, $\widehat u_k$ as in Definition~\CGref{def:regularized}:
\begin{enumerate}[label=(\alph*),leftmargin=2em]
\item $\widehat x_k$ is defined for every $k\in\IT\cup\mathcal I_T^\tau$, $\mathcal I_T^\tau=\{k:T\le\tau_k<2T\}$, and these points are increasing in $k$ with gaps \CGeqref{eq:regularized_gaps};
\item $\langle\widehat u_k^4\rangle_{\IT}\le C(1+\log(1/c))^2$ and $|\widehat x_k-\gamma_k|\le4\pi|\widehat u_k|/\log T$; hence
\begin{equation}
\bigl\langle|\widehat x_k-\gamma_k|^4\bigr\rangle_{\IT}\le\frac{C(1+\log(1/c))^2}{\log^4T},\qquad\bigl\langle|\widehat x_k-\gamma_k|^2\bigr\rangle_{\IT}\le\frac{C(1+\log(1/c))}{\log^2T};
\label{eq:regularized_main}
\end{equation}
\item $\max_{k\in\IT}|\widehat x_k-\gamma_k|\le CT^{1/5}$;
\item if $X\le T^{1/4}$, then $\bigl\langle(S_X(\gamma_k)-S_X(\widehat x_k))^2\bigr\rangle_{\IT}\le C(1+\log(1/c))\bigl((1+\log X)/\log T\bigr)^2\ll1$, with an absolute implied constant.
\end{enumerate}
\end{theorem}""",
    r"""There are absolute constants $T_0$ and $C$ such that for $T\ge T_0$ and $2\le X\le\sqrt{T/2}$, with $c=\log X/\log T$ and $\widehat F$, $\widehat x_k$, $\widehat u_k$ as in Definition~\CGref{def:regularized}, and with $\mathcal I$ either of the index sets $\IT$ and $\mathcal I_T^\tau=\{k:T\le\tau_k<2T\}$:
\begin{enumerate}[label=(\alph*),leftmargin=2em]
\item $\widehat x_k$ is defined for every $k\in\IT\cup\mathcal I_T^\tau$, and these points are increasing in $k$ with gaps \CGeqref{eq:regularized_gaps};
\item $\langle\widehat u_k^4\rangle_{\mathcal I}\le C(1+\log(1/c))^2$ and $|\widehat x_k-\gamma_k|\le4\pi|\widehat u_k|/\log T$; hence
\begin{equation}
\bigl\langle|\widehat x_k-\gamma_k|^4\bigr\rangle_{\mathcal I}\le\frac{C(1+\log(1/c))^2}{\log^4T},\qquad\bigl\langle|\widehat x_k-\gamma_k|^2\bigr\rangle_{\mathcal I}\le\frac{C(1+\log(1/c))}{\log^2T},
\label{eq:regularized_main}
\end{equation}
and for every $\lambda>0$
\begin{equation}
\frac{\#\{k\in\mathcal I:|\widehat x_k-\gamma_k|>\lambda\cdot2\pi/\log T\}}{\#\mathcal I}\le\frac{C(1+\log(1/c))^2}{(2\pi\lambda)^4};
\label{eq:regularized_tails}
\end{equation}
\item $\max_{k\in\IT\cup\mathcal I_T^\tau}|\widehat x_k-\gamma_k|\le CT^{1/5}$;
\item if $X\le T^{1/4}$, then $\bigl\langle(S_X(\gamma_k)-S_X(\widehat x_k))^2\bigr\rangle_{\mathcal I}\le C(1+\log(1/c))\bigl((1+\log X)/\log T\bigr)^2\ll1$, with an absolute implied constant.
\end{enumerate}
In particular every fixed $0<c<\frac12$ is admissible for $T\ge T_0(c)$, with the constant $C$ independent of $c$.
\end{theorem}""")
rep(r"""$\widehat F(\frac T2)<k-\frac12<\widehat F(3T)$ for $T\ge T_0$. Monotonicity and gaps are Lemma~\CGref{lem:regularized_def}.""",
    r"""$\widehat F(\frac T2)<k-\frac12<\widehat F(3T)$ for $T\ge T_0$. Monotonicity and gaps are Lemma~\CGref{lem:regularized_def}. Both index sets have $\asymp T\log T$ elements, and for $k\in\mathcal I_T^\tau$ the ordinate $\gamma_k$ lies in $[T-C_{10},2T+C_{10}]$ ($|\delta_k|\le C_{10}$, Theorem~\CGref{thm:known_basic}).""")
rep(r"""so $[\gamma_{k_1},\gamma_{k_2}]\subset(\frac T2,3T)$ and $\IT\subset\{k:k_1<k<k_2\}$.""",
    r"""so $[\gamma_{k_1},\gamma_{k_2}]\subset(\frac T2,3T)$ and $\IT\cup\mathcal I_T^\tau\subset\{k:k_1<k<k_2\}$, because $\gamma_{k_1}\le t_\flat\le\frac{3T}4<T-C_{10}$ and $\gamma_{k_2}>t_\sharp\ge\frac{9T}4>2T+C_{10}$.""")
rep(r"""\sum_{k\in\IT}\widehat u_k^4\le\sum_{k_1<k<k_2}\Psi_2(\widehat u_k)&=""",
    r"""\sum_{k\in\mathcal I}\widehat u_k^4\le\sum_{k_1<k<k_2}\Psi_2(\widehat u_k)&=""")
rep(r"""and $\#\IT\asymp T\log T$ gives the bound for $\langle\widehat u_k^4\rangle_{\IT}$. Since $\widehat F(\gamma_k)-\widehat F(\widehat x_k)=-\widehat u_k$ and $\widehat F'\ge\frac12\Lambda_T$, $|\widehat x_k-\gamma_k|\le2|\widehat u_k|/\Lambda_T=4\pi|\widehat u_k|/\log T$, which gives \CGeqref{eq:regularized_main}, the second bound by Cauchy--Schwarz.""",
    r"""and $\#\mathcal I\asymp T\log T$ gives the bound for $\langle\widehat u_k^4\rangle_{\mathcal I}$, for either index set. Since $\widehat F(\gamma_k)-\widehat F(\widehat x_k)=-\widehat u_k$ and $\widehat F'\ge\frac12\Lambda_T$, $|\widehat x_k-\gamma_k|\le2|\widehat u_k|/\Lambda_T=4\pi|\widehat u_k|/\log T$, which gives \CGeqref{eq:regularized_main}, the second bound by Cauchy--Schwarz, and \CGeqref{eq:regularized_tails} by Markov's inequality.""")
rep(r"""\emph{(c).} Let $d=|\widehat x_k-\gamma_k|>0$.""",
    r"""\emph{(c).} Let $k\in\IT\cup\mathcal I_T^\tau$, so that $\gamma_k$ and $\widehat x_k$ lie in $\mathsf J_T$, and let $d=|\widehat x_k-\gamma_k|>0$.""")
rep(r"""\emph{(d).} By (c), for $k\in\IT$ the interval""",
    r"""\emph{(d).} By (c), for $k\in\mathcal I$ the interval""")
rep(r"""every interval of length $\mathfrak b_T$ contains at most $2$ of the points $\widehat x_k$, so $\tilde n\le2$ and $\int_\R\tilde n^2\le2\int_\R\tilde n=2\mathfrak b_T\#\IT$ in Lemma~\CGref{lem:sampling_rho}, which with $r=1$ and $X\le T^{1/4}$ gives $\langle g(\widehat x_k)^4\rangle_{\IT}\ll(1+\log X)^4$ for $g=\mathcal M(\varphi S'_X)$.""",
    r"""every interval of length $\mathfrak b_T$ contains at most $2$ of the points $\widehat x_k$, so $\tilde n\le2$ and $\int_\R\tilde n^2\le2\int_\R\tilde n=2\mathfrak b_T\#\mathcal I$ in Lemma~\CGref{lem:sampling_rho}, which with $r=1$ and $X\le T^{1/4}$ gives $\langle g(\widehat x_k)^4\rangle_{\mathcal I}\ll(1+\log X)^4$ for $g=\mathcal M(\varphi S'_X)$; the proof of that lemma uses of its index set only that it has $\asymp T\log T$ elements and that the points lie in $[T-2T^{1/2},2T+2T^{1/2}]$, so it applies to $\mathcal I_T^\tau$ as well.""")
rep(r"""\bigl\langle(S_X(\gamma_k)-S_X(\widehat x_k))^2\bigr\rangle_{\IT}\le4\bigl\langle|\gamma_k-\widehat x_k|^4\bigr\rangle_{\IT}^{1/2}\bigl\langle g(\widehat x_k)^4\bigr\rangle_{\IT}^{1/2}\ll(1+\log(1/c))\frac{(1+\log X)^2}{\log^2T},""",
    r"""\bigl\langle(S_X(\gamma_k)-S_X(\widehat x_k))^2\bigr\rangle_{\mathcal I}\le4\bigl\langle|\gamma_k-\widehat x_k|^4\bigr\rangle_{\mathcal I}^{1/2}\bigl\langle g(\widehat x_k)^4\bigr\rangle_{\mathcal I}^{1/2}\ll(1+\log(1/c))\frac{(1+\log X)^2}{\log^2T},""")

# ================================================================ (3) tolerance of the convex program
rep(r"""\begin{remark}\label{rem:regularized}""",
    r"""\subsection{A certified tolerance for the convex program}
\label{subsec:tolerance}
The minimizer $\widehat F$ is computed by an iterative solver. The following statement shows that an approximate minimizer with a controlled excess of the objective gives points with the same guarantee, and that the excess can be certified from the data of the program alone. Write $P_{\mathbf v}\in\mathcal K_T$ for the function with nodal values $\mathbf v=(v_0,\dots,v_{\mathsf L_T})$,
\[
E(\mathbf v)=\int_{\mathsf J_T}|P_{\mathbf v}-F_X|^4\,dt,\qquad E_*=\min_{P_{\mathbf v}\in\mathcal K_T}E(\mathbf v)=E(\widehat F).
\]

\begin{proposition}[Approximate minimizers and a dual certificate]\label{prop:tolerance}
Let $T$, $X$, $c$ be as in Theorem~\CGref{thm:regularized_clock} and $0\le\eta_{\rm reg}\le1$.
\begin{enumerate}[label=(\alph*),leftmargin=2em]
\item If $P_{\mathbf v}\in\mathcal K_T$ satisfies $E(\mathbf v)\le E_*+\eta_{\rm reg}T$, and $\widehat x_k^{(\mathbf v)}$ are its level points, $P_{\mathbf v}(\widehat x_k^{(\mathbf v)})=k-\frac12$, then (a)--(c) of Theorem~\CGref{thm:regularized_clock} hold for these points with $(1+\log(1/c))^2$ replaced by $(1+\log(1/c))^2+\eta_{\rm reg}$ in \CGeqref{eq:regularized_main}, \CGeqref{eq:regularized_tails} and (c), and (d) holds unchanged.
\item Let $\mathsf D\mathbf v=(v_i-v_{i-1})_{1\le i\le\mathsf L_T}$, $\mathsf a=\frac12\Lambda_T$, $\mathsf b=2\Lambda_T$, $|\mathsf J_T|=\frac52T$, and for $\boldsymbol\mu_\pm\in\R^{\mathsf L_T}$ with nonnegative entries
\[
\begin{split}
\mathscr L(\mathbf v,\boldsymbol\mu_+,\boldsymbol\mu_-)&=E(\mathbf v)+\boldsymbol\mu_+^{\mathsf T}(\mathsf D\mathbf v-\mathsf b\mathsf h_T\mathbf 1)+\boldsymbol\mu_-^{\mathsf T}(\mathsf a\mathsf h_T\mathbf 1-\mathsf D\mathbf v),\\
\mathbf r&=\nabla E(\mathbf v)+\mathsf D^{\mathsf T}(\boldsymbol\mu_+-\boldsymbol\mu_-),\qquad A=\frac{\mathsf h_T^2}{108\,|\mathsf J_T|},\qquad
B_{\rm reg}=\mathscr L(\mathbf v,\boldsymbol\mu_+,\boldsymbol\mu_-)-\frac3{4^{4/3}}A^{-1/3}\|\mathbf r\|_2^{4/3},
\end{split}
\]
where $\partial_iE(\mathbf v)=4\int_{\mathsf J_T}(P_{\mathbf v}-F_X)^3\mathsf B_i\,dt$ and $\mathsf B_i$ is the hat function of the node $\mathsf t_i$. Then $B_{\rm reg}\le E_*$ for every $\mathbf v\in\R^{\mathsf L_T+1}$. Consequently, if $P_{\mathbf v}\in\mathcal K_T$, $\boldsymbol\mu_\pm\ge0$ and $E(\mathbf v)-B_{\rm reg}\le\eta_{\rm reg}T$, then $E(\mathbf v)\le E_*+\eta_{\rm reg}T$.
\end{enumerate}
All quantities in (b) are computed from $\NO$, the primes $p\le X$ and the mesh; no zero and no value of $\zeta$ enters.
\end{proposition}

\begin{proof}
(a) In \CGeqref{eq:regularized_close} replace $\|\widehat F-F_X\|_4\le\|P_N-F_X\|_4$ by $\|P_{\mathbf v}-F_X\|_4\le(E_*+\eta_{\rm reg}T)^{1/4}\le\|P_N-F_X\|_4+(\eta_{\rm reg}T)^{1/4}$, so that $\int_{\mathsf J_T}|P_{\mathbf v}-N|^4\le8\bigl(C_{\rm r}T(1+\log(1/c))^2+\eta_{\rm reg}T\bigr)$. The rest of the proof of Theorem~\CGref{thm:regularized_clock} uses of $\widehat F$ only its membership in $\mathcal K_T$ and this bound; with $K^4=16\cdot8(C_{\rm r}(1+\log(1/c))^2+\eta_{\rm reg})$ and $\eta_{\rm reg}\le1$ the good heights exist and the boundary terms are bounded as before. In (d), $(1+\log(1/c))^2+\eta_{\rm reg}\le2(1+\log(1/c))^2$.

(b) For real $x$ and $d$, $(x+d)^4-x^4-4x^3d-\frac13d^4=6d^2(x+\frac d3)^2\ge0$. Integrating with $x=P_{\mathbf v}-F_X$ and $d=P_{\mathbf d}$, $E(\mathbf v+\mathbf d)\ge E(\mathbf v)+\nabla E(\mathbf v)^{\mathsf T}\mathbf d+\frac13\int_{\mathsf J_T}P_{\mathbf d}^4$. By Cauchy--Schwarz, $\int_{\mathsf J_T}P_{\mathbf d}^4\ge|\mathsf J_T|^{-1}(\int_{\mathsf J_T}P_{\mathbf d}^2)^2$, and $\int_{\mathsf J_T}P_{\mathbf d}^2=\mathbf d^{\mathsf T}\mathsf M\mathbf d$ with the tridiagonal mass matrix $\mathsf M$ of the hat functions, whose diagonal entries are $\frac23\mathsf h_T$ ($\frac13\mathsf h_T$ at the two ends) and whose off-diagonal entries are $\frac16\mathsf h_T$; Gershgorin's theorem gives $\lambda_{\min}(\mathsf M)\ge\frac16\mathsf h_T$. Hence $\frac13\int P_{\mathbf d}^4\ge A\|\mathbf d\|_2^4$. The constraint terms of $\mathscr L$ are linear in $\mathbf v$, so $\mathscr L(\mathbf v+\mathbf d,\boldsymbol\mu_\pm)\ge\mathscr L(\mathbf v,\boldsymbol\mu_\pm)+\mathbf r^{\mathsf T}\mathbf d+A\|\mathbf d\|_2^4\ge\mathscr L(\mathbf v,\boldsymbol\mu_\pm)-\frac3{4^{4/3}}A^{-1/3}\|\mathbf r\|_2^{4/3}=B_{\rm reg}$ for every $\mathbf d$, by minimizing $-\|\mathbf r\|_2s+As^4$ over $s\ge0$. For feasible $\mathbf w$ (that is $P_{\mathbf w}\in\mathcal K_T$) and $\boldsymbol\mu_\pm\ge0$ the constraint terms are $\le0$, so $E(\mathbf w)\ge\mathscr L(\mathbf w,\boldsymbol\mu_\pm)\ge B_{\rm reg}$; taking $\mathbf w$ the minimizer gives $E_*\ge B_{\rm reg}$. The last assertion follows.
\end{proof}

A numerical certification would require enclosures of the integrals, the gradient and the inequalities in directed rounding; no solver was run for this paper, and the certificate controls the computation of the minimizer, not the constants $T_0$ and $C$.

\begin{remark}\label{rem:regularized}""")

# ================================================================ remark regularized: no Question; constants once
rep(r"""(a) Compared with Theorem~\CGref{thm:uniform_iteration} and Corollary~\CGref{cor:sorted_clock}, Theorem~\CGref{thm:regularized_clock} reaches the scale of one mean spacing with a fixed cutoff exponent and without Newton iteration, in fourth mean, with increasing and separated points; the dependence on $c$ is explicit and parallel to Theorem~\CGref{thm:main}. Markov's inequality gives, for $\lambda>0$, $\#\{k\in\IT:|\widehat x_k-\gamma_k|>\lambda\cdot\frac{2\pi}{\log T}\}\le C(1+\log(1/c))^2(2\pi\lambda)^{-4}\#\IT$. The constants $T_0$ and $C$ are not computed. (b)""",
    r"""(a) Compared with Theorem~\CGref{thm:uniform_iteration} and Corollary~\CGref{cor:sorted_clock}, Theorem~\CGref{thm:regularized_clock} reaches the scale of one mean spacing with a fixed cutoff exponent and without Newton iteration, in fourth mean, with increasing and separated points, on the clock window $\mathcal I_T^\tau$ as well as on $\IT$; the dependence on $c$ is explicit and parallel to Theorem~\CGref{thm:main}. The separation \CGeqref{eq:regularized_gaps} is imposed by the slope constraints; it is not a statement about the spacings of the zeros. (b)""")
rep(r"""(c) Part (d) bounds the transport from the regularized points, not from $\tau_k$: Question~\CGref{q:fixed_c} for the one-step clock $\tau_k^X$ remains open.""",
    r"""(c) Part (d) bounds the transport from the regularized points, not from $\tau_k$; for the one-step clock $\tau_k^X$ with a fixed cutoff exponent, Theorem~\CGref{thm:fixed_cutoff_step} gives $1+\log\log\log T$, and $O_c(1)$ is not proved (Remark~\CGref{rem:fixed_cutoff_heuristic}).""")

# ================================================================ (4) open problems removed; constants once
rep(r"""Rounding the corrected count to the nearest integer therefore fails to reproduce $N(t)$, for small cutoffs, on a set of $t$ of positive density: the obstruction is the size of $S-S_X$, not the sawtooth $N-\NO$. The proposition concerns the measure of a set of $t$; it does not give, without a further argument on the values at the $\gamma_k$, a positive proportion of ordinates to which rounding assigns a wrong index. For $c$ near $\frac12$ the question depends on the constant in \CGeqref{eq:main_theorem} (Question~\CGref{q:constant}), and for $c>\frac12$ nothing is proved.""",
    r"""Rounding the corrected count to the nearest integer therefore fails to reproduce $N(t)$, for small cutoffs, on a set of $t$ of positive density: the obstruction is the size of $S-S_X$, not the sawtooth $N-\NO$. The proposition concerns the measure of a set of $t$; it does not give, without a further argument on the values at the $\gamma_k$, a positive proportion of ordinates to which rounding assigns a wrong index. For $c$ near $\frac12$ the answer depends on the constant in \CGeqref{eq:main_theorem}, and for $c>\frac12$ nothing is proved.""")
rep(r"""\subsection{Open problems}
\begin{question}\label{q:constant}
For fixed $c\in(0,\frac12]$, do the bounded means of $u_k(T^c)^2$ converge, and to $(2\pi^2)^{-1}\log(1/c)$ plus which constant?
\end{question}

\begin{question}\label{q:fixed_c}
For the regularized points of Theorem~\CGref{thm:regularized_clock} a fixed $c$ suffices. For the one-step clock $\tau_k^X$ from $\tau_k$: does $\langle r_k(T^c)^2\rangle_{\IT}$ stay bounded for fixed $c$, that is (Remark~\CGref{rem:newton}), is $\langle\mathfrak t_k(T^c)^2\rangle_{\IT}$ bounded? Is the error of the corrected clock after $\log^*T+O(1)$ steps, or of $\widehat x_k$, bounded in units of zeros for \emph{almost every} index, and not only in mean? Can the regularization be localized to windows of bounded length in units of mean spacings with the same bound? Can Theorems~\CGref{thm:main} and \CGref{thm:computable_clock} be extended to $c>\frac12$?
\end{question}

\begin{question}\label{q:explicit}
Can the absolute constants $C_\star$, $H^*$ and $B_\star$ of Theorem~\CGref{thm:uniform_iteration}, and those of Fujii's and Montgomery--Vaughan's bounds on which they rest, be made explicit, so that the cutoff law \CGeqref{eq:cutoff_law} becomes a formula that can be evaluated at a given height?
\end{question}

Theorem~\CGref{thm:identity_general}""",
    r"""\subsection{Scope}
Theorem~\CGref{thm:identity_general}""")
rep(r"""Questions~\CGref{q:constant}--\CGref{q:explicit} & open & what remains to be proved & --\\
""", "")
rep(r"""\emph{Theorem}, \emph{Proposition}, \emph{Lemma} and \emph{Corollary} are proved here unconditionally, from the external results of Section~\CGref{sec:known_results}; \emph{Question} names an open problem.""",
    r"""\emph{Theorem}, \emph{Proposition}, \emph{Lemma} and \emph{Corollary} are proved here unconditionally, from the external results of Section~\CGref{sec:known_results}.""")
rep(r"""constants in the $O$-terms of Theorems B--D$'$ are absolute but not computed.""",
    r"""constants in the $O$-terms of Theorems B--E are absolute but not computed, and the same holds for $T_0$; making them explicit would require explicit forms of Selberg's and Fujii's estimates.""")
rep(r"""fixed in the proof, which are not computed here; once they are fixed""", r"""fixed in the proof; once they are fixed""")
rep(r"""after $\log^*T+O(1)$ steps the error is $O(1)$ mean spacings, using no ordinate; the cutoffs involve absolute constants that are not computed.""",
    r"""after $\log^*T+O(1)$ steps the error is $O(1)$ mean spacings, using no ordinate; with a fixed cutoff exponent the one-step clock has error $\ll(1+\log\log\log T)/\log^2T$ (Theorem~\CGref{thm:fixed_cutoff_step}).""")
rep(r"""through absolute constants that are not computed, locates""", r"""through absolute constants, locates""")

# ================================================================ abstract, intro, tables: ranges and D''
rep(r"""uniformly for $2\le X\le T^{1/3}$: no Newton iteration is needed and a fixed power of the height suffices; (E)""",
    r"""uniformly for $2\le X\le\sqrt{T/2}$, on the window $T\le\tau_k<2T$ defined by the clock as well as on $T<\gamma_k\le2T$: no Newton iteration is needed and a fixed power of the height suffices; an approximate minimizer with certified objective excess gives the same bounds; (D$''$) for the one-step clock itself with a fixed cutoff exponent, $\langle(\tau_k^{T^c}-\gamma_k)^2\rangle\ll(1+\log\log\log T)/\log^2T$ uniformly for $(\log\log T)^{-1/2}\le c\le\frac12$; (E)""")
rep(r"""and (D$'$), for $X\le T^{1/3}$, about points defined by a convex program in $\NO$ and $S_X$.""",
    r"""and (D$'$), for $X\le\sqrt{T/2}$, about points defined by a convex program in $\NO$ and $S_X$.""")
rep(r"""and for $p_N\le T^{1/3}$ Theorem D$'$ is a statement about points defined by a convex program in $\NO$ and $S_X$ (Table~\CGref{tab:evaluates});""",
    r"""and for $p_N\le\sqrt{T/2}$ Theorem D$'$ is a statement about points defined by a convex program in $\NO$ and $S_X$ (Table~\CGref{tab:evaluates});""")
rep(r"""and, for $p_N\le T^{1/3}$, Theorem~\CGref{thm:regularized_clock} by one convex regularization with a fixed cutoff exponent.\\""",
    r"""and, for $p_N\le\sqrt{T/2}$, Theorem~\CGref{thm:regularized_clock} by one convex regularization with a fixed cutoff exponent.\\""")
rep(r"""(Theorem~\CGref{thm:regularized_clock}). Let $2\le X\le T^{1/3}$, $c=\log X/\log T$, and let $\widehat F$""",
    r"""(Theorem~\CGref{thm:regularized_clock}). Let $2\le X\le\sqrt{T/2}$, $c=\log X/\log T$, and let $\widehat F$""")
rep(r"""with absolute constants. For fixed $c$ this is the scale of one mean spacing, reached without Newton iteration or sorting, with a fixed cutoff exponent. If $X\le T^{1/4}$, the transport $S_X(\gamma_k)-S_X(\widehat x_k)$ is bounded in mean square.""",
    r"""with absolute constants, over $T<\gamma_k\le2T$ and equally over the window $T\le\tau_k<2T$ defined by the clock; the tails are $\ll(1+\log\frac1c)^2\lambda^{-4}$ at $\lambda$ mean spacings. For fixed $c$ this is the scale of one mean spacing, reached without Newton iteration or sorting, with a fixed cutoff exponent. If $X\le T^{1/4}$, the transport $S_X(\gamma_k)-S_X(\widehat x_k)$ is bounded in mean square. An approximate minimizer whose objective exceeds the minimum by at most $\eta T$, $\eta\le1$, gives the same bounds with $(1+\log\frac1c)^2+\eta$, and the excess is certified by an explicit dual bound computed from the data of the program (Proposition~\CGref{prop:tolerance}).""")
rep(r"""\item \textbf{The pointwise envelope} (Proposition~\CGref{prop:envelope_equivalence} and Theorem~\CGref{thm:envelope}).""",
    r"""\item[\textbf{D$''$.}] \textbf{The one-step clock with a fixed cutoff exponent} (Theorem~\CGref{thm:fixed_cutoff_step}). Uniformly for $(\log\log T)^{-1/2}\le c\le\frac12$,
\begin{equation}
\frac1{\#\IT}\sum_{k\in\IT}\bigl(\tau_k^{T^c}-\gamma_k\bigr)^2\ll\frac{1+\log\log\log T}{\log^2T},\qquad\bigl\langle\mathfrak t_k(T^c)^2\bigr\rangle_{\IT}\ll1+\log\log\log T,
\label{eq:intro_Dpp}
\end{equation}
by comparison with the cutoff $T^{1/\sqrt{\log\log T}}$ inside the proof; the transport bound of Theorem D, $c^2\log\log T$, is replaced by its logarithm. Whether the factor $\log\log\log T$ can be removed is not decided; a heuristic in Remark~\CGref{rem:fixed_cutoff_heuristic} suggests that it cannot.
\item \textbf{The pointwise envelope} (Proposition~\CGref{prop:envelope_equivalence} and Theorem~\CGref{thm:envelope}).""")
rep(r"""Theorem~\CGref{thm:regularized_clock} (D$'$) & unconditional & no Newton iteration, fixed cutoff exponent, fourth mean $O(1)$ mean spacings, separated increasing points & no ($\NO$, primes)\\""",
    r"""Theorem~\CGref{thm:regularized_clock} (D$'$), Proposition~\CGref{prop:tolerance} & unconditional & no Newton iteration, fixed cutoff exponent, fourth mean $O(1)$ mean spacings on the clock window, separated increasing points, certified tolerance & no ($\NO$, primes)\\
Theorem~\CGref{thm:fixed_cutoff_step} (D$''$) & unconditional & one-step clock, fixed cutoff exponent, error $\ll(1+\log\log\log T)$ in units of zeros & no ($k$, $\tau_k$, primes)\\""")
rep(r"""& $\NO$ and the primes $p\le T^c$, $c$ fixed; one convex program on $[\frac T2,3T]$ and linear interpolation. No $\zeta$, no zero.
& Proved: $\langle|\widehat x_k-\gamma_k|^4\rangle\ll(1+\log\frac1c)^2/\log^4T$; increasing points with gaps in $[\pi/\log T,4\pi/\log T]$.\\""",
    r"""& $\NO$ and the primes $p\le T^c$, $c<\frac12$ fixed; one convex program on $[\frac T2,3T]$ and linear interpolation; a dual certificate for the solver. No $\zeta$, no zero.
& Proved: $\langle|\widehat x_k-\gamma_k|^4\rangle\ll(1+\log\frac1c)^2/\log^4T$ on $T<\gamma_k\le2T$ and on $T\le\tau_k<2T$; increasing points with gaps in $[\pi/\log T,4\pi/\log T]$.\\""")
rep(r"""explicit Newton-type steps give points with proved error, and so does, for $X\le T^{1/3}$, a convex regularization with a fixed cutoff exponent,""",
    r"""explicit Newton-type steps give points with proved error, and so does, for $X\le\sqrt{T/2}$, a convex regularization with a fixed cutoff exponent,""")
rep(r"""gives, without Newton iteration and with $X=T^c$, increasing points separated by at least $\pi/\log T$ with $\langle|\widehat x_k-\gamma_k|^4\rangle\ll(1+\log\frac1c)^2/\log^4T$; no ordinate enters the construction, which is global on the block $[\frac T2,3T]$.""",
    r"""gives, without Newton iteration and with $X=T^c$, $c<\frac12$, increasing points separated by at least $\pi/\log T$ with $\langle|\widehat x_k-\gamma_k|^4\rangle\ll(1+\log\frac1c)^2/\log^4T$ on the clock window; no ordinate enters the construction, which is global on the block $[\frac T2,3T]$, and an approximate minimizer with certified excess has the same guarantee. For the one-step clock from $\tau_k$ with a fixed cutoff exponent the error is $\ll(1+\log\log\log T)/\log^2T$ (Theorem~\CGref{thm:fixed_cutoff_step}); whether it is $O_c(1)$ mean spacings is not decided.""")
rep(r"""Section~\CGref{sec:iteration} iterates the Newton-type step uniformly in the number of steps, Section~\CGref{sec:regularized} proves Theorem D$'$, and Section~\CGref{sec:envelope} proves Theorem E.""",
    r"""Section~\CGref{sec:iteration} iterates the Newton-type step uniformly in the number of steps, Section~\CGref{sec:regularized} proves Theorem D$'$ and the tolerance certificate, and Section~\CGref{sec:envelope} proves Theorem E; Theorem D$''$ is proved in Section~\CGref{sec:computable}.""")
rep(r"""which is an upper bound and not the size of the transport. With $X=T^{1/\sqrt{\log\log T}}$,""",
    r"""which is an upper bound and not the size of the transport (for $c\ge(\log\log T)^{-1/2}$ Theorem~\CGref{thm:fixed_cutoff_step} replaces it by $1+\log\log\log T$). With $X=T^{1/\sqrt{\log\log T}}$,""")

# ================================================================ fixes after first build
rep(r"""is an explicit expression in $k$, $\tau_k$ and the primes (Question~\CGref{q:explicit}).""",
    r"""is an explicit expression in $k$, $\tau_k$ and the primes.""")
rep(r"""\begin{equation}
\bigl\langle r_k(X)^2\bigr\rangle_{\IT}\le C(1+\log\log\log T),\qquad
\bigl\langle\mathfrak t_k(X)^2\bigr\rangle_{\IT}\le C(1+\log\log\log T),\qquad
\frac1{\#\IT}\sum_{k\in\IT}\bigl(\tau_k^X-\gamma_k\bigr)^2\le\frac{C(1+\log\log\log T)}{\log^2T}.
\label{eq:fixed_cutoff_step}
\end{equation}""",
    r"""\begin{equation}
\begin{gathered}
\bigl\langle r_k(X)^2\bigr\rangle_{\IT}\le C(1+\log\log\log T),\qquad
\bigl\langle\mathfrak t_k(X)^2\bigr\rangle_{\IT}\le C(1+\log\log\log T),\\
\frac1{\#\IT}\sum_{k\in\IT}\bigl(\tau_k^X-\gamma_k\bigr)^2\le\frac{C(1+\log\log\log T)}{\log^2T}.
\end{gathered}
\label{eq:fixed_cutoff_step}
\end{equation}""")
rep(r"""\[
\bigl\langle\mathfrak D(\tau_k)^2\bigr\rangle_{\IT}\ll\frac1T\int_{T-1}^{2T+2}\mathfrak D^2+\frac1{T\log^2T}\int_{T-1}^{2T+2}\mathfrak D'^2\ll1+\log\bigl(c\sqrt{\log\log T}\bigr)+\frac{(1+\log X)^2}{\log^2T}\ll1+\log\log\log T,
\]""",
    r"""\[
\begin{split}
\bigl\langle\mathfrak D(\tau_k)^2\bigr\rangle_{\IT}&\ll\frac1T\int_{T-1}^{2T+2}\mathfrak D^2+\frac1{T\log^2T}\int_{T-1}^{2T+2}\mathfrak D'^2\\
&\ll1+\log\bigl(c\sqrt{\log\log T}\bigr)+\frac{(1+\log X)^2}{\log^2T}\ll1+\log\log\log T,
\end{split}
\]""")
rep(r"""\mathbf r&=\nabla E(\mathbf v)+\mathsf D^{\mathsf T}(\boldsymbol\mu_+-\boldsymbol\mu_-),\qquad A=\frac{\mathsf h_T^2}{108\,|\mathsf J_T|},\qquad
B_{\rm reg}=\mathscr L(\mathbf v,\boldsymbol\mu_+,\boldsymbol\mu_-)-\frac3{4^{4/3}}A^{-1/3}\|\mathbf r\|_2^{4/3},
\end{split}""",
    r"""\mathbf r&=\nabla E(\mathbf v)+\mathsf D^{\mathsf T}(\boldsymbol\mu_+-\boldsymbol\mu_-),\qquad A=\frac{\mathsf h_T^2}{108\,|\mathsf J_T|},\\
B_{\rm reg}&=\mathscr L(\mathbf v,\boldsymbol\mu_+,\boldsymbol\mu_-)-\frac3{4^{4/3}}A^{-1/3}\|\mathbf r\|_2^{4/3},
\end{split}""")

# ================================================================ after the independent review of v11
rep(r"""on the same two intervals give $\int_{T-1}^{2T+2}\mathfrak D'^2\ll T(1+\log X)^2$.""",
    r"""on the same two intervals give $\int_{T-1}^{2T+2}\mathfrak D'^2\ll T(1+\log X)^2$ (the proof of \CGeqref{eq:SX_derivative} uses $X\le T^{1/2}$ only through $X\log X\ll T$, so it applies with $T\mp1$ in place of $T$).""")
rep(r"""its terms $m=1$ are $\frac1\pi\sum_{Y<p\le X}p^{-1/2}\sin(t\log p)$""",
    r"""its terms $m=1$ are $-\frac1\pi\sum_{Y<p\le X}p^{-1/2}\sin(t\log p)$""")
rep(r"""Theorem~\CGref{thm:fixed_cutoff_step} improves the factor $c^2\log\log T$ of Lemma~\CGref{lem:transport} to $1+\log\log\log T$, but it does not give""",
    r"""Theorem~\CGref{thm:fixed_cutoff_step} replaces the factor $c^2\log\log T$ of Lemma~\CGref{lem:transport} by $1+\log\log\log T$, the better of the two when $c^2\log\log T\ge\log\log\log T$, in particular for fixed $c$; but it does not give""")
rep(r"""and Theorem~\CGref{thm:fixed_cutoff_step} below improves it to $\ll1+\log\log\log T$ for $c\ge(\log\log T)^{-1/2}$;""",
    r"""and Theorem~\CGref{thm:fixed_cutoff_step} below gives $\ll1+\log\log\log T$ for $c\ge(\log\log T)^{-1/2}$, the better bound for fixed $c$;""")
rep(r"""In particular, for every fixed $0<c\le\frac12$ the one-step clock $\tau_k^{T^c}$ has mean-square error""",
    r"""In particular, for every fixed $0<c\le\frac12$ and $T\ge T_0(c)$ the one-step clock $\tau_k^{T^c}$ has mean-square error""")
rep(r"""then (a)--(c) of Theorem~\CGref{thm:regularized_clock} hold for these points with $(1+\log(1/c))^2$ replaced by $(1+\log(1/c))^2+\eta_{\rm reg}$ in \CGeqref{eq:regularized_main}, \CGeqref{eq:regularized_tails} and (c), and (d) holds unchanged.""",
    r"""then (a)--(d) of Theorem~\CGref{thm:regularized_clock} hold for these points, with $(1+\log(1/c))^2$ replaced by $(1+\log(1/c))^2+\eta_{\rm reg}$ in the fourth-moment bounds and in \CGeqref{eq:regularized_tails}, and $1+\log(1/c)$ by $1+\log(1/c)+\sqrt{\eta_{\rm reg}}$ in the second-moment bound; since $\eta_{\rm reg}\le1$, all of them hold with $C$ replaced by $2C$.""")
rep(r"""$\mathcal K_T$, $\mathcal I_T^\tau$ & piecewise linear functions on the mesh with slopes in $[\frac12\Lambda_T,2\Lambda_T]$; the clock window $\{k:T\le\tau_k<2T\}$\\""",
    r"""$\mathcal K_T$ & piecewise linear functions on the mesh with slopes in $[\frac12\Lambda_T,2\Lambda_T]$ (Section~\CGref{sec:regularized})\\""")
rep(r"""$E$, $E_*$, $\eta_{\rm reg}$, $B_{\rm reg}$ & objective of the convex program, its minimum, tolerance, dual lower bound (Proposition~\CGref{prop:tolerance})\\""",
    r"""$E(\mathbf v)$, $E_*$, $\eta_{\rm reg}$, $B_{\rm reg}$, $\mathsf G$, $A_{\rm reg}$ & objective of the convex program, its minimum, tolerance, dual lower bound, mass matrix, convexity constant: local to Proposition~\CGref{prop:tolerance}\\""")
rep(r"""\mathbf r&=\nabla E(\mathbf v)+\mathsf D^{\mathsf T}(\boldsymbol\mu_+-\boldsymbol\mu_-),\qquad A=\frac{\mathsf h_T^2}{108\,|\mathsf J_T|},\\
B_{\rm reg}&=\mathscr L(\mathbf v,\boldsymbol\mu_+,\boldsymbol\mu_-)-\frac3{4^{4/3}}A^{-1/3}\|\mathbf r\|_2^{4/3},""",
    r"""\mathbf r&=\nabla E(\mathbf v)+\mathsf D^{\mathsf T}(\boldsymbol\mu_+-\boldsymbol\mu_-),\qquad A_{\rm reg}=\frac{\mathsf h_T^2}{108\,|\mathsf J_T|},\\
B_{\rm reg}&=\mathscr L(\mathbf v,\boldsymbol\mu_+,\boldsymbol\mu_-)-\frac3{4^{4/3}}A_{\rm reg}^{-1/3}\|\mathbf r\|_2^{4/3},""")
rep(r"""with the tridiagonal mass matrix $\mathsf M$ of the hat functions, whose diagonal entries are $\frac23\mathsf h_T$ ($\frac13\mathsf h_T$ at the two ends) and whose off-diagonal entries are $\frac16\mathsf h_T$; Gershgorin's theorem gives $\lambda_{\min}(\mathsf M)\ge\frac16\mathsf h_T$. Hence $\frac13\int P_{\mathbf d}^4\ge A\|\mathbf d\|_2^4$. The constraint terms of $\mathscr L$ are linear in $\mathbf v$, so $\mathscr L(\mathbf v+\mathbf d,\boldsymbol\mu_\pm)\ge\mathscr L(\mathbf v,\boldsymbol\mu_\pm)+\mathbf r^{\mathsf T}\mathbf d+A\|\mathbf d\|_2^4\ge\mathscr L(\mathbf v,\boldsymbol\mu_\pm)-\frac3{4^{4/3}}A^{-1/3}\|\mathbf r\|_2^{4/3}=B_{\rm reg}$ for every $\mathbf d$, by minimizing $-\|\mathbf r\|_2s+As^4$ over $s\ge0$.""",
    r"""with the tridiagonal mass matrix $\mathsf G$ of the hat functions, whose diagonal entries are $\frac23\mathsf h_T$ ($\frac13\mathsf h_T$ at the two ends) and whose off-diagonal entries are $\frac16\mathsf h_T$; Gershgorin's theorem gives $\lambda_{\min}(\mathsf G)\ge\frac16\mathsf h_T$. Hence $\frac13\int P_{\mathbf d}^4\ge A_{\rm reg}\|\mathbf d\|_2^4$. The constraint terms of $\mathscr L$ are linear in $\mathbf v$, so $\mathscr L(\mathbf v+\mathbf d,\boldsymbol\mu_\pm)\ge\mathscr L(\mathbf v,\boldsymbol\mu_\pm)+\mathbf r^{\mathsf T}\mathbf d+A_{\rm reg}\|\mathbf d\|_2^4\ge\mathscr L(\mathbf v,\boldsymbol\mu_\pm)-\frac3{4^{4/3}}A_{\rm reg}^{-1/3}\|\mathbf r\|_2^{4/3}=B_{\rm reg}$ for every $\mathbf d$, by minimizing $-\|\mathbf r\|_2s+A_{\rm reg}s^4$ over $s\ge0$.""")
rep(r"""and $\int_{\mathsf J_T}P_{\mathbf d}^2=\mathbf d^{\mathsf T}\mathsf M\mathbf d$""", r"""and $\int_{\mathsf J_T}P_{\mathbf d}^2=\mathbf d^{\mathsf T}\mathsf G\mathbf d$""")
rep(r"""Section~\CGref{sec:conclusions} lists what is open.""", r"""Section~\CGref{sec:conclusions} summarizes the results and their scope.""")
rep(r"""after $\log^*T+O(1)$ steps the error is $O(1)$ mean spacings, using no ordinate; with a fixed cutoff exponent the one-step clock has error $\ll(1+\log\log\log T)/\log^2T$ (Theorem~\CGref{thm:fixed_cutoff_step}).""",
    r"""after $\log^*T+O(1)$ steps the error is $O(1)$ mean spacings, using no ordinate.""")
rep(r"""constants in the $O$-terms of Theorems B--E are absolute but not computed, and the same holds for $T_0$;""",
    r"""constants in the $O$-terms of Theorems B, D, D$'$ and D$''$ are absolute but not computed, and the same holds for $T_0$;""")
rep(r"""Theorems B, D and D$'$ are asymptotic statements in mean square (in fourth mean for D$'$) over the zeros with $T<\gamma_k\le2T$;""",
    r"""Theorems B, D, D$'$ and D$''$ are asymptotic statements in mean square (in fourth mean for D$'$) over the zeros with $T<\gamma_k\le2T$, and for D$'$ also over the window $T\le\tau_k<2T$;""")
rep(r"""with $h_j\wedge1=\min(h_j,1)$ and $(h_j\wedge1)\log(4T)+3\le8j+3$""", r"""with $h_j\le1$ and $h_j\log(4T)+3\le8j+3$""")

rep(r"""The available transport estimate, Lemma~\CGref{lem:transport}, does not establish this boundedness.""",
    r"""The available transport estimates, Lemma~\CGref{lem:transport} and Theorem~\CGref{thm:fixed_cutoff_step}, do not establish this boundedness.""")

TEX.write_text(head + sep + body)
print('v11 patch applied')
