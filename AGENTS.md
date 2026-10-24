# Working rules for agents in LawCasanya (Claude and ChatGPT)

Two AI agents work on this repository for the author, Víctor Casaña-Giner (Doktor). These rules keep their work from colliding. The author's instructions override this file.

## 1. Branches and commits

* Both agents commit to `main`, and only when the author has asked for the work.
* Run `git pull` immediately before every commit, and push small commits right away so the other agent sees them.
* Never force-push or rewrite history. Never revert or reformat another agent's commit.
* Commit message prefix: `[claude]` or `[chatgpt]`. Say what changed and which results it produced.

## 2. Who writes where

| Path | Rule |
|---|---|
| `manuscript/`, `code/`, `outputs/`, `figures/`, `tools/`, `data/` (root) | v14 deliverable, frozen. Do not edit. |
| `work/versions/` | Earlier versions, frozen. |
| `work/data/` | Binary inputs, immutable. Add new files, never overwrite; record the SHA-256 in `work/data/HASHES.md`. |
| `work/` (except `work/shared/` and `work/LOG.md`) | Claude's area. ChatGPT reads it but does not edit it. |
| `chatgpt/` | ChatGPT's area. Claude reads it but does not edit it. |
| `work/shared/` | Joint material. Only add new files; to change a shared file, propose the change in `work/LOG.md` first. |

## 2A. Author-mandated write prohibitions (effective 2026-10-24)

* **ChatGPT: the entire separate repository `vcasana1/LIBRARY-TOTAL-28oct2026` is strictly READ-ONLY.** ChatGPT must not create, update, delete, rename, commit, push, change indexes, or otherwise write any file or repository state there. Reading the original PDFs and metadata is permitted.
* **Claude: ALL VERSIONED MANUSCRIPTS AND PAPERS OF THE AUTHOR are strictly READ-ONLY**, regardless of their location or filename (including `.tex`, `.txt`, `.pdf`, document versions and bundled manuscript packages). Claude must not create, modify, replace, rename, delete, or commit versions of the author's papers. Claude may read and analyze them and write separate research notes in its permitted areas without altering a versioned manuscript.
* Manuscript versions requested expressly by the author may be prepared by ChatGPT in ChatGPT's permitted area; this does not grant any write permission in `LIBRARY-TOTAL-28oct2026`. These role prohibitions supersede any older general guidance permitting agents to create a new manuscript version.

## 3. Communication: `work/LOG.md`

* `work/LOG.md` is the shared log. It is append-only: never edit or delete earlier entries. Both agents write in it. ChatGPT may also keep longer notes in `chatgpt/`.
* Entry format: `## YYYY-MM-DD HH:MM UTC — [claude|chatgpt] — topic`, then what was done, the files involved, the main numbers, and what is still open.
* Before starting a task, read the latest entries. If the other agent is already on that topic, do not duplicate it: continue from its result or write a note.
* Handing work over to the other agent is done with an entry addressed to it (`→ chatgpt:` or `→ claude:`). The two sessions do not talk to each other directly: they communicate only through the repository, and the author relays when needed.

## 4. Scientific rules (fixed by the author)

* **Reference = zeta.** Every error is measured against the true ordinates γ_k (`data/zeross.bin`). The RvM clock τ_k is only an intermediate tool, never the target.
* **No zeros in construction.** No construction or parameter choice may use γ_k. The γ_k are read only to evaluate.
* **Untouched test set:** indices k = 1 400 737 … 2 001 052 (the final 30 %). Never tune anything on them.
* **Names:** "Casaña law" (*Ley de Casaña*) is reserved for the complete method that takes τ_k to γ_k as exactly as possible. The sign alternation of Z at the midpoints of the corrected clock is called the **corrected Gram law**. `zCasanya` is the name of the data file built with cutoffs (8,8,512), not of a law.
* **Programs:** every reported number must come from a program committed to the repository, with its output committed next to it.
* **Literature:** claims taken from papers must be checked in the source before they are used.
* **Manuscript versions:** create a new version only when the author orders it. Every version gets a new integer number and is a self-contained paper, with no version history inside it. It is written in English LaTeX with an identical `.txt` copy; DOIs go in the references and the Python programs go in an appendix after the bibliography.

## 5. Current state (2026-10-18)

* Best zeta-free construction so far: certified monotone root (X = 16), then continuation of the root to cutoff (τ/2π)^c. On a test block: RMS 0.0212 (c = 1), 0.0164 (c = 1.15), 0.0128 (c = 1.30), against zCasanya 0.0403. The curve flattens; a floor near c ≈ 1.8 is possible (a 4-point estimate). Programs: `work/v15_prep/opc_task3*.py` and `opc_task4*.py`.
* Walk drift: dominated by the quotient pair 193/71 ≈ e (a continued-fraction convergent of e); see `work/v15_prep/outputs/task2_*`.
* Pending items for the next version: `work/notes/opc_pendiente_rutas_RH.md`.
