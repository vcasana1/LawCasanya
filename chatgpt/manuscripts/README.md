# CasanyaLaw I — manuscript archive (v8–v13)

All six complete versions are here as LaTeX source and identical plain-text copies. No previous version was overwritten.

| Version | LaTeX | Identical TXT |
|---|---|---|
| v8 | [Source](CasanyaLawI_v8.tex) | [TXT](CasanyaLawI_v8.txt) |
| v9 | [Source](CasanyaLawI_v9.tex) | [TXT](CasanyaLawI_v9.txt) |
| v10 | [Source](CasanyaLawI_v10.tex) | [TXT](CasanyaLawI_v10.txt) |
| v11 | [Source](CasanyaLawI_v11.tex) | [TXT](CasanyaLawI_v11.txt) |
| v12 | [Source](CasanyaLawI_v12.tex) | [TXT](CasanyaLawI_v12.txt) |
| v13 (latest) | [Source](CasanyaLawI_v13.tex) | [TXT](CasanyaLawI_v13.txt) |

Each LaTeX/TXT pair has the same Git blob SHA, proving byte-for-byte equality.

## Mathematical supporting files

- [v9 audit](../notes/CasanyaLawI_v9_auditoria.txt)
- [v9 mathematical gaps](../notes/CasanyaLawI_v9_lagunas_detectadas.txt)
- [v10 correction report](../notes/CasanyaLawI_v10_informe.txt)
- [v12 mathematical refutations](../notes/CasanyaLawI_v12_dictamen.txt)
- [Prime-power near-orthogonality](../notes/casi_ortogonalidad_potencias_primas_RvM.tex)
- [Index-dependent cutoff and Omega stability](../notes/lema_Omega_corte_variable_k.tex)
- [Recovered ordinal-defect and conditional Mertens arguments](../notes/2026-10-25_demostraciones_defecto_ordinal_y_M.md)
- [Claude's independent C1 boundary analysis](../../work/display/2026-10-25_prueba_completa_C1.md)

## Original PDF artifacts

The PDF binaries are available in the author's ChatGPT conversation but could not be transferred by the available GitHub text-file connection. **They are not uploaded to this repository.** Rebuild PDFs locally from each LaTeX source, for example:

    latexmk -pdf -interaction=nonstopmode -halt-on-error CasanyaLawI_v13.tex

Original PDF byte sizes and SHA-256 checksums, for reference:

| PDF | Size (bytes) | SHA-256 |
|---|---:|---|
| v8 | 650045 | 4452ef8934b6d930088c77c05e98ed98e963b53bbef0eb1ef4a7af2dfdb26485 |
| v9 | 658018 | f80bfbc9eaf5af63a4df7be9a47ec6f3fbeb045a4aa6e2568fe28998076f1719 |
| v10 | 679760 | fd33143c482dff6414a0f5b787fb454902209923bd04714a9f1beed59df8c64e |
| v11 | 807007 | 91e96d1fc9a78d2cce3cbe9ffef9d17cebb87f86c57b08974e1fdc374e749e58 |
| v12 | 839220 | 368a2f835b83fc542538330192a7f8e6540b2a00a4efa50541fcd8e8daa59916 |
| v13 | 752427 | f25d0b17f80e1765768cadac0159d690b19fe5834c38ce5df8ad99c1e3b28e6e |

The SHA-256 values identify the original produced PDFs and do not imply bit-for-bit reproducibility from other installations.

## Mathematical status

No version constitutes a proof of RH. The ordinal, prime-counting and Mertens routes in v13 identify conditional comparison targets; do not confuse those logical implications with proven uniform transport estimates.
