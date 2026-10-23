# LIBRARY TOTAL — índice maestro

Ruta en disco: `~/Documents/LIBRARY TOTAL/` (312 PDF).
Actualizado: 2026-10-23. Renumeración alfabética completa por autor, 001–312, sin excepciones (2026-10-23, tras añadir Arguin–Bourgade–Radziwiłł I y II). Orden ASCII del nombre sin número: mayúsculas antes que minúsculas, `-` antes que `_`. Nombre de fichero: `NNN_Autor_Año_Título.pdf`.

## Cómo usar este índice

1. Buscar aquí **antes** que en la web. `grep -i` sobre este fichero por tema, autor o palabra clave.
2. Citar **siempre por nombre de fichero completo**, no solo por número: el número cambia si se añaden PDF.
3. Antes de atribuir un enunciado a un paper, abrirlo y verificarlo. Este índice dice *dónde mirar*, no *qué afirmar*.
4. La colección histórica tiene capa OCR con errores, sobre todo en fórmulas: para citar una expresión hay que mirar la página. Los PDF sin capa de texto deben consultarse visualmente.

## Avisos de integridad

- Sin capa de texto (no grepeables; consultar visualmente): `046_Brent_1979_Zeros_Riemann_Zeta_Critical_Strip.pdf`, `124_Gonek_1985_Formula_Landau_Mean_Values_Zeta_INCOMPLETE_pp92-96.pdf`, `302_Volchkov_1995_Equality_Equivalent_Riemann_Hypothesis_Russian.pdf`.
- Año del nombre de fichero erróneo (es el identificador arXiv o una fecha ajena): `111_Frantzikinakis2020_1908_Correlations_of_multiplicative_functions_along_deterministic_and_independent_sequences.pdf` (2020), `132_GrepstadEtAl2019_1909_On_the_asymptotic_behaviour_of_the_sine_product.pdf` (2019), `226_Matiyasevich2007a_1983_Hidden_Life_of_Riemann_s_Zeta_Function_1_Arrow_Bow_and_Targets.pdf` (2007).
- **`003_Anonymous_2026_Unexpected_Phase_Summation_Patterns_Riemann_Zeros.pdf` no es de Riemann.** Es un preprint anónimo de 2026 (pdfTeX, 23-05-2026), *"Unexpected phase summation patterns in the imaginary parts of the Riemann zeros: a critical re-analysis"*, sobre las sumas parciales S(N) = Σ_{n≤N} e^{iγ_n}, con las citas rotas (`[?]`). Se llamaba `270_Riemann_1859_Number_Of_Primes_Below_A_Given_Magnitude.pdf`; renombrado el 2026-10-23 a `270_Anonymous_…` y, en la renumeración completa del mismo día, a `003_Anonymous_…`, su lugar alfabético. El texto real de Riemann está en `272_Riemann-Wilkins_1859_Prime_Counting_English_Translation.pdf` (texto alemán original, transcrito por D. R. Wilkins; el nombre del fichero dice `English_Translation` pero no lo es).
- **Renumeración completa del 2026-10-23**: los números anteriores (001–310 con el 270 fuera de orden) ya no valen. Las notas antiguas que citan por número deben leerse con la tabla de equivalencias `RENUMERACION_2026-10-23.md`.
- **`096_Edwards_1974_Riemanns_Zeta_Function.pdf` está incompleto**: el escaneo cubre las páginas impresas 1–122 de 311. Faltan los capítulos 7–12 y el apéndice. Detalle en §13.
- Tres artículos están escaneados a doble página (A4 apaisado, dos páginas impresas por hoja): `178_Jutila_1977_Zero_Density_Estimates_L_Functions.pdf`, `182_Kaczorowski_1991_k_Functions_Multiplicative_Number_Theory_V.pdf` y `270_Ramachandra_1976_Problems_Analytic_Number_Theory.pdf`. Al citar, hoja de PDF y página impresa no coinciden.
- **`168_Ivic_1985_Riemann_Zeta_Theory_Applications.pdf` y `170_Ivic_2003_Riemann_Zeta_Dover_Reprint.pdf` son el mismo libro.** El Dover 2003 es reimpresión sin abreviar de la Wiley 1985 — misma paginación — y solo aporta la lista de erratas (xvii–xix), extraída a `ERRATA_Ivic.md`. Esas erratas se aplican a ambos ficheros.
- Calidad no verificada / fuera de circuito arbitrado: `082_Dannon_2008_Riemann_Zeta_Function.pdf` (Gauge Institute), `301_Vega_2023_Simple_Proof_Riemann_Hypothesis.pdf`, `306_Youvan_2024_Phase_Winding_Riemann_Zeta.pdf` y el preprint anónimo `003_Anonymous_2026_Unexpected_Phase_Summation_Patterns_Riemann_Zeros.pdf`. Usar solo como material a contrastar, no como fuente.

## Huecos conocidos (citados en el trabajo, ausentes de la carpeta)

Comprobado el 2026-08-19. Al citarlos hay que decir que no están aquí.

- **Rudnick & Sarnak**, *Zeros of principal L-functions and random matrix theory*, Duke Math. J. **81** (1996), 269–322. Base del salto de estadística 2-level a n-level.
- **Forrester & Odlyzko**, *Gaussian unitary ensemble eigenvalues and Riemann zeta function zeros: a nonlinear equation for a new statistic*, Phys. Rev. E **54** (1996), R4493. Tratamiento Fredholm/Painlevé de nearest-neighbour; evita usar el Wigner surmise como exacto.
- **Kargin**, *Statistical properties of zeta functions' zeros*, Probability Surveys **11** (2014), 121–160, arXiv:1302.1452. El survey.

---

## 1. Núcleo RVM: sumas sobre ordenadas, fases y partes fraccionarias

- `007_Aryan_2019_Extension_Landau_Gonek_Formula.pdf` — extensión de la fórmula de Landau–Gonek; recupera sin RH consecuencias de pair correlation. arXiv:1902.05473
- `044_Brent-Platt-Trudgian_2020_Sums_Over_Zeros_Riemann_Zeta.pdf` — estimación explícita de sumas sobre ceros.
- `066_Coffey_2009_Certain_Sums_Over_Nontrivial_Zeta_Zeros.pdf` — coeficientes b_n como sumas sobre ceros y sobre las λ_j de Li/Keiper. arXiv:0912.2390
- `093_Durkan-Hughes-PearceCrump_2026_Generalisations_Landau_Gonek_Theorem.pdf` — sumas Σ_ρ χ(ρ)X^ρ; sensibilidad a la naturaleza aritmética de X. arXiv:2601.18025
- `169_Ivic_2001_Sums_Over_Ordinates_Zeta_Zeros.pdf` — G(s) = Σ_{γ>0} γ^{-s}; evaluación de sumas sobre γ e integrales de S(T). **Referencia base.**
- `246_Murahara-Onozuka_2025_Equidistribution_A_Points_Zeta_Derivatives.pdf` — sumas exponenciales sobre a-puntos de derivadas de ζ, siguiendo a Fujii. arXiv:2510.07710
- `003_Anonymous_2026_Unexpected_Phase_Summation_Patterns_Riemann_Zeros.pdf` **(preprint anónimo, ver avisos)** — sumas parciales S(N)=Σ e^{iγ_n}, banda estrecha de |S(N)|, picos y espaciados multimodales. Directamente sobre tu problema.
- `306_Youvan_2024_Phase_Winding_Riemann_Zeta.pdf` — dinámica de bobinado de fase de ζ, heatmaps y estadística. Sin arbitraje.
- `101_Ford-Meng-Zaharescu_2017_Simultaneous_Fractional_Parts.pdf` — distribución simultánea de {α_1γ,…,α_nγ}. arXiv:1511.06814
- `102_Ford-Soundararajan-Zaharescu_2009_Imaginary_Parts_II.pdf` — partes fraccionarias de αγ, continuación. arXiv:0805.2745
- `103_Ford-Zaharescu_2005_Imaginary_Parts_Zeta_Zeros.pdf` — partes fraccionarias de αγ, primer trabajo de la serie.
- `278_Saffari-Vaughan_1977_Fractional_Parts_X_Over_N_II.pdf` — partes fraccionarias de x/n y sucesiones relacionadas.
- `008_Aryan_2022_Extension_Landau_Gonek_Formula_Published.pdf` — versión publicada de la extensión de la fórmula de Landau–Gonek. J. Number Theory 233 (2022) 389–404
- `124_Gonek_1985_Formula_Landau_Mean_Values_Zeta_INCOMPLETE_pp92-96.pdf` — Gonek, fórmula de Landau y valores medios de ζ; **incompleto (solo pp. 92–96) y sin capa de texto**
- `134_Guillera_2013_Sums_Nontrivial_Zeros_Riemann_Zeta.pdf` — identidades con sumas sobre los ceros no triviales; desarrollos asintóticos en la línea de Cramér. arXiv:1307.5723
- `181_KaczorowskiLanguascoPerelli2000_2000_A_note_on_Landau_s_formula.pdf` — forma ponderada de la versión uniforme de Gonek de la fórmula de Landau. Funct. Approx. 28 (2000) 173–186

## 2. Pair correlation de Montgomery

- `241_Montgomery_1973_Pair_Correlation_Zeros_Zeta.pdf` — **el original**. F(α), 2/3 de ceros simples bajo RH.
- `018_Baluyot-Goldston-etal_2025_Pair_Correlation_Zeros_I_Proportions_Simple_Critical.pdf` — proporciones de ceros simples y en la crítica. arXiv:2501.14545
- `056_Carneiro-Chandee-Littmann-Milinovich_2014_Hilbert_Spaces_Pair_Correlation.pdf` — N(T,β) vía espacios de Hilbert de funciones enteras. arXiv:1406.5462
- `057_Carneiro-Milinovich-Ramos_2023_Fourier_Optimization_Montgomery_Pair_Correlation.pdf` — cotas del promedio de F(α,T) por optimización de Fourier. arXiv:2310.01913
- `061_Chan_2002_More_Precise_Pair_Correlation_Zeros_Primes_Short_Intervals.pdf` — segundos términos principales en la equivalencia Goldston–Montgomery.
- `071_Conrey-Keating_2016_Pair_Correlation_Twin_Primes_Revisited.pdf` — conexión ratios-conjecture / correlaciones aritméticas. arXiv:1604.06124
- `031_Bogomolny-Keating_1995_Random_Matrix_Theory_Riemann_Zeros_I_Three_Four_Point_Correlations.pdf` — correlaciones de 3 y 4 puntos de los ceros = GUE desde Hardy–Littlewood. doi:10.1088/0951-7715/8/6/013
- `032_Bogomolny-Keating_1996_Gutzwiller_Trace_Formula_Spectral_Statistics_Beyond_Diagonal.pdf` — correlación de dos puntos más allá de la aproximación diagonal; para ζ equivale a Hardy–Littlewood para pares de primos. doi:10.1103/PhysRevLett.77.1472
- `033_Bogomolny-Keating_1996_Random_Matrix_Theory_Riemann_Zeros_II_n_Point_Correlations.pdf` — correlaciones de n puntos = GUE para todo n, desde Hardy–Littlewood. doi:10.1088/0951-7715/9/4/006
- `083_Das-Ismoilov-Ramos_2025_Fourier_Optimization_Pair_Correlation_Problems.pdf` — marco genérico de cotas de pair correlation. arXiv:2502.05106
- `121_Goldston-Lee-Schettler-Suriajaya_2025_Pair_Correlation_Conjecture_II_Alternative_Hypothesis.pdf` — PCC bajo hipótesis alternativa. arXiv:2507.06823
- `122_Goldston-Lee-Schettler-Suriajaya_2025_Pair_Correlation_Conjecture_I_Simple_Critical.pdf` — PCC sin RH y ceros simples. arXiv:2503.15449
- `193_Kolountzakis-Revesz_2003_Turan_Extremal_Problem.pdf` — problema extremal de Turán; herramienta de optimización de Fourier.
- `117_GPY2009_2009_Annals_of_Mathematics.pdf` — Goldston–Pintz–Yıldırım, *Primes in tuples I*. Ann. of Math. 170 (2009)
- `240_MontgomerySoundararajan2004_2004_Comm_Math_Phys.pdf` — primos en intervalos cortos: varianza menor que la del modelo de Cramér. arXiv:math/0409258

## 3. Gaps entre ceros y arg ζ

- `113_Fujii_1974_Zeros_Dirichlet_L_Functions_I.pdf` — momentos de S(t+h)−S(t) (y de L(s,χ)) en intervalos cortos, con prueba; incondicional. Trans. AMS 196 (1974), DOI 10.1090/S0002-9947-1974-0349603-2
- `116_Fujii_1981_Zeros_Dirichlet_L_Functions_II_Corrections.pdf` — pruebas completas de consecuencias del teorema principal de Fujii 1974 (momentos de S(t+h)−S(t)), con correcciones a la parte I y a los artículos siguientes. Trans. AMS 267 (1981).
- `115_Fujii_1975_Distribution_Zeros_Zeta_Short_Intervals.pdf` — momentos de S(t+h)−S(t) en intervalos cortos (anuncio, sin pruebas). Bull. AMS 81 (1975), DOI 10.1090/S0002-9904-1975-13674-3
- `158_Hughes-Rudnick_2002_Linear_Statistics_Zeros_Zeta.pdf` — estadísticos lineales de ceros escalados; momentos gaussianos. arXiv:math/0208220
- `114_Fujii_1975_Difference_r_Consecutive_Ordinates_Zeros_Zeta.pdf` — momentos incondicionales de diferencias de r ordenadas consecutivas, muestreados en los ceros; conteo de r-gaps pequeños. Proc. Japan Acad. 51 (1975), DOI 10.3792/pja/1195518466
- `072_Conrey-TurnageButterbaugh_2018_r_Gaps_Between_Zeros_Zeta.pdf` — r-gaps, constantes explícitas bajo RH. arXiv:1708.00030
- `123_Gonek-Sahay_2024_Consecutive_Moderate_Gaps_Between_Zeros_Zeta.pdf` — gaps consecutivos moderados. arXiv:2412.15481
- `165_Inoue-Kobayashi-Toma_2026_Explicit_Extreme_Values_Argument_Zeta.pdf` — valores extremos explícitos de arg ζ; mejora Conrey–Turnage-Butterbaugh. arXiv:2510.14309
- `167_Ivic-Korolev_2018_Distribution_Values_Argument_Zeta.pdf` — distribución del signo de S(t): medida de {t∈[T,T+H]: S(t)>0} para T^{27/82+ε} ≤ H ≤ T.
- `200_Korolev_2016_Extreme_Values_S_Short_Intervals_Indian_J.pdf` — máximo y mínimo de S(t) en segmentos muy cortos de la recta crítica, bajo RH. Indian J. Pure Appl. Math. 47 (2016) 603–615, DOI 10.1007/s13226-016-0205-4
- `166_Inoue_2024_Note_On_r_Gaps_Between_Zeros_Zeta.pdf` — prueba del resultado anunciado por Selberg sobre r-gaps. arXiv:2303.06613
- `309_Zhao_2026_Density_Results_r_Gaps_Between_Zeros_Zeta.pdf` — resultados de densidad para r-gaps. arXiv:2603.17334
- `198_Korolev_2012_Gram_Law_Argument_Riemann_Zeta_Publ_Inst_Math.pdf` — ley de Gram y S(t) en los puntos de Gram; fórmulas de Selberg para momentos de Δ_n en intervalos cortos (Teorema 4.2). Publ. Inst. Math. 92(106) (2012), DOI 10.2298/PIM1206053K
- `199_Korolev_2012_Gram_Law_Riemann_Zeta.pdf` — ley de Gram, fórmulas de Selberg. arXiv:1011.3997
- `196_Korolev_2010_Gram_Law_Selberg_Conjecture_Zeros_Izv_Math.pdf` — ley de Gram y conjetura de Selberg sobre la distribución de los ceros. Izv. Math. 74 (2010) 743, DOI 10.1070/IM2010v074n04ABEH002506
- `197_Korolev_2011_Gram_Law_Argument_Riemann_Zeta_arXiv.pdf` — S(t) en los puntos de Gram; panorámica de los sentidos de "ley de Gram"; fórmulas de Selberg. arXiv:1106.0516
- `201_Korolev_2016_Gram_Law_Theory_Zeta_Part1_Proc_Steklov.pdf` — monografía (146 pág.) sobre la ley de Gram en la teoría de ζ, parte 1. Proc. Steklov Inst. Math. 292, suppl. 2 (2016) S1–S146, DOI 10.1134/S0081543816030019
- `172_Jerby_2023_New_Discriminant_Hardy_Z_Function_Corrected_Gram_Law.pdf` — discriminante Δ_n(a) de Z(t), ley de Gram corregida. arXiv:2310.14415
- `298_Trudgian_2008_Gram_Law_Fails_Positive_Proportion_Of_The_Time.pdf` — proporción positiva de fallos de la ley de Gram y de éxitos débiles. arXiv:0811.0883
- `107_Franca-LeClair_2014_Statistical_Properties_Riemann_Zeros_Explicit_Equation_nth_Zero.pdf` — ecuación para el n-ésimo cero con Lambert W (ỹ_n, sin puntos de Gram ni ley de Gram) y término arg ζ; reconstruye π(x) con ceros sintéticos. arXiv:1307.8395
- `108_Franca-LeClair_2014_Theory_Zeros_Riemann_Zeta_And_Other_L_Functions.pdf` — notas de curso: ceros de la línea crítica ↔ ceros del coseno, ecuación del n-ésimo cero, L-funciones. arXiv:1407.4358
- `110_Franca-LeClair_2015_Transcendental_Equations_Individual_Zeros_L_Functions_CNTP_Published.pdf` — versión publicada de la ecuación trascendente del n-ésimo cero (CNTP 9 (2015) 1–50).
- `214_LeClair_2016_Riemann_Hypothesis_Random_Walks_Zeta_Case.pdf` — producto de Euler truncado en N(t)<[t²], B_N(t)=O(√N) vía Kac, argumento heurístico de S(t)=O(1), modelo probabilístico de ceros y cero 10^100. arXiv:1601.00914
- `021_Bellotti-Wong_2025_Improved_Argument_Zero_Counting_Zeta.pdf` — cota explícita |N(T) − (T/2π)log(T/2πe)| ≤ 0.10076 log T + 0.24460 log log T + 8.08344. arXiv:2412.15470
- `075_Conrey_1989_More_Than_Two_Fifths_Zeros_Critical_Line.pdf` — Conrey, más de dos quintos de los ceros en la recta crítica. J. reine angew. Math. 399 (1989)
- `109_Franca-LeClair_2015_Transcendental_Equations_Individual_Zeros_L_Functions.pdf` — versión arXiv de las ecuaciones trascendentes para ceros individuales (publicada: `110_Franca-LeClair_2015_Transcendental_Equations_Individual_Zeros_L_Functions_CNTP_Published.pdf`). arXiv:1502.06003
- `143_Hasanalizade-Shen-Wong_2022_Counting_Zeros_Riemann_Zeta.pdf` — cota explícita |N(T) − (T/2π)log(T/2πe)| ≤ 0.1038 log T + 0.2573 log log T + 9.3675. arXiv:2107.06506
- `299_Trudgian_2014_Improved_Upper_Bound_Argument_Zeta_II.pdf` — cota superior mejorada para S(T) en la recta crítica, II. Math. Comp. arXiv:1208.5846

## 4. RMT, GUE/CUE y estadística de espaciados

- `027_Berry_1988_Semiclassical_Formula_Number_Variance_Riemann_Zeros.pdf` — varianza del número de ceros desde los primos: régimen universal GUE y régimen no universal por primos, separados por la escala τ*. doi:10.1088/0951-7715/1/3/001
- `255_Odlyzko_1987_Distribution_Spacings_Between_Zeros_Zeta.pdf` — **datos base**: 10^5 ceros y ceros 10^12+1…10^12+10^5, precisión 10^-8.
- `106_Forrester-Mays_2015_Finite_Size_Corrections_RMT_Odlyzko_Data.pdf` — correcciones de tamaño finito contra el dataset de Odlyzko. arXiv:1506.06531
- `040_Bornemann-Forrester-Mays_2017_Finite_Size_Effects_Spacing_Distributions.pdf` — efectos de tamaño finito en distribuciones de espaciado. arXiv:1608.04638
- `250_Nishigaki_2024_Consecutive_Level_Spacings_GUE_Ratio.pdf` — espaciados consecutivos GUE y su ratio, derivación ab initio. doi:10.1093/ptep/ptae120
- `251_Nishigaki_2025_Consecutive_Level_Spacings_CUE_Finite_Size_Zeta.pdf` — lo mismo para CUE, con correcciones finitas y ceros de ζ.
- `284_Shir-MartinezAzcona-Chenu_2025_Surmise_Level_Spacing_Beyond_Nearest.pdf` — surmise más allá del vecino inmediato. arXiv:2504.20134
- `034_Bohigas-Leboeuf-Sanchez_2001_Spectral_Spacing_Correlations.pdf` — autocovarianzas de espaciados como función de correlación discretizada.
- `105_Forrester-Lebowitz_2013_Local_CLT_Determinantal_Point_Processes.pdf` — TCL local para procesos determinantales. arXiv:1311.7126
- `173_Johansson_2001_Discrete_Orthogonal_Polynomial_Ensembles_Plancherel.pdf` — ensembles discretos de polinomios ortogonales.
- `188_Kargin_2013_Fluctuations_Riemann_Zeta_Zeros.pdf` — *On fluctuations of Riemann's zeta zeros*, arXiv:1203.5309, 25 pág. Fluctuaciones gaussianas de γ_k en torno a su posición predicha; ley conjunta de γ_k y γ_{k+x} con correlación (1-β)₊. **No confundir** con Kargin, *Statistical properties of zeta functions' zeros*, Probability Surveys 11 (2014), arXiv:1302.1452 — ese es el survey (soporte de Fourier en Montgomery, escalas, qué es local), y **no está en la biblioteca**.
- `099_Fazzari-Gerspach-Minelli_2025_Selberg_CLT_Weighted_Linear_Statistics_Zeta_Zeros.pdf` — TCL de Selberg ponderado por estadística local de ceros. arXiv:2507.04150
- `059_Cartier-Julia-Moussa-Vanhove_2006_Random_Matrices_Zeta_Dynamical_Systems.pdf` — actas *Frontiers in Number Theory, Physics and Geometry I*.
- `041_Borwein-Straub-Wan-Zudilin_2012_Densities_Short_Uniform_Random_Walks.pdf` — densidades de paseos aleatorios uniformes cortos (3–5 pasos); referencia para caminatas de fase. arXiv:1103.2995
- `073_ConreySnaith2008_2008_Communications_in_Number_Theory_and_Physics.pdf` — correlaciones de autovalores y ceros de Riemann (cocientes de polinomios característicos). CNTP (2008). arXiv:0803.2795
- `098_ErdosEtAl2012_2012_Spectral_statistics_of_Erd.pdf` — estadística espectral de grafos de Erdős–Rényi II: espaciados y autovalores extremos. arXiv:1103.3869
- `150_HeuslerEtAl2007_2007_Periodic_orbit_theory_of_level_correlations.pdf` — teoría de órbitas periódicas de las correlaciones de niveles. arXiv:nlin/0610053
- `245_MullerEtAl2005_2005_Periodic_orbit_theory_of_universality_in_quantum_chaos.pdf` — teoría de órbitas periódicas de la universalidad en caos cuántico. arXiv:nlin/0503052
- `264_PillaiYin2014_2014_Universality_of_covariance_matrices.pdf` — universalidad de matrices de covarianza. Ann. Appl. Probab. 24 (2014), DOI 10.1214/13-AAP939

## 5. Criterio de Li–Weil y positividad

- `065_Coffey_2005_Polygamma_Theory_Li_Keiper_Constants_Riemann_Hypothesis.pdf` — constantes λ_k y c_n, teoría poligamma.
- `281_Sekatskii_2013_Generalized_Bombieri_Lagarias_Li_Criterion.pdf` — teorema de Bombieri–Lagarias generalizado y criterio de Li generalizado.
- `282_Sekatskii_2014_Generalized_Li_Criterion_Zeroes_Location.pdf` — primeras aplicaciones a la localización de ceros. arXiv:1304.7895
- (ver también `066_Coffey_2009_Certain_Sums_Over_Nontrivial_Zeta_Zeros.pdf`)
- `006_AriasdeReyna_2024_Explicit_Formula_Quasicrystal_Definition.pdf` — RH ⇔ cierta medida con Λ(n) y cosh(x/2) es una distribución temperada; definición de cuasicristal de Fourier. arXiv:2402.10604
- `013_BaezDuarte-Balazard-Landreau-Saias_2000_Notes_sur_la_fonction_zeta_de_Riemann_3.pdf` — Báez-Duarte–Balazard–Landreau–Saias, criterio de Nyman–Beurling (distancias). Adv. Math. 149 (2000), DOI 10.1006/aima.1999.1861
- `014_BaezDuarte2002_2002_BaezDuarte2002.pdf` — refuerzo del criterio de Nyman–Beurling. arXiv:math/0202141
- `016_Balazard-Saias-Yor_1999_Notes_Fonction_Zeta_Riemann_2_Transcription_VellaChemla.pdf` — ∫ log|ζ| sobre la recta crítica en términos de los ceros con Re ρ > 1/2. Adv. Math. 143 (1999); transcripción
- `068_Connes1998_1998_Connes1998.pdf` — Connes, fórmula de traza en geometría no conmutativa y ceros de ζ (espectro de absorción). arXiv:math/9811068
- `210_Lagarias2007_2007_Li_coefficients_for_automorphic_functions.pdf` — Lagarias, coeficientes de Li para L-funciones automorfas. Ann. Inst. Fourier 57 (2007)
- `274_RodgersTao2018_2018_RodgersTao2018.pdf` — Rodgers–Tao, la constante de de Bruijn–Newman es no negativa. arXiv:1801.05914
- `280_Sekatskii-Beltraminelli-Merlini_2012_Integrals_Logarithm_Zeta_RH.pdf` — igualdades con integrales de log ζ equivalentes a RH (teorema de Littlewood generalizado)
- `290_Suzuki2025Hilbert_2025_On_the_Hilbert_space_derived_from_the_Weil_distribution.pdf` — Suzuki, espacio de Hilbert derivado de la distribución de Weil. Canad. J. Math. (2025), DOI 10.4153/S0008414X25101739
- `302_Volchkov_1995_Equality_Equivalent_Riemann_Hypothesis_Russian.pdf` — Volchkov, igualdad equivalente a RH (en ruso; **sin capa de texto**)
- `303_Weil_1952_Formules_Explicites_Nombres_Premiers_Transcription_VellaChemla.pdf` — Weil, *Sur les « formules explicites »* (1952); transcripción
- `310_deBruijn1950_1950_The_roots_of_trigonometric_integrals.pdf` — de Bruijn, raíces de integrales trigonométricas (origen de la constante de de Bruijn–Newman). Duke Math. J. 17 (1950) 197–226, DOI 10.1215/S0012-7094-50-01720-0

## 6. Matrices aritméticas: Redheffer, Toeplitz multiplicativas, GCD, Hilbert

- `020_Barrett-Jarvis_1992_Spectral_Properties_Redheffer_Matrix.pdf` — det A_n = M(n); propiedades espectrales.
- `300_Vaughan_1996_Eigenvalues_Redheffer_Matrix_II.pdf` — estimaciones precisas de autovalores. doi:10.1017/S1446788700037654
- `304_Wilf_2004_Redheffer_Matrix_Partially_Ordered_Set.pdf` — permutaciones que contribuyen al determinante; permanente.
- `275_Roesler_1986_Riemann_Hypothesis_Eigenvalue_Problem.pdf` — RH como problema de autovalores de una matriz entera.
- `276_Roesler_1987_Riemann_Hypothesis_Eigenvalue_Problem_II.pdf` — continuación; distribución de autovalores.
- `153_Hilberdink_2006_Determinants_Multiplicative_Toeplitz_Matrices.pdf` — a_ij = f(i/j) con f multiplicativa; determinantes truncados.
- `154_Hilberdink_2015_Multiplicative_Toeplitz_Matrices_Riemann_Zeta.pdf` — conexión directa con ζ.
- `155_Hilberdink_2017_Singular_Values_Multiplicative_Toeplitz_Matrices.pdf` — valores singulares. doi:10.1080/03081087.2016.1204978
- `152_Hilberdink-Pushnitski_2023_Spectral_Asymptotics_LCM_Matrices.pdf` — asintótica espectral de matrices n^σ m^σ / [n,m]^τ. arXiv:2110.14323
- `221_Lindqvist-Seip_1998_Note_Greatest_Common_Divisor_Matrices.pdf` — formas cuadráticas de matrices GCD como normas L².
- `048_Brevig-Perfekt-Seip-Siskakis-Vukotic_2016_Multiplicative_Hilbert_Matrix.pdf` — la matriz de Hilbert multiplicativa. arXiv:1411.7294
- `263_Perfekt-Pushnitski_2018_Spectrum_Multiplicative_Hilbert_Matrix.pdf` — su espectro. arXiv:1705.01959
- `254_Odlyzko-TeRiele_1985_Disproof_Mertens_Conjecture.pdf` — refutación de la conjetura de Mertens.
- `186_Kannan-Bachem_1979_Polynomial_Algorithms_Smith_Hermite_Normal_Forms.pdf` — algoritmos polinómicos para formas normales.
- `209_Labahn-Neiger-Zhou_2018_Hermite_Normal_Form_Polynomial_Matrix.pdf` — forma normal de Hermite para matrices polinómicas. arXiv:1607.04176
- `277_Rota_1964_Foundations_Combinatorial_Theory_Mobius_Functions.pdf` — funciones de Möbius sobre posets.
- `226_Matiyasevich2007a_1983_Hidden_Life_of_Riemann_s_Zeta_Function_1_Arrow_Bow_and_Targets.pdf` — Matiyasevich, RH reformulada como enunciados sobre autovalores de matrices (1). arXiv:0707.1983
- `227_Matiyasevich2007b_2007_Hidden_Life_of_Riemann_s_Zeta_Function_2_Electrons_and_Trains.pdf` — Matiyasevich, ídem (2). arXiv:0709.0028
- `239_Montgomery-Vaughan_1974_Hilberts_Inequality.pdf` — Montgomery–Vaughan, desigualdad de Hilbert generalizada

## 7. Sumas exponenciales y métodos de Van der Corput / Vinogradov

- `128_Graham-Kolesnik_1991_Computing_Optimal_Exponent_Pairs.pdf` — cálculo de pares de exponentes óptimos (cap. 5).
- `129_Graham-Kolesnik_1991_Simplest_Van_Der_Corput_Estimates.pdf` — estimaciones vdC de primera y segunda derivada (cap. 2).
- `042_Bourgain_2017_Decoupling_Exponential_Sums_Riemann_Zeta.pdf` — desacoplamiento; ζ(1/2+it) ≪ t^{13/84+ε}; par de exponentes (13/84, 55/84). arXiv:1408.5794v2, J. Amer. Math. Soc. 30 (2017)
- `191_Kinnunen_1997_Hardy_Littlewood_Maximal_Function_Sobolev_Function.pdf` — análisis armónico auxiliar: maximal de Hardy–Littlewood acotado en W^{1,p}, |D Mu| ≤ M Du. Israel J. Math. 100 (1997)
- `162_Huxley_1989_Exponential_Sums_Riemann_Zeta.pdf` — método de Bombieri–Iwaniec, trabajo Huxley–Watt en contexto.
- `187_Karatsuba-Voronin_1992_Vinogradov_Method_Riemann_Zeta.pdf` — método de Vinogradov, teorema del valor medio (cap. IV).
- `019_Baricz-Laforgia-Pogany_2015_Van_Der_Corput_Inequalities_Bessel.pdf` — desigualdades vdC para funciones de Bessel. doi:10.1080/10652469.2014.975419
- `189_Kelly-Le_2018_Van_Der_Corput_Sets_Compact_Groups.pdf` — conjuntos vdC en grupos compactos. doi:10.1007/s00013-017-1136-y
- `205_Kowalski_2021_Exponential_Sums_Finite_Fields_Elementary.pdf` — métodos elementales, curso ETH.
- `206_Kowalski_2021_Exponential_Sums_Finite_Fields_II.pdf` — métodos cohomológicos.
- `177_Jun-Lee_2014_Dedekind_And_Exponential_Sums.pdf` — equidistribución de sumas de Dedekind generalizadas. doi:10.1016/j.jnt.2013.10.020
- `252_Norvidas_2011_Entire_Functions_Exponential_Sums.pdf` — espacios de Bernstein y sumas exponenciales.
- `104_Ford_2002_Vinogradov_Integral_Bounds_Riemann_Zeta.pdf` — Ford, integral de Vinogradov y cotas para ζ; región libre de ceros. arXiv:1910.08209
- `132_GrepstadEtAl2019_1909_On_the_asymptotic_behaviour_of_the_sine_product.pdf` — comportamiento asintótico del producto de senos Π|2 sin πrα|. arXiv:1909.00980
- `136_Guth-Maynard_2026_New_Large_Value_Estimates_Dirichlet_Polynomials.pdf` — Guth–Maynard, nuevas estimaciones de valores grandes de polinomios de Dirichlet. arXiv:2405.20552
- `219_LiYang2023_2023_An_improvement_on_Gauss_s_circle_problem_and_Dirichlet_s_divisor_problem.pdf` — mejora en el problema del círculo de Gauss y del divisor de Dirichlet (Bombieri–Iwaniec). arXiv:2308.14859

## 8. Funciones multiplicativas: Liouville, Möbius, Chowla

- `231_Matomaki-Radziwill_2016_Multiplicative_Functions_Short_Intervals.pdf` — **el teorema MR**: promedios cortos vs. largos. doi:10.4007/annals.2016.183.3.6
- `229_Matomaki-Radziwill_2015_Liouville_Short_Intervals.pdf` — prueba corta y autocontenida para λ(n). arXiv:1502.02374
- `228_Matomaki-Radziwill-Tao_2015_Averaged_Chowla_Conjecture.pdf` — Chowla promediada. arXiv:1503.05121
- `140_Harman-Pintz-Wolke_1985_Mobius_And_Liouville_Functions.pdf` — nota sobre valores de μ y λ.
- `060_Cassaigne-Ferenczi-Mauduit-Rivat-Sarkozy_1999_Liouville_Pseudorandom_Sequences.pdf` — λ como sucesión binaria pseudoaleatoria.
- `080_Croot_2003_Oscillations_Multiplicative_PlusMinusOne.pdf` — oscilaciones de funciones multiplicativas ±1. [texto extraído ilegible]
- `130_Granville-Soundararajan_2003_Decay_Of_Mean_Values.pdf` — decaimiento de valores medios. [texto extraído ilegible]
- `279_Sawin_2022_Mobius_Cancellation_Polynomial_Sequences.pdf` — cancelación de Möbius en F_q[u], análogo de Chowla. doi:10.1007/s00222-022-01115-y
- `092_Drmota_2009_Sum_Of_Digits_Of_Primes.pdf` — suma de dígitos de los primos (charla, con Mauduit y Rivat).
- `001_AbercrombieBanksShparlinski2009_2009_Arithmetic_functions_on_Beatty_sequences.pdf` — funciones aritméticas sobre sucesiones de Beatty. Acta Arith. 136 (2009), DOI 10.4064/aa136-1-6
- `011_Aymone-Sidoravicius_2017_Partial_Sums_Biased_Random_Multiplicative_Functions.pdf` — sumas parciales de funciones multiplicativas aleatorias sesgadas. arXiv:1412.1157
- `012_Aymone2020_2020_A_note_on_multiplicative_functions_resembling_the_M_bius_function.pdf` — funciones multiplicativas que se parecen a μ con M_f(x)=o(√x). arXiv:1908.11014
- `025_BergelsonKulagaPrzymusLemanczykRichter2019_2019_Discrete_Contin_Dyn_Syst.pdf` — generalización del criterio de ortogonalidad de Kátai. arXiv:1705.07322
- `029_Bjorner_2011_Cell_Complex_Number_Theory.pdf` — Björner, complejo simplicial de los libres de cuadrados; característica de Euler = función de Mertens. arXiv:1101.5704
- `043_Bourgain_undated_On_the_Fourier_Walsh_spectrum_of_the_M_obius_function.pdf` — Bourgain, espectro de Fourier–Walsh de μ. arXiv:1112.1423
- `047_BretcheDressTenenbaum2020_2020_Mathematika.pdf` — de la Bretèche–Dress–Tenenbaum, la suma M(n,z)=Σ_{d|n, d≤z} μ(d). arXiv:1902.09956
- `077_Coons2010_2010_On_the_multiplicative_Erd_s_discrepancy_problem.pdf` — problema de discrepancia de Erdős multiplicativo. arXiv:1003.5388
- `111_Frantzikinakis2020_1908_Correlations_of_multiplicative_functions_along_deterministic_and_independent_sequences.pdf` — correlaciones de funciones multiplicativas sobre sucesiones deterministas e independientes (2020; el «1908» del nombre es el id arXiv). arXiv:1908.02732
- `142_Harper_2020_Moments_Random_Multiplicative_Functions_I.pdf` — Harper, momentos bajos de funciones multiplicativas aleatorias; caos multiplicativo crítico. arXiv:1703.06654
- `147_HelfgottRadziwill2021_undated_HelfgottRadziwill2021.pdf` — Helfgott–Radziwiłł, expansión, divisibilidad y paridad. arXiv:2103.06853
- `180_Kaczorowski-Pintz_1986_Oscillatory_Properties_Arithmetical_Functions_I.pdf` — Kaczorowski–Pintz, propiedades oscilatorias de funciones aritméticas I. Acta Math. Hung. 48 (1986)
- `202_Kotnik-vandeLune_2004_Order_Mertens_Function.pdf` — Kotnik–van de Lune, orden de la función de Mertens (experimento numérico sobre M(x)/√x)
- `215_LeeLeong2024_2024_New_explicit_bounds_for_the_Mertens_function_and_the_reciprocal_of_the_Riemann_zeta_function.pdf` — cotas explícitas incondicionales para M(x) y para 1/ζ en la banda crítica. arXiv:2208.06141
- `223_Liu2022_2022_Multiplicative_functions_resembling_the_M_bius_function.pdf` — funciones multiplicativas parecidas a μ: resultados O y Ω. arXiv:2205.00972
- `232_Matomaki-Shao-Tao-Teravainen_2023_Higher_Uniformity_Arithmetic_Functions.pdf` — uniformidad superior de μ, Λ y d_k en intervalos cortos. arXiv:2204.03754
- `233_Matomaki-Teravainen_2023_Mobius_Function_All_Short_Intervals.pdf` — μ en todos los intervalos cortos, Σ_{x<n≤x+x^θ} μ(n)=o(x^θ) para θ>0.55. arXiv:1911.09076
- `236_MelottiSaias2020_2020_On_path_partitions_of_the_divisor_graph.pdf` — particiones en caminos del grafo de divisores. arXiv:1807.07783
- `237_Mirsky_1949_Frequency_Pairs_Square_Free_Numbers_Given_Difference.pdf` — Mirsky, frecuencia de pares de libres de cuadrados con diferencia dada (1949)
- `242_MossinghoffOliveiraTrudgian2021_2021_The_distribution_of_k_free_numbers.pdf` — distribución de los k-libres: error R_k(x). arXiv:1912.04972
- `244_Muellner2017_2017_Automatic_sequences_fulfill_the_Sarnak_conjecture.pdf` — las sucesiones automáticas cumplen la conjetura de Sarnak. arXiv:1602.03042
- `247_MussardoLeClair2021_2021_Randomness_of_M_obius_coefficients_and_Brownian_motion_growth_of_the_Mertens_function_and_the_Riemann_hypothes.pdf` — Mussardo–LeClair, aleatoriedad de μ, movimiento browniano y crecimiento de M(x). arXiv:2101.10336
- `249_Ng2004_2004_Proc_London_Math_Soc.pdf` — Ng, distribución de M(x) bajo RH y otras hipótesis. arXiv:math/0310381
- `253_Nunes2015_2015_Journal_of_Number_Theory.pdf` — libres de cuadrados en progresiones aritméticas. arXiv:1402.0684
- `265_Pintz_2026_Oscillation_Mobius_Function_Zeta_Zeros.pdf` — Pintz, oscilación de M(x) y ceros de ζ. arXiv:2608.24878
- `287_Soundararajan_2009_Partial_Sums_Mobius_Function.pdf` — Soundararajan, sumas parciales de μ: M(x) bajo RH. arXiv:0705.0723
- `292_Tao-Teravainen_2018_Odd_Order_Logarithmically_Averaged_Chowla.pdf` — Tao–Teräväinen, casos de orden impar de Chowla con media logarítmica. arXiv:1710.02112
- `293_Tao-Teravainen_2019_Structure_Logarithmically_Averaged_Correlations.pdf` — Tao–Teräväinen, estructura de las correlaciones logarítmicas; Chowla y Elliott. arXiv:1708.02610
- `294_Tao_2016_Logarithmically_Averaged_Chowla_Elliott_Two_Point.pdf` — Tao, Chowla y Elliott logarítmicos para correlaciones de dos puntos. arXiv:1509.05422
- `296_Tenenbaum_2017_Generalized_Mertens_Sums.pdf` — Tenenbaum, sumas de Mertens generalizadas. arXiv:1910.02781

## 9. Números smooth e intervalos cortos

- `131_Granville_2008_Smooth_Numbers_Survey.pdf` — survey de referencia (MSRI).
- `017_Balog_1987_Integers_Without_Large_Prime_Factors.pdf` — Astérisque 147-148, pp. 27-31.
- `112_Friedlander-Granville_1993_Smoothing_Smooth_Numbers.pdf` — [texto extraído ilegible]
- `081_Croot_2007_Smooth_Numbers_Short_Intervals.pdf` — exponente 3/(14√e)+ε.
- `234_Matomaki_2010_Smooth_Numbers_Short_Intervals.pdf` — exponente 1/(5√e)+ε en [x, x+C√x].
- `235_Matomaki_2016_Smooth_Numbers_Short_Intervals_II.pdf` — intervalo √x(log x)^{7/3+δ}.
- `288_Soundararajan_2010_Smooth_Numbers_Short_Intervals.pdf` — bajo RH, x^ε-smooth en [x, x+C(ε)√x]. arXiv:1009.1591

## 10. Formas modulares, L-funciones y momentos

- `141_Harper_2013_Conditional_Bounds_Zeta_Moments.pdf` — bajo RH, momentos 2k-ésimos ≪ T log^{k²}T. arXiv:1305.4618
- `178_Jutila_1977_Zero_Density_Estimates_L_Functions.pdf` — M. Jutila, *Zero-density estimates for L-functions*, Acta Arithmetica **XXXII** (1977), pp. 55–62; completo, en 5 hojas a doble página. Método de Halász–Montgomery para mejorar Ingham en σ > 3/4; el corolario da N(α,q,χ) con A(α)=2 para α ≥ 21/26 = 0.8076…, 7/9 y 11/14 = 0.7857… según k.
- `269_Radziwill-Soundararajan_2015_Quadratic_Twists_Central_L_Values.pdf` — momentos y distribución de valores centrales. arXiv:1403.7067
- `119_Ghosh-Sarnak_2012_Real_Zeros_Hecke_Cusp_Forms.pdf` — ceros reales de formas cuspidales de Hecke. arXiv:1103.3262
- `216_Lester-Matomaki-Radziwill_2015_Small_Scale_Zeros_Modular_Forms.pdf` — ceros y masa a escala pequeña. arXiv:1501.01292
- `230_Matomaki-Radziwill_2015_Sign_Changes_Hecke_Eigenvalues.pdf` — cambios de signo de λ_f(n). arXiv:1405.7671
- `213_Lau-Liu-Wu_2010_Symmetric_Square_L_Function_Coefficients.pdf` — resultados Ω± para el cuadrado simétrico.
- `204_Kowalski-Robert-Wu_2007_Small_Gaps_And_B_Free_Numbers.pdf` — no existencia de gaps en series de formas modulares.
- `070_Conrad_2005_Partial_Euler_Products_Critical_Line.pdf` — Conrad, productos de Euler parciales en la recta crítica (de Birch–Swinnerton-Dyer a RH). Canad. J. Math. 57 (2005)
- `120_Goldfeld_1982_Produits_Partiels_Euleriens_Courbes_Elliptiques.pdf` — Goldfeld, productos parciales eulerianos de curvas elípticas. C. R. Acad. Sci. Paris 294 (1982)
- `125_Gonek_2012_Finite_Euler_Products_Riemann_Hypothesis.pdf` — Gonek, productos de Euler finitos y RH; modelo ζ_X = P_X + χP_X(1−s). Trans. AMS 364 (2012) 2157–2191, DOI 10.1090/S0002-9947-2011-05546-7
- `283_Sheth_2025_Euler_Products_Centre_Chebyshev_Bias.pdf` — Sheth, productos de Euler en el centro y sesgo de Chebyshev. Math. Proc. Camb. Phil. Soc. 179 (2025), DOI 10.1017/S0305004125000234
- `004_Arguin-Bourgade-Radziwill_2020_Fyodorov_Hiary_Keating_Conjecture_I.pdf` — L.-P. Arguin, P. Bourgade, M. Radziwiłł, *The Fyodorov–Hiary–Keating Conjecture. I*, arXiv:2007.00988v2 (2020), 49 pág. Incondicional: cota superior del máximo de |ζ| en intervalos cortos, medida ≪ y e^{-2y}. Esquema iterativo multiescala con barreras; §7 *Decoupling and second moment* (aproximación de indicadores por polinomios de Dirichlet, comparación con modelo aleatorio), §8 *Decoupling and twisted fourth moment*, Apéndice A sumas sobre primos. Fuente del desacoplo de escalas de primos.
- `005_Arguin-Bourgade-Radziwill_2023_Fyodorov_Hiary_Keating_Conjecture_II.pdf` — mismos autores, *The Fyodorov–Hiary–Keating Conjecture. II*, arXiv:2307.00982v1 (2023), 41 pág. Incondicional: cota inferior; tensión de max log|ζ| − (log log T − ¾ log log log T); §3 *Approximations by Gaussian random walks*; Lema 5: aproximación integral de ζ por producto de Euler finito directamente en la recta crítica.

## 11. Determinantes de Hankel y valores de ζ

- `145_Haynes-Zudilin_2015_Hankel_Determinants_Zeta_Values.pdf` — asintótica de Hankel con ζ(an+b); aplicación diofántica. arXiv:1510.01901
- `238_Monien_2009_Hankel_Determinants_Dirichlet_Series.pdf` — determinantes de Hankel de series de Dirichlet. arXiv:0901.1883
- `100_FazziGuglielmiMarkovsky2021_2021_A_gradient_system_approach_for_Hankel_structured_low_rank_approximation.pdf` — enfoque de sistema gradiente para aproximación de bajo rango con estructura de Hankel. arXiv:2002.06621
- `289_StampachStovicek2020_2020_On_Hankel_matrices_commuting_with_Jacobi_matrices_from_the_Askey_scheme.pdf` — matrices de Hankel que conmutan con matrices de Jacobi del esquema de Askey. arXiv:1911.07059

## 12. Verificación numérica y cálculo

- `266_Platt-Trudgian_2021_RH_True_Up_To_3e12.pdf` — RH verificada rigurosamente (aritmética de intervalos) hasta altura 3·10^12. arXiv:2004.09765
- `285_Sidi_2003_Riemann_And_Generalized_Zeta_Extrapolation.pdf` — extrapolación numérica de ζ (apéndice E).
- (ver también `255_Odlyzko_1987_Distribution_Spacings_Between_Zeros_Zeta.pdf` y `254_Odlyzko-TeRiele_1985_Disproof_Mertens_Conjecture.pdf`)
- `045_Brent2018_2019_On_asymptotic_approximations_to_the_log_Gamma_and_Riemann_Siegel_theta_functions.pdf` — Brent, cotas del error en las aproximaciones asintóticas de log Γ y de la θ de Riemann–Siegel (reloj RvM). arXiv:1609.03682
- `046_Brent_1979_Zeros_Riemann_Zeta_Critical_Strip.pdf` — Brent, ceros de ζ en la banda crítica (verificación, 1979); **sin capa de texto**
- `054_Buthe2014_2015_A_method_for_proving_the_completeness_of_a_list_of_zeros_of_certain_functions.pdf` — Büthe, método para probar la completitud de una lista de ceros (extensión del método de Turing). arXiv:1308.6704
- `078_Corless-Gonnet-Hare-Jeffrey-Knuth_1996_Lambert_W_Function.pdf` — Corless–Gonnet–Hare–Jeffrey–Knuth, la función W de Lambert (inversión del reloj). Adv. Comput. Math. 5 (1996)
- `146_Helfgott-Thompson_2023_Summing_Mobius_Faster_Elementary_Algorithm.pdf` — Helfgott–Thompson, algoritmo elemental más rápido para M(x). arXiv:2101.08773
- `159_Hurst2026_2026_Practical_computations_of_the_Mertens_function_M_10.pdf` — Hurst, cálculo de M(10^24) y M(10^25). arXiv:2607.07566
- `160_Hurst_2018_Computations_Mertens_Function_Improved_Bounds.pdf` — Hurst, cálculos de M(x) y cotas mejoradas de la conjetura de Mertens. arXiv:1610.08551
- `161_Hutchinson_1925_Roots_Riemann_Zeta_Function.pdf` — Hutchinson, raíces de ζ (cálculo de ceros, ley de Gram). Trans. AMS 27 (1925)
- `174_Johansson_2017_Arb_Arbitrary_Precision_Interval_Arithmetic.pdf` — Johansson, Arb: aritmética de intervalos de precisión arbitraria. arXiv:1611.02831
- `175_Johansson_2018_Numerical_Integration_Ball_Arithmetic.pdf` — Johansson, integración numérica en aritmética de bolas. arXiv:1802.07942
- `267_Platt_2017_Isolating_Nontrivial_Zeros_Zeta.pdf` — Platt, aislamiento de ceros no triviales de ζ. Math. Comp., DOI 10.1090/mcom/3198

## 13. Tratados, monografías y panorámicas

- `272_Riemann-Wilkins_1859_Prime_Counting_English_Translation.pdf` — **el texto de Riemann**, en alemán (original de 1859 transcrito por D. R. Wilkins, 10 páginas; no es una traducción al inglés pese al nombre del fichero). La inversión de Möbius para π y la serie Li(x) − ½Li(x^{1/2}) − ⅓Li(x^{1/3}) − ⅕Li(x^{1/5}) + ⅙Li(x^{1/6}) − … están en las págs. 8–9.
- `297_Titchmarsh-HeathBrown_1986_Theory_Riemann_Zeta_Function.pdf` — el tratado estándar. 2ª edición revisada por D. R. Heath-Brown, Clarendon Press. 418 hojas que llegan hasta la página impresa 412; las *Further references* de Heath-Brown terminan en Weil, así que el escaneo está completo.
- `168_Ivic_1985_Riemann_Zeta_Theory_Applications.pdf` — Wiley 1985, edición original. 538 pág. escaneadas; **con capa OCR desde 2026-08-19**, ya es grepeable. Completo (el índice de materias llega hasta las entradas en Z). No incluye erratas: usar `ERRATA_Ivic.md`.
- `170_Ivic_2003_Riemann_Zeta_Dover_Reprint.pdf` — **mismo libro que `168_Ivic_1985_Riemann_Zeta_Theory_Applications.pdf`**. Dover 2003, *unabridged republication* de Wiley 1985: cuerpo y paginación idénticos, no es una edición revisada. Lo único que añade es la lista de erratas en pág. xvii–xix (PDF 15–17), transcrita en `ERRATA_Ivic.md`. Completo; con capa OCR desde 2026-08-19.
- `096_Edwards_1974_Riemanns_Zeta_Function.pdf` — **ESCANEO INCOMPLETO**. Reimpresión Dover 2001 del original de Academic Press 1974. El PDF tiene 135 hojas que cubren las páginas impresas **1–122 de 311** (desfase: hoja PDF ≈ página impresa + 13).
  - **Sí está**: cap. 1 el paper de Riemann (p. 1), cap. 2 fórmula del producto para ξ (39), cap. 3 fórmula principal de Riemann (48), cap. 4 teorema de los números primos (68), cap. 5 De la Vallée Poussin (88), cap. 6 análisis numérico de las raíces por Euler–Maclaurin (96) — hasta ~p. 122.
  - **No está**: cap. 7 fórmula de Riemann–Siegel (136), cap. 8 cálculos a gran escala / Turing / fenómeno de Lehmer (171), cap. 9 crecimiento de zeta y Lindelöf (182), cap. 10 análisis de Fourier (203), cap. 11 ceros en la línea / teorema de Hardy (226), cap. 12 miscelánea (260), apéndice con el paper de Riemann (299), referencias (306) e índice (311).
  - Consecuencia práctica: para Riemann–Siegel, Turing o Hardy **no sirve este fichero**; usar `297_Titchmarsh-HeathBrown_1986_Theory_Riemann_Zeta_Function.pdf` o los Ivić de la biblioteca.
- `259_Patterson_1988_Introduction_Riemann_Zeta_Function.pdf` — S. J. Patterson, *An Introduction to the Theory of the Riemann Zeta-Function*, Cambridge Studies in Advanced Mathematics **14**. 172 hojas, completo (bibliografía p. 153, índice p. 156).
- `260_Patterson_1988_Zeros_Zeta_And_Prime_Number_Theorem.pdf` — cap. 4, ceros y TNP. doi:10.1017/CBO9780511623707.006
- `243_Motohashi_1997_Spectral_Theory_Riemann_Zeta.pdf` — teoría espectral, Cambridge Tracts 127.
- `295_Tenenbaum_2015_Analytic_Probabilistic_Number_Theory.pdf` — GSM 163, 3ª edición.
- `270_Ramachandra_1976_Problems_Analytic_Number_Theory.pdf` — K. Ramachandra, *Some problems of analytic number theory*, Acta Arithmetica **XXXI** (1976), pp. 313–324; completo, en 7 hojas a doble página. Dedicado a la memoria de Turán. Primos en intervalos cortos, resultado de Selberg para N₀(x), método de Heilbronn y aproximación diofántica simultánea.
- `036_Bombieri_2010_Classical_Theory_Zeta_And_L_Functions.pdf` — panorámica histórica. doi:10.1007/s00032-010-0121-8
- `076_Conrey_2003_Riemann_Hypothesis.pdf` — el survey del Notices.
- `074_Conrey_1986_Review_Ivic_Riemann_Zeta_Function.pdf` — reseña de una página (American Scientist).
- `139_Hardy-Littlewood_1917_Riemann_Zeta_And_Distribution_Primes.pdf` — memoria original de Acta Mathematica.
- `064_Christ_2014_Value_Distribution_Zeta_Near_Critical_Line_Thesis.pdf` — tesis doctoral (Würzburg 2013, 191 pág.): distribución de valores de ζ y funciones afines cerca de la recta crítica. arXiv:1405.1553
- `069_Connes2026_2026_Connes2026.pdf` — Connes, *The Riemann Hypothesis: past, present and a letter through time* (panorámica, 2026). arXiv:2602.04022
- `079_Cramer_1919_Nullstellen_Riemannschen_Zetafunktion.pdf` — Cramér, estudios sobre los ceros de ζ. Math. Z. 4 (1919)
- `137_Hadamard_1896_Distribution_Zeros_Zeta_Consequences_Arithmetiques.pdf` — Hadamard, distribución de los ceros de ζ y consecuencias aritméticas. Bull. SMF 24 (1896)
- `211_Landau_1912_Nullstellen_Zetafunktion.pdf` — Landau, sobre los ceros de la función zeta. Math. Ann. 71 (1912)
- `222_Littlewood_1924_Zeros_Riemann_Zeta_Function.pdf` — Littlewood, sobre los ceros de ζ. Proc. Camb. Phil. Soc. (1924), DOI 10.1017/S0305004100014225
- `311_deLaValleePoussin_1896_Recherches_Analytiques_Nombres_Premiers_I.pdf` — de la Vallée Poussin, *Recherches analytiques…* I (1896): teorema de los números primos
- `312_vonMangoldt_1895_Zu_Riemanns_Abhandlung_Anzahl_Primzahlen.pdf` — von Mangoldt, sobre la memoria de Riemann (1895)

## 14. Otras funciones zeta y contextos adyacentes

- `009_Avdonin-Ivanov_2001_Exponential_Riesz_Bases_Subspaces_Divided_Differences.pdf` — bases de Riesz de exponenciales y de diferencias divididas; criterio de Pavlov vía Helson–Szegő/A₂. arXiv:math/0103160
- `224_Lyubarskii-Seip_1997_Complete_Interpolating_Sequences_Paley_Wiener_Muckenhoupt_Ap.pdf` — sucesiones de interpolación completa en Paley–Wiener y condición A_p; Kadec 1/4 como corolario. Rev. Mat. Iberoam. 13 (1997), DOI 10.4171/RMI/224
- `163_Igusa_2000_Introduction_Local_Zeta_Functions.pdf` — zetas locales.
- `194_Komori-Matsumoto-Tsumura_2023_Zeta_Functions_Root_Systems.pdf` — zetas de sistemas de raíces.
- `220_Li_2019_Zeta_L_Functions_Number_Theory_Combinatorics.pdf` — CBMS 129. doi:10.1090/cbms/129
- `308_Zhao_2016_Multiple_Zeta_Polylogarithms_Special_Values.pdf` — zetas múltiples y polilogaritmos.
- `212_Lapidus-VanFrankenhuysen_2000_Fractal_Geometry_Number_Theory.pdf` — dimensiones complejas de cuerdas fractales.
- `184_Kanemitsu-Tsukada_2015_Hecke_Type_Zeta_Functions.pdf` — cap. 8 de *Contributions to the Theory of Zeta-Functions*.
- `185_Kanemitsu-Tsukada_2015_Modular_Relation_Supremacy.pdf` — *Contributions to the Theory of Zeta-Functions: The Modular Relation Supremacy*, World Scientific, Series on Number Theory and Its Applications vol. 9. 316 hojas, completo (índice hasta p. 303). Fórmulas de Voronoĭ, funciones de Bessel generalizadas de Wilton, transformación theta.
- `030_Bloch_2000_Higher_Regulators_K_Theory_Zeta_Elliptic_Curves.pdf` — S. Bloch, monografía AMS (vol. 11 de la serie), 110 pág., completo. Reguladores superiores, K-teoría algebraica y funciones zeta de curvas elípticas.
- `268_Popov_1985_Transfer_Functions_Riemann_Zeta.pdf` — sistemas con funciones de transferencia ligadas a ζ.
- `176_Jones-Sato-Wada-Wiens_1976_Diophantine_Representation_Primes.pdf` — el polinomio de 26 variables (Monthly).
- `195_Korolev-Laurincikas_2023_Approximation_Mellin_Transform_Zeta_Axioms.pdf` — aproximación de ζ por transformadas de Mellin. Axioms 12 (2023), 520.
- `015_Balanzario-SanchezOrtiz_2007_Zeros_Davenport_Heilbronn_Counterexample.pdf` — ceros fuera de la recta del contraejemplo de Davenport–Heilbronn. Math. Comp. 76 (2007)
- `035_Bohr_1926_Fastperiodische_Funktionen_III_Dirichletentwicklung.pdf` — Bohr, funciones casi periódicas III: desarrollos de Dirichlet. Acta Math. (1926)
- `062_Chandrasekharan-Mandelbrojt_1959_Solutions_Riemann_Functional_Equation.pdf` — Chandrasekharan–Mandelbrojt, soluciones de la ecuación funcional de Riemann (1959)
- `085_Davenport-Heilbronn_1936_Zeros_Certain_Dirichlet_Series_I.pdf` — Davenport–Heilbronn, ceros de ciertas series de Dirichlet I (1936)
- `133_Grosswald-Schnitzer_1978_Class_Modified_Zeta_L_Functions.pdf` — Grosswald–Schnitzer, una clase de funciones ζ y L modificadas. Pacific J. Math. 74 (1978)
- `138_Hamburger_1921_Riemannsche_Funktionalgleichung_Zeta_Funktion_I.pdf` — Hamburger, ecuación funcional de Riemann I. Math. Z. 10 (1921)
- `148_HerichiLapidus2014_2014_Truncated_infinitesimal_shifts_spectral_operators_and_quantized_universality_of_the_Riemann_zeta_function.pdf` — Herichi–Lapidus, desplazamientos infinitesimales truncados y universalidad cuantizada de ζ. Ann. Fac. Sci. Toulouse 23 (2014)
- `149_HerreraMoree2018_2018_Coefficients_and_higher_order_derivatives_of_cyclotomic_polynomials_old_and_new.pdf` — coeficientes y derivadas de polinomios ciclotómicos. arXiv:1805.05207
- `156_Hoffman1992_1992_Multiple_harmonic_series.pdf` — Hoffman, series armónicas múltiples. Pacific J. Math. 152 (1992)
- `179_Kaczorowski-Perelli_1999_Structure_Selberg_Class_I.pdf` — Kaczorowski–Perelli, estructura de la clase de Selberg I. Acta Math. 182 (1999)
- `192_Knopp_1994_Dirichlet_Series_Riemann_Functional_Equation.pdf` — Knopp, series de Dirichlet con la ecuación funcional de Riemann (Hamburger). Invent. Math. 117 (1994)
- `248_Nakamura_2020_Dirichlet_Series_Periodic_Coefficients_Functional_Equation.pdf` — series de Dirichlet de coeficientes periódicos con la ecuación funcional de Riemann; ceros reales de L(s,χ). arXiv:2008.02570
- `262_Perelli_2016_Converse_Theorems_Zeta_Selberg_Class.pdf` — Perelli, teoremas recíprocos: de ζ a la clase de Selberg. arXiv:1605.02354
- `286_Siegel_1922_Satz_Hamburger_Funktionalgleichung_Zetafunktion.pdf` — Siegel, sobre el teorema de Hamburger. Math. Ann. 86 (1922)

## 15. Material no arbitrado — contrastar antes de usar

- `082_Dannon_2008_Riemann_Zeta_Function.pdf` — Gauge Institute Journal.
- `301_Vega_2023_Simple_Proof_Riemann_Hypothesis.pdf` — vía función Ψ de Dedekind. doi:10.33774/coe-2023-5flmk
- `003_Anonymous_2026_Unexpected_Phase_Summation_Patterns_Riemann_Zeros.pdf` — preprint anónimo de 2026 sobre S(N)=Σ e^{iγ_n}, citas rotas.
- `306_Youvan_2024_Phase_Winding_Riemann_Zeta.pdf` — ver §1.

## 16. Primos generalizados de Beurling

- `028_Beurling_1937_Distribution_Nombres_Premiers_Generalises_I.pdf` — Beurling, primos generalizados I (1937)
- `049_Broucke-Debruyne-Revesz_2025_Well_Behaved_Beurling_Number_Systems.pdf` — sistemas de Beurling bien comportados (ahorro de potencia en primos y enteros). arXiv:2309.01567
- `050_Broucke-Debruyne-Vindas_2020_Beurling_Integers_RH_Large_Oscillation.pdf` — enteros de Beurling con RH y oscilación grande. arXiv:2004.11501
- `051_Broucke-Vindas_2024_Generalized_Prime_Random_Approximation.pdf` — aproximación aleatoria de primos generalizados. arXiv:2102.08478
- `086_Debruyne-Vindas_2019_Complex_Tauberian_Theorems_Laplace_Transforms.pdf` — teoremas tauberianos complejos para transformadas de Laplace. arXiv:1604.05069
- `090_Diamond-Montgomery-Vorhauer_2006_Beurling_Primes_Large_Oscillation.pdf` — Diamond–Montgomery–Vorhauer, primos de Beurling con oscilación grande. Math. Ann. 334 (2006), DOI 10.1007/s00208-005-0638-2
- `091_Diamond_1970_Asymptotic_Distribution_Beurling_Generalized_Integers.pdf` — Diamond, distribución asintótica de los enteros generalizados de Beurling (1970)
- `151_Hilberdink-Lapidus_2006_Beurling_Zeta_Generalised_Primes_Fractal_Membranes.pdf` — Hilberdink–Lapidus, zetas de Beurling, primos generalizados y membranas fractales. arXiv:math/0410270
- `307_Zhang_2013_Normalization_Beurling_Generalized_Primes_RH.pdf` — Zhang, normalización de primos generalizados de Beurling con RH. Ann. Univ. Sci. Budapest. Sect. Comp. 39 (2013)

## 17. Paseos aleatorios, excursiones y caminos de Dyck

- `055_Carmona-Petrelis_2017_Limit_Theorems_Random_Walk_Excursion.pdf` — excursión de paseo aleatorio condicionada a encerrar un área: teoremas límite. arXiv:1709.06448
- `063_Chatterjee2007_2007_Stein_s_method_for_concentration_inequalities.pdf` — Chatterjee, método de Stein para desigualdades de concentración. PTRF 138 (2007), DOI 10.1007/s00440-006-0029-y
- `088_Denisov-Kolb-Wachtel_2015_Local_Asymptotics_Random_Walk_Excursions.pdf` — asintótica local del área de las excursiones de paseos aleatorios (Oberwolfach Preprint 2013-19)
- `089_DerridaEnaudLebowitz2004_2004_The_asymmetric_exclusion_process_and_Brownian_excursions.pdf` — proceso de exclusión asimétrico y excursiones brownianas. arXiv:cond-mat/0306078
- `094_DurrettIglehartMiller1977_1977_Weak_convergence_to_Brownian_meander_and_Brownian_excursion.pdf` — convergencia débil al meandro y a la excursión brownianos. Ann. Probab. (1977)
- `126_GordinPeligrad2011_2011_On_the_functional_central_limit_theorem_via_martingale_approximation.pdf` — teorema central del límite funcional vía aproximación por martingalas. Bernoulli 17 (2011). arXiv:0910.3448
- `127_Gouezel2010_2010_Almost_sure_invariance_principle_for_dynamical_systems_by_spectral_methods.pdf` — principio de invariancia casi segura por métodos espectrales. Ann. Probab. 38 (2010), DOI 10.1214/10-AOP525
- `144_HaugPrellberg2015_2015_Uniform_asymptotics_of_area_weighted_Dyck_paths.pdf` — asintótica uniforme de caminos de Dyck ponderados por área. arXiv:1412.5108
- `171_Janson_2007_Brownian_Excursion_Area_Wright_Constants.pdf` — Janson, área de la excursión browniana y constantes de Wright. Probab. Surveys 4 (2007), DOI 10.1214/07-PS104
- `183_Kaigh1976_1976_An_invariance_principle_for_random_walk_conditioned_by_a_late_return_to_zero.pdf` — principio de invariancia para paseos condicionados a un retorno tardío a cero. Ann. Probab. (1976)
- `190_KhorunzhiyMarckert2009_2009_Uniform_bounds_for_exponential_moment_of_maximum_of_a_Dyck_path.pdf` — cotas uniformes del momento exponencial del máximo de un camino de Dyck. arXiv:0902.1229
- `203_Kousha2012_2012_Asymptotic_behavior_and_the_moderate_deviation_principle_for_the_maximum_of_a_Dyck_path.pdf` — comportamiento asintótico y desviaciones moderadas del máximo de un camino de Dyck. arXiv:1008.0606
- `258_OwczarekPrellberg2014_2014_Pressure_exerted_by_a_vesicle_on_a_surface.pdf` — presión de una vesícula sobre una superficie (caminos de Dyck). arXiv:1311.2174
- `261_PeligradUtev2005_2005_A_new_maximal_inequality_and_invariance_principle_for_stationary_sequences.pdf` — desigualdad maximal y principio de invariancia para sucesiones estacionarias. Ann. Probab. 33 (2005). arXiv:math/0406606
- `271_Richard_2005_Q_Functional_Equations_Excursion_Moments.pdf` — ecuaciones q-funcionales y momentos de excursiones. arXiv:math/0503198

## 18. Cuasicristales, bases de Riesz e interpolación de Fourier

- `010_Avdonin_1977_Riesz_Bases_Exponential_Functions_L2_Brief.pdf` — Avdonin, bases de Riesz de exponenciales en L² (nota breve, 1977)
- `038_Bondarenko-Radchenko-Seip_2023_Fourier_Interpolation_Zeros_Zeta_L_Functions.pdf` — Bondarenko–Radchenko–Seip, interpolación de Fourier con ceros de ζ y L-funciones. arXiv:2005.02996
- `067_Cohn-Elkies_2003_New_Upper_Bounds_Sphere_Packings_I.pdf` — Cohn–Elkies, cotas de programación lineal para empaquetamiento de esferas. Ann. of Math. 157 (2003). arXiv:math/0110009
- `097_Engert1970_1970_Finite_dimensional_translation_invariant_subspaces.pdf` — subespacios invariantes por traslación de dimensión finita. Pacific J. Math. 32 (1970)
- `157_Hruscev-Nikolskii-Pavlov_1981_Unconditional_Bases_Exponentials_Reproducing_Kernels.pdf` — Hruščev–Nikolskii–Pavlov, bases incondicionales de exponenciales y núcleos reproductores (1981)
- `164_Ingham_1936_Trigonometrical_Inequalities_Theory_Series.pdf` — Ingham, desigualdades trigonométricas en la teoría de series (1936)
- `207_Kozma-Lev_2011_Exponential_Riesz_Bases_Discrepancy_BMO.pdf` — Kozma–Lev, bases de Riesz de exponenciales, discrepancia de rotaciones irracionales y BMO. arXiv:1009.2188
- `208_Kurasov-Sarnak_2020_Stable_Polynomials_Crystalline_Measures.pdf` — Kurasov–Sarnak, polinomios estables y medidas cristalinas. arXiv:2004.05678
- `217_Lev-Olevskii_2015_Quasicrystals_Poisson_Summation_Formula.pdf` — Lev–Olevskii, cuasicristales y fórmula de sumación de Poisson. arXiv:1312.6884
- `218_Lev_2012_Riesz_Bases_Exponentials_Multiband_Spectra_Preprint.pdf` — Lev, bases de Riesz de exponenciales sobre espectros multibanda. arXiv:1101.3894
- `257_Olevskii-Ulanovskii_2020_Fourier_Quasicrystals_Unit_Masses.pdf` — Olevskii–Ulanovskii, cuasicristales de Fourier con masas unidad. C. R. Math. 358 (2020), DOI 10.5802/crmath.142
- `291_Szekelyhidi1982_1982_Note_on_exponential_polynomials.pdf` — Székelyhidi, nota sobre polinomios exponenciales. Pacific J. Math. 103 (1982)
- `305_Young_1974_Inequalities_Perturbation_Theorem_Paley_Wiener.pdf` — Young, desigualdades para el teorema de perturbación de Paley–Wiener. Proc. AMS 43 (1974)

## 19. Positividad total y funciones absolutamente monótonas

- `022_Belton2022_2022_Mathematics_Research_Reports.pdf` — preservadores de núcleos totalmente positivos y funciones de frecuencia de Pólya. Math. Res. Rep. 3 (2022), DOI 10.5802/mrr.12
- `026_Bernstein_1929_Fonctions_Absolument_Monotones.pdf` — Bernstein, funciones absolutamente monótonas. Acta Math. (1929)
- `039_BorceaBranden2009_2009_Annals_of_Mathematics.pdf` — Borcea–Brändén, teoremas maestros de Pólya–Schur. Ann. of Math. 170 (2009)
- `052_Burbea1974_1974_Pacific_Journal_of_Mathematics.pdf` — Burbea, positividad total y núcleos reproductores. Pacific J. Math. 55 (1974)
- `053_Burbea1976_1976_Pacific_Journal_of_Mathematics.pdf` — Burbea, positividad total de ciertos núcleos reproductores. Pacific J. Math. 67 (1976)

## 20. Otros temas (fuera del núcleo aritmético)

- `002_AkianGaubertNiv2018_2018_Tropical_compound_matrix_identities.pdf` — identidades de matrices compuestas tropicales. arXiv:1702.00980
- `023_Benedetto-Powell-Yilmaz_2006_Sigma_Delta_Quantization_Finite_Frames.pdf` — cuantización Sigma-Delta y marcos finitos
- `024_Benvenuti2019_2019_The_inverse_eigenvalue_problem_for_Leslie_matrices.pdf` — problema inverso de autovalores para matrices de Leslie. Electron. J. Linear Algebra 35 (2019)
- `037_Bonami1970_1970_Etude_des_coefficients_de_Fourier_des_fonctions_de_L_p_G.pdf` — Bonami, coeficientes de Fourier de funciones de L^p(G). Ann. Inst. Fourier 20 (1970)
- `058_CarrascoFlorens2000_2000_Econometric_Theory.pdf` — Carrasco–Florens, GMM con un continuo de condiciones de momentos (econometría)
- `084_Daubechies-DeVore_2003_Bandlimited_Function_Stable_Sigma_Delta_Modulators.pdf` — Daubechies–DeVore, moduladores Sigma-Delta estables de orden arbitrario. Ann. of Math. 158 (2003)
- `087_DellAnnaEtAl2016_2016_Violation_of_cluster_decomposition_and_absence_of_light_cones_in_local_integer_and_half_integer_spin_chains.pdf` — violación de la descomposición en clústeres en cadenas de espines. arXiv:1604.08281
- `095_DuttEtAl2019_2019_Nature_Communications.pdf` — espectroscopía de bandas en una dimensión sintética (fotónica). Nat. Commun. (2019), DOI 10.1038/s41467-019-11117-9
- `118_Gallier2016_2016_Spectral_theory_of_unsigned_and_signed_graphs_applications_to_graph_clustering_a_survey.pdf` — Gallier, teoría espectral de grafos con y sin signo; clustering. arXiv:1601.04692
- `135_Gunturk-Thao_2003_Ergodic_Dynamics_Sigma_Delta_Quantization.pdf` — dinámica ergódica en la cuantización Sigma-Delta. arXiv:math/0308223
- `225_LyubarskiiVershynin2010_2010_Uncertainty_principles_and_vector_quantization.pdf` — Lyubarskii–Vershynin, principios de incertidumbre y cuantización vectorial. arXiv:math/0611343
- `256_OganesyanHuse2007_2007_Localization_of_interacting_fermions_at_high_temperature.pdf` — Oganesyan–Huse, localización de fermiones interactuantes a alta temperatura. arXiv:cond-mat/0610854
- `273_RigalZadunaisky2015_2015_Twisted_semigroup_algebras.pdf` — álgebras de semigrupo torcidas. arXiv:1406.2985

## Catálogo completo actual — 2026-10-23 (312 PDF)

- `001_AbercrombieBanksShparlinski2009_2009_Arithmetic_functions_on_Beatty_sequences.pdf`
- `002_AkianGaubertNiv2018_2018_Tropical_compound_matrix_identities.pdf`
- `003_Anonymous_2026_Unexpected_Phase_Summation_Patterns_Riemann_Zeros.pdf`
- `004_Arguin-Bourgade-Radziwill_2020_Fyodorov_Hiary_Keating_Conjecture_I.pdf`
- `005_Arguin-Bourgade-Radziwill_2023_Fyodorov_Hiary_Keating_Conjecture_II.pdf`
- `006_AriasdeReyna_2024_Explicit_Formula_Quasicrystal_Definition.pdf`
- `007_Aryan_2019_Extension_Landau_Gonek_Formula.pdf`
- `008_Aryan_2022_Extension_Landau_Gonek_Formula_Published.pdf`
- `009_Avdonin-Ivanov_2001_Exponential_Riesz_Bases_Subspaces_Divided_Differences.pdf`
- `010_Avdonin_1977_Riesz_Bases_Exponential_Functions_L2_Brief.pdf`
- `011_Aymone-Sidoravicius_2017_Partial_Sums_Biased_Random_Multiplicative_Functions.pdf`
- `012_Aymone2020_2020_A_note_on_multiplicative_functions_resembling_the_M_bius_function.pdf`
- `013_BaezDuarte-Balazard-Landreau-Saias_2000_Notes_sur_la_fonction_zeta_de_Riemann_3.pdf`
- `014_BaezDuarte2002_2002_BaezDuarte2002.pdf`
- `015_Balanzario-SanchezOrtiz_2007_Zeros_Davenport_Heilbronn_Counterexample.pdf`
- `016_Balazard-Saias-Yor_1999_Notes_Fonction_Zeta_Riemann_2_Transcription_VellaChemla.pdf`
- `017_Balog_1987_Integers_Without_Large_Prime_Factors.pdf`
- `018_Baluyot-Goldston-etal_2025_Pair_Correlation_Zeros_I_Proportions_Simple_Critical.pdf`
- `019_Baricz-Laforgia-Pogany_2015_Van_Der_Corput_Inequalities_Bessel.pdf`
- `020_Barrett-Jarvis_1992_Spectral_Properties_Redheffer_Matrix.pdf`
- `021_Bellotti-Wong_2025_Improved_Argument_Zero_Counting_Zeta.pdf`
- `022_Belton2022_2022_Mathematics_Research_Reports.pdf`
- `023_Benedetto-Powell-Yilmaz_2006_Sigma_Delta_Quantization_Finite_Frames.pdf`
- `024_Benvenuti2019_2019_The_inverse_eigenvalue_problem_for_Leslie_matrices.pdf`
- `025_BergelsonKulagaPrzymusLemanczykRichter2019_2019_Discrete_Contin_Dyn_Syst.pdf`
- `026_Bernstein_1929_Fonctions_Absolument_Monotones.pdf`
- `027_Berry_1988_Semiclassical_Formula_Number_Variance_Riemann_Zeros.pdf`
- `028_Beurling_1937_Distribution_Nombres_Premiers_Generalises_I.pdf`
- `029_Bjorner_2011_Cell_Complex_Number_Theory.pdf`
- `030_Bloch_2000_Higher_Regulators_K_Theory_Zeta_Elliptic_Curves.pdf`
- `031_Bogomolny-Keating_1995_Random_Matrix_Theory_Riemann_Zeros_I_Three_Four_Point_Correlations.pdf`
- `032_Bogomolny-Keating_1996_Gutzwiller_Trace_Formula_Spectral_Statistics_Beyond_Diagonal.pdf`
- `033_Bogomolny-Keating_1996_Random_Matrix_Theory_Riemann_Zeros_II_n_Point_Correlations.pdf`
- `034_Bohigas-Leboeuf-Sanchez_2001_Spectral_Spacing_Correlations.pdf`
- `035_Bohr_1926_Fastperiodische_Funktionen_III_Dirichletentwicklung.pdf`
- `036_Bombieri_2010_Classical_Theory_Zeta_And_L_Functions.pdf`
- `037_Bonami1970_1970_Etude_des_coefficients_de_Fourier_des_fonctions_de_L_p_G.pdf`
- `038_Bondarenko-Radchenko-Seip_2023_Fourier_Interpolation_Zeros_Zeta_L_Functions.pdf`
- `039_BorceaBranden2009_2009_Annals_of_Mathematics.pdf`
- `040_Bornemann-Forrester-Mays_2017_Finite_Size_Effects_Spacing_Distributions.pdf`
- `041_Borwein-Straub-Wan-Zudilin_2012_Densities_Short_Uniform_Random_Walks.pdf`
- `042_Bourgain_2017_Decoupling_Exponential_Sums_Riemann_Zeta.pdf`
- `043_Bourgain_undated_On_the_Fourier_Walsh_spectrum_of_the_M_obius_function.pdf`
- `044_Brent-Platt-Trudgian_2020_Sums_Over_Zeros_Riemann_Zeta.pdf`
- `045_Brent2018_2019_On_asymptotic_approximations_to_the_log_Gamma_and_Riemann_Siegel_theta_functions.pdf`
- `046_Brent_1979_Zeros_Riemann_Zeta_Critical_Strip.pdf`
- `047_BretcheDressTenenbaum2020_2020_Mathematika.pdf`
- `048_Brevig-Perfekt-Seip-Siskakis-Vukotic_2016_Multiplicative_Hilbert_Matrix.pdf`
- `049_Broucke-Debruyne-Revesz_2025_Well_Behaved_Beurling_Number_Systems.pdf`
- `050_Broucke-Debruyne-Vindas_2020_Beurling_Integers_RH_Large_Oscillation.pdf`
- `051_Broucke-Vindas_2024_Generalized_Prime_Random_Approximation.pdf`
- `052_Burbea1974_1974_Pacific_Journal_of_Mathematics.pdf`
- `053_Burbea1976_1976_Pacific_Journal_of_Mathematics.pdf`
- `054_Buthe2014_2015_A_method_for_proving_the_completeness_of_a_list_of_zeros_of_certain_functions.pdf`
- `055_Carmona-Petrelis_2017_Limit_Theorems_Random_Walk_Excursion.pdf`
- `056_Carneiro-Chandee-Littmann-Milinovich_2014_Hilbert_Spaces_Pair_Correlation.pdf`
- `057_Carneiro-Milinovich-Ramos_2023_Fourier_Optimization_Montgomery_Pair_Correlation.pdf`
- `058_CarrascoFlorens2000_2000_Econometric_Theory.pdf`
- `059_Cartier-Julia-Moussa-Vanhove_2006_Random_Matrices_Zeta_Dynamical_Systems.pdf`
- `060_Cassaigne-Ferenczi-Mauduit-Rivat-Sarkozy_1999_Liouville_Pseudorandom_Sequences.pdf`
- `061_Chan_2002_More_Precise_Pair_Correlation_Zeros_Primes_Short_Intervals.pdf`
- `062_Chandrasekharan-Mandelbrojt_1959_Solutions_Riemann_Functional_Equation.pdf`
- `063_Chatterjee2007_2007_Stein_s_method_for_concentration_inequalities.pdf`
- `064_Christ_2014_Value_Distribution_Zeta_Near_Critical_Line_Thesis.pdf`
- `065_Coffey_2005_Polygamma_Theory_Li_Keiper_Constants_Riemann_Hypothesis.pdf`
- `066_Coffey_2009_Certain_Sums_Over_Nontrivial_Zeta_Zeros.pdf`
- `067_Cohn-Elkies_2003_New_Upper_Bounds_Sphere_Packings_I.pdf`
- `068_Connes1998_1998_Connes1998.pdf`
- `069_Connes2026_2026_Connes2026.pdf`
- `070_Conrad_2005_Partial_Euler_Products_Critical_Line.pdf`
- `071_Conrey-Keating_2016_Pair_Correlation_Twin_Primes_Revisited.pdf`
- `072_Conrey-TurnageButterbaugh_2018_r_Gaps_Between_Zeros_Zeta.pdf`
- `073_ConreySnaith2008_2008_Communications_in_Number_Theory_and_Physics.pdf`
- `074_Conrey_1986_Review_Ivic_Riemann_Zeta_Function.pdf`
- `075_Conrey_1989_More_Than_Two_Fifths_Zeros_Critical_Line.pdf`
- `076_Conrey_2003_Riemann_Hypothesis.pdf`
- `077_Coons2010_2010_On_the_multiplicative_Erd_s_discrepancy_problem.pdf`
- `078_Corless-Gonnet-Hare-Jeffrey-Knuth_1996_Lambert_W_Function.pdf`
- `079_Cramer_1919_Nullstellen_Riemannschen_Zetafunktion.pdf`
- `080_Croot_2003_Oscillations_Multiplicative_PlusMinusOne.pdf`
- `081_Croot_2007_Smooth_Numbers_Short_Intervals.pdf`
- `082_Dannon_2008_Riemann_Zeta_Function.pdf`
- `083_Das-Ismoilov-Ramos_2025_Fourier_Optimization_Pair_Correlation_Problems.pdf`
- `084_Daubechies-DeVore_2003_Bandlimited_Function_Stable_Sigma_Delta_Modulators.pdf`
- `085_Davenport-Heilbronn_1936_Zeros_Certain_Dirichlet_Series_I.pdf`
- `086_Debruyne-Vindas_2019_Complex_Tauberian_Theorems_Laplace_Transforms.pdf`
- `087_DellAnnaEtAl2016_2016_Violation_of_cluster_decomposition_and_absence_of_light_cones_in_local_integer_and_half_integer_spin_chains.pdf`
- `088_Denisov-Kolb-Wachtel_2015_Local_Asymptotics_Random_Walk_Excursions.pdf`
- `089_DerridaEnaudLebowitz2004_2004_The_asymmetric_exclusion_process_and_Brownian_excursions.pdf`
- `090_Diamond-Montgomery-Vorhauer_2006_Beurling_Primes_Large_Oscillation.pdf`
- `091_Diamond_1970_Asymptotic_Distribution_Beurling_Generalized_Integers.pdf`
- `092_Drmota_2009_Sum_Of_Digits_Of_Primes.pdf`
- `093_Durkan-Hughes-PearceCrump_2026_Generalisations_Landau_Gonek_Theorem.pdf`
- `094_DurrettIglehartMiller1977_1977_Weak_convergence_to_Brownian_meander_and_Brownian_excursion.pdf`
- `095_DuttEtAl2019_2019_Nature_Communications.pdf`
- `096_Edwards_1974_Riemanns_Zeta_Function.pdf`
- `097_Engert1970_1970_Finite_dimensional_translation_invariant_subspaces.pdf`
- `098_ErdosEtAl2012_2012_Spectral_statistics_of_Erd.pdf`
- `099_Fazzari-Gerspach-Minelli_2025_Selberg_CLT_Weighted_Linear_Statistics_Zeta_Zeros.pdf`
- `100_FazziGuglielmiMarkovsky2021_2021_A_gradient_system_approach_for_Hankel_structured_low_rank_approximation.pdf`
- `101_Ford-Meng-Zaharescu_2017_Simultaneous_Fractional_Parts.pdf`
- `102_Ford-Soundararajan-Zaharescu_2009_Imaginary_Parts_II.pdf`
- `103_Ford-Zaharescu_2005_Imaginary_Parts_Zeta_Zeros.pdf`
- `104_Ford_2002_Vinogradov_Integral_Bounds_Riemann_Zeta.pdf`
- `105_Forrester-Lebowitz_2013_Local_CLT_Determinantal_Point_Processes.pdf`
- `106_Forrester-Mays_2015_Finite_Size_Corrections_RMT_Odlyzko_Data.pdf`
- `107_Franca-LeClair_2014_Statistical_Properties_Riemann_Zeros_Explicit_Equation_nth_Zero.pdf`
- `108_Franca-LeClair_2014_Theory_Zeros_Riemann_Zeta_And_Other_L_Functions.pdf`
- `109_Franca-LeClair_2015_Transcendental_Equations_Individual_Zeros_L_Functions.pdf`
- `110_Franca-LeClair_2015_Transcendental_Equations_Individual_Zeros_L_Functions_CNTP_Published.pdf`
- `111_Frantzikinakis2020_1908_Correlations_of_multiplicative_functions_along_deterministic_and_independent_sequences.pdf`
- `112_Friedlander-Granville_1993_Smoothing_Smooth_Numbers.pdf`
- `113_Fujii_1974_Zeros_Dirichlet_L_Functions_I.pdf`
- `114_Fujii_1975_Difference_r_Consecutive_Ordinates_Zeros_Zeta.pdf`
- `115_Fujii_1975_Distribution_Zeros_Zeta_Short_Intervals.pdf`
- `116_Fujii_1981_Zeros_Dirichlet_L_Functions_II_Corrections.pdf`
- `117_GPY2009_2009_Annals_of_Mathematics.pdf`
- `118_Gallier2016_2016_Spectral_theory_of_unsigned_and_signed_graphs_applications_to_graph_clustering_a_survey.pdf`
- `119_Ghosh-Sarnak_2012_Real_Zeros_Hecke_Cusp_Forms.pdf`
- `120_Goldfeld_1982_Produits_Partiels_Euleriens_Courbes_Elliptiques.pdf`
- `121_Goldston-Lee-Schettler-Suriajaya_2025_Pair_Correlation_Conjecture_II_Alternative_Hypothesis.pdf`
- `122_Goldston-Lee-Schettler-Suriajaya_2025_Pair_Correlation_Conjecture_I_Simple_Critical.pdf`
- `123_Gonek-Sahay_2024_Consecutive_Moderate_Gaps_Between_Zeros_Zeta.pdf`
- `124_Gonek_1985_Formula_Landau_Mean_Values_Zeta_INCOMPLETE_pp92-96.pdf`
- `125_Gonek_2012_Finite_Euler_Products_Riemann_Hypothesis.pdf`
- `126_GordinPeligrad2011_2011_On_the_functional_central_limit_theorem_via_martingale_approximation.pdf`
- `127_Gouezel2010_2010_Almost_sure_invariance_principle_for_dynamical_systems_by_spectral_methods.pdf`
- `128_Graham-Kolesnik_1991_Computing_Optimal_Exponent_Pairs.pdf`
- `129_Graham-Kolesnik_1991_Simplest_Van_Der_Corput_Estimates.pdf`
- `130_Granville-Soundararajan_2003_Decay_Of_Mean_Values.pdf`
- `131_Granville_2008_Smooth_Numbers_Survey.pdf`
- `132_GrepstadEtAl2019_1909_On_the_asymptotic_behaviour_of_the_sine_product.pdf`
- `133_Grosswald-Schnitzer_1978_Class_Modified_Zeta_L_Functions.pdf`
- `134_Guillera_2013_Sums_Nontrivial_Zeros_Riemann_Zeta.pdf`
- `135_Gunturk-Thao_2003_Ergodic_Dynamics_Sigma_Delta_Quantization.pdf`
- `136_Guth-Maynard_2026_New_Large_Value_Estimates_Dirichlet_Polynomials.pdf`
- `137_Hadamard_1896_Distribution_Zeros_Zeta_Consequences_Arithmetiques.pdf`
- `138_Hamburger_1921_Riemannsche_Funktionalgleichung_Zeta_Funktion_I.pdf`
- `139_Hardy-Littlewood_1917_Riemann_Zeta_And_Distribution_Primes.pdf`
- `140_Harman-Pintz-Wolke_1985_Mobius_And_Liouville_Functions.pdf`
- `141_Harper_2013_Conditional_Bounds_Zeta_Moments.pdf`
- `142_Harper_2020_Moments_Random_Multiplicative_Functions_I.pdf`
- `143_Hasanalizade-Shen-Wong_2022_Counting_Zeros_Riemann_Zeta.pdf`
- `144_HaugPrellberg2015_2015_Uniform_asymptotics_of_area_weighted_Dyck_paths.pdf`
- `145_Haynes-Zudilin_2015_Hankel_Determinants_Zeta_Values.pdf`
- `146_Helfgott-Thompson_2023_Summing_Mobius_Faster_Elementary_Algorithm.pdf`
- `147_HelfgottRadziwill2021_undated_HelfgottRadziwill2021.pdf`
- `148_HerichiLapidus2014_2014_Truncated_infinitesimal_shifts_spectral_operators_and_quantized_universality_of_the_Riemann_zeta_function.pdf`
- `149_HerreraMoree2018_2018_Coefficients_and_higher_order_derivatives_of_cyclotomic_polynomials_old_and_new.pdf`
- `150_HeuslerEtAl2007_2007_Periodic_orbit_theory_of_level_correlations.pdf`
- `151_Hilberdink-Lapidus_2006_Beurling_Zeta_Generalised_Primes_Fractal_Membranes.pdf`
- `152_Hilberdink-Pushnitski_2023_Spectral_Asymptotics_LCM_Matrices.pdf`
- `153_Hilberdink_2006_Determinants_Multiplicative_Toeplitz_Matrices.pdf`
- `154_Hilberdink_2015_Multiplicative_Toeplitz_Matrices_Riemann_Zeta.pdf`
- `155_Hilberdink_2017_Singular_Values_Multiplicative_Toeplitz_Matrices.pdf`
- `156_Hoffman1992_1992_Multiple_harmonic_series.pdf`
- `157_Hruscev-Nikolskii-Pavlov_1981_Unconditional_Bases_Exponentials_Reproducing_Kernels.pdf`
- `158_Hughes-Rudnick_2002_Linear_Statistics_Zeros_Zeta.pdf`
- `159_Hurst2026_2026_Practical_computations_of_the_Mertens_function_M_10.pdf`
- `160_Hurst_2018_Computations_Mertens_Function_Improved_Bounds.pdf`
- `161_Hutchinson_1925_Roots_Riemann_Zeta_Function.pdf`
- `162_Huxley_1989_Exponential_Sums_Riemann_Zeta.pdf`
- `163_Igusa_2000_Introduction_Local_Zeta_Functions.pdf`
- `164_Ingham_1936_Trigonometrical_Inequalities_Theory_Series.pdf`
- `165_Inoue-Kobayashi-Toma_2026_Explicit_Extreme_Values_Argument_Zeta.pdf`
- `166_Inoue_2024_Note_On_r_Gaps_Between_Zeros_Zeta.pdf`
- `167_Ivic-Korolev_2018_Distribution_Values_Argument_Zeta.pdf`
- `168_Ivic_1985_Riemann_Zeta_Theory_Applications.pdf`
- `169_Ivic_2001_Sums_Over_Ordinates_Zeta_Zeros.pdf`
- `170_Ivic_2003_Riemann_Zeta_Dover_Reprint.pdf`
- `171_Janson_2007_Brownian_Excursion_Area_Wright_Constants.pdf`
- `172_Jerby_2023_New_Discriminant_Hardy_Z_Function_Corrected_Gram_Law.pdf`
- `173_Johansson_2001_Discrete_Orthogonal_Polynomial_Ensembles_Plancherel.pdf`
- `174_Johansson_2017_Arb_Arbitrary_Precision_Interval_Arithmetic.pdf`
- `175_Johansson_2018_Numerical_Integration_Ball_Arithmetic.pdf`
- `176_Jones-Sato-Wada-Wiens_1976_Diophantine_Representation_Primes.pdf`
- `177_Jun-Lee_2014_Dedekind_And_Exponential_Sums.pdf`
- `178_Jutila_1977_Zero_Density_Estimates_L_Functions.pdf`
- `179_Kaczorowski-Perelli_1999_Structure_Selberg_Class_I.pdf`
- `180_Kaczorowski-Pintz_1986_Oscillatory_Properties_Arithmetical_Functions_I.pdf`
- `181_KaczorowskiLanguascoPerelli2000_2000_A_note_on_Landau_s_formula.pdf`
- `182_Kaczorowski_1991_k_Functions_Multiplicative_Number_Theory_V.pdf`
- `183_Kaigh1976_1976_An_invariance_principle_for_random_walk_conditioned_by_a_late_return_to_zero.pdf`
- `184_Kanemitsu-Tsukada_2015_Hecke_Type_Zeta_Functions.pdf`
- `185_Kanemitsu-Tsukada_2015_Modular_Relation_Supremacy.pdf`
- `186_Kannan-Bachem_1979_Polynomial_Algorithms_Smith_Hermite_Normal_Forms.pdf`
- `187_Karatsuba-Voronin_1992_Vinogradov_Method_Riemann_Zeta.pdf`
- `188_Kargin_2013_Fluctuations_Riemann_Zeta_Zeros.pdf`
- `189_Kelly-Le_2018_Van_Der_Corput_Sets_Compact_Groups.pdf`
- `190_KhorunzhiyMarckert2009_2009_Uniform_bounds_for_exponential_moment_of_maximum_of_a_Dyck_path.pdf`
- `191_Kinnunen_1997_Hardy_Littlewood_Maximal_Function_Sobolev_Function.pdf`
- `192_Knopp_1994_Dirichlet_Series_Riemann_Functional_Equation.pdf`
- `193_Kolountzakis-Revesz_2003_Turan_Extremal_Problem.pdf`
- `194_Komori-Matsumoto-Tsumura_2023_Zeta_Functions_Root_Systems.pdf`
- `195_Korolev-Laurincikas_2023_Approximation_Mellin_Transform_Zeta_Axioms.pdf`
- `196_Korolev_2010_Gram_Law_Selberg_Conjecture_Zeros_Izv_Math.pdf`
- `197_Korolev_2011_Gram_Law_Argument_Riemann_Zeta_arXiv.pdf`
- `198_Korolev_2012_Gram_Law_Argument_Riemann_Zeta_Publ_Inst_Math.pdf`
- `199_Korolev_2012_Gram_Law_Riemann_Zeta.pdf`
- `200_Korolev_2016_Extreme_Values_S_Short_Intervals_Indian_J.pdf`
- `201_Korolev_2016_Gram_Law_Theory_Zeta_Part1_Proc_Steklov.pdf`
- `202_Kotnik-vandeLune_2004_Order_Mertens_Function.pdf`
- `203_Kousha2012_2012_Asymptotic_behavior_and_the_moderate_deviation_principle_for_the_maximum_of_a_Dyck_path.pdf`
- `204_Kowalski-Robert-Wu_2007_Small_Gaps_And_B_Free_Numbers.pdf`
- `205_Kowalski_2021_Exponential_Sums_Finite_Fields_Elementary.pdf`
- `206_Kowalski_2021_Exponential_Sums_Finite_Fields_II.pdf`
- `207_Kozma-Lev_2011_Exponential_Riesz_Bases_Discrepancy_BMO.pdf`
- `208_Kurasov-Sarnak_2020_Stable_Polynomials_Crystalline_Measures.pdf`
- `209_Labahn-Neiger-Zhou_2018_Hermite_Normal_Form_Polynomial_Matrix.pdf`
- `210_Lagarias2007_2007_Li_coefficients_for_automorphic_functions.pdf`
- `211_Landau_1912_Nullstellen_Zetafunktion.pdf`
- `212_Lapidus-VanFrankenhuysen_2000_Fractal_Geometry_Number_Theory.pdf`
- `213_Lau-Liu-Wu_2010_Symmetric_Square_L_Function_Coefficients.pdf`
- `214_LeClair_2016_Riemann_Hypothesis_Random_Walks_Zeta_Case.pdf`
- `215_LeeLeong2024_2024_New_explicit_bounds_for_the_Mertens_function_and_the_reciprocal_of_the_Riemann_zeta_function.pdf`
- `216_Lester-Matomaki-Radziwill_2015_Small_Scale_Zeros_Modular_Forms.pdf`
- `217_Lev-Olevskii_2015_Quasicrystals_Poisson_Summation_Formula.pdf`
- `218_Lev_2012_Riesz_Bases_Exponentials_Multiband_Spectra_Preprint.pdf`
- `219_LiYang2023_2023_An_improvement_on_Gauss_s_circle_problem_and_Dirichlet_s_divisor_problem.pdf`
- `220_Li_2019_Zeta_L_Functions_Number_Theory_Combinatorics.pdf`
- `221_Lindqvist-Seip_1998_Note_Greatest_Common_Divisor_Matrices.pdf`
- `222_Littlewood_1924_Zeros_Riemann_Zeta_Function.pdf`
- `223_Liu2022_2022_Multiplicative_functions_resembling_the_M_bius_function.pdf`
- `224_Lyubarskii-Seip_1997_Complete_Interpolating_Sequences_Paley_Wiener_Muckenhoupt_Ap.pdf`
- `225_LyubarskiiVershynin2010_2010_Uncertainty_principles_and_vector_quantization.pdf`
- `226_Matiyasevich2007a_1983_Hidden_Life_of_Riemann_s_Zeta_Function_1_Arrow_Bow_and_Targets.pdf`
- `227_Matiyasevich2007b_2007_Hidden_Life_of_Riemann_s_Zeta_Function_2_Electrons_and_Trains.pdf`
- `228_Matomaki-Radziwill-Tao_2015_Averaged_Chowla_Conjecture.pdf`
- `229_Matomaki-Radziwill_2015_Liouville_Short_Intervals.pdf`
- `230_Matomaki-Radziwill_2015_Sign_Changes_Hecke_Eigenvalues.pdf`
- `231_Matomaki-Radziwill_2016_Multiplicative_Functions_Short_Intervals.pdf`
- `232_Matomaki-Shao-Tao-Teravainen_2023_Higher_Uniformity_Arithmetic_Functions.pdf`
- `233_Matomaki-Teravainen_2023_Mobius_Function_All_Short_Intervals.pdf`
- `234_Matomaki_2010_Smooth_Numbers_Short_Intervals.pdf`
- `235_Matomaki_2016_Smooth_Numbers_Short_Intervals_II.pdf`
- `236_MelottiSaias2020_2020_On_path_partitions_of_the_divisor_graph.pdf`
- `237_Mirsky_1949_Frequency_Pairs_Square_Free_Numbers_Given_Difference.pdf`
- `238_Monien_2009_Hankel_Determinants_Dirichlet_Series.pdf`
- `239_Montgomery-Vaughan_1974_Hilberts_Inequality.pdf`
- `240_MontgomerySoundararajan2004_2004_Comm_Math_Phys.pdf`
- `241_Montgomery_1973_Pair_Correlation_Zeros_Zeta.pdf`
- `242_MossinghoffOliveiraTrudgian2021_2021_The_distribution_of_k_free_numbers.pdf`
- `243_Motohashi_1997_Spectral_Theory_Riemann_Zeta.pdf`
- `244_Muellner2017_2017_Automatic_sequences_fulfill_the_Sarnak_conjecture.pdf`
- `245_MullerEtAl2005_2005_Periodic_orbit_theory_of_universality_in_quantum_chaos.pdf`
- `246_Murahara-Onozuka_2025_Equidistribution_A_Points_Zeta_Derivatives.pdf`
- `247_MussardoLeClair2021_2021_Randomness_of_M_obius_coefficients_and_Brownian_motion_growth_of_the_Mertens_function_and_the_Riemann_hypothes.pdf`
- `248_Nakamura_2020_Dirichlet_Series_Periodic_Coefficients_Functional_Equation.pdf`
- `249_Ng2004_2004_Proc_London_Math_Soc.pdf`
- `250_Nishigaki_2024_Consecutive_Level_Spacings_GUE_Ratio.pdf`
- `251_Nishigaki_2025_Consecutive_Level_Spacings_CUE_Finite_Size_Zeta.pdf`
- `252_Norvidas_2011_Entire_Functions_Exponential_Sums.pdf`
- `253_Nunes2015_2015_Journal_of_Number_Theory.pdf`
- `254_Odlyzko-TeRiele_1985_Disproof_Mertens_Conjecture.pdf`
- `255_Odlyzko_1987_Distribution_Spacings_Between_Zeros_Zeta.pdf`
- `256_OganesyanHuse2007_2007_Localization_of_interacting_fermions_at_high_temperature.pdf`
- `257_Olevskii-Ulanovskii_2020_Fourier_Quasicrystals_Unit_Masses.pdf`
- `258_OwczarekPrellberg2014_2014_Pressure_exerted_by_a_vesicle_on_a_surface.pdf`
- `259_Patterson_1988_Introduction_Riemann_Zeta_Function.pdf`
- `260_Patterson_1988_Zeros_Zeta_And_Prime_Number_Theorem.pdf`
- `261_PeligradUtev2005_2005_A_new_maximal_inequality_and_invariance_principle_for_stationary_sequences.pdf`
- `262_Perelli_2016_Converse_Theorems_Zeta_Selberg_Class.pdf`
- `263_Perfekt-Pushnitski_2018_Spectrum_Multiplicative_Hilbert_Matrix.pdf`
- `264_PillaiYin2014_2014_Universality_of_covariance_matrices.pdf`
- `265_Pintz_2026_Oscillation_Mobius_Function_Zeta_Zeros.pdf`
- `266_Platt-Trudgian_2021_RH_True_Up_To_3e12.pdf`
- `267_Platt_2017_Isolating_Nontrivial_Zeros_Zeta.pdf`
- `268_Popov_1985_Transfer_Functions_Riemann_Zeta.pdf`
- `269_Radziwill-Soundararajan_2015_Quadratic_Twists_Central_L_Values.pdf`
- `270_Ramachandra_1976_Problems_Analytic_Number_Theory.pdf`
- `271_Richard_2005_Q_Functional_Equations_Excursion_Moments.pdf`
- `272_Riemann-Wilkins_1859_Prime_Counting_English_Translation.pdf`
- `273_RigalZadunaisky2015_2015_Twisted_semigroup_algebras.pdf`
- `274_RodgersTao2018_2018_RodgersTao2018.pdf`
- `275_Roesler_1986_Riemann_Hypothesis_Eigenvalue_Problem.pdf`
- `276_Roesler_1987_Riemann_Hypothesis_Eigenvalue_Problem_II.pdf`
- `277_Rota_1964_Foundations_Combinatorial_Theory_Mobius_Functions.pdf`
- `278_Saffari-Vaughan_1977_Fractional_Parts_X_Over_N_II.pdf`
- `279_Sawin_2022_Mobius_Cancellation_Polynomial_Sequences.pdf`
- `280_Sekatskii-Beltraminelli-Merlini_2012_Integrals_Logarithm_Zeta_RH.pdf`
- `281_Sekatskii_2013_Generalized_Bombieri_Lagarias_Li_Criterion.pdf`
- `282_Sekatskii_2014_Generalized_Li_Criterion_Zeroes_Location.pdf`
- `283_Sheth_2025_Euler_Products_Centre_Chebyshev_Bias.pdf`
- `284_Shir-MartinezAzcona-Chenu_2025_Surmise_Level_Spacing_Beyond_Nearest.pdf`
- `285_Sidi_2003_Riemann_And_Generalized_Zeta_Extrapolation.pdf`
- `286_Siegel_1922_Satz_Hamburger_Funktionalgleichung_Zetafunktion.pdf`
- `287_Soundararajan_2009_Partial_Sums_Mobius_Function.pdf`
- `288_Soundararajan_2010_Smooth_Numbers_Short_Intervals.pdf`
- `289_StampachStovicek2020_2020_On_Hankel_matrices_commuting_with_Jacobi_matrices_from_the_Askey_scheme.pdf`
- `290_Suzuki2025Hilbert_2025_On_the_Hilbert_space_derived_from_the_Weil_distribution.pdf`
- `291_Szekelyhidi1982_1982_Note_on_exponential_polynomials.pdf`
- `292_Tao-Teravainen_2018_Odd_Order_Logarithmically_Averaged_Chowla.pdf`
- `293_Tao-Teravainen_2019_Structure_Logarithmically_Averaged_Correlations.pdf`
- `294_Tao_2016_Logarithmically_Averaged_Chowla_Elliott_Two_Point.pdf`
- `295_Tenenbaum_2015_Analytic_Probabilistic_Number_Theory.pdf`
- `296_Tenenbaum_2017_Generalized_Mertens_Sums.pdf`
- `297_Titchmarsh-HeathBrown_1986_Theory_Riemann_Zeta_Function.pdf`
- `298_Trudgian_2008_Gram_Law_Fails_Positive_Proportion_Of_The_Time.pdf`
- `299_Trudgian_2014_Improved_Upper_Bound_Argument_Zeta_II.pdf`
- `300_Vaughan_1996_Eigenvalues_Redheffer_Matrix_II.pdf`
- `301_Vega_2023_Simple_Proof_Riemann_Hypothesis.pdf`
- `302_Volchkov_1995_Equality_Equivalent_Riemann_Hypothesis_Russian.pdf`
- `303_Weil_1952_Formules_Explicites_Nombres_Premiers_Transcription_VellaChemla.pdf`
- `304_Wilf_2004_Redheffer_Matrix_Partially_Ordered_Set.pdf`
- `305_Young_1974_Inequalities_Perturbation_Theorem_Paley_Wiener.pdf`
- `306_Youvan_2024_Phase_Winding_Riemann_Zeta.pdf`
- `307_Zhang_2013_Normalization_Beurling_Generalized_Primes_RH.pdf`
- `308_Zhao_2016_Multiple_Zeta_Polylogarithms_Special_Values.pdf`
- `309_Zhao_2026_Density_Results_r_Gaps_Between_Zeros_Zeta.pdf`
- `310_deBruijn1950_1950_The_roots_of_trigonometric_integrals.pdf`
- `311_deLaValleePoussin_1896_Recherches_Analytiques_Nombres_Premiers_I.pdf`
- `312_vonMangoldt_1895_Zu_Riemanns_Abhandlung_Anzahl_Primzahlen.pdf`
