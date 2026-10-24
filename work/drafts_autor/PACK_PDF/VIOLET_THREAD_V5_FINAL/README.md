# VIOLET_THREAD_V5

Principal manuscript
--------------------
- `manuscript/VIOLET_THREAD_V5.tex`
- `manuscript/VIOLET_THREAD_V5.pdf`

Version 5 changes
-----------------
- Rewritten in `amsart` 11pt format with a table of contents.
- Section-numbered and labelled displayed equations.
- Every section and every figure has a label.
- `hyperref` is loaded last.
- Bibliography uses `thebibliography` and citation keys of the form AuthorYear.
- Correct endpoint identity:
  `(Y_n'(1))^2 = w_n'(1)/w_n'(0)`.
- Correct scattering potential:
  `Q_n = -log(a_n) - i psi_n`.
- Corrected holonomy, square-root branch, complex moment, and telescoping product.
- Added the exact logical equivalence between a reciprocal pole of `U=1/F` and a zero of `F` at the same domain point.
- Added the Schwarzian one-arch characterization: for positive sweep, the constant RVM projective state occurs exactly at `s=1`.
- Removed the Chebyshev/Bernstein-ellipse detour from the manuscript.
- Figure layout reduced from 22 images in V4 to 15 images in V5, arranged in 10 figure environments. No forced `[H]` floats are used.
- The V5 PDF is 19 A4 pages.

Data policy for this revision
-----------------------------
Version 5 is an analytic and typographical revision. `zeross.bin`, `zLamb.bin`, the CSV outputs, and the previously generated numerical figures were copied unchanged from the preceding verified package. They were not read, inspected, or recomputed during the V5 revision.

Reproducibility
---------------
- `scripts/VIOLET_THREAD_ANALYSIS.py` is the consolidated Python analysis script used for the carried numerical material.
- `data/zeross.bin` and `data/zLamb.bin` are included unchanged.
- `outputs/` contains the carried CSV and TeX tables.
- `figures/` contains only the fifteen PNG files used by the V5 manuscript.

Compile from `manuscript/` with:

    pdflatex VIOLET_THREAD_V5.tex
    pdflatex VIOLET_THREAD_V5.tex
