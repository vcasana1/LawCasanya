# CasanyaLaw I — manuscript archive (v8–v18, selected archived versions)

Uploaded complete sources are here as LaTeX source and identical plain-text copies. No previous version was overwritten.

| Version | LaTeX | Identical TXT |
|---|---|---|
| v8 | [Source](CasanyaLawI_v8.tex) | [TXT](CasanyaLawI_v8.txt) |
| v9 | [Source](CasanyaLawI_v9.tex) | [TXT](CasanyaLawI_v9.txt) |
| v10 | [Source](CasanyaLawI_v10.tex) | [TXT](CasanyaLawI_v10.txt) |
| v11 | [Source](CasanyaLawI_v11.tex) | [TXT](CasanyaLawI_v11.txt) |
| v12 | [Source](CasanyaLawI_v12.tex) | [TXT](CasanyaLawI_v12.txt) |
| v13 | [Source](CasanyaLawI_v13.tex) | [TXT](CasanyaLawI_v13.txt) |
| v15 | [Source](CasanyaLawI_v15.tex) | [TXT](CasanyaLawI_v15.txt) |
| v18 (latest uploaded) | [Source](CasanyaLawI_v18.tex) | [TXT](CasanyaLawI_v18.txt) |

Each displayed LaTeX/TXT pair has the same Git blob SHA, proving byte-for-byte equality.

## Mathematical supporting files

- [v9 audit](../notes/CasanyaLawI_v9_auditoria.txt)
- [v9 mathematical gaps](../notes/CasanyaLawI_v9_lagunas_detectadas.txt)
- [v10 correction report](../notes/CasanyaLawI_v10_informe.txt)
- [v12 mathematical refutations](../notes/CasanyaLawI_v12_dictamen.txt)
- [v15 mathematical audit](../notes/CasanyaLawI_v15_auditoria_matematica.txt)
- [v18 build and change report](../notes/CasanyaLawI_v18_cambios_y_verificacion.txt)
- [Claude's v18 audit](../../work/notes/2026-10-25_auditoria_CasanyaLawI_v18.md)
- [Prime-power near-orthogonality](../notes/casi_ortogonalidad_potencias_primas_RvM.tex)
- [Index-dependent cutoff and Omega stability](../notes/lema_Omega_corte_variable_k.tex)
- [Recovered ordinal-defect and conditional Mertens arguments](../notes/2026-10-25_demostraciones_defecto_ordinal_y_M.md)
- [Claude's independent C1 boundary analysis](../../work/display/2026-10-25_prueba_completa_C1.md)

## Original PDF artifacts

The original PDF binaries are available in the author's ChatGPT conversation but could not be transferred by the available GitHub text-file connection. **They are not uploaded to this repository.** Rebuild PDFs locally from each LaTeX source, for example:

    latexmk -pdf -interaction=nonstopmode -halt-on-error CasanyaLawI_v18.tex

Original PDF byte sizes and SHA-256 checksums, for reference:

| PDF | Size (bytes) | SHA-256 |
|---|---:|---|
| v8 | 650045 | 4452ef8934b6d930088c77c05e98ed98e963b53bbef0eb1ef4a7af2dfdb26485 |
| v9 | 658018 | f80bfbc9eaf5af63a4df7be9a47ec6f3fbeb045a4aa6e2568fe28998076f1719 |
| v10 | 679760 | fd33143c482dff6414a0f5b787fb454902209923bd04714a9f1beed59df8c64e |
| v11 | 807007 | 91e96d1fc9a78d2cce3cbe9ffef9d17cebb87f86c57b08974e1fdc374e749e58 |
| v12 | 839220 | 368a2f835b83fc542538330192a7f8e6540b2a00a4efa50541fcd8e8daa59916 |
| v13 | 752427 | f25d0b17f80e1765768cadac0159d690b19fe5834c38ce5df8ad99c1e3b28e6e |
| v18 | 974807 | 87e1d8f52e94a0722a9dd58e4293f1aad848c09ba04ac9d704ea5d929f53bbb2 |

The SHA-256 values identify the original produced PDFs and do not imply bit-for-bit reproducibility from other installations.

## Mathematical status

No version constitutes a proof of RH. The ordinal, prime-counting and Mertens routes identify conditional comparison targets; do not confuse those implications with proven uniform transport estimates. In v18 the cubic boundary criterion is proved in the stated range, while Claude's wider proposed endpoint selection for c<5/3 is not integrated into the uploaded original.

Note: v14, v16 and v17 were produced as separate local/conversation deliverables; they are **not** represented as uploaded GitHub manuscript sources in this index. The v18 archive preserves its original text without inserting later suggestions.
