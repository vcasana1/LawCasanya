# Revision 3: changed passages v13->v14 (audit of hunks)

## F1 (abstract, v14 line 336) -- notation half-converted
Snippet: "turns sums of $\mathfrak G(u_k+\frac12)-\mathfrak G(u_k-\frac12)$ ... into $dF$-integrals of $g(N-F)$, where $\mathcal G'=g$, for every continuous $g$"
Wrong: hunk changed \mathcal G -> \mathfrak G in the sum but left "\mathcal G'=g" and plain g; body (l.505, 970ff) uses \mathfrak g with primitive \mathfrak G, and g is the maximal function elsewhere (Lemma sampling_rho).
Fix: "into $dF$-integrals of $\mathfrak g(N-F)$, where $\mathfrak G'=\mathfrak g$, for every continuous $\mathfrak g$"

## F2 (Remark envelope_inputs (c), v14 line 2128) -- C_L half-converted
Snippet: "$\mathsf C_L=(\frac{\sqrt3}2-\frac\pi6)/(2\pi\log2)=0.07862527\ldots$, that is $2\pi C_L=..."
Fix: "that is $2\pi\mathsf C_L=(\frac{\sqrt3}2-\frac\pi6)/\log2=0.49401719\ldots$". Values match envelope_best_profile_v10.txt (0.07862527909..., 0.494017198...).

## F3 (Lemma higher_moments statement, v14 l.1557) -- endpoint inconsistent with eq:D_def
Snippet: "$V=\sum_{X<p\le Y_{2r}}p^{-1}$, $Y_{2r}=T^{1/(160r)}$ (the sum \CGeqref{eq:D_def} with $Y_{2r}$ in place of $Y_0$)"
Wrong: eq:D_def sums over $\mathcal J=(X,Y_0)$ (open at $Y_0$, matching $S^{\rm pr}_{Y_0}$ over $p<Y_0$, l.1122-1124); the parenthesis claims identity with a closed sum. Harmless numerically, but the statement contradicts itself.
Fix: "$V=\sum_{X<p<Y_{2r}}p^{-1}$".

## F4 (Remark envelope_inputs (b), v14 l.2128) -- 10^{-15} claim not implied by the stated reason; not in cited output
Snippet: "except for $1-\sigma<3\cdot10^{-7}$, where $\mathfrak e_{\mathcal P}<10^{-10}$, and it would change $\mathsf C_{\mathcal P}$ by less than $10^{-15}$"
Wrong: via the reflection $\mathfrak e(\sigma)=\frac12-\sigma+\mathfrak e(1-\sigma)$ a change on $1-\sigma<a$ reappears near $\sigma=0$ with weight $(2\sigma)^{-1/2}$; with only $\mathfrak e_{\mathcal P}<10^{-10}$ one gets $10^{-10}\sqrt{2a}/(2\pi\log2)\approx1.8\cdot10^{-14}>10^{-15}$. The claim is true only using convexity (chord from the crossing point, $\mathfrak e_{\mathcal P}(\sigma)\le2.7\cdot10^{-4}(1-\sigma)$ there, giving ~5e-18). Also: envelope_best_profile_v10.txt contains no Heath-Brown-bound comparison (3e-7, 1e-10, 1e-15 are not in that output).
Fix: "where $\mathfrak e_{\mathcal P}(\sigma)\le3\cdot10^{-4}(1-\sigma)$ (convexity), and it would change ..." and cite the program/output that actually computes the crossing, or weaken to "by less than $10^{-13}$".

## F5 (Cor sorted_clock proof, v14 l.1873) vs new hypothesis of Lemma second_identity ($\tau_k\ge T-1$)
Snippet: "only the localization of the points proved below is used, and it is applied on $\mathcal I_T^{\rm blk}$"
Wrong: the localization is Lemma second_identity, now restricted to $\tau_k\ge T-1$; $\mathcal I_T^{\rm blk}$ contains $T/2\le\tau_k<T-1$. The actual application below is only to $k\in\mathcal I_T^\tau$ ($\tau_k\ge T$), which is fine.
Fix: "and it is used only for $k\in\mathcal I_T^\tau$, where $\tau_k\ge T$". All other uses checked: Prop deformation (k, k+1 with k in I_T: tau_k >= T-1 by |delta_k|<=1, l.1257), Thm multiplicity_all (k in I_T), sorted clock (k in I_T^tau) -- hypothesis satisfied.

## F6 (minor, intro Theorem G, l.548) -- $t_1$, $k_0$ used before definition
Snippet: "and the choices of $t_1$ and of $\mathsf r_k$, $k<k_0$."
Fix: "and the choices of the starting height and of the finitely many $\mathsf r_k$ below it (Theorem~\CGref{thm:euler_product})."

## F7 (minor notation, l.1776) -- index $J$
$J$ (first index with $L_J<K_\star$) reuses the letter of $J_{k,m}$ (same section, l.1612), $p_1<\dots<p_J$ (l.1226) and $\mathfrak e_J,\mathsf C_J$ (Thm E). Local, but avoidable. Fix: $J\to j_\circ$ (grepped: unused). Other new symbols checked: C_4, C_{11}, K_\star, K_{\rm M}, K_1, K_2 (vs K, K^4 of Sec. 9: different, local), Z (local; Z std normal l.920, Z_j l.1943: no conflict in scope), L_j (vs \lL=\mathcal L and \mathsf L_T: distinct glyphs; do NOT use \ell_j, taken by \ell_n=log n), \tilde\chi, \varepsilon_k (only l.1419), N^{\rm s}_{1/2}, P^{\rm G}_X, \Omega, \eta_{\rm reg}: no clash.

CHECKED: higher_moments second-bound chain (l.1564): integral bound, division by #I_T, Z>=1, K_1=4+4pi sqrt(C_d), K_2=9pi C_b+1, 2^{2r}K_1+K_2<=(2(K_1+K_2))^{2r}, constant 2(5+4pi sqrt C_d+9pi C_b)C -- correct.
CHECKED: Thm tails proof V via Mertens with Y_{2r} (l.1584): log(1/(160rc))+O(1), absolute, 160rc<=1 -- correct.
CHECKED: m^* paragraph (l.1776): H_j<=(9/8)L_j+K_star (uses K_star<=L_{j-1}), (9/8)log(17/8)=0.848<1, H_J<(17/8)K_star, H_{j+1}<=H_j/4 when H_{j+1}>=H^* is exactly what "the three conditions" proves (H_{j-1}>=4H_j whenever H_j>=H^*), count, lower bound -- correct; no circularity.
CHECKED: "log H_{j-1}<=H_j for H_{j-1}>=1" (l.1772); H^*>=max(4C_6,160^2) suffices (l.1819).
CHECKED: K_M absorption (l.1797): 1+V<=log(1/c_j)+K_M=H_j/2+K_M<=(K_M+1)H_j for H_j>=1; C fixed before C_star,H^*; H_j>=H^* at all levels j<=m-1 where the lemma is used -- correct, non-circular.
CHECKED: range 1<=j<m^* plus transport-only at j=m^* (l.1801) consistent with last step.
CHECKED: C_4 choice (l.1819); C_11=8pi^2(H^*/(4pi^2)+C_4(1+sqrt H^*)) and L(tau_k)^{-2}<=8pi^2/log^2T (l.1823); C_11+1 in Cor sorted_clock.
CHECKED: base X=2 admissibility (l.1795).
CHECKED: sampling_rho constants 12r, 48, 49, ||g'|| bound (l.1649).
CHECKED: r=4 case (l.1719).
CHECKED: second_identity: tilde chi algebra, sign, factor L(tau)/L(x), j=1 remark, both points >= T-T^{1/2} (l.1682-1694).
CHECKED: Prop recursion new hypothesis (l.1529), satisfied in Thm second_step and Thm uniform_iteration.
CHECKED: multiplicity covering [T-1,2T+1] (l.1625); "almost every t" (l.1616); (k,l) (l.1633); (T+1)^{1/4} (l.1741); second step r=2 admissibility (l.1665).
CHECKED: V_pm>=1/X_+ (l.1234).
CHECKED: Remark (b)/(c) numbers vs envelope_best_profile_v10.txt: unchanged C_P with ABA images, 0.6061342, 0.6060224, C_L, 2pi C_L, 0.6083074; profile>=0 argument.
CHECKED: hunks 336 (except F1), 363, 377, 385, 387, 475, 486, 524, 531, 537, 539, 640, 656, 671, 674, 719, 793 (S_1 removed; no remaining use), 1101, 1107, 1419, 1510, 1571, 1622, 1868, 1873, 1875, 2001, 2124, 2134-2173, 2266, 2281.
