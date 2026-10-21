# Notation/reference audit of prime_corrected_clock_v13.tex (read-only)

N1 [real] L1776/1781/1783 vs proof L1794,1805,1816,1818: Thm uniform_iteration states "absolute constants C_star,H^*,C,T_0", "<=C sqrt(H_j)" and eq:final_clock "C'/log^2T"; the proof uses C for the lemma constant (B_star=max(2C,2C_0,1) >= 2C, and it proves 4B_star >= 8C, so the statement's C cannot be the proof's C) and C' at L1794 for "1+V<=C'H_j". Cor sorted_clock (L1865,1872) uses C'+1. Fix: in statement, "\upsilon_m\,C_4\bigl(1+\sqrt{H_m}\bigr)" and "\|\lL(\tau_k)e_{j,k}\|_{4,\IT}\le C_4\sqrt{H_j}"; eq:final_clock "\le\frac{C_7}{\log^2T}"; Cor sorted "\frac{C_7+1}{\log^2T}" (twice); L1794 "(with $1+V\le\log\frac1{c_j}+O(1)\ll H_j$, since $H_j\ge H^*\ge1$, absorbed into $C$)"; end of "three conditions" L1816: "...for $j<m^*$, so $C_4=4B_\star$ is admissible." Fills the C_4/C_7 numbering gaps; update table L668/671.

N2 [real] L1792: "$|S_2|\le\sigma_2<1$" and "$\|u_k(2)\|$": subscript 2 means X=2, while in the same section X_2,c_2,H_2,\mathsf g_2,\chi_{2,k} index step 2 (sigma_2 reads as sigma_{X_2}). Fix: "by Lemma~\CGref{lem:higher_moments} with $X=2$, $|S_X|\le\sigma_X<1$ for $X=2$ and $0\le\chi_k\le1/T$".

N3 [real] L537, 2131, 2155, 2161, 2167, 2170 (and tooltip eq:intro_F): $N_0^s(T,2T)$ is visually \NO=N_0 with a superscript. Fix: rename to $N^{\rm s}_{1/2}(T,2T)$ (all occurrences).

N4 [real] L387 vs 545/2218: $P_X$ = Gonek's smoothed product (exp of sum over n<=X^2 with weights Lambda_X(n)) and later $P_X(s)=\prod_{p\le X}(1-p^{-s})^{-1}$. Fix L387: "$\zeta_X(s)=P^{\rm G}_X(s)+\chi(s)\overline{P^{\rm G}_X(s)}$, built from the smoothed Euler product $P^{\rm G}_X$, ..." and "$\Re\bigl(e^{i\vartheta(t)}P^{\rm G}_X(\frac12+it)\bigr)$", "$\pi\widetilde S_X(t)=\Im\log P^{\rm G}_X(\frac12+it)$".

N5 [reference] L1998: "($|\delta_k|\le C_{10}$, Theorem~\CGref{thm:known_basic})" — thm:known_basic does not bound delta_k; C_10 is defined from eq:BW_pointwise (table L671, L1870). Fix: "($|\delta_k|\le C_{10}$, \CGeqref{eq:BW_pointwise})".

N6 [table] L656: "$y_0$, $w_T$ ... (Corollary~\CGref{cor:dichotomy})" — neither occurs in cor:dichotomy; y_0 is in Remark korolev(a)/cor:fixed_cutoff (L917,1055), w_T in cor:power_cutoff (L1068). Fix: "(Corollaries~\CGref{cor:fixed_cutoff} and \CGref{cor:power_cutoff})".

N7 [table] L674: six symbols, five meanings: "$\mathsf M$, $\mathsf P$, $\mathsf F$, $\mathsf s$, $\mathsf W$, $\mathsf y$ & ...; $g^{4r}$ (Lemma sampling_rho); window and scale" — \mathsf s (bump, L1225) has no entry; also \mathsf F has a second meaning in the statement of Lemma midpoint_rule (L2207). Fix: "...; $g^{4r}$ (Lemma~\CGref{lem:sampling_rho}); bump function, window and scale (Lemma~\CGref{lem:maximal_primes})" and add row "$\mathsf F$, $x_k^{\mathsf F}$, $\mathsf c$, $\mathrm{sw}$ & monotone model, its level points, staircase, sawtooth $\lfloor v+\frac12\rfloor-v$ (Lemma~\CGref{lem:midpoint_rule})".

N8 [table] L640: "$\Psi_j$ & sawtooth polynomial" — Psi_j is the unit-interval mean of x^{2j} (L940, L1005), not periodic; the sawtooth is sw (L2207). Fix: "$\Psi_j$, $\kappa_j$ & mean of $x^{2j}$ over $[u-\frac12,u+\frac12]$ \CGeqref{eq:Psi_def}; ...".

N9 [cosmetic, abstract] L336: "(A) ... $\mathcal G(u_k+\frac12)-\mathcal G(u_k-\frac12)$ ... $g(N-F)$, where $\mathcal G'=g$, for every continuous $g$" — body uses \mathfrak g,\mathfrak G (L505, 657, 967); plain g = Gram points. Fix: \mathfrak G, \mathfrak g there.

N10 [cosmetic] plain g as a function: L1398-1404 (g=\mathcal M\mathfrak h), L1634-1646 (statement of Lemma sampling_rho, g=\mathcal M(\varphi^\sharp S'_X)), L1662 ("with $g^8$"), L2011-2013, L1240, L1926 (g_s), L2214; table L619 reserves g_m for Gram points and L677 uses \mathsf g_j. Fix: \mathsf g in Lemmas transport/sampling_rho, L1662 "$\mathsf g_1^8$", L2011/2013, table L674 "$\mathsf g^{4r}$".

N11 [cosmetic] L790: "$S_1(t)=\int_0^tS(y)\,dy=O(\log t)$" is never used and S_1 reads as S_X at X=1. Fix: delete "; and $S_1(t)=\int_0^tS(y)\,dy=O(\log t)$" (and drop \S9.12/Littlewood if only for that).

N12 [cosmetic] Fujii's parameter $a_2$ (L643,822,828,840) collides with the coefficient a_n at n=2. Fix: $a_{\rm F}$ throughout (matches x_F, kappa_F).

N13 [cosmetic] L2125 (Remark envelope_inputs(a)): "Yang's lines $\sigma_j=1-j/(2^j-2)$" right after Thm envelope defines sigma_j=l_j-k_j (L2078). Fix: "Yang's lines $\sigma=1-j/(2^j-2)$".

N14 [cosmetic] L2125 "$C_L$", L2278 "$C_{30}$", "$2\pi C_\infty$": plain C reads as the absolute constants C_j; envelope values are \mathsf C_J. Fix: \mathsf C_L, \mathsf C_{30}, \mathsf C_\infty.

N15 [cosmetic] L2107: "\Delta_{\sigma=\sigma^\sharp}^{1/2}\arg" although L1705 says Delta_k is reserved for the Gram displacement. Fix: "\bigl[\arg((\sigma+iT-1)\zeta(\sigma+iT))\bigr]_{\sigma=\sigma^\sharp}^{1/2}" (both terms).

N16 [cosmetic] L1376, 1556, 1561, 1564: derivative order nu in {1,2} vs nu(gamma) multiplicity (table L616, L1032). Fix: \iota in place of \nu there.

N17 [cosmetic] L537, 2139, 2141, 2148: index i in "u_{k+i}=u_k+i" next to the imaginary unit (L2149 "1-\beta+i\gamma"). Fix: index h: "u_{k+h}=u_k+h", "\sum_{h=0}^{m-1}(2u_{k+h})^{2j}".

N18 [cosmetic] L524 intro uses "$\eta T$, $\eta\le1$", "$(1+\log\frac1c)^2+\eta$"; Prop tolerance and table use \eta_{\rm reg}. Fix: \eta_{\rm reg} in L524.

N19 [cosmetic] L551: "outside a proportion $\ll(1+\log(1/c))/A^2$ of the zeros it is at most $A$" — A is the set of prime powers. Fix: \lambda/\lambda^2.

N20 [cosmetic, before definition] L1098 (proof of prop:rounding) uses V, E_X, eq:J_asymptotic, eq:R_fourth defined at L1116/1170-1183. Fix: add "with $V$ as in \CGeqref{eq:D_def} and $E_X=S-S_X$" after "$E=E_X+\varpi/\pi$". Likewise L1507 uses \|\cdot\|_{2,\IT} defined at L1523: add "($\|a\|_{2,I}=\langle a_k^2\rangle_I^{1/2}$)".

N21 [cosmetic] L671 and L1870: "(\CGeqref{eq:BW_pointwise})" prints double parentheses (\eqref adds them). Fix: drop the outer ( ).

N22 [cosmetic] L1630: "the number of pairs $(j,k)$ with $|x^{(1)}_j-x^{(1)}_k|\le b$" — lemma uses (k,l); j is the step index in this section. Fix: "$(k,l)$ with $|x^{(1)}_l-x^{(1)}_k|\le b$".

N23 [cosmetic] L1416: "$d_k=r_k(X)-u_k(X)$" collides with gaps d_{j,k}, d_{0,k} (table L676). Fix: rename to $\varepsilon_k$ in L1416 (4 occurrences).

N24 [cosmetic] L2238: "By \CGeqref{eq:intro_SX} and $\arg(1-w)=-\Im\sum_{m\ge1}w^m/m$ for $|w|<1$, $S_X(t)=\ldots$" — plain w beside \mathsf w of this section, and the expansion is already eq:SX_def. Fix: "By \CGeqref{eq:SX_def}, $S_X(t)=\ldots$".

N25 [cosmetic] L2207-2214 Lemma midpoint_rule uses \phi for the test function (table: \varphi cutoff, \psi test function); also \phi in L1922 and L2148 with other meanings. Fix: \psi in Lemma midpoint_rule and L2233 "with $\psi=f_z$".

N26 [cosmetic] L386, 440, 441, 476, 477, 2267: "first $N$ primes", "fixed $N$", "$p_N$" — N is the counting function. Fix: "first $K$ primes", "$X=p_K$", "fixed $K$".

N27 [cosmetic] L1679 "\chi''_{j,k}" with no \chi'. Fix: \tilde\chi_{j,k}.

N28 [table omissions] statement-level symbols not in List of symbols: Q_{2j} (eq:Q_def), N_0^s, P_X, f_z, \zeta_{\mathsf r}/\zeta_\tau, \mathsf A, \mathsf H (Thm multiplicity_all), \upsilon_m, (\mathsf p_m,\mathsf q_m), \sigma_j, \mathcal I'_T, \mathcal I_T^{\rm blk}, x^\uparrow_k, X_k^{\rm loc}, c_*, c_{\rm rd}. Attribution slips: \mathfrak b_T,\mathcal U_k first defined in proof of Lemma maximal_primes (L1240), not Lemma transport (L659); \mathfrak s_T first in Thm known_selberg_clt (L876), not Remark korolev (L632).

CHECKED: every \CGref/\CGeqref target exists (no missing labels, no duplicates); all Theorem/Lemma/Proposition/Corollary/Remark/Section/Table words (incl. 2nd/3rd refs in lists and ranges) match target environment; \CGeqref only to equations, \CGref never to equations; all above/below/next/previous references point the right way.
CHECKED: H_j=2log(1/c_j), cutoff_law, H_2=log H_1, c_1,c_2 consistent across Thm second_step, Prop deformation, eq:cutoff_law, table L667; kappa_j vs s_T normalization; Psi_1, Psi_2 coefficients; 7/240, 4/3-4Q_2 and 1-16Q_4+8Q_2-7/15; A_reg and 3/4^{4/3}; constants chain in Thm tails and induction claim; s_k and delta_k bounds in Remark korolev(b); Y_0=Y_2, x_F, kappa_F; Omega, \upsilon, \varkappa, \varrho, \rho, \mathfrak a, \mathfrak k, \mathcal Q vs \mathbf Q vs Q_{2j}, \mathsf r_k vs r_k(X), \mathcal H_X vs H_j/H^*, T_0 dependence (explicit wherever non-absolute).
