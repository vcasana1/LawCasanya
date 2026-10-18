# LIBRARY TOTAL — índice maestro

Ruta en disco: `~/Documents/LIBRARY TOTAL/` (302 PDFs).
Actualizado: 2026-10-18 (Conrad 2005, Goldfeld 1982 y Sheth 2025 sobre productos de Euler parciales; antes el mismo día Bogomolny–Keating Nonlinearity I y II; antes el mismo día Berry 1988 y Bogomolny–Keating 1996 PRL; antes el mismo día LeClair 2016 y França–LeClair 2015). Fuente de cada descripción: primera página del propio PDF (`pdftotext -f 1 -l 2`), salvo donde se indique.

## Cómo usar este índice

1. Buscar aquí **antes** que en la web. `grep -i` sobre este fichero por tema, autor o palabra clave.
2. Citar **siempre por nombre de fichero completo**, nunca por número: la numeración se reasignó el 2026-10-18 al incorporar Conrad, Goldfeld y Sheth (ver `_renumeracion_2026-10-18_d.tsv`; antes el mismo día, Bogomolny–Keating Nonlinearity I y II: `_renumeracion_2026-10-18_c.tsv`; antes el mismo día, Berry y Bogomolny–Keating PRL: `_renumeracion_2026-10-18_b.tsv`; el mismo día, LeClair y França–LeClair: `_renumeracion_2026-10-18.tsv`; el 2026-10-17, Bourgain, Kinnunen y Korolev: `_renumeracion_2026-10-17.tsv`; antes, el 2026-10-16: `_renumeracion_2026-10-16_todos_enviados.tsv` y `_renumeracion_2026-10-10_b.tsv`; anteriores: `_renumeracion_2026-10-10.tsv`, `_renumeracion_2026-10-03.tsv`, `_renumeracion_2026-10-02.tsv`, `_renumeracion_2026-10-02_b.tsv`) y es alfabética por autor, así que volverá a moverse al añadir papers.
3. Antes de atribuir un enunciado a un paper, abrirlo y verificarlo. Este índice dice *dónde mirar*, no *qué afirmar*.
4. La colección histórica tiene capa OCR; el nuevo escaneo `177_Kaczorowski_1991_k_Functions_Multiplicative_Number_Theory_V.pdf` carece de capa de texto y debe consultarse visualmente. Cuando haya OCR, recordar que puede contener errores, sobre todo en fórmulas: para citar una expresión hay que mirar la página.

## Artículos enviados: productos de Euler parciales en la recta crítica (Goldfeld, Conrad, Sheth) — 2026-10-18

Tres PDF nuevos. Al de Goldfeld se le han quitado las dos portadas de Gallica (quedan las 4 páginas 471–474). Inserción: Conrad en 066 (antiguos 066–114 → 067–115), Goldfeld en 116 (antiguos 115–272 → 117–274), Sheth en 275 (antiguos 273–299 → 276–302); renumeración en `_renumeracion_2026-10-18_d.tsv`.

- `066_Conrad_2005_Partial_Euler_Products_Critical_Line.pdf` — K. Conrad, Partial Euler products on the critical line, Canad. J. Math. 57 (2) (2005), 267–297, doi:10.4153/CJM-2005-012-6. Generaliza el teorema de Goldfeld a productos de Euler generales en Re(s)=1/2. Teorema 1.2/5.11: si L(s) es holomorfa en Re(s)≥1/2 (excluye ζ, que tiene polo; ver Ejemplos 4.5 y 7.3), cumple la hipótesis de segundo momento con punto excepcional 1+it0 y orden R0, y el producto parcial en 1/2+it ~ C_t/(log x)^{r_t}, entonces L no se anula en Re(s)>1/2, r_t es el orden en 1/2+it y C_t = B_t/e^{r_tγ} (con factor (√2)^{R0} extra en t=t0/2). Teorema 1.3 (curvas elípticas): la asintótica equivale a ψ_E(x)=o(x log x), "mucho más profunda que RH" (RH ⇔ O(x log²x)); Teorema 6.3 general con ecuación funcional. §8: análogos incondicionales en cuerpos de funciones. 31 páginas. SHA-256 `2c07ab3c7b1cf085e13ef5ded728e8fb213aafd3123e1ed18870e65ef2241f4a`.
- `116_Goldfeld_1982_Produits_Partiels_Euleriens_Courbes_Elliptiques.pdf` — D. Goldfeld, Sur les produits partiels eulériens attachés aux courbes elliptiques, C. R. Acad. Sci. Paris Sér. I Math. 294 (1982), 471–474 (nota presentada por J.-P. Serre; copia Gallica/BnF). Si P_E(x)=∏_{p≤x}N_p/p ~ C(log x)^r, entonces L_E satisface RH, su orden en s=1 es r, y para r=0, C=√2/L_E(1)... (constante con √2). 4 páginas. SHA-256 `d947070b3973cd1745687db6b6433ed82504810f8d2fd33c8c93ead48a0b9713`.
- `275_Sheth_2025_Euler_Products_Centre_Chebyshev_Bias.pdf` — A. Sheth, Euler products at the centre and applications to Chebyshev's bias, Math. Proc. Cambridge Philos. Soc. 179 (2025), 331–349, doi:10.1017/S0305004125000234. Bajo GRH (y Ramanujan–Petersson si hace falta), asintótica del producto de Euler parcial de L(s,π) en el centro fuera de un conjunto de medida logarítmica finita; confirma una conjetura de Kurokawa (2012); aplicación al sesgo de Chebyshev en el marco de Aoki–Koyama (2023). 19 páginas. SHA-256 `234acc3588e199b41b5e2a0d7125a2f2645aa1d11a62208953b5a3e1cf3111ca`.

## Artículos enviados: Bogomolny–Keating, Nonlinearity I (1995) y II (1996) — 2026-10-18

Dos PDF nuevos; a ambos se les ha quitado la portada de descarga de IOPscience. Se insertan junto al PRL de 1996: el PRL pasa de 028 a 029, y los antiguos 029 en adelante suben dos posiciones; renumeración en `_renumeracion_2026-10-18_c.tsv`.

- `028_Bogomolny-Keating_1995_Random_Matrix_Theory_Riemann_Zeros_I_Three_Four_Point_Correlations.pdf` — E. B. Bogomolny y J. P. Keating, Random matrix theory and the Riemann zeros I: three- and four-point correlations, Nonlinearity 8 (1995), 1115–1131, doi:10.1088/0951-7715/8/6/013. Desde la fórmula explícita ceros–primos (análogo de la fórmula de traza de Gutzwiller) y una conjetura de Hardy–Littlewood sobre la distribución de los primos, las correlaciones de 3 y 4 puntos de los ceros son asintóticamente las de GUE; generaliza el cálculo de 2 puntos. 17 páginas (sin portada IOP). SHA-256 `e0d697160a15d8f4a78ecb4bc8e756ef952636827b3c37952112aa2203c8fbb3`.
- `030_Bogomolny-Keating_1996_Random_Matrix_Theory_Riemann_Zeros_II_n_Point_Correlations.pdf` — E. B. Bogomolny y J. P. Keating, Random matrix theory and the Riemann zeros II: n-point correlations, Nonlinearity 9 (1996), 911–935, doi:10.1088/0951-7715/9/4/006. Para todo n ≥ 2 la correlación de n puntos de los ceros coincide con la de GUE en el límite asintótico, bajo la conjetura de correlación de primos de Hardy–Littlewood; técnicas combinatorias para las sumas múltiples sobre primos y para desarrollar el determinante GUE. 25 páginas (sin portada IOP). SHA-256 `c0865177b94f1c4b90547958ced65d4691ecc9ee733de8ec8af678aae26a4db9`.

## Artículos enviados: Berry 1988 y Bogomolny–Keating 1996 — 2026-10-18

Dos PDF nuevos (ninguno duplica por SHA-256 un PDF anterior). Se insertan en orden alfabético y desplazan la numeración: 024–026 anteriores pasan a 025–027, y 027 en adelante pasa a 029 en adelante; renumeración completa en `_renumeracion_2026-10-18_b.tsv`. Del PDF de Berry se ha eliminado la portada de descarga de IOPscience (quedan las 9 páginas del artículo).

- `024_Berry_1988_Semiclassical_Formula_Number_Variance_Riemann_Zeros.pdf` — M. V. Berry, Semiclassical formula for the number variance of the Riemann zeros, Nonlinearity 1 (1988), 399–407, doi:10.1088/0951-7715/1/3/001. Varianza del número de ceros V(L;x) desde la fórmula de traza con los primos como órbitas periódicas; división en un régimen universal (GUE, L ≪ 1/τ*) y otro no universal descrito por los primos (L ≫ 1/τ*), con la escala intermedia τ* sujeta a ln2/ln(E/2π) ≪ τ* ≪ 1, ecuaciones (9)–(19); comparación con los datos de Odlyzko. 9 páginas (sin portada IOP). SHA-256 `1ea1e9b5ad8a53b7f1a7d63f097db3d4ccd5cab70bf0d36badd74c5fdb2a6987`.
- `029_Bogomolny-Keating_1996_Gutzwiller_Trace_Formula_Spectral_Statistics_Beyond_Diagonal.pdf` — E. B. Bogomolny y J. P. Keating, Gutzwiller's trace formula and spectral statistics: beyond the diagonal approximation, Phys. Rev. Lett. 77 (1996), 1472–1475, doi:10.1103/PhysRevLett.77.1472. Función de correlación de dos puntos para sistemas caóticos en el límite semiclásico: los términos no diagonales (pares de órbitas distintas) se evalúan relacionándolos con los diagonales mediante una función zeta clásica; para ζ de Riemann el resultado equivale a la conjetura de Hardy–Littlewood para pares de primos (cita [8], [14]). 4 páginas. SHA-256 `8b14ebfd4bdc17b7ad11ef69bd10daa3715cf937c7fe06db771845d762335796`.

## Artículos enviados: LeClair 2016 y França–LeClair 2015 (versión publicada) — 2026-10-18

Cuatro PDF recibidos; dos ya estaban en la carpeta byte a byte (arXiv:1307.8395v3 = `100_…`, SHA `3521…aae0d8`; arXiv:1407.4358v2 = `101_…`, SHA `6d91…236b87`) y no se duplican. Los dos nuevos desplazan la numeración desde 103 y desde 199; renumeración en `_renumeracion_2026-10-18.tsv`.

- `108_Franca-LeClair_2015_Transcendental_Equations_Individual_Zeros_L_Functions_CNTP_Published.pdf` — G. França y A. LeClair, Transcendental equations satisfied by the individual zeros of Riemann ζ, Dirichlet and modular L-functions, Commun. Number Theory Phys. 9 (2015), no. 1, 1–50 (versión publicada; `102_…` es el preprint arXiv:1502.06003v1, 51 páginas). Ceros de la línea crítica en correspondencia con los ceros del coseno; ecuación trascendente del n-ésimo cero que depende solo de n; solución aproximada con Lambert W; generalización a L de Dirichlet y de formas modulares; cálculo numérico. 50 páginas. Es la referencia FrancaLeClair2015 a citar como publicada. SHA-256 `f66547aeb94fed16b5084326a027137e376b5f708eecd1cedc4344119f09ee51`.
- `205_LeClair_2016_Riemann_Hypothesis_Random_Walks_Zeta_Case.pdf` — A. LeClair, Riemann Hypothesis and random walks: the zeta case, arXiv:1601.00914v1 (5 ene 2016), 20 páginas; revista no verificada. Producto de Euler finito ζ_N como serie de Dirichlet generalizada sobre el grupo Q_N (Def. 1–3, Prop. 1); Teorema 1 (Kac): B_N(u)=Σ_{n≤N}cos(u log p_n) es asintóticamente normal de varianza N/2 para u uniforme en [T,2T]; Prop. 2: B_N(t)=O(√N) para N<N_max(t)=[t²]; Teorema 3: producto de Euler truncado en N(t) válido a la derecha de la línea crítica con error R_N(s)→0 (heurístico, usa Cramér–Granville sumado (18)); de ahí argumenta S_δ(t)=O(1) y casi siempre en la rama principal, conjetura una ley normal para la correlación de 1 punto de los ceros, modelo probabilístico de los ceros y algoritmo estocástico para ceros muy altos (el 10^100-ésimo con >100 dígitos). No arbitrado en esta versión: las afirmaciones sobre S(t)=O(1) son heurísticas, no teoremas. SHA-256 `918986a890267f39d609262088be065a0fab457dede2a6d0a1ab458ecc3be685`.

## Artículos enviados: Bourgain, Kinnunen y Korolev (versión publicada) — 2026-10-17

Tres PDF incorporados para verificar citas de `ordinal_prime_cutoff`. Ninguno duplica (por SHA-256) un PDF anterior. Renumeración en `_renumeracion_2026-10-17.tsv`.

- `039_Bourgain_2017_Decoupling_Exponential_Sums_Riemann_Zeta.pdf` — J. Bourgain, Decoupling, exponential sums and the Riemann zeta function, arXiv:1408.5794v2 (22 Feb 2016); publicado en J. Amer. Math. Soc. 30 (2017), 205–224. Teorema 5: ζ(1/2+it) ≪ |t|^{13/84+ε}; §5, Teorema 6: (ε+13/84, ε+55/84) es un par de exponentes. 22 páginas. SHA-256 `095de11a030ee40bc996957b15a1880ca6f8c8121c6ae5953ca5a82c6893faae`.
- `187_Kinnunen_1997_Hardy_Littlewood_Maximal_Function_Sobolev_Function.pdf` — J. Kinnunen, The Hardy–Littlewood maximal function of a Sobolev function, Israel J. Math. 100 (1997), 117–124 (versión del autor, 6 páginas). Teorema 1.4: para 1<p<∞, u∈W^{1,p}(R^n) ⇒ Mu∈W^{1,p} y |D_i Mu| ≤ M D_i u c.t.p. (maximal centrado en bolas); (1.2) cita la desigualdad de Hardy–Littlewood–Wiener como Stein, Theorem I.1. SHA-256 `437f66e180001e3d7ca32b1f2035aa57f4ef6a0d97481b805c621b8ca9f366f3`.
- `191_Korolev_2012_Gram_Law_Argument_Riemann_Zeta_Publ_Inst_Math.pdf` — M. Korolev, Gram's law and the argument of the Riemann zeta function, Publ. Inst. Math. (Beograd) (N.S.) 92(106) (2012), 53–78, DOI 10.2298/PIM1206053K; versión publicada de arXiv:1106.0516. Teorema 4.2: momentos pares e impares de Δ_n en intervalos N<n≤N+M, N^{27/82+0.9ε}≤M≤N^{27/82+ε}; convención t_n con ϑ(t_n)=(n−1)π y t_{m−1}<γ_n≤t_m, Δ_n=m−n. Lema 2.1: Mertens con error explícito. Distinto de `192_Korolev_2012_Gram_Law_Riemann_Zeta.pdf` (arXiv:1011.3997, Izv. Math.). 26 páginas. SHA-256 `471ae8b71db7de7afc947da447f231f9a712b393b0f728615158f5246e7042fe`.

## Artículos enviados: Lev, Aryan y escaneo parcial de Gonek — 2026-10-16

Se han incorporado tres PDF distintos, incluida la versión editorial de Aryan y el escaneo de Gonek claramente marcado como incompleto. Ninguno resuelve una de las nueve referencias pendientes de v26. `Download 1.pdf` repite exactamente `Download.pdf` y `3_tonon.pdf` es un resumen de una página, no un artículo. Véase `IMPORTACION_TODOS_ARTICULOS_ENVIADOS_2026-10-16.md`.

- `005_Aryan_2022_Extension_Landau_Gonek_Formula_Published.pdf` — Farzad Aryan, On an extension of the Landau-Gonek formula, J. Number Theory 233 (2022), 389–404. Versión editorial completa; el preprint de 2019 ya estaba incorporado. SHA-256 `9228b8fa38b4aff4e67ae9ef1cb1faabddc91ca2d9434fdfb8dea5ea8af352fb`.
- `120_Gonek_1985_Formula_Landau_Mean_Values_Zeta_INCOMPLETE_pp92-96.pdf` — S. M. Gonek, A formula of Landau and mean values of zeta(s), Topics in Analytic Number Theory (1985), escaneo de páginas impresas 92–96 de una referencia bibliográfica de páginas 92–97. ESCANEO INCOMPLETO: falta al menos la página 97; artículo distinto de Gonek 1993 citado en v26. SHA-256 `7c68870fc4fe095115ddb1279b3fa8fa718f31e6ea350e3e29168ec91bd787a4`.
- `209_Lev_2012_Riesz_Bases_Exponentials_Multiband_Spectra_Preprint.pdf` — Nir Lev, Riesz bases of exponentials on multiband spectra, preprint arXiv:1101.3894v2 (2011); published in Proc. Amer. Math. Soc. 140 (2012), 3127–3132. Artículo completo; versión preprint. SHA-256 `9b5b836a6d1c066ad75166450994b7cccc9c2dadd404830ebfe411a645ff5c6d`.

## Segunda tanda de envíos verificados — 2026-10-16

Tres artículos incorporados: Hutchinson (1925), Davenport–Heilbronn (1936, parte I) y Balanzario–Sánchez-Ortiz (2007). Nueve referencias de v26 siguen pendientes. El PDF `3_tonon.pdf` es un resumen de una página y no corresponde al artículo de Hlawka (1975). Véanse `IMPORTACION_ENVIOS_2_V26_2026-10-16.md` y `PENDIENTES_V26_ACTUALIZADOS_2_2026-10-16.txt`.

- `012_Balanzario-SanchezOrtiz_2007_Zeros_Davenport_Heilbronn_Counterexample.pdf` — E. P. Balanzario and J. Sánchez-Ortiz, Zeros of the Davenport-Heilbronn counterexample, Math. Comp. 76 (2007), 2045–2049. 5 páginas PDF. SHA-256 `037b3392336fbb0420c228a896afc5226a28c8fbe5c7d5ff0fccca3a7e93f786`.
- `081_Davenport-Heilbronn_1936_Zeros_Certain_Dirichlet_Series_I.pdf` — H. Davenport and H. Heilbronn, On the zeros of certain Dirichlet series (I), J. London Math. Soc. 11 (1936), 181–185. 5 páginas PDF. SHA-256 `101a846674201f455775ef115004df9e6667d1b0bb5708f31311df79e472aa21`.
- `158_Hutchinson_1925_Roots_Riemann_Zeta_Function.pdf` — J. I. Hutchinson, On the roots of the Riemann zeta function, Trans. Amer. Math. Soc. 27 (1925), 49–60; 12 pages plus JSTOR cover. 13 páginas PDF. SHA-256 `143e3abbc405c85959c92341055587ab700e840e2d1f4ffc338f177d363855e9`.

## Envíos adicionales verificados — 2026-10-16

Ocho PDF incorporados; cinco referencias de v26 resueltas y once aún pendientes. Tres incorporaciones son artículos adicionales enviados por el usuario. Véanse `IMPORTACION_ENVIOS_ADICIONALES_V26_2026-10-16.md` y `PENDIENTES_V26_ACTUALIZADOS_2026-10-16.txt`.

- `007_Avdonin_1977_Riesz_Bases_Exponential_Functions_L2_Brief.pdf` — Avdonin, Riesz bases of exponential functions in L2; English translation of a two-page 1974 Zapiski LOMI note, J. Soviet Math. 8 (1977), 130–131. PDF de 2 páginas, SHA-256 `669391abf697457c65d164272a7c7b13bed4f9ba1c8bc0f917b346c8ba6da654`.
- `059_Chandrasekharan-Mandelbrojt_1959_Solutions_Riemann_Functional_Equation.pdf` — Chandrasekharan and Mandelbrojt, On solutions of Riemann's functional equation, Bull. Amer. Math. Soc. 65 (1959), 358–362. PDF de 5 páginas, SHA-256 `4048157fbc5f8e45b53109d863e082246ebf13649ad3618caeb72fb0f952f051`.
- `088_Diamond-Montgomery-Vorhauer_2006_Beurling_Primes_Large_Oscillation.pdf` — Diamond, Montgomery and Vorhauer, Beurling primes with large oscillation, Math. Ann. 334 (2006), 1–36. PDF de 36 páginas, SHA-256 `2ed6d5180cf048ffc1861bba48a27852fcd5ed6f790f4be6246162a46f2da73e`.
- `089_Diamond_1970_Asymptotic_Distribution_Beurling_Generalized_Integers.pdf` — Diamond, Asymptotic distribution of Beurling's generalized integers, Illinois J. Math. 14 (1970), 12–28. PDF de 17 páginas, SHA-256 `dd9e4e2a4f0e7209a8bf7ad58672b1a8df92747dcadaf4b216de8d517b179cff`.
- `188_Knopp_1994_Dirichlet_Series_Riemann_Functional_Equation.pdf` — Knopp, On Dirichlet series satisfying Riemann's functional equation, Invent. Math. 117 (1994), 361–372. PDF de 12 páginas, SHA-256 `896462641b277564b0f6068473e84907912c17878c886254cec0cb6cc6ac568b`.
- `212_Littlewood_1924_Zeros_Riemann_Zeta_Function.pdf` — Littlewood, On the zeros of the Riemann zeta-function, Proc. Cambridge Philos. Soc. 22 (1924), 295–318; PDF includes a publisher cover page. PDF de 25 páginas, SHA-256 `5febb162a749d3318066b8abbbc84202b52fffca3d39f6b628f2c544c3e633ea`.
- `230_Montgomery-Vaughan_1974_Hilberts_Inequality.pdf` — Montgomery and Vaughan, Hilbert's inequality, J. London Math. Soc. (2) 8 (1974), 73–82. PDF de 10 páginas, SHA-256 `6dd51024602eafefc2cfa011fc5f5341317cfce623d745b092063fcafede1355`.
- `298_Young_1974_Inequalities_Perturbation_Theorem_Paley_Wiener.pdf` — Young, Inequalities for a perturbation theorem of Paley and Wiener, Proc. Amer. Math. Soc. 43 (1974), 320–322. PDF de 3 páginas, SHA-256 `eef71ba6823ff33b590599dbe319df0aced7de789fcd016cd668e490b45649d4`.

## Incorporaciones verificadas desde rvm_zeta_pi_mertens_v26.tex — 2026-10-16

48 PDF nuevos; 14 referencias de artículos ya presentes; 16 artículos pendientes. 15 referencias son libros u otros recursos, fuera de la importación de artículos. La numeración global se ha actualizado por orden alfabético. Véanse `IMPORTACION_V26_2026-10-16.md`, `PENDIENTES_V26_2026-10-16.txt` y `_renumeracion_2026-10-16_v26.tsv`.

- `003_AriasdeReyna_2024_Explicit_Formula_Quasicrystal_Definition.pdf` — AriasdeReyna2024; 6 páginas. Fuente: https://arxiv.org/pdf/2402.10604. SHA-256: `3708790b6a6e897995f9fdc9d76f50666d4200f3a9294be0620baec8933fa164`.
- `013_Balazard-Saias-Yor_1999_Notes_Fonction_Zeta_Riemann_2_Transcription_VellaChemla.pdf` — BalazardSaiasYor1999; 3 páginas. Fuente: https://denisevellachemla.eu/transc-Balazard-Saias-Yor-1999.pdf. SHA-256: `54bf004d12453d9dd35ef22ed76c8ddeef4c2af52cc80f1853c7769cdbd369f8`. Transcripcion de Denise Vella-Chemla; no es el facsimil editorial.
- `018_Bellotti-Wong_2025_Improved_Argument_Zero_Counting_Zeta.pdf` — BellottiWong2025; 32 páginas. Fuente: https://arxiv.org/pdf/2412.15470. SHA-256: `9299073e0fbb836ca744790e5ac2c03a496df3194409aaa87832ba6161ead3b5`.
- `020_Benedetto-Powell-Yilmaz_2006_Sigma_Delta_Quantization_Finite_Frames.pdf` — BenedettoPowellYilmaz2006; 14 páginas. Fuente: https://www.math.umd.edu/~jjb/ffsd.pdf. SHA-256: `fb5e4779f49da93b7bb5a5b3518addb08a358264033d10c8da9da4fa3ded1ad1`.
- `023_Bernstein_1929_Fonctions_Absolument_Monotones.pdf` — Bernstein1929; 66 páginas. Fuente: https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/5418-11511_2007_Article_BF02592679.pdf. SHA-256: `51ee140e6a0315f4cd0adaf7c84179ad2003d1360237bd30544ce94a2cea78dc`. El DOI de v26 (BF02547400) no identifica este articulo. DOI correcto verificado: 10.1007/BF02592679. No se ha modificado v26.
- `025_Beurling_1937_Distribution_Nombres_Premiers_Generalises_I.pdf` — Beurling1937; 37 páginas. Fuente: https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/5572-11511_2006_Article_BF02546666.pdf. SHA-256: `8c4969a037b55a3cdd770129e53a1e66d0837831eefcb4c1b1e50161564e8bff`.
- `032_Bohr_1926_Fastperiodische_Funktionen_III_Dirichletentwicklung.pdf` — Bohr1926; 45 páginas. Fuente: https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/5360-11511_2006_Article_BF02543846.pdf. SHA-256: `58a7ec6bbee63c8e7cb8afd4d0783756d6b8e764824e8780f2441263ff777c1c`.
- `035_Bondarenko-Radchenko-Seip_2023_Fourier_Interpolation_Zeros_Zeta_L_Functions.pdf` — BondarenkoRadchenkoSeip2023; 51 páginas. Fuente: https://arxiv.org/pdf/2005.02996. SHA-256: `39e45572fb715ebab56c0ce4471a9944f4ae091e1baea9a3944ec5ac29e78ab4`.
- `043_Brent_1979_Zeros_Riemann_Zeta_Critical_Strip.pdf` — Brent1979; 12 páginas. Fuente: https://maths-people.anu.edu.au/~brent/pd/rpb047.pdf. SHA-256: `dc4ebb30bfef64fad2ebe43d67f9651dae4132188f0b5dc9b3fc4fba0f89fa47`.
- `046_Broucke-Debruyne-Revesz_2025_Well_Behaved_Beurling_Number_Systems.pdf` — BrouckeDebruyneRevesz2025; 24 páginas. Fuente: https://arxiv.org/pdf/2309.01567. SHA-256: `eb6863d69a936594e9df03485688ec8115b3ac0ade7de4e3dd99efa4fe14d899`.
- `047_Broucke-Debruyne-Vindas_2020_Beurling_Integers_RH_Large_Oscillation.pdf` — BrouckeDebruyneVindas2020; 31 páginas. Fuente: https://arxiv.org/pdf/2004.11501. SHA-256: `375da1cc390d96ebd7ee8c9b177c23fcfc874c439c98051f9b3de3bfb0f814b6`.
- `048_Broucke-Vindas_2024_Generalized_Prime_Random_Approximation.pdf` — BrouckeVindas2024; 15 páginas. Fuente: https://arxiv.org/pdf/2102.08478. SHA-256: `66b727b7b5b151844558b88c1495e1eca902b1c0ea01840b5e783f4b2ff0c9c8`.
- `063_Cohn-Elkies_2003_New_Upper_Bounds_Sphere_Packings_I.pdf` — CohnElkies2003; 26 páginas. Fuente: https://arxiv.org/pdf/math/0110009. SHA-256: `bb0c97f2de33b0dd50a29fa379001d358e59c6ef303ff28aad3c2c5c703b79ce`.
- `070_Conrey_1989_More_Than_Two_Fifths_Zeros_Critical_Line.pdf` — Conrey1989; 27 páginas. Fuente: https://gdz.sub.uni-goettingen.de/download/pdf/PPN243919689_0399/LOG_0004.pdf. SHA-256: `dca940c13c721df8569c8cc66cdcdb745cb413dea2730dc51daf2e7bb091b8e9`.
- `074_Corless-Gonnet-Hare-Jeffrey-Knuth_1996_Lambert_W_Function.pdf` — Corless1996; 32 páginas. Fuente: https://cs.uwaterloo.ca/research/tr/1993/03/W.pdf. SHA-256: `b057325af1728ff80622a73fcff3a8654e31d495c16e780968d9f4ebc57cea34`.
- `075_Cramer_1919_Nullstellen_Riemannschen_Zetafunktion.pdf` — Cramer1919; 28 páginas. Fuente: https://gdz.sub.uni-goettingen.de/download/pdf/PPN266833020_0004/LOG_0009.pdf. SHA-256: `50ea0fd4122d9868e1d2a83e54300939e5899c2d7854e1dc2ef4073a6b187ece`.
- `080_Daubechies-DeVore_2003_Bandlimited_Function_Stable_Sigma_Delta_Modulators.pdf` — DaubechiesDeVore2003; 32 páginas. Fuente: https://sites.math.duke.edu/~ingrid/publications/annals-v158-n2-p09.pdf. SHA-256: `0673b5ea24a2016834088dcc507a21be631418b890c2a6a31bf68c5eb1cc8d4e`.
- `083_Debruyne-Vindas_2019_Complex_Tauberian_Theorems_Laplace_Transforms.pdf` — DebruyneVindas2019; 30 páginas. Fuente: https://arxiv.org/pdf/1604.05069. SHA-256: `12d464b46a730ab8b5c5763ced370eefb4d90906be7c136a5ddfcbedd7a9d978`.
- `084_deLaValleePoussin_1896_Recherches_Analytiques_Nombres_Premiers_I.pdf` — delaValleePoussin1896; 76 páginas. Fuente: https://archive.org/download/recherchesanalyt00lava/recherchesanalyt00lava.pdf. SHA-256: `142bc6745dcfe73a4f7dec75ad888947f5f2bf4ba1b2311b33d20e14ab080831`. Separata completa de la primera parte: pp. 1-74, correspondientes a 183-256 del articulo citado. Extraida de las hojas PDF 13-86 del ejemplar Toronto, con cubierta e imprenta (hojas 11-12).
- `107_Franca-LeClair_2015_Transcendental_Equations_Individual_Zeros_L_Functions.pdf` — FrancaLeClair2015; 51 páginas. Fuente: https://arxiv.org/pdf/1502.06003. SHA-256: `309700c1051dcfa6a4850c8da8e77839c247f3e91abaafc773815899b090d116`.
- `130_Grosswald-Schnitzer_1978_Class_Modified_Zeta_L_Functions.pdf` — GrosswaldSchnitzer1978; 11 páginas. Fuente: https://msp.org/pjm/1978/74-2/pjm-v74-n2-p09-s.pdf. SHA-256: `a311d5b72621d65bf64fe7bdd2bab90126a3a69eed8fc39912a2822e7c8b3717`.
- `131_Guillera_2013_Sums_Nontrivial_Zeros_Riemann_Zeta.pdf` — Guillera2013; 17 páginas. Fuente: https://arxiv.org/pdf/1307.5723. SHA-256: `31d643cab391998f575cf5345953839ff75c37acd9771cff2b833e9978393886`.
- `132_Gunturk-Thao_2003_Ergodic_Dynamics_Sigma_Delta_Quantization.pdf` — GunturkThao2003; 33 páginas. Fuente: https://arxiv.org/pdf/math/0308223. SHA-256: `7408b94a4869e0285a4e2da2d6340f805772d0224c481a0814da9865d2e82c56`.
- `134_Hadamard_1896_Distribution_Zeros_Zeta_Consequences_Arithmetiques.pdf` — Hadamard1896; 23 páginas. Fuente: https://www.numdam.org/item/BSMF_1896__24__199_1.pdf. SHA-256: `7620c7875b938e804fe11b81c465c76dd92debd0b90be4d8dffa06276da0c2ba`.
- `135_Hamburger_1921_Riemannsche_Funktionalgleichung_Zeta_Funktion_I.pdf` — Hamburger1921; 16 páginas. Fuente: https://gdz.sub.uni-goettingen.de/download/pdf/PPN266833020_0010/LOG_0027.pdf. SHA-256: `e73fc1a949fa52184e8c95cc4fe72f2dc3d8dd143ab131e117e9cc0adc4e7210`.
- `140_Hasanalizade-Shen-Wong_2022_Counting_Zeros_Riemann_Zeta.pdf` — HasanalizadeShenWong2022; 16 páginas. Fuente: https://arxiv.org/pdf/2107.06506. SHA-256: `3fc4c89f49249924e61cb0d289d81559faed53fcbb838628ea32dc7ec6f89fbf`.
- `148_Hilberdink-Lapidus_2006_Beurling_Zeta_Generalised_Primes_Fractal_Membranes.pdf` — HilberdinkLapidus2006; 31 páginas. Fuente: https://arxiv.org/pdf/math/0410270. SHA-256: `34fe75bc30bbcc68f8d94ddc9d9e7ab84d62a41e50924475ccc5d7aaaad22f08`.
- `154_Hruscev-Nikolskii-Pavlov_1981_Unconditional_Bases_Exponentials_Reproducing_Kernels.pdf` — HruscevNikolskiiPavlov1981; 122 páginas. Fuente: https://internetanalysisseminar.wustl.edu/sites/default/files/Hruschev_Nikolski_Pavlov.pdf. SHA-256: `5f3f6ddbf88a53184904ec26d8dd728b4f1532c6dc3acec66e53598ba346d639`.
- `161_Ingham_1936_Trigonometrical_Inequalities_Theory_Series.pdf` — Ingham1936; 14 páginas. Fuente: https://gdz.sub.uni-goettingen.de/download/pdf/PPN266833020_0041/LOG_0042.pdf. SHA-256: `064d613643f0c4bac17fe1390367d5c4d82b5cef883e73e72a9828d3ed647671`.
- `170_Johansson_2017_Arb_Arbitrary_Precision_Interval_Arithmetic.pdf` — Johansson2017; 12 páginas. Fuente: https://arxiv.org/pdf/1611.02831. SHA-256: `44802d5cce02bf91a3d155870b8f315f2955866e283bfb48f6776a07f35f6ebf`.
- `171_Johansson_2018_Numerical_Integration_Ball_Arithmetic.pdf` — Johansson2018; 8 páginas. Fuente: https://arxiv.org/pdf/1802.07942. SHA-256: `64abe78ce44e513bacf764e205f5f4eb728e6c6a0c79dc1a114b2cbfb44aae78`.
- `175_Kaczorowski-Perelli_1999_Structure_Selberg_Class_I.pdf` — KaczorowskiPerelli1999; 35 páginas. Fuente: https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6577-11511_2006_Article_BF02392574.pdf. SHA-256: `4e33441a8ef5a7c6d8263e72deb75ea2551854ab6e0dd1ffbaa1e716c0ff38ea`.
- `193_Kotnik-vandeLune_2004_Order_Mertens_Function.pdf` — KotnikvandeLune2004; 9 páginas. Fuente: https://www.maths.tcd.ie/EMIS/journals/EM/expmath/volumes/13/13.4/Kotnik.pdf. SHA-256: `749bc974510342e080942dafe6e65324765f17ff9232dc1c72c319629533844b`.
- `198_Kozma-Lev_2011_Exponential_Riesz_Bases_Discrepancy_BMO.pdf` — KozmaLev2011; 16 páginas. Fuente: https://arxiv.org/pdf/1009.2188. SHA-256: `7a45486d020f2fae0e06abb2d04407556b6169d96c1ce2b48eb36f0d72012995`.
- `199_Kurasov-Sarnak_2020_Stable_Polynomials_Crystalline_Measures.pdf` — KurasovSarnak2020; 15 páginas. Fuente: https://arxiv.org/pdf/2004.05678. SHA-256: `3d1bf0cec1b034878628a65f34b46ca00a29a8cfff28f63cdc1d60981ac3186d`.
- `202_Landau_1912_Nullstellen_Zetafunktion.pdf` — Landau1912; 18 páginas. Fuente: https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0071/LOG_0057.pdf. SHA-256: `92841e7262f65efb0bdaa774bf0dc56f621a608cc92b4fab858973bcf78a4cf7`.
- `208_Lev-Olevskii_2015_Quasicrystals_Poisson_Summation_Formula.pdf` — LevOlevskii2015; 16 páginas. Fuente: https://arxiv.org/pdf/1312.6884. SHA-256: `d79eabd9fcc6ea4bbce8b5fd1a23db3c55f49288a89361c67351c90bf8a58ef2`.
- `239_Nakamura_2020_Dirichlet_Series_Periodic_Coefficients_Functional_Equation.pdf` — Nakamura2020; 7 páginas. Fuente: https://arxiv.org/pdf/2008.02570. SHA-256: `b2f5410d4e219b51101d1ab09799ea83237f0e7b8048882aa43064a583a4f032`.
- `248_Olevskii-Ulanovskii_2020_Fourier_Quasicrystals_Unit_Masses.pdf` — OlevskiiUlanovskii2020; 6 páginas. Fuente: https://comptes-rendus.academie-sciences.fr/mathematique/item/10.5802/crmath.142.pdf. SHA-256: `9a22a260362536c2eba07a0aae2682847f47bb219f78158a53d7a590d6475c3c`.
- `253_Perelli_2016_Converse_Theorems_Zeta_Selberg_Class.pdf` — Perelli2016; 24 páginas. Fuente: https://arxiv.org/pdf/1605.02354. SHA-256: `1e09b1fa93612c9936417d18a024fc40e4f50c99cc6c586d8914af7ea81bdcfa`.
- `258_Platt_2017_Isolating_Nontrivial_Zeros_Zeta.pdf` — Platt2017; 20 páginas. Fuente: https://research-information.bris.ac.uk/ws/files/78836669/platt_zeta_submitted.pdf. SHA-256: `13c5b86a783d5bca55ad0eb881bb206efd3d15297da8cbbdf762af4aa3664697`.
- `272_Sekatskii-Beltraminelli-Merlini_2012_Integrals_Logarithm_Zeta_RH.pdf` — SekatskiiBeltraminelliMerlini2012; 22 páginas. Fuente: https://arxiv.org/pdf/0806.1596. SHA-256: `1cbdea34935471ddafff71891cf741a9b7d1455536ac1ba5845f2abd372dc2d5`.
- `278_Siegel_1922_Satz_Hamburger_Funktionalgleichung_Zetafunktion.pdf` — Siegel1922; 5 páginas. Fuente: https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0086/LOG_0022.pdf. SHA-256: `cbba7de9efd3dec8a25b61a1cf4c0d200d2fcc82ea1a6c0530b1478bd0b3cdfe`.
- `291_Trudgian_2014_Improved_Upper_Bound_Argument_Zeta_II.pdf` — Trudgian2014; 10 páginas. Fuente: https://arxiv.org/pdf/1208.5846. SHA-256: `274b3a0a14d79400f23505ede664a2f77b0a6ad7278245d25ec6e06169e2a303`.
- `294_Volchkov_1995_Equality_Equivalent_Riemann_Hypothesis_Russian.pdf` — Volchkov1995; 2 páginas. Fuente: https://umj.imath.kiev.ua/index.php/umj/article/download/5435/7559. SHA-256: `810b64c9427d2c56e75bb972d59db75cee3f44361df5a05456137d66d1ad8825`. Original ruso, Ukr. Mat. Zh. 47 (1995), 422-423; corresponde a la traduccion inglesa citada, 491-493.
- `295_vonMangoldt_1895_Zu_Riemanns_Abhandlung_Anzahl_Primzahlen.pdf` — vonMangoldt1895; 52 páginas. Fuente: https://gdz.sub.uni-goettingen.de/download/pdf/PPN243919689_0114/LOG_0020.pdf. SHA-256: `424be8674eb047fd3450ef00902f8cb42e05e3de1fdce0c13e19e7bdd67bd7a7`.
- `296_Weil_1952_Formules_Explicites_Nombres_Premiers_Transcription_VellaChemla.pdf` — Weil1952; 11 páginas. Fuente: https://denisevellachemla.eu/transc-Weil-1952.pdf. SHA-256: `1edd4a831d2fcc3a5d01d82d7bbb933b7916b84d4e87b60bbe144dd883c8ce26`. Transcripcion completa de Denise Vella-Chemla (2020); no es el facsimil editorial. Procedencia y transcripcion indicadas en el nombre.
- `300_Zhang_2013_Normalization_Beurling_Generalized_Primes_RH.pdf` — Zhang2013; 12 páginas. Fuente: https://ac.inf.elte.hu/Vol_039_2013/doi/459_39.pdf. SHA-256: `8ae7654d73869adcb8f354451e7116ba7e232c91bc1bc64347d4b8f0d903904f`.

## Avisos de integridad

- **`264_Riemann_1859_Number_Of_Primes_Below_A_Given_Magnitude.pdf` NO es el paper de Riemann.** Es un preprint anónimo de 2026 (pdfTeX, 23-05-2026) titulado *"Unexpected phase summation patterns in the imaginary parts of the Riemann zeros: a critical re-analysis"*, sobre las sumas parciales S(N) = Σ_{n≤N} e^{iγ_n}. Además tiene las citas rotas (`[?]`). El texto real de Riemann está en `263_Riemann-Wilkins_1859_Prime_Counting_English_Translation.pdf` (texto alemán original, transcrito por D. R. Wilkins; el nombre del fichero dice `English_Translation` pero no lo es). El fichero `264_Riemann_1859_Number_Of_Primes_Below_A_Given_Magnitude.pdf` conserva por ahora un nombre heredado incorrecto.
- **`094_Edwards_1974_Riemanns_Zeta_Function.pdf` está incompleto**: el escaneo cubre las páginas impresas 1–122 de 311. Faltan los capítulos 7–12 y el apéndice. Detalle en §13.
- Tres artículos están escaneados a doble página (A4 apaisado, dos páginas impresas por hoja): `174_Jutila_1977_Zero_Density_Estimates_L_Functions.pdf`, `177_Kaczorowski_1991_k_Functions_Multiplicative_Number_Theory_V.pdf` y `261_Ramachandra_1976_Problems_Analytic_Number_Theory.pdf`. Al citar, hoja de PDF y página impresa no coinciden.
- **`164_Ivic_1985_Riemann_Zeta_Theory_Applications.pdf` y `166_Ivic_2003_Riemann_Zeta_Dover_Reprint.pdf` son el mismo libro.** El Dover 2003 es reimpresión sin abreviar de la Wiley 1985 — misma paginación — y solo aporta la lista de erratas (xvii–xix), extraída a `ERRATA_Ivic.md`. Esas erratas se aplican a ambos ficheros.
- Calidad no verificada / fuera de circuito arbitrado: `078_Dannon_2008_Riemann_Zeta_Function.pdf` (Gauge Institute), `293_Vega_2023_Simple_Proof_Riemann_Hypothesis.pdf` y `299_Youvan_2024_Phase_Winding_Riemann_Zeta.pdf`. Usar solo como material a contrastar, no como fuente.

## Incorporaciones verificadas — 2026-10-10

- `111_Fujii_1974_Zeros_Dirichlet_L_Functions_I.pdf` — A. Fujii, *On the zeros of Dirichlet L-functions. I*, *Trans. Amer. Math. Soc.* **196** (1974), 225–235; DOI: 10.1090/S0002-9947-1974-0349603-2. 11 páginas, escaneo con capa de texto (OCR con errores en fórmulas). Main Theorem (incondicional, modificando el método de Selberg): para χ primitivo mod q, 0<a_i≤1/4, q≤T^{1/4−a_1}, T^{1/2+a_2}≤H≤T y 0<h≤H−(H/√T)^{1/8} (leído en la página 225), ∫_T^{T+H}(S(t+h,χ)−S(t,χ))^{2k}dt = c_k H (2 log(2+h log T))^k (1+O((Ak)^{3k}(log(2+h log T))^{−1/2})), con c_k=(2k)!/((2π)^{2k}k!). Para ζ (q=1), H=T, el rango cubre 0<h≤1. Es la prueba del lema de momentos anunciado en `113_Fujii_1975_Distribution_Zeros_Zeta_Short_Intervals.pdf` y usado como Lema 1 en `112_Fujii_1975_Difference_r_Consecutive_Ordinates_Zeros_Zeta.pdf`. SHA-256: `9c50fdb9699d779d6047a8a49f4bd82d5b29a879628da1843fa34992b4a40325`.
- `006_Avdonin-Ivanov_2001_Exponential_Riesz_Bases_Subspaces_Divided_Differences.pdf` — S. A. Avdonin y S. A. Ivanov, *Exponential Riesz bases of subspaces and divided differences*. Preprint arXiv:math/0103160v1 (26 mar 2001), 19 páginas con capa de texto; versión publicada: *St. Petersburg Math. J.* **13** (2002), núm. 3, 339–351 (no es el fichero). Bases de Riesz de diferencias divididas de exponenciales cuando puntos de Λ se acercan; Teorema 1 (criterio de Pavlov: Λ uniformemente discreta + función generatriz con |F(x+ih)|² de Helson–Szegő ⇔ A₂), Teorema 3 (diferencias divididas generalizadas para Λ unión finita de conjuntos separados), Teorema 4 (resultado negativo). DOI: 10.48550/arXiv.math/0103160. SHA-256: `40a557049e47703b55e670633bc120ac8cc054342fc4f0cac638718c628451b6`.
- `113_Fujii_1975_Distribution_Zeros_Zeta_Short_Intervals.pdf` — A. Fujii, *On the distribution of the zeros of the Riemann zeta function in short intervals*, *Bull. Amer. Math. Soc.* **81** (1975), núm. 1, 139–142; DOI: 10.1090/S0002-9904-1975-13674-3. 4 páginas, escaneo con capa de texto (OCR con errores en fórmulas). Anuncio sin pruebas ("Details will appear later"): Lema de momentos ∫_T^{2T}(S(t+h)−S(t))^{2k}dt con término principal en (log(3+h log T))^k, obtenido modificando el método de Selberg; consecuencias para diferencias de ordenadas y equidistribución. Distinto de `112_Fujii_1975_Difference_r_Consecutive_Ordinates_Zeros_Zeta.pdf` (Proc. Japan Acad.), cuyo Lema 1 remite la prueba del lema de momentos a Fujii, Trans. AMS 196 (1974). SHA-256: `44165f8987f9de3e92e2c83c9d63899a239fdacda9430d1efbfeed050a8c8fbc`.
- `155_Hughes-Rudnick_2002_Linear_Statistics_Zeros_Zeta.pdf` — C. P. Hughes y Z. Rudnick, *Linear statistics for zeros of Riemann's zeta function*. Preprint arXiv:math/0208220v1 (28 ago 2002), 9 páginas con capa de texto; revista no verificada. Estadísticos lineales suaves de los ceros escalados a altura T; los primeros momentos tienden a los gaussianos, con número de momentos dependiente del estadístico; sin RH. DOI: 10.48550/arXiv.math/0208220. SHA-256: `2225d590d97abd13a4b973bd3d936a7b07fb45a3296739438f8ce57f657cdebd`.
- `215_Lyubarskii-Seip_1997_Complete_Interpolating_Sequences_Paley_Wiener_Muckenhoupt_Ap.pdf` — Yu. I. Lyubarskii y K. Seip, *Complete interpolating sequences for Paley–Wiener spaces and Muckenhoupt's (A_p) condition*, *Rev. Mat. Iberoam.* **13** (1997), núm. 2, 361–376; DOI: 10.4171/RMI/224. Versión publicada (EMS Press), 16 páginas con capa de texto. Teorema 1: Λ es sucesión de interpolación completa para L^p_π ⇔ Carleson/separación, función generatriz S de tipo exponencial π, y condición (A_p) discreta (equivalentemente |S(x)|/dist(x,Λ) en A_p); para p=2 coincide con Pavlov–Nikol'skii–Minkin. Teorema 2: estabilidad tipo Kadec con constante 1/(2 max(p,q)); para p=2 es el teorema 1/4 de Kadec. SHA-256: `31d7cbe557909189972c7a5401924f2efc8c023f469dc853c6327bd08d5d471d`.

## Incorporaciones verificadas — 2026-10-03

- `112_Fujii_1975_Difference_r_Consecutive_Ordinates_Zeros_Zeta.pdf` — A. Fujii, *On the Difference between r Consecutive Ordinates of the Zeros of the Riemann Zeta Function*, *Proc. Japan Acad.* **51** (1975), núm. 10, 741–743; DOI: 10.3792/pja/1195518466. 3 páginas con capa de texto (OCR con errores en fórmulas; citar mirando la página). Con d(γ_n,r)=(γ_{n+r}−γ_n)/r (sin centrar), Teorema 1: S_{r,k}(T)=N(T)^{-1}Σ_{T<γ_n≤2T} d(γ_n,r)^k ≪ (Ak)^{3k²/(2k+1)}(log(3+k))^k r^{−2k²/(2k+1)}/(log T)^k, para 1≤k≪(T log T)^{2/3}, 1≤r≪k^{3/2}. Teorema 2: N_r(C/log T,T)≪N(T)exp(−A(rC)^{2/3}(log rC)^{−1/3}) (r-gaps grandes). Lema 1: momentos 2k de S(t+h)−S(t) (cita Fujii, Trans. AMS 196 (1974)). Lema 2: paso de promedio en t a promedio sobre ceros, solo para gaps grandes. SHA-256: `7a0df34ac25c372fe9faf4807d7b534f0072500734d9030922daa9c52cbeb715`.

## Incorporaciones verificadas — 2026-10-02

- `105_Franca-LeClair_2014_Statistical_Properties_Riemann_Zeros_Explicit_Equation_nth_Zero.pdf` — G. França y A. LeClair, *Statistical and other properties of Riemann zeros based on an explicit equation for the n-th zero on the critical line*. Preprint arXiv:1307.8395v3 (10 mar 2014), 26 páginas, con capa de texto; revista no verificada. Ecuación trascendente para la ordenada del n-ésimo cero, solución aproximada con Lambert W, ỹ_n = 2π(n−11/8)/W((n−11/8)/e) (ec. 25), correlación de pares y reconstrucción de π(x) con ceros sintéticos. SHA-256: `352192003691fb4c58a73729202acfb16605f48fd1c58eac35e9e53580aae0d8`.
- `106_Franca-LeClair_2014_Theory_Zeros_Riemann_Zeta_And_Other_L_Functions.pdf` — G. França y A. LeClair, *A theory for the zeros of Riemann ζ and other L-functions (updated)*. Notas de curso, arXiv:1407.4358v2 (16 ago 2024; la v1 es de 2014, de ahí el año del nombre), 93 páginas con capa de texto; revista no verificada. Repaso de ζ, analogía electrostática, ceros de la línea crítica en correspondencia con ceros del coseno, ecuación trascendente del n-ésimo cero, generalización a L-funciones de Dirichlet y de formas modulares. SHA-256: `6d91ed2dc58e083b5288d13bc03be274c73c68ba330e39aedd1dc83d37236b87`.
- `168_Jerby_2023_New_Discriminant_Hardy_Z_Function_Corrected_Gram_Law.pdf` — Y. Jerby, *A New Discriminant for the Hardy Z-Function and the Corrected Gram's Law*. arXiv:2310.14415v1 (22 oct 2023), 48 páginas con capa de texto; revista no verificada. Discriminante Δ_n(a) de la realidad de ceros consecutivos de Z(t), ley de Gram corregida, repulsión G-B-G. SHA-256: `dbc3933c3a8e627a47f4de7386bd4138e988fc566083ab04a5c944e9367ad7eb`.
- `290_Trudgian_2008_Gram_Law_Fails_Positive_Proportion_Of_The_Time.pdf` — T. Trudgian, *Gram's Law Fails a Positive Proportion of the Time*. arXiv:0811.0883v1 (6 nov 2008), 10 páginas con capa de texto; revista no verificada. Positividad de la proporción de fallos de la ley de Gram y de éxitos débiles. SHA-256: `24687edfb2336552f4a82eacfb820ddd4121d5241f0b8b7ed2a2b3649341b42c`.

## Incorporaciones verificadas — 2026-09-27

- `176_Kaczorowski-Pintz_1986_Oscillatory_Properties_Arithmetical_Functions_I.pdf` — J. Kaczorowski y J. Pintz, *Oscillatory Properties of Arithmetical Functions. I*, *Acta Mathematica Hungarica* **48** (1986), núms. 1–2, 173–185; DOI: 10.1007/BF01949062. Separata completa de 13 páginas, obtenida de una copia institucional de la University of British Columbia. SHA-256: `e8c5eb6d3dea6a4ae1d8180d8a9a5821b48030ab1b3322f49481f5e60f2168be`.
- `177_Kaczorowski_1991_k_Functions_Multiplicative_Number_Theory_V.pdf` — J. Kaczorowski, *The k-functions in multiplicative number theory. V. Changes of sign of some arithmetical error terms*, *Acta Arithmetica* **59** (1991), 37–58; DOI: 10.4064/aa-59-1-37-58. Escaneo editorial completo de 12 hojas a doble página, descargado de IMPAN y contrastado con la copia de EuDML/ICM. SHA-256: `fd84d3f82c1de764cb362ac2d26706e180512f7831993a671b77517761053b06`.

## Incorporaciones verificadas — 2026-09-26

- `008_Aymone-Sidoravicius_2017_Partial_Sums_Biased_Random_Multiplicative_Functions.pdf` — M. Aymone y V. Sidoravicius, *Partial Sums of Biased Random Multiplicative Functions*. Preprint arXiv:1412.1157v2; funciones multiplicativas aleatorias sesgadas, sumas parciales y formulación probabilística de RH.
- `121_Gonek_2012_Finite_Euler_Products_Riemann_Hypothesis.pdf` — S. M. Gonek, *Finite Euler Products and the Riemann Hypothesis*. *Transactions of the American Mathematical Society* 364 (2012), 2157–2191; DOI/identificador AMS S0002-9947(2011)05546-7.
- `066_Conrad_2005_Partial_Euler_Products_Critical_Line.pdf` — productos de Euler parciales en Re(s)=1/2: convergencia ⇒ no ceros a la derecha, orden de anulación, factor √2; equivale a una condición más profunda que RH. doi:10.4153/CJM-2005-012-6
- `116_Goldfeld_1982_Produits_Partiels_Euleriens_Courbes_Elliptiques.pdf` — teorema original de Goldfeld (productos parciales de curvas elípticas ⇒ RH, factor √2).
- `275_Sheth_2025_Euler_Products_Centre_Chebyshev_Bias.pdf` — asintótica del producto de Euler parcial en el centro bajo GRH; sesgo de Chebyshev. doi:10.1017/S0305004125000234
- `288_Tenenbaum_2017_Generalized_Mertens_Sums.pdf` — G. Tenenbaum, *Generalized Mertens Sums*. En *Analytic Number Theory, Modular Forms and q-Hypergeometric Series*, Springer Proc. Math. Stat. 221 (2017), pp. 733–736; también arXiv:1910.02781v1.

- `010_BaezDuarte-Balazard-Landreau-Saias_2000_Notes_sur_la_fonction_zeta_de_Riemann_3.pdf` — L. Báez-Duarte, M. Balazard, B. Landreau y E. Saias, *Notes sur la fonction ζ de Riemann, 3*, *Advances in Mathematics* 149 (2000), 130–144; DOI: 10.1006/aima.1999.1861. PDF completo de 15 páginas, procedente de la copia editorial aportada en Downloads.

## Incorporaciones verificadas desde excursion_area_section_v32.txt — 2026-09-26

Se incorporan únicamente PDFs completos procedentes de arXiv o repositorios institucionales/publisher open access. Matomäki–Radziwiłł (2016) se verificó como ya existente y no se duplicó.

- `052_Carmona-Petrelis_2017_Limit_Theorems_Random_Walk_Excursion.pdf` — incorporado desde una copia completa verificada de arXiv o repositorio institucional.
- `086_Denisov-Kolb-Wachtel_2015_Local_Asymptotics_Random_Walk_Excursions.pdf` — incorporado desde una copia completa verificada de arXiv o repositorio institucional.
- `133_Guth-Maynard_2026_New_Large_Value_Estimates_Dirichlet_Polynomials.pdf` — incorporado desde una copia completa verificada de arXiv o repositorio institucional.
- `139_Harper_2020_Moments_Random_Multiplicative_Functions_I.pdf` — incorporado desde una copia completa verificada de arXiv o repositorio institucional.
- `143_Helfgott-Thompson_2023_Summing_Mobius_Faster_Elementary_Algorithm.pdf` — incorporado desde una copia completa verificada de arXiv o repositorio institucional.
- `157_Hurst_2018_Computations_Mertens_Function_Improved_Bounds.pdf` — incorporado desde una copia completa verificada de arXiv o repositorio institucional.
- `167_Janson_2007_Brownian_Excursion_Area_Wright_Constants.pdf` — incorporado desde una copia completa verificada de arXiv o repositorio institucional.
- `223_Matomaki-Shao-Tao-Teravainen_2023_Higher_Uniformity_Arithmetic_Functions.pdf` — incorporado desde una copia completa verificada de arXiv o repositorio institucional.
- `224_Matomaki-Teravainen_2023_Mobius_Function_All_Short_Intervals.pdf` — incorporado desde una copia completa verificada de arXiv o repositorio institucional.
- `256_Pintz_2026_Oscillation_Mobius_Function_Zeta_Zeros.pdf` — incorporado desde una copia completa verificada de arXiv o repositorio institucional.
- `262_Richard_2005_Q_Functional_Equations_Excursion_Moments.pdf` — incorporado desde una copia completa verificada de arXiv o repositorio institucional.
## Incorporaciones verificadas desde excursion_area_section_v32.txt — 2026-09-26

Se incorporan únicamente PDFs completos procedentes de arXiv o repositorios institucionales/publisher open access. Matomäki–Radziwiłł (2016) se verificó como ya existente y no se duplicó.

- `279_Soundararajan_2009_Partial_Sums_Mobius_Function.pdf` — incorporado desde una copia completa verificada de arXiv o repositorio institucional.
- `284_Tao-Teravainen_2018_Odd_Order_Logarithmically_Averaged_Chowla.pdf` — incorporado desde una copia completa verificada de arXiv o repositorio institucional.
- `285_Tao-Teravainen_2019_Structure_Logarithmically_Averaged_Correlations.pdf` — incorporado desde una copia completa verificada de arXiv o repositorio institucional.
- `286_Tao_2016_Logarithmically_Averaged_Chowla_Elliott_Two_Point.pdf` — incorporado desde una copia completa verificada de arXiv o repositorio institucional.
## Incorporaciones verificadas desde excursion_area_section_v32.txt — 2026-09-26

Se incorporan únicamente PDFs completos procedentes de arXiv o repositorios institucionales/publisher open access. Matomäki–Radziwiłł (2016) se verificó como ya existente y no se duplicó.

- `026_Bjorner_2011_Cell_Complex_Number_Theory.pdf` — incorporado desde una copia completa verificada de arXiv o repositorio institucional.
- `102_Ford_2002_Vinogradov_Integral_Bounds_Riemann_Zeta.pdf` — incorporado desde una copia completa verificada de arXiv o repositorio institucional.
- `279_Soundararajan_2009_Partial_Sums_Mobius_Function.pdf` — incorporado desde una copia completa verificada de arXiv o repositorio institucional.
- `284_Tao-Teravainen_2018_Odd_Order_Logarithmically_Averaged_Chowla.pdf` — incorporado desde una copia completa verificada de arXiv o repositorio institucional.
- `285_Tao-Teravainen_2019_Structure_Logarithmically_Averaged_Correlations.pdf` — incorporado desde una copia completa verificada de arXiv o repositorio institucional.
- `286_Tao_2016_Logarithmically_Averaged_Chowla_Elliott_Two_Point.pdf` — incorporado desde una copia completa verificada de arXiv o repositorio institucional.
- `228_Mirsky_1949_Frequency_Pairs_Square_Free_Numbers_Given_Difference.pdf` — L. Mirsky, *On the frequency of pairs of square-free numbers with a given difference*, Bull. Amer. Math. Soc. 55 (1949), 936–939; DOI: 10.1090/S0002-9904-1949-09313-8.
## Incorporaciones verificadas de la lista bibliográfica — 2026-09-26

Se incorporan solo PDFs completos validados por extracción de páginas y procedentes de arXiv, editoriales o repositorios institucionales.

- `001_AbercrombieBanksShparlinski2009_2009_Arithmetic_functions_on_Beatty_sequences.pdf` — fuente: https://www.impan.pl/shop/publication/transaction/download/product/82054?download.pdf
- `002_AkianGaubertNiv2018_2018_Tropical_compound_matrix_identities.pdf` — fuente: https://arxiv.org/pdf/1702.00980
- `009_Aymone2020_2020_A_note_on_multiplicative_functions_resembling_the_M_bius_function.pdf` — fuente: https://arxiv.org/pdf/1908.11014
- `011_BaezDuarte2002_2002_BaezDuarte2002.pdf` — fuente: https://arxiv.org/pdf/math/0202141
- `019_Belton2022_2022_Mathematics_Research_Reports.pdf` — fuente: https://mrr.centre-mersenne.org/item/10.5802/mrr.12.pdf
- `022_BergelsonKulagaPrzymusLemanczykRichter2019_2019_Discrete_Contin_Dyn_Syst.pdf` — fuente: https://arxiv.org/pdf/1705.07322
- `034_Bonami1970_1970_Etude_des_coefficients_de_Fourier_des_fonctions_de_L_p_G.pdf` — fuente: https://aif.centre-mersenne.org/item/10.5802/aif.357.pdf
- `036_BorceaBranden2009_2009_Annals_of_Mathematics.pdf` — fuente: http://annals.math.princeton.edu/wp-content/uploads/annals-v170-n1-p14-p.pdf
- `040_Bourgain_undated_On_the_Fourier_Walsh_spectrum_of_the_M_obius_function.pdf` — fuente: https://arxiv.org/pdf/1112.1423
- `042_Brent2018_2019_On_asymptotic_approximations_to_the_log_Gamma_and_Riemann_Siegel_theta_functions.pdf` — fuente: https://arxiv.org/pdf/1609.03682
- `044_BretcheDressTenenbaum2020_2020_Mathematika.pdf` — fuente: https://arxiv.org/pdf/1902.09956
- `049_Burbea1974_1974_Pacific_Journal_of_Mathematics.pdf` — fuente: http://msp.org/pjm/1974/55-2/pjm-v55-n2-p04-s.pdf
- `050_Burbea1976_1976_Pacific_Journal_of_Mathematics.pdf` — fuente: http://msp.org/pjm/1976/67-1/pjm-v67-n1-p02-s.pdf
- `051_Buthe2014_2015_A_method_for_proving_the_completeness_of_a_list_of_zeros_of_certain_functions.pdf` — fuente: https://arxiv.org/pdf/1308.6704
- `055_CarrascoFlorens2000_2000_Econometric_Theory.pdf` — fuente: http://publications.ut-capitole.fr/1830/1/gmm.pdf
- `060_Chatterjee2007_2007_Stein_s_method_for_concentration_inequalities.pdf` — fuente: https://link.springer.com/content/pdf/10.1007/s00440-006-0029-y.pdf
- `064_Connes1998_1998_Connes1998.pdf` — fuente: https://arxiv.org/pdf/math/9811068
- `065_Connes2026_2026_Connes2026.pdf` — fuente: https://arxiv.org/pdf/2602.04022v1
- `072_ConreySnaith2008_2008_Communications_in_Number_Theory_and_Physics.pdf` — fuente: https://arxiv.org/pdf/0803.2795
- `073_Coons2010_2010_On_the_multiplicative_Erd_s_discrepancy_problem.pdf` — fuente: https://arxiv.org/pdf/1003.5388
- `082_deBruijn1950_1950_The_roots_of_trigonometric_integrals.pdf` — fuente: https://pure.tue.nl/ws/files/1769368/597490.pdf
- `085_DellAnnaEtAl2016_2016_Violation_of_cluster_decomposition_and_absence_of_light_cones_in_local_integer_and_half_integer_spin_chains.pdf` — fuente: https://arxiv.org/pdf/1604.08281
- `087_DerridaEnaudLebowitz2004_2004_The_asymmetric_exclusion_process_and_Brownian_excursions.pdf` — fuente: https://arxiv.org/pdf/cond-mat/0306078
- `092_DurrettIglehartMiller1977_1977_Weak_convergence_to_Brownian_meander_and_Brownian_excursion.pdf` — fuente: https://projecteuclid.org/journals/annals-of-probability/volume-5/issue-1/Weak-Convergence-to-Brownian-Meander-and-Brownian-Excursion/10.1214/aop/1176995895.pdf
- `093_DuttEtAl2019_2019_Nature_Communications.pdf` — fuente: https://www.nature.com/articles/s41467-019-11117-9.pdf
- `095_Engert1970_1970_Finite_dimensional_translation_invariant_subspaces.pdf` — fuente: http://msp.org/pjm/1970/32-2/pjm-v32-n2-p05-s.pdf
- `096_ErdosEtAl2012_2012_Spectral_statistics_of_Erd.pdf` — fuente: https://arxiv.org/pdf/1103.3869
- `098_FazziGuglielmiMarkovsky2021_2021_A_gradient_system_approach_for_Hankel_structured_low_rank_approximation.pdf` — fuente: https://arxiv.org/pdf/2002.06621v3
- `109_Frantzikinakis2020_1908_Correlations_of_multiplicative_functions_along_deterministic_and_independent_sequences.pdf` — fuente: https://arxiv.org/pdf/1908.02732
- `114_Gallier2016_2016_Spectral_theory_of_unsigned_and_signed_graphs_applications_to_graph_clustering_a_survey.pdf` — fuente: https://arxiv.org/pdf/1601.04692
- `122_GordinPeligrad2011_2011_On_the_functional_central_limit_theorem_via_martingale_approximation.pdf` — fuente: https://arxiv.org/pdf/0910.3448
- `123_Gouezel2010_2010_Almost_sure_invariance_principle_for_dynamical_systems_by_spectral_methods.pdf` — fuente: https://projecteuclid.org/journals/annals-of-probability/volume-38/issue-4/Almost-sure-invariance-principle-for-dynamical-systems-by-spectral-methods/10.1214/10-AOP525.pdf
- `124_GPY2009_2009_Annals_of_Mathematics.pdf` — fuente: http://annals.math.princeton.edu/wp-content/uploads/annals-v170-n2-p10-p.pdf
- `129_GrepstadEtAl2019_1909_On_the_asymptotic_behaviour_of_the_sine_product.pdf` — fuente: https://arxiv.org/pdf/1909.00980
- `141_HaugPrellberg2015_2015_Uniform_asymptotics_of_area_weighted_Dyck_paths.pdf` — fuente: https://arxiv.org/pdf/1412.5108
- `144_HelfgottRadziwill2021_undated_HelfgottRadziwill2021.pdf` — fuente: https://arxiv.org/pdf/2103.06853
- `145_HerichiLapidus2014_2014_Truncated_infinitesimal_shifts_spectral_operators_and_quantized_universality_of_the_Riemann_zeta_function.pdf` — fuente: https://afst.centre-mersenne.org/item/10.5802/afst.1419.pdf
- `147_HeuslerEtAl2007_2007_Periodic_orbit_theory_of_level_correlations.pdf` — fuente: https://arxiv.org/pdf/nlin/0610053
- `153_Hoffman1992_1992_Multiple_harmonic_series.pdf` — fuente: http://msp.org/pjm/1992/152-2/pjm-v152-n2-p04-s.pdf
- `156_Hurst2026_2026_Practical_computations_of_the_Mertens_function_M_10.pdf` — fuente: https://arxiv.org/pdf/2607.07566
- `178_KaczorowskiLanguascoPerelli2000_2000_A_note_on_Landau_s_formula.pdf` — fuente: https://projecteuclid.org/journals/functiones-et-approximatio-commentarii-mathematici/volume-28/issue-none/A-note-on-Landaus-formula/10.7169/facm/1538186693.pdf
- `179_Kaigh1976_1976_An_invariance_principle_for_random_walk_conditioned_by_a_late_return_to_zero.pdf` — fuente: https://projecteuclid.org/journals/annals-of-probability/volume-4/issue-1/An-Invariance-Principle-for-Random-Walk-Conditioned-by-a-Late/10.1214/aop/1176996189.pdf
- `186_KhorunzhiyMarckert2009_2009_Uniform_bounds_for_exponential_moment_of_maximum_of_a_Dyck_path.pdf` — fuente: https://arxiv.org/pdf/0902.1229
- `194_Kousha2012_2012_Asymptotic_behavior_and_the_moderate_deviation_principle_for_the_maximum_of_a_Dyck_path.pdf` — fuente: https://arxiv.org/pdf/1008.0606
- `201_Lagarias2007_2007_Li_coefficients_for_automorphic_functions.pdf` — fuente: https://aif.centre-mersenne.org/item/10.5802/aif.2311.pdf
- `206_LeeLeong2024_2024_New_explicit_bounds_for_the_Mertens_function_and_the_reciprocal_of_the_Riemann_zeta_function.pdf` — fuente: https://arxiv.org/pdf/2208.06141
- `213_Liu2022_2022_Multiplicative_functions_resembling_the_M_bius_function.pdf` — fuente: https://arxiv.org/pdf/2205.00972
- `214_LiYang2023_2023_An_improvement_on_Gauss_s_circle_problem_and_Dirichlet_s_divisor_problem.pdf` — fuente: https://arxiv.org/pdf/2308.14859
- `216_LyubarskiiVershynin2010_2010_Uncertainty_principles_and_vector_quantization.pdf` — fuente: https://arxiv.org/pdf/math/0611343
- `217_Matiyasevich2007a_1983_Hidden_Life_of_Riemann_s_Zeta_Function_1_Arrow_Bow_and_Targets.pdf` — fuente: https://arxiv.org/pdf/0707.1983
- `218_Matiyasevich2007b_2007_Hidden_Life_of_Riemann_s_Zeta_Function_2_Electrons_and_Trains.pdf` — fuente: https://arxiv.org/pdf/0709.0028
- `227_MelottiSaias2020_2020_On_path_partitions_of_the_divisor_graph.pdf` — fuente: https://arxiv.org/pdf/1807.07783
- `232_MontgomerySoundararajan2004_2004_Comm_Math_Phys.pdf` — fuente: https://arxiv.org/pdf/math/0409258
- `233_MossinghoffOliveiraTrudgian2021_2021_The_distribution_of_k_free_numbers.pdf` — fuente: https://arxiv.org/pdf/1912.04972
- `235_Muellner2017_2017_Automatic_sequences_fulfill_the_Sarnak_conjecture.pdf` — fuente: https://arxiv.org/pdf/1602.03042
- `236_MullerEtAl2005_2005_Periodic_orbit_theory_of_universality_in_quantum_chaos.pdf` — fuente: https://arxiv.org/pdf/nlin/0503052
- `238_MussardoLeClair2021_2021_Randomness_of_M_obius_coefficients_and_Brownian_motion_growth_of_the_Mertens_function_and_the_Riemann_hypothes.pdf` — fuente: https://arxiv.org/pdf/2101.10336
- `240_Ng2004_2004_Proc_London_Math_Soc.pdf` — fuente: https://arxiv.org/pdf/math/0310381
- `244_Nunes2015_2015_Journal_of_Number_Theory.pdf` — fuente: https://arxiv.org/pdf/1402.0684
- `247_OganesyanHuse2007_2007_Localization_of_interacting_fermions_at_high_temperature.pdf` — fuente: https://arxiv.org/pdf/cond-mat/0610854
- `249_OwczarekPrellberg2014_2014_Pressure_exerted_by_a_vesicle_on_a_surface.pdf` — fuente: https://arxiv.org/pdf/1311.2174
- `252_PeligradUtev2005_2005_A_new_maximal_inequality_and_invariance_principle_for_stationary_sequences.pdf` — fuente: https://arxiv.org/pdf/math/0406606
- `255_PillaiYin2014_2014_Universality_of_covariance_matrices.pdf` — fuente: https://arxiv.org/pdf/1110.2501
- `265_RigalZadunaisky2015_2015_Twisted_semigroup_algebras.pdf` — fuente: https://arxiv.org/pdf/1406.2985
- `266_RodgersTao2018_2018_RodgersTao2018.pdf` — fuente: https://arxiv.org/pdf/1801.05914v5
- `281_StampachStovicek2020_2020_On_Hankel_matrices_commuting_with_Jacobi_matrices_from_the_Askey_scheme.pdf` — fuente: https://arxiv.org/pdf/1911.07059
- `282_Suzuki2025Hilbert_2025_On_the_Hilbert_space_derived_from_the_Weil_distribution.pdf` — fuente: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/FD33EBD117A6B448053450DD8D62ADB6/S0008414X25101739a.pdf/div-class-title-on-the-hilbert-space-derived-from-the-weil-distribution-div.pdf
- `283_Szekelyhidi1982_1982_Note_on_exponential_polynomials.pdf` — fuente: http://msp.org/pjm/1982/103-2/pjm-v103-n2-p26-s.pdf
## Incorporaciones verificadas adicionales — 2026-09-26

- Benvenuti (2019), *The inverse eigenvalue problem for Leslie matrices*, Electronic Journal of Linear Algebra 35, 319–330.
- Herrera-Poyatos–Moree (2018), *Coefficients and higher order derivatives of cyclotomic polynomials: old and new*, MPIM Preprint 2018 (46).

---

## Huecos conocidos (citados en el trabajo, ausentes de la carpeta)

Comprobado el 2026-08-19. Al citarlos hay que decir que no están aquí.

- **Rudnick & Sarnak**, *Zeros of principal L-functions and random matrix theory*, Duke Math. J. **81** (1996), 269–322. Base del salto de estadística 2-level a n-level.
- **Forrester & Odlyzko**, *Gaussian unitary ensemble eigenvalues and Riemann zeta function zeros: a nonlinear equation for a new statistic*, Phys. Rev. E **54** (1996), R4493. Tratamiento Fredholm/Painlevé de nearest-neighbour; evita usar el Wigner surmise como exacto.
- **Kargin**, *Statistical properties of zeta functions' zeros*, Probability Surveys **11** (2014), 121–160, arXiv:1302.1452. El survey (distinto del 069, ver §4).

---

## 1. Núcleo RVM: sumas sobre ordenadas, fases y partes fraccionarias

- `004_Aryan_2019_Extension_Landau_Gonek_Formula.pdf` — extensión de la fórmula de Landau–Gonek; recupera sin RH consecuencias de pair correlation. arXiv:1902.05473
- `041_Brent-Platt-Trudgian_2020_Sums_Over_Zeros_Riemann_Zeta.pdf` — estimación explícita de sumas sobre ceros.
- `062_Coffey_2009_Certain_Sums_Over_Nontrivial_Zeta_Zeros.pdf` — coeficientes b_n como sumas sobre ceros y sobre las λ_j de Li/Keiper. arXiv:0912.2390
- `091_Durkan-Hughes-PearceCrump_2026_Generalisations_Landau_Gonek_Theorem.pdf` — sumas Σ_ρ χ(ρ)X^ρ; sensibilidad a la naturaleza aritmética de X. arXiv:2601.18025
- `165_Ivic_2001_Sums_Over_Ordinates_Zeta_Zeros.pdf` — G(s) = Σ_{γ>0} γ^{-s}; evaluación de sumas sobre γ e integrales de S(T). **Referencia base.**
- `237_Murahara-Onozuka_2025_Equidistribution_A_Points_Zeta_Derivatives.pdf` — sumas exponenciales sobre a-puntos de derivadas de ζ, siguiendo a Fujii. arXiv:2510.07710
- `264_Riemann_1859_Number_Of_Primes_Below_A_Given_Magnitude.pdf` **(mal etiquetado, ver avisos)** — sumas parciales S(N)=Σ e^{iγ_n}, banda estrecha de |S(N)|, picos y espaciados multimodales. Directamente sobre tu problema.
- `299_Youvan_2024_Phase_Winding_Riemann_Zeta.pdf` — dinámica de bobinado de fase de ζ, heatmaps y estadística. Sin arbitraje.
- `099_Ford-Meng-Zaharescu_2017_Simultaneous_Fractional_Parts.pdf` — distribución simultánea de {α_1γ,…,α_nγ}. arXiv:1511.06814
- `100_Ford-Soundararajan-Zaharescu_2009_Imaginary_Parts_II.pdf` — partes fraccionarias de αγ, continuación. arXiv:0805.2745
- `101_Ford-Zaharescu_2005_Imaginary_Parts_Zeta_Zeros.pdf` — partes fraccionarias de αγ, primer trabajo de la serie.
- `270_Saffari-Vaughan_1977_Fractional_Parts_X_Over_N_II.pdf` — partes fraccionarias de x/n y sucesiones relacionadas.

## 2. Pair correlation de Montgomery

- `231_Montgomery_1973_Pair_Correlation_Zeros_Zeta.pdf` — **el original**. F(α), 2/3 de ceros simples bajo RH.
- `015_Baluyot-Goldston-etal_2025_Pair_Correlation_Zeros_I_Proportions_Simple_Critical.pdf` — proporciones de ceros simples y en la crítica. arXiv:2501.14545
- `053_Carneiro-Chandee-Littmann-Milinovich_2014_Hilbert_Spaces_Pair_Correlation.pdf` — N(T,β) vía espacios de Hilbert de funciones enteras. arXiv:1406.5462
- `054_Carneiro-Milinovich-Ramos_2023_Fourier_Optimization_Montgomery_Pair_Correlation.pdf` — cotas del promedio de F(α,T) por optimización de Fourier. arXiv:2310.01913
- `058_Chan_2002_More_Precise_Pair_Correlation_Zeros_Primes_Short_Intervals.pdf` — segundos términos principales en la equivalencia Goldston–Montgomery.
- `067_Conrey-Keating_2016_Pair_Correlation_Twin_Primes_Revisited.pdf` — conexión ratios-conjecture / correlaciones aritméticas. arXiv:1604.06124
- `028_Bogomolny-Keating_1995_Random_Matrix_Theory_Riemann_Zeros_I_Three_Four_Point_Correlations.pdf` — correlaciones de 3 y 4 puntos de los ceros = GUE desde Hardy–Littlewood. doi:10.1088/0951-7715/8/6/013
- `029_Bogomolny-Keating_1996_Gutzwiller_Trace_Formula_Spectral_Statistics_Beyond_Diagonal.pdf` — correlación de dos puntos más allá de la aproximación diagonal; para ζ equivale a Hardy–Littlewood para pares de primos. doi:10.1103/PhysRevLett.77.1472
- `030_Bogomolny-Keating_1996_Random_Matrix_Theory_Riemann_Zeros_II_n_Point_Correlations.pdf` — correlaciones de n puntos = GUE para todo n, desde Hardy–Littlewood. doi:10.1088/0951-7715/9/4/006
- `079_Das-Ismoilov-Ramos_2025_Fourier_Optimization_Pair_Correlation_Problems.pdf` — marco genérico de cotas de pair correlation. arXiv:2502.05106
- `118_Goldston-Lee-Schettler-Suriajaya_2025_Pair_Correlation_Conjecture_II_Alternative_Hypothesis.pdf` — PCC bajo hipótesis alternativa. arXiv:2507.06823
- `117_Goldston-Lee-Schettler-Suriajaya_2025_Pair_Correlation_Conjecture_I_Simple_Critical.pdf` — PCC sin RH y ceros simples. arXiv:2503.15449
- `189_Kolountzakis-Revesz_2003_Turan_Extremal_Problem.pdf` — problema extremal de Turán; herramienta de optimización de Fourier.

## 3. Gaps entre ceros y arg ζ

- `111_Fujii_1974_Zeros_Dirichlet_L_Functions_I.pdf` — momentos de S(t+h)−S(t) (y de L(s,χ)) en intervalos cortos, con prueba; incondicional. Trans. AMS 196 (1974), DOI 10.1090/S0002-9947-1974-0349603-2
- `113_Fujii_1975_Distribution_Zeros_Zeta_Short_Intervals.pdf` — momentos de S(t+h)−S(t) en intervalos cortos (anuncio, sin pruebas). Bull. AMS 81 (1975), DOI 10.1090/S0002-9904-1975-13674-3
- `155_Hughes-Rudnick_2002_Linear_Statistics_Zeros_Zeta.pdf` — estadísticos lineales de ceros escalados; momentos gaussianos. arXiv:math/0208220
- `112_Fujii_1975_Difference_r_Consecutive_Ordinates_Zeros_Zeta.pdf` — momentos incondicionales de diferencias de r ordenadas consecutivas, muestreados en los ceros; conteo de r-gaps pequeños. Proc. Japan Acad. 51 (1975), DOI 10.3792/pja/1195518466
- `068_Conrey-TurnageButterbaugh_2018_r_Gaps_Between_Zeros_Zeta.pdf` — r-gaps, constantes explícitas bajo RH. arXiv:1708.00030
- `119_Gonek-Sahay_2024_Consecutive_Moderate_Gaps_Between_Zeros_Zeta.pdf` — gaps consecutivos moderados. arXiv:2412.15481
- `162_Inoue-Kobayashi-Toma_2026_Explicit_Extreme_Values_Argument_Zeta.pdf` — valores extremos explícitos de arg ζ; mejora Conrey–Turnage-Butterbaugh. arXiv:2510.14309
- `163_Inoue_2024_Note_On_r_Gaps_Between_Zeros_Zeta.pdf` — prueba del resultado anunciado por Selberg sobre r-gaps. arXiv:2303.06613
- `302_Zhao_2026_Density_Results_r_Gaps_Between_Zeros_Zeta.pdf` — resultados de densidad para r-gaps. arXiv:2603.17334
- `191_Korolev_2012_Gram_Law_Argument_Riemann_Zeta_Publ_Inst_Math.pdf` — ley de Gram y S(t) en los puntos de Gram; fórmulas de Selberg para momentos de Δ_n en intervalos cortos (Teorema 4.2). Publ. Inst. Math. 92(106) (2012), DOI 10.2298/PIM1206053K
- `192_Korolev_2012_Gram_Law_Riemann_Zeta.pdf` — ley de Gram, fórmulas de Selberg. arXiv:1011.3997
- `168_Jerby_2023_New_Discriminant_Hardy_Z_Function_Corrected_Gram_Law.pdf` — discriminante Δ_n(a) de Z(t), ley de Gram corregida. arXiv:2310.14415
- `290_Trudgian_2008_Gram_Law_Fails_Positive_Proportion_Of_The_Time.pdf` — proporción positiva de fallos de la ley de Gram y de éxitos débiles. arXiv:0811.0883
- `105_Franca-LeClair_2014_Statistical_Properties_Riemann_Zeros_Explicit_Equation_nth_Zero.pdf` — ecuación para el n-ésimo cero con Lambert W (ỹ_n, sin puntos de Gram ni ley de Gram) y término arg ζ; reconstruye π(x) con ceros sintéticos. arXiv:1307.8395
- `106_Franca-LeClair_2014_Theory_Zeros_Riemann_Zeta_And_Other_L_Functions.pdf` — notas de curso: ceros de la línea crítica ↔ ceros del coseno, ecuación del n-ésimo cero, L-funciones. arXiv:1407.4358
- `108_Franca-LeClair_2015_Transcendental_Equations_Individual_Zeros_L_Functions_CNTP_Published.pdf` — versión publicada de la ecuación trascendente del n-ésimo cero (CNTP 9 (2015) 1–50); el preprint es `102_…`.
- `205_LeClair_2016_Riemann_Hypothesis_Random_Walks_Zeta_Case.pdf` — producto de Euler truncado en N(t)<[t²], B_N(t)=O(√N) vía Kac, argumento heurístico de S(t)=O(1), modelo probabilístico de ceros y cero 10^100. arXiv:1601.00914

## 4. RMT, GUE/CUE y estadística de espaciados

- `024_Berry_1988_Semiclassical_Formula_Number_Variance_Riemann_Zeros.pdf` — varianza del número de ceros desde los primos: régimen universal GUE y régimen no universal por primos, separados por la escala τ*. doi:10.1088/0951-7715/1/3/001
- `246_Odlyzko_1987_Distribution_Spacings_Between_Zeros_Zeta.pdf` — **datos base**: 10^5 ceros y ceros 10^12+1…10^12+10^5, precisión 10^-8.
- `104_Forrester-Mays_2015_Finite_Size_Corrections_RMT_Odlyzko_Data.pdf` — correcciones de tamaño finito contra el dataset de Odlyzko. arXiv:1506.06531
- `037_Bornemann-Forrester-Mays_2017_Finite_Size_Effects_Spacing_Distributions.pdf` — efectos de tamaño finito en distribuciones de espaciado. arXiv:1608.04638
- `241_Nishigaki_2024_Consecutive_Level_Spacings_GUE_Ratio.pdf` — espaciados consecutivos GUE y su ratio, derivación ab initio. doi:10.1093/ptep/ptae120
- `242_Nishigaki_2025_Consecutive_Level_Spacings_CUE_Finite_Size_Zeta.pdf` — lo mismo para CUE, con correcciones finitas y ceros de ζ.
- `276_Shir-MartinezAzcona-Chenu_2025_Surmise_Level_Spacing_Beyond_Nearest.pdf` — surmise más allá del vecino inmediato. arXiv:2504.20134
- `031_Bohigas-Leboeuf-Sanchez_2001_Spectral_Spacing_Correlations.pdf` — autocovarianzas de espaciados como función de correlación discretizada.
- `103_Forrester-Lebowitz_2013_Local_CLT_Determinantal_Point_Processes.pdf` — TCL local para procesos determinantales. arXiv:1311.7126
- `169_Johansson_2001_Discrete_Orthogonal_Polynomial_Ensembles_Plancherel.pdf` — ensembles discretos de polinomios ortogonales.
- `184_Kargin_2013_Fluctuations_Riemann_Zeta_Zeros.pdf` — *On fluctuations of Riemann's zeta zeros*, arXiv:1203.5309, 25 pág. Fluctuaciones gaussianas de γ_k en torno a su posición predicha; ley conjunta de γ_k y γ_{k+x} con correlación (1-β)₊. **No confundir** con Kargin, *Statistical properties of zeta functions' zeros*, Probability Surveys 11 (2014), arXiv:1302.1452 — ese es el survey (soporte de Fourier en Montgomery, escalas, qué es local), y **no está en la biblioteca**.
- `097_Fazzari-Gerspach-Minelli_2025_Selberg_CLT_Weighted_Linear_Statistics_Zeta_Zeros.pdf` — TCL de Selberg ponderado por estadística local de ceros. arXiv:2507.04150
- `056_Cartier-Julia-Moussa-Vanhove_2006_Random_Matrices_Zeta_Dynamical_Systems.pdf` — actas *Frontiers in Number Theory, Physics and Geometry I*.
- `038_Borwein-Straub-Wan-Zudilin_2012_Densities_Short_Uniform_Random_Walks.pdf` — densidades de paseos aleatorios uniformes cortos (3–5 pasos); referencia para caminatas de fase. arXiv:1103.2995

## 5. Criterio de Li–Weil y positividad

- `061_Coffey_2005_Polygamma_Theory_Li_Keiper_Constants_Riemann_Hypothesis.pdf` — constantes λ_k y c_n, teoría poligamma.
- `273_Sekatskii_2013_Generalized_Bombieri_Lagarias_Li_Criterion.pdf` — teorema de Bombieri–Lagarias generalizado y criterio de Li generalizado.
- `274_Sekatskii_2014_Generalized_Li_Criterion_Zeroes_Location.pdf` — primeras aplicaciones a la localización de ceros. arXiv:1304.7895
- (ver también `019_Coffey_2009` en §1)

## 6. Matrices aritméticas: Redheffer, Toeplitz multiplicativas, GCD, Hilbert

- `017_Barrett-Jarvis_1992_Spectral_Properties_Redheffer_Matrix.pdf` — det A_n = M(n); propiedades espectrales.
- `292_Vaughan_1996_Eigenvalues_Redheffer_Matrix_II.pdf` — estimaciones precisas de autovalores. doi:10.1017/S1446788700037654
- `297_Wilf_2004_Redheffer_Matrix_Partially_Ordered_Set.pdf` — permutaciones que contribuyen al determinante; permanente.
- `267_Roesler_1986_Riemann_Hypothesis_Eigenvalue_Problem.pdf` — RH como problema de autovalores de una matriz entera.
- `268_Roesler_1987_Riemann_Hypothesis_Eigenvalue_Problem_II.pdf` — continuación; distribución de autovalores.
- `150_Hilberdink_2006_Determinants_Multiplicative_Toeplitz_Matrices.pdf` — a_ij = f(i/j) con f multiplicativa; determinantes truncados.
- `151_Hilberdink_2015_Multiplicative_Toeplitz_Matrices_Riemann_Zeta.pdf` — conexión directa con ζ.
- `152_Hilberdink_2017_Singular_Values_Multiplicative_Toeplitz_Matrices.pdf` — valores singulares. doi:10.1080/03081087.2016.1204978
- `149_Hilberdink-Pushnitski_2023_Spectral_Asymptotics_LCM_Matrices.pdf` — asintótica espectral de matrices n^σ m^σ / [n,m]^τ. arXiv:2110.14323
- `211_Lindqvist-Seip_1998_Note_Greatest_Common_Divisor_Matrices.pdf` — formas cuadráticas de matrices GCD como normas L².
- `045_Brevig-Perfekt-Seip-Siskakis-Vukotic_2016_Multiplicative_Hilbert_Matrix.pdf` — la matriz de Hilbert multiplicativa. arXiv:1411.7294
- `254_Perfekt-Pushnitski_2018_Spectrum_Multiplicative_Hilbert_Matrix.pdf` — su espectro. arXiv:1705.01959
- `245_Odlyzko-TeRiele_1985_Disproof_Mertens_Conjecture.pdf` — refutación de la conjetura de Mertens.
- `182_Kannan-Bachem_1979_Polynomial_Algorithms_Smith_Hermite_Normal_Forms.pdf` — algoritmos polinómicos para formas normales.
- `200_Labahn-Neiger-Zhou_2018_Hermite_Normal_Form_Polynomial_Matrix.pdf` — forma normal de Hermite para matrices polinómicas. arXiv:1607.04176
- `269_Rota_1964_Foundations_Combinatorial_Theory_Mobius_Functions.pdf` — funciones de Möbius sobre posets.

## 7. Sumas exponenciales y métodos de Van der Corput / Vinogradov

- `125_Graham-Kolesnik_1991_Computing_Optimal_Exponent_Pairs.pdf` — cálculo de pares de exponentes óptimos (cap. 5).
- `126_Graham-Kolesnik_1991_Simplest_Van_Der_Corput_Estimates.pdf` — estimaciones vdC de primera y segunda derivada (cap. 2).
- `039_Bourgain_2017_Decoupling_Exponential_Sums_Riemann_Zeta.pdf` — desacoplamiento; ζ(1/2+it) ≪ t^{13/84+ε}; par de exponentes (13/84, 55/84). arXiv:1408.5794v2, J. Amer. Math. Soc. 30 (2017)
- `187_Kinnunen_1997_Hardy_Littlewood_Maximal_Function_Sobolev_Function.pdf` — análisis armónico auxiliar: maximal de Hardy–Littlewood acotado en W^{1,p}, |D Mu| ≤ M Du. Israel J. Math. 100 (1997)
- `159_Huxley_1989_Exponential_Sums_Riemann_Zeta.pdf` — método de Bombieri–Iwaniec, trabajo Huxley–Watt en contexto.
- `183_Karatsuba-Voronin_1992_Vinogradov_Method_Riemann_Zeta.pdf` — método de Vinogradov, teorema del valor medio (cap. IV).
- `016_Baricz-Laforgia-Pogany_2015_Van_Der_Corput_Inequalities_Bessel.pdf` — desigualdades vdC para funciones de Bessel. doi:10.1080/10652469.2014.975419
- `185_Kelly-Le_2018_Van_Der_Corput_Sets_Compact_Groups.pdf` — conjuntos vdC en grupos compactos. doi:10.1007/s00013-017-1136-y
- `196_Kowalski_2021_Exponential_Sums_Finite_Fields_Elementary.pdf` — métodos elementales, curso ETH.
- `197_Kowalski_2021_Exponential_Sums_Finite_Fields_II.pdf` — métodos cohomológicos.
- `173_Jun-Lee_2014_Dedekind_And_Exponential_Sums.pdf` — equidistribución de sumas de Dedekind generalizadas. doi:10.1016/j.jnt.2013.10.020
- `243_Norvidas_2011_Entire_Functions_Exponential_Sums.pdf` — espacios de Bernstein y sumas exponenciales.

## 8. Funciones multiplicativas: Liouville, Möbius, Chowla

- `222_Matomaki-Radziwill_2016_Multiplicative_Functions_Short_Intervals.pdf` — **el teorema MR**: promedios cortos vs. largos. doi:10.4007/annals.2016.183.3.6
- `220_Matomaki-Radziwill_2015_Liouville_Short_Intervals.pdf` — prueba corta y autocontenida para λ(n). arXiv:1502.02374
- `219_Matomaki-Radziwill-Tao_2015_Averaged_Chowla_Conjecture.pdf` — Chowla promediada. arXiv:1503.05121
- `137_Harman-Pintz-Wolke_1985_Mobius_And_Liouville_Functions.pdf` — nota sobre valores de μ y λ.
- `057_Cassaigne-Ferenczi-Mauduit-Rivat-Sarkozy_1999_Liouville_Pseudorandom_Sequences.pdf` — λ como sucesión binaria pseudoaleatoria.
- `076_Croot_2003_Oscillations_Multiplicative_PlusMinusOne.pdf` — oscilaciones de funciones multiplicativas ±1. [texto extraído ilegible]
- `127_Granville-Soundararajan_2003_Decay_Of_Mean_Values.pdf` — decaimiento de valores medios. [texto extraído ilegible]
- `271_Sawin_2022_Mobius_Cancellation_Polynomial_Sequences.pdf` — cancelación de Möbius en F_q[u], análogo de Chowla. doi:10.1007/s00222-022-01115-y
- `090_Drmota_2009_Sum_Of_Digits_Of_Primes.pdf` — suma de dígitos de los primos (charla, con Mauduit y Rivat).

## 9. Números smooth e intervalos cortos

- `128_Granville_2008_Smooth_Numbers_Survey.pdf` — survey de referencia (MSRI).
- `014_Balog_1987_Integers_Without_Large_Prime_Factors.pdf` — Astérisque 147-148, pp. 27-31.
- `110_Friedlander-Granville_1993_Smoothing_Smooth_Numbers.pdf` — [texto extraído ilegible]
- `077_Croot_2007_Smooth_Numbers_Short_Intervals.pdf` — exponente 3/(14√e)+ε.
- `225_Matomaki_2010_Smooth_Numbers_Short_Intervals.pdf` — exponente 1/(5√e)+ε en [x, x+C√x].
- `226_Matomaki_2016_Smooth_Numbers_Short_Intervals_II.pdf` — intervalo √x(log x)^{7/3+δ}.
- `280_Soundararajan_2010_Smooth_Numbers_Short_Intervals.pdf` — bajo RH, x^ε-smooth en [x, x+C(ε)√x]. arXiv:1009.1591

## 10. Formas modulares, L-funciones y momentos

- `138_Harper_2013_Conditional_Bounds_Zeta_Moments.pdf` — bajo RH, momentos 2k-ésimos ≪ T log^{k²}T. arXiv:1305.4618
- `174_Jutila_1977_Zero_Density_Estimates_L_Functions.pdf` — M. Jutila, *Zero-density estimates for L-functions*, Acta Arithmetica **XXXII** (1977), pp. 55–62; completo, en 5 hojas a doble página. Método de Halász–Montgomery para mejorar Ingham en σ > 3/4; el corolario da N(α,q,χ) con A(α)=2 para α ≥ 21/26 = 0.8076…, 7/9 y 11/14 = 0.7857… según k.
- `260_Radziwill-Soundararajan_2015_Quadratic_Twists_Central_L_Values.pdf` — momentos y distribución de valores centrales. arXiv:1403.7067
- `115_Ghosh-Sarnak_2012_Real_Zeros_Hecke_Cusp_Forms.pdf` — ceros reales de formas cuspidales de Hecke. arXiv:1103.3262
- `207_Lester-Matomaki-Radziwill_2015_Small_Scale_Zeros_Modular_Forms.pdf` — ceros y masa a escala pequeña. arXiv:1501.01292
- `221_Matomaki-Radziwill_2015_Sign_Changes_Hecke_Eigenvalues.pdf` — cambios de signo de λ_f(n). arXiv:1405.7671
- `204_Lau-Liu-Wu_2010_Symmetric_Square_L_Function_Coefficients.pdf` — resultados Ω± para el cuadrado simétrico.
- `195_Kowalski-Robert-Wu_2007_Small_Gaps_And_B_Free_Numbers.pdf` — no existencia de gaps en series de formas modulares.

## 11. Determinantes de Hankel y valores de ζ

- `142_Haynes-Zudilin_2015_Hankel_Determinants_Zeta_Values.pdf` — asintótica de Hankel con ζ(an+b); aplicación diofántica. arXiv:1510.01901
- `229_Monien_2009_Hankel_Determinants_Dirichlet_Series.pdf` — determinantes de Hankel de series de Dirichlet. arXiv:0901.1883

## 12. Verificación numérica y cálculo

- `257_Platt-Trudgian_2021_RH_True_Up_To_3e12.pdf` — RH verificada rigurosamente (aritmética de intervalos) hasta altura 3·10^12. arXiv:2004.09765
- `277_Sidi_2003_Riemann_And_Generalized_Zeta_Extrapolation.pdf` — extrapolación numérica de ζ (apéndice E).
- (ver también `097_Odlyzko_1987` en §4 y `096_Odlyzko-TeRiele_1985` en §6)

## 13. Tratados, monografías y panorámicas

- `263_Riemann-Wilkins_1859_Prime_Counting_English_Translation.pdf` — **el texto de Riemann**, en alemán (original de 1859 transcrito por D. R. Wilkins, 10 páginas; no es una traducción al inglés pese al nombre del fichero). La inversión de Möbius para π y la serie Li(x) − ½Li(x^{1/2}) − ⅓Li(x^{1/3}) − ⅕Li(x^{1/5}) + ⅙Li(x^{1/6}) − … están en las págs. 8–9.
- `289_Titchmarsh-HeathBrown_1986_Theory_Riemann_Zeta_Function.pdf` — el tratado estándar. 2ª edición revisada por D. R. Heath-Brown, Clarendon Press. 418 hojas que llegan hasta la página impresa 412; las *Further references* de Heath-Brown terminan en Weil, así que el escaneo está completo.
- `164_Ivic_1985_Riemann_Zeta_Theory_Applications.pdf` — Wiley 1985, edición original. 538 pág. escaneadas; **con capa OCR desde 2026-08-19**, ya es grepeable. Completo (el índice de materias llega hasta las entradas en Z). No incluye erratas: usar `ERRATA_Ivic.md`.
- `166_Ivic_2003_Riemann_Zeta_Dover_Reprint.pdf` — **mismo libro que el 058**. Dover 2003, *unabridged republication* de Wiley 1985: cuerpo y paginación idénticos, no es una edición revisada. Lo único que añade es la lista de erratas en pág. xvii–xix (PDF 15–17), transcrita en `ERRATA_Ivic.md`. Completo; con capa OCR desde 2026-08-19.
- `094_Edwards_1974_Riemanns_Zeta_Function.pdf` — **ESCANEO INCOMPLETO**. Reimpresión Dover 2001 del original de Academic Press 1974. El PDF tiene 135 hojas que cubren las páginas impresas **1–122 de 311** (desfase: hoja PDF ≈ página impresa + 13).
  - **Sí está**: cap. 1 el paper de Riemann (p. 1), cap. 2 fórmula del producto para ξ (39), cap. 3 fórmula principal de Riemann (48), cap. 4 teorema de los números primos (68), cap. 5 De la Vallée Poussin (88), cap. 6 análisis numérico de las raíces por Euler–Maclaurin (96) — hasta ~p. 122.
  - **No está**: cap. 7 fórmula de Riemann–Siegel (136), cap. 8 cálculos a gran escala / Turing / fenómeno de Lehmer (171), cap. 9 crecimiento de zeta y Lindelöf (182), cap. 10 análisis de Fourier (203), cap. 11 ceros en la línea / teorema de Hardy (226), cap. 12 miscelánea (260), apéndice con el paper de Riemann (299), referencias (306) e índice (311).
  - Consecuencia práctica: para Riemann–Siegel, Turing o Hardy **no sirve este fichero**; usar `118_Titchmarsh` o `058/060_Ivic`.
- `250_Patterson_1988_Introduction_Riemann_Zeta_Function.pdf` — S. J. Patterson, *An Introduction to the Theory of the Riemann Zeta-Function*, Cambridge Studies in Advanced Mathematics **14**. 172 hojas, completo (bibliografía p. 153, índice p. 156).
- `251_Patterson_1988_Zeros_Zeta_And_Prime_Number_Theorem.pdf` — cap. 4, ceros y TNP. doi:10.1017/CBO9780511623707.006
- `234_Motohashi_1997_Spectral_Theory_Riemann_Zeta.pdf` — teoría espectral, Cambridge Tracts 127.
- `287_Tenenbaum_2015_Analytic_Probabilistic_Number_Theory.pdf` — GSM 163, 3ª edición.
- `261_Ramachandra_1976_Problems_Analytic_Number_Theory.pdf` — K. Ramachandra, *Some problems of analytic number theory*, Acta Arithmetica **XXXI** (1976), pp. 313–324; completo, en 7 hojas a doble página. Dedicado a la memoria de Turán. Primos en intervalos cortos, resultado de Selberg para N₀(x), método de Heilbronn y aproximación diofántica simultánea.
- `033_Bombieri_2010_Classical_Theory_Zeta_And_L_Functions.pdf` — panorámica histórica. doi:10.1007/s00032-010-0121-8
- `071_Conrey_2003_Riemann_Hypothesis.pdf` — el survey del Notices.
- `069_Conrey_1986_Review_Ivic_Riemann_Zeta_Function.pdf` — reseña de una página (American Scientist).
- `136_Hardy-Littlewood_1917_Riemann_Zeta_And_Distribution_Primes.pdf` — memoria original de Acta Mathematica.

## 14. Otras funciones zeta y contextos adyacentes

- `006_Avdonin-Ivanov_2001_Exponential_Riesz_Bases_Subspaces_Divided_Differences.pdf` — bases de Riesz de exponenciales y de diferencias divididas; criterio de Pavlov vía Helson–Szegő/A₂. arXiv:math/0103160
- `215_Lyubarskii-Seip_1997_Complete_Interpolating_Sequences_Paley_Wiener_Muckenhoupt_Ap.pdf` — sucesiones de interpolación completa en Paley–Wiener y condición A_p; Kadec 1/4 como corolario. Rev. Mat. Iberoam. 13 (1997), DOI 10.4171/RMI/224
- `160_Igusa_2000_Introduction_Local_Zeta_Functions.pdf` — zetas locales.
- `190_Komori-Matsumoto-Tsumura_2023_Zeta_Functions_Root_Systems.pdf` — zetas de sistemas de raíces.
- `210_Li_2019_Zeta_L_Functions_Number_Theory_Combinatorics.pdf` — CBMS 129. doi:10.1090/cbms/129
- `301_Zhao_2016_Multiple_Zeta_Polylogarithms_Special_Values.pdf` — zetas múltiples y polilogaritmos.
- `203_Lapidus-VanFrankenhuysen_2000_Fractal_Geometry_Number_Theory.pdf` — dimensiones complejas de cuerdas fractales.
- `180_Kanemitsu-Tsukada_2015_Hecke_Type_Zeta_Functions.pdf` — cap. 8 de *Contributions to the Theory of Zeta-Functions*.
- `181_Kanemitsu-Tsukada_2015_Modular_Relation_Supremacy.pdf` — *Contributions to the Theory of Zeta-Functions: The Modular Relation Supremacy*, World Scientific, Series on Number Theory and Its Applications vol. 9. 316 hojas, completo (índice hasta p. 303). Fórmulas de Voronoĭ, funciones de Bessel generalizadas de Wilton, transformación theta.
- `027_Bloch_2000_Higher_Regulators_K_Theory_Zeta_Elliptic_Curves.pdf` — S. Bloch, monografía AMS (vol. 11 de la serie), 110 pág., completo. Reguladores superiores, K-teoría algebraica y funciones zeta de curvas elípticas.
- `259_Popov_1985_Transfer_Functions_Riemann_Zeta.pdf` — sistemas con funciones de transferencia ligadas a ζ.
- `172_Jones-Sato-Wada-Wiens_1976_Diophantine_Representation_Primes.pdf` — el polinomio de 26 variables (Monthly).

## 15. Material no arbitrado — contrastar antes de usar

- `078_Dannon_2008_Riemann_Zeta_Function.pdf` — Gauge Institute Journal.
- `293_Vega_2023_Simple_Proof_Riemann_Hypothesis.pdf` — vía función Ψ de Dedekind. doi:10.33774/coe-2023-5flmk
- `299_Youvan_2024_Phase_Winding_Riemann_Zeta.pdf` — ver §1.

## Catálogo completo actual — 2026-10-18 (302 PDF)

- `001_AbercrombieBanksShparlinski2009_2009_Arithmetic_functions_on_Beatty_sequences.pdf`
- `002_AkianGaubertNiv2018_2018_Tropical_compound_matrix_identities.pdf`
- `003_AriasdeReyna_2024_Explicit_Formula_Quasicrystal_Definition.pdf`
- `004_Aryan_2019_Extension_Landau_Gonek_Formula.pdf`
- `005_Aryan_2022_Extension_Landau_Gonek_Formula_Published.pdf`
- `006_Avdonin-Ivanov_2001_Exponential_Riesz_Bases_Subspaces_Divided_Differences.pdf`
- `007_Avdonin_1977_Riesz_Bases_Exponential_Functions_L2_Brief.pdf`
- `008_Aymone-Sidoravicius_2017_Partial_Sums_Biased_Random_Multiplicative_Functions.pdf`
- `009_Aymone2020_2020_A_note_on_multiplicative_functions_resembling_the_M_bius_function.pdf`
- `010_BaezDuarte-Balazard-Landreau-Saias_2000_Notes_sur_la_fonction_zeta_de_Riemann_3.pdf`
- `011_BaezDuarte2002_2002_BaezDuarte2002.pdf`
- `012_Balanzario-SanchezOrtiz_2007_Zeros_Davenport_Heilbronn_Counterexample.pdf`
- `013_Balazard-Saias-Yor_1999_Notes_Fonction_Zeta_Riemann_2_Transcription_VellaChemla.pdf`
- `014_Balog_1987_Integers_Without_Large_Prime_Factors.pdf`
- `015_Baluyot-Goldston-etal_2025_Pair_Correlation_Zeros_I_Proportions_Simple_Critical.pdf`
- `016_Baricz-Laforgia-Pogany_2015_Van_Der_Corput_Inequalities_Bessel.pdf`
- `017_Barrett-Jarvis_1992_Spectral_Properties_Redheffer_Matrix.pdf`
- `018_Bellotti-Wong_2025_Improved_Argument_Zero_Counting_Zeta.pdf`
- `019_Belton2022_2022_Mathematics_Research_Reports.pdf`
- `020_Benedetto-Powell-Yilmaz_2006_Sigma_Delta_Quantization_Finite_Frames.pdf`
- `021_Benvenuti2019_2019_The_inverse_eigenvalue_problem_for_Leslie_matrices.pdf`
- `022_BergelsonKulagaPrzymusLemanczykRichter2019_2019_Discrete_Contin_Dyn_Syst.pdf`
- `023_Bernstein_1929_Fonctions_Absolument_Monotones.pdf`
- `024_Berry_1988_Semiclassical_Formula_Number_Variance_Riemann_Zeros.pdf`
- `025_Beurling_1937_Distribution_Nombres_Premiers_Generalises_I.pdf`
- `026_Bjorner_2011_Cell_Complex_Number_Theory.pdf`
- `027_Bloch_2000_Higher_Regulators_K_Theory_Zeta_Elliptic_Curves.pdf`
- `028_Bogomolny-Keating_1995_Random_Matrix_Theory_Riemann_Zeros_I_Three_Four_Point_Correlations.pdf`
- `029_Bogomolny-Keating_1996_Gutzwiller_Trace_Formula_Spectral_Statistics_Beyond_Diagonal.pdf`
- `030_Bogomolny-Keating_1996_Random_Matrix_Theory_Riemann_Zeros_II_n_Point_Correlations.pdf`
- `031_Bohigas-Leboeuf-Sanchez_2001_Spectral_Spacing_Correlations.pdf`
- `032_Bohr_1926_Fastperiodische_Funktionen_III_Dirichletentwicklung.pdf`
- `033_Bombieri_2010_Classical_Theory_Zeta_And_L_Functions.pdf`
- `034_Bonami1970_1970_Etude_des_coefficients_de_Fourier_des_fonctions_de_L_p_G.pdf`
- `035_Bondarenko-Radchenko-Seip_2023_Fourier_Interpolation_Zeros_Zeta_L_Functions.pdf`
- `036_BorceaBranden2009_2009_Annals_of_Mathematics.pdf`
- `037_Bornemann-Forrester-Mays_2017_Finite_Size_Effects_Spacing_Distributions.pdf`
- `038_Borwein-Straub-Wan-Zudilin_2012_Densities_Short_Uniform_Random_Walks.pdf`
- `039_Bourgain_2017_Decoupling_Exponential_Sums_Riemann_Zeta.pdf`
- `040_Bourgain_undated_On_the_Fourier_Walsh_spectrum_of_the_M_obius_function.pdf`
- `041_Brent-Platt-Trudgian_2020_Sums_Over_Zeros_Riemann_Zeta.pdf`
- `042_Brent2018_2019_On_asymptotic_approximations_to_the_log_Gamma_and_Riemann_Siegel_theta_functions.pdf`
- `043_Brent_1979_Zeros_Riemann_Zeta_Critical_Strip.pdf`
- `044_BretcheDressTenenbaum2020_2020_Mathematika.pdf`
- `045_Brevig-Perfekt-Seip-Siskakis-Vukotic_2016_Multiplicative_Hilbert_Matrix.pdf`
- `046_Broucke-Debruyne-Revesz_2025_Well_Behaved_Beurling_Number_Systems.pdf`
- `047_Broucke-Debruyne-Vindas_2020_Beurling_Integers_RH_Large_Oscillation.pdf`
- `048_Broucke-Vindas_2024_Generalized_Prime_Random_Approximation.pdf`
- `049_Burbea1974_1974_Pacific_Journal_of_Mathematics.pdf`
- `050_Burbea1976_1976_Pacific_Journal_of_Mathematics.pdf`
- `051_Buthe2014_2015_A_method_for_proving_the_completeness_of_a_list_of_zeros_of_certain_functions.pdf`
- `052_Carmona-Petrelis_2017_Limit_Theorems_Random_Walk_Excursion.pdf`
- `053_Carneiro-Chandee-Littmann-Milinovich_2014_Hilbert_Spaces_Pair_Correlation.pdf`
- `054_Carneiro-Milinovich-Ramos_2023_Fourier_Optimization_Montgomery_Pair_Correlation.pdf`
- `055_CarrascoFlorens2000_2000_Econometric_Theory.pdf`
- `056_Cartier-Julia-Moussa-Vanhove_2006_Random_Matrices_Zeta_Dynamical_Systems.pdf`
- `057_Cassaigne-Ferenczi-Mauduit-Rivat-Sarkozy_1999_Liouville_Pseudorandom_Sequences.pdf`
- `058_Chan_2002_More_Precise_Pair_Correlation_Zeros_Primes_Short_Intervals.pdf`
- `059_Chandrasekharan-Mandelbrojt_1959_Solutions_Riemann_Functional_Equation.pdf`
- `060_Chatterjee2007_2007_Stein_s_method_for_concentration_inequalities.pdf`
- `061_Coffey_2005_Polygamma_Theory_Li_Keiper_Constants_Riemann_Hypothesis.pdf`
- `062_Coffey_2009_Certain_Sums_Over_Nontrivial_Zeta_Zeros.pdf`
- `063_Cohn-Elkies_2003_New_Upper_Bounds_Sphere_Packings_I.pdf`
- `064_Connes1998_1998_Connes1998.pdf`
- `065_Connes2026_2026_Connes2026.pdf`
- `066_Conrad_2005_Partial_Euler_Products_Critical_Line.pdf`
- `067_Conrey-Keating_2016_Pair_Correlation_Twin_Primes_Revisited.pdf`
- `068_Conrey-TurnageButterbaugh_2018_r_Gaps_Between_Zeros_Zeta.pdf`
- `069_Conrey_1986_Review_Ivic_Riemann_Zeta_Function.pdf`
- `070_Conrey_1989_More_Than_Two_Fifths_Zeros_Critical_Line.pdf`
- `071_Conrey_2003_Riemann_Hypothesis.pdf`
- `072_ConreySnaith2008_2008_Communications_in_Number_Theory_and_Physics.pdf`
- `073_Coons2010_2010_On_the_multiplicative_Erd_s_discrepancy_problem.pdf`
- `074_Corless-Gonnet-Hare-Jeffrey-Knuth_1996_Lambert_W_Function.pdf`
- `075_Cramer_1919_Nullstellen_Riemannschen_Zetafunktion.pdf`
- `076_Croot_2003_Oscillations_Multiplicative_PlusMinusOne.pdf`
- `077_Croot_2007_Smooth_Numbers_Short_Intervals.pdf`
- `078_Dannon_2008_Riemann_Zeta_Function.pdf`
- `079_Das-Ismoilov-Ramos_2025_Fourier_Optimization_Pair_Correlation_Problems.pdf`
- `080_Daubechies-DeVore_2003_Bandlimited_Function_Stable_Sigma_Delta_Modulators.pdf`
- `081_Davenport-Heilbronn_1936_Zeros_Certain_Dirichlet_Series_I.pdf`
- `082_deBruijn1950_1950_The_roots_of_trigonometric_integrals.pdf`
- `083_Debruyne-Vindas_2019_Complex_Tauberian_Theorems_Laplace_Transforms.pdf`
- `084_deLaValleePoussin_1896_Recherches_Analytiques_Nombres_Premiers_I.pdf`
- `085_DellAnnaEtAl2016_2016_Violation_of_cluster_decomposition_and_absence_of_light_cones_in_local_integer_and_half_integer_spin_chains.pdf`
- `086_Denisov-Kolb-Wachtel_2015_Local_Asymptotics_Random_Walk_Excursions.pdf`
- `087_DerridaEnaudLebowitz2004_2004_The_asymmetric_exclusion_process_and_Brownian_excursions.pdf`
- `088_Diamond-Montgomery-Vorhauer_2006_Beurling_Primes_Large_Oscillation.pdf`
- `089_Diamond_1970_Asymptotic_Distribution_Beurling_Generalized_Integers.pdf`
- `090_Drmota_2009_Sum_Of_Digits_Of_Primes.pdf`
- `091_Durkan-Hughes-PearceCrump_2026_Generalisations_Landau_Gonek_Theorem.pdf`
- `092_DurrettIglehartMiller1977_1977_Weak_convergence_to_Brownian_meander_and_Brownian_excursion.pdf`
- `093_DuttEtAl2019_2019_Nature_Communications.pdf`
- `094_Edwards_1974_Riemanns_Zeta_Function.pdf`
- `095_Engert1970_1970_Finite_dimensional_translation_invariant_subspaces.pdf`
- `096_ErdosEtAl2012_2012_Spectral_statistics_of_Erd.pdf`
- `097_Fazzari-Gerspach-Minelli_2025_Selberg_CLT_Weighted_Linear_Statistics_Zeta_Zeros.pdf`
- `098_FazziGuglielmiMarkovsky2021_2021_A_gradient_system_approach_for_Hankel_structured_low_rank_approximation.pdf`
- `099_Ford-Meng-Zaharescu_2017_Simultaneous_Fractional_Parts.pdf`
- `100_Ford-Soundararajan-Zaharescu_2009_Imaginary_Parts_II.pdf`
- `101_Ford-Zaharescu_2005_Imaginary_Parts_Zeta_Zeros.pdf`
- `102_Ford_2002_Vinogradov_Integral_Bounds_Riemann_Zeta.pdf`
- `103_Forrester-Lebowitz_2013_Local_CLT_Determinantal_Point_Processes.pdf`
- `104_Forrester-Mays_2015_Finite_Size_Corrections_RMT_Odlyzko_Data.pdf`
- `105_Franca-LeClair_2014_Statistical_Properties_Riemann_Zeros_Explicit_Equation_nth_Zero.pdf`
- `106_Franca-LeClair_2014_Theory_Zeros_Riemann_Zeta_And_Other_L_Functions.pdf`
- `107_Franca-LeClair_2015_Transcendental_Equations_Individual_Zeros_L_Functions.pdf`
- `108_Franca-LeClair_2015_Transcendental_Equations_Individual_Zeros_L_Functions_CNTP_Published.pdf`
- `109_Frantzikinakis2020_1908_Correlations_of_multiplicative_functions_along_deterministic_and_independent_sequences.pdf`
- `110_Friedlander-Granville_1993_Smoothing_Smooth_Numbers.pdf`
- `111_Fujii_1974_Zeros_Dirichlet_L_Functions_I.pdf`
- `112_Fujii_1975_Difference_r_Consecutive_Ordinates_Zeros_Zeta.pdf`
- `113_Fujii_1975_Distribution_Zeros_Zeta_Short_Intervals.pdf`
- `114_Gallier2016_2016_Spectral_theory_of_unsigned_and_signed_graphs_applications_to_graph_clustering_a_survey.pdf`
- `115_Ghosh-Sarnak_2012_Real_Zeros_Hecke_Cusp_Forms.pdf`
- `116_Goldfeld_1982_Produits_Partiels_Euleriens_Courbes_Elliptiques.pdf`
- `117_Goldston-Lee-Schettler-Suriajaya_2025_Pair_Correlation_Conjecture_I_Simple_Critical.pdf`
- `118_Goldston-Lee-Schettler-Suriajaya_2025_Pair_Correlation_Conjecture_II_Alternative_Hypothesis.pdf`
- `119_Gonek-Sahay_2024_Consecutive_Moderate_Gaps_Between_Zeros_Zeta.pdf`
- `120_Gonek_1985_Formula_Landau_Mean_Values_Zeta_INCOMPLETE_pp92-96.pdf`
- `121_Gonek_2012_Finite_Euler_Products_Riemann_Hypothesis.pdf`
- `122_GordinPeligrad2011_2011_On_the_functional_central_limit_theorem_via_martingale_approximation.pdf`
- `123_Gouezel2010_2010_Almost_sure_invariance_principle_for_dynamical_systems_by_spectral_methods.pdf`
- `124_GPY2009_2009_Annals_of_Mathematics.pdf`
- `125_Graham-Kolesnik_1991_Computing_Optimal_Exponent_Pairs.pdf`
- `126_Graham-Kolesnik_1991_Simplest_Van_Der_Corput_Estimates.pdf`
- `127_Granville-Soundararajan_2003_Decay_Of_Mean_Values.pdf`
- `128_Granville_2008_Smooth_Numbers_Survey.pdf`
- `129_GrepstadEtAl2019_1909_On_the_asymptotic_behaviour_of_the_sine_product.pdf`
- `130_Grosswald-Schnitzer_1978_Class_Modified_Zeta_L_Functions.pdf`
- `131_Guillera_2013_Sums_Nontrivial_Zeros_Riemann_Zeta.pdf`
- `132_Gunturk-Thao_2003_Ergodic_Dynamics_Sigma_Delta_Quantization.pdf`
- `133_Guth-Maynard_2026_New_Large_Value_Estimates_Dirichlet_Polynomials.pdf`
- `134_Hadamard_1896_Distribution_Zeros_Zeta_Consequences_Arithmetiques.pdf`
- `135_Hamburger_1921_Riemannsche_Funktionalgleichung_Zeta_Funktion_I.pdf`
- `136_Hardy-Littlewood_1917_Riemann_Zeta_And_Distribution_Primes.pdf`
- `137_Harman-Pintz-Wolke_1985_Mobius_And_Liouville_Functions.pdf`
- `138_Harper_2013_Conditional_Bounds_Zeta_Moments.pdf`
- `139_Harper_2020_Moments_Random_Multiplicative_Functions_I.pdf`
- `140_Hasanalizade-Shen-Wong_2022_Counting_Zeros_Riemann_Zeta.pdf`
- `141_HaugPrellberg2015_2015_Uniform_asymptotics_of_area_weighted_Dyck_paths.pdf`
- `142_Haynes-Zudilin_2015_Hankel_Determinants_Zeta_Values.pdf`
- `143_Helfgott-Thompson_2023_Summing_Mobius_Faster_Elementary_Algorithm.pdf`
- `144_HelfgottRadziwill2021_undated_HelfgottRadziwill2021.pdf`
- `145_HerichiLapidus2014_2014_Truncated_infinitesimal_shifts_spectral_operators_and_quantized_universality_of_the_Riemann_zeta_function.pdf`
- `146_HerreraMoree2018_2018_Coefficients_and_higher_order_derivatives_of_cyclotomic_polynomials_old_and_new.pdf`
- `147_HeuslerEtAl2007_2007_Periodic_orbit_theory_of_level_correlations.pdf`
- `148_Hilberdink-Lapidus_2006_Beurling_Zeta_Generalised_Primes_Fractal_Membranes.pdf`
- `149_Hilberdink-Pushnitski_2023_Spectral_Asymptotics_LCM_Matrices.pdf`
- `150_Hilberdink_2006_Determinants_Multiplicative_Toeplitz_Matrices.pdf`
- `151_Hilberdink_2015_Multiplicative_Toeplitz_Matrices_Riemann_Zeta.pdf`
- `152_Hilberdink_2017_Singular_Values_Multiplicative_Toeplitz_Matrices.pdf`
- `153_Hoffman1992_1992_Multiple_harmonic_series.pdf`
- `154_Hruscev-Nikolskii-Pavlov_1981_Unconditional_Bases_Exponentials_Reproducing_Kernels.pdf`
- `155_Hughes-Rudnick_2002_Linear_Statistics_Zeros_Zeta.pdf`
- `156_Hurst2026_2026_Practical_computations_of_the_Mertens_function_M_10.pdf`
- `157_Hurst_2018_Computations_Mertens_Function_Improved_Bounds.pdf`
- `158_Hutchinson_1925_Roots_Riemann_Zeta_Function.pdf`
- `159_Huxley_1989_Exponential_Sums_Riemann_Zeta.pdf`
- `160_Igusa_2000_Introduction_Local_Zeta_Functions.pdf`
- `161_Ingham_1936_Trigonometrical_Inequalities_Theory_Series.pdf`
- `162_Inoue-Kobayashi-Toma_2026_Explicit_Extreme_Values_Argument_Zeta.pdf`
- `163_Inoue_2024_Note_On_r_Gaps_Between_Zeros_Zeta.pdf`
- `164_Ivic_1985_Riemann_Zeta_Theory_Applications.pdf`
- `165_Ivic_2001_Sums_Over_Ordinates_Zeta_Zeros.pdf`
- `166_Ivic_2003_Riemann_Zeta_Dover_Reprint.pdf`
- `167_Janson_2007_Brownian_Excursion_Area_Wright_Constants.pdf`
- `168_Jerby_2023_New_Discriminant_Hardy_Z_Function_Corrected_Gram_Law.pdf`
- `169_Johansson_2001_Discrete_Orthogonal_Polynomial_Ensembles_Plancherel.pdf`
- `170_Johansson_2017_Arb_Arbitrary_Precision_Interval_Arithmetic.pdf`
- `171_Johansson_2018_Numerical_Integration_Ball_Arithmetic.pdf`
- `172_Jones-Sato-Wada-Wiens_1976_Diophantine_Representation_Primes.pdf`
- `173_Jun-Lee_2014_Dedekind_And_Exponential_Sums.pdf`
- `174_Jutila_1977_Zero_Density_Estimates_L_Functions.pdf`
- `175_Kaczorowski-Perelli_1999_Structure_Selberg_Class_I.pdf`
- `176_Kaczorowski-Pintz_1986_Oscillatory_Properties_Arithmetical_Functions_I.pdf`
- `177_Kaczorowski_1991_k_Functions_Multiplicative_Number_Theory_V.pdf`
- `178_KaczorowskiLanguascoPerelli2000_2000_A_note_on_Landau_s_formula.pdf`
- `179_Kaigh1976_1976_An_invariance_principle_for_random_walk_conditioned_by_a_late_return_to_zero.pdf`
- `180_Kanemitsu-Tsukada_2015_Hecke_Type_Zeta_Functions.pdf`
- `181_Kanemitsu-Tsukada_2015_Modular_Relation_Supremacy.pdf`
- `182_Kannan-Bachem_1979_Polynomial_Algorithms_Smith_Hermite_Normal_Forms.pdf`
- `183_Karatsuba-Voronin_1992_Vinogradov_Method_Riemann_Zeta.pdf`
- `184_Kargin_2013_Fluctuations_Riemann_Zeta_Zeros.pdf`
- `185_Kelly-Le_2018_Van_Der_Corput_Sets_Compact_Groups.pdf`
- `186_KhorunzhiyMarckert2009_2009_Uniform_bounds_for_exponential_moment_of_maximum_of_a_Dyck_path.pdf`
- `187_Kinnunen_1997_Hardy_Littlewood_Maximal_Function_Sobolev_Function.pdf`
- `188_Knopp_1994_Dirichlet_Series_Riemann_Functional_Equation.pdf`
- `189_Kolountzakis-Revesz_2003_Turan_Extremal_Problem.pdf`
- `190_Komori-Matsumoto-Tsumura_2023_Zeta_Functions_Root_Systems.pdf`
- `191_Korolev_2012_Gram_Law_Argument_Riemann_Zeta_Publ_Inst_Math.pdf`
- `192_Korolev_2012_Gram_Law_Riemann_Zeta.pdf`
- `193_Kotnik-vandeLune_2004_Order_Mertens_Function.pdf`
- `194_Kousha2012_2012_Asymptotic_behavior_and_the_moderate_deviation_principle_for_the_maximum_of_a_Dyck_path.pdf`
- `195_Kowalski-Robert-Wu_2007_Small_Gaps_And_B_Free_Numbers.pdf`
- `196_Kowalski_2021_Exponential_Sums_Finite_Fields_Elementary.pdf`
- `197_Kowalski_2021_Exponential_Sums_Finite_Fields_II.pdf`
- `198_Kozma-Lev_2011_Exponential_Riesz_Bases_Discrepancy_BMO.pdf`
- `199_Kurasov-Sarnak_2020_Stable_Polynomials_Crystalline_Measures.pdf`
- `200_Labahn-Neiger-Zhou_2018_Hermite_Normal_Form_Polynomial_Matrix.pdf`
- `201_Lagarias2007_2007_Li_coefficients_for_automorphic_functions.pdf`
- `202_Landau_1912_Nullstellen_Zetafunktion.pdf`
- `203_Lapidus-VanFrankenhuysen_2000_Fractal_Geometry_Number_Theory.pdf`
- `204_Lau-Liu-Wu_2010_Symmetric_Square_L_Function_Coefficients.pdf`
- `205_LeClair_2016_Riemann_Hypothesis_Random_Walks_Zeta_Case.pdf`
- `206_LeeLeong2024_2024_New_explicit_bounds_for_the_Mertens_function_and_the_reciprocal_of_the_Riemann_zeta_function.pdf`
- `207_Lester-Matomaki-Radziwill_2015_Small_Scale_Zeros_Modular_Forms.pdf`
- `208_Lev-Olevskii_2015_Quasicrystals_Poisson_Summation_Formula.pdf`
- `209_Lev_2012_Riesz_Bases_Exponentials_Multiband_Spectra_Preprint.pdf`
- `210_Li_2019_Zeta_L_Functions_Number_Theory_Combinatorics.pdf`
- `211_Lindqvist-Seip_1998_Note_Greatest_Common_Divisor_Matrices.pdf`
- `212_Littlewood_1924_Zeros_Riemann_Zeta_Function.pdf`
- `213_Liu2022_2022_Multiplicative_functions_resembling_the_M_bius_function.pdf`
- `214_LiYang2023_2023_An_improvement_on_Gauss_s_circle_problem_and_Dirichlet_s_divisor_problem.pdf`
- `215_Lyubarskii-Seip_1997_Complete_Interpolating_Sequences_Paley_Wiener_Muckenhoupt_Ap.pdf`
- `216_LyubarskiiVershynin2010_2010_Uncertainty_principles_and_vector_quantization.pdf`
- `217_Matiyasevich2007a_1983_Hidden_Life_of_Riemann_s_Zeta_Function_1_Arrow_Bow_and_Targets.pdf`
- `218_Matiyasevich2007b_2007_Hidden_Life_of_Riemann_s_Zeta_Function_2_Electrons_and_Trains.pdf`
- `219_Matomaki-Radziwill-Tao_2015_Averaged_Chowla_Conjecture.pdf`
- `220_Matomaki-Radziwill_2015_Liouville_Short_Intervals.pdf`
- `221_Matomaki-Radziwill_2015_Sign_Changes_Hecke_Eigenvalues.pdf`
- `222_Matomaki-Radziwill_2016_Multiplicative_Functions_Short_Intervals.pdf`
- `223_Matomaki-Shao-Tao-Teravainen_2023_Higher_Uniformity_Arithmetic_Functions.pdf`
- `224_Matomaki-Teravainen_2023_Mobius_Function_All_Short_Intervals.pdf`
- `225_Matomaki_2010_Smooth_Numbers_Short_Intervals.pdf`
- `226_Matomaki_2016_Smooth_Numbers_Short_Intervals_II.pdf`
- `227_MelottiSaias2020_2020_On_path_partitions_of_the_divisor_graph.pdf`
- `228_Mirsky_1949_Frequency_Pairs_Square_Free_Numbers_Given_Difference.pdf`
- `229_Monien_2009_Hankel_Determinants_Dirichlet_Series.pdf`
- `230_Montgomery-Vaughan_1974_Hilberts_Inequality.pdf`
- `231_Montgomery_1973_Pair_Correlation_Zeros_Zeta.pdf`
- `232_MontgomerySoundararajan2004_2004_Comm_Math_Phys.pdf`
- `233_MossinghoffOliveiraTrudgian2021_2021_The_distribution_of_k_free_numbers.pdf`
- `234_Motohashi_1997_Spectral_Theory_Riemann_Zeta.pdf`
- `235_Muellner2017_2017_Automatic_sequences_fulfill_the_Sarnak_conjecture.pdf`
- `236_MullerEtAl2005_2005_Periodic_orbit_theory_of_universality_in_quantum_chaos.pdf`
- `237_Murahara-Onozuka_2025_Equidistribution_A_Points_Zeta_Derivatives.pdf`
- `238_MussardoLeClair2021_2021_Randomness_of_M_obius_coefficients_and_Brownian_motion_growth_of_the_Mertens_function_and_the_Riemann_hypothes.pdf`
- `239_Nakamura_2020_Dirichlet_Series_Periodic_Coefficients_Functional_Equation.pdf`
- `240_Ng2004_2004_Proc_London_Math_Soc.pdf`
- `241_Nishigaki_2024_Consecutive_Level_Spacings_GUE_Ratio.pdf`
- `242_Nishigaki_2025_Consecutive_Level_Spacings_CUE_Finite_Size_Zeta.pdf`
- `243_Norvidas_2011_Entire_Functions_Exponential_Sums.pdf`
- `244_Nunes2015_2015_Journal_of_Number_Theory.pdf`
- `245_Odlyzko-TeRiele_1985_Disproof_Mertens_Conjecture.pdf`
- `246_Odlyzko_1987_Distribution_Spacings_Between_Zeros_Zeta.pdf`
- `247_OganesyanHuse2007_2007_Localization_of_interacting_fermions_at_high_temperature.pdf`
- `248_Olevskii-Ulanovskii_2020_Fourier_Quasicrystals_Unit_Masses.pdf`
- `249_OwczarekPrellberg2014_2014_Pressure_exerted_by_a_vesicle_on_a_surface.pdf`
- `250_Patterson_1988_Introduction_Riemann_Zeta_Function.pdf`
- `251_Patterson_1988_Zeros_Zeta_And_Prime_Number_Theorem.pdf`
- `252_PeligradUtev2005_2005_A_new_maximal_inequality_and_invariance_principle_for_stationary_sequences.pdf`
- `253_Perelli_2016_Converse_Theorems_Zeta_Selberg_Class.pdf`
- `254_Perfekt-Pushnitski_2018_Spectrum_Multiplicative_Hilbert_Matrix.pdf`
- `255_PillaiYin2014_2014_Universality_of_covariance_matrices.pdf`
- `256_Pintz_2026_Oscillation_Mobius_Function_Zeta_Zeros.pdf`
- `257_Platt-Trudgian_2021_RH_True_Up_To_3e12.pdf`
- `258_Platt_2017_Isolating_Nontrivial_Zeros_Zeta.pdf`
- `259_Popov_1985_Transfer_Functions_Riemann_Zeta.pdf`
- `260_Radziwill-Soundararajan_2015_Quadratic_Twists_Central_L_Values.pdf`
- `261_Ramachandra_1976_Problems_Analytic_Number_Theory.pdf`
- `262_Richard_2005_Q_Functional_Equations_Excursion_Moments.pdf`
- `263_Riemann-Wilkins_1859_Prime_Counting_English_Translation.pdf`
- `264_Riemann_1859_Number_Of_Primes_Below_A_Given_Magnitude.pdf`
- `265_RigalZadunaisky2015_2015_Twisted_semigroup_algebras.pdf`
- `266_RodgersTao2018_2018_RodgersTao2018.pdf`
- `267_Roesler_1986_Riemann_Hypothesis_Eigenvalue_Problem.pdf`
- `268_Roesler_1987_Riemann_Hypothesis_Eigenvalue_Problem_II.pdf`
- `269_Rota_1964_Foundations_Combinatorial_Theory_Mobius_Functions.pdf`
- `270_Saffari-Vaughan_1977_Fractional_Parts_X_Over_N_II.pdf`
- `271_Sawin_2022_Mobius_Cancellation_Polynomial_Sequences.pdf`
- `272_Sekatskii-Beltraminelli-Merlini_2012_Integrals_Logarithm_Zeta_RH.pdf`
- `273_Sekatskii_2013_Generalized_Bombieri_Lagarias_Li_Criterion.pdf`
- `274_Sekatskii_2014_Generalized_Li_Criterion_Zeroes_Location.pdf`
- `275_Sheth_2025_Euler_Products_Centre_Chebyshev_Bias.pdf`
- `276_Shir-MartinezAzcona-Chenu_2025_Surmise_Level_Spacing_Beyond_Nearest.pdf`
- `277_Sidi_2003_Riemann_And_Generalized_Zeta_Extrapolation.pdf`
- `278_Siegel_1922_Satz_Hamburger_Funktionalgleichung_Zetafunktion.pdf`
- `279_Soundararajan_2009_Partial_Sums_Mobius_Function.pdf`
- `280_Soundararajan_2010_Smooth_Numbers_Short_Intervals.pdf`
- `281_StampachStovicek2020_2020_On_Hankel_matrices_commuting_with_Jacobi_matrices_from_the_Askey_scheme.pdf`
- `282_Suzuki2025Hilbert_2025_On_the_Hilbert_space_derived_from_the_Weil_distribution.pdf`
- `283_Szekelyhidi1982_1982_Note_on_exponential_polynomials.pdf`
- `284_Tao-Teravainen_2018_Odd_Order_Logarithmically_Averaged_Chowla.pdf`
- `285_Tao-Teravainen_2019_Structure_Logarithmically_Averaged_Correlations.pdf`
- `286_Tao_2016_Logarithmically_Averaged_Chowla_Elliott_Two_Point.pdf`
- `287_Tenenbaum_2015_Analytic_Probabilistic_Number_Theory.pdf`
- `288_Tenenbaum_2017_Generalized_Mertens_Sums.pdf`
- `289_Titchmarsh-HeathBrown_1986_Theory_Riemann_Zeta_Function.pdf`
- `290_Trudgian_2008_Gram_Law_Fails_Positive_Proportion_Of_The_Time.pdf`
- `291_Trudgian_2014_Improved_Upper_Bound_Argument_Zeta_II.pdf`
- `292_Vaughan_1996_Eigenvalues_Redheffer_Matrix_II.pdf`
- `293_Vega_2023_Simple_Proof_Riemann_Hypothesis.pdf`
- `294_Volchkov_1995_Equality_Equivalent_Riemann_Hypothesis_Russian.pdf`
- `295_vonMangoldt_1895_Zu_Riemanns_Abhandlung_Anzahl_Primzahlen.pdf`
- `296_Weil_1952_Formules_Explicites_Nombres_Premiers_Transcription_VellaChemla.pdf`
- `297_Wilf_2004_Redheffer_Matrix_Partially_Ordered_Set.pdf`
- `298_Young_1974_Inequalities_Perturbation_Theorem_Paley_Wiener.pdf`
- `299_Youvan_2024_Phase_Winding_Riemann_Zeta.pdf`
- `300_Zhang_2013_Normalization_Beurling_Generalized_Primes_RH.pdf`
- `301_Zhao_2016_Multiple_Zeta_Polylogarithms_Special_Values.pdf`
- `302_Zhao_2026_Density_Results_r_Gaps_Between_Zeros_Zeta.pdf`
