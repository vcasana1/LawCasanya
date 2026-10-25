# $E_T=\langle u_k(F)^2\rangle_T\to0$: qué implica, forma equivalente exacta y qué se puede demostrar hoy

Nota de Claude, 25-oct-2026. Sin ejecuciones numéricas. Ningún manuscrito cambiado. Notación:
- $u_k(F)=k-\tfrac12-F(\gamma_k)$ y $E_T=\langle u_k(F)^2\rangle_{T<\gamma_k\le2T}$;
- $N(t)=\theta(t)/\pi+1+S(t)$.

## 1. Lo que implicaría (T)

Por el teorema de bloques, $B_T\le4\sum u_k^2$. Si $E_T\to0$, el **100 % asintótico** de los ceros es simple y está en la recta.

Eso es más que todo lo conocido:
- incondicionalmente, el récord es en torno al 40 % de ceros simples y en la recta (sin cotejar en la biblioteca);
- bajo RH sola, Montgomery da ≥ 2/3 de ceros simples;
- "casi todos simples" se obtiene con RH más la conjetura de correlación de pares.

**Por tanto $E_T\to0$ no se puede demostrar con los teoremas de que disponemos.** Es un objetivo más fuerte que lo que se sabe bajo RH sola.

## 2. Forma equivalente exacta, sin ceros en el integrando (T)

Se toma el Teorema `identity_general` de v14 con $j=1$, entre las ordenadas extremas de la ventana:

$$\sum u_k^2=\int(N-F)^2F'\,dt-\frac{n_{\rm int}}{12}-\mathcal B_1 .$$

Por tanto

$$E_T\to0\iff\frac1{M_T}\int_{\gamma_{k_1}}^{\gamma_{k_2}}\bigl(N-F\bigr)^2\,dF=\frac1{12}+o(1),$$

con $N-F=\theta/\pi+1+S-F$, siempre que los bordes sean $o(M_T)$.

En palabras: el error de conteo $\arg\zeta$ frente al modelo sin ceros tiene que ser, en media cuadrática con peso $dF$, **exactamente el diente de sierra puro**, que aporta $\tfrac1{12}$ por cero. Todo exceso sobre $\tfrac1{12}$ es $E_T$.

## 3. Lo que sí se demuestra hoy: cortes que no pueden dar $E_T\to0$ (T, v14)

Para $F=F_X=N_0+S_X$:
- **$X$ fijo** (v14, Cor. `fixed_cutoff`): $E_T=\frac1{2\pi^2}\log\log T+O_X(\sqrt{\log\log T})\to\infty$.
- **$X=T^c$ con $c\le\tfrac12$ fijo** (v14, Thm `main`, que es una cota en las dos direcciones):
$$E_T\ \ge\ \frac1{2\pi^2}\log\frac1c-C\Bigl(1+\sqrt{\log\tfrac1c}\Bigr).$$
Esto es $>0$ para $c<c_1$, con $c_1>0$ absoluta pero no explícita. Para esos $c$, $\liminf E_T>0$.
- **$\log X/\log T\to0$** (v14, Cor. `dichotomy`): $E_T\to\infty$.

**Necesario dentro de la familia $F_X$:** el exponente de corte no puede tender a 0 ni quedarse por debajo de $c_1$. Para $c_1\le c\le\tfrac12$ la teoría no decide si $\liminf E_T$ es 0 o positivo; es la Pregunta 13.1 de v14. Para $c>\tfrac12$ no hay teoría.

## 4. Qué haría falta

En el modelo (RH más correlación de pares; no demostrado), la varianza del defecto con corte $T^c$ decrece cuando $c$ crece más allá de 1. Por tanto $E_T\to0$ exigiría un corte por índice $X_k=(\tau_k/2\pi)^{c(k)}$ con $c(k)\to\infty$, como en la nota de la vía M.

Un corte con $c$ fijo da como mucho $E_T\to$ una constante. Por los datos, esa constante sería $\approx0.035+K$ en $c=\tfrac12$; con eso se obtendría un porcentaje, no el 100 %.

**Objetivo intermedio:** $\limsup E_T<\tfrac14$, que da una proporción positiva incondicional por el reloj. Es más realista que $E_T\to0$, pero sigue abierto.

## 5. Corrección de enfoque y descomposición exacta de $E_T$ (T)

Que $E_T\to0$ supere lo conocido bajo RH no es un obstáculo; solo indica que hace falta un ingrediente nuevo. Lo que importa es **qué parte de $E_T$ depende del reloj y qué parte no**. Eso lo da la identidad siguiente.

**Descomposición.** Sean $\gamma$ las ordenadas distintas de la ventana, $m_\gamma$ su multiplicidad (contando los ceros de todas las abscisas) y $N^*(\gamma)=\frac12\bigl(N(\gamma^-)+N(\gamma^+)\bigr)$ el conteo en el punto medio del salto. Dentro de un bloque, $u=N^*(\gamma)-F(\gamma)+\ell-\frac{m_\gamma-1}2$ para $\ell=0,\dots,m_\gamma-1$. Por la descomposición de la varianza:

$$\boxed{\ \sum_{k\in\mathcal I_T}u_k^2=\underbrace{\sum_\gamma m_\gamma\bigl(N^*(\gamma)-F(\gamma)\bigr)^2}_{\text{aproximación: depende de }F}\;+\;\underbrace{\sum_\gamma\frac{m_\gamma(m_\gamma^2-1)}{12}}_{\text{multiplicidad: no depende de }F}\ }$$

**Consecuencias.**

1. El teorema de bloques $B_T\le4\sum u^2$ sale de aquí directamente: el término de multiplicidad ya es $\ge B_T/4$. La función $F$ solo añade un término no negativo.
2. $E_T\to0$ equivale a dos cosas a la vez:
   - (a) $\frac1M\sum_\gamma m_\gamma(N^*-F)^2\to0$, que es el problema del reloj: aproximar el conteo en el punto medio en las ordenadas;
   - (b) $\frac1M\sum_\gamma m_\gamma(m_\gamma^2-1)\to0$, es decir, casi todas las ordenadas sin repetir.
3. Ninguna mejora de $F$ toca (b). (b) solo se obtiene por la vía de la integral: con la identidad de v14,
$$\frac1M\sum_\gamma\frac{m_\gamma(m_\gamma^2-1)}{12}\ \le\ \frac1M\int(N-F)^2\,dF-\frac1{12}+\frac{|\mathcal B_1|}M .$$
   Así que lo que hay que demostrar es una **cota superior asintótica** de la media de $(\theta/\pi+1+S-F)^2$ con peso $dF$:
$$\frac1M\int(N-F)^2\,dF\ \le\ \frac1{12}+o(1).$$
   Es un enunciado sobre $\arg\zeta$ en la recta: su media cuadrática menos la parte prima tiene que ser **exactamente** la del diente de sierra.
4. Por qué es el punto difícil: requiere la constante de segundo orden de $\frac1T\int S^2$ con precisión $o(1)$, además de la parte prima. En la fórmula de Goldston (bajo RH; sin cotejar en la biblioteca), esa constante contiene $\int_1^\infty F(\alpha)\alpha^{-2}d\alpha$, y la media de $F(\alpha)$ para $\alpha$ grande es la multiplicidad media. Es la misma información de (b) vista desde el lado de $t$.

**El paso siguiente concreto:**
- elegir $F$ con corte por índice $c(k)\to\infty$, con la fase de primos amortiguada tipo Selberg ($n^{-\sigma_x}$), porque la fase de Euler pura sobre la recta no converge cuando $X\gg t$;
- calcular $\frac1M\int(N-F)^2dF$ hasta $o(1)$. Por la descomposición, el resultado dirá a la vez cuánto vale la aproximación y cuánto la multiplicidad.
