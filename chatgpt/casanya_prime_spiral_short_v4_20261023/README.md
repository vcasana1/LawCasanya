# Casaña prime-corrected clock — v4 (2026-10-23)

Author: Rotkiv Aynäsac. Archived on request from the prior ChatGPT delivery; not a new manuscript version beyond v4.

**Available in this directory**
- `casanya_prime_spiral_short_v4.tex` — complete 17-page article source.
- `casanya_prime_spiral_short_v4.txt` — byte-identical copy of the same LaTeX source.
- `audit_pairs_arb.py` — independent Arb/FLINT audit template for the pair examples around 1283 and 1290. Not executed in the ChatGPT environment.
- `rouche_one_zero_v4.py` — same-disc Arb/Turing index-validator correction; syntax checked in the original delivery but not executed here.
- `precheck_v4_appendix.py` — non-interval high-precision arithmetic cross-check, as printed in the appendix.

**Limits**
- The original Claude run in `work/paper1/rouche_cert/` reported 292/300 successful local tests in each of two blocks. Of the 584 positive statuses, 238 were Newton-recentered; the original code verified index membership only against an expanded radius around x, not the Rouché disc itself. Consequently these statuses are not all fully validated ordinal certificates until rerun with the corrected test.
- The pair examples' archived M3 bounds still require independent Arb verification. No universal RH claim.
- The `work/paper1/pendiente_siguiente_version/transporte_tabla7_2026-10-23.md` correction was committed separately by Claude after v4 and is not incorporated into this unchanged archive.

**Binary files:** the compiled PDF and full ZIP are available as files in the originating chat, but are **not committed to GitHub here**; this connector accepts UTF-8 text, and the original binary files cannot be read into this tool's upload payload. Compile the TEX with a LaTeX engine to recreate the PDF.

Historical filename `prime_spiral` does not assert that the meromorphic phase quotient has a proved geometrical spiral property.
