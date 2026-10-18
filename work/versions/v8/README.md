# The Riemann–von Mangoldt clock and the zeros of the Riemann zeta function (v8)

Companion repository of the manuscript `manuscript/ordinal_prime_cutoff_v8.tex`
(identical text copy `ordinal_prime_cutoff_v8.txt`, compiled PDF alongside), prepared for
submission to the Journal of Number Theory.

## Input data (not included; regenerated with a certificate)

The ordinates are A. M. Odlyzko's table **zeros6**: the first 2,001,052 zeros of the Riemann zeta
function, accurate to within 4e-9, from https://www-users.cse.umn.edu/~odlyzko/zeta_tables/ .
Download it (plain text or `.gz`) and run

    python3 code/make_inputs_v8.py zeros6.gz data --legacy-clock OLD/zLamb.bin   # last option optional

This writes

* `data/zeross.bin` – ordinates gamma_k, little-endian float64, correctly rounded from the table;
  SHA-256 `fafb9436ce6a506de58c96c9bc9765d3942de3f15c921e99e0015b3e945fe0ac`
  (the script reports whether the hash matches; equality proves the data are the table);
* `data/zLamb.bin` – RvM clock tau_k, N_0(tau_k) = k - 1/2, the float64 nearest to the exact root
  for every k; SHA-256 `b4c6758f0aef3724d3345f894ff82d5bbcb0f6139025b8b266091f713faa9504`;
* `data/make_inputs_certificate.json` – the certificate: correct rounding decided for every k in
  extended precision, near-midpoint cases (20,679) decided with mpmath at 40 digits, and an
  independent bit-for-bit mpmath check at 19,900 indices.

`outputs/make_inputs_certificate.json` is the certificate of the files used for this version.
An earlier clock file (SHA-256 `b6f2a8d6...1252`) differs by at most 3 units in the last place
(2.3e-10); all printed numbers of the paper are identical with either file
(maximal relative change of any tabulated quantity 3e-9).

## Programs (`code/`, each with an identical `.txt` copy)

Run from the repository root, in this order:

| program | produces |
|---|---|
| `make_inputs_v8.py ZEROS6 data` | the two input files and their certificate |
| `opc_validate_v8.py` | `outputs/identity_checks.json`: implementation checks of the exact identity (repeated ordinate, nonmonotone model) and of the kernel integral |
| `opc_extensions_v8.py data` | `outputs/table_F_direct_defects.csv` (Theorem B observables), `outputs/table_G_prime_responses.csv` (responses of all 2,262 primes <= 20,000), `outputs/extension_metadata.json` |
| `opc_analysis_v8.py data` | one-step-clock comparisons `outputs/table_A`–`table_E`, `close_pair_k258318.txt`, `opc_analysis_log.txt`, `analysis_*.json`; figures 1, 4, 5, 6 and S1–S3 |
| `opc_checks_v8.py data` | `outputs/check_accounting.csv` (Theorem C decomposition), `check_envelope.csv`, `check_response_bins.csv`, `check_log.txt`; figures 2, 3, 7, 8 |

Requirements: Python 3 with NumPy, SciPy, Matplotlib and mpmath. Versions used: Python 3.13.16,
NumPy 2.5.3, SciPy 1.18.1, Matplotlib 3.11.2, mpmath 1.3.0. Total running time about 10 minutes;
memory linear in the number of ordinates. No parameter is fitted and no subsampling is used.

## Figures (`figures/`)

`fig01`–`fig08` are the figures of the paper, numbered as in the paper. `figS1_rms_by_height`,
`figS2_optimal_cutoff` and `figS3_close_pair` are supplementary and are not printed in the paper.

## Manuscript tools (`tools/`)

`make_tips_v8.py` and `replace_tips_v8.py` generate the hover texts of the PDF:

    cd manuscript
    pdflatex ordinal_prime_cutoff_v8.tex && pdflatex ordinal_prime_cutoff_v8.tex
    python3 ../tools/make_tips_v8.py ordinal_prime_cutoff_v8.tex ordinal_prime_cutoff_v8.aux tips.tex
    python3 ../tools/replace_tips_v8.py ordinal_prime_cutoff_v8.tex tips.tex
    pdflatex ordinal_prime_cutoff_v8.tex (three times)

The class `elsarticle` (TeX Live package `texlive-publishers`) and `pdfcomment` are required.

## Status of the statements

Theorems A, B, C are unconditional. Section 8 contains rigorous implications from the named
Hypotheses L, U and W. Section 9 (determinantal model, Conjecture 9.2 and its numerical comparison)
is heuristic support only. The one-step-clock exponent 0.5744 is exploratory.
