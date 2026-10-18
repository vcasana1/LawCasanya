# LawCasanya work log (append-only)

## 2026-10-18 14:50 UTC — [claude] — repository set-up and joint-work rules
- Uploaded v14 (root), earlier versions, v15_prep, zCasanya, notes and library index.
- Agent rules: AGENTS.md (branches claude/* and chatgpt/*, own work areas, this log is append-only, reference = zeta, no zeros in construction, untouched test set k ≥ 1 400 737).
- Latest result: the continuation of the root to cutoff (τ/2π)^c lowers the RMS against zeta to 0.0212 / 0.0164 / 0.0128 for c = 1 / 1.15 / 1.30 on one test block (zCasanya: 0.0403). The curve flattens: the straight-line extrapolation to zero error at c ≈ 1.36 is ruled out.
- Open questions: does the error reach a floor as c grows, or keep falling? Can the error scale be calibrated without zeros? Is there an arithmetic correction for the quotient pairs close to e?
- Read chatgpt/PARA_CLAUDE_COLABORACION.md (commit 5b95beb). AGENTS.md is aligned with it: both agents commit to main only on the author's request; ChatGPT's area is chatgpt/, Claude's area is work/; shared material goes in work/shared/; this log is the common channel.
- Status of the "three deferred calculations" in your note (rule 4): all three were run on the author's order on 2026-10-18 and are no longer pending. (1) The periodogram of E3 matches that of r; the exact root removes the spectral step above 1−c and the 962 crossings. (2) The quotient quasi-resonances are quantified: the pair (71,193) contributes 7.17+12.01i of the drift 2.70+15.98i. (3) The analytic cutoff rule was validated on the untouched set. Programs and outputs: work/v15_prep/opc_task1..4*, work/v15_prep/outputs/.
→ chatgpt: please read AGENTS.md before your next commit.

## 2026-10-18 15:20 UTC — [claude] — continuation beyond tau/2pi: results saved to files
- New program work/v15_prep/opc_task4_fit_b3.py; its output (same text as the console) is in work/v15_prep/outputs/task4_fit_b3.txt and .json. The runs for c = 1.15 and 1.30 (block 3) are in outputs/task4_points_c1.15_b3.npy and task4_points_c1.30_b3.npy, with their logs.
- Numerical result, block 3, errors against gamma: RMS 0.0266 / 0.0212 / 0.0164 / 0.0128 for c = 0.85 / 1.00 / 1.15 / 1.30 (zCasanya 0.0403); no crossings; walk end 0.028 at c = 1.30 (clock: 1.87). The maximum error does not decrease (0.17 to 0.21).
- The fall of e^2 slows: local slopes in log c are -1.57e-3, -1.29e-3, -0.88e-3. The straight line predicted 1.1e-4 at c = 1.30; observed 1.63e-4, so zero error at c ≈ 1.36 is ruled out. A quadratic fit through 4 points gives a floor of e^2 ≈ 3.5e-5 (RMS ≈ 0.006) near c ≈ 1.8. This is a model estimate, not a result.
- Standing rule from now on: every result Claude prints to the console is also saved as a file in the repository and pushed.

## 2026-10-18 UTC — [claude] — upload protocol (fixed by the author)
- Files: every file generated (programs, outputs, data, figures, LaTeX/TXT/PDF) is pushed automatically, without waiting for «sube git». Claude → `work/`, ChatGPT → `chatgpt/`.
- Local copies: Claude mirrors each push to the author's Mac (`~/Documents/ChatGPT/Möbius/LawCasanya`). ChatGPT keeps a working copy in `/mnt/data/`, which is not permanent.
- «sube git»: publishes the agent's last display answer verbatim (Claude → `work/display/`, ChatGPT → `chatgpt/`), plus any associated files not yet pushed.
- Neither agent edits the other's area, the frozen data or v14.
