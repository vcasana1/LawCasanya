**La v8 ya corrige los problemas principales que señalamos en la v6.** Están reparados el factor del transporte, el reordenamiento final, la conversión a alturas, la conclusión sobre redondeo, la definición de BW, las constantes de las colas y la colisión de \(\Delta\).

También incorpora los enlaces entre cortes y el rango de órdenes que faltaban en la discusión de Fujii–Korolev. No repetiría esas objeciones como si siguieran sin tratarse.

Estas son las correcciones que quedan en los pasajes revisados. **Las presento aquí; no he modificado el archivo.**

**1. Muestreo: la constante \(7\) no es válida uniformemente en \(r\).**

En la prueba del lema `lem:sampling_rho` se escribe

\[
4r\,\mathfrak b_T(1+\log X)
\le 8\pi rc(1+o(1))\le7.
\]

El \(o(1)\) no es uniforme cuando \(X\) permanece pequeño y \(r\) crece. La sustitución directa y uniforme es

\[
\begin{aligned}
4r\,\mathfrak b_T(1+\log X)
&=\frac{8\pi r(1+\log X)}{\log(3T)}\\
&\le
2\pi\left(1+\frac1{\log2}\right)
\frac{\log T}{\log(3T)}
<16,
\end{aligned}
\]

porque

\[
\log X\ge\log2,
\qquad
r\log X\le\frac14\log T.
\]

Por tanto, en la desigualdad siguiente hay que sustituir el factor \(8\) por \(17\). **El enunciado del lema se conserva**, pues utiliza una constante absoluta sin valor prefijado.

**2. Momentos superiores: falta un factor dependiente de \(r\) en las potencias cuadráticas.**

La prueba de `lem:higher_moments` afirma que las contribuciones de potencias \(m=2\) y \(m\ge3\) son ambas

\[
O\!\left(T^{1/(4r)}\right)
\]

en \(L^{4r}\). El cálculo factorial que ofrece el propio texto solo justifica, para la parte cuadrática,

\[
\left\|S_X^{(2)}\right\|_{L^{4r}(T,2T)}
\le C\sqrt r\,T^{1/(4r)}.
\]

Para las potencias superiores sí basta la convergencia absoluta:

\[
\left\|S_X^{(\ge3)}\right\|_{L^{4r}(T,2T)}
\le C\,T^{1/(4r)}.
\]

La conclusión del lema permanece igual: el término adicional \(C\sqrt r\) queda absorbido por \(Cr^2\).

**3. Pares y ternas: el intervalo elegido puede tener longitud menor que \(1\).**

En `lem:zero_pairs`, el caso

\[
4\mathsf Rb>1
\]

utiliza una estimación declarada para \(h\ge1\), pero después elige

\[
h=\min(2\mathsf Rb,T),
\]

que puede ser menor que \(1\).

La reparación es separar primero el caso grande:

\[
2\mathsf Rb\ge T
\quad\Longrightarrow\quad
n_{\mathsf R}(\gamma_k)
\le\#\mathcal I_T
\ll T\log T
\ll\mathsf R.
\]

En el caso restante se toma un intervalo que contenga las ordenadas pertinentes y tenga longitud

\[
h=\max(1,2\mathsf Rb)\le T.
\]

Como \(4\mathsf Rb>1\), se cumple

\[
h\le4\mathsf Rb,
\qquad
n_{\mathsf R}(\gamma_k)\ll h\log T\ll\mathsf R.
\]

Así quedan justificadas las dos cotas del lema.

**4. Deformación: corregir el exponente del resto y cuantificar el error final.**

La prueba de `prop:deformation` todavía atribuye al resto el exponente \(c_1-1\). El lema anterior proporciona \(c_2-1\). Debe utilizarse

\[
\left|
\nabla_k\left(\frac{\mathfrak r_2}{\mathcal L(\tau)}\right)
\right|
\ll
\frac{T^{c_2-1}}{\log T}.
\]

Además, terminar la estimación intermedia con un mero \(o(1)\) no basta para concluir una cota \(O(c_2)\), porque \(c_2\to0\). Hay que conservar el tamaño de los restos. Con las estimaciones puntuales ya utilizadas puede escribirse

\[
\left\|
\frac{d_2-d_0}{d_0}
\right\|_{4,\mathcal I_T}
\ll
c_2+c_1c_2+
O\!\left(T^{-1/2}\log^3T\right)
\ll c_2.
\]

Esto sí implica la conclusión anunciada:

\[
\left\langle
\left|\frac{d_{2,k}-d_{0,k}}{d_{0,k}}\right|^4
\right\rangle_{\mathcal I_T}
\ll c_2^4.
\]

**5. Corolario final: restringir correctamente el dominio de construcción.**

La v8 dice que, con los parámetros elegidos a altura \(T\), la iteración está definida para **todo** índice con \(\tau_k\ge T_0\). Es una afirmación innecesariamente amplia: las pruebas de localización son para puntos próximos al bloque de altura \(T\).

La formulación suficiente es definir la construcción, para cada \(T\), sobre

\[
\mathcal J_T=\{k:T/2\le\tau_k\le3T\}.
\]

Para \(T\) suficientemente grande,

\[
\mathcal I_T\cup\mathcal I_T^\tau\subseteq\mathcal J_T.
\]

Se aplica la localización en ese bloque ampliado y se mantienen las estimaciones medias sobre sus conjuntos originales. No cambia la salida del reloj.

**6. Sustituir la frase sobre el “corte final fijo”.**

Después del corolario se sigue invocando el transporte del **primer paso** para explicar una limitación del corte **final de la iteración**. Son situaciones diferentes.

La sustitución precisa sería:

> For the one-step clock with a fixed cutoff exponent \(c\), bounded mean-square error in units of zeros is equivalent to bounded mean-square transport. The available transport estimate does not establish this boundedness. This limitation concerns the one-step construction; it does not establish a corresponding obstruction for the final cutoff of the iterated construction.

La equivalencia a la que se refiere es

\[
\|r(T^c)\|_{2,\mathcal I_T}=O_c(1)
\quad\Longleftrightarrow\quad
\|\mathfrak t(T^c)\|_{2,\mathcal I_T}=O_c(1).
\]

**Estas correcciones son internas al TEX.** La nueva afirmación de la v8 de que Ivić–Korolev omite el factor \(k^{2k}\) requiere conservar su respaldo en el original de Korolev; esta lectura del manuscrito no constituye una verificación independiente de esa discrepancia bibliográfica.