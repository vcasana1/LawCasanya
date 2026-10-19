#!/usr/bin/env python3
"""v10 = v9 + Theorem D' (regularized clock with a fixed cutoff) + attribution of the clock
equation to the Riemann--von Mangoldt main term inverted by Lambert's function (the corrected
clock equation is no longer called "LeClair's equation") + Gonek's finite Euler products.

Run on a copy of ../v9/manuscript/prime_corrected_clock_v9.tex saved as the v10 file name.
Every replacement must match exactly once.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
TEX = ROOT / 'manuscript' / 'prime_corrected_clock_v10.tex'
src = TEX.read_text()
head, sep, body = src.partition('\\begin{document}')
assert sep


def rep(old, new):
    global body
    n = body.count(old)
    if n != 1:
        sys.exit(f'expected 1 match, found {n}:\n{old[:300]}')
    body = body.replace(old, new)


# ================================================================ abstract
rep(r"""in units of $\sqrt{H_m}$; (E)""",
    r"""in units of $\sqrt{H_m}$; (D$'$) with a fixed cutoff $X=T^c$, the best $L^4$ approximation of $\NO+S_X$ on $[\frac T2,3T]$ by piecewise linear functions with slopes between $\frac{\log T}{4\pi}$ and $\frac{\log T}\pi$ is unique and is computed without zeros, its level points $\widehat x_k$ are increasing with gaps between $\pi/\log T$ and $4\pi/\log T$, and $\langle|\widehat x_k-\gamma_k|^4\rangle_{\IT}\ll(1+\log\frac1c)^2/\log^4T$ uniformly for $2\le X\le T^{1/3}$: one step and a fixed power of the height suffice; (E)""")
rep(r"""The clock equation corrected by the primes $p\le X$ is, up to the term $1/(48t)$ of Stirling's series, the prime equation proposed by LeClair for the $n$-th zero, whose accuracy was estimated there numerically; for $p_N\le T^{1/2}$, (B) and (D) are proved statements about that equation at the true ordinates and about explicit corrected points.""",
    r"""The clock is the Riemann--von Mangoldt main term inverted by Lambert's function; the same clock equation corrected by the first $N$ primes was solved numerically by LeClair, and the zeros of Gonek's finite Euler products solve a version of it with smoothed weights, with accuracy supported numerically in both cases; for $X\le T^{1/2}$, (B), (D) and (D$'$) are proved statements about this equation at the true ordinates and about explicit points.""")

# ================================================================ intro: program, degree, known results
rep(r"""by one or several Newton-type steps for the corrected equation $\NO(t)+S_X(t)=k-\frac12$ from $t=\tau_k$, with cutoffs that depend only on the height. Every corrected point is a closed expression in $k$, $\tau_k$ and the primes:""",
    r"""by one or several Newton-type steps for the corrected equation $\NO(t)+S_X(t)=k-\frac12$ from $t=\tau_k$, with cutoffs that depend only on the height, or, with a fixed cutoff, by solving the same equation for a regularized version of $\NO+S_X$, its best $L^4$ approximation by increasing piecewise linear functions with controlled slopes (Theorem D$'$). Every corrected point is computed from $k$, $\NO$ and the primes:""")
rep(r"""Theorems A and C are exact identities; Theorems B and D are asymptotic statements in mean square over the zeros with $T<\gamma_k\le2T$;""",
    r"""Theorems A and C are exact identities; Theorems B, D and D$'$ are asymptotic statements in mean square (in fourth mean for D$'$) over the zeros with $T<\gamma_k\le2T$;""")
rep(r"""its first approximation, without the argument, is solved by the Lambert formula \cite[(63), p.~24]{FrancaLeClair2015}, which is the clock \CGeqref{eq:intro_clock}.""",
    r"""its first approximation, without the argument, is the clock equation $\NO(t)=n-\frac12$, which they solve with Lambert's function \cite[(62)--(63), p.~24]{FrancaLeClair2015}, as in \CGeqref{eq:intro_clock}; this inversion of the Riemann--von Mangoldt main term is elementary \cite{Corless1996}.""")
rep(r"""LeClair \cite[\S VI, (49), p.~18]{LeClair2021} replaces $\arg\zeta$ by the Euler phase of the first $N$ primes; the resulting equation no longer contains $\zeta$, and it is, up to the term $1/(48t)$ of Stirling's series, the corrected clock equation $\NO(t)+S_X(t)=n-\frac12$ of this paper with $X=p_N$. It is solved there by a root finder, adding one prime at a time from the Lambert value.""",
    r"""LeClair \cite[\S VI, (49), p.~18]{LeClair2021} replaces $\arg\zeta$ by the Euler phase of the first $N$ primes; the resulting equation contains no $\zeta$, and, up to the term $1/(48t)$ of Stirling's series, it is the clock equation corrected by the primes, $\NO(t)+S_X(t)=n-\frac12$ with $X=p_N$. It is solved there by a root finder, adding one prime at a time from the Lambert value.""")
rep(r"""For $p_N\le T^{1/2}$, Theorem B below is a statement about LeClair's equation at the true ordinates, and Theorem D about explicit corrected points that replace its root finder (Table~\CGref{tab:evaluates});""",
    r"""For $p_N\le T^{1/2}$, Theorem B below is a statement about this equation at the true ordinates, and Theorems D and D$'$ about explicit points that replace the root finder (Table~\CGref{tab:evaluates});""")
rep(r"""lie inside it.
\end{itemize}""",
    r"""lie inside it.
\item Gonek's finite Euler products $\zeta_X(s)=P_X(s)+\chi(s)\overline{P_X(s)}$, with $P_X$ the exponential of a sum over $n\le X^2$ with weights $\Lambda_X(n)$ \cite[(7), \S5]{Gonek2012}, have all their zeros above a fixed height on the critical line \cite[Thm.~6.2]{Gonek2012}. On the line $\zeta_X(\frac12+it)=2e^{-i\vartheta(t)}\Re\bigl(e^{i\vartheta(t)}P_X(\frac12+it)\bigr)$, so these zeros are the solutions of $\NO(t)+\widetilde S_X(t)+\varpi(t)/\pi\in\mathbb Z+\frac12$, where $\pi\widetilde S_X(t)=\Im\log P_X(\frac12+it)$ is the prime phase with Gonek's weights: a corrected clock equation with smoothed weights. Their closeness to the zeros of $\zeta$ is supported numerically there; under the Riemann hypothesis, a modified function $\zeta_X^*$ has, for $X$ large depending on the interval, no zero in a closed interval between consecutive ordinates \cite[Thm.~9.1]{Gonek2012}.
\end{itemize}""")

# ================================================================ tab:antecedents
rep(r"""Prime equation for the $n$-th zero
& Fran\c{c}a--LeClair's equation with $\arg\zeta$ \cite[(20)]{FrancaLeClair2015} and LeClair's equation with the first $N$ primes \cite[(49)]{LeClair2021}, solved numerically; accuracy shown by comparison with known zeros \cite[Table~I]{LeClair2021}, without a proved error bound.
& LeClair's equation is the corrected clock equation with $X=p_N$, up to $1/(48t)$. For $p_N\le T^{1/2}$, Theorem~\CGref{thm:main} gives its mean-square defect at the true ordinates;""",
    r"""Corrected clock equation, solved numerically
& The equation with $\arg\zeta$ \cite[(20)]{FrancaLeClair2015}; the clock equation corrected by the first $N$ primes \cite[(49)]{LeClair2021}; with smoothed weights, the equation of the zeros of Gonek's $\zeta_X$ \cite[Thm.~6.2]{Gonek2012}. Accuracy shown by comparison with known zeros \cite[Table~I]{LeClair2021}, without a proved error bound.
& For $p_N\le T^{1/2}$, Theorem~\CGref{thm:main} gives the mean-square defect of the corrected clock equation at the true ordinates;""")
rep(r"""Theorems~\CGref{thm:computable_clock}--\CGref{thm:uniform_iteration} replace the root finder by explicit steps with proved mean-square error.\\""",
    r"""Theorems~\CGref{thm:computable_clock}--\CGref{thm:uniform_iteration} replace the root finder by explicit steps with proved mean-square error, and Theorem~\CGref{thm:regularized_clock} by one regularization with a fixed cutoff.\\""")
rep(r"""& Theorem~\CGref{thm:uniform_iteration} gives uniform control through $\log^*T+O(1)$ prescribed corrections, with a multiplicity estimate. Corollary~\CGref{cor:sorted_clock} gives a nondecreasing output with height MSE $O(\log^{-2}T)$.""",
    r"""& Theorem~\CGref{thm:uniform_iteration} gives uniform control through $\log^*T+O(1)$ prescribed corrections, with a multiplicity estimate. Corollary~\CGref{cor:sorted_clock} gives a nondecreasing output with height MSE $O(\log^{-2}T)$. Theorem~\CGref{thm:regularized_clock} gives the same scale in one step with a fixed cutoff, in fourth mean, with increasing points separated by at least $\pi/\log T$; its points are defined by a convex program on the whole block, not index by index.""")

# ================================================================ tab:evaluates
rep(r"""Lambert formula \cite[(63)]{FrancaLeClair2015} $=$ clock $\tau_k$
& Nothing: a closed expression in $k$.""",
    r"""Clock $\tau_k$: the Riemann--von Mangoldt main term inverted by $W_0$ \cite{Corless1996}; also \cite[(63)]{FrancaLeClair2015}
& Nothing: a closed expression in $k$.""")
rep(r"""LeClair, prime equation \cite[(49)]{LeClair2021}
& The first $N$ primes; root finder. No $\zeta$, no zero.""",
    r"""Clock equation corrected by the first $N$ primes, solved numerically \cite[(49)]{LeClair2021}
& The first $N$ primes; root finder. No $\zeta$, no zero.""")
rep(r"""& Estimated numerically \cite[Table~I]{LeClair2021}; argued from $S(t)=O(1)$, which is false.\\""",
    r"""& Estimated numerically \cite[Table~I]{LeClair2021}; argued from $S(t)=O(1)$, which is false.\\
Zeros of Gonek's $\zeta_X$ \cite{Gonek2012}
& The prime powers $n\le X^2$ with weights $\Lambda_X(n)$; the zeros are computed numerically. No $\zeta$, no zero.
& On the critical line above a fixed height (proved); closeness to the zeros of $\zeta$ supported numerically.\\""")
rep(r"""& Proved: defect at the ordinates (B), mean-square error in height, $O(1)$ mean spacings after $\log^*T+O(1)$ steps, tails (D).\\""",
    r"""& Proved: defect at the ordinates (B), mean-square error in height, $O(1)$ mean spacings after $\log^*T+O(1)$ steps, tails (D).\\
Theorem D$'$ (this paper)
& $\NO$ and the primes $p\le T^c$, $c$ fixed; one convex program on $[\frac T2,3T]$ and linear interpolation. No $\zeta$, no zero.
& Proved: $\langle|\widehat x_k-\gamma_k|^4\rangle\ll(1+\log\frac1c)^2/\log^4T$; increasing points with gaps in $[\pi/\log T,4\pi/\log T]$.\\""")

# ================================================================ intro: what this paper adds, item D'
rep(r"""\item \textbf{The pointwise envelope} (Proposition~\CGref{prop:envelope_equivalence} and Theorem~\CGref{thm:envelope}).""",
    r"""\item[\textbf{D$'$.}] \textbf{A regularized clock with a fixed cutoff} (Theorem~\CGref{thm:regularized_clock}). Let $2\le X\le T^{1/3}$, $c=\log X/\log T$, and let $\widehat F$ be the best $L^4$ approximation of $\NO+S_X$ on $[\frac T2,3T]$ among the piecewise linear functions on a mesh of step at most $2\pi/\log T$ with slopes between $\frac{\log T}{4\pi}$ and $\frac{\log T}\pi$; it is unique and depends only on $\NO$ and the primes $p\le X$. The level points $\widehat F(\widehat x_k)=k-\frac12$ are increasing, $\pi/\log T\le\widehat x_{k+1}-\widehat x_k\le4\pi/\log T$, and
\begin{equation}
\frac1{\#\IT}\sum_{k\in\IT}\bigl|\widehat x_k-\gamma_k\bigr|^4\ll\frac{(1+\log(1/c))^2}{\log^4T},
\label{eq:intro_Dprime}
\end{equation}
with absolute constants. For fixed $c$ this is the scale of one mean spacing, reached in one step without iteration, sorting or growing cutoffs. If $X\le T^{1/4}$, the transport $S_X(\gamma_k)-S_X(\widehat x_k)$ is bounded in mean square. The price is locality: $\widehat x_k$ depends on $S_X$ on the whole block, through a convex program with $\asymp T\log T$ variables, whereas the Newton-type points of Theorem D are explicit index by index.
\item \textbf{The pointwise envelope} (Proposition~\CGref{prop:envelope_equivalence} and Theorem~\CGref{thm:envelope}).""")
rep(r"""iterating the Newton-type step brings it down to $O(1)$.""",
    r"""iterating the Newton-type step brings it down to $O(1)$, and the regularization of Theorem D$'$ does so in one step with a fixed cutoff $X=T^c$.""")

# ================================================================ tab:status
rep(r"""& unconditional & zero-free corrected points with mean-square error $O(1)$ mean spacings & no ($k$, $\tau_k$, primes)\\""",
    r"""& unconditional & zero-free corrected points with mean-square error $O(1)$ mean spacings & no ($k$, $\tau_k$, primes)\\
Theorem~\CGref{thm:regularized_clock} (D$'$) & unconditional & one step, fixed cutoff, fourth mean $O(1)$ mean spacings, separated increasing points & no ($\NO$, primes)\\""")

# ================================================================ organization
rep(r"""Section~\CGref{sec:iteration} iterates the Newton-type step uniformly in the number of steps, and Section~\CGref{sec:envelope} proves Theorem E.""",
    r"""Section~\CGref{sec:iteration} iterates the Newton-type step uniformly in the number of steps, Section~\CGref{sec:regularized} proves Theorem D$'$, and Section~\CGref{sec:envelope} proves Theorem E.""")

# ================================================================ notation
rep(r"""$\tau_k$, $\tau_x$, $W_0$ & RvM clock \CGeqref{eq:clock}; the same for real $x\ge1$; principal Lambert function\\""",
    r"""$\tau_k$, $\tau_x$, $W_0$ & RvM clock \CGeqref{eq:clock}; the same for real $x\ge1$; principal Lambert function\\
$\Lambda_T$, $\mathsf J_T$, $\mathcal K_T$ & $\frac{\log T}{2\pi}$; the block $[\frac T2,3T]$; piecewise linear functions with slopes in $[\frac12\Lambda_T,2\Lambda_T]$ (Section~\CGref{sec:regularized})\\
$\widehat F$, $\widehat x_k$, $\widehat u_k$ & regularized counting model, its level points, its defect at $\gamma_k$ (Section~\CGref{sec:regularized})\\""")

# ================================================================ the new section
NEW_SECTION = r"""%======================================================================
\section{\texorpdfstring{Theorem D$'$}{Theorem D'}: a regularized clock with a fixed cutoff}
\label{sec:regularized}

For a fixed cutoff exponent the one-step clock is controlled in mean square if and only if its transport is (Remark~\CGref{rem:newton}), and this is not proved here. The construction below avoids the transport from $\tau_k$: it replaces $F_X=\NO+S_X$ by its best $L^4$ approximation among increasing piecewise linear functions with slopes comparable to $\lL$, and solves the clock equation for that function. A fixed power of the height then suffices, in one step.

\subsection{The construction}
For $T\ge T_0$ let $\Lambda_T=\frac{\log T}{2\pi}$, $\mathsf J_T=[\frac T2,3T]$, $\mathsf M_T=\lceil\frac52T\Lambda_T\rceil$, $\eta_T=\frac{5T}{2\mathsf M_T}\le\Lambda_T^{-1}$ and $t_i=\frac T2+i\eta_T$, $0\le i\le\mathsf M_T$. Let $\mathcal K_T$ be the set of continuous functions $P$ on $\mathsf J_T$ that are linear on each $[t_{i-1},t_i]$ with slope in $[\frac12\Lambda_T,2\Lambda_T]$. For $X\ge2$ let $F_X=\NO+S_X$.

\begin{definition}[Regularized clock]\label{def:regularized}
$\widehat F=\widehat F_{T,X}$ is the element of $\mathcal K_T$ that minimizes $\int_{\mathsf J_T}|P-F_X|^4\,dt$ over $P\in\mathcal K_T$. For every integer $k$ with $\widehat F(\frac T2)<k-\frac12<\widehat F(3T)$, $\widehat x_k=\widehat x_k(T,X)\in\mathsf J_T$ is the solution of $\widehat F(\widehat x_k)=k-\frac12$, and $\widehat u_k=k-\frac12-\widehat F(\gamma_k)$ when $\gamma_k\in\mathsf J_T$.
\end{definition}

\begin{lemma}[The regularized clock is well defined]\label{lem:regularized_def}
For $T\ge T_0$ and $X\ge2$ the minimizer $\widehat F$ exists and is unique; $\widehat F$ is strictly increasing with $\frac12\Lambda_T\le\widehat F'\le2\Lambda_T$ on each mesh interval; each $\widehat x_k$ is unique, obtained by locating the mesh interval where $\widehat F$ crosses $k-\frac12$ and interpolating linearly; and
\begin{equation}
\frac\pi{\log T}\le\widehat x_{k+1}-\widehat x_k\le\frac{4\pi}{\log T}
\label{eq:regularized_gaps}
\end{equation}
whenever both points are defined. $\widehat F$ and the $\widehat x_k$ depend only on $T$, $\NO$ and the primes $p\le X$; no value of $\zeta$ and no zero enters.
\end{lemma}

\begin{proof}
For $T\ge T_0$ and $t\in[\frac T2-1,3T+1]$, $\NO'(t)=\lL(t)=\frac1{2\pi}\log\frac t{2\pi}\in[\frac34\Lambda_T,\frac54\Lambda_T]$. An element of $\mathcal K_T$ is determined by its nodal values $v=(v_0,\dots,v_{\mathsf M_T})$, and $\mathcal K_T$ corresponds to the closed convex polyhedron $\{v:\frac12\Lambda_T\eta_T\le v_i-v_{i-1}\le2\Lambda_T\eta_T\}$; it contains the interpolation of $\NO$, whose chord slopes are values of $\NO'$. The functional $\Phi(v)=\int_{\mathsf J_T}|P_v-F_X|^4\,dt$ is continuous; it is strictly convex, because $z\mapsto|z|^4$ is strictly convex and $P_v\ne P_w$ on a set of positive measure when $v\ne w$; and it tends to infinity on the polyhedron as $|v|\to\infty$, because the slopes are bounded and $F_X$ is bounded on $\mathsf J_T$, so $|v_0|\to\infty$ and $|P_v-F_X|\to\infty$ uniformly. Hence there is a unique minimizer. The slope bounds give strict monotonicity and the uniqueness of $\widehat x_k$, and $1=\widehat F(\widehat x_{k+1})-\widehat F(\widehat x_k)$ lies between $\frac12\Lambda_T$ and $2\Lambda_T$ times $\widehat x_{k+1}-\widehat x_k$, which is \CGeqref{eq:regularized_gaps}. The data of the program are $\NO$ and $S_X$.
\end{proof}

\subsection{Three lemmas}

\begin{lemma}[Theorem A for Lipschitz models]\label{lem:identity_lipschitz}
Theorems~\CGref{thm:identity_general} and \CGref{thm:identity_g} hold for every real Lipschitz function $F$ on an open interval containing $[\gamma_{k_1},\gamma_{k_2}]$, with $F'$ its derivative almost everywhere; in particular for the functions of $\mathcal K_T$.
\end{lemma}

\begin{proof}
The integrands are bounded and measurable. In the proofs, the only use of $F\in C^1$ is the evaluation of $\int_{\gamma_k}^{\gamma_{k+1}}\mathfrak g(k-F)F'\,dt$ on a gap. If $F$ is Lipschitz, $t\mapsto\mathfrak G(k-F(t))$ is Lipschitz on $[\gamma_k,\gamma_{k+1}]$ ($\mathfrak G$ is $C^1$ and $F$ is bounded there), hence absolutely continuous, with derivative $-\mathfrak g(k-F(t))F'(t)$ almost everywhere (chain rule for a $C^1$ function of a Lipschitz function), and the fundamental theorem of calculus for absolutely continuous functions gives the same value. The rest of both proofs is unchanged.
\end{proof}

\begin{lemma}[A slope-constrained model of the counting function]\label{lem:slope_envelope}
There are absolute constants $T_0$ and $C$ such that for $T\ge T_0$ there is $P_N\in\mathcal K_T$ with $\int_{\mathsf J_T}|P_N-N|^4\,dt\le CT$.
\end{lemma}

\begin{proof}
Let $\mathsf a=\frac12\Lambda_T$, $\mathsf b=2\Lambda_T$, $h_j=j/\Lambda_T$, $\phi(x)=\mathsf ax$ for $x\ge0$ and $\phi(x)=\mathsf bx$ for $x<0$, and
\[
H(t)=\sup_{s\in\mathsf J_T}\bigl(N(s)+\phi(t-s)\bigr)\qquad(t\in\mathsf J_T).
\]
Each function $t\mapsto N(s)+\phi(t-s)$ satisfies $\mathsf a(t_2-t_1)\le g(t_2)-g(t_1)\le\mathsf b(t_2-t_1)$ for $t_1<t_2$, and so does their supremum, which is finite because $N$ is bounded on $\mathsf J_T$; and $H\ge N$ (take $s=t$). Thus
\[
0\le H(t)-N(t)=\max\Bigl\{\sup_{s\le t}\bigl(\mathsf a(t-s)-(N(t)-N(s))\bigr),\ \sup_{s>t}\bigl(N(s)-N(t)-\mathsf b(s-t)\bigr)\Bigr\},
\]
with $s\in\mathsf J_T$. By \CGeqref{eq:N_decomposition} and $|\varpi|/\pi<\frac1{100}$, $N(y)-N(x)=\NO(y)-\NO(x)+S(y)-S(x)+\theta$ with $|\theta|<\frac1{50}$. Let $D^\pm_j(t)=\pm(S(t\pm h_j)-S(t))$.

If $s\le t$ and $t-s\in[h_j,h_{j+1})$, $j\ge0$, then $s\le t-h_j$, $N(s)\le N(t-h_j)$ and $\mathsf a(t-s)<\mathsf ah_j+\frac12$, so, with $\NO(t)-\NO(t-h_j)\ge\frac34j$,
\[
\mathsf a(t-s)-(N(t)-N(s))\le\tfrac12j-\tfrac34j+|D^-_j(t)|+1=|D^-_j(t)|-\tfrac14j+1 ,
\]
with $D_0^-=0$. If $s>t$ and $s-t\in[h_j,h_{j+1})$, then $N(s)\le N(t+h_{j+1})$ and $\mathsf b(s-t)\ge\mathsf bh_{j+1}-2$, and $\NO(t+h_{j+1})-\NO(t)\le\frac54(j+1)$ since $t+h_{j+1}\le3T+1$, so
\[
N(s)-N(t)-\mathsf b(s-t)\le|D^+_{j+1}(t)|-\tfrac34(j+1)+3 .
\]
Hence, with $Z_j=\max(|D^+_j|,|D^-_j|)$ for $1\le j\le j^*=\lceil\frac52T\Lambda_T\rceil+1$ (the terms with $t-h_j<\frac T2$ omitted from $D^-_j$),
\[
0\le H-N\le3+\sup_{1\le j\le j^*}\bigl(Z_j-\tfrac14j\bigr)_+ ,\qquad (H-N)^4\le8\Bigl(81+\sum_{j=1}^{j^*}\bigl(Z_j-\tfrac14j\bigr)_+^4\Bigr).
\]
Since $(z-\frac j4)_+^4\le(4z/j)^4z^4=256\,z^8/j^4$,
\[
\int_{\mathsf J_T}(H-N)^4\,dt\le648\cdot\tfrac52T+2048\sum_{j=1}^{j^*}j^{-4}\int_{\mathsf J_T}Z_j^8\,dt .
\]
By the substitution $u=t-h_j$ in the terms $D^-_j$, $\int_{\mathsf J_T}Z_j^8\le2\int_{T/2}^{3T}(S(u+h_j)-S(u))^8du$, and Theorem~\CGref{thm:known_fujii_difference} with $k=4$ on $(\frac T2,T)$, $(T,2T)$ and $(2T,4T)$ gives, with $h_j\wedge1=\min(h_j,1)$ and $(h_j\wedge1)\log(4T)+3\le8j+3$,
\[
\int_{T/2}^{3T}\bigl(S(u+h_j)-S(u)\bigr)^8du\ll T\bigl(\log((8j+3)e^4)\bigr)^4\ll T\log^4(j+3)\quad(j\le\Lambda_T),
\]
and $\ll T(\log\log T)^4$ for $j>\Lambda_T$. Therefore $\int_{\mathsf J_T}(H-N)^4\ll T+T\sum_{j\ge1}j^{-4}\log^4(j+3)+T(\log\log T)^4\Lambda_T^{-3}\ll T$. Let $P_N$ be the linear interpolation of $H$ at the nodes $t_i$. Its slopes are chord slopes of $H$, so $P_N\in\mathcal K_T$; on $[t_{i-1},t_i]$ both $H$ and $P_N$ lie between $H(t_{i-1})+\mathsf a(t-t_{i-1})$ and $H(t_{i-1})+\mathsf b(t-t_{i-1})$, so $|P_N-H|\le(\mathsf b-\mathsf a)\eta_T\le\frac32$. Hence $|P_N-N|\le H-N+\frac32$ and $\int_{\mathsf J_T}|P_N-N|^4\ll T$.
\end{proof}

\begin{lemma}[The prime model on the block]\label{lem:block_fourth}
There are absolute constants $T_0$ and $C$ such that for $T\ge T_0$ and $2\le X\le T^{1/3}$, with $c=\log X/\log T$,
\[
\int_{\mathsf J_T}|F_X-N|^4\,dt\le CT\bigl(1+\log(1/c)\bigr)^2 .
\]
\end{lemma}

\begin{proof}
By \CGeqref{eq:N_decomposition}, $F_X-N=-(S-S_X)-\varpi/\pi$ with $|\varpi|/\pi<\frac1{100}$. Apply \CGeqref{eq:R_fourth} on $(T',2T']$ for $T'\in\{\frac T2,T,2T\}$, which cover $\mathsf J_T$: for $T\ge T_0$, $2\le X\le T^{1/3}\le T'^{1/2}$, and by Lemma~\CGref{lem:V_size} the quantity $V$ computed at height $T'$ is $\log(\log T'/\log X)+O(1)=\log(1/c)+O(1)$, with $\log T'/\log T=1+O(1/\log T)$.
\end{proof}

\subsection{The theorem}

\begin{theorem}[Theorem D$'$]\label{thm:regularized_clock}
There are absolute constants $T_0$ and $C$ such that for $T\ge T_0$ and $2\le X\le T^{1/3}$, with $c=\log X/\log T$ and $\widehat F$, $\widehat x_k$, $\widehat u_k$ as in Definition~\CGref{def:regularized}:
\begin{enumerate}[label=(\alph*),leftmargin=2em]
\item $\widehat x_k$ is defined for every $k\in\IT\cup\mathcal I_T^\tau$, $\mathcal I_T^\tau=\{k:T\le\tau_k<2T\}$, and these points are increasing in $k$ with gaps \CGeqref{eq:regularized_gaps};
\item $\langle\widehat u_k^4\rangle_{\IT}\le C(1+\log(1/c))^2$ and $|\widehat x_k-\gamma_k|\le4\pi|\widehat u_k|/\log T$; hence
\begin{equation}
\bigl\langle|\widehat x_k-\gamma_k|^4\bigr\rangle_{\IT}\le\frac{C(1+\log(1/c))^2}{\log^4T},\qquad\bigl\langle|\widehat x_k-\gamma_k|^2\bigr\rangle_{\IT}\le\frac{C(1+\log(1/c))}{\log^2T};
\label{eq:regularized_main}
\end{equation}
\item $\max_{k\in\IT}|\widehat x_k-\gamma_k|\le CT^{1/5}$;
\item if $X\le T^{1/4}$, then $\bigl\langle(S_X(\gamma_k)-S_X(\widehat x_k))^2\bigr\rangle_{\IT}\le C(1+\log(1/c))\bigl((1+\log X)/\log T\bigr)^2\le C$.
\end{enumerate}
\end{theorem}

\begin{proof}
\emph{The regularized model is close to $N$.} By the minimizing property, Lemma~\CGref{lem:slope_envelope} and Lemma~\CGref{lem:block_fourth}, with $\|\cdot\|_4$ the norm of $L^4(\mathsf J_T)$,
\begin{equation}
\|\widehat F-N\|_4\le\|\widehat F-F_X\|_4+\|F_X-N\|_4\le\|P_N-F_X\|_4+\|F_X-N\|_4\le\|P_N-N\|_4+2\|F_X-N\|_4,
\label{eq:regularized_close}
\end{equation}
so $\int_{\mathsf J_T}|\widehat F-N|^4\le C_1T(1+\log(1/c))^2$ with an absolute $C_1$.

\emph{Two good heights.} Let $C_{\rm g}$ bound the gaps between consecutive ordinates (Theorem~\CGref{thm:known_basic}) and $K=(16C_1)^{1/4}(1+\log(1/c))^{1/2}$. By Chebyshev's inequality the set where $|\widehat F-N|>K$ has measure at most $T/16$, so there are $t_1\in[\frac T2+C_{\rm g},\frac{3T}4]$ and $t_2\in[\frac{9T}4,3T-C_{\rm g}]$ with $|\widehat F(t_i)-N(t_i)|\le K$. Since $c\ge\log2/\log T$, $K\ll(\log\log T)^{1/2}$.

\emph{(a).} $\widehat F$ is increasing, so $\widehat F(\frac T2)\le\widehat F(t_1)\le N(\frac{3T}4)+K$ and $\widehat F(3T)\ge\widehat F(t_2)\ge N(\frac{9T}4)-K$. For $k\in\IT$, $N(T)+1\le k\le N(2T)$; for $k\in\mathcal I_T^\tau$, $k-\frac12=\NO(\tau_k)\in[\NO(T),\NO(2T))$, and $|N-\NO|\ll\log T$ (Theorem~\CGref{thm:known_basic}). Since $N(T)-N(\frac{3T}4)$ and $N(\frac{9T}4)-N(2T)$ are $\gg T\log T$, $\widehat F(\frac T2)<k-\frac12<\widehat F(3T)$ for $T\ge T_0$. Monotonicity and gaps are Lemma~\CGref{lem:regularized_def}.

\emph{(b).} Let $k_1=N(t_1)$ and $k_2=N(t_2)+1$. Then $t_1-C_{\rm g}<\gamma_{k_1}\le t_1<\gamma_{k_1+1}$ and $\gamma_{k_2-1}\le t_2<\gamma_{k_2}\le t_2+C_{\rm g}$, so $[\gamma_{k_1},\gamma_{k_2}]\subset(\frac T2,3T)$ and $\IT\subset\{k:k_1<k<k_2\}$. As $\widehat F$ is increasing, $\widehat u_{k_1}\ge N(t_1)-\frac12-\widehat F(t_1)\ge-K-\frac12$ and $\widehat u_{k_2}\le N(t_2)+\frac12-\widehat F(t_2)\le K+\frac12$. Lemma~\CGref{lem:identity_lipschitz} with $j=2$, $\Psi_2(u)=u^4+\frac12u^2+\frac1{80}\ge u^4$ and $\widehat F'\le2\Lambda_T$ gives
\[
\begin{split}
\sum_{k\in\IT}\widehat u_k^4\le\sum_{k_1<k<k_2}\Psi_2(\widehat u_k)&=\int_{\gamma_{k_1}}^{\gamma_{k_2}}(N-\widehat F)^4\widehat F'\,dt-\frac{(\frac12+\widehat u_{k_1})^5+(\frac12-\widehat u_{k_2})^5}5\\
&\le2\Lambda_T\int_{\mathsf J_T}|N-\widehat F|^4\,dt+K^5 ,
\end{split}
\]
and $\#\IT\asymp T\log T$ gives the bound for $\langle\widehat u_k^4\rangle_{\IT}$. Since $\widehat F(\gamma_k)-\widehat F(\widehat x_k)=-\widehat u_k$ and $\widehat F'\ge\frac12\Lambda_T$, $|\widehat x_k-\gamma_k|\le2|\widehat u_k|/\Lambda_T=4\pi|\widehat u_k|/\log T$, which gives \CGeqref{eq:regularized_main}, the second bound by Cauchy--Schwarz.

\emph{(c).} Let $d=|\widehat x_k-\gamma_k|>0$. If $\widehat x_k>\gamma_k$, then for $t\in(\gamma_k,\widehat x_k)$, $N(t)\ge k$ and $\widehat F(t)\le k-\frac12-\frac12\Lambda_T(\widehat x_k-t)$; if $\widehat x_k<\gamma_k$, then for $t\in(\widehat x_k,\gamma_k)$, $N(t)\le k-1$ and $\widehat F(t)\ge k-\frac12+\frac12\Lambda_T(t-\widehat x_k)$. In both cases $\int_{\mathsf J_T}|N-\widehat F|^4\ge(\frac12\Lambda_T)^4d^5/5$, so $d^5\ll T(1+\log(1/c))^2/\log^4T\ll T$.

\emph{(d).} By (c), for $k\in\IT$ the interval $[\widehat x_k-d_k,\widehat x_k+d_k]$, $d_k=|\widehat x_k-\gamma_k|$, lies in $[T-2T^{1/2},2T+2T^{1/2}]$ for $T\ge T_0$, where the cutoff $\varphi$ of Lemma~\CGref{lem:sampling_rho} equals $1$. By \CGeqref{eq:regularized_gaps} and $\mathfrak b_T=2\pi/\log(3T)<2\pi/\log T$, every interval of length $\mathfrak b_T$ contains at most $3$ of the points $\widehat x_k$, so $\tilde n\le3$ and $\int_\R\tilde n^2\le3\int_\R\tilde n=3\mathfrak b_T\#\IT$ in Lemma~\CGref{lem:sampling_rho}, which with $r=1$ and $X\le T^{1/4}$ gives $\langle g(\widehat x_k)^4\rangle_{\IT}\ll(1+\log X)^4$ for $g=\mathcal M(\varphi S'_X)$. Since $|S_X(\gamma_k)-S_X(\widehat x_k)|\le2|\gamma_k-\widehat x_k|\,g(\widehat x_k)$, Cauchy--Schwarz and \CGeqref{eq:regularized_main} give
\[
\bigl\langle(S_X(\gamma_k)-S_X(\widehat x_k))^2\bigr\rangle_{\IT}\le4\bigl\langle|\gamma_k-\widehat x_k|^4\bigr\rangle_{\IT}^{1/2}\bigl\langle g(\widehat x_k)^4\bigr\rangle_{\IT}^{1/2}\ll(1+\log(1/c))\frac{(1+\log X)^2}{\log^2T},
\]
and $(1+\log X)/\log T\le(1+\frac1{\log2})c$ because $c\ge\log2/\log T$, while $c^2(1+\log(1/c))\le1$.
\end{proof}

\begin{remark}\label{rem:regularized}
(a) Compared with Theorem~\CGref{thm:uniform_iteration} and Corollary~\CGref{cor:sorted_clock}, Theorem~\CGref{thm:regularized_clock} reaches the scale of one mean spacing with a fixed cutoff and one step, in fourth mean, with increasing and separated points; the dependence on $c$ is explicit and parallel to Theorem~\CGref{thm:main}. Markov's inequality gives, for $\lambda>0$, $\#\{k\in\IT:|\widehat x_k-\gamma_k|>\lambda\cdot\frac{2\pi}{\log T}\}\le16C(1+\log(1/c))^2\lambda^{-4}\#\IT$. The constants $T_0$ and $C$ are not computed. (b) The cost is locality: $\widehat F$ is the solution of a convex program with $\mathsf M_T+1\asymp T\log T$ unknowns whose data are $S_X$ on the whole block $\mathsf J_T$, and it depends on the block; the points of Theorem~\CGref{thm:computable_clock} and of the iteration are explicit expressions index by index. A version on short overlapping windows is not treated here. (c) Part (d) bounds the transport from the regularized points, not from $\tau_k$: Question~\CGref{q:fixed_c} for the one-step clock $\tau_k^X$ remains open. (d) The slope constraints $[\frac12\Lambda_T,2\Lambda_T]$ enclose the main slope $\lL$ of the counting function on $\mathsf J_T$ and are fixed in advance; no zero is used to choose them, and the ordinates enter only in the proofs (through $P_N$ in Lemma~\CGref{lem:slope_envelope} and the heights $t_1$, $t_2$).
\end{remark}

"""
rep(r"""%======================================================================
\section{Theorem E: the pointwise envelope}""",
    NEW_SECTION + r"""%======================================================================
\section{Theorem E: the pointwise envelope}""")

# ================================================================ conclusions
rep(r"""\item \emph{Tails and order} (Theorem~\CGref{thm:tails}""",
    r"""\item \emph{A regularized clock with a fixed cutoff} (Theorem~\CGref{thm:regularized_clock}). The best $L^4$ approximation of $\NO+S_X$ by increasing piecewise linear functions with slopes in $[\frac{\log T}{4\pi},\frac{\log T}\pi]$ gives, in one step and with $X=T^c$, increasing points separated by at least $\pi/\log T$ with $\langle|\widehat x_k-\gamma_k|^4\rangle\ll(1+\log\frac1c)^2/\log^4T$; no ordinate enters the construction, which is global on the block $[\frac T2,3T]$.
\item \emph{Tails and order} (Theorem~\CGref{thm:tails}""")
rep(r"""\item \emph{LeClair's prime equation} (Theorems~\CGref{thm:main} and \CGref{thm:computable_clock}, Table~\CGref{tab:evaluates}). The equation for the $n$-th zero with the first $N$ primes \cite{LeClair2021} is the corrected clock equation; for $p_N\le T^{1/2}$ its mean-square defect""",
    r"""\item \emph{The corrected clock equation solved numerically} (Theorems~\CGref{thm:main}, \CGref{thm:computable_clock} and \CGref{thm:regularized_clock}, Table~\CGref{tab:evaluates}). The clock equation, which is the Riemann--von Mangoldt main term inverted by Lambert's function, corrected by the first $N$ primes was solved numerically in \cite{LeClair2021}, and with smoothed weights it is the equation of the zeros of Gonek's $\zeta_X$ \cite{Gonek2012}; for $p_N\le T^{1/2}$ its mean-square defect""")
rep(r"""and explicit Newton-type steps give points with proved mean-square error, where the accuracy of its numerical solutions was estimated from known zeros.""",
    r"""and explicit Newton-type steps, or one regularization with a fixed cutoff, give points with proved error, where the accuracy of its numerical solutions was estimated from known zeros.""")
rep(r"""\begin{question}\label{q:fixed_c}
Does $\langle r_k(T^c)^2\rangle_{\IT}$ stay bounded for fixed $c$,""",
    r"""\begin{question}\label{q:fixed_c}
For the regularized points of Theorem~\CGref{thm:regularized_clock} a fixed $c$ suffices. For the one-step clock $\tau_k^X$ from $\tau_k$: does $\langle r_k(T^c)^2\rangle_{\IT}$ stay bounded for fixed $c$,""")
rep(r"""Is the error of the corrected clock after $\log^*T+O(1)$ steps bounded in units of zeros for \emph{almost every} index, and not only in mean square?""",
    r"""Is the error of the corrected clock after $\log^*T+O(1)$ steps, or of $\widehat x_k$, bounded in units of zeros for \emph{almost every} index, and not only in mean? Can the regularization be localized to windows of bounded length in units of mean spacings with the same bound?""")

# ================================================================ bibliography
rep(r"""\bibitem{HasanalizadeShenWong2022}""",
    r"""\bibitem{Gonek2012}
S.M. Gonek, Finite Euler products and the Riemann hypothesis, Trans. Amer. Math. Soc. 364 (2012) 2157--2191, \href{https://doi.org/10.1090/S0002-9947-2011-05546-7}{https://doi.org/10.1090/S0002-9947-2011-05546-7}.

\bibitem{HasanalizadeShenWong2022}""")

TEX.write_text(head + sep + body)
print('v10 patch applied')
