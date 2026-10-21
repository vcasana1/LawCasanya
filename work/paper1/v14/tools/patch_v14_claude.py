#!/usr/bin/env python3
"""v14 = v13 + corrections of the second review (audit/revision2), each derived in
audit/VERIFICACION_v14.md before being applied. Every replacement is asserted to match
exactly the stated number of times, in the body only (hover previews are regenerated)."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT.parent / 'v13' / 'manuscript' / 'prime_corrected_clock_v13.tex'
DST = ROOT / 'manuscript' / 'prime_corrected_clock_v14.tex'
text = SRC.read_text()
B0 = text.index('\\begin{document}')

def rep(old, new, cnt=1):
    global text
    head, body = text[:B0], text[B0:]
    n = body.count(old)
    assert n == cnt, f'{n} matches (expected {cnt}) for: {old[:100]!r}'
    text = head + body.replace(old, new)

def fresh(sym):
    """New symbols must not occur in the v13 body."""
    assert sym not in text[B0:], f'symbol {sym!r} already used'

for s in [r'C_4', r'C_{11}', r'\tilde\chi', r'K_\star', r'K_{\rm M}', r'N^{\rm s}_{1/2}', r'P^{\rm G}_X', r'\varepsilon_k']:
    fresh(s)
assert not re.search(r'(?<!\\mathsf )C_{11}(?![0-9])', text[B0:]), 'plain C_{11} in use'

# ===================== 1. Lemma 8.2, second bound (VERIFICACION 1)
rep(r'The second: Theorem~\CGref{thm:identity_general} with $j=r$ and $F=F_X$,',
    r'The second: Theorem~\CGref{thm:identity_general} with $j=r$, $F=F_X$, $k_1=N(T)$ and $k_2=N(2T)+1$ (so that the sum runs over $\IT$),')
rep(r'$\int_T^{2T}E_X^{2r}|S_X'"'"r'|\le\mathcal E_{4r}^{1/2}C_{\rm d}T^{1/2}(1+\log X)$, $C_{\rm d}$ the constant of \CGeqref{eq:SX_derivative}',
    r'$\int_T^{2T}E_X^{2r}|S_X'"'"r'|\le\mathcal E_{4r}^{1/2}\sqrt{C_{\rm d}}\,T^{1/2}(1+\log X)$, $C_{\rm d}$ the constant in $\int_T^{2T}S_X'"'"r'^2\le C_{\rm d}T(1+\log X)^2$ \CGeqref{eq:SX_derivative}')
rep(r'and the first bound gives the second with $2(4+2\pi\sqrt{C_{\rm d}}+9\pi C_{\rm b})C$ in place of $C$, since $2^{2r}K_1+K_2\le(2(K_1+K_2))^{2r}$ for $K_1,K_2\ge1$.',
    r'and the first bound, with $Z=C(r^2+\sqrt{r(1+V)})\ge1$ ($C\ge1$), gives $T^{-1/2}\mathcal E_{4r}^{1/2}\le Z^{2r}$, $T^{-2r}\le Z^{2r}$ and $(Cr^2)^{2r}\le Z^{2r}$, hence $\langle u_k(X)^{2r}\rangle_{\IT}\le(2^{2r}K_1+K_2)Z^{2r}$ with $K_1=4+4\pi\sqrt{C_{\rm d}}$ and $K_2=9\pi C_{\rm b}+1$; since $2^{2r}K_1+K_2\le2^{2r}(K_1+K_2)\le(2(K_1+K_2))^{2r}$, the second bound holds with $2(5+4\pi\sqrt{C_{\rm d}}+9\pi C_{\rm b})C$ in place of $C$.')

# ===================== 2. V with the cutoff Y_{2r} (VERIFICACION 2)
rep(r'with $V$ as in Lemma~\CGref{lem:V_size} computed with $Y_{2r}=T^{1/(160r)}$ in place of $Y_0$,',
    r'with $V=\sum_{X<p\le Y_{2r}}p^{-1}$, $Y_{2r}=T^{1/(160r)}$ (the sum \CGeqref{eq:D_def} with $Y_{2r}$ in place of $Y_0$),')
rep(r'Lemma~\CGref{lem:V_size} gives $V=\log(1/(160rc))+O(1)\le\log(1/c)+C_9\le(\lambda/C_8)^{3/2}+C_9$, with an absolute constant $C_9\ge0$,',
    r'Theorem~\CGref{thm:known_mertens}, as in the proof of Lemma~\CGref{lem:V_size} with $Y_{2r}$ in place of $Y_0$, gives $V=\log\frac{\log Y_{2r}}{\log X}+O(1)=\log(1/(160rc))+O(1)$ with an absolute $O(1)$ (note $160rc\le1$), so $V\le\log(1/c)+C_9\le(\lambda/C_8)^{3/2}+C_9$ with an absolute constant $C_9\ge0$,')

# ===================== 3. Theorem 8.11 (VERIFICACION 3)
rep(r'and $\log H_{j-1}\le H_j$ for all $j$.', r'and $\log H_{j-1}\le H_j$ for every $j$ with $H_{j-1}\ge1$ (as $C_\star\le1$).')
rep(r'the sequence $H_j$ decreases from $\log\log T$ to below $H^*$ in $m^*=\log^*T+O(1)$ steps, where $\log^*$ is the iterated logarithm.',
    r'the sequence $H_j$ decreases from $\log\log T$ to below $H^*$ in $m^*=\log^*T+O(1)$ steps, where $\log^*$ is the iterated logarithm. Indeed, let $L_j=\log^{(j)}H_0$ and $K_\star=2\log(1/C_\star)+1$. While $L_{j-1}\ge K_\star$, induction gives $H_j\le\frac98L_j+K_\star$: for $j\le2$, $H_j=L_j$; for $j\ge3$, $H_j\le\frac98\log(\frac98L_{j-1}+K_\star)+K_\star-1\le\frac98L_j+\frac98\log\frac{17}8+K_\star-1$, and $\frac98\log\frac{17}8<1$. If $J$ is the first index with $L_J<K_\star$, then $J\le\log^*T+O_{C_\star}(1)$ and $H_J\le\frac{17}8K_\star$; after $J$, as long as $H_{j+1}\ge H^*$ one has $H_{j+1}\le\frac14H_j$ (\emph{the three conditions} in the proof of Theorem~\CGref{thm:uniform_iteration}), so at most $1+\log_4^+(\frac{17}8K_\star/H^*)$ further indices have $H_j\ge H^*$. Hence $m^*\le\log^*T+O(1)$ with an $O(1)$ depending only on $C_\star$ and $H^*$; conversely $H_j\ge L_j$ while $L_{j-1}\ge1$, so $m^*\ge\log^*T-O(1)$. Only the upper bound is used.')
rep(r'There are absolute constants $C_\star$, $H^*$, $C$ and $T_0$ such that, with the cutoffs',
    r'There are absolute constants $C_\star$, $H^*$, $C_4$, $C_{11}$ and $T_0$ such that, with the cutoffs')
rep(r'+\upsilon_m\,C\bigl(1+\sqrt{H_m}\bigr),\qquad|\upsilon_m|\le1,', r'+\upsilon_m\,C_4\bigl(1+\sqrt{H_m}\bigr),\qquad|\upsilon_m|\le1,')
rep(r'and $\|\lL(\tau_k)e_{j,k}\|_{4,\IT}\le C\sqrt{H_j}$ for $1\le j<m^*$.', r'and $\|\lL(\tau_k)e_{j,k}\|_{4,\IT}\le C_4\sqrt{H_j}$ for $1\le j<m^*$.')
rep(r'\le\frac{C'"'"r'}{\log^2T}:' '\n' r'\label{eq:final_clock}', r'\le\frac{C_{11}}{\log^2T}:' '\n' r'\label{eq:final_clock}')
rep(r'\le\frac{C'"'"r'+1}{\log^2T}.', r'\le\frac{C_{11}+1}{\log^2T}.')
rep(r'\le\frac{C'"'"r'\,\#\IT}{\log^2T}+O\bigl(T^{1/160}\bigr)\le\frac{(C'"'"r'+1)\,\#\mathcal I_T^\tau}{\log^2T}',
    r'\le\frac{C_{11}\,\#\IT}{\log^2T}+O\bigl(T^{1/160}\bigr)\le\frac{(C_{11}+1)\,\#\mathcal I_T^\tau}{\log^2T}')
rep(r'\emph{Base.} For every $r\ge1$ with $2r\le\kappa_{\rm F}\log T$, by Lemma~\CGref{lem:higher_moments} with $X=2$, $|S_2|\le\sigma_2<1$',
    r'\emph{Base.} For every $r\ge1$ with $2r\le\kappa_{\rm F}\log T$, by Lemma~\CGref{lem:higher_moments} with $X=2$ (admissible: $2r\le\kappa_{\rm F}\log T$ gives $160r\log2\le\frac{160}{600}\log T$, so $2\le T^{1/(160r)}$), $|S_X|\le\sigma_X<1$ for $X=2$')
rep(r'Lemma~\CGref{lem:higher_moments} (with $1+V\le\log\frac1{c_j}+O(1)\le C'"'"r'H_j$, $C'"'"r'$ absolute since $H_j\ge H^*\ge1$, absorbed into $C$),',
    r'Lemma~\CGref{lem:higher_moments} (with $1+V\le\log\frac1{c_j}+K_{\rm M}=\frac12H_j+K_{\rm M}\le(K_{\rm M}+1)H_j$ when $H_j\ge1$, $K_{\rm M}$ the absolute constant given by Theorem~\CGref{thm:known_mertens}; the factor $\sqrt{K_{\rm M}+1}$ is absorbed into $C$, which stays absolute and is fixed before $C_\star$ and $H^*$; the condition $H_j\ge1$ holds at every level $j\le m-1<m^*$ where the bound is used, because $H_j\ge H^*\ge1$),')
rep(r'Then, for all $j\ge1$ and $r\ge1$,', r'Then, for $1\le j<m^*$ and $r\ge1$ (and, for the transport term alone, also at $j=m^*$, which only needs $H_{j-1}\ge H^*$),')
rep(r'Let $H^*$ be an absolute constant with $H^*\ge\max(4C_6,160^2\cdot4)$', r'Let $H^*$ be an absolute constant with $H^*\ge\max(4C_6,160^2)$')
rep(r'which is the statement $\|\lL e_j\|_{4,\IT}\le4B_\star\sqrt{H_j}$ for $j<m^*$.',
    r'which is the statement $\|\lL e_j\|_{4,\IT}\le4B_\star\sqrt{H_j}$ for $j<m^*$; so $C_4$ may be taken as the larger of $4B_\star$ and the implied constant of the last step below.')
rep(r'and $\lL(\tau_k)=\frac{\log T}{2\pi}(1+O(1/\log T))$ give \CGeqref{eq:final_clock}.',
    r'and $\lL(\tau_k)=\frac{\log T}{2\pi}(1+O(1/\log T))$ give \CGeqref{eq:final_clock}, with $C_{11}=8\pi^2\bigl(H^*/(4\pi^2)+C_4(1+\sqrt{H^*})\bigr)$, since $\lL(\tau_k)^{-2}\le8\pi^2/\log^2T$ for $T\ge T_0$.')

# ===================== 4. Prop 8.8: case r=4 (VERIFICACION 4)
rep(r'which need the case $r=2$ of the third bound of Lemma~\CGref{lem:higher_moments} ($X_2\le T^{1/8}$,',
    r'which need the case $r=4$ of the third bound of Lemma~\CGref{lem:higher_moments} ($\int|\partial_t^\nu S_{X_2}|^{16}$, $4r=16$; it requires $X_2\le T^{1/8}$,')

# ===================== 5. Lemma 8.5: constant (VERIFICACION 5)
rep(r'and $\|\mathsf F'"'"r'\|_2\le4r\|g\|_{8r}^{4r-1}\|g'"'"r'\|_{8r}\le4r(1+\log X)\,(C\sqrt r(1+\log X))^{4r}T^{1/2}$,',
    r'and, since $\|g'"'"r'\|_{8r}\le\mathcal A_{8r}(2\|S'"'"r'_X\|+\|S'"'"r''"'"r'_X\|)\le3(1+\log X)\,\mathcal A_{8r}(2Cr)^{1/2}T^{1/(8r)}(1+\log X)$, $\|\mathsf F'"'"r'\|_2\le4r\|g\|_{8r}^{4r-1}\|g'"'"r'\|_{8r}\le12r(1+\log X)\,(C\sqrt r(1+\log X))^{4r}T^{1/2}$ (with $C$ enlarged),')
rep(r'$b\cdot4r(1+\log X)=\frac{8\pi r(1+\log X)}{\log(3T)}', r'$b\cdot4r(1+\log X)=\frac{8\pi r(1+\log X)}{\log(3T)}')
rep(r'<16$, and we get $\sum_k\mathsf F(\mathsf x_k)\le17\,b^{-1}', r'<16$, so $b\cdot12r(1+\log X)<48$, and we get $\sum_k\mathsf F(\mathsf x_k)\le49\,b^{-1}')

# ===================== 6. Theorem 8.6: admissibility (VERIFICACION 6)
rep(r'Lemma~\CGref{lem:higher_moments} with $r=2$ gives $\langle u_k(X_1)^4\rangle',
    r'Lemma~\CGref{lem:higher_moments} with $r=2$ (admissible: $c_1=H_0^{-1/2}\le\frac1{320}$ and $4\le\kappa_{\rm F}\log T$ for $T\ge T_0$) gives $\langle u_k(X_1)^4\rangle')

# ===================== 7. Lemma 8.7 (VERIFICACION 7)
rep(r'For $j\ge1$, with $y^{(j)}_k=\tau_k-x^{(j)}_k$ and $\chi'"'"r''"'"r'_{j,k}=', r'For $j\ge1$ and $k$ with $\tau_k\ge T-1$, with $y^{(j)}_k=\tau_k-x^{(j)}_k$ and $\tilde\chi_{j,k}=')
rep(r'+\frac{S_{X_j}(x^{(j-1)}_k)+\chi'"'"r''"'"r'_{j,k}}{\lL(x^{(j-1)}_k)},', r'+\frac{S_{X_j}(x^{(j-1)}_k)+\tilde\chi_{j,k}}{\lL(x^{(j-1)}_k)},')
rep(r'(the first condition holds by \CGeqref{eq:sigma_M_def} and induction), and $|\mathfrak r_{j,k}|\ll T^{c_j-1}$ when moreover $c_{j-1}\le c_j$:',
    r'(the first condition holds by \CGeqref{eq:sigma_M_def} and induction; for $j=1$, $y^{(0)}_k=0$ and $\mathfrak r_{1,k}=0$), and $|\mathfrak r_{j,k}|\ll T^{c_j-1}$ when moreover $c_{j-1}\le c_j$:')
rep(r'and $\chi'"'"r''"'"r'_{j,k}\le(y^{(j-1)}_k)^2/(4\pi(T-T^{1/2}))$. Newton',
    r'and $\frac{\lL(\tau_k)}{\lL(x)}\tilde\chi_{j,k}\le(1+o(1))(y^{(j-1)}_k)^2/(4\pi(T-T^{1/2}))$. Newton')
rep(r'=-\lL(\tau_k)y^{(j-1)}_k+\chi'"'"r''"'"r'_{j,k}$, with $0\le\chi'"'"r''"'"r'_{j,k}\le(y^{(j-1)}_k)^2/(4\pi(T-T^{1/2}))$;',
    r'=-\lL(\tau_k)y^{(j-1)}_k+\tilde\chi_{j,k}$, with $0\le\tilde\chi_{j,k}\le(y^{(j-1)}_k)^2/(4\pi(T-T^{1/2}))$ (both $\tau_k$ and $x^{(j-1)}_k$ are $\ge T-T^{1/2}$);')
assert "chi''" not in text[B0:], 'chi double prime left'

# ===================== 8. Lemma 8.4 (VERIFICACION 8)
rep(r'Each $t$ lies in at most $m$ of the intervals $J_{k,m}$ ($k$ varying)', r'Almost every $t$ lies in at most $m$ of the intervals $J_{k,m}$ ($k$ varying)')
rep(r'\ll T\log T\,c_1^2\asymp \mathsf M\,c_1^2 .' '\n' r'\end{aligned}' '\n' r'\]' '\n' r'by \CGeqref{eq:SX_derivative}, uniformly in $m$.',
    r'\ll T\log T\,c_1^2\asymp \mathsf M\,c_1^2' '\n' r'\end{aligned}' '\n' r'\]' '\n' r'by \CGeqref{eq:SX_derivative} on $[T-1,2T-2]$ and on $[T+1,2T+2]$ (with $T-1$ and $T+1$ in place of $T$, as in the proof of Theorem~\CGref{thm:fixed_cutoff_step}), uniformly in $m$.')
rep(r'Hence the number of pairs $(j,k)$ with $|x^{(1)}_j-x^{(1)}_k|\le b$ is $\ll \mathsf M$', r'Hence the number of pairs $(k,l)$ with $|x^{(1)}_l-x^{(1)}_k|\le b$ is $\ll \mathsf M$')

# ===================== 9. Lemma 8.9, Hölder (VERIFICACION 9)
rep(r'\le\frac{T^{1/4}(C\mathsf R^4T)^{3/4}}{2\mathsf R b}', r'\le\frac{(T+1)^{1/4}(C\mathsf R^4T)^{3/4}}{2\mathsf R b}')

# ===================== 10. Lemma 5.11 (VERIFICACION 10)
rep(r'\ll T\bigl(\sum_pp^{-2}+4V_\pm^2\bigr)\ll TV_\pm^2$,', r'\ll T\bigl(\sum_pp^{-2}+4V_\pm^2\bigr)\ll TV_\pm^2$ (using $V_\pm\ge1/X_+$, as $(X_-,X_+]$ contains a prime),')

# ===================== 11. Prop 8.1 (VERIFICACION 11)
rep(r'Let $j\ge1$ and suppose $x^{(j-1)}_k>2\pi$. Then', r'Let $j\ge1$, let $I$ be a finite set of indices, and suppose $x^{(i)}_k>2\pi$ for $0\le i\le j-1$ and $k\in I$. Then, for $k\in I$,')

# ===================== 12. Theorem E, remarks and data (VERIFICACION 12; program v10 run)
rep(r'and adding the $\mathscr A$-images ($j\le10$) of the $\mathscr B$-images of the $\mathscr A$-images of the pairs with $m\le300$ does not lower the value (same program)',
    r'and adding to $\mathcal P$ the $\mathscr A$-images ($j\le10$) of the $\mathscr B$-images of the $\mathscr A$-images of the pairs with $m\le300$ leaves $\mathsf C_{\mathcal P}$ unchanged (\texttt{envelope\_\allowbreak best\_\allowbreak profile\_\allowbreak v10.py})')
rep(r'for $1-\sigma<3\cdot10^{-7}$, beyond the last vertex used, where it would change $\mathsf ', r'for $1-\sigma<3\cdot10^{-7}$, where $\mathfrak e_{\mathcal P}<10^{-10}$, and it would change $\mathsf ')
rep(r'Every admissible profile is at least the Lindel\"of profi', r'Every admissible profile is $\ge0$ on $[\frac12,1]$, since $\int_T^{2T}|\zeta(\sigma+it)|^2dt\gg T$ there, hence at least the Lindel\"of profi')
rep(r'the right side is $C_L=(\frac{\sqrt3}2-\frac\pi6)/(2\pi\log2)', r'the right side is $\mathsf C_L=(\frac{\sqrt3}2-\frac\pi6)/(2\pi\log2)')
rep(r'Yang\textquoteright s lines $\sigma_j=1-j/(2^j-2)$ with exponents', r'Yang\textquoteright s lines $\sigma=1-j/(2^j-2)$ with exponents')
rep(r'encloses $C_{30}$ and the analytic', r'encloses $\mathsf C_{30}$ and the analytic')
rep(r'the upper bound $2\pi C_\infty<0.6083074$', r'the upper bound $2\pi\mathsf C_\infty<0.6083074$')
rep(r'numerical manifest identifies each program', r'numerical manifest (\texttt{audit/\allowbreak numerical\_\allowbreak manifest.json}) identifies each program')
rep(r'\texttt{envelope\_best\_profile\_v9.py}', r'\texttt{envelope\_best\_profile\_v10.py}')
rep(r'best\_\allowbreak profile\_\allowbreak v9.py}', r'best\_\allowbreak profile\_\allowbreak v10.py}')
rep(r'best\_\allowbreak profile\_\allowbreak v9.txt}', r'best\_\allowbreak profile\_\allowbreak v10.txt}')
assert 'profile\\_\\allowbreak v9' not in text[B0:] and 'profile\\_v9' not in text[B0:]
n9 = text[B0:].count('profile\\_\\allowbreak v9'); print('v9 program refs in body:', n9)

# ===================== 13. Abstract, introduction, tables, conclusions
rep(r'(A) an exact identity that turns sums of $\mathcal G(u_k+\frac12)-\mathcal G(u_k-\frac12)$,', r'(A) an exact identity that turns sums of $\mathfrak G(u_k+\frac12)-\mathfrak G(u_k-\frac12)$,')
rep(r'the ordinal defect has exponential tails and the errors of the corrected clocks have all moments bounded in units of $\sqrt{H_m}$;',
    r'the ordinal defect has tails $\ll2^{-\sqrt{\lambda/C_8}}$ at $\lambda$ positions for cutoffs $T^c$ in a range of $c$ depending on $\lambda$, and for each fixed level $j$ and order $q$ the errors of the $j$-th corrected clock have bounded moments in units of $\sqrt{H_j}$ for $T\ge T_0(j,q)$;')
rep(r'piecewise linear functions with slopes between $\frac{\log T}{4\pi}$', r'piecewise linear functions on a mesh of step at most $2\pi/\log T$ with slopes between $\frac{\log T}{4\pi}$')
rep(r'is at least $\#\{T<\gamma_k\le2T\}-\sum_k(2u_k)^{2j}$,', r'is at least $\#\{T<\gamma_k\le2T\}-\sum_{T<\gamma_k\le2T}(2u_k)^{2j}$ ($j\ge1$),')
rep(r'\begin{theorem}[Exponential tails of the ordinal defect]\label{thm:tails}', r'\begin{theorem}[Stretched-exponential tails of the ordinal defect]\label{thm:tails}')
rep(r'and for D$'"'"r'$, Corollary~\CGref{cor:local_clock} and Corollary~\CGref{cor:sorted_clock} over the window $T\le\tau_k<2T$;',
    r'and for D$'"'"r'$ also over the window $T\le\tau_k<2T$, over which Corollaries~\CGref{cor:local_clock} and \CGref{cor:sorted_clock} are stated;')
rep(r'together with Fujii'"'"r's moments of $S(t+h)-S(t)$ \cite{Fujii1975,Titchmarsh1986}.',
    r'together with Fujii'"'"r's corrected moments of $S(t+h)-S(t)$ for $0<h\le1$ \cite[($\alpha'"'"r'$)]{Fujii1981} (Theorem~\CGref{thm:known_fujii_difference}).')
rep(r'for every exponent profile $\mathfrak e$ of the Riemann zeta function on $[\frac12,1]$,',
    r'for every continuous $\mathfrak e$ on $[\frac12,1]$ with $\mathfrak e(1)=0$ and $\zeta(\sigma+it)\ll_\varepsilon|t|^{\mathfrak e(\sigma)+\varepsilon}$ uniformly for $\frac12\le\sigma\le1$, $|t|\ge2$,')
rep(r'given explicitly by $X$, $\NO$ and the primes.', r'given explicitly by $X$, $\NO$, the primes and the choices of $t_1$ and of $\mathsf r_k$, $k<k_0$.')
rep(r'$\log\#\{p\le X\}=\log X+O(\log\log X)$', r'$\log\#\{p\le X\}=\log X+O(\log\log(3X))$')
rep(r'$\limsup|\delta_k|$ is Theorem E.\\', r'$\limsup|\delta_k|=2\pi\limsup|S(t)|/\log t$ (Proposition~\CGref{prop:envelope_equivalence}), bounded in Theorem E.\\')
rep(r'the primes $p\le T^c$, $c<\frac12$ fixed;', r'the primes $p\le X$, $2\le X\le\sqrt{T/2}$;')
rep(r'exceeds the minimum by at most $\eta T$, $\eta\le1$, gives the same bounds with $(1+\log\frac1c)^2+\eta$',
    r'exceeds the minimum by at most $\eta_{\rm reg}T$, $\eta_{\rm reg}\le1$, gives the same bounds with $(1+\log\frac1c)^2+\eta_{\rm reg}$')
rep(r'exceeds $\lambda$ on at most $2^{2-\sqrt{\lambda/C_8}}$ of the zeros', r'exceeds $\lambda$ on at most a proportion $2^{2-\sqrt{\lambda/C_8}}$ of the zeros')
rep(r'between the consecutive Gram points $g_{k-2}$ and $g_{k-1}$ for $k$ large.', r'between the consecutive Gram points $g_{k-2}$ and $g_{k-1}$ for every $k\ge1$.')
rep(r'so $g_{k-2}<\tau_k<g_{k-1}$ for $k$ large;', r'so $g_{k-2}<\tau_k<g_{k-1}$ for every $k\ge1$, since $\tau_1>14$, $|\varpi|/\pi<\frac1{100}$ on $[14,\infty)$ and $\vartheta$ is increasing there;')

# ===================== 14. Notation (second sweep)
rep(r'($|\delta_k|\le C_{10}$, Theorem~\CGref{thm:known_basic})', r'($|\delta_k|\le C_{10}$, \CGeqref{eq:BW_pointwise})')
rep(r'an absolute bound for $|\delta_k|$ (\CGeqref{eq:BW_pointwise})', r'an absolute bound for $|\delta_k|$, \CGeqref{eq:BW_pointwise}')
rep(r'for all $k$ (\CGeqref{eq:BW_pointwise}), the symmetric difference', r'for all $k$, by \CGeqref{eq:BW_pointwise}, the symmetric difference')
rep(r'$\Psi_j$, $\kappa_j$ & sawtooth polynomial \CGeqref{eq:Psi_def};', r'$\Psi_j$, $\kappa_j$ & mean of $x^{2j}$ over $[u-\frac12,u+\frac12]$ \CGeqref{eq:Psi_def};')
rep(r'$y_0$, $w_T$ & fixed threshold; threshold tending to infinity (Corollary~\CGref{cor:dichotomy})\\',
    r'$y_0$, $w_T$ & fixed threshold; threshold tending to infinity (Corollaries~\CGref{cor:fixed_cutoff} and \CGref{cor:power_cutoff})\\')
rep(r'$\mathsf M$, $\mathsf P$, $\mathsf F$, $\mathsf s$, $\mathsf W$, $\mathsf y$ & local names in proofs: $\#\IT$; number of close pairs; $g^{4r}$ (Lemma~\CGref{lem:sampling_rho}); window and scale (Lemma~\CGref{lem:maximal_primes})\\',
    r'$\mathsf M$, $\mathsf P$, $\mathsf F$, $\mathsf s$, $\mathsf W$, $\mathsf y$ & local names in proofs: $\#\IT$; number of close pairs; $g^{4r}$ (Lemma~\CGref{lem:sampling_rho}; in Lemma~\CGref{lem:midpoint_rule}, a monotone model); bump function, window and scale (Lemma~\CGref{lem:maximal_primes})\\'
    '\n'
    r'$C_4$, $C_{11}$, $K_\star$, $K_{\rm M}$, $\upsilon_m$ & constants of Theorem~\CGref{thm:uniform_iteration} and of its proof; $|\upsilon_m|\le1$\\'
    '\n'
    r'$N^{\rm s}_{1/2}(T,2T)$, $Q_{2j}$, $f_z$, $P_X$, $P^{\rm G}_X$ & simple zeros on the line in $(T,2T]$; $dF_X$-moments of $N-F_X$; \CGeqref{eq:f_z}; $\prod_{p\le X}(1-p^{-s})^{-1}$; Gonek'"'"r's smoothed product\\'
    '\n'
    r'$\mathcal I'"'"r'_T$, $\mathcal I_T^{\rm blk}$, $x^\uparrow_k$, $X^{\rm loc}_k$, $\mathrm{sw}$ & index sets of Proposition~\CGref{prop:monotone} and Corollary~\CGref{cor:sorted_clock}; sorted points; local cutoff (Corollary~\CGref{cor:local_clock}); sawtooth $\lfloor v+\frac12\rfloor-v$\\')
rep(r'$S(t)=O(\log t)$; $\gamma_{k+1}-\gamma_k$ is bounded; and $S_1(t)=\int_0^tS(y)\,dy=O(\log t)$.', r'$S(t)=O(\log t)$, and $\gamma_{k+1}-\gamma_k$ is bounded.')
# N_0^s -> N^s_{1/2}
nS = text[B0:].count('N_0^s'); print('N_0^s occurrences:', nS)
rep('N_0^s', r'N^{\rm s}_{1/2}', nS)
# Gonek's product
rep(r'Gonek'"'"r's functions $\zeta_X(s)=P_X(s)+\chi(s)\overline{P_X(s)}$, built from the finite Euler product $P_X$,',
    r'Gonek'"'"r's functions $\zeta_X(s)=P^{\rm G}_X(s)+\chi(s)\overline{P^{\rm G}_X(s)}$, built from the smoothed Euler product $P^{\rm G}_X$,')
g387 = re.search(r'\\item Gonek.*', text[B0:]).group(0)
print('P_X left in Gonek item:', g387.count('P_X(')-g387.count('P^{\\rm G}_X('))
# local d_k (Theorem D'') collides with the gaps d_{j,k}: rename to \varepsilon_k in its paragraph only
a = text.index(r'so $d_k=r_k(X)-u_k(X)=\mathfrak t_k+\chi_k$', B0); b = text.index('\n', a)
seg = text[a:b]; nd = len(re.findall(r'd_k(?![\w])', seg)); print('d_k in paragraph:', nd)
text = text[:a] + re.sub(r'd_k(?![\w])', r'\\varepsilon_k', seg) + text[b:]
# used before defined
rep(r'i.e.\ $|E|\le\frac12$ with $E=E_X+\varpi/\pi$.', r'i.e.\ $|E|\le\frac12$ with $E=E_X+\varpi/\pi$, $E_X=S-S_X$ ($V$ below is the sum in \CGeqref{eq:D_def}).')
rep(r'Theorem~\CGref{thm:main} gives $\|u(X)\|_{2,\IT}=O_c(1)$,', r'Theorem~\CGref{thm:main} gives $\|u(X)\|_{2,\IT}=\langle u_k(X)^2\rangle_{\IT}^{1/2}=O_c(1)$,')

# ===================== 15. Targeted check of the changed passages (audit/revision3)
fresh(r"\mathsf C_{\mathcal P'}"); fresh(r'j_\circ'); fresh(r's_{\rm c}')
rep(r'integrals of $g(N-F)$, where $\mathcal G'"'"r'=g$, for every continuous $g$', r'integrals of $\mathfrak g(N-F)$, where $\mathfrak G'"'"r'=\mathfrak g$, for every continuous $\mathfrak g$')
rep(r'that is $2\pi C_L=', r'that is $2\pi\mathsf C_L=')
rep(r'lies above $\mathfrak e_{\mathcal P}$ except for $1-\sigma<3\cdot10^{-7}$, where $\mathfrak e_{\mathcal P}<10^{-10}$, and it would change $\mathsf C_{\mathcal P}$ by less than $10^{-15}$.',
    r'lies above $\mathfrak e_{\mathcal P}$ except for $1-\sigma<s_{\rm c}$, with a crossing point $s_{\rm c}<3\cdot10^{-7}$; there, by convexity, $0\le\mathfrak e_{\mathcal P}(\sigma)\le\kappa\sqrt{s_{\rm c}}\,(1-\sigma)$ (the chord from the crossing to $(1,0)$), so taking the smaller of the two profiles would lower $\mathsf C_{\mathcal P}$, reflected part included, by less than $\frac{\kappa\sqrt{s_{\rm c}}}{2\pi\log2}\bigl(s_{\rm c}^2+\tfrac23s_{\rm c}^{3/2}\bigr)<10^{-14}$.')
rep(r'the same program gives $2\pi\mathsf C<0.6061342$', r'the same program gives $2\pi\mathsf C_{\mathcal P'"'"r'}<0.6061342$ for the enlarged set $\mathcal P'"'"r'$')
rep(r'adding them gives $2\pi\mathsf C<0.6060224$', r'adding them gives $2\pi\mathsf C_{\mathcal P'"'"r''"'"r'}<0.6060224$')
rep(r'with $V=\sum_{X<p\le Y_{2r}}p^{-1}$,', r'with $V=\sum_{X<p<Y_{2r}}p^{-1}$,')
rep(r'the localization of the points proved below is used, and it is applied on $\mathcal I_T^{\rm blk}$', r'the localization of the points proved below is used, and it is used only for $k\in\mathcal I_T^\tau$, where $\tau_k\ge T$')
rep(r'the primes and the choices of $t_1$ and of $\mathsf r_k$, $k<k_0$.', r'the primes, the starting height and the finitely many $\mathsf r_k$ below it (Theorem~\CGref{thm:euler_product}).')
rep(r'If $J$ is the first index with $L_J<K_\star$, then $J\le\log^*T+O_{C_\star}(1)$ and $H_J\le\frac{17}8K_\star$; after $J$,',
    r'If $j_\circ$ is the first index with $L_{j_\circ}<K_\star$, then $j_\circ\le\log^*T+O_{C_\star}(1)$ and $H_{j_\circ}\le\frac{17}8K_\star$; after $j_\circ$,')
DST.write_text(text)
print('v14 written,', len(text), 'bytes')
