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
