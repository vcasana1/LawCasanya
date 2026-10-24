# Version 11 audit

## Version 11 additions

1. Exact fixed-level crossing and return formulae separate the cases $h>0$,
   $h=0$, and $h<0$.
2. Complete negative excursions carry a positive prime-separation energy with
   the unconditional cubic lower bound `(H^3-H)/3`.
3. Replacing `p_j` by `1` or `j` gives exact positional and ordinal controls;
   the genuine prime block has asymptotic amplitude amplification `log(Q/2)`.
4. `code/v11_level_energy_entropy.py` verifies the new integer identities and
   excursion bounds through `N=10^6`. Entropy counts remain finite diagnostics.

## Major exact corrections and additions

1. The inverse-pair variables `alpha_j,beta_j` are squarefree-clock ordinals. The original integer occurrence positions are `A_j=s_{alpha_j}`, `B_j=s_{beta_j}`.
2. The self-map `phi(n)=|S(n)|` therefore satisfies `phi^{-1}(p_j)={A_j,B_j}`.
3. The periodic points are exactly the first ten primes. All are fixed; every other orbit reaches a prime at least 31 and then increases strictly.
4. On primes, `phi(p_j)=p_{f(j)}` with the exact index map `f(j)=N_-(p_j)=j+C_-(p_j)`. The map is strictly increasing, equals the identity for `j<=10`, and satisfies `f(j)>j` for `j>=11`.
5. The image of the prime-index map has counting function asymptotic to `(pi^2/3) J/log J`; hence the source indices of the escaping prime rays have density one.
6. A length-two collision `SS(n+2)=SS(n)` is equivalent to `|Delta_j|=1` for the corresponding integer-coordinate pair `Delta_j=B_j-A_j`; it is not equivalent to `|d_j|=1` in the squarefree clock.
7. The full `SS` trajectory universally and locally decodes the underlying ternary sequence. This is identification, not authentication and not encryption.
8. A genuine `SS` prefix through `sqrt(N)`, together with `SS(N)`, recovers `Q(N)` and then `M(N)` uniquely. Independent arithmetic checking of the short decoded Mobius prefix is still required for verification.
9. Active-pair cut kernels and their first lifetime moment collapse to one- or two-point height data; multicut crossing kernels reduce to the extreme cuts by interval convexity.

## Numerical regeneration

All numerical calculations and all eight PNG figures were regenerated from Python. No MATLAB output is used. The package preserves the raw NumPy arrays and every textual stage output.

The regenerated signed third-moment fit is explicitly treated as protocol-sensitive and is not assigned a stable asymptotic exponent. Regenerated active-lifetime and quadratic-fit values replace earlier report-only values where the protocols differed.

## LaTeX review

The final manuscript compiles without undefined references, multiply defined labels, overfull boxes, or underfull-box warnings in the final pass. All sections are labelled, equation numbering is by section, and the document contains a table of contents and a manual bibliography.
