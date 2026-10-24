Hecho, con dos leyes de corte: A es $c$ fijo índice a índice, $X_k=(\tau_k/2\pi)^c$; B es $c(\tau)=(\log\log\tau)^{-1/2}$, el corte del primer paso localizado en $k$. Primero va el Teorema A′ y después el B′. La nota nueva es `2026-10-24_mertens_sintetico_corte_variable.md`; la de corte fijo no la he tocado. No he subido nada.

**Construcción.** Los puntos son $\kappa_k=\tau_k-S_{X_k}(\tau_k)/\Lambda(\tau_k)$ y la zeta es $\zeta_C=\mathcal P_C/G$ sobre ellos. El producto no depende del orden de los puntos, así que ya no hace falta un reloj corregido monótono, y $\zeta_C$ no tiene ceros fuera de $\tfrac12$.

**Teorema A′ (transición en media).** En cada recta $\Re s=\tfrac12+\sigma'$,

$$\frac1T\int_T^{2T}\Bigl|\log\zeta_C(s)-\mathrm{cte}-\log E^\natural_{X(t)}(s)\Bigr|\,dt\ \ll\ \frac{\log\log T}{\log T}+T^{-(1-c_0)\sigma'}+\cdots\ \to0 .$$

- **La clave de la prueba.** La suma sobre $k$ se hace en los $\tau_k$, que sí son cruces de nivel de $N_0$. En la parte lisa, el $\Lambda$ de $dN_0$ cancela exactamente el $1/\Lambda$ del paso de Newton, y el residuo en $\tau_*$ da $\log E_{X(t)}(s)$, con el corte evaluado a la altura $t$.
- **El segundo orden** se acota de forma absoluta con la media de $S_X^2$ en los puntos del reloj, sin ceros.
- **El aliasing** no tiene fase estacionaria porque

$$m\log\frac{\tau}{2\pi}-\log p\ \ge\ (1-c_0)\log\frac{\tau}{2\pi}.$$

Ese es el único sitio donde se usa $c<1$: la resonancia $p\approx t/2\pi$ de v14 corresponde a $c=1$. Esta parte del aliasing tiene el mecanismo y los exponentes escritos, pero no la he comprobado línea a línea.

**Corolario.** Combinando A′ con Titchmarsh §11.9, (11.9.1), pp. 303–304, que es incondicional, se obtiene que $\zeta$ y $\zeta_C$ coinciden en $\log$, salvo una constante, en todo $\Re s>\tfrac12$, para $t$ fuera de un conjunto de medida pequeña. La $\zeta_{\RVM}$ desnuda no cumple esto. Si el conjunto excepcional fuera vacío, se tendría RH salvo un número finito de ceros (clase R).

**Teorema B′ (Perron).** Con un corte que crece con la altura, el primo $P^+(n)$ solo está presente para $|t|\ge t_n=X^{-1}(P^+(n))$. Por Perron truncado,

$$\frac1{2\pi}\int_{t_n\le|t|\le U}\frac{(x/n)^{c+it}}{c+it}\,dt=O\Bigl(\frac{(x/n)^c}{t_n|\log(x/n)|}\Bigr).$$

El indicador $\mathbf 1_{n<x}$ que convierte Perron en $\sum_{n\le x}\mu(n)$ se genera en las alturas bajas, justo donde ese primo todavía falta. Por eso el término principal de $M_C$ es $1$ y no $M(x)$, igual que en $M^{\rm crit}_{\RVM}$. Esto vale para las leyes A y B y para la multietapa.

**Qué falta.** Para que Perron vea $M$, el corte tiene que ser al menos $x$ en las alturas bajas, lo que significa $c>1$, pasada la resonancia. Ahí el aliasing ya no se puede acotar y hay que calcularlo: son los términos duales $\chi(s)\sum n^{s-1}$. Coincide con la prioridad I del traspaso, con $\theta\ge1$, y queda abierto.
