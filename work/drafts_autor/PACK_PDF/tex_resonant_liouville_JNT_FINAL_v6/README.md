# Rational Resonances and Microscopic Natural--Logarithmic Profiles for the Liouville Function

Final Journal of Number Theory short-notice submission and reproducibility pack.

## Submission
- `submission/tex_resonant_liouville_JNT_FINAL.tex`
- `submission/tex_resonant_liouville_JNT_FINAL.pdf`
- `submission/elsarticle.cls`
- `submission/elsarticle-num.bst`
- three manuscript figures, PNG only

## Reproducibility
- `src/`: every Python script used for numerical checks and figure generation
- `data/liouville_int8_N21000000.bin`: the only binary used
- `outputs/`: literal Python stdout captures, CSV/TXT numerical outputs, LaTeX compilation logs, binary regeneration audit, and PDF preflight/render checks
- `figures/`: PNG figures only
- `checksums/`: SHA-256 inventories

The Liouville binary was regenerated from `lambda(n)=(-1)^Omega(n)` and verified byte-for-byte against the supplied data file before packaging.

No zeta/RVM binaries are used or included.
