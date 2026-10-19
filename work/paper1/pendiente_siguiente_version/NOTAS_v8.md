# Pending for Paper I v8 (not ordered yet)

## Author's instruction (2026-10-19): stress that the bounds do not use zeta
In every comparison table (tab:antecedents, tab:status, the Theorem E comparison):
add a column "What the construction evaluates" separating
- the clocks of Theorems B-D (only k, tau_k, primes p <= X: no evaluation of zeta, Z, theta,
  Riemann-Siegel, and no zero) from
- the antecedents that evaluate zeta or use zeros (certified zero computations,
  Gram/Turing methods, Odlyzko-type data, LeClair-type equations solved numerically).
Keep the distinction honest: the *proofs* use theorems about zeta (Selberg, Fujii, Korolev,
Montgomery-Vaughan, exponent pairs); the *constructed points* do not use zeta. Theorem E is a bound
for S(t) itself (a property of zeta), obtained without computing zeta or any zero.

## Mathematical changes pending (see patch_pending_claude.py)
- Fujii 1974 p. 225: non-strict hypotheses; Fujii 1981 corrections; (alpha'); Korolev 2016 Lemma 3.13 (c0 k)^{2k}.

## Proposed before v8 (author to decide)
1. Theorem E: optimise the exponent profile with all published inputs (Trudgian-Yang pairs,
   B-process, Vinogradov-Korobov near sigma=1); give the Lindelof ceiling 2*pi*0.07863.
2. Tails of the defect: Gaussian then exponential via Korolev's (Ck)^{2k}.
3. CLT for u_k(T^c) at the ordinates as c -> 0 (Theorem A + Selberg-Tsang), and a positive
   proportion of zeros misindexed by rounding.
4. Literature search on 1 and 3; GPT review of the new proofs before v8.
