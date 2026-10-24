# An Ordinal-Prime Transform of the Mobius Function — Version 12

Version 12, 7 September 2026. This package retains the Version 11 manuscript,
data, figures and computational history, with corrections and an independent
research-programme chapter. It does not claim a proof of RH.

## Read these files

- `mobius_ordinal_prime_transform_S_SS_v12.pdf`: complete manuscript.
- `mobius_ordinal_prime_transform_S_SS_v12.tex`: canonical source, including the chapter through an input.
- `alpha_research_program_v12.pdf`: independently readable research chapter.
- `alpha_research_program_v12.tex`: standalone chapter source, with its own preamble and bibliography.
- `chapters/alpha_research_program_v12.tex`: canonical chapter fragment.
- `submission/`: flattened full TeX, complete PDF and all eight figures.
- `docs/AUDIT.md`: corrections, proved results, remaining obligations and verification.
- `docs/BIBLIOGRAPHIC_AUDIT.md`: literature comparison and source scope.

## New mathematics and corrections

The chapter fixes the ordinal and physical clocks, proves the exact pair and
two-cut identities, and proves holomorphy of each fixed-duration paired
subseries for real part greater than 1. The uniform signed and weighted
arithmetic estimate needed for the full delta series remains unresolved.

The SS energy is defined with the correct real step-function subtraction.
It is finite for every sigma greater than 3/2 if and only if RH holds.
A zero beta+i gamma forces divergence for sigma at most 1+beta, including
the endpoint. In particular, the energy at 3/2 diverges unconditionally.

The explicit block B has poles at 1+rho. The differentiated block
P_delta=B/s-B' has one higher pole order; the first five numerical principal
parts are included. These are candidates for delta, not established poles
of the full delta function. An explicit remainder and a branch-singularity
control example explain the missing step.

The five proposals based on Connes's 2026 survey are audited separately.
In particular, there are explicit matrices with entries zero or signed primes
whose determinants equal T(n) and SS(n). Their construction is proved and
checked with exact integer determinants. It represents a sum; it does not
prove an RH-strength determinant bound. A finite regularised Guinand–Weil
identity is also derived with both Mellin normalisations distinguished.

## Reproduce the additions

Install the dependencies in `requirements.txt`, then run from this folder:

```bash
python3 code/v12_alpha_program_audit.py
python3 code/build_v12_release.py
```

The second command requires a LaTeX installation providing pdflatex and the
packages in the manuscript preamble. It exports the standalone sources,
audits references, and compiles both PDFs in three passes.
Edit the canonical root manuscript and chapter fragment, not their exports.
See `docs/REPRODUCE.md` for the full numerical pipeline.

## Data and checks

The original 17 NumPy arrays and eight PNG figures are retained byte for byte
from Version 11. They cover N=1,000,000. Existing output logs are historical;
files beginning with `v12_` or `60_v12_` report the new work.

The new audit checks 17,576 balanced words through length 16, 2,199,618
two-time point identities, one million arithmetic prefixes, and exact T/SS
and Redheffer determinants through n=40. Numerical Laurent checks concern
only the explicitly known meromorphic blocks. Finite verification supports
the identities, not infinite-tail claims.

`checksums/SHA256SUMS.txt` records the packaged files, excluding the checksum
manifest itself. Run `sha256sum -c checksums/SHA256SUMS.txt` in this directory.

Earlier reference PDFs and documentation are marked as inherited in
`outputs/` and `docs/history/`. They are not the current manuscript.
