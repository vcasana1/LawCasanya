# Reproduction — Version 12

Run commands from the package root. Python dependencies are listed in
`requirements.txt`; LaTeX is a separate system dependency.

## Verify the new chapter using the supplied data

```bash
python3 code/v12_alpha_program_audit.py > outputs/60_v12_alpha_program_audit.txt
python3 code/build_v12_release.py
```

The mathematical audit checks finite combinatorial identities with integers
or fractions, determinants with fraction-free elimination, and explicit
meromorphic principal parts with 60-decimal working precision. It writes
`outputs/v12_alpha_program_audit.json`. The last checks are numerical,
not certified complex interval calculations, and do not locate poles of
the unknown full delta continuation.

The build script first generates a flattened submission TeX and an
independent chapter TeX. It checks labels, references, citations and figure
paths; then compiles both PDFs in three passes. Individual LaTeX logs are
retained in `outputs/v12_*_pdflatex_pass*.txt`.

## Regenerate the inherited data and figures

```bash
python3 code/run_all.py
python3 code/build_v12_release.py
```

The pipeline lists every stage explicitly. It retains the historical script
names for stages introduced in Versions 5, 9 and 11, and adds the v12 audit.
`figures.py` generates Figures 1–6; `envelope_origin.py` generates Figures
7–8. This release did not need to rerun those stages: their NumPy inputs and
PNG outputs were verified identical to Version 11 by SHA-256.

The archived `code/history/` scripts are provenance records and are not
required by either reproduction command.

## Compile the submission independently

In `submission/`, run pdflatex twice on
`mobius_ordinal_prime_transform_S_SS_v12.tex`. This file includes the full
chapter directly and needs only the eight adjacent figure files.
The standalone `alpha_research_program_v12.tex` requires no figure files.

## Check package integrity

```bash
sha256sum -c checksums/SHA256SUMS.txt
```

Regeneration can change PDF timestamps and floating-point diagnostic
formatting. The distributed manifest describes the release, not future
byte-for-byte reproducibility of a fresh PDF build.
