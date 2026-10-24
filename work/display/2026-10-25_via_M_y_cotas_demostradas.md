# Vía M: bloqueo de $M_{\tau^C}$, Teorema L y L′; resumen de las cotas demostradas

Respuestas de Claude, 25-oct-2026. Nota completa: `work/notes/2026-10-25_via_M_localizacion_uniforme.md`.

## A. Vía M

La vía M a través de $M_{\tau^C}$ no puede cerrar por sí sola; está demostrado y no es una cuestión de técnica. Lo que la cierra es una condición solo de ordenadas, que he escrito en forma exacta: el Teorema L y su versión integral L′. Lo que falta está identificado con precisión.

### 0. Por qué $M_C$ sola no cierra

El Teorema B da, con corte fijo $X$,

$$\varpi_XM_{C,X}(x)=M_X^*(x)+O_X\bigl(x^{1/2+\varepsilon}\bigr).$$

Para $x\le X$ se tiene exactamente $M_X^*(x)=M(x)$, porque todo $n\le x$ libre de cuadrados divide a $\prod_{p\le X}p$. Además $M_{C,X}=O_X(x^{1/2+\varepsilon})$, ya que $\zeta_{C,X}$ tiene los ceros en la recta por construcción.

Las dos constantes $O_X$ vienen de $1/E_X$ en $\sigma=\tfrac12+\varepsilon$, que puede llegar a $\exp\bigl(2X^{1/2-\varepsilon}/\log X\bigr)$. Por eso, pedir que ambas cotas sean uniformes para $X\ge x$ es literalmente pedir $M(x)\ll x^{1/2+\varepsilon}$.

Con corte variable en altura falta además la parte rugosa: Perron resuelve $\mu(n)$ en alturas bajas, donde $X(t)$ es pequeño. Es la regla del autor de que "μ pura sin sustituir no se demuestra", ahora con prueba: la información tiene que entrar por las ordenadas.

### 1. Teorema L (demostrado, solo conteo y distancia de ordenadas)

Sea $u_k=k-\tfrac12-F(\gamma_k)$, con $F$ continua construida sin ceros. Si

$$|u_k|<\tfrac12\quad\text{para todo }k\text{ con }T<\gamma_k\le2T,$$

entonces todos los ceros de esa ventana son simples y están en la recta.

La prueba es la de los bloques: un bloque de ordenadas repetidas contiene dos valores consecutivos $u$ y $u+1$, y uno de ellos tiene módulo $\ge\tfrac12$. Si esto vale para todo $T$ grande, se sigue RH y por tanto $M(x)\ll x^{1/2+\varepsilon}$ (Littlewood; Titchmarsh–Heath-Brown §14.25, sin cotejar la página). El $\tfrac12$ es un umbral en unidades de conteo, no una abscisa.

### 2. Teorema L′: la misma condición como integral en $t$

Por la identidad de v14 (`identity_general`, exponente $2j$), sea $n_{\rm int}$ el número de índices interiores entre $\gamma_{k_1}$ y $\gamma_{k_2}$. Si

$$(2j+1)\Bigl(\int_{\gamma_{k_1}}^{\gamma_{k_2}}(N-F)^{2j}F'\,dt-\mathcal B_j\Bigr)<n_{\rm int}\,4^{-j}+1-4^{-j},$$

no hay ningún índice interior malo. Aquí $\mathcal B_j$ son los dos términos de borde de la identidad.

- **Qué se integra.** $N-F=\theta/\pi+1+S-F$, es decir, $\arg\zeta$ sobre la recta frente al modelo sin ceros. Las ordenadas solo entran como extremos de integración.
- **Qué exige.** El error de conteo tiene que ser el diente de sierra puro, cuyo mínimo es $\Psi_j(0)=4^{-j}/(2j+1)$, con un exceso total menor que $(1-4^{-j})/(2j+1)$ en toda la ventana.
- **Relación con L.** Con $j\asymp\log T$, L′ equivale a L salvo margen.

### 3. Qué ley de corte hace falta (modelo, no demostrado)

Los resultados en media (Thm main de v14, S2) no bastan, porque L pide que no falle ningún índice de los $\asymp T\log T$. En el modelo gaussiano eso exige

$$V\le\frac1{8\log M_T},$$

con $V$ la varianza del defecto $u_k$. Es decir, la varianza tiene que tender a 0 con la altura. Con exponente $c$ fijo eso no ocurre en el modelo. Hace falta un corte por índice $X_k=(\tau_k/2\pi)^{c(k)}$ con $c(k)\to\infty$, es decir, primos más allá de la resonancia $p\approx t/2\pi$.

### 4. Lo que falta

Un único objeto: los momentos de orden $2j\asymp\log T$ del defecto $N-F$ para la tauc con $c\to\infty$. Con las herramientas incondicionales conocidas no se llega: los momentos de Selberg tienen constantes del orden de $j^{2j}$, y la teoría de v14 solo cubre $X\le T^{1/(160r)}$. El resto de la vía M está demostrado: Teorema L, L′ y el paso de RH a $M$.

## B. Resumen de las cotas demostradas de hoy

**1. Cota de proporción (incondicional y exacta).** Sea $u_k=k-\tfrac12-F(\gamma_k)$, con $F$ cualquier función continua construida sin ceros. Sea $B_T$ el número de ceros con $T<\gamma\le2T$ que están fuera de la recta o no son simples. Entonces

$$B_T\le4\sum_{T<\gamma_k\le2T}u_k^2,\qquad B_T\le2\,\#\{k:|u_k|\ge\tfrac12\}.$$

Por tanto, la fracción de ceros en la recta y simples cumple

$$\ \ge\ 1-4\langle u_k^2\rangle .$$

Prueba: en un bloque de $r\ge2$ ordenadas iguales, $u$ avanza de 1 en 1, y

$$\sum_{i<r}(u+i)^2\ \ge\ \frac{r(r^2-1)}{12}\ \ge\ \frac r4 .$$

**2. Umbrales.**

$$\langle u^2\rangle<\tfrac14\ \Rightarrow\ \text{proporción}>0,\qquad \langle u^2\rangle<0.14568\ \Rightarrow\ \text{proporción}>41.73\,\%.$$

**3. Teorema L.** Si $|u_k|<\tfrac12$ para todo $k$ de la ventana, todos sus ceros son simples y están en la recta. Si eso vale para todo $T$, se sigue RH, y con ella

$$M(x)\ll x^{1/2+\varepsilon}.$$

**4. Teorema L′ (forma integral).** Sea $n_{\rm int}$ el número de índices entre $\gamma_{k_1}$ y $\gamma_{k_2}$, extremos excluidos, y $\mathcal B_j$ los dos términos de borde de la identidad de v14. Si

$$(2j+1)\Bigl(\int_{\gamma_{k_1}}^{\gamma_{k_2}}(N-F)^{2j}F'\,dt-\mathcal B_j\Bigr)<n_{\rm int}\,4^{-j}+1-4^{-j},$$

no hay ningún índice malo en ese tramo. Aquí $N-F=\theta/\pi+1+S-F$.

**Lo que no está demostrado:** que $\langle u^2\rangle$ quede por debajo de $\tfrac14$, que es la Pregunta 13.1 de v14. La prueba de v14 da como mucho $\approx0.494$.
