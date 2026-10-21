#!/usr/bin/env python3
"""v12 = v11.2 (identical to v11) with the pending corrections of 2026-10-20/21.

Run on a copy of ../v11/manuscript/prime_corrected_clock_v11.tex saved as
manuscript/prime_corrected_clock_v12.tex.  Every replacement must match exactly once.

Sources of the changes:
  * pendiente_siguiente_version/revision_matematica_v11_2_2026-10-20.md (first review)
  * pendiente_siguiente_version/revision_matematica_v11_2_segunda_2026-10-20.md (second review)
  * pendiente_siguiente_version/comentarios_estilo_autor_2026-10-20.txt (author's style comments)
  * pendiente_siguiente_version/defect_certificate_pending.tex (unconditional part only)
  * the finite-Euler-product identity for the roots of the corrected equation (chat, 2026-10-21)
  * the author's request of 2026-10-21: define the Lambert function.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
TEX = ROOT / 'manuscript' / 'prime_corrected_clock_v12.tex'
src = TEX.read_text()
head, sep, body = src.partition('\\begin{document}')
assert sep


def rep(old, new, where='body'):
    global body, head
    text = body if where == 'body' else head
    n = text.count(old)
    if n != 1:
        sys.exit(f'expected 1 match, found {n}:\n{old[:300]}')
    text = text.replace(old, new)
    if where == 'body':
        body = text
    else:
        head = text


def rep_re(pattern, new):
    global body
    m = list(re.finditer(pattern, body, re.S))
    if len(m) != 1:
        sys.exit(f'regex expected 1 match, found {len(m)}: {pattern[:160]}')
    body = body[:m[0].start()] + new + body[m[0].end():]


# ---------------------------------------------------------------- abstract
rep_re(r'\\begin\{abstract\}\n.*?\n\\end\{abstract\}', r'''\begin{abstract}
Let $\gamma_k$ be the ordinates of the nontrivial zeros of the Riemann zeta function, counted with multiplicity, and let $\tau_k$ be the midpoint Riemann--von Mangoldt clock (RvM clock): the solution of $\NO(\tau_k)=k-\frac12$, where $\NO$ is the main term of the Riemann--von Mangoldt formula, given in closed form by Lambert's function. The clock is close to the ordinates, $\tau_k-\gamma_k$ being bounded; in units of zeros, however, the ordinal displacement $s_k=k-\frac12-\NO(\gamma_k)$ has mean square $\frac1{2\pi^2}\log\log T$ (Selberg), which is unbounded. We prove, unconditionally: (A) an exact identity that turns sums of $\mathcal G(u_k+\frac12)-\mathcal G(u_k-\frac12)$, $u_k=k-\frac12-F(\gamma_k)$, over consecutive ordinates into $dF$-integrals of $g(N-F)$, where $\mathcal G'=g$, for every continuous $g$ and every $C^1$ model $F$ of the counting function $N$; (B) for the clock equation corrected by the Euler phase $S_X$ of the primes $p\le X$, the mean square of the ordinal defect at the ordinates is $\frac1{2\pi^2}\log\frac{\log T}{\log X}+O(1+\sqrt{\log\frac{\log T}{\log X}})$ uniformly for $2\le X\le T^{1/2}$, so that it is bounded if and only if $\log X\asymp\log T$; (C) an exact finite-height accounting of the gain of the one-step clock $\tau_k-S_X(\tau_k)/\lL(\tau_k)$, $\lL(t)=\frac1{2\pi}\log\frac t{2\pi}$; (D) with $X=T^{1/\sqrt{\log\log T}}$ the one-step clock, calculated from $\tau_k$ and the primes alone, has mean-square error $(\log\log\log T+O(\sqrt{\log\log\log T}))/\log^2T$ in the ordinates, against $(2+o(1))\log\log T/\log^2T$ for the clock, and the Newton-type step iterated $\log^*T+O(1)$ times, with cutoffs depending only on $T$ through absolute constants, locates the ordinates with a mean-square error of $O(1)$ mean spacings; sorting the final points gives a nondecreasing sequence with no larger mean-square error; the ordinal defect has exponential tails and the errors of the corrected clocks have all moments bounded in units of $\sqrt{H_m}$; (D$'$) with a fixed cutoff $X=T^c$, the best $L^4$ approximation of $\NO+S_X$ on $[\frac T2,3T]$ by piecewise linear functions with slopes between $\frac{\log T}{4\pi}$ and $\frac{\log T}\pi$ is unique and is obtained without zeros, its level points $\widehat x_k$ are increasing with gaps between $\pi/\log T$ and $4\pi/\log T$, and $\langle|\widehat x_k-\gamma_k|^4\rangle\ll(1+\log\frac1c)^2/\log^4T$ uniformly for $2\le X\le\sqrt{T/2}$, without Newton iteration; (D$''$) for the one-step clock with a fixed cutoff exponent, $\langle(\tau_k^{T^c}-\gamma_k)^2\rangle\ll(1+\log\log\log T)/\log^2T$ uniformly for $(\log\log T)^{-1/2}\le c\le\frac12$; (E) the largest displacement satisfies $\limsup_k|\tau_k-\gamma_k|=2\pi\limsup_t|S(t)|/\log t$, and Backlund's method with the convex hull of the exponent pairs of Bourgain and Heath-Brown and of their images under van der Corput's process gives $\limsup_k|\tau_k-\gamma_k|\le0.6072889$ ($0.6060224$ with the exponent pairs of the preprints of Trudgian--Yang and Tao--Trudgian--Yang), against $2\pi\cdot0.10076=0.6331\ldots$ from the explicit bound of Bellotti and Wong; this bound for the $\limsup$ is asymptotic and is not an effective finite-height estimate; (F) an ordinate of multiplicity one carries a simple zero on the critical line, so for every model $F$ the number of simple zeros on the line in $(T,2T]$ is at least $\#\{T<\gamma_k\le2T\}-\sum_k(2u_k)^{2j}$, and with (A) their proportion is at least $\frac43-4Q_2-o(1)$, where $Q_2$ is the $dF_X$-mean square of $N-F_X$, $F_X=\NO+S_X$; (G) for a fixed cutoff, the zeta function whose zeros are $\frac12\pm i\kappa_k$, $\kappa_k$ the roots of the corrected equation in its monotone range, is the zeta function of the clock times the finite Euler product $\prod_{p\le X}(1-p^{-s})^{-1}$, up to a factor holomorphic and without zeros in $\Re s>\frac12$. No corrected point evaluates the Riemann zeta function or any of its zeros, and the constant of (E) is obtained without evaluating the zeta function. Our approach is similar to that of LeClair, who solves numerically the clock equation corrected by the first $N$ primes and compares the solutions with known zeros, and the zeros of Gonek's functions $\zeta_X$, built from finite Euler products, solve a version of the same equation with smoothed weights; here the corrected points are explicit or defined by a convex program, and their errors are proved.
\end{abstract}''')

# ---------------------------------------------------------------- 1.1 clock, Lambert, defect, index rule
rep_re(r'Let \$\\zeta\(s\)\$ be the Riemann zeta function, let \$N\(T\)\$ be the number.*?its correct index\.\n', r'''Let $\zeta(s)$ be the Riemann zeta function, let $N(T)$ be the number of its nontrivial zeros $\rho=\beta+i\gamma$ with $0<\gamma\le T$, counted with multiplicity, and list their ordinates as $\gamma_1\le\gamma_2\le\cdots$, with multiplicity. No assumption is made on the real parts: $\gamma_k$ is the ordinate of a zero whether or not it lies on the critical line. Throughout, $t$ is a real variable, $T$ is the height of a window $(T,2T]$, and $k$, $l$ are indices of ordinates. For $T$ not an ordinate the Riemann--von Mangoldt formula reads \cite[\S\S9.3--9.4]{Titchmarsh1986}
\begin{equation}
 N(T)=\NO(T)+\frac1\pi\arg\zeta\Bigl(\frac12+iT\Bigr)+O\Bigl(\frac1T\Bigr),\qquad \NO(T)=\frac{T}{2\pi}\log\frac{T}{2\pi e}+\frac78,
 \label{eq:intro_rvm}
\end{equation}
where $\arg\zeta(\frac12+iT)$ has its classical determination \cite[\S9.3]{Titchmarsh1986}: the value obtained by continuous variation along $2\to2+iT\to\frac12+iT$, starting from $\arg\zeta(2)=0$. With this determination $S(T)=\frac1\pi\arg\zeta(\frac12+iT)$ is the remainder of the counting function, and every result quoted below on $S$ (its moments, its normal law, Selberg's approximation, the bound of Bellotti and Wong) refers to it. The \emph{midpoint Riemann--von Mangoldt clock} (RvM clock) is the sequence of solutions $\tau_k>2\pi$ of the main-term equation,
\begin{equation}
 \NO(\tau_k)=k-\frac12,\qquad \tau_k=\frac{2\pi\,(k-\frac{11}8)}{W_0\bigl((k-\frac{11}8)/e\bigr)}\qquad(k\ge1).
 \label{eq:intro_clock}
\end{equation}
Here $W$ is the Lambert function \cite{Corless1996}, the inverse of $w\mapsto we^w$: for real $y\ge-1/e$ the equation $we^w=y$ has a real solution, unique if $y\ge0$ and two if $-1/e<y<0$. The principal branch $W_0$ is the solution with $W_0(y)\ge-1$; it is increasing on $[-1/e,\infty)$, $W_0(0)=0$, and $W_0(y)=\log y-\log\log y+o(1)$ as $y\to\infty$; the other real branch, $W_{-1}\le-1$, is defined only on $[-1/e,0)$. Substituting $w=W_0((k-11/8)/e)$ in $we^w=(k-11/8)/e$ proves the inversion. For $k=1$ the argument is negative and $W_{-1}$ gives a value below $2\pi$, excluded by the defining condition $\tau_k>2\pi$. The clock is explicit: if $g_n$ is the $n$-th Gram point, $\vartheta(g_n)=n\pi$ with $\vartheta$ the Riemann--Siegel theta function (Section~\CGref{subsec:counting}), then $\vartheta(\tau_k)=\pi(k-\frac32)+O(1/\tau_k)$, so $\tau_k$ lies between the consecutive Gram points $g_{k-2}$ and $g_{k-1}$ for $k$ large. The explicit, fully determined Lambert values are an essential part of this paper: its aim is to improve and characterize the ordinates $\gamma_k$ starting precisely from them. The prime information added to the clock is the Euler phase of the primes $p\le X$,
\begin{equation}
 S_X(t)=-\frac1\pi\sum_{p\le X}\arg\bigl(1-p^{-1/2-it}\bigr),\qquad F_X(t)=\NO(t)+S_X(t),
 \label{eq:intro_SX}
\end{equation}
which turns the clock equation into the \emph{corrected clock equation} $F_X(t)=k-\frac12$. The relation between the clock and the ordinates is measured in units of zeros by the ordinal displacement and by its version for the corrected equation, the \emph{ordinal defect},
\begin{equation}
 s_k=k-\frac12-\NO(\gamma_k),\qquad u_k(X)=s_k-S_X(\gamma_k)=k-\frac12-F_X(\gamma_k).
 \label{eq:intro_defect}
\end{equation}
$u_k(X)$ is the residual of the corrected clock equation at the true ordinate. If $|u_k(X)|<\frac12$, then $k-1<F_X(\gamma_k)<k$: the half-integer level of $F_X$ nearest to $F_X(\gamma_k)$ is $k-\frac12$, and the assignment $\hat k=\lfloor F_X(\gamma_k)\rfloor+1$ gives $\gamma_k$ its index $k$. This is not the assignment by rounding, $\lfloor F_X(\gamma_k)+\frac12\rfloor$, which equals $k$ exactly when $-1<u_k(X)\le0$ (Proposition~\CGref{prop:rounding} concerns that rule). For a multiple ordinate, $k$ is one of the indices $N(\gamma_k^-)+1,\dots,N(\gamma_k^+)$, and in general not $N(\gamma_k)$.
''')

rep('Every corrected point is computed from $k$, $\\NO$ and the primes: the construction evaluates neither',
    'Every corrected point is calculated from $k$, $\\NO$ and the primes: the construction evaluates neither')
rep('Theorem E concerns the worst zero.',
    'Theorem E concerns the largest displacement $\\limsup_k|\\tau_k-\\gamma_k|$. Theorem F is a consequence of Theorem A for the simple zeros on the critical line, and Theorem G identifies the zeta function of the roots of the corrected equation for a fixed cutoff.')

rep('\\subsection{What is known and only used}\n\\label{subsec:known_intro}\nThe following facts are quoted with references in Section~\\CGref{sec:known_results} and are not reproved.\n',
    '\\subsection{Background}\n\\label{subsec:known_intro}\nThe exact statements are in Section~\\CGref{sec:known_results}.\n')

rep('its first approximation, without the argument, is the clock equation $\\NO(t)=n-\\frac12$, which they solve with Lambert\'s function \\cite[(62)--(63), p.~24]{FrancaLeClair2015}, as in \\CGeqref{eq:intro_clock}; this inversion of the Riemann--von Mangoldt main term is elementary \\cite{Corless1996}.',
    'its first approximation, without the argument, is the clock equation $\\NO(t)=n-\\frac12$, for which they use Lambert\'s function \\cite[(62)--(63), p.~24]{FrancaLeClair2015}, as in \\CGeqref{eq:intro_clock}.')

rep_re(r'No error bound for the solutions of either equation is proved in \\cite\{FrancaLeClair2015,LeClair2021\}\. For \$p_N\\le T\^\{1/2\}\$, Theorem B below.*?lie inside it\.',
       r'''No error bound for the solutions of either equation is proved in \cite{FrancaLeClair2015,LeClair2021}. Our approach is similar: we also start from the RvM clock and correct it with the Euler phase of the primes. The differences are the following. (i) The points of Theorem D are explicit expressions in $k$, $\tau_k$ and the primes, and those of Theorem D$'$ are defined by a convex program in $\NO$ and $S_X$; the points of \cite{LeClair2021} are numerical roots. (ii) Their errors are proved: one Newton-type step gives mean-square error $(\log\log\log T+O(\sqrt{\log\log\log T}))/\log^2T$ in the ordinates (Theorem D), $\log^*T+O(1)$ steps give $O(1)$ mean spacings, and so does the regularization of Theorem D$'$ with a fixed cutoff exponent, in fourth mean. (iii) Theorem B measures the corrected equation at the true ordinates and shows how many primes are needed: with a fixed set of primes the mean-square defect grows like $\frac1{2\pi^2}\log\log T$, and it is bounded if and only if $\log p_N\asymp\log T$. (iv) Theorem E gives the exact $\limsup$ of the displacement in terms of $S$, and a bound for it; Theorems F and G relate the defect to the simple zeros on the line and the roots of the corrected equation to the finite Euler product. The range covered here is $p_N\le T^{1/2}$ for Theorems B and D and $p_N\le\sqrt{T/2}$ for Theorem D$'$ (Table~\CGref{tab:evaluates}); the larger numbers of primes allowed in \cite[p.~19]{LeClair2021}, up to $[t^2]$, are not covered.''')

rep('& This is the baseline used here, not a contribution. The Lambert expression is not claimed as new; neither is the tendency of its mean-square height error to zero.\\\\',
    '& The explicit, fully determined Lambert values are the starting point of every construction of this paper, which improves and characterizes the ordinates from them.\\\\')

# ---------------------------------------------------------------- "in height", "worst"
rep('turns the clock from an approximation in height into an approximation in position.',
    'turns the clock from an approximation of the ordinates into an approximation of the indices.')
rep('for the worst zero, Proposition~\\CGref{prop:envelope_equivalence} shows',
    'for the largest displacement, Proposition~\\CGref{prop:envelope_equivalence} shows')
rep('& the worst error of the clock is the extreme size of $S(t)$ &',
    '& the largest displacement of the clock is the extreme size of $S(t)$ &')
rep('the one-step clock $\\tau_k^{T^c}$ has mean-square error $\\ll(1+\\log\\log\\log T)/\\log^2T$ in height,',
    'the one-step clock $\\tau_k^{T^c}$ has mean-square error $\\ll(1+\\log\\log\\log T)/\\log^2T$ in the ordinates,')
rep('its root gains nothing in order: the error in height of $t_k^X$ has mean square',
    'its root gains nothing in order: the error of $t_k^X$ in the ordinates has mean square')
rep('Since $\\Theta_0(\\tau_k)=\\pi(k-\\frac32)$ and $\\varpi=O(1/t)$, $\\tau_k$ lies in phase half way between $g_{k-2}$ and $g_{k-1}$, up to $O(\\tau_k^{-1}(\\log\\tau_k)^{-1})$.',
    'Since $\\Theta_0(\\tau_k)=\\pi(k-\\frac32)$ and $\\varpi=O(1/t)$, $\\vartheta(\\tau_k)=\\pi(k-\\frac32)+O(1/\\tau_k)$, so $g_{k-2}<\\tau_k<g_{k-1}$ for $k$ large; in the phase $\\Theta_0$ the point $\\tau_k$ is the midpoint of the two neighbouring levels $\\pi(k-2)$ and $\\pi(k-1)$.')

# ---------------------------------------------------------------- degree of proof: constants of Theorem D
rep('In Theorem~\\CGref{thm:uniform_iteration} the cutoffs and the number of steps depend on two such constants, $C_\\star$ and $H^*$; the corrected points are explicit expressions in $k$, $\\tau_k$ and the primes once these constants are fixed.',
    'In Theorem~\\CGref{thm:uniform_iteration} the cutoffs and the number of steps depend on two such constants, $C_\\star$ and $H^*$, whose existence is proved and whose numerical values are not; the corrected points are explicit expressions in $k$, $\\tau_k$ and the primes once these constants are fixed. Thus a fixed number of Newton-type steps with specified cutoffs (Theorems~\\CGref{thm:computable_clock} and \\CGref{thm:second_step}) is a fully specified construction, while the uniform statement up to $\\log^*T+O(1)$ steps asserts the existence of admissible constants $C_\\star$, $H^*$.')

# ---------------------------------------------------------------- reviews: Mertens by partial summation (1.2/1.6)
rep('By Theorem~\\CGref{thm:known_mertens}, $V_\\pm=\\log\\frac{\\log X_+}{\\log X_-}+O(\\frac1{\\log X_-})\\ll\\frac1{\\log X_-}\\ll\\frac1{1+c\\log T}$ (and $V_\\pm=0$ if $X_-=X_+=2$).',
    'By partial summation from the first estimate of Theorem~\\CGref{thm:known_mertens}, written $\\sum_{p\\le y}\\frac{\\log p}p=\\log y+R(y)$ with $|R|\\le C_{\\rm M}$, one has $V_\\pm=\\int_{X_-}^{X_+}\\frac{d(\\log y+R(y))}{\\log y}=\\log\\frac{\\log X_+}{\\log X_-}+\\Bigl[\\frac{R(y)}{\\log y}\\Bigr]_{X_-}^{X_+}+\\int_{X_-}^{X_+}\\frac{R(y)\\,dy}{y\\log^2y}=\\log\\frac{\\log X_+}{\\log X_-}+O\\Bigl(\\frac1{\\log X_-}\\Bigr)$, hence $V_\\pm\\ll\\frac1{\\log X_-}\\ll\\frac1{1+c\\log T}$ (and $V_\\pm=0$ if $X_-=X_+=2$).')

# ---------------------------------------------------------------- reviews: endpoints by Stieltjes (1.3/1.7)
rep('\\emph{At the ordinates.} Let $T,2T$ be non-ordinates (otherwise move them by less than the distance to the nearest ordinate, which changes neither side). As Lebesgue--Stieltjes measures on $(T,2T]$, $dN=\\lL\\,dt+dG$, and $\\mathcal Q^2$ is Lipschitz, so integration by parts \\cite[\\S3.5]{Folland1999} gives',
    '\\emph{At the ordinates.} With the right-continuous $N$, the atoms of $dN$ in $(T,2T]$ are exactly the ordinates of $\\IT$, with their multiplicities, whether or not $T$ and $2T$ are ordinates. As Lebesgue--Stieltjes measures on $(T,2T]$, $dN=\\lL\\,dt+dG$, with $G=N-\\NO$ right-continuous and of bounded variation on $[T,2T]$; since $\\mathcal Q^2$ is continuous (indeed Lipschitz), it has no jump in common with $G$, and integration by parts on $(T,2T]$ \\cite[\\S3.5]{Folland1999} gives, with no restriction on the endpoints,')

# ---------------------------------------------------------------- reviews: alpha = 1/2 (1.4)
rep('the first inequality of \\CGeqref{eq:deformation} follows, and the second is Markov\'s inequality; the last statement is $\\alpha=1$.',
    'the first inequality of \\CGeqref{eq:deformation} follows, and the second is Markov\'s inequality; the last statement is the case $\\alpha=\\frac12$, since $d_{2,k}\\le0$ gives $|d_{2,k}/d_{0,k}-1|\\ge1>\\frac12$ (with $\\alpha=1$ the strict inequality would miss $d_{2,k}=0$).')

# ---------------------------------------------------------------- second review 1.1: domain of the cutoff in the sampling lemma
rep('and for every $r\\ge1$ and $2\\le X\\le T^{1/(2r)}$,\n\\[\n\\int_{T-3}^{2T+3}|S_X^{(\\nu)}(t)|^{4r}dt\\le(Cr)^{2r}\\,T(1+\\log X)^{4r\\nu}\\qquad(\\nu=1,2).\n\\]',
    'and for every $r\\ge1$, $2\\le X\\le T^{1/(2r)}$ and every interval $\\mathcal J\\subset[\\frac T2,3T]$ of length at most $2T$ (in particular $[T-3,2T+3]$ and $\\mathcal J_T^\\sharp=[T-3T^{1/2},2T+3T^{1/2}]$),\n\\[\n\\int_{\\mathcal J}|S_X^{(\\nu)}(t)|^{4r}dt\\le(Cr)^{2r}\\,T(1+\\log X)^{4r\\nu}\\qquad(\\nu=1,2).\n\\]')
rep('The third: Lemma~\\CGref{lem:SX_fourth} with products of $2r$ primes, $n\\le X^{2r}\\le T$',
    'The third: the proof of Lemma~\\CGref{lem:SX_fourth} on $\\mathcal J$ in place of $[T-3,2T+3]$ (Theorem~\\CGref{thm:known_MV} on an interval of length $H\\le2T$ gives $\\sum|\\eta_n|^2(H+O(n))\\le(2T+O(T))\\sum|\\eta_n|^2$ for $n\\le T$), with products of $2r$ primes, $n\\le X^{2r}\\le T$')
rep('Let $r\\ge1$ be an integer, $2\\le X\\le T^{1/(4r)}$, $\\varphi$ a cutoff equal to $1$ on $[T-2T^{1/2},2T+2T^{1/2}]$ as in Lemma~\\CGref{lem:transport}, and $g=\\mathcal M(\\varphi S\'_X)$.',
    'Let $r\\ge1$ be an integer, $2\\le X\\le T^{1/(4r)}$, $\\varphi^\\sharp\\in C^\\infty(\\R)$ with $0\\le\\varphi^\\sharp\\le1$, $\\varphi^\\sharp=1$ on $[T-2T^{1/2},2T+2T^{1/2}]$, $\\varphi^\\sharp=0$ outside $\\mathcal J_T^\\sharp=[T-3T^{1/2},2T+3T^{1/2}]$ and $|\\varphi^{\\sharp\\prime}|\\le2$ (a cutoff different from the one of Lemma~\\CGref{lem:transport}, which equals $1$ only on $[T-2,2T+2]$), and $g=\\mathcal M(\\varphi^\\sharp S\'_X)$.')
rep('Here $\\|\\mathsf F\\|_2=\\|g\\|_{8r}^{4r}\\le(\\mathcal A_{8r}\\|\\varphi S\'_X\\|_{8r})^{4r}',
    'Here $\\|\\varphi^\\sharp S\'_X\\|_{8r}\\le\\|S\'_X\\|_{L^{8r}(\\mathcal J_T^\\sharp)}$ and $\\|(\\varphi^\\sharp S\'_X)\'\\|_{8r}\\le2\\|S\'_X\\|_{L^{8r}(\\mathcal J_T^\\sharp)}+\\|S\'\'_X\\|_{L^{8r}(\\mathcal J_T^\\sharp)}$, both bounded by the third estimate of Lemma~\\CGref{lem:higher_moments} on $\\mathcal J=\\mathcal J_T^\\sharp$; so $\\|\\mathsf F\\|_2=\\|g\\|_{8r}^{4r}\\le(\\mathcal A_{8r}\\|\\varphi^\\sharp S\'_X\\|_{8r})^{4r}')
rep('with $\\mathsf g_2=\\mathcal M(\\varphi S\'_{X_2})$', 'with $\\mathsf g_2=\\mathcal M(\\varphi^\\sharp S\'_{X_2})$')
rep('Let $\\mathsf g_j=\\mathcal M(\\varphi S\'_{X_j})$ with $\\varphi=1$ on $[T-2T^{1/2},2T+2T^{1/2}]$',
    'Let $\\mathsf g_j=\\mathcal M(\\varphi^\\sharp S\'_{X_j})$ with the cutoff $\\varphi^\\sharp$ of Lemma~\\CGref{lem:sampling_rho}')
rep('where the cutoff $\\varphi$ of Lemma~\\CGref{lem:sampling_rho} equals $1$', 'where the cutoff $\\varphi^\\sharp$ of Lemma~\\CGref{lem:sampling_rho} equals $1$')
rep('for $g=\\mathcal M(\\varphi S\'_X)$; the proof of that lemma uses', 'for $g=\\mathcal M(\\varphi^\\sharp S\'_X)$; the proof of that lemma uses')

# ---------------------------------------------------------------- second review 1.2: intervals near the ends in the pair counts
rep('the ordinates counted by $n_{\\mathsf R}(\\gamma_k)$ lie in an interval of length $h$ contained in $[T-1,2T]$,',
    'the ordinates counted by $n_{\\mathsf R}(\\gamma_k)$ lie in $(T,2T]\\cap[\\gamma_k-\\mathsf Rb,\\gamma_k+\\mathsf Rb]\\subset[u_k,u_k+h]$ with $u_k=\\max(T-1,\\gamma_k-\\mathsf Rb)\\in[T-1,2T]$, because $h\\ge2\\mathsf Rb$,')
rep('a set of measure $\\mathsf R b$ contained in $[T-1,2T]$;',
    'a set of measure $\\mathsf R b$ contained in $[T-1,2T]$, because $\\min(\\gamma_k,\\gamma_l)\\in(T,2T]$ and $\\mathsf Rb\\le\\frac14$;')
rep('lies in $[u,u+4\\mathsf R b]$ for $u$ in a set of measure $2\\mathsf R b$;',
    'lies in $[u,u+4\\mathsf R b]$ for $u\\in[\\gamma_k-3\\mathsf Rb,\\gamma_k-\\mathsf Rb]$, a set of measure $2\\mathsf R b$ contained in $[T-1,2T]$ since $\\gamma_k\\in(T,2T]$ and $4\\mathsf Rb\\le1$;')

# ---------------------------------------------------------------- second review 1.3: uniformity in Fujii
rep('By the remark on p.~226, the implied constants in that paper do not depend on $q$, $k$ and $h$.',
    'By the remark on p.~226, read on the page image of the original, the implied constants in that paper do not depend on $q$, $k$ and $h$; this uniformity in $k$ is the external input on which the moments of growing order of Lemma~\\CGref{lem:selberg_uniform}, and through them Theorem~\\CGref{thm:uniform_iteration}, depend.')

# ---------------------------------------------------------------- second review 1.4: base case and order of the constants
rep('\\emph{Base.} By Lemma~\\CGref{lem:higher_moments} with $X=2$,',
    '\\emph{Base.} For every $r\\ge1$ with $2r\\le\\kappa_{\\rm F}\\log T$, by Lemma~\\CGref{lem:higher_moments} with $X=2$,')
rep('So \\CGeqref{eq:induction_claim} holds for every $m\\le m^*$, which is the statement $\\|\\lL e_j\\|_{4,\\IT}\\le4B_\\star\\sqrt{H_j}$ for $j<m^*$.',
    'So \\CGeqref{eq:induction_claim} holds for every $m\\le m^*$, which is the statement $\\|\\lL e_j\\|_{4,\\IT}\\le4B_\\star\\sqrt{H_j}$ for $j<m^*$.\n\n\\emph{Order of the constants.} The constants are fixed in this order, and none of them depends on $m$, $j$, $r$ or $T$: first $C$, $C_0$, $C_3$, $C_5$, given by Lemmas~\\CGref{lem:higher_moments}, \\CGref{lem:sampling_rho}, Theorem~\\CGref{thm:multiplicity_all} and \\CGeqref{eq:uniform_recursion}; then $C_\\star$; then $B_\\star$ and $C_6$; then $H^*$. With $C_\\star$ and $H^*$ fixed, $m^*(T)=\\log^*T+O(1)$ with an $O(1)$ depending only on them. Finally $T_0$ is taken so large that for $T\\ge T_0$: the $o(1)$ terms of the one-step bound are at most $1$; $2^{m^*(T)+1}\\le\\kappa_{\\rm F}\\log T$; and $c_j\\ge C_\\star(\\log\\log T)^{-9/16}$ gives $X_j\\ge2$. The second condition contains the base case, where the orders reach $r\\le2^m\\le2^{m^*}$. With these choices all the conditions used above hold simultaneously for every $m\\le m^*(T)$ and every $T\\ge T_0$.')

# ---------------------------------------------------------------- conclusions
rep('so $\\langle\\delta_k^2\\rangle\\sim2\\log\\log T/\\log^2T$: the clock is close to the zeros in height but misplaces almost every zero by an unbounded number of positions.',
    'so $\\langle\\delta_k^2\\rangle\\sim2\\log\\log T/\\log^2T$: the clock is close to the ordinates, while in units of zeros its displacement has unbounded mean square.')
rep('the one-step clock has mean-square error $(\\log\\log\\log T+O(\\sqrt{\\log\\log\\log T}))/\\log^2T$ in height, against $(2+o(1))\\log\\log T/\\log^2T$ for the bare clock;',
    'the one-step clock has mean-square error $(\\log\\log\\log T+O(\\sqrt{\\log\\log\\log T}))/\\log^2T$ in the ordinates, against $(2+o(1))\\log\\log T/\\log^2T$ for the bare clock;')
rep_re(r'\\item \\emph\{The corrected clock equation solved numerically\}.*?estimated from known zeros\.\n',
       r'''\item \emph{Simple zeros on the critical line from the defect} (Theorem~\CGref{thm:simple_certificate}, Corollary~\CGref{cor:simple_Q}). An ordinate of multiplicity one carries a simple zero on the line; for any model $F$ the simple zeros on the line in $(T,2T]$ number at least $\#\IT-\sum_{k\in\IT}(2u_k)^{2j}$, and with Theorem A their proportion is at least $\frac43-4Q_2-o(1)$; a positive proportion would follow from any proved bound $\limsup Q_2(T,T^c)<\frac13$ at one fixed $c$.
\item \emph{The finite Euler product in the zeta function of the corrected roots} (Theorem~\CGref{thm:euler_product}). For a fixed cutoff, the zeta function of the roots of the corrected equation in its monotone range is $\zeta_\tau(s)\,P_X(s)/P_X(1)$ times a factor holomorphic and zero-free in $\Re s>\frac12$, where $\zeta_\tau$ is the zeta function of the clock and $P_X(s)=\prod_{p\le X}(1-p^{-s})^{-1}$: the construction reproduces exactly the finite Euler product of the primes it uses.
\item \emph{Comparison with the corrected clock equation solved numerically} (Theorems~\CGref{thm:main}, \CGref{thm:computable_clock} and \CGref{thm:regularized_clock}, Table~\CGref{tab:evaluates}). The clock equation corrected by the first $N$ primes was solved numerically in \cite{LeClair2021}, with an accuracy estimated from known zeros, and with smoothed weights it is the equation of the zeros of Gonek's $\zeta_X$ \cite{Gonek2012}. Here, for $p_N\le T^{1/2}$, its mean-square defect at the true ordinates is $\frac1{2\pi^2}\log\frac{\log T}{\log p_N}+O(1+\sqrt{\log(\log T/\log p_N)})$, unbounded for a fixed number of primes; explicit Newton-type steps give points with proved error, and so does, for $X\le\sqrt{T/2}$, a convex regularization with a fixed cutoff exponent.
''')

# ---------------------------------------------------------------- intro list: items F and G, status table, organization
rep('\\paragraph{Main finding} The Euler phase',
    r'''\item \textbf{Simple zeros on the critical line} (Lemma~\CGref{lem:mult_ordinate}, Theorem~\CGref{thm:simple_certificate}, Corollary~\CGref{cor:simple_Q}). An ordinate of multiplicity $m\ge2$ forces $u_{k+i}=u_k+i$ along its indices, for any model $F$, and an ordinate of multiplicity one carries a simple zero on the critical line. Hence, for every $j\ge1$ and every real function $F$, the number $N_0^s(T,2T)$ of simple zeros on the line with $T<\gamma\le2T$ satisfies $N_0^s(T,2T)\ge\#\IT-\sum_{k\in\IT}(2u_k)^{2j}$, and with Theorem A, for $F=F_X$ and $2\le X\le T^{1/2}$,
\begin{equation}
\frac{N_0^s(T,2T)}{\#\IT}\ge\frac43-4Q_2(T,X)-o(1),\qquad Q_2(T,X)=\frac1{\#\IT}\int_T^{2T}\bigl(N-F_X\bigr)^2dF_X .
\label{eq:intro_F}
\end{equation}
A positive proportion would follow from any proved bound $\limsup_TQ_2(T,T^c)<\frac13$ at one fixed $c$; Theorem B gives the size of $Q_2$ with an absolute constant that is not computed, so no numerical proportion is claimed.
\item \textbf{The finite Euler product} (Theorem~\CGref{thm:euler_product}). Let $X\ge2$ be fixed, let $\kappa_k$ be the roots of $F_X(t)=k-\frac12$ in the range where $F_X$ is increasing (for the finitely many smaller indices $\kappa_k$ is fixed arbitrarily), and let $\zeta_\kappa$ and $\zeta_\tau$ be the functions of order one with the functional equation whose nontrivial zeros are $\frac12\pm i\kappa_k$ and $\frac12\pm i\tau_k$. Then
\begin{equation}
\zeta_\kappa(s)=\zeta_\tau(s)\,\frac{P_X(s)}{P_X(1)}\,e^{H_X(s)},\qquad P_X(s)=\prod_{p\le X}\bigl(1-p^{-s}\bigr)^{-1},
\label{eq:intro_G}
\end{equation}
with $H_X$ holomorphic in $\Re s>\frac12$ and given explicitly by $X$, $\NO$ and the primes. The main term of $\log\zeta_\kappa$ is exactly the finite Euler product of the primes used by the construction.
\end{enumerate}

\paragraph{Main finding} The Euler phase''')
# the old enumerate closed before Main finding; remove that \end{enumerate}
rep('although on the Lindel\\"of hypothesis $S(t)=o(\\log t)$.\n\\end{enumerate}\n\n\\item \\textbf{Simple zeros',
    'although on the Lindel\\"of hypothesis $S(t)=o(\\log t)$.\n\\item \\textbf{Simple zeros')

rep('Proposition~\\CGref{prop:envelope_equivalence}, Theorem~\\CGref{thm:envelope} (E) & unconditional, asymptotic & the largest displacement of the clock is the extreme size of $S(t)$ & no (exponent pairs)\\\\',
    'Proposition~\\CGref{prop:envelope_equivalence}, Theorem~\\CGref{thm:envelope} (E) & unconditional, asymptotic & the largest displacement of the clock is the extreme size of $S(t)$ & no (exponent pairs)\\\\\nLemma~\\CGref{lem:mult_ordinate}, Theorem~\\CGref{thm:simple_certificate}, Corollary~\\CGref{cor:simple_Q} (F) & unconditional & simple zeros on the line bounded below by the defect & no\\\\\nTheorem~\\CGref{thm:euler_product} (G) & unconditional, exact & the zeta function of the corrected roots contains the finite Euler product exactly & no ($\\NO$, primes $p\\le X$)\\\\')

rep('and Section~\\CGref{sec:envelope} proves Theorem E; Theorem D$\'\'$ is proved in Section~\\CGref{sec:computable}.',
    'Section~\\CGref{sec:envelope} proves Theorem E, Section~\\CGref{sec:simple_zeros} Theorem F and Section~\\CGref{sec:euler_product} Theorem G; Theorem D$\'\'$ is proved in Section~\\CGref{sec:computable}.')

# ---------------------------------------------------------------- new sections F and G, before the conclusions
rep('\\section{Conclusions}\n\\label{sec:conclusions}', r'''\section{Theorem F: simple zeros on the critical line from the defect}
\label{sec:simple_zeros}
In this section $F$ is any real function, $u_k=k-\frac12-F(\gamma_k)$, and $N_0^s(T,2T)$ is the number of zeros $\rho$ with $T<\gamma\le2T$, $\beta=\frac12$ and multiplicity $1$. For $X\ge2$ and $j\ge1$ put
\begin{equation}
Q_{2j}(T,X)=\frac1{\#\IT}\int_T^{2T}\bigl(N(t)-F_X(t)\bigr)^{2j}F_X'(t)\,dt .
\label{eq:Q_def}
\end{equation}

\begin{lemma}[Multiplicity of an ordinate]\label{lem:mult_ordinate}
\begin{enumerate}[label=\textup{(\alph*)}]
\item If an ordinate $\gamma$ occurs with multiplicity $m\ge2$ in the list $(\gamma_k)$, at the indices $k,\dots,k+m-1$, then $u_{k+i}=u_k+i$ for $0\le i<m$, and for every $j\ge1$
\[
\sum_{i=0}^{m-1}\bigl(2u_{k+i}\bigr)^{2j}\ge m .
\]
\item If $\gamma$ occurs with multiplicity $1$, the zero with ordinate $\gamma$ is simple and lies on the critical line.
\end{enumerate}
\end{lemma}

\begin{proof}
(a) $F(\gamma_{k+i})=F(\gamma)$ for all $i$, so $u_{k+i}=u_k+i$. Put $\phi(x)=(2x)^{2j}$: it is even, convex, increasing on $[0,\infty)$ and $\phi(\pm\frac12)=1$. For two reals $a,b$ with $|a|+|b|\ge1$, convexity and evenness give $\phi(a)+\phi(b)\ge2\phi(\frac{|a|+|b|}2)\ge2$; this applies to consecutive $u_{k+i},u_{k+i+1}$, since $|x|+|x+1|\ge1$. If $m$ is even, pair the $m$ values consecutively. If $m\ge3$ is odd, at most one of the $m$ values lies in $(-\frac12,\frac12)$, and the two extreme values $u_k$ and $u_k+m-1$ differ by $m-1\ge2$, so one of them, say $v$, has $|v|\ge\frac12$; pair the other $m-1$ values consecutively and add $\phi(v)\ge1$. In both cases the sum is at least $m$.
(b) If $\rho=\beta+i\gamma$ with $\beta\ne\frac12$, then $1-\bar\rho=1-\beta+i\gamma$ is a zero with the same ordinate, by the functional equation and the reflection principle; a multiple zero repeats its ordinate. In both cases $\gamma$ has multiplicity at least $2$.
\end{proof}

\begin{theorem}[Theorem F]\label{thm:simple_certificate}
For every real function $F$, every $j\ge1$ and every $T>0$,
\begin{equation}
N_0^s(T,2T)\ge\#\IT-\sum_{k\in\IT}\bigl(2u_k\bigr)^{2j}.
\label{eq:simple_certificate}
\end{equation}
\end{theorem}

\begin{proof}
The set $\IT=(N(T),N(2T)]$ contains, for every ordinate $\gamma\in(T,2T]$, all its indices. By Lemma~\CGref{lem:mult_ordinate}(b), every index of $\IT$ whose ordinate has multiplicity one is a simple zero on the critical line, so $N_0^s(T,2T)\ge\#\IT-\mathsf m_T$, where $\mathsf m_T$ is the number of indices of $\IT$ whose ordinate has multiplicity at least $2$. By part (a) the indices of each such ordinate contribute at least their number to $\sum_{k\in\IT}(2u_k)^{2j}$, and the other terms are nonnegative, so $\mathsf m_T\le\sum_{k\in\IT}(2u_k)^{2j}$.
\end{proof}

\begin{corollary}\label{cor:simple_Q}
Let $j\ge1$ and $0<\theta<\frac2{2j+1}$ be fixed. For $F=F_X$ with $2\le X\le T^\theta$, as $T\to\infty$,
\begin{equation}
\frac{N_0^s(T,2T)}{\#\IT}\ge1-4^j\bigl\langle u_k(X)^{2j}\bigr\rangle_{\IT},\qquad\bigl\langle u_k(X)^2\bigr\rangle_{\IT}=Q_2(T,X)-\frac1{12}+o(1),
\label{eq:simple_Q}
\end{equation}
so that $N_0^s(T,2T)/\#\IT\ge\frac43-4Q_2(T,X)-o(1)$ for $X\le T^{1/2}$, and $N_0^s(T,2T)/\#\IT\ge1-16Q_4(T,X)+8Q_2(T,X)-\frac7{15}-o(1)$ for $X\le T^{1/3}$.
\end{corollary}

\begin{proof}
The first inequality is \CGeqref{eq:simple_certificate} divided by $\#\IT$. Apply Theorem~\CGref{thm:identity_general} with $F=F_X$, $k_1=N(T)$ and $k_2=N(2T)+1$, so that the inner indices are exactly $\IT$. The interval $[\gamma_{k_1},\gamma_{k_2}]$ differs from $[T,2T]$ by the pieces $[\gamma_{k_1},T]$ and $[2T,\gamma_{k_2}]$, on which $N$ is constant; on such a piece the integrand is $(n-F_X)^{2j}F_X'$ with $n$ fixed, whose integral is $\frac1{2j+1}$ times a difference of two values of $(n-F_X)^{2j+1}$. As $|N-F_X|\le|S|+|\varpi|/\pi+\sigma_X\ll\log T+\sqrt X$ near $T$ and $2T$, and the same bound holds for the $u_k$ at $k_1,k_2$, the end pieces and the boundary terms of \CGeqref{eq:identity_general} are $O((\log T+\sqrt X)^{2j+1})=O(T^{1-\eta})$ for some $\eta=\eta(j,\theta)>0$, which is $o(\#\IT)$. Hence $\sum_{k\in\IT}\Psi_j(u_k)=\#\IT\,Q_{2j}(T,X)+o(\#\IT)$. With $\Psi_1(u)=u^2+\frac1{12}$ and $\Psi_2(u)=u^4+\frac12u^2+\frac1{80}$ from \CGeqref{eq:Psi_def}, $\langle u^2\rangle=Q_2-\frac1{12}+o(1)$ and $\langle u^4\rangle=Q_4-\frac12Q_2+\frac7{240}+o(1)$; insert them in the first inequality with $j=1$ and $j=2$.
\end{proof}

\begin{remark}[What the certificate needs]\label{rem:simple_threshold}
The cross term $\frac1{\#\IT}\int_T^{2T}(N-F_X)^2S_X'\,dt$, which comes from $dF_X=(\lL+S_X')\,dt$, is part of $Q_2$; no hypothesis on the zeros enters \CGeqref{eq:simple_Q}. The first form gives a positive proportion as soon as $Q_2(T,T^c)\le\frac13-\eta$ for one fixed $c\le\frac12$, $\eta>0$ and all large $T$, and the proportion $\frac23$ when $Q_2\le\frac16$. Theorem~\CGref{thm:main} and \CGeqref{eq:identity_quadratic} give $Q_2(T,T^c)=\frac1{2\pi^2}\log\frac1c+O(1+\sqrt{\log(1/c)})$, with an absolute constant that is not computed; so the corollary yields no numerical proportion here. Unconditionally, more than two thirds of the zeros are simple and on the critical line, $0.6725$ with the window of Montgomery and Taylor, by Alp\"oge and Furman \cite{AlpogeFurman2026} and, with another proof, by Lamzouri \cite{Lamzouri2026}; Knausg\aa rd \cite{Knausgard2026} obtains $0.67353$ by a computer-assisted argument. These proofs rest on Montgomery's pair-correlation method in the unconditional form of Baluyot, Goldston, Suriajaya and Turnage-Butterbaugh \cite{BGSTB2024}; Theorem F uses a different integrality step, Lemma~\CGref{lem:mult_ordinate}, and a different quantity, $Q_2$.
\end{remark}

\section{Theorem G: the finite Euler product in the zeta function of the corrected roots}
\label{sec:euler_product}
For a real sequence $\kappa=(\kappa_k)_{k\ge1}$ with $\kappa_k\ne0$ and $\sum_k\kappa_k^{-2}<\infty$ put
\begin{equation}
\zeta_\kappa(s)=\frac1{G(s)}\prod_{k\ge1}\Bigl(1+\frac{s(s-1)}{\frac14+\kappa_k^2}\Bigr),\qquad G(s)=s(s-1)\pi^{-s/2}\Gamma\bigl(\tfrac s2\bigr).
\label{eq:zeta_kappa}
\end{equation}
The product converges absolutely and locally uniformly, its factors vanish exactly at $s=\frac12\pm i\kappa_k$, and $G(1-s)\zeta_\kappa(1-s)=G(s)\zeta_\kappa(s)$, the functional equation of $\zeta$ in the form $\xi(1-s)=\xi(s)$; if all nontrivial zeros of $\zeta$ were on the critical line, the Hadamard product of $\xi$ would give $\zeta_\gamma=\zeta$. With $z=s-\frac12$,
\begin{equation}
1+\frac{s(s-1)}{\frac14+t^2}=\frac{t^2+z^2}{t^2+\frac14},\qquad f_z(t)=\log\frac{t^2+z^2}{t^2+\frac14}\quad(\Re z>0,\ t\in\R),
\label{eq:f_z}
\end{equation}
with the principal logarithm: for $\Re z>0$ and real $t$, $t^2+z^2\notin(-\infty,0]$, so $f_z(t)$ is holomorphic in $z$, real for real $z>0$, and $f_z(t)=O_z(t^{-2})$, $\partial_tf_z(t)=2t(\frac14-z^2)/((t^2+z^2)(t^2+\frac14))=O_z(t^{-3})$ as $t\to\infty$, locally uniformly in $z$. For two such sequences $\kappa,\kappa'$ with $\kappa_k-\kappa'_k$ bounded, $\sum_k(f_z(\kappa_k)-f_z(\kappa'_k))$ converges absolutely and is a holomorphic logarithm of $\zeta_\kappa/\zeta_{\kappa'}$ in $\Re s>\frac12$, real on $(\frac12,\infty)$.

\begin{lemma}\label{lem:fourier_log}
For $\Re z>0$ and $\omega>0$,
\[
\int_0^\infty f_z(t)\cos(\omega t)\,dt=\frac\pi\omega\bigl(e^{-\omega/2}-e^{-\omega z}\bigr).
\]
\end{lemma}

\begin{proof}
For real $a>0$, $\int_0^\infty\frac{2a\cos\omega t}{t^2+a^2}dt=\pi e^{-a\omega}$ (residue theorem). Differentiation under the integral sign, dominated by $2a_2/(t^2+a_1^2)$ for $a\in[a_1,a_2]\subset(0,\infty)$, gives $\frac d{da}\int_0^\infty\log\frac{t^2+a^2}{t^2+1/4}\cos\omega t\,dt=\pi e^{-a\omega}$; both sides of the lemma vanish at $a=\frac12$, so the lemma holds for real $z=a>0$. Both sides are holomorphic in $z$ on $\Re z>0$, the left one by dominated convergence ($|f_z(t)|\ll_K1+|\log t|$ for $t\le1$ and $\ll_Kt^{-2}$ for $t\ge1$, uniformly for $z$ in a compact $K$), and they agree on $(0,\infty)$.
\end{proof}

\begin{lemma}[The midpoint rule along a monotone model]\label{lem:midpoint_rule}
Let $\mathsf F\in C^1[t_*,\infty)$ with $\mathsf F'>0$ on $[t_*,\infty)$, $\mathsf F(t)\to\infty$ and $\mathsf F(t_*)=v_*\in\mathbb Z$, and let $\rho_k$ be the root of $\mathsf F(t)=k-\frac12$, $k>v_*$. Let $\phi\in C^1[t_*,\infty)$ with $\phi\to0$ at $\infty$ and $\int_{t_*}^\infty(|\phi|\mathsf F'+|\phi'|)\,dt<\infty$. Then, with the $1$-periodic sawtooth $\psi(v)=\lfloor v+\frac12\rfloor-v$,
\[
\sum_{k>v_*}\phi(\rho_k)=\int_{t_*}^\infty\phi(t)\mathsf F'(t)\,dt-\int_{t_*}^\infty\phi'(t)\,\psi\bigl(\mathsf F(t)\bigr)\,dt .
\]
\end{lemma}

\begin{proof}
Put $g=\phi\circ\mathsf F^{-1}$ on $[v_*,\infty)$ and $C(v)=\#\{k>v_*:k-\frac12\le v\}=\lfloor v+\frac12\rfloor-v_*$. Then $\sum_{k>v_*}\phi(\rho_k)=\int_{(v_*,\infty)}g\,dC$, and $C(v)-(v-v_*)=\psi(v)$ vanishes at $v=v_*$ and is bounded; integration by parts gives $\int g\,dC=\int_{v_*}^\infty g\,dv-\int_{v_*}^\infty g'(v)\psi(v)\,dv$, the boundary term at $\infty$ vanishing because $g\to0$. Substitute $v=\mathsf F(t)$, $g'(v)\,dv=\phi'(t)\,dt$.
\end{proof}

\begin{theorem}[Theorem G]\label{thm:euler_product}
Let $X\ge2$ be fixed and $M_X$ the bound for $|S_X'|$ in \CGeqref{eq:sigma_M_def}. Let $t_1>2\pi$ with $\lL(t_1)\ge2M_X$, so that $F_X'\ge\frac12\lL>0$ on $[t_1,\infty)$; let $v_0=\lceil F_X(t_1)\rceil$, $t_0=F_X^{-1}(v_0)$, $k_0=v_0+1$, and for $k\ge k_0$ let $\kappa_k$ be the unique root of $F_X(t)=k-\frac12$ in $[t_0,\infty)$; for $1\le k<k_0$ let $\kappa_k$ be any nonzero reals, for instance $\kappa_k=\tau_k$. Let $P_X(s)=\prod_{p\le X}(1-p^{-s})^{-1}$. Then, for $\Re s>\frac12$,
\begin{equation}
\sum_{k\ge1}\bigl(f_z(\kappa_k)-f_z(\tau_k)\bigr)=\log P_X(s)-\log P_X(1)+H_X(s),
\label{eq:euler_product}
\end{equation}
that is $\zeta_\kappa(s)=\zeta_\tau(s)\,P_X(s)P_X(1)^{-1}e^{H_X(s)}$, where, with $t_0'=\NO^{-1}(0)$ and $\psi$ as in Lemma~\CGref{lem:midpoint_rule},
\[
H_X(s)=\sum_{k<k_0}f_z(\kappa_k)-\int_{t_0'}^{t_0}f_z\lL\,dt-\int_0^{t_0}f_zS_X'\,dt-\int_{t_0}^\infty\partial_tf_z\,\psi(F_X)\,dt+\int_{t_0'}^\infty\partial_tf_z\,\psi(\NO)\,dt
\]
is holomorphic in $\Re s>\frac12$ and is determined by $X$, $\NO$, the primes $p\le X$ and the choices of $t_1$ and of $\kappa_k$, $k<k_0$, on which the left side of \CGeqref{eq:euler_product} depends in the same way.
\end{theorem}

\begin{proof}
$\NO$ is increasing on $(2\pi,\infty)$ with $\NO(t_0')=0$, and $\tau_k$, $k\ge1$, are the roots of $\NO=k-\frac12$; $F_X$ is increasing on $[t_0,\infty)$ and the $\kappa_k$, $k\ge k_0$, are the roots of $F_X=k-\frac12$ there. Lemma~\CGref{lem:midpoint_rule} applies to both, with $\phi=f_z$ (the integrability conditions hold by the bounds after \CGeqref{eq:f_z}, $\lL\ll\log t$ and $|S_X'|\le M_X$):
\begin{gather*}
\sum_{k\ge k_0}f_z(\kappa_k)=\int_{t_0}^\infty f_z(\lL+S_X')\,dt-\int_{t_0}^\infty\partial_tf_z\,\psi(F_X)\,dt,\\
\sum_{k\ge1}f_z(\tau_k)=\int_{t_0'}^\infty f_z\lL\,dt-\int_{t_0'}^\infty\partial_tf_z\,\psi(\NO)\,dt .
\end{gather*}
Subtracting, it remains to evaluate $\int_0^\infty f_zS_X'\,dt$. By \CGeqref{eq:intro_SX} and $\arg(1-w)=-\Im\sum_{m\ge1}w^m/m$ for $|w|<1$, $S_X(t)=-\frac1\pi\sum_{p\le X}\sum_{m\ge1}\frac{\sin(mt\log p)}{mp^{m/2}}$, so $S_X'(t)=-\frac1\pi\sum_{p\le X}\sum_{m\ge1}\frac{\log p}{p^{m/2}}\cos(mt\log p)$, uniformly convergent. Since $f_z\in L^1(0,\infty)$, the sum may be integrated term by term, and Lemma~\CGref{lem:fourier_log} with $\omega=m\log p$ gives
\[
\int_0^\infty f_zS_X'\,dt=-\sum_{p\le X}\sum_{m\ge1}\frac{\log p}{p^{m/2}}\,\frac{p^{-m/2}-p^{-mz}}{m\log p}=\sum_{p\le X}\sum_{m\ge1}\frac{p^{-ms}-p^{-m}}m=\log P_X(s)-\log P_X(1),
\]
with principal logarithms, $|p^{-s}|<1$. Each term of $H_X$ is holomorphic in $\Re s>\frac12$: the finite sum and the integrals over bounded intervals because $f_z(t)$ is holomorphic in $z$ and locally bounded, the two integrals with $\psi$ by dominated convergence, since $|\psi|\le\frac12$ and $\partial_tf_z(t)=O(t^{-3})$ locally uniformly in $z$. Exponentiating, and using that both sides of \CGeqref{eq:euler_product} are real for real $s>\frac12$, gives the product form.
\end{proof}

\begin{remark}\label{rem:euler_product}
The zeros of $\zeta_\kappa$ are on the critical line by construction, and $\zeta_\tau$, $P_X$ and $e^{H_X}$ are free of $\zeta$: Theorem G separates, in the zeta function of the corrected roots, the part supplied by the primes, which is exactly the finite Euler product $P_X$, from the part supplied by the clock. Consequently, in $\Re s>1$, $\zeta(s)/\zeta_\kappa(s)=\bigl(\zeta(s)/P_X(s)\bigr)\,P_X(1)\,e^{-H_X(s)}/\zeta_\tau(s)$, and in $\Re s>\frac12$ the only factor on the right whose singularities are not explicit is $\zeta/P_X$, whose zeros and poles there are those of $\zeta$. The roots $\kappa_k$, $k\ge k_0$, are the roots $t_k^X$ of Proposition~\CGref{prop:monotone} on every window where both are defined. For a cutoff growing with the height, as in Theorems B and D, the same computation gives a hybrid form in which the prime $p$ enters from the height where it enters the cutoff; this is not proved here.
\end{remark}

\section{Conclusions}
\label{sec:conclusions}''')

# ---------------------------------------------------------------- bibliography additions
rep('\\bibitem{BellottiWong2025}', r'''\bibitem{AlpogeFurman2026}
L. Alp\"oge, R. Furman, More than two thirds of the zeta zeros are simple and on the critical line, preprint (2026), \href{https://arxiv.org/abs/2608.13637}{arXiv:2608.13637}. (No DOI.)

\bibitem{BGSTB2024}
S.A.C. Baluyot, D.A. Goldston, A.I. Suriajaya, C.L. Turnage-Butterbaugh, An unconditional Montgomery theorem for pair correlation of zeros of the Riemann zeta-function, Acta Arith. 214 (2024) 357--376, \href{https://doi.org/10.4064/aa230612-20-3}{https://doi.org/10.4064/aa230612-20-3}.

\bibitem{BellottiWong2025}''')
rep('\\bibitem{KorolevPIM2012}', r'''\bibitem{Knausgard2026}
K.M. Knausg\aa rd, More than 83.9\% of the zeros of the Riemann zeta function are distinct and more than 67.35\% are simple and on the critical line, preprint (2026), \href{https://arxiv.org/abs/2610.08965}{arXiv:2610.08965}. (No DOI.)

\bibitem{KorolevPIM2012}''')
rep('\\bibitem{LeClair2021}', r'''\bibitem{Lamzouri2026}
Y. Lamzouri, A new proof that more than $2/3$ of the zeros of the Riemann zeta function are simple and on the critical line, preprint (2026), \href{https://arxiv.org/abs/2609.02882}{arXiv:2609.02882}. (No DOI.)

\bibitem{LeClair2021}''')

rep('mean-square error in height, $O(1)$ mean spacings after', 'mean-square error in the ordinates, $O(1)$ mean spacings after')
rep('and the error of a point computed from the primes are different objects', 'and the error of a point calculated from the primes are different objects')

rep(r'first $C$, $C_0$, $C_3$, $C_5$, given by Lemmas~\CGref{lem:higher_moments}, \CGref{lem:sampling_rho}, Theorem~\CGref{thm:multiplicity_all} and \CGeqref{eq:uniform_recursion}; then $C_\star$; then $B_\star$ and $C_6$; then $H^*$.',
    r'first $C$, $C_0$, $C_3$, given by Lemmas~\CGref{lem:higher_moments}, \CGref{lem:sampling_rho} and Theorem~\CGref{thm:multiplicity_all}; then $C_\star$, which depends only on $C$ and $C_3$; then $C_5$, the coefficient of \CGeqref{eq:uniform_recursion}, obtained once $C_\star$ is fixed; then $B_\star$ and $C_6$; then $H^*$.')
rep(r'with $u_k=\max(T-1,\gamma_k-\mathsf Rb)\in[T-1,2T]$, because $h\ge2\mathsf Rb$,',
    r'with $u_k=\max(T-1,\gamma_k-\mathsf Rb)\in[T-1,2T]$, because $h\ge2\mathsf Rb$; since $N(u_k+h)-N(u_k)$ counts $(u_k,u_k+h]$, we bound the count by $N(u_k+h)-N(u_k-1)$, an interval of length $h+1\le2h$ with $u_k-1\in[T-2,2T]$, which changes only the constant,')
rep(r'so $A_0(r)\le C_0r^2$ for $r\ge1$.', r'so $A_0(r)\le C_0(r^2/\sqrt{H_0}+\sqrt r)\le2C_0r^2$ for $r\ge1$.')
rep(r'Let $B_\star=\max(2C,C_0,1)$', r'Let $B_\star=\max(2C,2C_0,1)$')

TEX.write_text(head + sep + body)
print('patched', TEX)
