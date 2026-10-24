# Exponential centroids and Montgomery pair correlation

This directory is a self-contained reproducibility archive for
`montgomery_from_exponential_centroids_v1.tex`.

## Data

- `data/g_hp.bin`: 22,491 zeta ordinates, raw little-endian IEEE-754 float64.
- `data/g_hp.npy`: provenance NumPy copy of the same array.
- `data/gammas.bin` and `data/gammas.npy`: second supplied ordinate table,
  preserved for provenance but not used by the principal figures.
- `data/rvm_tau_2001052.bin`: 2,001,052 generated Lambert--RVM levels, raw
  little-endian IEEE-754 float64.

Every binary is headerless. Its element count, byte count, and SHA-256 digest
are printed in `outputs/` and recorded in `SHA256SUMS.txt`.

## Reproduction

From this directory, run:

```bash
bash run_all.sh
latexmk -pdf -interaction=nonstopmode montgomery_from_exponential_centroids_v1.tex
```

The heaviest step is the full 2,001,052-level carrier-saddle calculation.
No network access is required. Python dependencies are listed in
`requirements.txt`.

## Status of the mathematics

The archive separates exact identities, proved conditional results, numerical
compatibility checks, and two explicitly labelled hypotheses. Numerical
agreement is not used as a replacement for a proof. The unrestricted
Montgomery plateau remains reduced to the frequency-localized Selberg
remainder transfer stated in the paper.

The two original supplied ZIP files and the supplied form-factor PNG are kept
unchanged under `source_archive/`.

