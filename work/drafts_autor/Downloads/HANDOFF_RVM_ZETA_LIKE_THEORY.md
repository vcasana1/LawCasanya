# Handoff: teoría zeta-like del reloj RVM

Quiero desarrollar un manuscrito autónomo, separado de la ruta de colisiones y de la teoría de excursiones, sobre el sistema sintético determinado por el reloj midpoint de Riemann--von Mangoldt.

El resultado debe llamarse inicialmente `rvm_zeta_pi_mertens_v1.tex` y tener una copia `.txt` byte a byte idéntica. Debe ser un documento de investigación matemático, con dominios, convenciones de inversión, pruebas completas de cada afirmación marcada como teorema, y una separación estricta entre teoremas, hipótesis y objetivos. No afirmar RH ni insinuar que el hecho de poner ceros sintéticos en la recta crítica prueba nada sobre los ceros genuinos.

## Fuente obligatoria

Extraer primero el material pertinente de `excursion_area_section_v56.tex`, en particular la sección **The RVM arithmetic system and its relation to the classical one**. Mantener el contenido matemático, pero reorganizarlo de forma autosuficiente. No importar la cota cúbica de colisiones ni la ruta Catalan, salvo una frase que diga que son programas distintos y no son premisas de esta teoría.

La notación correcta es:

\[
\rho_k=\beta_k+i\gamma_k
\]

para ceros genuinos, sin imponer \(\beta_k=1/2\), y

\[
\rho_k^{\rm RVM}=\frac12+i\gamma_k^{\rm RVM}
\]

para los ceros sintéticos del reloj. No usar \(\tau_k\) como sustituto de \(\gamma_k^{\rm RVM}\).

## Núcleo que debe quedar como teorema

Definir el reloj midpoint

\[
\mathcal N_{\rm RVM}(T)=\frac{T}{2\pi}\log\frac{T}{2\pi e}+\frac78,
\qquad
\mathcal N_{\rm RVM}(\gamma_k^{\rm RVM})=k-\frac12,
\]

y su inversa de Lambert

\[
\gamma_k^{\rm RVM}
=\frac{2\pi(k-11/8)}{W_0((k-11/8)/e)}.
\]

Definir

\[
P_{\rm RVM}^{\rm crit}(s)=
\prod_{k\ge1}\left(1+
\frac{s(s-1)}{1/4+(\gamma_k^{\rm RVM})^2}\right),
\]

\[
G(s)=s(s-1)\Gamma(s/2)\pi^{-s/2},
\qquad
\zeta_{\rm RVM}(s)=\frac{P_{\rm RVM}^{\rm crit}(s)}{G(s)}.
\]

Probar con normal convergencia:

- \(P_{\rm RVM}^{\rm crit}\) es entero y \(P(s)=P(1-s)\);
- los ceros no triviales de \(\zeta_{\rm RVM}\) son exactamente \(1/2\pm i\gamma_k^{\rm RVM}\), simples;
- \(\zeta_{\rm RVM}\) tiene residuo 1 en \(s=1\) y los ceros triviales usuales;
- el carácter crítico es una **entrada de la construcción**, no RH.

## Centroides y sumas exponenciales RVM

Incluir una sección específica para

\[
S_{\rm RVM}(N;u)=\sum_{k\le N}e^{iu\gamma_k^{\rm RVM}},
\quad
C_{\rm RVM}^{\rm pts}(N;u)=\frac{S_{\rm RVM}(N;u)}N,
\]

\[
C_{\rm RVM}^{\rm path}(N;u)=\frac1N\sum_{n\le N}S_{\rm RVM}(n;u)
=\sum_{k\le N}\frac{N-k+1}{N}e^{iu\gamma_k^{\rm RVM}}.
\]

Extraer y probar el resultado de v56:

\[
\sup_{u\in[a,b]}|S_{\rm RVM}(N;u)|\ll_{a,b}1+\log N
\qquad(0<a\le b<\infty).
\]

La prueba usa los incrementos y segundas diferencias del reloj inverso y sumación de Abel. Consecuencias: el centroide de puntos tiende a cero; no afirmar que el centroide de camino converge.

Incluir además el transformado por altura, que debe distinguirse de Mertens:

\[
M_H^{\rm RVM}(x)=\frac{1}{N_{\rm RVM}(H)}
\sum_{\gamma_k^{\rm RVM}\le H}x^{i\gamma_k^{\rm RVM}}.
\]

Para los ceros genuinos, reservar

\[
M_H(x)=\frac1{N(H)}\sum_{\rho=\beta+i\gamma,\ 0<\gamma\le H}x^{i\gamma}.
\]

Este \(M_H\) es un promedio exponencial de ordenadas; **no** es la función de Mertens.

## Construcción completa de \(J_{\rm RVM}\) y \(\pi_{\rm RVM}\)

Definir primero la versión simétrica de la fórmula explícita:

\[
J_{\rm RVM}(x)=\operatorname{li}(x)
-2\Re\sum_{k\ge1}\operatorname{Ei}\bigl((1/2+i\gamma_k^{\rm RVM})\log x\bigr)
-\log2+\int_x^\infty\frac{dt}{t(t^2-1)\log t}.
\]

Probar, como en v56, que esta suma existe y converge uniformemente sobre compactos de \(\log x\in(0,\infty)\). Usar el resultado de sumas exponenciales RVM y la expansión de \(\operatorname{Ei}\).

Definir \(J_{\rm RVM}^*=0\) bajo 2 y \(J_{\rm RVM}^*=J_{\rm RVM}\) a partir de 2. Después definir exactamente

\[
\pi_{\rm RVM}(x)=\sum_{m\le\log_2x}\frac{\mu(m)}m
J_{\rm RVM}^*(x^{1/m}),
\]

y demostrar la inversión finita

\[
J_{\rm RVM}^*(x)=\sum_{m\le\log_2x}\frac1m\pi_{\rm RVM}(x^{1/m}).
\]

La estimación

\[
J_{\rm RVM}(x)-\operatorname{li}(x),\
\pi_{\rm RVM}(x)-\operatorname{li}(x)
=O\!\left(\frac{\sqrt x(\log\log x)^2}{\log x}\right)
\]

debe estar sólo como **Hipótesis de estimación Lambert**, con las obligaciones explícitas: colas, ramas de \(\operatorname{Ei}\), extremos e integración por partes uniforme en bloques del reloj.

## Pesos enteros y paso continuo-a-atómico

Definir

\[
c_n^{\rm RVM}=\pi_{\rm RVM}(n)-\pi_{\rm RVM}(n-1),
\qquad
\zeta_{\mathbb Z,\rm RVM}(s)=
\prod_{n\ge2}(1-n^{-s})^{-c_n^{\rm RVM}}.
\]

Incluir sólo condicionalmente la factorización con \(\zeta_{\rm RVM}\), bajo control de celda unidad y la identificación Mellin--Stieltjes. Mantener visible el lema de cancelación exacta

\[
\int_{n-1}^{n}2\cos(2\pi x)\,dx=0,
\]

y la hipótesis de resto de celda que llevaría a \(c_n^{\rm RVM}\sim1/\log n\) y luego a la realización \(0/1\). No confundir pesos analíticos con primos genuinos.

## Construcción completa de \(M_{\rm RVM}^{\rm crit}\)

Definir

\[
\widehat M_{\rm RVM}^{\rm crit}(s)=\frac1{\zeta_{\rm RVM}(s)},
\]

y, cuando exista inversión ordinaria,

\[
M_{\rm RVM}^{\rm crit}(x)=\frac1{2\pi i}
\int_{c-i\infty}^{c+i\infty}
\frac{x^s}{s\zeta_{\rm RVM}(s)}\,ds.
\]

El documento debe declarar con precisión que los polos no triviales de su transformada están en \(1/2\pm i\gamma_k^{\rm RVM}\), de modo que la abscisa de polos es \(1/2\) por construcción.

De v56 se puede incluir el teorema regularizado:

\[
M_{\rm RVM,G}^{\rm crit}(x)=
\frac1{2\pi i}\int_{(c)}e^{s^2}
\frac{x^s}{s\zeta_{\rm RVM}(s)}\,ds
=O_\varepsilon(x^{1/2+\varepsilon}),
\]

**bajo** la hipótesis uniforme

\[
1/\zeta_{\rm RVM}(\sigma+it)=\exp(o(t^2)).
\]

No presentar todavía como teorema la cota puntual no suavizada

\[
M_{\rm RVM}^{\rm crit}(x)=O_\varepsilon(x^{1/2+\varepsilon}).
\]

La vía nueva candidata para cerrarla es demostrar, en bandas cerradas a la derecha de \(1/2\),

\[
\zeta_{\rm RVM}(s)=Z_{\rm RVM}(1+\chi(s))(1+O(1/|t|)),
\]

por Abel--Plana aplicado al producto midpoint y su polo móvil. Si esto se prueba de forma plenamente uniforme, entonces

\[
\frac1{\zeta_{\rm RVM}(\sigma+it)}-rac1{Z_{\rm RVM}}
=O(|t|^{-(\sigma-1/2)})
\]

y la Perron renormalizada se desplaza a \(1/2+\varepsilon\), dando la cota sin suavizar. Pero el documento inicial debe clasificar el asintótico funcional como **teorema objetivo pendiente de auditoría**, no como resultado cerrado, hasta justificar: contorno Abel--Plana, polo móvil, ramas y cota uniforme de borde.

## Defecto exacto respecto a \(\zeta\), \(\pi\) y \(M\)

Incluir

\[
\mathcal Q_{\rm RVM}(s)=
\frac{\zeta(s)}{\zeta_{\rm RVM}(s)}
=\frac{P_\zeta(s)}{P_{\rm RVM}^{\rm crit}(s)},
\]

y

\[
\widehat M_{\rm RVM}^{\rm crit}(s)
=\mathcal Q_{\rm RVM}(s)\frac1{\zeta(s)}.
\]

Condicionalmente a que las inversas Mellin vivan en el mismo espacio, esto es una convolución Mellin. No afirmar que el cociente sea acotado o invertible: ése es precisamente el problema que conecta la teoría sintética con \(M\) genuina.

También incluir

\[
\varepsilon_n^{\rm RVM}=\mathbf 1_{\{n\text{ primo}\}}-c_n^{\rm RVM},
\qquad
\sum_{n\le N}\varepsilon_n^{\rm RVM}=pi(N)-\pi_{\rm RVM}(N).
\]

## Reglas de redacción

- No declarar que RH se sigue de \(\zeta_{\rm RVM}\), \(M_{\rm RVM}\), \(M_H\), los centroides, ni de la cota gaussiana.
- No tratar el exponente cúbico de colisiones como input de este manuscrito.
- Distinguir siempre: \(M_H\) (promedio finito de fases), \(M_{\rm RVM}^{\rm crit}\) (Mertens sintético), y \(M\) (Mertens genuina).
- Distinguir teoremas de v56, hipótesis analíticas y objetivos nuevos.
- Mantener las ecuaciones a la derecha y evitar colisiones de variables.
- Añadir bibliografía de França--LeClair para la fórmula Lambert, y Titchmarsh para la fórmula de Riemann--von Mangoldt.

## Referencias que debe usar el manuscrito

Usar únicamente las que correspondan a una afirmación realmente empleada. No citar trabajos de colisiones, GUE o excursiones salvo que una sección los use de verdad.

### Reloj Riemann--von Mangoldt y aproximación Lambert

1. Guilherme França and André LeClair, *Statistical and other properties of Riemann zeros based on an explicit equation for the \(n\)-th zero on the critical line*, arXiv:1307.8395v3 (2014). Fuente de la aproximación Lambert con el desplazamiento \(11/8\) y de la reconstrucción numérica por las ordenadas sintéticas.

2. NIST Digital Library of Mathematical Functions, §4.13, *Lambert W-Function*. Citar para la rama principal \(W_0\), sus identidades de derivación y expansión asintótica.

3. E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed., revised by D. R. Heath-Brown, Clarendon Press, Oxford, 1986. Referencia principal para Riemann--von Mangoldt, \(S(T)\), productos canónicos y fórmula explícita.

4. H. M. Edwards, *Riemann's Zeta Function*, Academic Press, 1974. Referencia alternativa para la fórmula de conteo, \(\vartheta\) de Riemann--Siegel y normalizaciones históricas.

### Productos canónicos, función funcional y fórmulas explícitas

5. J. Hadamard, *Sur la distribution des zéros de la fonction \(\zeta(s)\) et ses conséquences arithmétiques*, Bulletin de la Société Mathématique de France **24** (1896), 199--220. Sólo si se expone el contexto histórico de la factorización.

6. H. L. Montgomery and R. C. Vaughan, *Multiplicative Number Theory I: Classical Theory*, Cambridge Studies in Advanced Mathematics 97, Cambridge University Press, 2007. Para Perron, inversión de Möbius, Dirichlet series y herramientas de análisis elemental.

7. H. Iwaniec and E. Kowalski, *Analytic Number Theory*, American Mathematical Society Colloquium Publications 53, 2004. Para formulaciones modernas de la fórmula explícita, contornos e inversión Mellin/Perron.

8. S. M. Gonek, *An explicit formula of Landau and its applications to the theory of the zeta-function*, Contemporary Mathematics **143** (1993), 395--413. Usar sólo si se incluye la comparación de resonancias del sistema sintético con sumas de fases de ordenadas genuinas.

### \(J_{\rm RVM}\), \(\pi_{\rm RVM}\), pesos y sistemas generalizados

9. A. F. Möbius, *Über eine besondere Art von Umkehrung der Reihen*, Journal für die reine und angewandte Mathematik **9** (1832), 105--123. Referencia histórica opcional para la inversión de Möbius; la prueba usada en el texto debe ser autosuficiente.

10. Frederik Broucke, Gregory Debruyne and Jasson Vindas, *Beurling integers with RH and large oscillation*, Advances in Mathematics **370** (2020), 107240; arXiv:2004.11501. Usar solamente en la discusión de que el objeto con pesos \(c_n^{\rm RVM}\) es un sistema generalizado/ponderado, no un sistema de primos ordinarios.

### Referencias que entran sólo en extensiones futuras

11. H. Hamburger, *Über die Riemannsche Funktionalgleichung der \(\zeta\)-Funktion*, Mathematische Zeitschrift **10** (1921), 240--254. Incluir sólo si se añade el criterio endpoint de Hamburger; no es necesario para la v1 centrada en \(\zeta_{\rm RVM}\), \(\pi_{\rm RVM}\), \(M_{\rm RVM}\) y \(M_H\).

12. F. W. J. Olver, *Asymptotics and Special Functions*, AK Peters/CRC Press, 1997. Útil sólo si se redacta en detalle el programa de fase estacionaria y los restos uniformes de \(\operatorname{Ei}\); no sustituye la demostración específica requerida por el reloj Lambert.

### Referencias que no deben usarse como sustituto de una prueba

- França--LeClair no prueba el producto \(\zeta_{\rm RVM}\), la factorización de Hadamard de este nuevo objeto ni la cota de \(M_{\rm RVM}^{\rm crit}\).
- Ninguna referencia de Beurling o de modelos de primos artificiales prueba positividad de \(c_n^{\rm RVM}\) ni el resto de celda de este reloj.
- Los teoremas clásicos de Perron o de desplazamiento de contorno no prueban por sí solos la cota no suavizada de \(M_{\rm RVM}^{\rm crit}\): antes hay que demostrar el control vertical de \(1/\zeta_{\rm RVM}\).
