# Constants for the correct index of the zeros (2026-10-20, Claude)

Author's request (chat): find out how far the constants of Paper I can be pushed so that the corrected
count gives the correct index to most zeros. Not for the manuscript; no version is created.

Training indices only (k <= 1 400 736); the test set is untouched. Zeros are read only to evaluate.

## 1. What is proved (from v11, nothing new)

* Correct index of gamma_k for the corrected count F_X = N0 + S_X means |u_k(X)| < 1/2 (v11, line 349).
* Theorem A, (eq:identity_quadratic): sum_k u_k^2 = int (N - F_X)^2 F_X' dt - (k2-k1-1)/12 - boundary.
  Hence, with Q_2(T,X) = (1/#I_T) int_{I_T} (N - F_X)^2 dF_X,
      <u^2>_{I_T} = Q_2 - 1/12 + O(1/#I_T),
      #{k in I_T : |u_k(X)| >= 1/2} / #I_T  <=  4 <u^2>  =  4 Q_2 - 1/3 + O(1/#I_T).
* So the index question at the true ordinates needs only Theorem B at one cutoff. The constants of the
  iteration (H^*, C_*, C_5, the exponent 1/(160 r)) do not enter it. They matter only for the
  zeta-free points x_k^(m) (identification of gamma_k as the nearest zero to x_k^(m)).

## 2. Numerical results (programs and outputs in this folder)

`u_defect_scan.py` -> `u_defect_scan.{txt,json}`; window T = 408 392, #I_T = 745 418, k in [655 315, 1 400 732].

| c | X = T^c | <u^2> | a log(1/c) | K_emp = <u^2> - a log(1/c) | frac |u| >= 1/2 |
|---|---|---|---|---|---|
| 1/2 | 639 | 0.01213 | 0.03512 | -0.02299 | 0.00065 |
| 1/4 | 25.3 | 0.03274 | 0.07023 | -0.03749 | 0.00531 |
| 1/8 | 5.0 | 0.05440 | 0.10535 | -0.05095 | 0.02888 |
| plain clock s_k | - | 0.11172 | a loglog T = 0.12963 | -0.01791 | 0.13810 |

(a = 1/(2 pi^2).) The constant of Theorem B is negative at these heights. Q_2 = <u^2> + 1/12 = 0.0955 at c = 1/2,
against the threshold 1/3 for the Chebyshev bound to say anything.

`u_defect_T_dependence.py` -> `.txt/.json`: dyadic windows T = 12 500 ... 408 392. K_emp(1/2) goes from -0.0244 to -0.0230,
K_emp(1/4) from -0.0386 to -0.0375: slow drift, no sign change in the range.

Zeta-free fixed-point steps x <- x - (F_X(x) - k + 1/2)/L(x) from tau_k, fixed X = T^c:
* c = 1/4 (9 primes): after 4 steps <eps^2> = 0.0275 (index units), and the nearest ordinate to x_k is gamma_k
  for all 745 418 indices (0 failures at steps 4, 5, 6; 41 790 failures for tau_k).
* c = 1/2 (115 primes): best after one step (12 414 failures); further steps do not contract (16 563 at step 6),
  consistent with sup |S_X'| >> L for X = T^{1/2}.

## 3. Corrections to the chat analysis of 2026-10-20

* The final mean square of the iteration is governed by H_{m*} = 2 log(1/c_{m*}), not by H^*. Choosing the
  penultimate cutoff with H_{m*-1} = H^* (allowed: every hypothesis of thm:uniform_iteration is an upper bound on c_j
  or a lower bound on H_j) gives H_{m*} = (9/8) log H^* + 2 log(1/C_*), about 13 + 2 log(1/C_*) for H^* = 102 400.
* The floor H^* >= 4 * 160^2 comes from tying c_j to H_{j-1}; with c_j = min(C_* H_{j-1}^{-9/16}, 1/(160 r_j)) the
  length condition costs H_j >= 2 log(160 r_j), and only H^* >= 4 C_6 remains.
* Neither point is needed for the index question (section 1).

## 4. What would have to be proved (open)

The single inequality that gives a positive proportion of correctly indexed ordinates is an explicit bound
    Q_2(T, T^c) <= 1/3 - eta   for T >= T_0, at one fixed c <= 1/2,
i.e. an explicit constant in the mean square of N - F_X over t (weighted by dF_X). Measured: Q_2 = 0.0955 at c = 1/2.
The v11 proof cannot give it: it splits at Y_0 = T^{1/160} and bounds cross terms by Cauchy-Schwarz; the piece
S - S^pr_{Y_0} alone has mean square of order a (log 160 + const), comparable to 1/3. An asymptotic formula for
int (S - S_X)^2 with explicit constant is needed instead. Candidate source to check (not in LIBRARY TOTAL, not read):
D. A. Goldston, On the function S(T) in the theory of the Riemann zeta-function, J. Number Theory (1987),
doi:10.1016/0022-314X(87)90059-X; it is expected to involve RH and pair correlation, unverified.

A fixed c keeps the proportion of misindexed zeros positive (Gaussian-like tails of S - S_X with bounded variance):
at c = 1/4 the Gaussian prediction 2 Phi(-0.5/sqrt(0.0327)) = 0.0058 matches the measured 0.0053. "Almost all" needs c -> 1,
outside X <= T^{1/2}.
