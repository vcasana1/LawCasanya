"""Edits of paper I v4 (after the author's review of v3): sorted clock over the computable window, sorting at
intermediate levels justified, secondary references for the uniformity in k of Selberg's approximation,
certified enclosure of C_infty, quantifiers of the tail statements."""


def apply(ns):
    must_replace = ns['must_replace']
    theory = ns['theory']; envelope = ns['envelope']; external = ns['external']

    # ---- Lemma sorted: precise consequence.
    theory = must_replace(theory,
        r"Consequently, replacing $x^{(j)}_k$ by its sorted version at any level of \CGeqref{eq:newton_iteration} does not increase $\|e_j\|_{r,\IT}$ for any $r$, does not change the multiplicity function $\tilde n_j$, and leaves Theorems~\CGref{thm:second_step}, \CGref{thm:multiplicity_all} and \CGref{thm:uniform_iteration} and Corollary~\CGref{cor:clock_tails} unchanged; it removes the inversions $d_{j,k}\le0$ of Proposition~\CGref{prop:deformation}.",
        r"Consequently, if at some level $j$ the points $x^{(j)}_k$, $k\in I$, are replaced by their sorted version and the iteration \CGeqref{eq:newton_iteration} is continued from the sorted points, then $\|e_j\|_{r,I}$ does not increase for any $r$, the multiplicity function $\tilde n_j$ is unchanged, and the bounds of Proposition~\CGref{prop:recursion}, Lemma~\CGref{lem:sampling_rho}, Theorems~\CGref{thm:second_step}, \CGref{thm:multiplicity_all}, \CGref{thm:uniform_iteration} and Corollary~\CGref{cor:clock_tails} hold for the continued iteration with the same constants; the inversions $d_{j,k}\le0$ of Proposition~\CGref{prop:deformation} are removed.")
    theory = must_replace(theory,
        r"With $\varphi(t)=|t|^q$, each transposition of an inverted pair of $z$'s does not increase the sum, and finitely many transpositions sort $z$. The recursion \CGeqref{eq:recursion_norms} uses only $\|e_{j-1}\|_{4r}$ and the sampling of $\mathsf g_j$ on the point set $\{x^{(j-1)}_k\}$, both unchanged or improved.",
        r"With $\varphi(t)=|t|^q$, each transposition of an inverted pair of $z$'s does not increase the sum, and finitely many transpositions sort $z$. For the second statement: Proposition~\CGref{prop:recursion} holds for the Newton step from any points $x^{(j)}_k>2\pi$, and its bound \CGeqref{eq:recursion_norms} for the next level involves the level $j$ only through $\|e_j\|_{4r,I}$, which does not increase, and through $\|\mathsf g_{j+1}(x^{(j)})\|_{4r,I}$, a sum over the point set $\{x^{(j)}_k\}$, which is unchanged; Lemma~\CGref{lem:sampling_rho} depends on the point set only through $\tilde n_j$; the induction in the proof of Theorem~\CGref{thm:uniform_iteration} uses nothing else.")

    # ---- Corollary sorted clock: computable window.
    old = theory[theory.index(r"\begin{corollary}[An increasing computable clock]"):theory.index(r"\end{proof}", theory.index(r"\begin{corollary}[An increasing computable clock]")) + len(r"\end{proof}")]
    new = r"""\begin{corollary}[An increasing computable clock]\label{cor:sorted_clock}
Let $\mathcal I_T^\tau=\{k:T\le\tau_k<2T\}$, a set of consecutive indices defined by the clock alone, and let $x^\uparrow_k$, $k\in\mathcal I_T^\tau$, be the values $x^{(m^*)}_k$ of Theorem~\CGref{thm:uniform_iteration} in increasing order. Then $x^\uparrow_k\le x^\uparrow_{k+1}$, every $x^\uparrow_k$ is computed from the clock and the primes alone, and for $T\ge T_0$
\[
\frac1{\#\mathcal I_T^\tau}\sum_{k\in\mathcal I_T^\tau}\bigl(x^\uparrow_k-\gamma_k\bigr)^2\le\frac{C'+1}{\log^2T}.
\]
\end{corollary}

\begin{proof}
By Lemma~\CGref{lem:sorted} with $q=2$ on the index set $\mathcal I_T^\tau$, the sum is at most $\sum_{k\in\mathcal I_T^\tau}(x^{(m^*)}_k-\gamma_k)^2$. Since $|\delta_k|\le C_{10}$ for all $k$ (Theorem~\CGref{thm:known_basic}), the symmetric difference $\mathcal I_T^\tau\triangle\IT$ consists of indices with $|\gamma_k-T|\le C_{10}$ or $|\gamma_k-2T|\le C_{10}$, and has $O(\log T)$ elements by \CGeqref{eq:N_decomposition}. For every $k\in\mathcal I_T^\tau$ the points $x^{(j)}_k$ lie in $[T-2T^{1/2},2T+2T^{1/2}]$ and Lemma~\CGref{lem:second_identity} gives $|x^{(j)}_k-\tau_k|=|y^{(j)}_k|\le(\sigma_{X_j}+1)/\lL(\tau_k)\ll T^{1/320}/\log T$, because $X_j\le T^{1/160}$ for every $j\le m^*$ (proof of Theorem~\CGref{thm:uniform_iteration}, \emph{the two conditions}, with $r=1$) and $\sigma_X\ll\sqrt X/\log X$. Hence $|x^{(m^*)}_k-\gamma_k|\le C_{10}+O(T^{1/320}/\log T)$ for $k\in\mathcal I_T^\tau\triangle\IT$, these indices contribute $O(\log T\cdot T^{1/160}/\log^2T)=O(T^{1/160})$ to the sum, and \CGeqref{eq:final_clock} gives
\[
\sum_{k\in\mathcal I_T^\tau}\bigl(x^\uparrow_k-\gamma_k\bigr)^2\le\frac{C'\,\#\IT}{\log^2T}+O\bigl(T^{1/160}\bigr)\le\frac{(C'+1)\,\#\mathcal I_T^\tau}{\log^2T}
\]
for $T\ge T_0$, since $\#\mathcal I_T^\tau=\#\IT+O(\log T)$ and $\#\IT\asymp T\log T$.
\end{proof}"""
    theory = theory.replace(old, new)

    # ---- Quantifiers of the tails.
    theory = must_replace(theory,
        r"For fixed $j$ and $q$ the right side is $\ll_q\lambda^{-2q}\#\IT$ for $T\ge T_0(j,q)$, since $2^{m^*-j}\to\infty$: the $j$-th corrected clock misses its ordinate by more than $\lambda\sqrt{H_j}$ positions on a proportion of indices that decays faster than any power of $\lambda$.",
        r"For fixed $j$ and $q$ the right side is $\ll_q\lambda^{-2q}\#\IT$ for $T\ge T_0(j,q)$, since $2^{m^*-j}\to\infty$: for every fixed $q$, and $T$ large in terms of $q$, the $j$-th corrected clock misses its ordinate by more than $\lambda\sqrt{H_j}$ positions on a proportion $\ll_q\lambda^{-2q}$ of the indices. The orders available at a given $T$ are $q\le2^{m^*-j}$; nothing is claimed uniformly in $q$.")
    theory = must_replace(theory,
        r"The range \CGeqref{eq:tails_range} is the price of the moment order:",
        r"The bound \CGeqref{eq:tails} is for cutoffs that depend on $\lambda$; for a fixed cutoff exponent $c$ it applies only to $\lambda\le(C_8c)^{-2}$, and no exponential tail is claimed beyond that. The range \CGeqref{eq:tails_range} is the price of the moment order:")

    # ---- Secondary references for the uniformity in k.
    external = must_replace(external,
        r"For $k=2$ this is the form used in Section~\CGref{sec:main_theorem}; $k=4$, with $Y_4=T^{1/320}$, and the general $k$ are used in Section~\CGref{sec:iteration}.",
        r"For $k=2$ this is the form used in Section~\CGref{sec:main_theorem}; $k=4$, with $Y_4=T^{1/320}$, and the general $k$ are used in Section~\CGref{sec:iteration}. The uniformity in $k$ of Selberg's approximation is stated with explicit constants in other places: Korolev \cite[Lemma~4]{Korolev2012} proves $\sum_{N<n\le N+M}(S(t_n+0)+V_y(t_n+0))^{2k}\le(Ae^{-4}k)^{2k}M$ at the Gram points $t_n$, with $V_y(t)=\frac1\pi\sum_{p<y}p^{-1/2}\sin(t\log p)$, $y=x^{1/(4k)}$, $x=t_N^{0.1\varepsilon}$, uniformly for $1\le k\le\frac1{192}\log x$, and \cite[Thm.~2]{Korolev2012} bounds the $2k$-th moments of $S(t_n+0)-S(t_{n-1}+0)$ by $2Mk(4k\sqrt B)^{2k}$ in the same range; a $t$-mean version over short intervals is \cite[Lemma~3.13]{Korolev2016}, as quoted in \cite[Lemma~12]{IvicKorolev2018}; for $\log|\zeta(\frac12+it)|$ the bound $\ll A^kk^{4k}$, of the same shape $(Ck^2)^{2k}$, is \cite[Lemma~1]{Radziwill2011}, after Tsang \cite[p.~60]{Tsang1984}.")

    # ---- Theorem E: certified enclosure.
    envelope = must_replace(envelope,
        r"It gives $C_{30}=0.09681511427905377\ldots$ and $3\mathsf k_{30}\sqrt{1-\sigma_{30}}/(2\pi\log2)<5\cdot10^{-15}$, hence $C_\infty\in[C_{30}-5\cdot10^{-15},C_{30}]$ and \CGeqref{eq:envelope_value}; $C_7$ agrees with the $40$-digit quadrature of \texttt{opc\_envelope\_coefficient\_v14.py}.",
        r"It gives $C_{30}=0.09681511427905377\ldots$ and $3\mathsf k_{30}\sqrt{1-\sigma_{30}}/(2\pi\log2)<5\cdot10^{-15}$. The same quantities are enclosed by interval arithmetic with outward rounding at $60$ digits (\texttt{opc\_envelope\_certified\_p1.py}, with $\arcsin x=\operatorname{atan2}(x,\sqrt{1-x^2})$ on intervals): $C_{30}\in[0.09681511427905376,0.09681511427905377]$ and the bound for $C_{30}-C_\infty$ lies in $[4.58,4.59]\cdot10^{-15}$, hence" + "\n" + r"\begin{align*}C_\infty&\in[0.0968151142790491,\,0.0968151142790538],\\2\pi C_\infty&\in[0.6083073035510344,\,0.6083073035510633],\end{align*}" + "\n" + r"which is \CGeqref{eq:envelope_value}; $C_7$ agrees with the $40$-digit quadrature of \texttt{opc\_envelope\_coefficient\_v14.py}.")

    ns['theory'] = theory; ns['envelope'] = envelope; ns['external'] = external
