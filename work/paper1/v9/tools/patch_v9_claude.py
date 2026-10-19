#!/usr/bin/env python3
"""v9 = v8 + the six corrections of the external review of v8 + Theorem E with the convex hull
of published exponent pairs + the comparison with França--LeClair and LeClair read in the
originals + a table of what each approximation of the zeros evaluates.

Run on a copy of ../v8/manuscript/prime_corrected_clock_v8.tex saved as the v9 file name.
Every replacement must match exactly once.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
TEX = ROOT / 'manuscript' / 'prime_corrected_clock_v9.tex'
src = TEX.read_text()
head, sep, body = src.partition('\\begin{document}')
assert sep


def rep(old, new):
    global body
    n = body.count(old)
    if n != 1:
        sys.exit(f'expected 1 match, found {n}:\n{old[:300]}')
    body = body.replace(old, new)


# ---------------------------------------------------------------- abstract
rep(r"""(E) $\limsup_k|\tau_k-\gamma_k|=2\pi\limsup_t|S(t)|/\log t$, and Backlund's method with the exponent profile generated from Bourgain's exponent pair by van der Corput's process gives $\limsup_k|\tau_k-\gamma_k|\le0.6083074$, compared with $2\pi\cdot0.10076=0.6331\ldots$ from the explicit bound of Bellotti and Wong; the new envelope is asymptotic and is not an effective finite-height estimate. No zero of the Riemann zeta function is used in the construction of the corrected clocks.""",
    r"""(E) $\limsup_k|\tau_k-\gamma_k|=2\pi\limsup_t|S(t)|/\log t$, and Backlund's method with the convex hull of the exponent pairs of Bourgain and Heath-Brown and of their images under van der Corput's process gives $\limsup_t|S(t)|/\log t\le0.0966531$ and $\limsup_k|\tau_k-\gamma_k|\le0.6072889$ ($0.6060224$ with the exponent pairs of the preprints of Trudgian--Yang and Tao--Trudgian--Yang), compared with $2\pi\cdot0.10076=0.6331\ldots$ from the explicit bound of Bellotti and Wong; the new envelope is asymptotic and is not an effective finite-height estimate. The corrected clocks are computed from $k$, $\tau_k$ and the primes alone: their construction evaluates neither the Riemann zeta function nor any of its zeros, and the constant of (E) is obtained without evaluating the zeta function. The clock equation corrected by the primes $p\le X$ is, up to the term $1/(48t)$ of Stirling's series, the prime equation proposed by LeClair for the $n$-th zero, whose accuracy was estimated there numerically; (B) and (D) are proved statements about that equation at the true ordinates and about explicit corrected points.""")

# ---------------------------------------------------------------- intro: known results, LeClair
rep(r"""% SOURCECHECK: The former comparison with LeClair and França--LeClair is omitted: the specific original passages were not available for verification. No argument depends on that comparison.
\end{itemize}""",
    r"""\item Fran\c{c}a and LeClair \cite[(20), p.~11]{FrancaLeClair2015} write the condition $\vartheta(t_n)+\lim_{\delta\to0^+}\arg\zeta(\frac12+\delta+it_n)=(n-\frac32)\pi$, that is $\NO(t_n)+S(t_n)=n-\frac12$ up to the terms $O(1/t)$ of Stirling's series, as an equation for the $n$-th zero on the critical line, exact under the assumption that the limit exists for every $t$; its first approximation, without the argument, is solved by the Lambert formula \cite[(63), p.~24]{FrancaLeClair2015}, which is the clock \CGeqref{eq:intro_clock}. Their numerical solutions evaluate $\arg\zeta$ \cite[\S7.1, p.~28]{FrancaLeClair2015}. LeClair \cite[\S VI, (49), p.~18]{LeClair2021} replaces $\arg\zeta$ by the Euler phase of the first $N$ primes; the resulting equation no longer contains $\zeta$, and it is, up to the term $1/(48t)$ of Stirling's series, the corrected clock equation $\NO(t)+S_X(t)=n-\frac12$ of this paper with $X=p_N$. It is solved there by a root finder, adding one prime at a time from the Lambert value. Its accuracy is estimated numerically, by comparison with zeros computed by Odlyzko near $n=10^{21}$ and $n=10^{22}$ \cite[Table~I, p.~19]{LeClair2021}, and is argued from the claim $S(t)=O(1)$ \cite[Prop.~4, p.~12]{LeClair2021}, made under the assumption of \cite[Thm.~3]{LeClair2021}; that claim is incompatible with the normal law of $S(t)$ \cite{Selberg1946a,Tsang1984}, by which $S$ is unbounded. No error bound for the solutions of either equation is proved in \cite{FrancaLeClair2015,LeClair2021}. Theorem B below is a statement about LeClair's equation at the true ordinates, and Theorem D about explicit corrected points that replace its root finder (Table~\CGref{tab:evaluates}).
\end{itemize}""")

# ---------------------------------------------------------------- tab:antecedents: worst error row + LeClair row
rep(r"""& Proposition~\CGref{prop:envelope_equivalence} identifies the two limsups exactly. Theorem~\CGref{thm:envelope} evaluates the stated exponent-profile family, giving $2\pi C_\infty=0.6083073\ldots$. This comparison improves that cited asymptotic coefficient; it is not a new explicit bound valid at a given height, nor a claim to optimize over all known profiles.\\""",
    r"""& Proposition~\CGref{prop:envelope_equivalence} identifies the two limsups exactly. Theorem~\CGref{thm:envelope} evaluates the convex hull of the published exponent pairs of Bourgain and Heath-Brown, giving $2\pi C_{\mathcal P}<0.6072889$, and $0.6060224$ with the pairs of the preprints \cite{TrudgianYang2023,TaoTrudgianYang2025} (Remark~\CGref{rem:envelope_inputs}). This comparison improves that cited asymptotic coefficient; it is not a new explicit bound valid at a given height. No value of $\zeta$ is computed: the inputs are theorems on exponent pairs.\\
Prime equation for the $n$-th zero
& Fran\c{c}a--LeClair's equation with $\arg\zeta$ \cite[(20)]{FrancaLeClair2015} and LeClair's equation with the first $N$ primes \cite[(49)]{LeClair2021}, solved numerically; accuracy shown by comparison with known zeros \cite[Table~I]{LeClair2021}, without a proved error bound.
& LeClair's equation is the corrected clock equation with $X=p_N$, up to $1/(48t)$. Theorem~\CGref{thm:main} gives its mean-square defect at the true ordinates; with a fixed $N$ the defect grows like $(2\pi^2)^{-1}\log\log T$ and is bounded iff $\log p_N\asymp\log T$ (Corollary~\CGref{cor:dichotomy}). Theorems~\CGref{thm:computable_clock}--\CGref{thm:uniform_iteration} replace the root finder by explicit steps with proved mean-square error.\\""")

rep(r"""& No certified finite-height precision constant or individual-zero accuracy is obtained from the asymptotic $O$-terms here. No superiority at the available data heights is inferred from those terms.\\
\end{longtable}
\endgroup""",
    r"""& No certified finite-height precision constant or individual-zero accuracy is obtained from the asymptotic $O$-terms here. No superiority at the available data heights is inferred from those terms.\\
\end{longtable}
\endgroup

Table~\CGref{tab:evaluates} separates the approximations of the zeros by what has to be evaluated to produce the points. The proofs of Theorems B--E use theorems about $\zeta$ (Selberg's approximation, Fujii's moments, the Montgomery--Vaughan inequality, exponent pairs); what is free of $\zeta$ is the construction of the points, and the numbers of Theorem E, which come from exponent pairs and not from values of $\zeta$.

\begingroup
\footnotesize
\setlength{\tabcolsep}{4pt}
\renewcommand{\arraystretch}{1.13}
\begin{longtable}{@{}p{0.25\textwidth}p{0.33\textwidth}p{0.37\textwidth}@{}}
\caption{What each approximation of the zeros evaluates, and what is proved about its error.}\label{tab:evaluates}\\
\toprule
Approximation & Evaluated to produce the points & Error\\
\midrule
\endfirsthead
\multicolumn{3}{l}{\textit{Table \thetable\ continued}}\\
\toprule
Approximation & Evaluated to produce the points & Error\\
\midrule
\endhead
\bottomrule
\endfoot
Certified zero computations, e.g.\ \cite[\S2, p.~2]{PlattTrudgian2021}
& Values of the completed zeta function on the critical line in ball arithmetic; sign changes; Turing's method.
& Every zero up to the height reached is isolated rigorously.\\
Fran\c{c}a--LeClair, exact equation \cite[(20)]{FrancaLeClair2015}
& $\arg\zeta(\frac12+it)$, principal value \cite[\S7.1]{FrancaLeClair2015}; root finder.
& Exact under the assumption that $\lim_{\delta\to0^+}\arg\zeta(\frac12+\delta+it)$ exists for every $t$; accuracy shown numerically.\\
Lambert formula \cite[(63)]{FrancaLeClair2015} $=$ clock $\tau_k$
& Nothing: a closed expression in $k$.
& $\delta_k$ bounded; $\langle\delta_k^2\rangle\sim2\log\log T/\log^2T$ (Selberg, Korolev); $\limsup|\delta_k|$ is Theorem E.\\
LeClair, prime equation \cite[(49)]{LeClair2021}
& The first $N$ primes; root finder. No $\zeta$, no zero.
& Estimated numerically \cite[Table~I]{LeClair2021}; argued from $S(t)=O(1)$, which is false.\\
Theorems B--D (this paper)
& $k$, $\tau_k$ and the primes $p\le X(T)$; explicit Newton-type steps. No $\zeta$, no zero.
& Proved: defect at the ordinates (B), mean-square error in height, $O(1)$ mean spacings after $\log^*T+O(1)$ steps, tails (D).\\
Theorem E (this paper)
& Not a construction: a bound for $S(t)$ from exponent pairs. No value of $\zeta$ computed.
& Proved, asymptotic: $\limsup|\tau_k-\gamma_k|\le0.6072889$.\\
Bellotti--Wong \cite{BellottiWong2025}
& Not a construction: an explicit bound for $S(t)$.
& Proved for all $T\ge e$: $\limsup|\tau_k-\gamma_k|\le2\pi\cdot0.10076$.\\
\end{longtable}
\endgroup""")

# ---------------------------------------------------------------- intro: what this paper adds, E
rep(r"""Theorem E applies Backlund's method in the form of \cite{Trudgian2010,Trudgian2014,BellottiWong2025} to exponents of \cite{Bourgain2017,Ivic1985}.""",
    r"""Theorem E applies Backlund's method in the form of \cite{Trudgian2010,Trudgian2014,BellottiWong2025} to exponents of \cite{Bourgain2017,HeathBrown2017,Ivic1985}.""")

rep(r"""The profiles $\mathfrak e_J$ generated from Bourgain's exponent pair by $J$ applications of van der Corput's $\mathscr A$-process give a decreasing sequence of bounds with limit $C_\infty=0.0968151142790\ldots$, so $\limsup_k|\tau_k-\gamma_k|\le2\pi C_\infty=0.6083073\ldots$ and $\limsup_t|S(t)|/\log t\le0.09681512$, compared with $0.10076$ in \cite{BellottiWong2025} and $0.1013$ in \cite{Trudgian2010} (Remark~\CGref{rem:envelope_inputs}). This is an asymptotic bound and does not replace the explicit bounds of \cite{BellottiWong2025}, valid for all $T\ge e$.""",
    r"""The lower convex hull of the exponent pairs of Bourgain \cite{Bourgain2017} and Heath-Brown \cite{HeathBrown2017} and of their images under van der Corput's $\mathscr A$-process gives $C_{\mathcal P}=0.0966530245541\ldots$, so $\limsup_t|S(t)|/\log t\le0.0966531$ and $\limsup_k|\tau_k-\gamma_k|\le2\pi C_{\mathcal P}<0.6072889$, compared with $0.10076$ in \cite{BellottiWong2025} and $0.1013$ in \cite{Trudgian2010}; with the exponent pairs of the preprints \cite{TrudgianYang2023,TaoTrudgianYang2025} the bound is $0.6060224$ (Remark~\CGref{rem:envelope_inputs}). This is an asymptotic bound and does not replace the explicit bounds of \cite{BellottiWong2025}, valid for all $T\ge e$. With one Backlund disc no exponent profile gives less than $0.4940$ (the Lindel\"of profile), although on the Lindel\"of hypothesis $S(t)=o(\log t)$.""")

# ---------------------------------------------------------------- degree of proof: programs
rep(r"""computed in closed form by the two programs named in the Data availability statement;""",
    r"""computed in closed form and in interval arithmetic by the programs named in the Data availability statement;""")

# ---------------------------------------------------------------- tab:status: column
rep(r"""\begin{longtable}{p{0.40\textwidth}p{0.17\textwidth}p{0.35\textwidth}}
\caption{Main results: degree of proof and role.}\label{tab:status}\\
\toprule
result & status & role\\
\midrule
\endfirsthead
\toprule
result & status & role\\
\midrule
\endhead""",
    r"""\begin{longtable}{p{0.31\textwidth}p{0.14\textwidth}p{0.29\textwidth}p{0.13\textwidth}}
\caption{Main results: degree of proof, role, and whether $\zeta$ or its zeros are evaluated.}\label{tab:status}\\
\toprule
result & status & role & evaluates $\zeta$ or zeros\\
\midrule
\endfirsthead
\toprule
result & status & role & evaluates $\zeta$ or zeros\\
\midrule
\endhead""")
for old, new in [
    (r"""(A) & unconditional & statistics of the errors at the zeros as $t$-integrals\\""",
     r"""(A) & unconditional & statistics of the errors at the zeros as $t$-integrals & no\\"""),
    (r"""(B) & unconditional & bounded error in units of zeros iff $\log X\asymp\log T$\\""",
     r"""(B) & unconditional & bounded error in units of zeros iff $\log X\asymp\log T$ & no (primes $p\le X$)\\"""),
    (r"""(C) & unconditional, exact & finite-height balance of the gain of one correction\\""",
     r"""(C) & unconditional, exact & finite-height balance of the gain of one correction & no\\"""),
    (r"""(D) & unconditional & zero-free corrected points with mean-square error $O(1)$ mean spacings\\""",
     r"""(D) & unconditional & zero-free corrected points with mean-square error $O(1)$ mean spacings & no ($k$, $\tau_k$, primes)\\"""),
    (r"""& unconditional & tails of the defect and of the corrected clocks; a nondecreasing clock built without ordinates\\""",
     r"""& unconditional & tails of the defect and of the corrected clocks; a nondecreasing clock built without ordinates & no\\"""),
    (r"""(E) & unconditional, asymptotic & the worst error of the clock is the extreme size of $S(t)$\\""",
     r"""(E) & unconditional, asymptotic & the worst error of the clock is the extreme size of $S(t)$ & no (exponent pairs)\\"""),
    (r"""& open & what remains to be proved\\""",
     r"""& open & what remains to be proved & --\\"""),
]:
    rep(old, new)

# ---------------------------------------------------------------- known exponents: Heath-Brown
rep(r"""\begin{theorem}[{\cite[Lemma~2.8 and (7.57)]{Ivic1985}}; Bourgain {\cite[\S5, Thm.~6]{Bourgain2017}}]\label{thm:known_exponents}""",
    r"""\begin{theorem}[{\cite[Lemma~2.8 and (7.57)]{Ivic1985}}; Bourgain {\cite[\S5, Thm.~6]{Bourgain2017}}; Heath-Brown {\cite[Thm.~2]{HeathBrown2017}}]\label{thm:known_exponents}""")
rep(r"""(c) For every $\varepsilon>0$, $(\frac{13}{84}+\varepsilon,\frac{55}{84}+\varepsilon)$ is an exponent pair.
\end{theorem}""",
    r"""(c) For every $\varepsilon>0$, $(\frac{13}{84}+\varepsilon,\frac{55}{84}+\varepsilon)$ is an exponent pair. (d) For every integer $m\ge3$ and every $\varepsilon>0$, $\bigl(\frac2{(m-1)^2(m+2)},1-\frac{3m-2}{m(m-1)(m+2)}+\varepsilon\bigr)$ is an exponent pair.
\end{theorem}""")

# ---------------------------------------------------------------- review 1: sampling constant
rep(r"""Since $b\cdot4r(1+\log X)\le8\pi r\,c\,(1+o(1))\le7$ for $c=\log X/\log T\le1/(4r)$, we get $\sum_kF(\mathsf x_k)\le8\,b^{-1}""",
    r"""Since $\log X\ge\log2$ and $r\log X\le\frac14\log T$, uniformly in $r$ and $X$, $b\cdot4r(1+\log X)=\frac{8\pi r(1+\log X)}{\log(3T)}\le8\pi\bigl(1+\frac1{\log2}\bigr)\frac{r\log X}{\log(3T)}\le2\pi\bigl(1+\frac1{\log2}\bigr)\frac{\log T}{\log(3T)}<16$, and we get $\sum_kF(\mathsf x_k)\le17\,b^{-1}""")

# ---------------------------------------------------------------- review 2: higher moments
rep(r"""The terms $m=2$ and $m\ge3$ are $O(T^{1/4r})$ in the same norm (products of $2r$ squares of primes, $\sum|\eta'_n|^2\le(2r)!\,(\sum_pp^{-2})^{2r}\le(2r)!$, and a bounded function).""",
    r"""The term $m=2$ is at most $C\sqrt r\,T^{1/4r}$ in the same norm (products of $2r$ squares of primes, $\sum|\eta'_n|^2\le(2r)!\,(\sum_pp^{-2})^{2r}\le(2r)!$, and $((2r)!)^{1/4r}\le\sqrt{2r}$), and the terms $m\ge3$ form a bounded function, $O(T^{1/4r})$ in that norm; the factor $\sqrt r$ is absorbed by $Cr^2$.""")

# ---------------------------------------------------------------- review 3: zero pairs
rep(r"""Since only $l\in\IT$ are counted, $n_{\mathsf R}(\gamma_k)$ is at most the number of ordinates in an interval of length $h=\min(2\mathsf R b,T)$ contained in $[T-1,2T]$, which is $\le Ch\log T\le C'\mathsf R$ (for $h=T$ use $T\log T\le2\mathsf R b\log T\le4\pi\mathsf R$); both bounds follow.""",
    r"""Only $l\in\IT$ are counted. If $2\mathsf Rb\ge T$, then $n_{\mathsf R}(\gamma_k)\le\#\IT\le CT\log T\le2C\mathsf Rb\log T\le4\pi C\mathsf R$. Otherwise $h=\max(1,2\mathsf Rb)$ satisfies $1\le h\le T$ and, since $4\mathsf Rb>1$, $h\le4\mathsf Rb$; the ordinates counted by $n_{\mathsf R}(\gamma_k)$ lie in an interval of length $h$ contained in $[T-1,2T]$, so $n_{\mathsf R}(\gamma_k)\le Ch\log T\le4C\mathsf Rb\log T\le8\pi C\mathsf R$. Both bounds follow.""")

# ---------------------------------------------------------------- review 4: deformation
rep(r"""the last term is $\ll T^{c_1-1}$, negligible against $d_{0,k}\asymp1/\log T$, and $\nabla_k(1/\lL(\tau))\ll1/(T\log^3T)$ is negligible too, so it suffices""",
    r"""by Lemma~\CGref{lem:second_identity} with $j=2$ the last term is $\ll T^{c_2-1}/\log T$, and $\nabla_k(1/\lL(\tau))\ll1/(T\log^3T)$; divided by $d_{0,k}\asymp1/\log T$, these terms and the term $O(T^{c_1/2-1})$ below contribute $O(T^{-1/2}\log^3T)$ to the $\ell^4(\IT)$ norm of $(d_2-d_0)/d_0$, since $c_1,c_2\le\frac12$ and $\sigma_{X_2}\ll T^{c_2/2}$, so it suffices""")
rep(r"""\Bigl\|\frac{\nabla S_{X_2}(x^{(1)})}{d_0\,\lL(\tau)}\Bigr\|_{4,\IT}\ll\Bigl\|\frac{\mathsf g_2(x^{(1)})}{\log T}\Bigr\|_{4,\IT}+\Bigl\|\frac{\mathsf g_2(x^{(1)})}{\log T}\Bigr\|_{8,\IT}\Bigl\|\frac{\mathsf g_1(\tau)}{\log T}\Bigr\|_{8,\IT}+o(1).""",
    r"""\Bigl\|\frac{\nabla S_{X_2}(x^{(1)})}{d_0\,\lL(\tau)}\Bigr\|_{4,\IT}\ll\Bigl\|\frac{\mathsf g_2(x^{(1)})}{\log T}\Bigr\|_{4,\IT}+\Bigl\|\frac{\mathsf g_2(x^{(1)})}{\log T}\Bigr\|_{8,\IT}\Bigl\|\frac{\mathsf g_1(\tau)}{\log T}\Bigr\|_{8,\IT}+O\bigl(T^{-1/2}\log^3T\bigr).""")
rep(r"""the result is $\|\mathsf g_2(x^{(1)})/\log T\|_8\ll c_2$. The first inequality of \CGeqref{eq:deformation} follows,""",
    r"""the result is $\|\mathsf g_2(x^{(1)})/\log T\|_8\ll c_2$. Hence
\[
\Bigl\|\frac{d_2-d_0}{d_0}\Bigr\|_{4,\IT}\ll c_2+c_1c_2+T^{-1/2}\log^3T\ll c_2,
\]
because $c_2=H_1^{-1/2}\gg T^{-1/2}\log^3T$; the first inequality of \CGeqref{eq:deformation} follows,""")

# ---------------------------------------------------------------- review 5: domain of the sorted clock
rep(r"""The points $x^{(m^*)}_k$ of Theorem~\CGref{thm:uniform_iteration} are defined by \CGeqref{eq:newton_iteration} for every index $k$ with $\tau_k\ge T_0$, in particular for $k\in\mathcal I_T^\tau$;""",
    r"""For each $T$, with the cutoffs and the number of steps chosen at height $T$, the points $x^{(m^*)}_k$ of Theorem~\CGref{thm:uniform_iteration} are defined by \CGeqref{eq:newton_iteration} on the block $\mathcal J_T=\{k:T/2\le\tau_k\le3T\}$, which contains $\IT\cup\mathcal I_T^\tau$ for $T\ge T_0$;""")
rep(r"""Theorem~\CGref{thm:uniform_iteration} is a statement over $\IT$; for the indices of $\mathcal I_T^\tau\setminus\IT$ only the localization of the points proved below is used.""",
    r"""Theorem~\CGref{thm:uniform_iteration} is a statement over $\IT$; for the indices of $\mathcal I_T^\tau\setminus\IT$ only the localization of the points proved below is used, and it is applied on $\mathcal J_T$, while the mean estimates are kept on their original index sets. The output for $k\in\mathcal I_T^\tau$ does not depend on this choice of block.""")

# ---------------------------------------------------------------- review 6: fixed cutoff sentence
rep(r"""A bounded error in units of zeros with a \emph{fixed} final cutoff $T^{c_0}$ is not obtained by this method: for a fixed cutoff exponent the error in units of zeros is bounded in mean square if and only if the transport is (Remark~\CGref{rem:newton}), and the only available bound for the transport, Lemma~\CGref{lem:transport}, grows like $c^2\log\log T$.""",
    r"""For the one-step clock with a fixed cutoff exponent $c$, bounded mean-square error in units of zeros is equivalent to bounded mean-square transport, $\|r(T^c)\|_{2,\IT}=O_c(1)$ if and only if $\|\mathfrak t(T^c)\|_{2,\IT}=O_c(1)$ (Remark~\CGref{rem:newton}). The available transport estimate, Lemma~\CGref{lem:transport}, does not establish this boundedness. This limitation concerns the one-step construction; it does not establish a corresponding obstruction for the final cutoff of the iterated construction.""")

# ---------------------------------------------------------------- Theorem E statement
rep(r"""for comparison $C_0=0.1010228\ldots$ (the exponent $\frac{13}{84}$ alone) and $C_7=0.0968160\ldots$.
\end{theorem}""",
    r"""for comparison $C_0=0.1010228\ldots$ (the exponent $\frac{13}{84}$ alone) and $C_7=0.0968160\ldots$.
Let $\mathcal P$ be the set of pairs consisting of $(\frac{13}{84},\frac{55}{84})$, of $(\mathsf p_m,\mathsf q_m)=\bigl(\frac2{(m-1)^2(m+2)},1-\frac{3m-2}{m(m-1)(m+2)}\bigr)$ for $3\le m\le3000$, and of their images $\mathscr A^j$, $1\le j\le25$, and let $\mathfrak e_{\mathcal P}$ be the lower convex hull on $[\frac12,1]$ of the points $(\mathsf l-\mathsf k,\mathsf k)$, $(\mathsf k,\mathsf l)\in\mathcal P$, and $(1,0)$. Let $C_{\mathcal P}$ be the right side of \CGeqref{eq:envelope_formula} for $\mathfrak e=\mathfrak e_{\mathcal P}$. Then $\mathfrak a\le C_{\mathcal P}$ and
\begin{equation}
C_{\mathcal P}=0.0966530245541\ldots,\qquad\limsup_{k\to\infty}|\tau_k-\gamma_k|\le2\pi C_{\mathcal P}=0.6072888637\ldots<0.6072889 .
\label{eq:envelope_value_hull}
\end{equation}
\end{theorem}""")

# ---------------------------------------------------------------- Theorem E proof: hull profile and its values
rep(r"""Multiply by $2\pi$ and use Proposition~\CGref{prop:envelope_equivalence}(a).
\end{proof}

\begin{remark}\label{rem:envelope_inputs}""",
    r"""Multiply by $2\pi$ and use Proposition~\CGref{prop:envelope_equivalence}(a).

\emph{The hull profile.} Let $\varepsilon'>0$ and replace each $(\mathsf k,\mathsf l)\in\mathcal P$ by the exponent pair given by Theorem~\CGref{thm:known_exponents}(a),(c),(d) with $\varepsilon'$ added to $\mathsf k$ and $\mathsf l$ for Bourgain's pair and to $\mathsf q_m$ for Heath-Brown's, before applying $\mathscr A^j$. Every point satisfies $\mathsf l-\mathsf k\ge\frac12$ (for $m\ge3$, $\mathsf q_m-\mathsf p_m\ge\frac23$, and $\mathscr A$ maps $\mathsf l-\mathsf k\ge\frac12$ to $\frac12+(\mathsf l-\mathsf k)/(2\mathsf k+2)\ge\frac12$), so Theorem~\CGref{thm:known_exponents}(b) gives $|\zeta(\mathsf l-\mathsf k+it)|\ll|t|^{\mathsf k}\log|t|$. The leftmost point is Bourgain's, at $\sigma=\frac12$, and the hull ends at $(1,0)$; a convex function on $[\frac12,1]$ that is positive before $1$ and vanishes at $1$ is decreasing, so consecutive vertices have decreasing ordinates and Theorem~\CGref{thm:known_PL} between them gives the hypothesis of the theorem for $\mathfrak e_{\mathcal P}$. The right side of \CGeqref{eq:envelope_formula} depends continuously on $\varepsilon'$, so $\mathfrak a\le C_{\mathcal P}$. The vertices are rational; the program \texttt{envelope\_best\_profile\_v9.py} (Data availability) evaluates $C_{\mathcal P}$ from the primitive above in interval arithmetic at $50$ digits and returns an interval of width below $10^{-25}$ around the value \CGeqref{eq:envelope_value_hull}. Every finite subset of the pairs of Theorem~\CGref{thm:known_exponents} gives an admissible profile; the truncation $m\le3000$, $j\le25$ is only a choice of finite set.
\end{proof}

\begin{remark}\label{rem:envelope_inputs}""")

# ---------------------------------------------------------------- Remark: inputs, preprints, the disc and Lindelöf
rep(r"""(b) Profiles of the growth exponent of $\zeta(\sigma+it)$ below $\mathfrak e_J$ are known: Trudgian and Yang \cite{TrudgianYang2023} close a convex hull of known exponent pairs, Bourgain\textquoteright s among them, under van der Corput\textquoteright s $\mathscr A$- and $\mathscr B$-processes and the $\mathscr C$-process and deduce piecewise bounds for that exponent on $[\frac12,1]$. Any such profile can be inserted in \CGeqref{eq:envelope_formula}; we do not evaluate it here. (c) For the Lindel\"of profile ($\mathfrak e=0$ on $[\frac12,1]$) the right side is $0.07863$: Backlund\textquoteright s method with a disc cannot give less, whatever the exponents.""",
    r"""(b) The hull $\mathfrak e_{\mathcal P}$ uses only published exponent pairs. Trudgian and Yang \cite[Lemma~1.1]{TrudgianYang2023} give four further pairs, $(\frac{4742}{38463},\frac{35731}{51284})$, $(\frac{18}{199},\frac{593}{796})$, $(\frac{2779}{38033},\frac{58699}{76066})$, $(\frac{715}{10238},\frac{7955}{10238})$; with them and their $\mathscr A$-images added to $\mathcal P$ the same program gives $2\pi C<0.6061342$. Tao, Trudgian and Yang \cite{TaoTrudgianYang2025} give $(\frac{89}{1282},\frac{997}{1282})$, $(\frac{652397}{9713986},\frac{7599781}{9713986})$, $(\frac{10769}{351096},\frac{609317}{702192})$, $(\frac{89}{3478},\frac{15327}{17390})$; adding them gives $2\pi C<0.6060224$. Both are preprints, so these values are not stated in Theorem~\CGref{thm:envelope}. The bound $\zeta(\sigma+it)\ll t^{\kappa(1-\sigma)^{3/2}+\varepsilon}$, $\kappa=\frac8{63}\sqrt{15}$, of \cite[Thm.~5]{HeathBrown2017} lies above $\mathfrak e_{\mathcal P}$ and changes nothing. The $\mathscr B$-process maps the points with $\mathsf l-\mathsf k\ge\frac12$ to $\sigma\le\frac12$, where the profile is fixed by the functional equation, and adding the $\mathscr A$-images of these $\mathscr B$-images ($j\le10$, $m\le300$) did not lower the value in our computation. (c) For the Lindel\"of profile ($\mathfrak e=0$ on $[\frac12,1]$) the right side is $0.0786253$, that is $2\pi\cdot0.0786253=0.4940172$ for the clock: with one disc of Theorem~\CGref{thm:known_backlund} no exponent profile gives less. A numerical scan of the admissible discs, $1<\sigma_\circ<\varrho$ with $\varrho/(\sigma_\circ-\frac12)$ free, finds the infimum at the corner $\sigma_\circ\to1$, $\varrho\to1$ used in the proof, for each of the profiles above (program \texttt{envelope\_disc\_scan\_v9.py}). This is a limit of the one-disc method, not of $\mathfrak a$: on the Lindel\"of hypothesis $S(t)=o(\log t)$ \cite[Thm.~13.6(A), p.~333]{Titchmarsh1986}, that is $\mathfrak a=0$, by an argument that also uses the zeros near $\frac12+it$.""")

# ---------------------------------------------------------------- conclusions item 6
rep(r"""and Backlund's method with the profiles generated from Bourgain's exponent pair gives $\limsup|\tau_k-\gamma_k|\le2\pi C_\infty=0.6083073\ldots$.""",
    r"""and Backlund's method with the convex hull of the published exponent pairs of Bourgain and Heath-Brown gives $\limsup|\tau_k-\gamma_k|\le2\pi C_{\mathcal P}<0.6072889$ ($0.6060224$ with the pairs of the preprints \cite{TrudgianYang2023,TaoTrudgianYang2025}), with no evaluation of $\zeta$; one Backlund disc cannot go below $0.4940$.
\item \emph{LeClair's prime equation} (Theorems~\CGref{thm:main} and \CGref{thm:computable_clock}, Table~\CGref{tab:evaluates}). The equation for the $n$-th zero with the first $N$ primes \cite{LeClair2021} is the corrected clock equation; its mean-square defect at the true ordinates is $\frac1{2\pi^2}\log\frac{\log T}{\log p_N}+O(1+\sqrt{\log(\log T/\log p_N)})$, unbounded for a fixed number of primes, and explicit Newton-type steps give points with proved mean-square error, where the accuracy of its numerical solutions was estimated from known zeros.""")

# ---------------------------------------------------------------- data availability
rep(r"""its output \texttt{envelope\_\allowbreak intervals\_\allowbreak v5.json} confirms the upper bound $2\pi C_\infty<0.6083074$.""",
    r"""its output \texttt{envelope\_\allowbreak intervals\_\allowbreak v5.json} confirms the upper bound $2\pi C_\infty<0.6083074$. The program \texttt{envelope\_\allowbreak best\_\allowbreak profile\_\allowbreak v9.py} builds the lower convex hulls of Theorem~\CGref{thm:envelope} and Remark~\CGref{rem:envelope_inputs} with exact rational arithmetic and evaluates the integral \CGeqref{eq:envelope_formula} in interval arithmetic at $50$ digits (output \texttt{envelope\_\allowbreak best\_\allowbreak profile\_\allowbreak v9.txt}); \texttt{envelope\_\allowbreak disc\_\allowbreak scan\_\allowbreak v9.py} scans the Backlund disc in floating point (output \texttt{envelope\_\allowbreak disc\_\allowbreak scan\_\allowbreak v9.txt}).""")

# ---------------------------------------------------------------- bibliography
rep(r"""\bibitem{Fujii1974}""",
    r"""\bibitem{FrancaLeClair2015}
G. Fran\c{c}a, A. LeClair, Transcendental equations satisfied by the individual zeros of Riemann $\zeta$, Dirichlet and modular $L$-functions, Commun. Number Theory Phys. 9 (1) (2015) 1--50, \href{https://doi.org/10.4310/CNTP.2015.v9.n1.a1}{https://doi.org/10.4310/CNTP.2015.v9.n1.a1}.

\bibitem{Fujii1974}""")
rep(r"""\bibitem{Hunt1968}""",
    r"""\bibitem{HeathBrown2017}
D.R. Heath-Brown, A new $k$th derivative estimate for exponential sums via Vinogradov's mean value, Proc. Steklov Inst. Math. 296 (2017) 88--103, \href{https://doi.org/10.1134/S0081543817010072}{https://doi.org/10.1134/S0081543817010072}.

\bibitem{Hunt1968}""")
rep(r"""\bibitem{DiPlinioLerner2014}""",
    r"""\bibitem{LeClair2021}
A. LeClair, Riemann hypothesis and random walks: the zeta case, Symmetry 13 (11) (2021) 2014 (section, equation, table and page numbers cited from arXiv:1601.00914v1), \href{https://doi.org/10.3390/sym13112014}{https://doi.org/10.3390/sym13112014}.

\bibitem{DiPlinioLerner2014}""")
rep(r"""\bibitem{Selberg1946a}""",
    r"""\bibitem{PlattTrudgian2021}
D. Platt, T. Trudgian, The Riemann hypothesis is true up to $3\cdot10^{12}$, Bull. Lond. Math. Soc. 53 (3) (2021) 792--797, \href{https://doi.org/10.1112/blms.12460}{https://doi.org/10.1112/blms.12460}.

\bibitem{Selberg1946a}""")
rep(r"""\bibitem{Tenenbaum2015}""",
    r"""\bibitem{TaoTrudgianYang2025}
T. Tao, T. Trudgian, A. Yang, New exponent pairs, zero density estimates, and zero additive energy estimates: a systematic approach, preprint, arXiv:2501.16779 (2025), \href{https://doi.org/10.48550/arXiv.2501.16779}{https://doi.org/10.48550/arXiv.2501.16779}.

\bibitem{Tenenbaum2015}""")

TEX.write_text(head + sep + body)
print('v9 patch applied')
