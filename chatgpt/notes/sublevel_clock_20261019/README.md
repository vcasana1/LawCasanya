# Ordered prime clock by sublevel integration

Research note prepared on the author's instruction of 2026-10-19: use an analytic guarantee; do not select a cutoff or correction from comparisons against the zero data.

## Contents

- prime_sublevel_clock.tex and byte-identical prime_sublevel_clock.txt: complete definitions, proofs, source audit, and limitations.
- prime_sublevel_clock.pdf: compiled note with equation numbers on the right, contents, links, citation backreferences, and tooltip widgets on the principal references.
- build.py: compiles three passes, checks unresolved references, copies TEX to TXT, and records structural PDF verification when pypdf is available.
- build.log and build_metadata.json: output of that build.
- source_audit.json: precise source statements and local PDF checksums.

The directory is a standalone note in ChatGPT's own area. It does not edit or replace a manuscript version.

## Result and its scope

The clock is the measure of a sublevel set of a continuous prime-phase approximation to N(t). It is a universal map of the RvM input tau. All local Euler factors of the prescribed prime prefix are retained. The prefix size is the largest integer m with m squared at most the dyadic height; adjacent phases are interpolated affinely to obtain continuity.

The deterministic theorem bounds squared errors of the ordered points by a third gap moment and a fourth counting-error moment. Its application gives an unconditional asymptotic mean-square height error O(1/log(T)^2), using the checked standard estimates listed below. Strict order is proved directly.

This is not a numerical accuracy guarantee at the heights of the existing datasets. The implied constant and onset height have not been evaluated. There is no asserted finite-height improvement over zCasanya, R2, or the quotient-only point, and no claim of novelty in the literature. The note requires further mathematical review before incorporation in a paper.

R2, its Gaussian cutoff model, the quotient-only selection, and every fitted numerical improvement are absent from the construction and proof. No zero dataset was opened or used for numerical experimentation in this task.

## Source verification

Read the actual local PDF statements:

1. Fazzari, Gerspach, Minelli, arXiv:2507.04150v1, 5 July 2025, printed/PDF page 7, (3.1), (3.6): the unconditional fourth-moment approximation of the imaginary part of log zeta by a short prime polynomial, with moment parameter 2.
2. Titchmarsh, revised by Heath-Brown, The Theory of the Riemann Zeta-function, second edition (1986), printed page 175, (7.20.1): the Montgomery--Vaughan weighted mean-value estimate.
3. Same book, printed page 246 / PDF page 252, (9.25.4): third moments of gaps for all zero ordinates, counted with multiplicity.

The source PDF checksums are in source_audit.json. The original Tsang thesis and the original Fujii papers were not read; the note explicitly says so and cites the actual statements read above. No assertion that a bibliographic index verifies a theorem is made.

## Build

Run:

    python3 build.py

Requires Python 3 and pdflatex with the standard packages used in the preamble: amsmath, amssymb, amsthm, mathtools, mathrsfs, lmodern, microtype, geometry, enumitem, hyperref. Optional pypdf enables structural PDF metadata checks. The tooltip macro uses standard PDF widgets and has no dependency on pdfcomment, tracklang, or soulutf8.

No reference data or external figure is needed to compile. The archive contains only the note and its build/audit files.
