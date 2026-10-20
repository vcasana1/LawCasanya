# Route via the defect: proportion of simple zeros on the line from Theorems A and B (2026-10-20, Claude)

Not for a manuscript version. Author's request: continue the route that uses most of his results.

## Lemma (derived here)
Let F be any real function and u_k = k - 1/2 - F(gamma_k), ordinates counted with multiplicity.
If an ordinate has multiplicity m >= 2 (a multiple zero or an off-line pair beta+i gamma, 1-beta+i gamma),
its indices k,...,k+m-1 have u_{k+j} = u_k + j, so sum_j u_{k+j}^2 >= m(m^2-1)/12 >= m/4.
An ordinate of multiplicity 1 carries a zero that is simple and on the line.
Hence, for the window I_T (boundary groups O(log T)):
    N_0^s(T,2T) >= #I_T - 4 sum_{k in I_T} u_k^2 - O(log T)
and, with Theorem A (identity_quadratic), <u^2> = Q_2 - 1/12 + O(1/#I_T), Q_2 = (1/#I_T) int (N-F)^2 dF:
    N_0^s(T,2T) / N(T,2T) >= 4/3 - 4 Q_2 - o(1)  =  1 - 4 <u_k(X)^2> - o(1).
Unconditional; no Z, no clock, no iteration. Novelty not searched (same family as Montgomery's integrality step).

## Thresholds and measured values (work/paper1/constantes_2026-10-20)
* positive proportion: <u^2> < 1/4; Conrey 2/5: < 0.15; PRZZ 5/12: < 0.1458;
  current record 0.6735 (arXiv:2610.08965; 0.6725 in Alpöge-Furman arXiv:2608.13637, Lamzouri arXiv:2609.02882): < 0.0816.
* measured at T = 408 392: <u^2> = 0.0121 (c = 1/2), i.e. the certificate would read 0.95 if <u^2> could be proved
  at its true size. Theorem B: <u^2> <= a log(1/c) + C(1+sqrt(log(1/c))), a log 2 = 0.0351; record needs C <= 0.025.

## Where it meets the known barrier (heuristic, to be derived)
Via Theorem A the triple-correlation sum sum_gamma u_gamma^2 becomes the t-integral of (S - S_X)^2, a pair-correlation
quantity. Expected shape: Q_2 = a [ log(1/c) + int_1^infty F(alpha) alpha^{-2} d alpha + const ], with the prime part
(alpha <= 1, unconditional: Montgomery-Vaughan / BGSTB 2024 form factor for complex zeros) giving a log(1/c), and the
rest needing F beyond support 1: the barrier stated in Alpöge-Furman §7.2(a). Measured rest: Q_2 - a log 2 = 0.060;
the record needs an upper bound <= 0.13 for it. Next step: derive this formula with explicit constants.

Sources read today (alphaXiv): arXiv:2608.13637 (Alpöge-Furman, argument by Claude), arXiv:2609.02882 (Lamzouri).
Not in LIBRARY TOTAL.

## Continuation: Q_2 in terms of Montgomery's F (heuristic derivation, 2026-10-20 later)
n(t) = sum_gamma delta(t-gamma) - L(t) has S' = n (N = N0 + S), so S has spectrum n_hat/(i omega). Montgomery's F
is the normalised power spectrum of the ordinates at omega = alpha log T. Parseval gives
    (1/T) int_T^{2T} (S - S_X)^2 dt  ~  (1/2 pi^2) int_c^infty F(alpha) alpha^{-2} d alpha
(S_X removes the prime spectrum alpha < c), and F(alpha) = alpha + o(1) on [c,1] gives
    Q_2 ~ a [ log(1/c) + B ],   B := int_1^infty F(alpha) alpha^{-2} d alpha  (B = 1 under the pair correlation conj.),
plus the dF-cross term (1/#I_T) int (N-F_X)^2 S_X' dt (zero under independence of prime ranges). The structure
agrees with what I recall of Goldston's mean square of S (JNT 1987, under RH; not verified in the source).
Measured B_emp = Q_2/a - log(1/c) at T = 408 392: 1.19 (c=1/2), 0.99 (c=1/3), 0.91 (c=1/4).
Certificate at c = 1/2:  N_0^s/N >= 1.1928 - 0.2026 B - (cross term) - o(1).
  B = 1 (PCC) -> 0.990;  B_emp -> 0.952;  record 0.6735 <=> B < 2.563;  positive proportion <=> B < 5.887.
Unconditional decomposition (derived): with R = S - S_x^pr (x in Selberg's range, Lemma selberg_uniform) and
W = S_X - S_x, Var(S - S_X) = Var R - Var W + 2 Delta_off, where Delta_off comes only from off-line pairs:
for a pair beta = 1/2 +- delta, p^{-1/2}(p^rho + p^{rho'}) - 2 p^{i gamma} = p^{i gamma} (p^{delta/2} - p^{-delta/2})^2,
so the ordinate sums at prime frequencies equal Landau-Gonek's sums minus sum_pairs p^{i gamma} 4 sinh^2(delta log p / 2).
Var R needs an explicit Selberg-Fujii constant; Delta_off needs zero density near the line.

## Correction (author: a proportion of off-line zeros does not locate them)
* The bootstrap "proportion -> Delta_off" does not work: Delta_off depends on the ordinates of the pairs through p^{i gamma}.
  The absolute-value bound also fails (weights ~ 1/(sqrt p log p) give a factor sqrt X): the phases are essential.
* Exact form (derived): Delta_off = sum_pairs [P(rho) + P(1-conj rho) - 2 P(1/2 + i gamma)], P(s) = sum_{x<p<=X} b_p p^{s-1/2},
  b_p of order 1/(sqrt p log p): a horizontal second difference of a prime Dirichlet polynomial at each off-line pair.
* No location needed: Cauchy-Schwarz + mean value of |P|^2 over zeros (zero-density technology), with weights X^{2(beta-1/2)}.
  Convergence needs N(1/2+u, T) << T^{1-Au} log T with A > 2c. Selberg's A = 1/4 allows c < 1/8; then sum |b_p|^2 << 1/log x
  suggests Delta_off = o(#I_T) (outline, to be written).
* At c = 1/8 with B = 1 the certificate is 4/3 - 0.2026 (log 8 + 1) = 0.709 (record 0.6735 needs B < 1.18).
  Stronger densities near the line (mollifier methods; not checked, Conrey 1989 in LIBRARY TOTAL has no text layer) would allow larger c.

## Explicit bound for B: status (author asked to extract it)
* The only unconditional source of a bound for B here is Selberg's approximation plus Selberg's density theorem
  (v11 Lemma selberg_uniform, via Fujii 1974). Needed: Var(S - S^pr_x) <= a (log(1/c_x) + 2.56); with x = T^{1/80}
  that is <= 0.352 (true value about 0.27 if B = 1); with the density condition c < 1/8 the record needs B < 1.18,
  i.e. Var R <= 0.282.
* The closest explicit version of that machinery found: Hiary-Zhao, arXiv:2512.14907 (2025), Selberg made explicit for
  the family of Dirichlet L-functions mod q: first moment of S bounded by 982; their mean-square constant D is larger.
  Pointwise explicit Selberg for zeta: Karatsuba-Korolev (Russian Math. Surveys 2005), cited there, not read.
* So the explicit B obtainable by this method is orders of magnitude above 2.56: true but useless. Not computed.

## Q_2 as one quantity (q2_single_quantity.py, T = 100 000, training heights)
* dF_X = (L + S_X') dt is the zero density predicted by the primes; Q_2 is the mean of R_X^2 under it, equal by Theorem A
  to the zero-side mean <R_X(gamma)^2> + 1/12 (measured: t-side 0.09498, zero side 0.09497 at c = 1/2).
* Split: V_L = (1/M) int E^2 L = 0.0790, C_X = (1/M) int E^2 S_X' = +0.0159 (c = 1/2; corr(E^2, S_X') = +0.31);
  c = 1/4: 0.1106 and +0.0042. The weighting does not cancel: it adds 17 % at c = 1/2, 4 % at c = 1/4.
* Rigorous conditional form (no density condition needed, c = 1/2 allowed by Theorem B's range):
  if limsup Q_2(T, T^{1/2}) <= a (log 2 + b), then liminf N_0^s/N >= 4/3 - (2/pi^2)(log 2 + b) = 1.1928 - 0.2026 b.
  b includes C_X. Measured b = 1.19 (0.31 of it from C_X).

## Comparison with Lamzouri (arXiv:2609.02882, Prop. 2.1) / Alpöge-Furman
* Both are integrality certificates. Per group of multiplicity m >= 2: ours charges 4 sum_j (u+j)^2 >= m(m^2-1)/3 >= m;
  theirs charges through m^2 >= 2m - 1 (and (m-1)(m-2) >= 0), flat charge 4 for multiple points and off-line pairs.
* Information used: theirs, the pair correlation with Fourier support in [-1,1] (known unconditionally, gives 2/3);
  ours, the weight alpha^{-2} on [c, infinity): the part [c,1] is known (log(1/c)), the part > 1 is b. With support <= 1 only,
  ours gives nothing; with b = 1 (pair correlation conjecture) it gives 0.99. Neither dominates.
* Same groups: at Lamzouri's extremal configuration (2/3 simple, 1/6 N on-line doubles or shallow off-line pairs) our lemma
  forces <u^2> >= 1/12, i.e. Q_2 >= 1/6, i.e. b >= 1/(6a) - log(1/c) = 2.597 (c = 1/2). So "b < 2.597" excludes their
  extremal configuration: the two inequalities see the same groups through different information.
* Joint problem (proposed, ADAPT of the Chirre-Goncalves-de Laat programme): minimise the simple-on-line proportion over
  configurations with F = Montgomery on [0,1] and Q_2 <= a(log(1/c) + b); expected to beat max of the two bounds.

## Joint extremal problem, computed (joint_extremal.py)
* Lamzouri's Prop. 2.1 holds for any support lambda; extended beyond lambda = 1/2 under H(b): int_1^inf F alpha^-2 <= b, F >= 0
  (tail bounded by 2b max_{[1,2lambda]} alpha^2 Q). Discretised SLSQP (n = 120): lambda = 1/2 gives 0.66964 vs exact 0.67250
  (under-optimised by 0.003).
* b:        1.0     1.5     2.0     2.597   3.0
  Lamzouri-extended: 0.718 (lambda=1.5, search edge)  0.675  0.674  0.674  0.673
  defect certificate (c = 1/2): 0.990  0.889  0.788  0.667  0.585
* The defect certificate dominates for b < 2.597; above, Lamzouri wins and gains only about 0.005 from the b-information.
  Combining the two inequalities as stated gives their maximum; a gain beyond it would need a joint inequality per group.
* Consistency: the defect certificate exceeds 1 for b < 0.95, so (under the Parseval heuristic) b >= 0.95 for zeta; measured 1.19.
