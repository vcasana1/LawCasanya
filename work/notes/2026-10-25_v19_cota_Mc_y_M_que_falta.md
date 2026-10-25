# v19: ¿tiene $M_C$ la cota $x^{1/2+\varepsilon}$? ¿y $M$? Qué falta exactamente

Nota de Claude, 25-oct-2026. Estudio de `CasanyaLawI_v19.tex` (adjunto), secciones "Finite Euler coefficients…" (l. 4499–4661) y "Three exact transfer targets" (l. 4662–4770), contrastadas con mi nota `2026-10-24_mertens_sintetico_reloj_casanya.md` (Teoremas A y B). Sin ejecuciones numéricas.

## 0. Qué cambia en v19 respecto a v18 (y es correcto)

Solo el Lema `long-cutoff-mean-square` y el Cor. `long-cutoff-shifted-endpoints` (l. 4091–4218): incorporan mi argumento de extremos elegidos por Montgomery–Vaughan. Verificado: el término de MV sin peso es $\pi(X)$; para $c=5/3$ el cociente cúbico es $(\log T)^{-5/2}$; los $a_j\in[T_j,\tfrac32T_j]$ se eligen a la vez para $X_{j-1}$ y $X_j$. Correcto, y bien delimitado: ventanas desplazadas, no $(T,2T]$.

## 1. Respuesta corta

| Objeto | ¿$\ll x^{1/2+\varepsilon}$? | Estado |
|---|---|---|
| $M_{C,X}$, $X$ **fijo**, lista de raíces exactas | **Sí**, para todo $x$, con constante que depende de $X$ | (T): Teorema B de mi nota + Teorema A |
| $M_{C,X}$, $X$ fijo, lista de **un paso** $\tau_k^X$ (el candidato que nombra v19) | No establecido | falta $J_X<\infty$ |
| $M_{C,X}$ **uniforme** en $X\ge x$ | No | es lo que falta; equivale en la práctica a la información de RH |
| $M$ | $\ll x^{1/2+\varepsilon}\iff$ RH | Littlewood; v19 Cor. `bothtransfersRH` da la implicación desde lo uniforme |

## 2. $M_{C,X}$ con $X$ fijo: la cota existe y es trivial, y por eso no dice nada

Para la lista de raíces exactas $\kappa^X_k=N_X^{-1}(k-\tfrac12)$ (definida para $t\ge t_0(X)$, donde $N_X=N_0+S_X$ es monótona), el Teorema A da, en $\Re s=\tfrac12+\sigma'$,

$$\varpi_XF_{C,X}-E_X^{-1}=E_X^{-1}\bigl[(1+w_X)^{-1}(1+\mathcal E_X)^{-1}-1\bigr]\ll_{X}t^{-\min(\sigma'/2,\delta)}\log t,$$

integrable contra $dt/|s|$. Luego $J_X(\sigma)<\infty$ (la hipótesis (6)/`eq:JMfixed` de v19 **está demostrada para esta lista**) y

$$\varpi_XM_{C,X}(x)=M_X^*(x)+\mathcal R_X(x),\qquad|\mathcal R_X|\le J_Xx^{1/2+\varepsilon},\quad\text{para todo }x\ge2 .$$

Y $M_X^*$ es una suma **finita**: $|M_X^*(x)|\le2^{\pi(X)}$ siempre, y $M_X^*(x)=\prod_{p\le X}(1-1)=0$ para $x\ge P(X)$. Por tanto

$$\boxed{M_{C,X}(x)=O_X\bigl(x^{1/2+\varepsilon}\bigr)\quad\text{para todo }x,}$$

con constante $\le(2^{\pi(X)}+J_X)/\varpi_X$. **Esto es un teorema, pero es vacío para RH:** la cota vale porque $M_X^*$ es finita, no porque $M_C$ sepa nada de $M$. En el tramo útil $x\le X$ se tiene $M_X^*=M^*$, y en ese tramo la cota $x^{1/2+\varepsilon}$ para $M_{C,X}$ es cierta **si y solo si** $|M(x)+\mathcal R_X(x)|\ll x^{1/2+\varepsilon}$, lo que no dice nada sin controlar $\mathcal R_X$.

v19 (Rem. tras `cor:bothtransfersRH`, y Prop. `reciprocalgap`) dice que la cota de $1/\zeta_{C,X}$ no se infiere de la posición de los ceros. Cierto en general; **pero para esta lista concreta sí está**, por el Teorema A, que usa la estructura del reloj (Poisson + TR de v26), no solo la posición de los ceros. Conviene que v20 lo diga: la hipótesis `eq:JMfixed` está demostrada para $X$ fijo con la lista de raíces exactas.

## 3. Aviso sobre el candidato de v19: la lista de un paso

v19 propone como candidato $\kappa_k^X=\tau_k^X=\tau_k-S_X(\tau_k)/\Lambda(\tau_k)$ (un paso de Newton), y dice que cumple las hipótesis de `prop:xiSynthetic`. Eso es cierto para la **construcción** de $\Xi_\kappa$. Pero para $J_X<\infty$ no basta:

- la raíz exacta y el paso de Newton difieren en $\kappa_k^{\rm exact}-\tau_k^X\ll_X\log^{-2}\tau_k$ (Newton de segundo orden: $F_X''\cdot(\text{paso})^2/\Lambda$, con paso $\ll\sqrt X/\log\tau$);
- un desplazamiento $\epsilon_k$ de los ceros cerca de la altura $t$ cambia $\log\zeta_\kappa(\sigma'+\tfrac12+it)$ en $\approx\sum_k\epsilon_k\,\Re\frac{1}{\ldots}$, que **sin cancelación** es $\ll\epsilon\,\Lambda(t)\log t\ll_X1/\log t$;
- y $\int^\infty\frac{dt}{t\log t}$ **diverge**.

Así que con la lista de un paso, $J_X<\infty$ exige demostrar cancelación en la suma de los residuos de Newton; no está hecho. Con la lista de raíces exactas no hace falta. **v20 debería nombrar la lista de raíces exactas** (la de mi nota, §1.3; es la del "identidad exacta para $Y$ fijo" que el autor pidió guardar el 21-oct) como candidato para `thm:PerronMfixed`, o añadir la hipótesis explícita de que $J_X<\infty$ para la lista de un paso.

## 4. Por qué la uniformidad en $X\ge x$ no sale de aquí: dos obstáculos, cuantificados

Para pasar de (2) a $M(x)\ll x^{1/2+\varepsilon}$ hace falta $J_X=x^{o(1)}$ con $X\ge x$. Dos cosas lo impiden con la construcción actual:

**(a) El umbral de monotonía.** La lista de raíces exactas solo existe para $t\ge t_0(X)$ con $\Lambda(t_0)\ge2A_X\asymp\sqrt X$, es decir

$$t_0(X)\asymp\exp\bigl(c\sqrt X\bigr).$$

Por debajo, la lista es convencional y $D_X=\varpi_XF_{C,X}-E_X^{-1}$ no es pequeño; esa zona aporta a $J_X$ del orden de $\int_1^{t_0}\frac{|D_X|}{t}dt\asymp\log t_0(X)\asymp\sqrt X$ (estimación, salvo cancelación que nadie ha demostrado). Con $X\ge x$ esto da $\mathcal R_X\gtrsim\sqrt x\cdot x^{1/2+\varepsilon}=x^{1+\varepsilon}$: **inútil**. v14 (Rem. `localization`) ya lo decía en otra forma: la localización por raíces exactas solo vale para $X\ll\log^2T$.

**(b) El régimen de alturas que Perron necesita.** El coeficiente $\mu(n)$ con $n\le x$ lo resuelve Perron a alturas $|t|\lesssim x$ (altura de truncación $U\asymp x^{1+\epsilon}$). Para tener $X\ge x$ a esas alturas hace falta $X\ge t$, es decir, exponente de corte $c\ge1$: **más allá de la resonancia $p\approx t/2\pi$**. Ahí:
- $N_X$ no es monótona ($|S_X'|\asymp\sqrt X\gg\Lambda$), así que no hay lista de raíces exactas y hay que usar el reloj de un paso o multietapa, con el problema de §3;
- el Teorema A′ (corte variable, mi nota del 24-oct) está probado en mecanismo solo para $c<1$; en $c\ge1$ el paso de aliasing deja de ser pequeño y aparecen exactamente los dos canales de v15–v19 (`cor:resonancechannels`): el alias de cociente $p/q\asymp N$ y el de producto $pq\asymp N^2$.

**Y lo de fondo.** En $\sigma=\tfrac12+\varepsilon$ y altura $t$, con $X\ge t^A$, el polinomio $\log E_X(s)=\sum_{p\le X}p^{-s}+\dots$ es, por la fórmula explícita, $\log\zeta(s)$ más una suma sobre ceros $\sum_\rho X^{\rho-s}/(\rho-s)$; un cero con $\beta>\sigma$ hace crecer esa suma con $X$. Controlar $E_X^{-1}$ uniformemente en $X$ grande a altura $t$ en $\sigma>\tfrac12$ **es** controlar los ceros a la derecha de $\sigma$. Por eso la uniformidad en $X\ge x$ no puede salir de la aritmética de $E_X$ sola: la información tiene que entrar por las ordenadas (Teorema L / bloques), como ya decía la nota de la vía M.

## 5. Lo que falta, en orden

1. **Inmediato (redacción, v20):** nombrar la lista de raíces exactas como candidato de `thm:PerronMfixed`, con $J_X<\infty$ demostrado (Teorema A); señalar que con la lista de un paso falta la cancelación de §3; y enunciar explícitamente $M_{C,X}=O_X(x^{1/2+\varepsilon})$ para todo $x$ con la explicación de por qué es vacío.
2. **Cuantificar $J_X$.** Demostrar la cota inferior $J_X\gg\log t_0(X)$ de (a) o refutarla eligiendo la lista baja con cancelación. Si se confirma, la ruta "corte fijo + uniformidad" queda cerrada como tal y hay que ir a (3).
3. **Corte variable en $c\ge1$ con Perron.** Es el mismo objeto que en $E_T\to0$: el reloj con primos hasta $t^{c}$, $c\ge1$, y los dos canales de alias sumados. Para $M$ hace falta además la versión de Perron de A′ (mi Teorema B′), cuyo resto no está acotado.
4. **Alternativa que evita $1/\zeta_C$:** no pasar por $M_C$. Usar el Teorema L (localización $|u_k|<\tfrac12$ para todo $k$ alto) ⇒ RH ⇒ $M\ll x^{1/2+\varepsilon}$. Es la vía que no necesita ni $J_X$ ni la uniformidad; necesita el control puntual del defecto, con corte $c(k)\to\infty$.

**Conclusión.** $M_C$ tiene la cota $x^{1/2+\varepsilon}$ para cada $X$ fijo (con la lista correcta), y esa cota no aporta nada sobre $M$ porque su constante crece con $X$ al menos como $\exp$ de algo del orden de $\sqrt X$ en el peor caso y, en el mejor caso imaginable, exige información sobre los ceros a la derecha de $\tfrac12$. $M$ tiene la cota si y solo si RH. Lo que falta no es un lema de Perron, sino el reloj más allá de la resonancia.
