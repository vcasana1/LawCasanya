# Vía M: dónde queda bloqueada $M_{\tau^C}$ y la condición exacta, solo de ordenadas, que la cierra

Nota de Claude, 25-oct-2026. Sin ejecuciones numéricas. Ningún manuscrito cambiado. Notación de v14:
- $F$ es una función real $C^1$ construida sin ceros, y $u_k=k-\tfrac12-F(\gamma_k)$;
- $N(t)=\theta(t)/\pi+1+S(t)$ (identidad exacta para $t$ que no sea ordenada; $S=\frac1\pi\arg\zeta(\frac12+it)$ por variación continua desde $\sigma=2$);
- $\Psi_j(u)=\frac{(\frac12+u)^{2j+1}+(\frac12-u)^{2j+1}}{2j+1}$ (v14, eq. Psi_def).

## 0. La vía $M_{\tau^C}$ sola no puede cerrar (T)

Por el Teorema B (nota de corte fijo), con corte fijo $X$:

$$\varpi_XM_{C,X}(x)=M_X^*(x)+O_X\bigl(x^{1/2+\varepsilon}\bigr),\qquad M_X^*(x)=\sum_{\substack{n\le x\\ n\mid\prod_{p\le X}p}}\mu(n).$$

Para $x\le X$, todo $n\le x$ libre de cuadrados divide a $\prod_{p\le X}p$, así que $M_X^*(x)=M(x)$ **exactamente**. Además $M_{C,X}=O_X(x^{1/2+\varepsilon})$, porque $\zeta_{C,X}$ tiene sus ceros en la recta por construcción. Las dos constantes $O_X$ vienen del tamaño de $1/\zeta_{C,X}\approx1/(\varpi_XE_X)$ en $\sigma=\tfrac12+\varepsilon$, que puede llegar a

$$\prod_{p\le X}(1+p^{-1/2-\varepsilon})=\exp\Bigl(\frac{(2+o(1))X^{1/2-\varepsilon}}{\log X}\Bigr).$$

Por tanto, **que ambas cotas valgan uniformemente para $X\ge x$ equivale literalmente a $M(x)\ll x^{1/2+\varepsilon}$**. Con corte variable en altura falta además la parte rugosa (nota de consecuencias, §4.3): Perron resuelve $\mu(n)$ en alturas bajas, donde $X(t)$ es pequeño.

Conclusión: la vía M a través de $M_C$ no aporta información que no se le haya puesto. La información tiene que entrar por las **ordenadas**. Es tu regla "μ pura sin sustituir no se demuestra", ahora con prueba.

## 1. Teorema L: localización uniforme $\Rightarrow$ ceros simples y en la recta (T, solo ordenadas)

**Teorema L.** Sea $F$ continua. Si $|u_k(F)|<\tfrac12$ para todo $k$ con $T<\gamma_k\le2T$, entonces todos los ceros con $T<\gamma\le2T$ están en $\Re s=\tfrac12$ y son simples.

*Prueba.* Un cero fuera de la recta tiene pareja $1-\bar\rho$ con la misma ordenada; uno múltiple repite su ordenada. Un bloque de $r\ge2$ ordenadas iguales tiene $u_{j+i}=u_j+i$ y contiene dos valores consecutivos $u,u+1$, de los que uno cumple $|\cdot|\ge\tfrac12$. $\square$

**Corolario (vía M).** Si esto vale para todo $T$ grande, y los ceros de altura acotada están verificados, entonces vale RH y por tanto

$$M(x)\ll_\varepsilon x^{1/2+\varepsilon}$$

(Littlewood; Titchmarsh–Heath-Brown, §14.25, sin cotejar la página). Aquí $\tfrac12$ es un umbral **en unidades de conteo**, no una abscisa: el enunciado solo usa conteo y distancia de ordenadas.

## 2. Teorema L′: la misma condición como integral en $t$ (T, exacto)

Por el Teorema `identity_general` de v14 con exponente $2j$, entre dos ordenadas $\gamma_{k_1}<\gamma_{k_2}$:

$$\sum_{k_1<k<k_2}\Psi_j(u_k)=\mathcal J_j-\mathcal B_j,\qquad \mathcal J_j:=\int_{\gamma_{k_1}}^{\gamma_{k_2}}\bigl(N(t)-F(t)\bigr)^{2j}F'(t)\,dt,$$

$$\mathcal B_j=\frac{(\frac12+u_{k_1})^{2j+1}+(\frac12-u_{k_2})^{2j+1}}{2j+1}.$$

La función $\Psi_j(u)=\int_{u-1/2}^{u+1/2}x^{2j}\,dx$ es par y creciente en $|u|$. Su mínimo es $\Psi_j(0)=\frac{4^{-j}}{2j+1}$ (diente de sierra perfecto), y $\Psi_j(u)\ge\frac1{2j+1}$ si $|u|\ge\tfrac12$. Por tanto, con $n_{\rm int}=k_2-k_1-1$ índices interiores:

$$\#\{k_1<k<k_2:\ |u_k|\ge\tfrac12\}\ \le\ \frac{(2j+1)(\mathcal J_j-\mathcal B_j)-n_{\rm int}4^{-j}}{1-4^{-j}} .$$

**Teorema L′.** Si

$$(2j+1)(\mathcal J_j-\mathcal B_j)\ <\ n_{\rm int}\,4^{-j}+1-4^{-j},$$

entonces no hay índices interiores malos, y por el Teorema L todos los ceros entre $\gamma_{k_1}$ y $\gamma_{k_2}$ son simples y están en la recta.

**Lectura.**
- $\mathcal J_j$ es una integral en $t$ de $N-F=\theta/\pi+1+S-F$, es decir, de $\arg\zeta$ sobre la recta frente a un modelo sin ceros. Las ordenadas solo aparecen como extremos de integración y en los dos términos de borde.
- La condición dice que el error de conteo $N-F$ tiene que ser, en $L^{2j}(dF)$, el diente de sierra puro con un exceso **total** menor que $(1-4^{-j})/(2j+1)$ en toda la ventana.
- Con $j\asymp\log n_{\rm int}$, L′ equivale a L salvo margen. Si $\max|u_k|\le\bar u<\tfrac12$, basta $j\approx\log n_{\rm int}/(2\log\frac1{1/2+\bar u})$.

## 3. Qué ley de corte exige L (modelo, no demostrado)

Los teoremas en media no dan L:
- v14 Thm main da $\langle u_k(T^c)^2\rangle$ acotado para $c\le\tfrac12$;
- S2 descompone el error en media.

Para que *ningún* índice de $\asymp T\log T$ supere $\tfrac12$, en el modelo gaussiano de $u_k$ con varianza $V$ hace falta

$$V\ \le\ \frac1{8\log M_T}\quad\Bigl(\text{de }M_T\cdot2\bar\Phi\bigl(\tfrac1{2\sqrt V}\bigr)<1\Bigr).$$

Esto exige que la varianza del defecto tienda a $0$ con la altura. Con exponente de corte $c$ fijo, el defecto conserva varianza positiva en el modelo. **Hace falta un corte por índice $X_k=(\tau_k/2\pi)^{c(k)}$ con $c(k)\to\infty$: primos más allá de la resonancia $p\approx t/2\pi$.** Coincide con la conclusión de la nota de consecuencias, y ahora con la tasa necesaria: $V(c(T))\lesssim1/\log T$.

## 4. El paso siguiente concreto

Evaluar $\mathcal J_j$ para el $F$ de la tauc con corte $c(k)\to\infty$ y $j\asymp\log T$. Para ello hacen falta momentos de orden $2j\asymp\log T$ del defecto corregido, más allá de la resonancia.

Con las herramientas incondicionales conocidas no se llega. Los momentos de Selberg tienen constantes que crecen como $j^{2j}$, y la teoría solo cubre $c\le\tfrac12$ (v14, `higher_moments`: $X\le T^{1/(160r)}$). El objeto que falta está identificado: **momentos altos del defecto $N-F$ con primos hasta $t^{c(t)}$, $c\to\infty$.** Todo lo demás de la vía M (Teorema L, L′ y el paso a $M$) está demostrado.

**Corrección (25-oct, tras auditar v15).** En §0, "que ambas cotas valgan uniformemente para $X\ge x$ equivale literalmente a $M(x)\ll x^{1/2+\varepsilon}$" debe decir **implica**. El recíproco no está demostrado: que $M$ sea pequeña no acota por separado $\varpi_XM_{C,X}$ ni $\mathcal R_{M,X}$. La conclusión de fondo no cambia: la vía $M_C$ sola no aporta la información, y esta tiene que entrar por otra parte. v15 (Cor. `bothtransfersRH`) lo formula correctamente, como condición suficiente.
