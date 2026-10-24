# Reproducibility status — Version 12

All 17 data arrays and all eight figures are inherited byte for byte from
Version 11. Their comparison hashes are recorded in
`outputs/v12_inherited_assets_verified.json`.

The new mathematical audit is deterministic except for elapsed-time reporting.
It uses the supplied arithmetic arrays and exact finite words; there is no
random sampling. The finite word range is every balanced word of length
2, 4, ..., 16, giving 17,576 words.

The last balanced physical prefix in the stored range is n=973,828,
with Q=592,020 and J=296,010. At that prefix, the audit checks the two-cut
identity for r=0,...,64 and the weighted area identities in both clocks:

- Prime-displacement-weighted physical area: 209,113,497,735,172.
- Prime-displacement-weighted ordinal area: 127,129,010,723,267.
- Unweighted ordinal area V(0): 55,062,648.

These distinct values also check that physical displacement, ordinal
displacement and prime displacement have not been conflated.

For n=1,...,40, fraction-free elimination independently checks the explicit
prime-entry determinants for T and SS, and the classical Redheffer determinant
for M. Every matrix entry is checked against zero or signed primes.

The first five positive zeta-zero ordinates are evaluated using mpmath at
60-decimal working precision. Laurent limits verify the explicit B and
P_delta formulae. No finite coefficient polynomial is used to infer poles
of the full delta function.

The analytic theorems are justified by the written proofs. In particular,
finite tests are not substitutes for normal convergence, the energy
equivalence, or the missing arithmetic tail estimate.
