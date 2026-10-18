# The Riemann–von Mangoldt clock and the zeros of the Riemann zeta function (v14)

Companion repository of the manuscript `manuscript/ordinal_prime_cutoff_v14.tex`
(identical text copy `ordinal_prime_cutoff_v14.txt`, compiled PDF alongside), prepared for
submission to the Journal of Number Theory.

## Input data (included in `data/`; also regenerable with a certificate)

The ordinates are A. M. Odlyzko's table **zeros6**: the first 2,001,052 zeros of the Riemann zeta
function, accurate to within 4e-9, from https://www-users.cse.umn.edu/~odlyzko/zeta_tables/ .
Download it (plain text or `.gz`) and run

    python3 code/make_inputs_v14.py zeros6.gz data --legacy-clock OLD/zLamb.bin   # last option optional

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
| `make_inputs_v14.py ZEROS6 data` | the two input files and their certificate |
| `opc_validate_v14.py` | `outputs/identity_checks.json`: implementation checks of the exact identity (repeated ordinate, nonmonotone model) and of the kernel integral |
| `opc_extensions_v14.py data` | `outputs/table_F_direct_defects.csv` (Theorem B observables), `outputs/table_G_prime_responses.csv` (responses of all 2,262 primes <= 20,000), `outputs/extension_metadata.json` |
| `opc_analysis_v14.py data` | one-step-clock comparisons `outputs/table_A`–`table_E`, `close_pair_k258318.txt`, `opc_analysis_log.txt`, `analysis_*.json`; figures 1, 4, 5, 6 and S1–S3 |
| `opc_checks_v14.py data` | `outputs/check_accounting.csv` (Theorem C decomposition), `check_envelope.csv`, `check_response_bins.csv`, `check_log.txt`; figures 2, 3, 7, 8 |
| `opc_transport_v14.py data` | `outputs/table_H_transport.csv`, `transport_log.txt` (Table 5: transport and Newton term, Theorem D) |
| `opc_resonance_v14.py data` | `outputs/table_I_cross_term_onset.csv`, `table_I_resonance.json` (Table 6 and the resonant-pair decomposition) |
| `opc_envelope_check_v14.py data` | `outputs/check_envelope_S.csv` (finite-height envelopes, Proposition 8.2) |
| `opc_twist_v14.py data` | `outputs/table_J_twist.csv`, `twist_log.txt` (Table 2: transport identity in a prime frequency, resonance) |
| `opc_iteration_v14.py data` | `outputs/table_K_iteration.csv` (Table 3: iterated Newton steps, deformation and multiplicity at T=2^19) |
| `opc_computable_response_v14.py data` | `outputs/table_L_computable_response.csv` (Table: computable, transport and residual parts of the prime responses at T=2^19) |
| `opc_envelope_coefficient_v14.py outputs` | `outputs/envelope_coefficient.json` (constant of Theorem E; reads no data) |

Requirements: Python 3 with NumPy, SciPy, Matplotlib and mpmath. Versions used: Python 3.13.16,
NumPy 2.5.3, SciPy 1.18.1, Matplotlib 3.11.2, mpmath 1.3.0. Total running time about 10 minutes;
memory linear in the number of ordinates. No parameter is fitted and no subsampling is used.

## Figures (`figures/`)

`fig01`–`fig08` are the figures of the paper, numbered as in the paper. `figS1_rms_by_height`,
`figS2_optimal_cutoff` and `figS3_close_pair` are supplementary and are not printed in the paper.

## Manuscript tools (`tools/`)

`make_tips_v14.py` and `replace_tips_v14.py` generate the hover texts of the PDF:

    cd manuscript
    pdflatex ordinal_prime_cutoff_v14.tex && pdflatex ordinal_prime_cutoff_v14.tex
    python3 ../tools/make_tips_v14.py ordinal_prime_cutoff_v14.tex ordinal_prime_cutoff_v14.aux tips.tex
    python3 ../tools/replace_tips_v14.py ordinal_prime_cutoff_v14.tex tips.tex
    pdflatex ordinal_prime_cutoff_v14.tex (three times)

The class `elsarticle` (TeX Live package `texlive-publishers`) and `pdfcomment` are required.

## Status of the statements

Theorems A-E, all Newton steps with constants uniform in their number (Section 8: multiplicity of the
corrected clock points of every level, cutoff law, error O(1) mean spacings after log* T + O(1) steps), the
local deformation of the second clock, the transport identity, the resonance and its pair version, the almost
orthogonality of the prime phases and the spectral energy inequality (Section 8.6), the rounding obstruction (Section 5),
the explicit bound for |S(T)|, all statements of Sections 11.1-11.3 and the spectral analysis of the Newton
nonlinearity (Section 11.4: barrier, Bessel expansion, dispersion, orthogonality, computable and residual responses) are unconditional. Section 11.5
contains rigorous implications from the named Hypotheses U and W. Section 12 (determinantal model, conjectured
law and its numerical comparison) is heuristic support only. The subsection "Status of the proofs and pending
verification" in the conclusions lists what was read in the original sources, what was communicated and not
recomputed, and what is not proved. Appendix A reproduces every program verbatim.


## Repository layout beyond the v14 deliverable

The root (`manuscript/`, `code/`, `outputs/`, `figures/`, `tools/`, `data/`) is the v14 deliverable.
`data/zeross.bin` is derived from A. M. Odlyzko's table zeros6 (source above; please cite Odlyzko);
`data/zLamb.bin` is the clock of the paper (SHA-256 `b4c6758f...`).

`work/` contains working material that is not part of the v14 paper:

* `work/versions/v1 ... v13/` - earlier versions (code, outputs, figures, manuscripts), without data files;
* `work/v15_prep/` - programs and outputs prepared after v14 (Newton residual spectrum, exact
  product/quotient decomposition of the walk drift, analytic per-index cutoff rule, self-consistent
  cutoff beyond tau/2pi); `opc_common.py` holds the shared definitions;
* `work/zcasanya/` - construction, validation and report programs of zCasanya (cutoffs (8,8,512)),
  with manifests, results and figure; `work/zcasanya/matlab/` - MATLAB reimplementation
  `zCasanya_newton3_graficos.m` and its seven figures;
* `work/data/` - `zCasanya.bin` (Python, SHA-256 `64d1de13...`), `zCasanya_matlab.bin` (MATLAB,
  SHA-256 `d01d2366...`; max difference from the Python file 7.0e-10) and the clock file zCasanya
  was built from, `zLamb_clock_zCasanya_input.bin` (SHA-256 `b6f2a8d6...`);
* `work/notes/` - pending-verification notes for the next version;
* `work/library/` - index of the author's reference library (`INDEX.md`, renumbering tables); the
  PDFs themselves are not distributed;
* `work/misc/` - figures removed from earlier versions.

The `work/v15_prep` programs expect `zLamb.bin`, `zeross.bin` and `zCasanya.bin` in their working
directory (copy them from `data/` and `work/data/`; for runs that reproduce zCasanya use
`zLamb_clock_zCasanya_input.bin` as `zLamb.bin`).
