# Inventario editorial de resultados matemáticos en GitHub — 25 oct 2026

## Alcance y criterio
Se han revisado los árboles de los repositorios `vcasana1/LawCasanya`, `vcasana1/rational-resonances-liouville` y `vcasana1/AMP_LogPhaseWalk_Zeta_RVM_REPRODUCIBLE`, además de las auditorías internas más recientes. Existen 341 fuentes TeX en LawCasanya, pero muchas son versiones, copias y documentos auxiliares. Esto es una selección editorial de familias de resultados, **no una revisión línea por línea de todos los teoremas** ni una garantía de originalidad, arbitraje o aceptación. Las notas del autor tienen precedencia sobre conjeturas.

## A. Candidatos inmediatos a artículo independiente (pendientes de auditoría final)
1. **Rational Resonances and Microscopic Natural–Logarithmic Profiles for the Liouville Function**, `rational-resonances-liouville/submission/tex_resonant_liouville_JNT_FINAL_v2.tex`. Preparado con PDF, datos, scripts y comprobaciones. Partes incondicionales: aislamiento exacto de resonancias proporcionales, perfil logarítmico de un lado, ventana mayoritaria natural en resonancias enteras y régimen mesoscópico `theta<1/2`. El perfil natural racional general depende **expresamente** de Chowla afín; no anunciarlo como teorema incondicional. Prioridad **muy alta**.
2. **A Fixed-Mask Permutation Model for the Möbius Summatory Path**, `LawCasanya/work/drafts_autor/Downloads/Mobius_Fixed_Mask_Permutation_Model_Version_4.tex`. Fórmulas finitas exactas de media/covarianza, núcleo semiseparable, inversa tridiagonal, mínimo y propiedad M-convexa. Buen artículo de matemática discreta/probabilidad combinatoria después de cotejar novedad respecto de puentes hipergeométricos estándar.
3. **Möbius Surface Coordinates v6**, `LawCasanya/work/drafts_autor/Downloads/mobius_surface_padic_unimodular_v6/manuscript/mobius_surface_padic_unimodular_v6.tex`. Inversa unimodular, Gram por diferencias de `tau(gcd)`, identidades p-ádicas, `kappa_2(B_N) >= (1+o(1)) sqrt(2 N log N)`. Separar teoremas exactos de hipótesis de transporte.
4. **Reciprocal Sine Products and Centered Euclidean Kernels v9**, `LawCasanya/work/drafts_autor/PACK_PDF/Pis/reciprocal_sine_products_v9/reciprocal_sine_products_v9.tex`. Identidades exactas y para primos `log |P(p)|=-Cp+O(p^(1/3)(log p)^2)` propuesto con teorema Saffari–Vaughan; requiere verificar aplicación en diagonal y pérdidas en extremos. El control observado `max|H_p| ~ p^(1/3)` es conjetural.

## B. Prioridad alta, pero dividir y cerrar auditorías
5. **Prime-corrected clock** (Paper I, v14), `work/paper1/v14/manuscript/prime_corrected_clock_v14.tex`: momento de defecto para cortes `c<=1/2`, iteraciones, correcciones auditadas; candidato técnico central para teoría de números. `work/paper1/v14/audit/VERIFICACION_v14.md` y `revision_externa_cierre_v11.2_a_v14.md` documentan reparaciones, pero no certifican todos los resultados añadidos.
6. **Transport energy theorem v7**, `chatgpt/Basis for New Papers 24oct2026/transport_energy_theorem_v7.tex`: ley `(2pi^2)^(-1) logloglog T` para transporte de un paso bajo hipótesis precisas sobre teoremas auxiliares del Paper I. Publicable potencialmente como Paper II si se comprueban íntegros los enlaces de pruebas y dominios.
7. **CasanyaLaw I v20**, `chatgpt/manuscripts/CasanyaLawI_v20.tex`: dividir en (i) reloj/corrección prima y (ii) nota corta del defecto ordinal, multiplicidad horizontal y término exacto `1/12`; incluir desigualdad `B_T<=4 sum u_k(F)^2`, descomposición reloj + multiplicidad y extremos desplazados hasta `c<=5/3`. La reducción del integrando de seis piezas a dos respuestas discretas es exacta. Atribuir multiplicidad horizontal a GLSS, citar Gallagher–Mueller. **La v20 completa, de 64 páginas, no está lista como artículo unitario**, y la convergencia incondicional de `J_X^N` debe conservar sus reservas de Fourier/cortes.
8. **Orientation-Bit Geometry of the Möbius Path v6**, `work/drafts_autor/Downloads/orientation_bit_gram_geometry_v6.tex`: identidad de cociclos frontera, base Haar algebraica, criterio de observabilidad/no-go para filas sublineales. Publicable como nota de operadores discretos si se prueba que los resultados no son meras instancias conocidas.
9. **Analytic Möbius Prime Spectral Manuscript**, `work/drafts_autor/Downloads/ANALYTIC_MOBIUS_PRIME_SPECTRAL_MANUSCRIPT_FINAL.tex`: geometría elíptica de coeficientes, ley de `Delta_omega(Q)`, resonancia `n=3` a `omega=1`; la eliminación de regularización y la reconstrucción global de ceros no están demostradas.

## C. Artículos experimentales o de alcance limitado
10. **AMP LogPhaseWalk / Zeta RvM**: repositorio independiente con scripts y datos reproducibles; contraste Rayleigh planar frente a RvM y varios controles nulos. Para matemática experimental; no una demostración de GUE/RH.
11. **Möbius divisor surface GOE v5**, `work/drafts_autor/Downloads/mobius_gram_goe_conjecture_v5.tex`: matriz unimodular, inversa y trazas exactas, pruebas numéricas GOE; separar contribución algebraica de conjetura de universalidad.
12. **Prime spiral short v4**, `chatgpt/casanya_prime_spiral_short_v4_20261023/casanya_prime_spiral_short_v4.tex`: certificados locales Rouché con control del índice e identidades de frecuencias racionales. Confirmar certificación Arb de discos concretos; el reporte reconoce que 584/600 etiquetas experimentales anteriores no eran aún certificados indexados válidos.
13. **Li–Weil reflection matrices v22**, `work/drafts_autor/PACK_PDF/Matrix Weil-Li/reflection_li_weil_matrices_v22-copia.tex`: compresiones pares/impares, rango dos y Schur; equivalencia RH de positividad se fundamenta en Li–Weil y no demuestra RH. Publicable solo si se aisla contenido matricial nuevo y se coteja antecedentes.
14. **Heisenberg twisted Möbius theory**, `work/drafts_autor/Downloads/mobius_heisenberg_zeta_operator_theory_final.tex`: curvatura cocíclica y formas de Gram exactas, necesitaría separar el núcleo realmente nuevo de equivalencias/régimen hipotético.
15. **Leslie moving windows v9**, `work/drafts_autor/Downloads/leslie_mobius_ventanas_moviles_final_v9.tex`: dimensiones de estratos de recurrencia y transversabilidad, candidato especializado en dinámica algebraica tras verificar rangos y genericidad.

## D. Aún no como pruebas de RH ni como teoremas incondicionales
- `excursion_area_section_v56`: criterio de colisiones sobre ordenadas y transporte; la condición final que excluiría colisiones (y RH) no se demuestra.
- `rvm_zeta_pi_mertens_v26`: zeta sintética y rutas pi/M, faltan identificaciones y controles uniformes; no transferir RH por construcción de ceros sobre la recta.
- `Critical_Parameter_Rigidity_Zeta_v14` y `reflection_li_weil_matrices_v22`: separar rigidez/álgebra demostrada de condiciones de colapso o positividad que son equivalentes a RH.
- `montgomery_from_exponential_centroids_v1`: inversión exacta de centroides y contraejemplo del portador RvM, pero ley seno completa no se deduce de convergencia simple.
- `Catalan_Mertens_v9`, modelos GOE, módulos p-ádicos y otras rutas Mertens: publicar solo los teoremas finitos exactos previamente auditados, no los programas condicionales.

## Orden propuesto de envío
1. Liouville resonances v2 (paquete de sumisión y reproducibilidad ya integrado).
2. Fixed-mask permutation model v4, como artículo discreto/autónomo.
3. Möbius surface coordinates v6, con depuración de las afirmaciones más amplias.
4. Reciprocal sine products v9, tras cotejo estricto Saffari–Vaughan.
5. Prime-corrected clock (Paper I) y transport energy (Paper II), separados de criterios RH.
6. Nota breve de 1/12 y multiplicidad horizontal derivada de CasanyaLaw I v20.
7. Artículos experimentales AMP/GOE y certificados Rouché, explicitando límites.

## Control de versiones
La colección activa es `vcasana1/LawCasanya/chatgpt/manuscripts/`, no la biblioteca `LIBRARY-TOTAL-28oct2026` (esta última sigue sin cambios). La v20 ya está como TEX/TXT; se retiraron v18 TEX/TXT de la colección por petición del autor, conservándose los originales en el historial Git. PDF v20 existe en la conversación, no en GitHub.