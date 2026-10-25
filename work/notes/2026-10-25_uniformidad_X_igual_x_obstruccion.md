# Uniformidad en $X=x$ y control independiente de $M^N_{C,x}(x)$: qué se puede demostrar y dónde está la obstrucción exacta

Nota de Claude, 25-oct-2026. Continúa `2026-10-25_texto_v20_PerronMfixed_incondicional.md`. Sin ejecuciones numéricas. Resultado: **la integrabilidad a $X$ fijo no se convierte en cotas uniformes para $X=x$ con estas herramientas, y se demuestra por qué**: las constantes crecen como $\exp(cX^{1/2+Y})$ por construcción (§1), y cualquier cota uniforme del tipo necesario en un solo punto ya implica un semiplano sin ceros (§2). Además, en el rango de alturas que Perron usa, la zeta sintética con $X=x$ está en régimen de aliasing (§3). Lo que sí queda: un teorema de equivalencia y una proposición de incompatibilidad.

Notación como en el texto para v20: $s=\tfrac12+\sigma'+it$, $\mathscr E_X$, $\zeta^{\rm ex}_{C,X}$, $\zeta^N_{C,X}$, $J_X$, $M^*_X$.

## 1. Dependencia en $X$ de todas las constantes del Corolario (T)

1. **Umbral de la banda.** Lema 1 exige $\Lambda(\tau')\ge2A_X(Y)$, $Y>\sigma'$, y $A_X(Y)=\frac1\pi\sum_{p\le X}\log p\,\frac{p^{Y-1/2}}{1-p^{Y-1/2}}=\frac{(1+o(1))X^{Y+1/2}}{\pi(Y+\tfrac12)}$. Luego
$$\log\frac{\tau'(X)}{2\pi}\ \ge\ \frac{4X^{Y+1/2}}{Y+\tfrac12},\qquad\text{es decir}\qquad \tau'(X)=\exp\bigl(cX^{1/2+Y}\bigr),\ c\ge4/(Y+\tfrac12)>4 .$$
Para $t<\tau'(X)$ el Teorema A no dice nada: ni $1+w_X$ es $1+o(1)$ ni el término $\mathcal E_X$ está controlado.

2. **Tamaño de $\mathscr E_X^{-1}$ en la recta.** $|\mathscr E_X^{-1}(\sigma+it)|\le\prod_{p\le X}(1+p^{-\sigma})\le\exp\bigl(\frac{(2+o(1))X^{1/2-\sigma'}}{\log X}\bigr)$, y esta cota se alcanza salvo factor $X^{o(1)}$ en el exponente para algún $t$ (Kronecker).

3. **Constantes de Theorem C.** $A_0\asymp\sqrt X/\log X$, $A_2\asymp\sqrt X\log X$, así que $C_1(X)\asymp X\log^2X$ y $C_2(X,\sigma')\ll X^{3/2+o(1)}/\sigma'$. Benignas: polinomiales. **El problema no está en el paso de Newton.**

4. **Consecuencia para $J_X$.** $J_X=J_{\rm low}+J_{\rm high}$ con $J_{\rm high}=\frac1{2\pi}\int_{|t|\ge\tau'}\ll_{\sigma'}1+C_2(X)$ y
$$J_{\rm low}=\frac1{2\pi}\int_{|t|<\tau'(X)}\frac{|D_X|}{|s|}dt\ \le\ \log\tau'(X)\cdot\sup_{|t|<\tau'}|D_X|\ \ll\ X^{1/2+Y}\Bigl(\sup_{|t|<\tau'}\Bigl|\frac{\varpi_X}{\zeta_{C,X}}\Bigr|+e^{2X^{1/2-\sigma'}/\log X}\Bigr).$$
El supremo de $|1/\zeta_{C,X}|$ en $|t|<\tau'$ **no tiene cota demostrada**: exigiría una cota inferior de $|\Xi_\kappa|$ fuera de sus ceros a alturas donde el producto aún no ha "convergido" a $\mathscr E_X$. La única cota disponible es la trivial de la banda ($|1+w_X|\ge1-|w_X|$ no vale: para $t<\tau'$ no se sabe que $|w_X|<1$).

Con $X=x$: aunque $\sup|1/\zeta_{C,x}|$ fuera $x^{O(1)}$, se tendría $|\mathcal R_x(x)|\le J_xx^{1/2+\sigma'}$ con $J_x\ge$ (nada mejor que) $e^{2x^{1/2-\sigma'}/\log x}$: **vacío**. Y esto no es pesimismo de la prueba: §3 muestra que $D_x$ no es pequeño en $|t|\le x$.

## 2. Teorema de equivalencia: una cota uniforme en un solo punto ya es un semiplano sin ceros (T)

**Teorema E.** Sea $s_0=\sigma_0+it_0$ con $\tfrac12<\sigma_0<1$. Si existe $C$ con
$$|\log\mathscr E_X(s_0)|\le C\qquad\text{para todo }X\ge2,$$
entonces $\zeta(s)\ne0$ para $\Re s>\sigma_0$ (y, por la ecuación funcional, para $\Re s<1-\sigma_0$).

*Prueba.* $\log\mathscr E_X(s_0)=\sum_{p\le X}\sum_{m\ge1}\frac{p^{-ms_0}}m=\sum_{n\le X}\frac{\Lambda(n)}{\log n}n^{-s_0}+\sum_{p\le X<p^m}\frac{p^{-ms_0}}m$. La segunda suma es $\le\sum_{p\le X}\frac{p^{-2\sigma_0}}{1-p^{-\sigma_0}}\ll1$. Así $A(X):=\sum_{n\le X}\frac{\Lambda(n)}{\log n}n^{-s_0}$ está acotado para todo $X$. Por sumación parcial, $\sum_n\frac{\Lambda(n)}{\log n}n^{-s_0-u}=u\int_1^\infty A(X)X^{-u-1}dX$ converge para $\Re u>0$, luego la serie de Dirichlet $\sum\frac{\Lambda(n)}{\log n}n^{-w}=\log\zeta(w)$ (para $\Re w>1$) converge en el semiplano $\Re w>\sigma_0$ y define allí una función holomorfa que coincide con $\log\zeta$ en $\Re w>1$. Por tanto $\log\zeta$ se prolonga holomorfa a $\Re w>\sigma_0$: $\zeta$ no tiene ceros ni polos en $\Re w>\sigma_0$ salvo $w=1$. $\square$

**Lectura.** La hipótesis uniforme natural para la vía M ("$|D_X|$ integrable uniformemente en $X\ge x$") contiene la acotación uniforme de $\mathscr E_X^{-1}$ en la recta. Acotación superior de $|\mathscr E_X^{-1}|$ es acotación inferior de $\Re\log\mathscr E_X$; la acotación de $|M_{C,X}|$ (primera hipótesis de `cor:bothtransfersRH`) exige además control de $|1/\zeta_{C,X}|$, que en el rango $t\ge\tau'$ es $|\mathscr E_X^{-1}||1+w_X|^{-1}$. Cualquier versión **bilateral** uniforme en un punto da el Teorema E. No es sorprendente: es la versión en productos de Euler finitos del teorema clásico "la serie de $1/\zeta$ converge en $\Re s>\tfrac12$ ⇔ RH". **Luego "cotas uniformes para $X=x$" no es un paso intermedio hacia RH: es RH en otra forma.**

## 3. El régimen de alturas de Perron con $X=x$ es el régimen de aliasing (T en la forma demostrada; modelo en la forma precisa)

Por Theorem A, (2.3): para $t\ge\tau'(X)$,
$$\zeta_{C,X}(s)=\varpi_X\bigl[\mathscr E_X(s)+\chi(s)\mathscr E_X(1-s)\bigr]+O(t^{-Y/2}\log t),\qquad w_X=\chi(s)\frac{\mathscr E_X(1-s)}{\mathscr E_X(s)}(1+O(t^{-1})).$$
Exactamente, para todo $t$: $|w_X(s)|=|\chi(s)|\,\bigl|\mathscr E_X(1-s)/\mathscr E_X(s)\bigr|(1+O(1/t))$ con $|\chi(\tfrac12+\sigma'+it)|\asymp(t/2\pi)^{-\sigma'}$, y
$$\log\Bigl|\frac{\mathscr E_X(1-s)}{\mathscr E_X(s)}\Bigr|=\Re\sum_{p\le X}\bigl(p^{-1/2+\sigma'}-p^{-1/2-\sigma'}\bigr)p^{-it}+O(1).$$
La media cuadrática en $t$ de la suma es $\asymp\sum_{p\le X}p^{-1+2\sigma'}\asymp X^{2\sigma'}/\log X$. Así, para $X=x$ y $|t|\le x^{1+\epsilon}$:
- el factor $|\chi|$ vale como mucho $x^{-\sigma'(1+\epsilon)}$,
- el cociente de productos vale $\exp(\pm x^{\sigma'+o(1)})$ en una proporción positiva de $t$.

**Conclusión (demostrada en lo que afirma):** en el rango $|t|\le x^{1+\epsilon}$, $|w_x(s)|$ toma valores $\ge1$ (de hecho $\ge e^{x^{\sigma'-o(1)}}$) en un conjunto de $t$ de medida positiva. Allí, si vale la forma (2.3) —que **no está demostrada** para $t<\tau'(x)$—, $\zeta_{C,x}(s)\approx\varpi\chi\mathscr E_x(1-s)$ y $1/\zeta_{C,x}$ no se parece a $\mathscr E_x^{-1}$ en absoluto: $D_x$ es del tamaño de $\mathscr E_x^{-1}$, no pequeño. Sin la forma (2.3), lo que sí se sabe es que la prueba de Theorem A no se aplica. En ambos casos, el "control independiente" de $M^N_{C,x}(x)$ por Perron en $|t|\le x^{1+\epsilon}$ exige cotas inferiores de $|\mathscr E_x(s)+\chi\mathscr E_x(1-s)|$ (o de $|\Xi_\kappa|$) que nadie tiene y que el modelo niega.

Esto es exactamente la observación de Gonek (2012, §5, p. 2169; biblioteca 125): $P_X+\chi\overline{P_X}$ modela $\zeta$ a altura $t$ solo si $X\lesssim\sqrt{t/2\pi}$ (el rango de la ecuación funcional aproximada); con $X\gg\sqrt t$ el término $\chi\overline{P_X}$ sobreincluye primos y el modelo deja de valer.

## 4. Proposición de incompatibilidad (T)

Para que la identidad friable cubra $n\le x$ hace falta $X\ge x$. Para que Perron resuelva $\mu(n)$, $n\le x$, hace falta integrar en $|t|\le U$ con $U\ge x^{1+\epsilon}$ (el error de truncación es $\ll x^{\sigma}\sum_{d|P(X)}d^{-\sigma}/(U|\log(x/d)|)$, y con $X\ge x$ la suma vale $e^{(2+o(1))X^{1/2-\sigma'}/\log X}$, lo que empuja $U$ aún más arriba, $U\ge e^{cX^{1/2-\sigma'}}$). Para que la transición del Teorema A esté demostrada hace falta $t\ge\tau'(X)=e^{cX^{1/2+Y}}$. Por tanto:

$$\boxed{\ \text{heights de Perron: }|t|\le U\quad\text{y}\quad\text{Teorema A: }|t|\ge e^{cX^{1/2+Y}}\ \text{ con }X\ge x\ \Longrightarrow\ U\ge e^{cx^{1/2+Y}} .\ }$$

Con una altura de truncación tan grande, el error de Perron es controlable (es $\ll x^{\sigma}e^{2x^{1/2-\sigma'}/\log x}/U\to0$) **pero** $J_{\rm low}$ (§1.4) acumula $\int_{|t|<\tau'}|D_X|/|s|$, que es $\log\tau'$ veces el tamaño típico de $|D_X|$ en esa zona, y ese tamaño es el de $\mathscr E_X^{-1}$ (§3). Es decir: no hay elección de $U$ que evite integrar $D_X$ en la zona de aliasing. **La ruta "producto de Euler finito de corte $X\ge x$ + Perron" no puede cerrar con un solo corte fijo.** No es una limitación de la prueba: es la estructura $\mathscr E_X(s)+\chi\mathscr E_X(1-s)$.

## 5. Lo que queda, y es lo mismo que en las otras dos vías

El corte tiene que depender de la altura, $X(t)\lesssim\sqrt{t/2\pi}$ para que la transición valga ($c\le\tfrac12$ en el reloj, que es donde está la teoría de v14), y entonces la identidad friable cubre solo $n\le X(t)\le\sqrt t$: Perron resuelve $\mu(n)$ a alturas $t\lesssim n$, donde $X(t)\le\sqrt n<n$. **Los $n\le x$ nunca están dentro del corte a las alturas en que Perron los necesita.** Es el contenido de la nota de consecuencias (§4.3) y de `prop:notanalytic` de v15–v19 (un corte en altura no es holomorfo), ahora con los exponentes exactos: la cola de Möbius rugosa $\sum_{P^+(n)>X(|t|)}\mu(n)n^{-s}$ es lo único que separa $M_C$ de $M$, y su Perron es $M(x)-M_{\sqrt{\cdot}}^*(x)$, es decir, la propia $M$ sobre los $n$ con un factor primo $>\sqrt{\text{altura}}$: no hay ganancia.

Por tanto, con la vía M lo único demostrable sin información de ceros es lo que ya está: a $X$ fijo, $M_{C,X}=\varpi^{-1}M_X^*+O_X(x^{1/2+\sigma'})$. La información tiene que entrar por las ordenadas (Teorema L / bloques / $E_T$), donde el corte por índice $c(k)\to\infty$ no choca con ninguna transición analítica porque no hay que invertir ninguna transformada.

## 6. Resumen

| Pregunta | Respuesta |
|---|---|
| ¿Cotas uniformes en $X=x$ a partir de la integrabilidad? | No. Las constantes de la prueba son $e^{cX^{1/2+Y}}$ (§1), y cualquier cota bilateral uniforme en un punto implica un semiplano sin ceros (Teorema E, §2). |
| ¿Control independiente de $M^N_{C,x}(x)$? | No. En $|t|\le x^{1+\epsilon}$ con $X=x$, $|w_x|\ge1$ en medida positiva (§3, demostrado); allí $1/\zeta_{C,x}$ no es $\approx\mathscr E_x^{-1}$ y faltan cotas inferiores de $|\Xi_\kappa|$ que el modelo niega. |
| ¿Hay algún corte fijo que funcione? | No (§4). |
| ¿Qué sí es teorema? | Teorema E; la proposición de incompatibilidad; y a $X$ fijo, todo el Corolario del texto para v20. |
