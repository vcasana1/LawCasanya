# CasanyaLaw I v20 — mathematical and build audit
Date: 2026-10-25

## Files
- chatgpt/manuscripts/CasanyaLawI_v20.tex
- chatgpt/manuscripts/CasanyaLawI_v20.txt (same Git blob: 92eceaac5ec0068cf5d2401f513d08f73521081e)
- Local/conversation PDF: CasanyaLawI_v20.pdf (62 pp.; not uploaded to GitHub by text-only connector)

## Sources reviewed
- User's uploaded CasanyaLawI_v19(1).tex (unmodified original)
- work/notes/2026-10-25_literatura_multiplicidad_horizontal_y_un_doceavo.md (commit 168df78)
- work/notes/2026-10-25_texto_v20_PerronMfixed_incondicional.md
- work/notes/2026-10-25_JX_Newton_completo.md
- work/notes/2026-10-25_JX_un_paso_diverge.md
- work/notes/2026-10-25_ET_a_cero_estado.md
- work/notes/2026-10-25_via_M_localizacion_uniforme.md

## Explicit changes
- Preserves v19 structural sections and historical theorem labels, equation numbers on the right, TOC, hyperref back-references, pdfcomment tooltips.
- Corrected the sign in the decomposition of S_X via Im(p^{-it}); the v19 printed -Im despite S_X defined as -sin.
- Horizontal multiplicity credit to Goldston--Lee--Schettler--Suriajaya; Gallagher--Mueller connection; Baluyot et al. benchmark 41.72% and numerical threshold 0.1457; clearly distinguishes the reported 40.75% simultaneous simple/critical benchmark.
- New fixed-X Newton geometry with full derivative N_0'+S_X' and complete Taylor proof of O_X((log k)^-3) versus exact roots.
- Exact all-x consequence of the conditional finite Euler/Perron comparison, and diagonal sufficient criterion for RH.
- Six-term expansion of (N-F)^2 dF and proof of exact jump cancellations; the 1/12 target as a one-sided upper-bound criterion once cubic endpoints vanish.
- Smooth differentiable growing-prime cutoff with complete derivative, including the weight derivative.

## Important mathematical boundary
The proposed notes' statement that S_X^2 S_X'' and S_X^2 S_X'' S_X' are *finite* trigonometric polynomials is false for the complete finite-base Euler phase: all prime powers remain, so the Fourier expansions are infinite. Zero mean from oddness does NOT alone justify termwise Hilbert transforms uniformly near arbitrarily small nonzero frequencies. For this reason v20 does not assert the unconditional convergence J_X^full<infinity, or J_X^one=infinity, without an additional small-divisor proof. The note's implication that J_X^one=infinity forces nonexistence of symmetric Perron inversion is likewise not established. The written conditional Perron theorem is mathematically exact under its explicit hypothesis.

The paper does not prove RH or E_T->0. Fixed-X bounds cannot be used with X=x without uniform constants.

## Checks
- pdfLaTeX/latexmk compiled successfully: 62 pages.
- TeX and TXT files byte-identical; Git blob SHA equals local git hash-object.
- Zero duplicate \label keys.
- Zero unresolved \eqref/\cref references and zero unresolved citations in final build log.
- Rendered title and sample proof page manually inspected.
- No writes to Claude-owned work/ except append-only work/LOG; no writes to LIBRARY TOTAL.
