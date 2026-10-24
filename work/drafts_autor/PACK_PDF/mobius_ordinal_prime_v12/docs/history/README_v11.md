# An Ordinal-Prime Transform of the Mobius Function - Version 11

This package contains the complete Version 11 manuscript, the compiled PDF, all eight figures, all Python source used for the numerical calculations and figure generation, intermediate NumPy arrays, and the corresponding textual outputs.

## Main files

- `mobius_ordinal_prime_transform_S_SS_v11.tex` - canonical LaTeX source.
- `mobius_ordinal_prime_transform_S_SS_v11.pdf` - compiled manuscript.
- `submission/` - submission-ready TeX, PDF, and figure files.
- `code/` - Python source. No MATLAB calculation is used in Version 11.
- `data/` - generated NumPy arrays for the `N=10^6` audit.
- `outputs/` - textual output from every numerical stage and the final LaTeX compilation passes.
- `figures/` - all manuscript PNG figures, regenerated from Python.
- `docs/` - data, reproduction, and audit notes.
- `checksums/` - SHA-256 manifests.

## Reproduction

Create a Python environment with `requirements.txt`, then run the numerical stages in the order documented in `docs/REPRODUCE.md`. Compile the TeX from the package root with two passes of `pdflatex`.

Version 11 adds exact fixed-level crossing and return formulae, a positive energy for complete negative excursions with the unconditional bound `A >= (H^3-H)/3`, and exact controls that remove primality while retaining either positions or ordinal ranks. Replacing `p_j` by `j` gives `SS_ord=n-Q+M(Q+1)/2`; the genuine prime block amplifies this ordinal signal by `log(Q/2)` asymptotically, and its squared energy by `log^2(Q/2)`. Finite entropy and collision counts are included only as diagnostics, not as proofs.
