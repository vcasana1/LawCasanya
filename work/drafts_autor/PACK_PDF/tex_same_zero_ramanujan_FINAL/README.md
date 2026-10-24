# Same-Zero Gaussian--Phase Coupling for Riemann-Zeta Zeros

Repository prepared for submission to **The Ramanujan Journal**.

## Journal submission directory

`submission/` is deliberately flat, as required for the LaTeX upload. It contains:

- `same_zero_gaussian_phase_Ramanujan.tex`
- `same_zero_gaussian_phase_Ramanujan.pdf`
- `sn-jnl.cls`
- `Fig1.png`
- `Fig2.png`
- `Fig3.png`
- `Fig4.png`

The manuscript uses the Springer Nature mathematical/physical-sciences numerical-reference setup:

```latex
\documentclass[pdflatex,sn-mathphys-num]{sn-jnl}
```

There is **no table of contents**. The title page contains six keywords and the 2020 MSC codes 11M26, 11M06, and 11K06.

Compile from the submission directory with:

```bash
cd submission
pdflatex -interaction=nonstopmode -halt-on-error same_zero_gaussian_phase_Ramanujan.tex
pdflatex -interaction=nonstopmode -halt-on-error same_zero_gaussian_phase_Ramanujan.tex
pdflatex -interaction=nonstopmode -halt-on-error same_zero_gaussian_phase_Ramanujan.tex
```

The bibliography is embedded directly in the main TeX source; BibTeX is not required to reproduce the supplied PDF.

## Author metadata

- Víctor Casaña-Giner
- Universidad Nacional de Educación a Distancia
- C/ Bravo Murillo, 38, 28015 Madrid, Spain
- vcasana1@alumno.uned.es
- ORCID: 0000-0002-8252-2608

The ORCID is printed without repeating the author's name beside it.

## AI-use statement

The manuscript contains the same AI-use declaration used in the author's latest JNT submission, as requested. It is included in the body as `Use of AI tools`.

## Reproducibility data

Exactly three data files are used by the article:

- `data/zeros6.txt`: A. M. Odlyzko's table of the first 2,001,052 positive zeta-zero ordinates.
- `data/zeross.bin`: float64 encoding of all 2,001,052 ordinates.
- `data/zLamb.bin`: float64 smooth Riemann--von Mangoldt clock data with 2,001,052 values.

The scripts in `src/` require the complete binary arrays and abort if either binary has a length other than 2,001,052. Smaller derived counts arise only from the mathematical observable itself (adjacent pairs, nonzero lags, or the explicitly stated high-window diagnostic).

## Repository layout

- `submission/` -- flat journal submission files
- `src/` -- reproducibility scripts
- `outputs/` -- numerical outputs
- `figures/` -- original-named copies of the four figures actually used
- `docs/` -- final submission/preflight notes
- `data/` -- the three data files used by the paper
- `checksums/` -- SHA-256 manifest and data audit
