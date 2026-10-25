# $J_X<\infty$ para el paso de Newton con derivada completa: prueba completa, sin Poisson

Nota de Claude, 25-oct-2026. Completa el §4 de `2026-10-25_JX_un_paso_diverge.md` y cierra también su paso 2c. Sin ejecuciones numéricas. $X\ge2$ fijo. Fuentes: mi nota del 24-oct (`2026-10-24_mertens_sintetico_reloj_casanya.md`, §1–2: lista de raíces exactas, Teorema A), v15–v19 (`prop:xiSynthetic`, `thm:PerronMfixed`).

## 0. Objetos

- $N_X=N_0+S_X$, $\Lambda=N_0'$. $A_0=\sup|S_X|$, $A_j=\sup|S_X^{(j)}|$ ($j=1,2,3$); todos finitos para $X$ fijo (series de $p^{-m/2}\log^jp$ convergentes).
- $\tau'=\tau'(X)$ tal que $\Lambda(\tau)\ge2A_1$ para $\tau\ge\tau'$; entonces $\tfrac12\Lambda\le N_X'\le\tfrac32\Lambda$ en $[\tau',\infty)$.
- $K'=\lfloor N_X(\tau')+\tfrac12\rfloor$. Para $k\le K'$, ambas listas usan los **mismos** puntos convencionales.
- Para $k>K'$: $\kappa^{\rm ex}_k$ raíz de $N_X(\kappa)=k-\tfrac12$ en $(\tau',\infty)$, y
$$\kappa^N_k:=\tau_k-\frac{S_X(\tau_k)}{N_X'(\tau_k)}=\tau_k-\frac{S_X(\tau_k)}{\Lambda(\tau_k)+S_X'(\tau_k)} .$$
- $n^{\rm ex}(\tau)=\#\{k:\kappa^{\rm ex}_k\le\tau\}=\lfloor N_X(\tau)+\tfrac12\rfloor$ para $\tau\ge\tau'$ (exacto, por monotonía). $n^N(\tau)=\#\{k:\kappa^N_k\le\tau\}$. $\nu:=n^N-n^{\rm ex}$.
- $\Xi_\kappa$, $\zeta_\kappa$ como en `prop:xiSynthetic`; $s=\tfrac12+\sigma'+it$, $0<\sigma'<\tfrac12$ fijo, $z=s-\tfrac12$, $w:=t-i\sigma'$.

## 1. El residuo de Newton (T)

Para $k>K'$ escribimos $\kappa^{\rm ex}_k=\tau_k-h_k$. Como $N_0(\tau_k)=k-\tfrac12$, se tiene $N_X(\tau_k)=k-\tfrac12+S_X(\tau_k)$, y Taylor con resto de Lagrange da, para algún $\xi_k$ entre $\tau_k$ y $\kappa^{\rm ex}_k$,

$$0=N_X(\kappa^{\rm ex}_k)-\bigl(k-\tfrac12\bigr)=S_X(\tau_k)-h_kN_X'(\tau_k)+\frac{h_k^2}2N_X''(\xi_k).$$

Luego $h_k=\dfrac{S_X(\tau_k)}{N_X'(\tau_k)}+\dfrac{h_k^2N_X''(\xi_k)}{2N_X'(\tau_k)}$ y

$$\boxed{\ \epsilon_k:=\kappa^N_k-\kappa^{\rm ex}_k=h_k-\frac{S_X(\tau_k)}{N_X'(\tau_k)}=\frac{h_k^2\,N_X''(\xi_k)}{2N_X'(\tau_k)} .\ }$$

Con $|h_k|\le2A_0/\Lambda(\tau_k)$ (de $|S_X|\le A_0$, $N_X'\ge\Lambda/2$, y $|h_k^2N_X''|\le\ldots$ absorbido para $\tau_k$ grande), $|N_X''|\le A_2+1$ y $N_X'\ge\Lambda/2$:

$$|\epsilon_k|\le\frac{C_1(X)}{\Lambda(\tau_k)^3},\qquad C_1=4A_0^2(A_2+1). \tag{1.1}$$

**Término principal.** $h_k=S_X(\tau_k)/\Lambda(\tau_k)+O_X(\Lambda^{-2})$; $N_X''(\xi_k)=S_X''(\tau_k)+O(A_3|h_k|)+O(1/\tau_k)$; $N_X'(\tau_k)=\Lambda(\tau_k)(1+O_X(\Lambda^{-1}))$. Por tanto

$$\epsilon_k=\mathcal E(\tau_k)+O_X\bigl(\Lambda(\tau_k)^{-4}\bigr),\qquad \mathcal E(\tau):=\frac{S_X(\tau)^2S_X''(\tau)}{2\Lambda(\tau)^3}. \tag{1.2}$$

Además $\mathcal E(\tau_k)=\mathcal E(\kappa^{\rm ex}_k)+O(|h_k|\sup|\mathcal E'|)=\mathcal E(\kappa^{\rm ex}_k)+O_X(\Lambda^{-4})$, porque $|\mathcal E'|\ll_X\Lambda^{-3}$.

**Paridad.** $S_X$ es suma de senos, luego **impar** en $\tau$; $S_X'$ par, $S_X''$ impar. Así $S_X^2S_X''$ y $S_X^2S_X''S_X'$ son polinomios trigonométricos **impares**, y por tanto **sin término constante**:

$$S_X^2S_X''=\sum_{\omega\in\Omega}q_\omega e^{i\omega\tau},\qquad S_X^2S_X''S_X'=\sum_{\omega\in\Omega_1}q^1_\omega e^{i\omega\tau},\qquad 0\notin\Omega\cup\Omega_1, \tag{1.3}$$

con $\Omega,\Omega_1$ finitos, $|\omega|\le4\log X$. (Observación: lo mismo vale a todo orden: la ecuación $\Lambda h=S_X(\tau-h)$ que define formalmente $h$ con $\Lambda$ congelada es impar en $\tau$, así que ningún orden del residuo tiene media.)

## 2. Identidad exacta de transporte y constante de normalización (T)

Para cualquier lista $\kappa$ con $\sum\kappa_k^{-2}<\infty$, $\log\Xi_\kappa(s)=\log C_\kappa+\int_{0}^\infty\log\bigl(1+z^2/\tau^2\bigr)\,dn_\kappa(\tau)$. Para las dos listas, con $\nu=n^N-n^{\rm ex}$ (nula en $[0,\tau']$ y fuera de $\bigcup_kI_k$, $I_k$ el intervalo entre $\kappa^{\rm ex}_k$ y $\kappa^N_k$, donde vale $-\operatorname{sgn}\epsilon_k$), integrando por partes (términos de frontera nulos: $\nu$ se anula cerca de $\tau'$, y $\nu\log(1+z^2/\tau^2)\to0$):

$$\Delta(s):=\log\zeta^N(s)-\log\zeta^{\rm ex}(s)=\log\frac{C^N}{C^{\rm ex}}+\int_{\tau'}^\infty\nu(\tau)\,\frac{2z^2}{\tau(\tau^2+z^2)}\,d\tau .$$

Como $|\nu|\le1$ en $I_k$ y $|I_k|=|\epsilon_k|$, la integral $\int\nu\cdot\frac2\tau\,d\tau$ converge absolutamente ($\sum|\epsilon_k|/\kappa_k\ll\sum\Lambda^{-3}/\tau_k<\infty$). Definimos

$$\Delta_\infty:=\log\frac{C^N}{C^{\rm ex}}+\int_{\tau'}^\infty\nu(\tau)\frac{2}{\tau}\,d\tau,\qquad \varpi^N_X:=\varpi^{\rm ex}_X\,e^{\Delta_\infty}.$$

Entonces, exactamente,

$$\boxed{\ \Delta(s)-\Delta_\infty=-\int_{\tau'}^\infty\nu(\tau)\,g_w(\tau)\,d\tau,\qquad g_w(\tau):=\frac{2\tau}{\tau^2+z^2}=\frac1{\tau-w}+\frac1{\tau+\bar w}.\ } \tag{2.1}$$

(Comprobación: $\frac{2z^2}{\tau(\tau^2+z^2)}-\frac2\tau=\frac{-2\tau}{\tau^2+z^2}$; y $\tau^2+z^2=(\tau-w)(\tau+\bar w)$ con $w=t-i\sigma'$.)

## 3. Reducción a sumas sobre la lista exacta (T)

$\int\nu g_w=\sum_k\bigl(-\operatorname{sgn}\epsilon_k\bigr)\int_{I_k}g_w=-\sum_k\int_{\kappa^{\rm ex}_k}^{\kappa^{\rm ex}_k+\epsilon_k}g_w(\tau)\,d\tau=-\sum_k\Bigl[\epsilon_kg_w(\kappa^{\rm ex}_k)+O\bigl(\epsilon_k^2\sup_{I_k}|g_w'|\bigr)\Bigr]$.

Los huecos de la lista exacta están en $[\frac{2}{3\Lambda},\frac2\Lambda]$ (de $\tfrac12\Lambda\le N_X'\le\tfrac32\Lambda$), y $|\epsilon_k|\ll_X\Lambda^{-3}$ es mucho menor; así el número de $k$ con $|\kappa^{\rm ex}_k-t|\in[j,j+1)$ es $\le2\Lambda(t)+2$ para $j\le t/2$.

- **Cuadráticos:** $\sum_k\epsilon_k^2\sup_{I_k}|g_w'|\ll_X\sum_k\frac{\Lambda^{-6}}{|\kappa_k-w|^2}\ll_X\frac{\Lambda^{-6}\cdot\Lambda}{\sigma'}+\Lambda^{-6}\ll_X\Lambda(t)^{-5}$.
- **Resto $O(\Lambda^{-4})$ de (1.2):** $\sum_k\frac{\Lambda(\tau_k)^{-4}}{|\kappa_k-w|}$. Para $|\kappa_k-t|\le t/2$: $\le\Lambda(t)^{-4}\bigl[(2\Lambda+2)/\sigma'+(2\Lambda+2)\sum_{j\le t/2}1/j\bigr]\ll_X\Lambda^{-4}\cdot\Lambda\log t\ll\Lambda(t)^{-2}$. Para $\kappa_k\le t/2$: $\le\frac2t\sum_k\Lambda(\tau_k)^{-4}\ll\frac1t\int^{t}\Lambda^{-3}d\tau\ll\Lambda(t)^{-3}$. Para $\kappa_k\ge2t$: $\ll\sum_{\kappa_k\ge2t}\frac{\Lambda^{-4}}{\kappa_k}\ll\int_{2t}^\infty\frac{d\tau}{\tau\Lambda^3}\ll\Lambda(t)^{-2}$.

Queda el término principal

$$\mathcal M(s):=-\sum_{k>K'}\mathcal E(\kappa^{\rm ex}_k)\,g_w(\kappa^{\rm ex}_k)=-\int_{\tau'}^\infty\mathcal E\,g_w\,dn^{\rm ex}, \qquad \Delta(s)-\Delta_\infty=-\mathcal M(s)\cdot(-1)+O_X(\Lambda^{-2})$$

(el signo global es irrelevante para la cota). Y $dn^{\rm ex}=dN_X-d\rho$ con $\rho(\tau):=N_X(\tau)-\lfloor N_X(\tau)+\tfrac12\rfloor\in[-\tfrac12,\tfrac12)$.

## 4. La parte diente de sierra (T)

$\int\mathcal Eg_w\,d\rho=[\mathcal Eg_w\rho]_{\tau'}^\infty-\int\rho\,(\mathcal Eg_w)'\,d\tau$. El término de frontera en $\tau'$ es $O_X(1/t)$; en $\infty$ es 0. Y

$$\int_{\tau'}^\infty|(\mathcal Eg_w)'|\,d\tau\le\int|\mathcal E'||g_w|+\int|\mathcal E||g_w'|\ll_X\int_{\tau'}^\infty\frac{\Lambda(\tau)^{-3}}{|\tau-w|}d\tau+\int\frac{\Lambda(\tau)^{-3}}{|\tau-w|^2}d\tau+(\text{lo mismo con }\tau+\bar w).$$

Primera integral: en $[t/2,2t]$ es $\le\Lambda(t/2)^{-3}\int_{t/2}^{2t}\frac{d\tau}{|\tau-w|}\ll\Lambda^{-3}\log(t/\sigma')\ll\Lambda(t)^{-2}$; en $[\tau',t/2]$ es $\le\frac2t\int^{t}\Lambda^{-3}\ll\Lambda^{-3}$; en $[2t,\infty)$ es $\ll\int_{2t}^\infty\frac{d\tau}{\tau\Lambda^3}\ll\Lambda^{-2}$. Segunda: $\ll\Lambda^{-3}/\sigma'$. Los términos con $\tau+\bar w$ no tienen singularidad y son menores. **Total $O_{X,\sigma'}(\Lambda(t)^{-2})$.**

## 5. La parte continua: aquí entra la paridad (T)

$\int\mathcal Eg_w\,dN_X=\int\mathcal E\,N_X'\,g_w\,d\tau$ con

$$\mathcal EN_X'=\frac{S_X^2S_X''}{2\Lambda^2}+\frac{S_X^2S_X''S_X'}{2\Lambda^3}=\sum_{\omega\in\Omega}\frac{q_\omega}{2}\frac{e^{i\omega\tau}}{\Lambda(\tau)^2}+\sum_{\omega\in\Omega_1}\frac{q^1_\omega}{2}\frac{e^{i\omega\tau}}{\Lambda(\tau)^3},$$

**sin término $\omega=0$** por (1.3). Basta probar, para cada $\omega\ne0$ fijo y $m\in\{2,3\}$,

$$I_{\omega,m}(t):=\int_{\tau'}^\infty\frac{e^{i\omega\tau}}{\Lambda(\tau)^m}\,\frac{d\tau}{\tau-w}=O_{X,\omega,\sigma'}\bigl(\Lambda(t)^{-m}\bigr), \tag{5.1}$$

y lo análogo con $\tau+\bar w$ (más fácil: sin singularidad, integración por partes da $O(1/(|\omega|t))$).

*Prueba de (5.1).* Escribimos $\Lambda(\tau)^{-m}=\Lambda(t)^{-m}+\delta(\tau)$, $\delta(\tau)=\Lambda(\tau)^{-m}-\Lambda(t)^{-m}$.

(a) $\Lambda(t)^{-m}\int_{\tau'}^\infty\frac{e^{i\omega\tau}}{\tau-w}d\tau$. Para $\Im w<0$: $\int_{\mathbb R}\frac{e^{i\omega\tau}}{\tau-w}d\tau=-2\pi ie^{i\omega w}\mathbf 1_{\omega<0}$, de módulo $\le2\pi e^{|\omega|\sigma'}$; y $\bigl|\int_{-\infty}^{\tau'}\bigr|\le\frac{2}{|\omega|(t-\tau')}$ por integración por partes ($t\ge2\tau'$). Luego (a) $\ll\Lambda(t)^{-m}$.

(b) $\int\delta(\tau)\frac{e^{i\omega\tau}}{\tau-w}d\tau$. Como $|\Lambda(\tau)-\Lambda(t)|=\frac{|\log(\tau/t)|}{2\pi}$:
- en $[t/2,2t]$: $|\delta|\ll\frac{|\tau-t|}{t\,\Lambda(t)^{m+1}}$ y $\frac{|\tau-t|}{|\tau-w|}\le1$, luego la integral es $\ll\frac{1}{\Lambda^{m+1}}$;
- en $[2t,\infty)$: $\phi(\tau)=\delta(\tau)/(\tau-w)$ cumple $|\phi(2t)|\ll\Lambda^{-m}/t$ y $\int_{2t}^\infty|\phi'|\ll\int_{2t}^\infty\bigl(\frac{\Lambda^{-m-1}}{\tau^2}+\frac{\Lambda^{-m}}{\tau^2}\bigr)d\tau\ll\frac{\Lambda^{-m}}{t}$; integración por partes contra $e^{i\omega\tau}$ da $O\bigl(\frac{\Lambda^{-m}}{|\omega|t}\bigr)$;
- en $[\tau',t/2]$: $|\phi|\le\frac{2\Lambda(\tau)^{-m}}{t}$, $|\phi(\tau')|+\int_{\tau'}^{t/2}|\phi'|\ll_X\frac1t$; integración por partes da $O\bigl(\frac{1}{|\omega|t}\bigr)$.

Así $I_{\omega,m}=O(\Lambda(t)^{-m})$. $\square$

Sumando sobre el número finito de frecuencias: **la parte continua es $O_{X,\sigma'}(\Lambda(t)^{-2})$.**

## 6. Teorema

**Teorema.** Sea $X\ge2$ fijo y $0<\sigma'<\tfrac12$. Con $\varpi^N_X=\varpi^{\rm ex}_Xe^{\Delta_\infty}$, existe $t_1=t_1(X,\sigma')$ tal que para $t\ge t_1$

$$\bigl|\Delta(\tfrac12+\sigma'+it)-\Delta_\infty\bigr|\le\frac{C_2(X,\sigma')}{\log^2t}.$$

En consecuencia, con el Teorema A ($\varpi^{\rm ex}_X/\zeta^{\rm ex}_{C,X}=E_X^{-1}(1+w_X)^{-1}(1+\mathcal E_X)^{-1}$, $|w_X|+|\mathcal E_X|\ll_Xt^{-\delta}\log t$),

$$D^N_X(s):=\frac{\varpi^N_X}{\zeta^N_{C,X}(s)}-E_X(s)^{-1}=E_X^{-1}\Bigl[(1+w_X)^{-1}(1+\mathcal E_X)^{-1}e^{-(\Delta-\Delta_\infty)}-1\Bigr]\ll_{X,\sigma'}\ t^{-\delta}\log t+\frac1{\log^2t},$$

y por tanto

$$\boxed{\ J^N_X(\tfrac12+\sigma')=\frac1{2\pi}\int_{-\infty}^\infty\frac{|D^N_X(\tfrac12+\sigma'+it)|}{|\tfrac12+\sigma'+it|}\,dt<\infty .\ }$$

Por `thm:PerronMfixed` de v19 (o el Teorema B de mi nota del 24-oct): para todo $x\ge2$,

$$\varpi^N_X\,M^N_{C,X}(x)=M_X^*(x)+\mathcal R(x),\qquad|\mathcal R(x)|\le J^N_X\,x^{1/2+\sigma'},$$

y $M^N_{C,X}(x)=O_{X,\sigma'}(x^{1/2+\sigma'})$ para todo $x$ (porque $|M_X^*|\le2^{\pi(X)}$). Para $2\le x\le X$, $M_X^*(x)=M^*(x)$.

*Prueba.* §§2–5: $\Delta-\Delta_\infty=O(\Lambda^{-5})+O(\Lambda^{-2})+O(\Lambda^{-2})+O(\Lambda^{-2})$. Para $|t|\le t_1$, $D^N_X$ es continua en la recta (no hay polos de $1/\zeta^N$ en $\Re s>\tfrac12$ y $\zeta^N$ no tiene polo salvo en $s=1$), así que la integral sobre $[-t_1,t_1]$ es finita; $t<0$ por simetría. $\int_{t_1}^\infty\frac{dt}{t\log^2t}<\infty$. $\square$

## 7. Lo que la prueba muestra sobre la lista de un paso

El mismo esquema con $\kappa^{(1)}_k=\tau_k-S_X/\Lambda$ da $\epsilon^{(1)}_k=-\frac{S_XS_X'}{\Lambda^2}(\tau_k)+O_X(\Lambda^{-3})$, y en §5 la parte continua es $-\int\frac{S_XS_X'}{\Lambda^2}N_X'g_w\,d\tau$, cuya pieza principal es $\frac{1}{\Lambda(t)}\cdot\bigl(-2\pi i\sum_{\omega<0}c_\omega e^{i\omega w}\bigr)$ con $\tfrac12(S_X^2)'=\sum c_\omega e^{i\omega\tau}$: exactamente el término $-\pi iP^-(t)/\Lambda(t)$ de la nota anterior, ahora **demostrado** por (5.1) con $m=1$ y el cálculo exacto de (a). Como $P^-\not\equiv0$ y el resto es $O(\Lambda^{-2})$, $|D^{(1)}_X|\gg|E_X^{-1}||P^-|/\log t$ en un conjunto de densidad positiva y $J^{(1)}_X=\infty$. El paso 2c de la nota anterior queda cerrado sin Poisson.

## 8. Resumen

| Lista | $\epsilon_k$ | $\Delta-\Delta_\infty$ | $J_X$ |
|---|---|---|---|
| raíces exactas | $0$ | $0$ | $<\infty$ (Teorema A) |
| un paso con $\Lambda$ (v19) | $-\frac{S_XS_X'}{\Lambda^2}+O(\Lambda^{-3})$ | $-\frac{\pi iP^-(t)}{\Lambda(t)}+O(\Lambda^{-2})$ | $=\infty$ |
| un paso con $N_X'$ | $\frac{S_X^2S_X''}{2\Lambda^3}+O(\Lambda^{-4})$ | $O(\Lambda^{-2})$ | $<\infty$ |

Ingredientes: Taylor con resto; la función de conteo exacta $n^{\rm ex}=\lfloor N_X+\tfrac12\rfloor$ (sin Poisson); paridad impar de $S_X$ (todas las correcciones de Newton tienen media cero); la transformada de Hilbert de $e^{i\omega\tau}$. Para v20: candidato de `thm:PerronMfixed` = raíces exactas o $\kappa^N$; la lista de un paso con $\Lambda$ no cumple `eq:JMfixed`.

---

**Corrección (25-oct, tras leer v20).** $S_X$ lleva todas las potencias $m\ge1$, así que $S_X^2S_X''$ y $S_X^2S_X''S_X'$ **no** son polinomios trigonométricos finitos: son series casi periódicas con frecuencias $\sum_{p\le X}j_p\log p$, que pueden acumularse en 0. El §5 tal como está escrito vale si se trunca $S_X$ en $m\le m_0$ (polinomio finito) y se controla la cola $m>m_0$ en norma uniforme con derivadas ($O_X(2^{-m_0/2})$). Con todas las potencias hace falta el paso que añade v20 (Lema `v20FourierPrimitive`): decaimiento exponencial de los coeficientes por analiticidad en la poli-banda, y la cota de Baker–Wüstholz $|\omega_{\boldsymbol j}|\ge c_X(1+\|\boldsymbol j\|_1)^{-B_X}$ para las frecuencias no nulas, que da una primitiva acotada. La conclusión $J^N_X<\infty$ no cambia. Lo mismo afecta al "polinomio trigonométrico $P^-$" del §7: es una función casi periódica no nula; la conclusión $J^{(1)}_X=\infty$ se mantiene porque una función casi periódica no nula está acotada inferiormente en un conjunto de densidad positiva.
