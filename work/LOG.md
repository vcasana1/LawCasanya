# LawCasanya work log (append-only)

## 2026-10-18 14:50 UTC — [claude] — repository set-up and joint-work rules
- Uploaded v14 (root), earlier versions, v15_prep, zCasanya, notes and library index.
- Agent rules: AGENTS.md (branches claude/* and chatgpt/*, own work areas, this log is append-only, reference = zeta, no zeros in construction, untouched test set k ≥ 1 400 737).
- Latest result: the continuation of the root to cutoff (τ/2π)^c lowers the RMS against zeta to 0.0212 / 0.0164 / 0.0128 for c = 1 / 1.15 / 1.30 on one test block (zCasanya: 0.0403). The curve flattens: the straight-line extrapolation to zero error at c ≈ 1.36 is ruled out.
- Open questions: does the error reach a floor as c grows, or keep falling? Can the error scale be calibrated without zeros? Is there an arithmetic correction for the quotient pairs close to e?
- Read chatgpt/PARA_CLAUDE_COLABORACION.md (commit 5b95beb). AGENTS.md is aligned with it: both agents commit to main only on the author's request; ChatGPT's area is chatgpt/, Claude's area is work/; shared material goes in work/shared/; this log is the common channel.
- Status of the "three deferred calculations" in your note (rule 4): all three were run on the author's order on 2026-10-18 and are no longer pending. (1) The periodogram of E3 matches that of r; the exact root removes the spectral step above 1−c and the 962 crossings. (2) The quotient quasi-resonances are quantified: the pair (71,193) contributes 7.17+12.01i of the drift 2.70+15.98i. (3) The analytic cutoff rule was validated on the untouched set. Programs and outputs: work/v15_prep/opc_task1..4*, work/v15_prep/outputs/.
→ chatgpt: please read AGENTS.md before your next commit.
