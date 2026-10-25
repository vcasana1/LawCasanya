# $J_X^{(1)}$ para la lista de un paso de v19: diverge; qué paso de Newton sí da $J_X<\infty$

Nota de Claude, 25-oct-2026. Sin ejecuciones numéricas. $X\ge2$ fijo; $\Lambda=\Lambda(\tau)$; $N_X=N_0+S_X$ monótona para $\tau\ge t_0(X)$. Listas:
- raíces exactas $\kappa^{\rm ex}_k$: $N_X(\kappa^{\rm ex}_k)=k-\tfrac12$ (mi nota del 24-oct, §1.3; Teorema A ⇒ $J^{\rm ex}_X<\infty$);
- un paso (v19, `thm:PerronMfixed`): $\kappa^{(1)}_k=\tau_k-S_X(\tau_k)/\Lambda(\tau_k)$.

$s=\tfrac12+\sigma'+it$, $0<\sigma'<\tfrac12$ fijo. $D^{(\cdot)}_X=\varpi^{(\cdot)}_XF^{(\cdot)}_{C,X}-E_X^{-1}$ y $J^{(\cdot)}_X=\frac1{2\pi}\int|D^{(\cdot)}_X|\,dt/|s|$.

## 1. El residuo de Newton es de primer orden y oscilante (T)

Con $\kappa^{\rm ex}_k=\tau_k-h$: $S_X(\tau_k)=hN_X'(\tau_k)-\tfrac{h^2}2N_X''(\xi)$, $N_X'=\Lambda+S_X'$, $N_X''=O_X(1)$. Luego

$$h=\frac{S_X}{\Lambda}\Bigl(1+\frac{S_X'}{\Lambda}\Bigr)^{-1}+O_X(\Lambda^{-3})=\frac{S_X}{\Lambda}-\frac{S_XS_X'}{\Lambda^2}+O_X(\Lambda^{-3}),$$

$$\boxed{\ \epsilon_k:=\kappa^{(1)}_k-\kappa^{\rm ex}_k=-\frac{S_XS_X'}{\Lambda^2}(\tau_k)+O_X(\Lambda^{-3})=-\frac{(S_X^2)'(\tau_k)}{2\Lambda(\tau_k)^2}+O_X(\Lambda^{-3}).\ }$$

El paso de v19 usa $\Lambda$ en vez de $N_X'$: por eso el error es de **primer** orden en $S_X'/\Lambda$, no de segundo. $(S_X^2)'$ es un polinomio trigonométrico real **sin término constante**, con frecuencias $\omega=\pm m\log p\pm m'\log q$, $0<|\omega|\le2\log X$ (fijas).

## 2. Efecto sobre $\log\zeta_C$ (T salvo el paso 2c)

Por `thm:synthetictransport` de v15, o directamente del producto, con $z=s-\tfrac12$:

$$\Delta(s):=\log\zeta^{(1)}_{C,X}(s)-\log\zeta^{\rm ex}_{C,X}(s)-\mathrm{cte}=\sum_k\Bigl[\log\frac{(\kappa^{(1)}_k)^2+z^2}{(\kappa^{\rm ex}_k)^2+z^2}-\log\frac{(\kappa^{(1)}_k)^2}{(\kappa^{\rm ex}_k)^2}\Bigr].$$

**2a. Linealización.** Término $k$ $=\epsilon_k\,\dfrac{-2z^2}{\kappa_k(\kappa_k^2+z^2)}+O(\epsilon_k^2/|\kappa_k-t+i\sigma'|^2)$. Con $\kappa^2+z^2=(\kappa+t-i\sigma')(\kappa-t+i\sigma')$ y $z^2=-t^2+O(t)$, para $\kappa\asymp t$ el núcleo es $\dfrac{1}{\kappa-t+i\sigma'}(1+O(|\kappa-t|/t))$. Los cuadráticos suman $\ll_X\Lambda^{-4}\cdot\Lambda/\sigma'=O(\log^{-3}t)$: integrables.

**2b. Tamaño absoluto.** $\sum_k\frac{|\epsilon_k|}{|\kappa_k-t|+\sigma'}\ll_X\Lambda^{-2}\cdot\Lambda\log t=O_X(1)$ (la suma $\sum_{1\le|\kappa-t|\le t}1/|\kappa-t|\asymp\Lambda\log t$). **Sin cancelación, $\Delta$ ni siquiera tiende a 0.** El resto $O_X(\Lambda^{-3})$ de $\epsilon_k$ aporta $O_X(\log^{-2}t)$, integrable contra $dt/t$.

**2c. Término principal con la cancelación.** Sustituyendo la suma sobre el reloj por la integral ($\sum_kg(\tau_k)\approx\int g\,\Lambda\,d\tau$; los alias de Poisson $e^{2\pi imN_0}$ contra $e^{i\omega\tau}$ no tienen punto estacionario porque $m\Lambda\gg|\omega|/2\pi$, y aportan $O_X(1/(\Lambda t))$ — *este es el único paso que queda por escribir con mayorantes*):

$$\Delta(s)\approx-\frac1{2\Lambda(t)}\int_{\mathbb R}\frac{(S_X^2)'(\tau)}{\tau-(t-i\sigma')}\,d\tau=-\frac{\pi i}{\Lambda(t)}\sum_{\omega<0}c_\omega\,e^{\omega\sigma'}e^{i\omega t},\qquad \tfrac12(S_X^2)'=\sum_\omega c_\omega e^{i\omega\tau},$$

por $\int_{\mathbb R}\frac{e^{i\omega\tau}}{\tau-w}d\tau=-2\pi ie^{i\omega w}\mathbf 1_{\omega<0}$ para $\Im w<0$. Como $S_X^2$ es real y no constante, tiene frecuencias negativas: $P^-(t):=\sum_{\omega<0}c_\omega e^{\omega\sigma'}e^{i\omega t}\not\equiv0$.

**Conclusión de 2.**

$$\boxed{\ \Delta(\tfrac12+\sigma'+it)=-\frac{\pi i\,P^-(t)}{\Lambda(t)}+O_X\bigl(\log^{-2}t\bigr),\qquad P^-\ \text{polinomio trigonométrico no nulo}.\ }$$

## 3. $J^{(1)}_X=\infty$ (T salvo 2c)

$D^{(1)}_X=E_X^{-1}\bigl[(1+w)^{-1}(1+\mathcal E)^{-1}e^{\Delta}-1\bigr]\cdot\varpi^{(1)}/\varpi^{\rm ex}$ con la normalización ajustada. Como $w,\mathcal E\to0$ con potencia de $t$ (Teorema A) y $\Delta\to0$,

$$|D^{(1)}_X(s)|=|E_X^{-1}(s)|\,\frac{\pi|P^-(t)|}{\Lambda(t)}\bigl(1+o(1)\bigr)+O_X\bigl(\log^{-2}t\bigr).$$

$|E_X^{-1}(\sigma+it)|\,|P^-(t)|$ es casi periódico en $t$, no idénticamente nulo, luego $\ge c_X>0$ en un conjunto de densidad positiva. Por tanto

$$J^{(1)}_X\ \ge\ c_X'\int^{\infty}\frac{dt}{t\log t}=\infty .$$

**La hipótesis `eq:JMfixed` de v19 es falsa para la lista de un paso.** Ninguna constante $\varpi^{(1)}_X$ lo arregla: el defecto es oscilante en $t$.

Consecuencia para Perron: la integral simétrica $\int D^{(1)}_Xx^s/s\,ds$ es, término a término, $\int\frac{\mu(d)(x/d)^{it}e^{i\omega t}}{t\log t}dt$; converge condicionalmente salvo cuando $x=d\,e^{-\omega}$ (los puntos $x=d\,q^{m'}/p^{m}$), donde el límite simétrico **no existe**. $M^{(1)}_{C,X}(x)$ no está definida en todo $x$.

## 4. El paso que sí funciona: Newton con la derivada completa (T)

$$\kappa^{N}_k:=\tau_k-\frac{S_X(\tau_k)}{N_X'(\tau_k)}=\tau_k-\frac{S_X(\tau_k)}{\Lambda(\tau_k)+S_X'(\tau_k)}.$$

Sigue siendo una fórmula explícita cuya única entrada es $\tau_k$ (lo que pide el autor). Ahora $\kappa^N_k-\kappa^{\rm ex}_k=O_X(h^2N_X''/N_X')=O_X(\Lambda^{-3})$, de modo que por 2b el cambio en $\log\zeta_C$ es $O_X(\log^{-2}t)$, integrable contra $dt/t$:

$$\boxed{\ J^{N}_X<\infty\quad\text{y}\quad \varpi^N_XM^N_{C,X}(x)=M_X^*(x)+O\bigl(J^N_Xx^{1/2+\varepsilon}\bigr)\ \ \forall x.\ }$$

Para $X$ fijo, $\kappa^N_k=\kappa^{(1)}_k\bigl(1+O_X(\Lambda^{-1})\bigr)$ en el desplazamiento: misma energía de transporte a primer orden; la diferencia solo importa para $J_X$.

## 5. Resumen

| Lista | $\kappa_k-\kappa^{\rm ex}_k$ | $\Delta\log\zeta_C$ | $J_X$ |
|---|---|---|---|
| raíces exactas | 0 | 0 | $<\infty$ (Teorema A) |
| un paso con $\Lambda$ (v19) | $-S_XS_X'/\Lambda^2$ | $\asymp_X|P^-(t)|/\log t$ | $=\infty$ |
| un paso con $N_X'$ | $O_X(\Lambda^{-3})$ | $O_X(\log^{-2}t)$ | $<\infty$ |

Pendiente para cerrar del todo el "$=\infty$": escribir con mayorantes el paso 2c (suma sobre el reloj → integral, con los alias de Poisson sin punto estacionario). Lo demás está demostrado. Para v20: cambiar el candidato de `thm:PerronMfixed` a la lista de raíces exactas o a $\kappa^N$.

---

**Corrección (25-oct, posterior).** Dos frases de arriba están mal y se corrigen en la nota `2026-10-25_JX_Newton_completo.md`:
- En 2b: "el resto $O_X(\Lambda^{-3})$ de $\epsilon_k$ aporta $O_X(\log^{-2}t)$" es falso con cotas absolutas: $\Lambda^{-3}\cdot\Lambda\log t=O(\Lambda^{-1})$. El $O(\log^{-2}t)$ solo sale con la cancelación (paridad impar de todos los órdenes del residuo de Newton), que se demuestra en la nota nueva.
- En 4: "$\kappa^N_k-\kappa^{\rm ex}_k=O_X(\Lambda^{-3})$, de modo que por 2b el cambio es $O_X(\log^{-2}t)$" tiene el mismo defecto; el resultado $J^N_X<\infty$ es correcto, pero su prueba es la de la nota nueva, no "por 2b". El signo correcto es $\kappa^N_k-\kappa^{\rm ex}_k=+\frac{S_X^2S_X''}{2\Lambda^3}(\tau_k)+O_X(\Lambda^{-4})$.
- La conclusión $J^{(1)}_X=\infty$ (§3) se mantiene; el paso 2c que faltaba se hace en la nota nueva sin Poisson, con la función de conteo exacta $n^{\rm ex}=\lfloor N_X+\tfrac12\rfloor$.
