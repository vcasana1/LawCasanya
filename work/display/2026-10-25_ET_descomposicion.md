# $E_T\to0$: descomposición exacta en aproximación + multiplicidad

Respuestas de Claude, 25-oct-2026. Nota completa: `work/notes/2026-10-25_ET_a_cero_estado.md`.

## A. Respuesta a "demuestra $E_T\to0$"

No puedo demostrar $E_T\to0$, y conviene decir por qué. Por el teorema de bloques, $E_T\to0$ implica que el 100 % asintótico de los ceros es simple y está en la recta. Eso va más allá de lo que se sabe incluso bajo RH: Montgomery da $\ge2/3$ de ceros simples con RH sola, y "casi todos simples" necesita además la conjetura de correlación de pares. Ningún teorema disponible da algo tan fuerte.

**Forma equivalente exacta, sin ceros en el integrando.** La identidad de v14 con $j=1$ da

$$\sum u_k^2=\int(N-F)^2F'\,dt-\frac{n_{\rm int}}{12}-\mathcal B_1,$$

con $n_{\rm int}$ el número de índices interiores y $\mathcal B_1$ los dos términos de borde. Por tanto

$$E_T\to0\iff\frac1{M_T}\int(N-F)^2\,dF=\frac1{12}+o(1),$$

donde $N-F=\theta/\pi+1+S-F$ y $M_T$ es el número de ceros de la ventana. Es decir, el error de conteo tiene que ser, en media cuadrática, exactamente el diente de sierra puro. Todo exceso sobre $\tfrac1{12}$ por cero es $E_T$.

**Lo que sí está demostrado (v14), para $F_X=N_0+S_X$:**
- **Con $X$ fijo:** $E_T\sim\frac1{2\pi^2}\log\log T\to\infty$.
- **Con $\log X/\log T\to0$:** $E_T\to\infty$.
- **Con $X=T^c$ y $c$ fijo pequeño:** el Thm main es una cota en las dos direcciones,

  $$E_T\ \ge\ \frac1{2\pi^2}\log\frac1c-C\Bigl(1+\sqrt{\log\tfrac1c}\Bigr)>0\qquad(c<c_1).$$

  Para esos $c$, $E_T$ no tiende a 0. La constante $c_1>0$ es absoluta pero no explícita.
- **Para $c_1\le c\le\tfrac12$** no está decidido: es la Pregunta 13.1 de v14. **Para $c>\tfrac12$** no hay teoría.

**Qué haría falta.** En el modelo, que no está demostrado, un corte con $c$ fijo deja $E_T$ en una constante, del orden de $0.035+K$ en $c=\tfrac12$. Eso daría un porcentaje, no el 100 %. Para $E_T\to0$ hace falta un corte por índice con $c(k)\to\infty$, es decir, primos más allá de la resonancia. Es el mismo requisito que en la vía M.

**Sobre el texto de ChatGPT pegado por el autor:** sus números están bien.
- $1-4\cdot0.0351=85.96\,\%$.
- $1-4E_T$ con los valores de la tabla de v14 da entre $95.12\,\%$ y $95.63\,\%$.
- Su conclusión también es correcta: asintóticamente, con lo demostrado, el método certifica hoy un 0 %. El objetivo realista es $\limsup E_T<\tfrac14$, no $E_T\to0$.

## B. Respuesta a "¿y qué? ¿eso es problema?"

No, no es ningún problema. Lo planteé mal: que algo vaya más allá de lo conocido bajo RH solo significa que hace falta un ingrediente nuevo, no que sea imposible. Lo que de verdad importa es qué parte de $E_T$ depende del reloj y qué parte no, y eso tiene una respuesta exacta.

**Descomposición exacta (demostrada).** Para cada ordenada distinta $\gamma$ de la ventana, sea $m_\gamma$ su multiplicidad y $N^*(\gamma)=\tfrac12\bigl(N(\gamma^-)+N(\gamma^+)\bigr)$ el conteo en el punto medio del salto. Dentro de un bloque, $u=(N^*-F)+\ell-\frac{m_\gamma-1}2$. Por la descomposición de la varianza,

$$\sum_k u_k^2=\underbrace{\sum_\gamma m_\gamma\bigl(N^*(\gamma)-F(\gamma)\bigr)^2}_{\text{aproximación (depende de }F)}+\underbrace{\sum_\gamma\frac{m_\gamma(m_\gamma^2-1)}{12}}_{\text{multiplicidad (no depende de }F)} .$$

Esto tiene tres consecuencias:

1. **El teorema de bloques sale de aquí directamente.** El término de multiplicidad ya es $\ge B_T/4$, y $F$ solo añade un término no negativo.
2. **$E_T\to0$ son dos cosas a la vez:**
   - (a) que el reloj aproxime el conteo en el punto medio en las ordenadas;
   - (b) que casi ninguna ordenada esté repetida.
3. **(b) no se mejora mejorando $F$; solo sale por la integral en $t$.** Con la identidad de v14,

   $$\frac1M\sum_\gamma\frac{m_\gamma(m_\gamma^2-1)}{12}\le\frac1M\int(N-F)^2\,dF-\frac1{12}+\frac{|\mathcal B_1|}M ,$$

   donde $M$ es el número de ceros de la ventana y $\mathcal B_1$ los dos términos de borde. Así que lo que hay que demostrar es

   $$\frac1M\int\bigl(\theta/\pi+1+S-F\bigr)^2\,dF\ \le\ \frac1{12}+o(1).$$

   Es un enunciado sobre $\arg\zeta$ en la recta: quitada la parte prima, su media cuadrática tiene que ser exactamente la del diente de sierra.

**Dónde está la dificultad real.** Hay que conocer la constante de segundo orden de $\frac1T\int S^2$ con precisión $o(1)$. En la fórmula de Goldston (bajo RH; sin cotejar en la biblioteca) esa constante contiene $\int_1^\infty F(\alpha)\alpha^{-2}\,d\alpha$, y la media de $F(\alpha)$ para $\alpha$ grande es precisamente la multiplicidad media. Es la información de (b) vista desde el lado de $t$.

**Paso siguiente.** Tomar $F$ con corte por índice $c(k)\to\infty$, usando una fase de primos amortiguada tipo Selberg, porque la fase de Euler pura sobre la recta no converge cuando $X\gg t$. Después, calcular $\frac1M\int(N-F)^2\,dF$ hasta $o(1)$. Por la descomposición, ese número da a la vez el error del reloj y la multiplicidad.
