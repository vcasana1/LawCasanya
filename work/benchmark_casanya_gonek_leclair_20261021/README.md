# Casanya–Gonek–França–LeClair: supporting scripts (2026-10-21)

This directory gathers **existing supporting code** supplied in the project and the experiment protocol for Codex. These are not new proofs, not a v17 implementation, and not validated Gonek/LeClair implementations.

## Contents

- `benchmark_casanya_gonek_leclair_codex.txt`: complete instructions for a fair benchmark with true zeros used **only for evaluation**, matching prime budgets, root-index preservation, accuracy/cost and staged pilot.
- `zCasanya0_optimizar.m`: MATLAB experimental Casanya prime-power-clock correction [8, 8, X] with a *subsequent monotonic projection*, using separate tuning, selection and evaluation windows. **Not** the original c667 constructor of `zCasanya.bin`, and not the certified v17 continuation. Intended as a supplementary MATLAB implementation to be independently audited.
- `prime_cutoff_odlyzko_local.m`: separate MATLAB experiment for local low/high Odlyzko ordinate data and prime-power cutoffs; high ordinates require **offset** files and Symbolic Math Toolbox. Its default `cfg.createBinary=true` can write `zCasanya0.bin` in the current directory. Inspect configuration before executing.

## Existing code already in the repository

See the repository's main `README.md` and `code/` directory for existing Python/RvM/prime-defect implementations (in particular `opc_analysis_v14.py`, `opc_transport_v14.py`, `opc_resonance_v14.py`, and `make_inputs_v14.py`). Prefer reusing those instead of duplicating them.

## Cautions

1. Keep source inputs intact (`data/zeross.bin`, `data/zLamb.bin`, and any `zCasanya.bin`); run MATLAB in a separate working/output directory to avoid output collisions.
2. The existing MATLAB files access true ordinate data for **tuning/evaluation** but not inside the per-index prime-clock update. Do not conflate this with a new unconditional theorem.
3. The Oct-18 experiment report records `zCasanya.bin` RMS 0.0439885472, and 962 non-positive adjacent gaps in the selected configuration. Verify numbers against available data and disclose crossings.
4. Gonek uses a smoothed product: reproducing a sharp-cutoff Euler phase does not count as implementing Gonek.
5. The full benchmark requires faithful published Gonek/França–LeClair equations and a separate `M4` continuation implementation, if actual v17 source is found.
6. No modifications to manuscript versions or original datasets have been made as part of this upload.

Published reference papers should be consulted before interpreting differences in benchmark results.
