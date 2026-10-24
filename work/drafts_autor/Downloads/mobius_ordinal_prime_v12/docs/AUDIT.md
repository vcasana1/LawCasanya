# Version 12 audit

## Scope

The new independent chapter records a research programme, proved intermediate
results, and unresolved estimates. It is Section 27 in the complete
manuscript and Section 1 in the standalone export.

## Corrections to the proposed programme

1. B has a proved pole correspondence with zeta zeros. A corresponding
   assertion for the full alpha is not established without continuation and
   noncancellation of the remaining blocks.
2. Holomorphy of delta alone does not exclude a B pole from alpha.
   The rigorous analytic criterion uses holomorphic continuation of
   alpha minus delta to real part greater than 3/2.
3. An abscissa of convergence is not a pole line or a functional equation.
   The sign involution changes signed coefficients, not the complex argument.
4. A zero argument-principle integral counts equal numbers of zeros and
   poles; it does not prove that there are no poles.
5. PNT already excludes macroscopic relative separation of the matched
   occurrences asymptotically. It does not give square-root bounds or
   summable Taylor errors. The active proof uses exact integrals.
6. Finite balanced prefixes require half-open pair intervals. The two-cut
   identity is exact and retains order through two times.
7. A fixed-lag increment theorem leaves an unestimated absolute-height term.
   It does not by itself estimate V(r), even for fixed r.
8. V(0) is an area, at least J; a bound of order J^(1/2+epsilon) for every
   epsilon is impossible. The height and area scales must be separated.
9. An auxiliary pair of words disproves the blanket assertion that every
   quadratic functional loses order. The old coercivity/evenisation
   proposition has its actual, narrower scope.
10. Off-boundary mean-square finiteness for every sigma>1/2 is equivalent
    to RH without assumptions of simple zeros. The weak Mertens estimate
    at the critical boundary is a different, stronger assertion.
11. The original integer ordering must retain unfinished pairs.
    Convergence after completing pairs need not prove convergence of all
    ordinary partial sums.
12. The literature comparison states what cited authors prove and what their
    programmes still require. It asserts neither universal failure of other
    methods nor priority over every construction.

## New proved results

- Every fixed ordinal-duration paired subseries delta_{<=L} converges
  normally for real part greater than 1, with a bound proportional to L.
- The energy of SS has the exact RH threshold 3/2. A nontrivial zero of
  real part beta forces divergence at every sigma<=1+beta, including equality.
  The proof uses the log-squared factor in a boundary Cauchy–Schwarz bound.
- Exact decomposition delta=P_delta+E_delta, where P_delta=B/s-B'.
  At a simple zero rho, the explicit block has a double pole at 1+rho
  with leading coefficient equal to the residue of B.
- Explicit prime-entry bordered matrices have determinants T(n) and SS(n).
  Fraction-free elimination checks the formula independently.
- The regularised finite coefficient measure satisfies an explicit
  Guinand–Weil identity with shifted delta_X arguments.

## What remains unresolved

The arithmetic estimation of the signed, weighted two-time terms is still
missing. The exact identity does not control delta by itself. The
fixed-duration holomorphy bound grows with the duration cutoff and does not
justify its infinite limit near real part 3/2.

The poles of P_delta are candidates for the full delta function. The Mellin
remainder E_delta is not shown holomorphic near those points. A relatively
smaller asymptotic remainder can even introduce a logarithmic branch point,
as an explicit control example demonstrates. No complete pole list for
alpha or delta is claimed.

The finite determinant representation does not supply its RH-strength
growth bound. The finite Guinand–Weil identity does not justify removing
the cutoff and smoothing. A concrete embedding from prime-gap weights
to the Weil test space, and the needed positivity implication, are absent.

## Verification

- 17,576 balanced words; 2,199,618 two-time point checks.
- 264 rational checks retaining unfinished pairs in a nonuniform clock.
- Exact coefficient identities at all 1,000,000 stored integer prefixes.
- Two-cut tails at 65 lags in the last balanced prefix.
- Exact T, SS and Redheffer determinants for n=1,...,40.
- Five numerical Laurent checks for explicit B/P_delta blocks, labelled
  as numerical and not as a continuation of delta.
- Static labels, citations, figure paths and independently compiled
  chapter/full-document references are checked by the build scripts.

See the JSON files and LaTeX logs in outputs for the released results.
The source-level correction to the older Mellin argument distinguishes
analytic continuation from ordinary series convergence; the older
closed-interval survival notation is also corrected to half-open intervals.

## Release verification

The final complete PDF has 61 pages; the independent chapter has 18. All
chapter pages were visually inspected. A fresh isolated submission build
produced exactly the same extracted text as the complete PDF. Final LaTeX
logs have no unresolved references or box warnings. PDF end markers and
reader opening are checked before packaging. The duplicate inherited
bibliography entries in the table of contents have been removed.
