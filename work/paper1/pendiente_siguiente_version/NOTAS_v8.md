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

## External review of the withdrawn v8 (2026-10-19) -- revision_externa_v8_2026-10-19.md

Checked against the v7 source (the passages are unchanged in v7 and in the pending patch):
1. lem:sampling_rho (v7 l.1473): "8 pi r c (1+o(1)) <= 7" is not uniform in r for small X.
   CONFIRMED. Use 4 r b (1+log X) <= 2 pi (1+1/log 2) log T/log(3T) < 16, factor 8 -> 17.
2. lem:higher_moments (v7 ~l.1390): the m=2 term carries ((2r)!)^{1/4r} <= sqrt(2r), so
   C sqrt(r) T^{1/4r}, not O(T^{1/4r}). CONFIRMED; absorbed by C r^2.
3. lem:zero_pairs (v7 l.1557): h = min(2Rb,T) may be < 1, estimate stated for h >= 1.
   CONFIRMED. Fix: case 2Rb >= T separately; else h = max(1, 2Rb) <= 4Rb.
4. prop:deformation (v7 l.1532): remainder written T^{c_1-1}; lem:second_identity gives
   T^{c_j-1}, j=2 -> T^{c_2-1}. CONFIRMED. Quantify: ||(d2-d0)/d0||_4 << c_2 + c_1 c_2 + T^{-1/2} log^3 T.
5. cor:sorted_clock (v7 l.1684): "defined for every k with tau_k >= T_0" too broad. Restrict to
   J_T = {k : T/2 <= tau_k <= 3T}. Accept.
6. v7 l.1700 ("fixed final cutoff"): replace by the reviewer's sentence (one-step clock only).
Reviewer's last caveat (Ivic-Korolev omits k^{2k}): already checked against Korolev 2016 original,
Lemma 3.13, p. S126 (uploaded PDF).

## Theorem E: the disc and the Lindelof value (2026-10-19)

- Scan over the Bellotti-Wong disc (1 < sigma_o < rho, general rho, not only rho -> 1):
  envelope/envelope_disc_scan.{py,txt}. The infimum is at the corner (sigma_o, rho) -> (1,1),
  i.e. v7's choice; increasing rho only worsens (TTY25 profile: rho=1.1 gives 0.6307).
- v7 Remark (c) ("Backlund's method with a disc cannot give less, whatever the exponents") must
  say: with a single disc of Theorem known_backlund. Under LH the truth is S(t) = o(log t)
  (Titchmarsh-Heath-Brown, Thm 13.6(A), p. 333, Littlewood; proof uses the zeros near 1/2+iT),
  so 2 pi * 0.07863 = 0.494 is the floor of the one-disc method, not a value of limsup|S|/log t
  under LH. State this in v8.
