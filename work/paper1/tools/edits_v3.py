"""Edits of paper I v3 applied by assemble_p1.py: the higher-moments lemma without a range condition on r,
exponential tails of the ordinal defect, tails of the corrected clocks, the sorted (increasing) clock,
and Theorem E with the limit constant C_infty.  Imported by assemble_p1.py; operates on the strings
theory, envelope, external through apply(ns)."""
import re


def apply(ns):
    must_replace = ns['must_replace']; sub_block = ns['sub_block']
    theory = ns['theory']; envelope = ns['envelope']; external = ns['external']

    # ---- Lemma on higher moments: boundary term bounded for every admissible r (two cases).
    theory = must_replace(theory,
        r"There is an absolute constant $C$ such that for every integer $r\ge1$, every $T\ge T_0$ with $T^{1/(160r)}\ge2$ and $r\le\log T/(4\log(2\log T))$, and every $2\le X\le T^{1/(160r)}$,",
        r"There is an absolute constant $C$ such that for every integer $r\ge1$, every $T\ge T_0$ with $T^{1/(160r)}\ge2$ and every $2\le X\le T^{1/(160r)}$,")
    theory = must_replace(theory,
        r" For $r\le\log T/(4\log(2\log T))$ and $T\ge4$ one has $4^rT^{1/100}\le T$ and $(2\log T)^{2r+1}\le T\log T$, so this term is at most $2C_{\rm b}T\log T\le9\pi C_{\rm b}\,\#\IT$ for $T\ge T_0$: it contributes an absolute constant to the mean.",
        r" Since $r\le\log T/(160\log2)$, $4^rT^{1/100}\le T^{1/80+1/100}\le T^{1/2}$. For $(2\log T)^{2r+1}$ there are two cases: if $r\ge\sqrt{2\log T/C}$ then $2\log T\le Cr^2$ and $(2\log T)^{2r+1}\le(Cr^2)^{2r}\,2\log T\le(Cr^2)^{2r}\,T\log T$; if $r<\sqrt{2\log T/C}$ then $(2\log T)^{2r+1}\le\exp\bigl(3\sqrt{2\log T/C}\,\log(2\log T)\bigr)\le T^{1/2}$ for $T\ge T_0$. In both cases the boundary term is at most $C_{\rm b}(Cr^2)^{2r}(T^{1/2}+T\log T)\le9\pi C_{\rm b}(Cr^2)^{2r}\,\#\IT$ for $T\ge T_0$.")
    theory = must_replace(theory,
        r"\langle u_k(X)^{2r}\rangle_{\IT}\le(4+4\pi C_{\rm d})T^{-1/2}\mathcal E_{4r}^{1/2}+9\pi C_{\rm b}+1$, and the first bound gives the second ($C\ge1$ absorbs the constant, as $(Cr^2)^{2r}\ge C^2$).",
        r"\langle u_k(X)^{2r}\rangle_{\IT}\le(4+4\pi C_{\rm d})T^{-1/2}\mathcal E_{4r}^{1/2}+(9\pi C_{\rm b}+1)(Cr^2)^{2r}$, and the first bound gives the second with $(9\pi C_{\rm b}+2)C$ in place of $C$, since $(9\pi C_{\rm b}+2)^{2r}\ge9\pi C_{\rm b}+2$.")
    theory = must_replace(theory,
        r"with absolute $C,C_5$, provided $X_j\le T^{1/(160r)}$ and $r\le\log T/(4\log(2\log T))$ (the range of Lemma~\CGref{lem:higher_moments}).",
        r"with absolute $C,C_5$, provided $X_j\le T^{1/(160r)}$.")
    theory = must_replace(theory,
        r" The condition $r\le\log T/(4\log(2\log T))$ holds for all $r\le2^{m^*}$ and $T\ge T_0$, since $m^*=\log^*T+O(1)$ gives $2^{m^*}\ll2^{\log\log\log T}=(\log\log T)^{\log2}$. So \CGeqref{eq:induction_claim} holds",
        r" So \CGeqref{eq:induction_claim} holds")

    # ---- Exponential tails of the ordinal defect (new theorem), after the remark that follows the lemma.
    anchor = r"for fixed $r$ the three bounds read $\ll_rT(1+V)^{2r}$, $\ll_r(1+V)^r$ and $\ll_rT(1+\log X)^{4r\nu}$."
    tails = anchor + r"""

The moments of all orders give a tail bound for the defect that no second-moment argument can give: the proportion of zeros whose corrected index is off by more than $\lambda$ positions decays exponentially in $\sqrt\lambda$, provided the cutoff is chosen in a range that depends on $\lambda$.

\begin{theorem}[Exponential tails of the ordinal defect]\label{thm:tails}
There are absolute constants $C_8\ge1$, $\lambda_0$ and $T_0$ such that, for $T\ge T_0$, every $\lambda\ge\lambda_0$ and every $X=T^c\ge2$ with
\begin{equation}
\exp\bigl(-(\lambda/C_8)^{3/2}\bigr)\le c\le\frac1{C_8\sqrt\lambda},
\label{eq:tails_range}
\end{equation}
\begin{equation}
\#\{k\in\IT:|u_k(X)|>\lambda\}\le2^{\,2-\sqrt{\lambda/C_8}}\;\#\IT .
\label{eq:tails}
\end{equation}
\end{theorem}

\begin{proof}
Let $C$ be the constant of Lemma~\CGref{lem:higher_moments} and $r=\lfloor\sqrt{\lambda/(4C)}\rfloor$, so $r\ge1$ for $\lambda\ge4C$ and $Cr^2\le\lambda/4$. The lemma applies: $X\le T^{1/(160r)}$ because $c\le1/(C_8\sqrt\lambda)\le1/(160r)$ once $C_8\ge80$, since $160r\le160\sqrt{\lambda/(4C)}\le80\sqrt\lambda$; and $T^{1/(160r)}\ge X\ge2$. With $Y_{2r}=T^{1/(160r)}\ge X$, Lemma~\CGref{lem:V_size} gives $V=\log(1/(160rc))+O(1)\le\log(1/c)+C_9\le(\lambda/C_8)^{3/2}+C_9$ by \CGeqref{eq:tails_range}, so $1+V\le2(\lambda/C_8)^{3/2}$ for $\lambda\ge C_8(C_9+1)^{2/3}$. Then $r(1+V)\le\sqrt{\lambda/(4C)}\cdot2\lambda^{3/2}C_8^{-3/2}=\lambda^2/(\sqrt C\,C_8^{3/2})$ and $C\sqrt{r(1+V)}\le C^{3/4}C_8^{-3/4}\lambda\le\lambda/4$ once $C_8\ge7C$. Hence $C(r^2+\sqrt{r(1+V)})\le\lambda/2$, and Chebyshev's inequality with the second bound of the lemma gives
\[
\#\{k\in\IT:|u_k(X)|>\lambda\}\le\lambda^{-2r}\sum_{k\in\IT}u_k(X)^{2r}\le2^{-2r}\,\#\IT\le2^{\,2-\sqrt{\lambda/C}}\,\#\IT ,
\]
since $2r\ge2\sqrt{\lambda/(4C)}-2$. Take $C_8=\max(80,7C)$ and $\lambda_0=C_8(C_9+1)^{2/3}$; then $\lambda\ge\lambda_0\ge4C$, and $2^{-\sqrt{\lambda/C}}\le2^{-\sqrt{\lambda/C_8}}$.
\end{proof}

For the cutoff $X=T^{1/(C_8\sqrt\lambda)}$, Theorem~\CGref{thm:main} gives $\langle u_k(X)^2\rangle_{\IT}=\frac1{4\pi^2}\log\lambda+O(\sqrt{\log\lambda})$, so Chebyshev's inequality alone bounds the proportion in \CGeqref{eq:tails} by $\lambda^{-2}\log\lambda$; the moments of order $2r\asymp\sqrt\lambda$ replace this by $2^{2-\sqrt{\lambda/C_8}}$. The range \CGeqref{eq:tails_range} is the price of the moment order: Lemma~\CGref{lem:higher_moments} needs $X\le T^{1/(160r)}$, and Fujii's approximation \CGref{thm:known_selberg_approx} with $2r$ in place of $k$ needs the prime polynomial of length $T^{1/(160r)}$."""
    theory = must_replace(theory, anchor, tails)

    # ---- Tails of the corrected clocks and the sorted clock, after the third-step corollary.
    anchor2 = r"Theorem~\CGref{thm:uniform_iteration} with $m=3$ (for $T\ge T_0$, $H_2\ge H^*$), and Theorem~\CGref{thm:multiplicity_all} with $\mathsf A=A_2(2)\le4B_\star$ and $\mathsf H=H_2$." + "\n" + r"\end{proof}"
    add2 = anchor2 + r"""

The induction \CGeqref{eq:induction_claim} bounds the moments of every order $2r\le2^{m^*-j+1}$ of the $j$-th error, not only its mean square, and the number of available moments grows with $T$. This gives tails.

\begin{corollary}[Tails of the corrected clocks]\label{cor:clock_tails}
With the cutoffs \CGeqref{eq:cutoff_law}, for $T\ge T_0$, every $1\le j<m^*$, every integer $1\le q\le2^{m^*-j}$ and every $\lambda>0$,
\begin{equation}
\#\bigl\{k\in\IT:\lL(\tau_k)|e_{j,k}|>\lambda\sqrt{H_j}\bigr\}\le\Bigl(\frac{B_\star q^2}{\lambda}\Bigr)^{2q}\#\IT .
\label{eq:clock_tails}
\end{equation}
For fixed $j$ and $q$ the right side is $\ll_q\lambda^{-2q}\#\IT$ for $T\ge T_0(j,q)$, since $2^{m^*-j}\to\infty$: the $j$-th corrected clock misses its ordinate by more than $\lambda\sqrt{H_j}$ positions on a proportion of indices that decays faster than any power of $\lambda$.
\end{corollary}

\begin{proof}
\CGeqref{eq:induction_claim} with $m=m^*$ gives $\|\lL(\tau_k)e_{j,k}\|_{2q,\IT}\le B_\star q^2\sqrt{H_j}$ for $j\le m^*-1$ and $q\le2^{m^*-j}$; apply Chebyshev's inequality to the $2q$-th moment.
\end{proof}

The Newton points of a level need not be in increasing order (Proposition~\CGref{prop:deformation} bounds the proportion of inversions of the second clock). Sorting them costs nothing.

\begin{lemma}[Sorted Newton steps]\label{lem:sorted}
Let $\gamma_1\le\dots\le\gamma_{\mathsf M}$ and let $z_1,\dots,z_{\mathsf M}$ be arbitrary reals, with $z^\uparrow$ the same values in increasing order. Then $\sum_k|z^\uparrow_k-\gamma_k|^q\le\sum_k|z_k-\gamma_k|^q$ for every $q\ge1$, and $\{z^\uparrow_k\}=\{z_k\}$ as multisets. Consequently, replacing $x^{(j)}_k$ by its sorted version at any level of \CGeqref{eq:newton_iteration} does not increase $\|e_j\|_{r,\IT}$ for any $r$, does not change the multiplicity function $\tilde n_j$, and leaves Theorems~\CGref{thm:second_step}, \CGref{thm:multiplicity_all} and \CGref{thm:uniform_iteration} and Corollary~\CGref{cor:clock_tails} unchanged; it removes the inversions $d_{j,k}\le0$ of Proposition~\CGref{prop:deformation}.
\end{lemma}

\begin{proof}
For $a\le b$, $x\le y$ and $\varphi$ convex, $\varphi(a-x)+\varphi(b-y)\le\varphi(a-y)+\varphi(b-x)$ (the points $a-y\le a-x,b-y\le b-x$ have the same sum in both pairings, and the outer pair majorizes the inner one). With $\varphi(t)=|t|^q$, each transposition of an inverted pair of $z$'s does not increase the sum, and finitely many transpositions sort $z$. The recursion \CGeqref{eq:recursion_norms} uses only $\|e_{j-1}\|_{4r}$ and the sampling of $\mathsf g_j$ on the point set $\{x^{(j-1)}_k\}$, both unchanged or improved.
\end{proof}

\begin{corollary}[An increasing computable clock]\label{cor:sorted_clock}
Let $x^{\uparrow}_k$, $k\in\IT$, be the values $x^{(m^*)}_k$ of Theorem~\CGref{thm:uniform_iteration} in increasing order. Then $x^\uparrow_k\le x^\uparrow_{k+1}$, every $x^\uparrow_k$ is computed from the clock and the primes alone, and
\[
\frac1{\#\IT}\sum_{k\in\IT}\bigl(x^\uparrow_k-\gamma_k\bigr)^2\le\frac{C'}{\log^2T}.
\]
\end{corollary}

\begin{proof}
Lemma~\CGref{lem:sorted} with $q=2$ and \CGeqref{eq:final_clock}.
\end{proof}"""
    theory = must_replace(theory, anchor2, add2)

    # ---- Theorem E: the limit constant.
    old_stmt = envelope[envelope.index(r"For $J\ge0$ let $(\mathsf k_0,\mathsf l_0)"):envelope.index(r"\end{theorem}")]
    new_stmt = (r"For $J\ge0$ let $(\mathsf k_0,\mathsf l_0)=(\frac{13}{84},\frac{55}{84})$, $(\mathsf k_j,\mathsf l_j)=\mathscr A^j(\mathsf k_0,\mathsf l_0)$ with $\mathscr A(\mathsf k,\mathsf l)=\bigl(\frac{\mathsf k}{2\mathsf k+2},\frac12+\frac{\mathsf l}{2\mathsf k+2}\bigr)$, $\sigma_j=\mathsf l_j-\mathsf k_j$, and let $\mathfrak e_J$ be the piecewise linear function through the points $(\sigma_j,\mathsf k_j)$, $0\le j\le J$, and $(1,0)$; the first vertices are $(\frac12,\frac{13}{84})$, $(\frac{139}{194},\frac{13}{194})$, $(\frac{173}{207},\frac{13}{414})$, $(\frac{773}{854},\frac{13}{854})$. Let $C_J$ be the right side of \CGeqref{eq:envelope_formula} for $\mathfrak e=\mathfrak e_J$. Then $\mathfrak a\le C_J$ for every $J$; the sequence $C_J$ decreases to a limit $C_\infty$ with $0\le C_J-C_\infty\le3\mathsf k_J\sqrt{1-\sigma_J}/(2\pi\log2)$, and" + "\n"
                r"\begin{equation}" + "\n" + r"C_\infty=0.0968151142790\ldots,\qquad\limsup_{k\to\infty}|\tau_k-\gamma_k|=2\pi\mathfrak a\le2\pi C_\infty=0.608307303\ldots ;" + "\n" + r"\label{eq:envelope_value}" + "\n" + r"\end{equation}" + "\n"
                r"for comparison $C_0=0.1010228\ldots$ (the exponent $\frac{13}{84}$ alone) and $C_7=0.0968160\ldots$." + "\n")
    envelope = envelope.replace(old_stmt, new_stmt)
    i = envelope.index(r"\emph{The profile.}"); j = envelope.index(r"\end{proof}", i)
    new_prof = (r"\emph{The profile.} Let $\varepsilon'>0$, $(\mathsf k_0,\mathsf l_0)=(\frac{13}{84}+\varepsilon',\frac{55}{84}+\varepsilon')$ and $(\mathsf k_j,\mathsf l_j)=\mathscr A^j(\mathsf k_0,\mathsf l_0)$ for $1\le j\le J$, exponent pairs by Theorem~\CGref{thm:known_exponents}(a),(c), with $\mathsf l_j-\mathsf k_j\ge\frac12$; by (b), $|\zeta(\mathsf l_j-\mathsf k_j+it)|\ll|t|^{\mathsf k_j}\log|t|$, and $|\zeta(1+it)|\ll\log|t|$. The points $(\mathsf l_j-\mathsf k_j,\mathsf k_j)$ and $(1,0)$ have decreasing ordinates, and Theorem~\CGref{thm:known_PL} between consecutive points gives the hypothesis of the theorem for the piecewise linear function through them. For $\varepsilon'=0$ these are the vertices of $\mathfrak e_J$; the right side of \CGeqref{eq:envelope_formula} depends continuously on $\varepsilon'$, so $\mathfrak a\le C_J$." + "\n\n"
                r"\emph{The limit.} From $\mathsf k_{j+1}=\mathsf k_j/(2\mathsf k_j+2)$ and $\mathsf l_{j+1}-\mathsf k_{j+1}=\frac12+(\mathsf l_j-\mathsf k_j)/(2\mathsf k_j+2)$ one gets $\mathsf k_j\le2^{-j}\mathsf k_0$, $\sigma_j<\sigma_{j+1}<1$ and $1-\sigma_{j+1}=(1-\sigma_j+\mathsf k_j)/(2\mathsf k_j+2)\le\frac12(1-\sigma_j)+\mathsf k_j$, so $\sigma_j\to1$. Each new vertex $(\sigma_{J+1},\mathsf k_{J+1})$ lies below the chord from $(\sigma_J,\mathsf k_J)$ to $(1,0)$: this is $\mathsf k_{J+1}(1-\sigma_J)\le\mathsf k_J(1-\sigma_{J+1})$, i.e.\ $\frac{1-\sigma_J}{2\mathsf k_J+2}\le\frac{1-\sigma_J+\mathsf k_J}{2\mathsf k_J+2}$, which holds. Hence $\mathfrak e_{J+1}\le\mathfrak e_J$ on $[\frac12,1]$ (they agree on $[\frac12,\sigma_J]$), the reflected parts are ordered in the same way, and $C_{J+1}\le C_J$; the limit $C_\infty$ exists. Since $0\le\mathfrak e_J-\mathfrak e_{J'}\le\mathsf k_J$ for $J'\ge J$, supported on $[\sigma_J,1]$ and, after reflection, on $[0,1-\sigma_J]$, and $\sigma(2-\sigma)\ge\sigma$ on $[0,1]$," + "\n"
                r"\[" + "\n" + r"\begin{split}0\le C_J-C_{J'}&\le\frac{\mathsf k_J}{2\pi\log2}\Bigl(\int_{\sigma_J}^1\frac{d\sigma}{\sqrt{\sigma(2-\sigma)}}+\int_0^{1-\sigma_J}\frac{d\sigma}{\sqrt\sigma}\Bigr)\\&\le\frac{\mathsf k_J\bigl((1-\sigma_J)\sqrt2+2\sqrt{1-\sigma_J}\bigr)}{2\pi\log2}\le\frac{3\mathsf k_J\sqrt{1-\sigma_J}}{2\pi\log2}.\end{split}" + "\n" + r"\]" + "\n"
                r"\emph{The values.} On each linear piece $\mathfrak e(\sigma)=\alpha\sigma+\beta$ of $[0,1]$ a primitive of $\mathfrak e(\sigma)/\sqrt{\sigma(2-\sigma)}$ is $-\alpha\sqrt{\sigma(2-\sigma)}+(\alpha+\beta)\arcsin(\sigma-1)$; the vertices are rational, and the program \texttt{opc\_envelope\_iterations\_p1.py} (Data availability) evaluates $C_J$ from this primitive at $50$ digits for $0\le J\le30$. It gives $C_{30}=0.09681511427905377\ldots$ and $3\mathsf k_{30}\sqrt{1-\sigma_{30}}/(2\pi\log2)<5\cdot10^{-15}$, hence $C_\infty\in[C_{30}-5\cdot10^{-15},C_{30}]$ and \CGeqref{eq:envelope_value}; $C_7$ agrees with the $40$-digit quadrature of \texttt{opc\_envelope\_coefficient\_v14.py}. Multiply by $2\pi$ and use Proposition~\CGref{prop:envelope_equivalence}(a)." + "\n")
    envelope = envelope[:i] + new_prof + envelope[j:]

    ns['theory'] = theory; ns['envelope'] = envelope; ns['external'] = external
