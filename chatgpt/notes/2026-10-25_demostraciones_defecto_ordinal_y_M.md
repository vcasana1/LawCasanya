# Dos demostraciones recuperadas: cota ordinal y vía M de Mertens

Fecha: 25 de octubre de 2026. Nota de ChatGPT para el autor. No constituye una nueva versión del artículo. Ninguna construcción utiliza los ceros verdaderos.

## I. Cota ordinal recuperada del móvil (incondicional)

Sean \(\rho_k=\beta_k+i\gamma_k\) los ceros no triviales, ordenados por ordenada y contados con multiplicidad, sin ninguna hipótesis sobre \(\beta_k\). Sea \(F:\mathbb R\to\mathbb R\) una función real cualquiera, construida sin usar los ceros de \(\zeta\). Definamos
\[
u_k(F)=k-\frac12-F(\gamma_k),\qquad
\mathcal I_T=\{k:T<\gamma_k\le2T\}.
\]
Sea \(B_T\) el número de ceros de esa ventana, contados con multiplicidad, que están fuera de la recta crítica o no son simples.

**Teorema 1 (exacto, sin RH).**
\[
\boxed{B_T\le4\sum_{k\in\mathcal I_T}u_k(F)^2},\qquad
\boxed{B_T\le2\,\#\{k\in\mathcal I_T:|u_k(F)|\ge\tfrac12\}}. \tag{1}
\]

**Demostración.**
1. Por la simetría de la ecuación funcional, si \(\rho=\beta+i\gamma\) es un cero con \(\beta\ne1/2\), también lo es \(1-\overline\rho=(1-\beta)+i\gamma\). Por tanto, su ordenada aparece repetida. Un cero múltiple también produce repetición. Recíprocamente, una ordenada repetida corresponde necesariamente a ceros fuera de la recta crítica o a un cero múltiple. Cada bloque de repeticiones está íntegro en \(\mathcal I_T\), porque los extremos de la ventana se definen por la ordenada.
2. En un bloque de \(r\ge2\) ceros con la misma ordenada \(\gamma\), los defectos satisfacen
\[
u_{j+\ell}=u_j+\ell,\qquad 0\le\ell<r,
\]
pues \(F(\gamma)\) no cambia.
3. Para cualquier \(u\in\mathbb R\),
\[
\sum_{\ell=0}^{r-1}(u+\ell)^2
=r\left(u+\frac{r-1}{2}\right)^2+\frac{r(r^2-1)}{12}
\ge\frac{r(r^2-1)}{12}\ge\frac r4.
\]
Por tanto, \(r\le4\sum_{\ell<r}u_{j+\ell}^2\). Sumamos sobre los bloques repetidos y añadimos los cuadrados no negativos de todos los demás índices. Esto prueba la primera cota.
4. Una progresión de paso 1 puede tener como máximo un valor en el intervalo abierto \((-1/2,1/2)\). Así, al menos \(r-1\ge r/2\) defectos de ese bloque satisfacen \(|u|\ge1/2\). Sumando sobre los bloques se obtiene la segunda cota. \(\square\)

La constante 4 es óptima para este argumento: un bloque de longitud 2 con defectos \(-1/2,+1/2\) alcanza la igualdad.

Sea \(K_T=\#\mathcal I_T\). **Corolario 1**:
\[
\frac{N_{\mathrm{recta,simple}}(T,2T]}{K_T}
\ge1-4\left\langle u_k(F)^2\right\rangle_T. \tag{2}
\]
Por tanto, \(\limsup_T\langle u^2\rangle_T<1/4\) da una proporción positiva, y una cota \(<0.145675\) da una proporción garantizada mayor que \(41.73\%\). Si \(\sum_{k\in\mathcal I_T}u_k^2<1/2\) en todas las ventanas suficientemente altas, no puede aparecer ningún bloque repetido a esas alturas; con la comprobación finita restante, se siguen RH y simplicidad. El umbral total \(1/2\) procede del mínimo exacto para un bloque de tamaño 2.

**Teorema 2 (criterio puntual).** Si \(|u_k(F)|<1/2\) para todos los índices de una ventana, todos sus ceros están en la recta y son simples. Prueba: un bloque repetido contiene dos defectos consecutivos \(u,u+1\), incompatibles con que ambos tengan módulo \(<1/2\). Es una condición suficiente, no una estimación ya obtenida para la función \(F\) del reloj.

## II. Demostración de la vía M anterior: lo exacto y la condición que sigue abierta

### II.1. Identidad aritmética de corte fijo

Para \(X\ge2\) definamos el producto de Euler finito
\[
E_X(s)=\prod_{p\le X}(1-p^{-s})^{-1},\qquad
P(X)=\prod_{p\le X}p.
\]
Su recíproco es exactamente el polinomio finito
\[
E_X(s)^{-1}=\prod_{p\le X}(1-p^{-s})
=\sum_{n\mid P(X)}\frac{\mu(n)}{n^s}. \tag{3}
\]
Sea
\[
M_X^*(x)=\sum_{\substack{n\le x\\n\mid P(X)}}^{*}\mu(n),
\qquad
M^*(x)=\sum_{n\le x}^{*}\mu(n),
\]
con peso \(1/2\) si \(n=x\) es entero.

**Teorema 3 (exacto, elemental).** Para \(2\le x\le X\),
\[
\boxed{M_X^*(x)=M^*(x)}. \tag{4}
\]
**Prueba.** Si \(\mu(n)\ne0\), entonces \(n\) es libre de cuadrados. Si además \(n\le x\le X\), todos sus factores primos son \(\le X\); por ello \(n\mid P(X)\). Los demás términos tienen coeficiente cero. Las dos sumas coinciden término a término, incluido el peso en el extremo. \(\square\)

### II.2. Comparación por Perron bajo una hipótesis analítica explícita

Sea \(\zeta_{C,X}\) una zeta sintética de corte fijo, construida con las ordenadas del reloj Casaña y los primos, y sea
\[
F_{C,X}(s)=\zeta_{C,X}(s)^{-1},\qquad \varpi_X\ne0.
\]
Fijemos \(\sigma=1/2+\varepsilon\in(1/2,1)\). **Hipótesis de transición a verificar:** \(F_{C,X}\) es holomorfa en esa recta y
\[
D_X(s):=\varpi_XF_{C,X}(s)-E_X(s)^{-1}
\]
satisface
\[
J_X(\sigma):=\frac1{2\pi}\int_{-\infty}^{\infty}
\frac{|D_X(\sigma+it)|}{|\sigma+it|}\,dt<\infty. \tag{5}
\]
La fórmula de transición que se había propuesto para el corte fijo pretende establecer esta hipótesis; sus controles uniformes de contorno no estaban completamente auditados. No se toma (5) por demostrada sin ese paso.

Definimos, cuando el límite simétrico existe,
\[
M_{C,X}(x):=\lim_{U\to\infty}
\frac1{2\pi i}\int_{\sigma-iU}^{\sigma+iU}
\frac{x^s F_{C,X}(s)}s\,ds.
\]

**Teorema 4 (implicación rigurosa de (5)).**
\[
\boxed{\varpi_X M_{C,X}(x)=M_X^*(x)+\mathcal R_X(x)},\qquad
|\mathcal R_X(x)|\le J_X(\sigma)x^\sigma, \tag{6}
\]
donde
\[
\mathcal R_X(x)=\frac1{2\pi i}
\int_{\sigma-i\infty}^{\sigma+i\infty}\frac{x^sD_X(s)}s\,ds.
\]
**Prueba.** Por (3) y el lema de Perron simétrico aplicado a cada término del polinomio finito,
\[
\lim_{U\to\infty}\frac1{2\pi i}
\int_{\sigma-iU}^{\sigma+iU}
\frac{x^sE_X(s)^{-1}}s\,ds=M_X^*(x).
\]
Por (5), la integral de \(D_X(s)x^s/s\) converge absolutamente. Sumando ambas integrales resulta (6), y el módulo de la segunda está acotado por \(x^\sigma J_X(\sigma)\). \(\square\)

Combinando (4) y (6), para \(2\le x\le X\) resulta
\[
\boxed{M^*(x)=\varpi_X M_{C,X}(x)-\mathcal R_X(x)}. \tag{7}
\]
La igualdad (7) es exacta **si se satisface (5)**; el término restante no puede eliminarse solo porque la zeta sintética tenga ceros en la recta.

### II.3. Condición de cierre de la vía M y RH

Si para todo \(\varepsilon>0\), de manera uniforme al tomar \(X\ge x\), se consiguiera demostrar
\[
\varpi_X |M_{C,X}(x)|\ll_\varepsilon x^{1/2+\varepsilon},
\qquad
|\mathcal R_X(x)|\ll_\varepsilon x^{1/2+\varepsilon},
\tag{8}
\]
entonces (7) daría \(M(x)\ll_\varepsilon x^{1/2+\varepsilon}\) (sin diferencia relevante entre \(M^*\) y \(M\)). No se ha demostrado (8): el subíndice \(O_X\) para corte fijo no puede suprimirse ni sustituirse por una cota uniforme en \(X=x\).

**Prueba de que (8) implicaría RH.** Por sumación parcial, inicialmente para \(\Re s>1\),
\[
\frac1{\zeta(s)}=s\int_1^\infty M(x)x^{-s-1}\,dx.
\]
Si \(M(x)\ll_\varepsilon x^{1/2+\varepsilon}\) para todo \(\varepsilon>0\), la integral converge localmente uniformemente en \(\Re s>1/2\) y proporciona continuación holomorfa de \(1/\zeta(s)\) allí. Por unicidad analítica, \(\zeta\) carece de ceros en \(\Re s>1/2\). La simetría de la ecuación funcional da RH. \(\square\)

**Ruta directa por la cota ordinal:** el Teorema 2, si se demostrase para todos los índices altos de una \(F\) construida solo con reloj y primos, daría RH y, como consecuencia, \(M(x)\ll_\varepsilon x^{1/2+\varepsilon}\). Esta implicación es incondicional; su hipótesis puntual no está todavía obtenida.

## III. Estado de los resultados

- Demostrados incondicionalmente: las dos cotas ordinales (1), la igualdad friable (4), el criterio puntual como implicación.
- Demostrada como implicación bajo (5): la comparación Perron (6) y la identidad (7).
- Pendiente: justificar completamente la transición analítica (5) para la zeta Casaña definida, y obtener controles uniformes en \(X\) del tipo (8); alternativamente, demostrar el criterio puntual \(|u_k(F)|<1/2\) para todos los índices suficientemente altos.
- Ni la identidad friable ni el hecho de que los ceros de \(\zeta_{C,X}\) estén en \(\Re s=1/2\) demuestran por sí solos RH.

Fuentes internas consultadas: \`CasanyaLawI_v13.tex\`, sección «The Mertens transfer target»; \`work/notes/2026-10-24_mertens_sintetico_reloj_casanya.md\`, teorema B; \`work/notes/2026-10-25_umbrales_proporcion_cota_exacta.md\`; \`work/notes/2026-10-25_via_M_localizacion_uniforme.md\`. No se han utilizado ceros reales para construir \(F\), \(E_X\) o \(\zeta_{C,X}\).
