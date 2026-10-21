# v12->v13 regression audit (findings, B = prime_corrected_clock_v13.tex)

F1 (math, wrong index) B1716: "which need the case $r=2$ of the third bound of Lemma~\CGref{lem:higher_moments} ($X_2\le T^{1/8}$, ...)". $\|\mathsf g_2\|_{16}$ needs $\int|S'_{X_2}|^{16}$, i.e. $4r=16$, $r=4$ (hypothesis $X\le T^{1/(2r)}=T^{1/8}$); $r=2$ gives $L^8$ and $T^{1/4}$. Fix: "the case $r=4$ of the third bound of Lemma~\CGref{lem:higher_moments} ($X_2\le T^{1/8}$, true for $T\ge T_0$ since $c_2\to0$)".

F2 (leftover rename) B2278 Data availability: "encloses $C_{30}$ ... upper bound $2\pi C_\infty<0.6083074$". Fix: "$\mathsf C_{30}$", "$2\pi\mathsf C_\infty<0.6083074$".

F3 (constant inconsistency) B1561: "$\int_T^{2T}E_X^{2r}|S_X'|\le\mathcal E_{4r}^{1/2}C_{\rm d}T^{1/2}(1+\log X)$, $C_{\rm d}$ the constant of (SX_derivative)" but next lines use $\sqrt{C_{\rm d}}$ (correct: (SX_derivative) bounds $\int S_X'^2$). Fix: "$\int_T^{2T}E_X^{2r}|S_X'|\le\mathcal E_{4r}^{1/2}\sqrt{C_{\rm d}}\,T^{1/2}(1+\log X)$". Also K_1,K_2 undefined: add "with $K_1=2+2\pi\sqrt{C_{\rm d}}$, $K_2=9\pi C_{\rm b}+2$ (the term $2^{2r}K_1T^{-2r}\le1$ for $T\ge T_0$ is absorbed into $K_2$, and $(Cr^2)^{2r}$, $1\le(C(r^2+\sqrt{r(1+V)}))^{2r}$)". Final constant itself verified correct.

F4 (meaning change) B377: "and for D$'$, Corollary~\CGref{cor:local_clock} and Corollary~\CGref{cor:sorted_clock} over the window $T\le\tau_k<2T$" -- "also" dropped, so D' reads as window-only. Fix: "and for D$'$ also over the window $T\le\tau_k<2T$, over which Corollaries~\CGref{cor:local_clock} and \CGref{cor:sorted_clock} are stated".

F5 (abstract notation) B336: abstract still "$\mathcal G(u_k+\frac12)-\mathcal G(u_k-\frac12)$ ... $g(N-F)$, where $\mathcal G'=g$, for every continuous $g$"; intro/body/conclusions use $\mathfrak g,\mathfrak G$. Fix: "$\mathfrak G(u_k+\frac12)-\mathfrak G(u_k-\frac12)$ ... $\mathfrak g(N-F)$, where $\mathfrak G'=\mathfrak g$, for every continuous $\mathfrak g$".

F6 (README) README.md:49 under "Changes from v11.2": "Applied by `tools/patch_v13_claude.py` to a copy of the v11 (= v11.2) source." Fix: "`tools/patch_v12_claude.py`" (as in v12 README); heading "Changes from v11.2 to v12". README.md:262 "$O_{X_0,c}$ in (5.6)": eq:dichotomy is (5.3) in tips.tex ((5.6) is eq:D_second). Fix "(5.3)". v12->v13 section placed after v6->v7 (line 249); move to top of change log.

F7 (attribution) B1998 "($|\delta_k|\le C_{10}$, Theorem~\CGref{thm:known_basic})" vs B1870 and symbol row citing (BW_pointwise). Fix: "($|\delta_k|\le C_{10}$, \CGeqref{eq:BW_pointwise})".

F8 (scope) B1794 "$C'$ absolute since $H_j\ge H^*\ge1$": true only for $j<m^*$ (H_{m^*}<H^*); the one-step bound is stated for all j>=1. Fix: "...since $H_j\ge H^*\ge1$ for the indices $j\le m-1<m^*$ where it is used...".

F9 (grammar) B2203 "($|f_z(t)|\ll_K1$ for $0\le t\le1$, since $t^2+z^2\ne0$ there and $\ll_Kt^{-2}$ for $t\ge1$, ...)" Fix: "($|f_z(t)|\ll_K1$ for $0\le t\le1$, since $t^2+z^2\ne0$ there, and $|f_z(t)|\ll_Kt^{-2}$ for $t\ge1$, ...)".

F10 (wording) B599 "The letter $\mu$ is not used for the M\"obius function (...)": the Möbius function never occurs. Fix: "The letter $\mu$ alone is not used (the vectors $\boldsymbol\mu_\pm$ of Proposition~\CGref{prop:tolerance} are Lagrange multipliers)".

F11 (conclusions) B2263 "exceeds $\lambda$ on at most $2^{2-\sqrt{\lambda/C_8}}$ of the zeros" -> "on at most a proportion $2^{2-\sqrt{\lambda/C_8}}$ of the zeros" (as intro B518).

F12 (minor notation) B2125 Remark envelope_inputs keeps $C_L$ and bare $2\pi\mathsf C$; symbol table lacks $\mathrm{sw}$, $\mathcal I_T^{\rm blk}$ (both in statements). $\mathcal H_X$ vs Hilbert transform $\mathcal H$ (B887); $\mathsf r_k$ vs residual $r_k(X)$ — near-collisions, optional.

CHECKED: 2^{2r}K1+K2<=(2(K1+K2))^{2r}; final constant 2(4+2pi sqrt Cd+9pi Cb) valid with K1=2+2pi sqrt Cd, K2=9pi Cb+2
CHECKED: m=2 term of third bound (sum|eta'|^2<=(Cr)^{2r}, sum n|eta'|^2<=(Cr)^{2r}X^{2r}(1+log X)^{4r nu}<=...T)
CHECKED: Theorem E sigma_j<sigma_{j+1} induction, 13/110, 1-sigma_{j+1} formula
CHECKED: Theorem G admissibility (r_k>=t_1, MVT bound sigma_X/L(t_1), f_z difference O(|r-tau| tau^-3))
CHECKED: maximal-function continuity (Lemma 7.2); X_-=X_+; Chebyshev range; Lemma 8.7 remainder max(c_{j-1},c_j); tower remark vs induction (H_j>=C_6 4^{m-j} proved for 1<=j<=m-1, excess r^{3/4}); min_k L(tau_k); Prop 9.7(a) factor 8(1+eta)<=16; selberg_uniform sign; |omega|<pi; X_2<=T^{1/4} for sampling r=1
CHECKED: leftover grep (kappa_k, zeta_kappa, H_X, vartheta_m, kappa_0, C_{\mathcal P}, rho_k, psi sawtooth, S_X^{(nu)}, D_nu, J_T block, u_k=max, sum_{j,k}) clean except F2
CHECKED: abstract/intro/conclusions Theorem G notation; README numbering except (5.6)
