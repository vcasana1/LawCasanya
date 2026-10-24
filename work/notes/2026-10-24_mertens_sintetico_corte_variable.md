# Zeta y Mertens del reloj Casaña con corte dependiente del índice: Teorema A′ (transición en media) y Teorema B′ (Perron)

Nota de Claude, 24-oct-2026. Continúa `2026-10-24_mertens_sintetico_reloj_casanya.md` (corte fijo), que queda como está. Sin ejecuciones numéricas. Ningún $\gamma_k$ en ninguna construcción ni prueba. Ningún manuscrito cambiado.

**Fuentes.**
- [v26] `rvm_zeta_pi_mertens_v26.tex`: §9 (Thm transition, Cor. vertical-limit, Thm unsmoothed-RVM, ec. (sawtooth-count)).
- [v14] `manuscript/ordinal_prime_cutoff_v14.tex`: Thm variable_cutoff, l. 1114; ley de cortes (8.x), l. 1558; Prop. rounding, muestreo de Sobolev en los intervalos $\mathcal U_k$; Lema 8.2 higher_moments; Lema 11.2 clock_equidistribution.
- [TH] Titchmarsh–Heath-Brown, 2.ª ed., biblioteca 297: §11.9, pp. 302–306, ec. (11.9.1).
- [G] Gonek 2012, biblioteca 125.
- [MV] Montgomery–Vaughan, biblioteca 239; citado para momentos de polinomios de Dirichlet, **sin cotejar en el PDF**.

Clases: (T) demostrado; (R) reducción que implica el objetivo; (A) abierto.

---

## 1. Construcción con corte $X_k$ dependiente del índice

Corte de altura $X(\tau):=(\tau/2\pi)^{c(\tau)}$, con $c$ de una de las dos leyes:

- **Ley A** (v14, Thm variable_cutoff): $c(\tau)\equiv c\in(0,\tfrac12]$ fijo; $X_k=(\tau_k/2\pi)^c$ cambia en cada índice.
- **Ley B** (v14, corte del primer paso de Newton, localizado en la altura): $c(\tau)=(\log\log\tau)^{-1/2}$, es decir $X_k=(\tau_k/2\pi)^{(\log\log\tau_k)^{-1/2}}$. En v14 el corte $X_1=T^{H_0^{-1/2}}$ depende de la ventana; aquí depende de $k$.

En ambas leyes $X$ es creciente, $c(\tau)\le c_0<1$ y $c(\tau)\log\tau\to\infty$. Solo se usan estas tres propiedades. La iteración multietapa ($c_j=C_\star H_{j-1}^{-9/16}$) está en §5.

Fase con potencias de primos $n\le X$:

$$S_Y(\tau)=\sum_{n\le Y}b_n\sin(\tau\log n),\qquad b_n=-\frac{\Lambda(n)}{\pi\sqrt n\,\log n}\quad\bigl(=\beta_{p^m}\text{ si }n=p^m\bigr). \tag{1.1}$$

Desplazamiento y puntos, solo con $\tau_k$:

$$\delta_k:=-\frac{S_{X(\tau_k)}(\tau_k)}{\Lambda(\tau_k)},\qquad \kappa_k:=\tau_k+\delta_k. \tag{1.2}$$

Es el reloj de un paso $\tau^X_k$ con $X=X_k$. Zeta Casaña:

$$\mathcal P_C(s)=\prod_{k\ge1}\Bigl(1+\frac{q(s)}{\frac14+\kappa_k^2}\Bigr),\qquad \zeta_C:=\frac{\mathcal P_C}{G}. \tag{1.3}$$

(T): el producto converge absolutamente porque $|\delta_k|\le X_k^{1/2}/\Lambda\ll\tau_k^{1/2}$ y $\sum\kappa_k^{-2}<\infty$. Además $\mathcal P_C(1-s)=\mathcal P_C(s)$, los ceros son exactamente $\tfrac12\pm i\kappa_k$ y **$\zeta_C$ no tiene ceros en $\Re s\ne\tfrac12$**. El producto no depende del orden de la lista: **no hace falta ordenar los puntos ni que $\tau\mapsto\tau+\delta(\tau)$ sea monótona.** El Lema 8.19 de v14 sobra aquí.

---

## 2. Teorema A′: transición en media

**Teorema A′.** Bajo la ley A o la ley B, fijo $\sigma'\in(0,\tfrac12)$, $s=\tfrac12+\sigma'+it$. Existe una constante real $\nu_C$, que depende solo de la lista, tal que

$$\frac1T\int_T^{2T}\Bigl|\log\zeta_C(s)-\log\varpi_{\RVM}-\nu_C-\log E^\natural_{X(t)}(s)\Bigr|\,dt\ \ll_{\sigma'}\ \frac{\log\log T}{\log T}+T^{-(1-c_0)\sigma'}+T^{-\sigma'}\sqrt{\log\log T}+T^{-c(T)/2}\ \longrightarrow\ 0, \tag{2.1}$$

con

$$\log E^\natural_Y(s):=\sum_{n\le Y}\frac{\Lambda(n)}{n^s\log n}.$$

La rama de $\log\zeta_C$ es la holomorfa en $\Re s>\tfrac12$ dada por la suma (2.2). En $\Re s>\tfrac12$ no hay ceros, así que la rama es global.

Es el análogo sintético e incondicional del enunciado de Gonek de que $\zeta$ se aproxima por $P_{X}$ con $X$ potencia de $t$ (Gonek 2012, Thm 3.x y Thm 5.1, p. 2169, **bajo RH** para $\zeta$). Aquí no hace falta RH: los ceros de $\zeta_C$ están en $\tfrac12$ por construcción.

**Prueba.** $z=\sigma'+it$, $\tau_*=t-i\sigma'$, $f(\tau)=\operatorname{Log}(1+z^2/\tau^2)$,

$$f'(\tau)=-\frac2\tau+\frac1{\tau-iz}+\frac1{\tau+iz},\qquad \tau+iz=\tau-\tau_*\ \ (\text{polo cercano}).$$

*Paso 0 (identidad exacta).* Se tiene

$$\log\frac{\zeta_C(s)}{\zeta_{\RVM}(s)}=\sum_k\ell_k(s),\qquad \ell_k=f(\kappa_k)-f(\tau_k)-\Bigl[\log\bigl(1+\tfrac1{4\kappa_k^2}\bigr)-\log\bigl(1+\tfrac1{4\tau_k^2}\bigr)\Bigr]. \tag{2.2}$$

La serie de corchetes converge absolutamente y es independiente de $s$; va a $\nu_C$. Además $\log\zeta_{\RVM}(s)=\log\varpi_{\RVM}+\operatorname{Log}(1+w)+O(t^{-1})$ con $|w|\le(t/2\pi)^{-\sigma'}(1+o(1))$ ([v26, Thm transition (a) y Cor. vertical-limit]). Ese término cuesta $O(T^{-\sigma'})$.

*Paso 1 (índices malos).* Se llama malo a $k$ si $|\delta_k|>\sigma'/4$, i.e. $|S_{X_k}(\tau_k)|>\sigma'\Lambda(\tau_k)/4$. Para cada $k$, $\int_{\mathbb R}|f(\kappa_k)-f(\tau_k)|\,dt\ll|\delta_k|\log(2+|\delta_k|/\sigma')$: el logaritmo del cociente de distancias a $\tau_*$ más el salto de argumento, integrado en $t$. Con Chebyshev en cuarto momento,

$$\frac1T\sum_{k\ \text{malo}}|\delta_k|^{1+\eta}\ll\frac{\#\{\tau_k\in[T/2,3T]\}}{T}\cdot\frac{\langle S_X(\tau_k)^4\rangle}{\Lambda^4(\sigma')^{3-\eta}}\ll\frac{(\log\log T)^2}{(\sigma')^3\log^3T}.$$

Los momentos en los puntos del reloj salen de:
- los momentos en $t$, $\int_T^{2T}|S_X|^{2r}\ll_r T(\log\log X)^r$ para $X^{r}\le T$ (MV, polinomio de Dirichlet de longitud $X^r$);
- el muestreo de Sobolev en los intervalos disjuntos $\mathcal U_k$ de longitud $\mathfrak b_T=2\pi/\log3T$ (v14, prueba de Prop. rounding): $g(x)^2\le\frac2{\mathfrak b}\int_{\mathcal U}g^2+2\mathfrak b\int_{\mathcal U}g'^2$.

Con la ley A y $c$ fijo hace falta $X^4\le T$, es decir $c\le\tfrac14$. Para $\tfrac14<c\le\tfrac12$ se usa el segundo momento en lugar del cuarto y el exponente empeora a $(\log T)^{-1}$, que sigue tendiendo a 0. *Sin comprobar*: la constante.

*Paso 2 (segundo orden en los índices buenos).* Para $|u|\le\sigma'/4$, $|f''(\tau_k+u)|\ll\tau_k^{-2}+\max(|\tau_k-t|,\sigma')^{-2}$. Por Taylor, $f(\kappa_k)-f(\tau_k)=f'(\tau_k)\delta_k+R_k$ con

$$\frac1T\int_T^{2T}\sum_k|R_k|\,dt\ll\frac1T\sum_{\tau_k\in[T/2,3T]}\delta_k^2\int\frac{dt}{\max(|\tau_k-t|,\sigma')^2}+O(T^{-1})\ll\frac{\langle S_X(\tau_k)^2\rangle}{\sigma'\,\Lambda(T)}\ll\frac{\log\log T}{\sigma'\log T}. \tag{2.3}$$

Es una cota **absoluta**: no requiere ninguna cancelación.

*Paso 3 (primer orden: sierra sobre el reloj RvM).* Sea $g_s(\tau):=-f'(\tau)S_{X(\tau)}(\tau)/\Lambda(\tau)$, de modo que $f'(\tau_k)\delta_k=g_s(\tau_k)$. Los $\tau_k$ **sí** son cruces de nivel de la función creciente $N_0$. Por [v26, (sawtooth-count)], $n_{\RVM}=N_0-\psi(N_0+\tfrac12)$ en $[\tau_0,\infty)$. Stieltjes (con $g_s$ continua a trozos y saltos donde $X(\tau)$ cruza una potencia de primo):

$$\sum_kg_s(\tau_k)=\int_{\tau_0}^\infty g_s\,dN_0\;+\;g_s(\tau_0)\psi\bigl(N_0(\tau_0)+\tfrac12\bigr)\;+\;\underbrace{\int_{\tau_0}^\infty\psi\bigl(N_0+\tfrac12\bigr)\,dg_s}_{\mathfrak A(s)}. \tag{2.4}$$

*Paso 3a (parte lisa, cálculo exacto).* Como $dN_0=\Lambda\,d\tau$, **el $\Lambda$ del reloj cancela exactamente el $1/\Lambda$ del paso de Newton**:

$$\int g_s\,dN_0=-\int_{\tau_0}^\infty f'(\tau)S_{X(\tau)}(\tau)\,d\tau=-\sum_nb_n\int_{\tau_n}^\infty f'(\tau)\sin(\tau\ell_n)\,d\tau,\qquad \tau_n:=\max\bigl(\tau_0,X^{-1}(n)\bigr),\ \ \ell_n=\log n.$$

El intercambio es válido porque $\int_{\tau_n}^\infty|f'|\ll|z|^2\tau_n^{-2}$ para $\tau_n\ge2t$ y $\tau_n\asymp n^{1/c}$, $c<1$. Girando $[\tau_n,\infty)$ hacia el rayo $\tau_n\mp iy$ (residuo en $\tau_*$ solo si $\tau_n<t$, orientación de [v26, (lower-contour)]):

$$\int_{\tau_n}^\infty f'\sin(\tau\ell_n)\,d\tau=c_n+\pi\sqrt n\,n^{-s}\,\mathbf 1[\tau_n<t]+O\Bigl(\frac1{\ell_n\max(|\tau_n-t|,\sigma')}+\frac1{\ell_nt}\Bigr),\qquad |c_n|\le\frac4{\tau_n\ell_n}.$$

$c_n$ viene de $-2/\tau$ y no depende de $s$. Como $X$ es creciente, $\tau_n<t\iff n<X(t)$, así que

$$\int g_s\,dN_0=\log E^\natural_{X(t)}(s)+\nu'+\mathcal R,\qquad |\mathcal R|\ll t^{c/2-1}+\frac{t^{-c(t)/2}}{\sigma'}. \tag{2.5}$$

$\mathcal R$ se acota en tres tramos:
- $n\le X(t/2)$: $\ll t^{-1}X^{1/2}/\log X$;
- $n\ge X(2t)$: $\ll\sum n^{-1/2-1/c}\ll X^{1/2-1/c}$;
- borde $|n-X(t)|$ pequeño: con $X'(t)\asymp cX/t$, $\ll cX^{1/2}/t+X^{-1/2}/\sigma'$.

**Aquí no se usa monotonía de ningún reloj corregido.** El corte duro entra solo por el borde, que cuesta $X(t)^{-1/2}$.

*Paso 3b (aliasing, donde entra $c<1$).* Se escribe $\psi(y+\tfrac12)=-\sum_{m\ge1}(-1)^m\sin(2\pi my)/(\pi m)$ (regularización de Abel $\psi_r$, como en [v26, Lemma TR-harmonic]). En $dg_s$ aparecen productos

$$e^{\pm2\pi imN_0(\tau)}\cdot e^{\pm i\tau\ell_n}\cdot(\text{amplitud lisa})\cdot K(\tau-t),\qquad K(x)=\frac1{x+i\sigma'}\ \text{o su derivada}.$$

Tienen frecuencia instantánea $\pm m\log(\tau/2\pi)\pm\ell_n$, y $\ell_n\le c\log(\tau/2\pi)$ en el soporte. Por tanto

$$\bigl|m\log\tfrac\tau{2\pi}\pm\ell_n\bigr|\ \ge\ (m-c_0)\log\tfrac\tau{2\pi}\ \ge\ (1-c_0)\log\tfrac\tau{2\pi}. \tag{2.6}$$

**Sin fase estacionaria.** La resonancia $p\approx t/2\pi$ de v14 corresponde a $c=1$.

El núcleo de Cauchy tiene representación de Fourier unilateral:

$$\frac1{x+i\sigma'}=-i\int_0^\infty e^{i\xi x-\xi\sigma'}d\xi .$$

Las frecuencias $\ge\xi_0$ quedan amortiguadas por $e^{-\sigma'\xi_0}$. Con $\xi_0=(1-c_0)\log(T/2\pi)$, Plancherel en $t$ y la suma de $|b_n|^2n^{2\sigma'}$ sobre $n\le X$:

$$\frac1T\int_T^{2T}|\mathfrak A(s)|^2dt\ll_{\sigma'}\Bigl(\frac{T}{2\pi}\Bigr)^{-2\sigma'}\sum_{n\le X(3T)}|b_n|^2\,n^{2\sigma'}\ll\frac{T^{-2(1-c_0)\sigma'}}{\sigma'\,c(T)\log T}+T^{-2\sigma'}\log\log T. \tag{2.7}$$

El factor $n^{2\sigma'}$ es el tamaño de $e^{\mp i\tau_*\ell_n}$ en el residuo; el factor $T^{-2\sigma'}$, el de $w=e^{-2\pi iN_0(\tau_*)}$.

*Estado de 3b:* mecanismo y exponentes escritos; la cota completa (chirp de $\Lambda(\tau)$ en la escala del núcleo, colas $|\tau-t|\gg t$, mayorantes uniformes en $r$) **sin comprobar línea a línea**. El término de frontera de (2.4) es una constante más $O(t^{-1})$.

*Montaje.* Se suman los pasos 0–3: Cauchy–Schwarz para (2.7), $L^1$ para (2.3) y el paso 1, y (2.5) puntual. Resulta (2.1) con $\nu_C=\nu'+\text{corchetes}+\text{frontera}$. $\square$

**Lo que muestra A′.** La corrección prima con $c(k)$ hace que $\log\zeta_C$ siga a $\log E^\natural_{X(t)}$ en todo el semiplano derecho de la banda, en media. El reloj desnudo da en cambio una constante: $\log\zeta_{\RVM}\to\log\varpi$. El único lugar donde entra el corte es el paso 3b, y la condición es $c_0<1$.

### 2.1. Corolario: $\zeta_C$ y $\zeta$ coinciden en medida a la derecha de $\tfrac12$ (T, con [TH])

[TH, §11.9, pp. 303–304, (11.9.1)], incondicional, con la densidad de ceros vía §9.19: para $\sigma_0>\tfrac12$, $\eta,\eta'>0$ y $N\ge N_0$, $T\ge T_0(N)$,

$$\bigl|\log\zeta(s)-\log E_{p_N}(s)\bigr|<2\eta\qquad(\sigma_0\le\sigma\le\sigma_1)$$

en un conjunto de $t\le T$ de medida $>(1-\eta')T$. Por otro lado, $\log E^\natural_{X(t)}-\log E_{p_N}$ tiene media cuadrática $\ll\sum_{p>p_N}p^{-2\sigma_0}$, pequeña. Con (2.1), Chebyshev y el lema de [TH, §11.9] (de área a punto) para la uniformidad en $\sigma$:

$$\bigl|\log\zeta(s)-\log\zeta_C(s)+\log\varpi_{\RVM}+\nu_C\bigr|<\eta\qquad(\sigma_0\le\sigma\le\sigma_1) \tag{2.8}$$

para $t\in[T,2T]$ fuera de un conjunto de medida $<\eta'T$.

*Estado:* la combinación es directa; el paso de área a punto exige (2.1) en $L^2$ en el rectángulo, y los pasos 1 y 2 están en $L^1$; *sin comprobar*: basta tomar raíces en (2.3) o cuarto momento en el paso 1.

**Clasificación.** (2.8) es incondicional y no usa ningún cero de $\zeta$: la zeta Casaña con corte $c(k)$ es la versión de $\zeta$ sin ceros fuera de la recta, igual a ella en medida en todo $\Re s>\tfrac12$. Para $\zeta_{\RVM}$ (sin primos) (2.8) es **falso**, porque $\log\zeta$ no es casi constante. **(R):** si el conjunto excepcional de (2.8) fuera vacío para todo $t\ge t_0(\sigma_0)$ y todo $\sigma_0>\tfrac12$, $\zeta$ no tendría ceros con $\beta\ge\sigma_0$ y $t\ge t_0$, pues $\log\zeta_C$ es finita. Eso es RH salvo un número finito de ceros. El conjunto excepcional es exactamente el control de la densidad de ceros $N(\sigma,T)$; es el obstáculo 6.1 e del traspaso trasladado al plano $s$.

---

## 3. Teorema B′: el Mertens Casaña con corte $c(k)$

**Definición.** Para $c\in(\tfrac12,1)$ y $U=U(x)\ge x^2$:

$$M_C(x;U):=\frac1{2\pi i}\int_{c-iU}^{c+iU}\frac{x^s}{s\,\zeta_C(s)}\,ds .$$

Es Perron truncado: con $c(k)$ los errores de A′ decaen solo como $1/\log t$ y la integral simétrica infinita no está garantizada.

### 3.1. B′1: reducción al término principal (A, parcialmente T)

Por A′, $F_C:=1/\zeta_C=L_C\,E^\natural_{X(t)}(s)^{-1}\,e^{-\Delta(s)}$, con $L_C=(\varpi_{\RVM}e^{\nu_C})^{-1}$ y $\Delta\to0$ en $L^1(dt)$ por bloques diádicos. Entonces

$$M_C(x;U)=L_C\,\mathbb M(x;U)+O\Bigl(x^c\int_{|t|\le U}\bigl|E^\natural_{X(t)}(s)^{-1}\bigr|\,\bigl|e^{-\Delta(s)}-1\bigr|\frac{dt}{|s|}\Bigr),\qquad \mathbb M(x;U):=\frac1{2\pi i}\int_{c-iU}^{c+iU}\frac{x^s}{s\,E^\natural_{X(|t|)}(s)}\,ds. \tag{3.1}$$

Para que el resto sea $O(x^{c}(\log U)^{O(1)})$ faltan momentos exponenciales de $\Delta$ y momentos negativos de $E^\natural_{X}$ en $\Re s=c$. Los segundos son estándar para $X\le T^{c_0}$ (método de desacoplo de Arguin–Bourgade–Radziwiłł I, §7, biblioteca 004, *sin cotejar para este uso*); los primeros son (A).

### 3.2. B′2: el término principal no contiene $M(x)$ (T)

Con corte que crece con la altura, $E^\natural_{X(|t|)}(s)^{-1}$ no es una serie de Dirichlet. Su coeficiente en $n$ (igual a $\mu(n)$ salvo potencias de primos pequeños) solo está presente en alturas $|t|\ge t_n:=X^{-1}(P^+(n))$. Coeficiente a coeficiente, con el lema de Perron truncado (Davenport, cap. 17), $y=x/n\ne1$:

$$\frac1{2\pi}\int_{t_n\le|t|\le U}\frac{y^{c+it}}{c+it}\,dt=\Bigl[\mathbf 1_{y>1}+O\Bigl(\frac{y^c}{U|\log y|}\Bigr)\Bigr]-\Bigl[\mathbf 1_{y>1}+O\Bigl(\frac{y^c}{t_n|\log y|}\Bigr)\Bigr]=O\Bigl(\frac{(x/n)^c}{t_n|\log(x/n)|}\Bigr). \tag{3.2}$$

El indicador $\mathbf 1_{n<x}$, que es lo que convierte Perron en $\sum_{n\le x}\mu(n)$, **se produce en las alturas $|t|<t_n$, y ahí el reloj corregido aún no contiene el primo $P^+(n)$**. Solo $n=1$ está presente en todas las alturas. Por tanto, para cualquier corte $X(t)\le t^{c_0}$ que crezca con la altura (leyes A y B, y también la multietapa):

$$\mathbb M(x;U)=1+\bigl(\text{integral sobre }|t|\ge t_2\text{ de }(E^{-1}_{X(|t|)}-1)x^s/s\bigr), \tag{3.3}$$

**sin el término $\sum_{n\le x}\mu(n)$**. Estructuralmente, $M_C$ es del mismo tipo que $M^{\rm crit}_{\RVM}=L+O(x^{1/2+\varepsilon})$. La diferencia $M-M_C$ es $M$ menos un objeto de tamaño $x^{1/2+\varepsilon}$, y el puente $M-M_C=O(x^{1/2+\varepsilon})$ equivale a $M=O(x^{1/2+\varepsilon})$: clase (R), sin más contenido.

(3.2) es (T). (3.3) como identidad entre integrales también es (T), pero su resto no lo acoto aquí: el intercambio coeficiente a coeficiente no es absolutamente convergente en $\Re s=c<1$.

### 3.3. Qué haría falta para que Perron vea $M$ (dictamen después de construir)

Juntando (3.2) con el Teorema B de la nota de corte fijo: para que el término principal sea $\sum_{n\le x}\mu(n)$, el corte en altura $t$ tiene que ser $X\ge x$ **en las alturas bajas** $|t|\lesssim1/|\log(x/n)|$. Es decir, un corte que depende de $x$, no de $k$, como en la nota anterior con $X=x$.

En alturas $t<x$ eso es $c>1$: más allá de la resonancia $p\approx t/2\pi$. Ahí (2.6) falla y el aliasing del paso 3b ya no es pequeño: hay que **calcularlo**. Los términos residuales en $\tau_*$ son los duales $\chi(s)\sum n^{s-1}\cdots$ del tipo de la ecuación funcional aproximada, y en el modelo de corte fijo eran exactamente $\chi(s)E_X(1-s)/E_X(s)$. Esto coincide con la prioridad I del traspaso (resonancia no lineal en $p=T^\theta$), con $\theta\ge1$ en lugar de $\theta<1$. Es (A) y es el único sitio donde el corte variable podría entrar en la identidad con $M$.

---

## 4. Tabla de clases

| Enunciado | Clase |
|---|---|
| $\zeta_C$ con corte $c(k)$: definición, ceros solo en $\frac12$, sin necesidad de ordenar | (T) |
| A′, pasos 0, 1, 2, 3a (incluida la cancelación exacta $\Lambda\cdot\Lambda^{-1}$ y la aparición de $E^\natural_{X(t)}$) | (T) |
| A′, paso 3b (aliasing $\ll T^{-(1-c_0)\sigma'}$ en $L^2$, requiere $c_0<1$) | (T) en mecanismo; sin comprobar línea a línea |
| (2.8): $\zeta$ y $\zeta_C$ coinciden en medida en $\Re s>\frac12$ | (T) dado A′ y [TH §11.9]; uniformidad en $\sigma$ sin comprobar |
| (2.8) sin conjunto excepcional $\Rightarrow$ RH (salvo un número finito de ceros) | (R) |
| B′1 (resto de Perron) | (A): momentos exponenciales de $\Delta$ |
| B′2 (3.2): con corte creciente en altura, Perron no produce $\sum_{n\le x}\mu(n)$ | (T) |
| Identidad con $M$ vía corte $\ge x$ en alturas bajas ($c>1$, resonancia) | (A), prioridad I |

## 5. Ley multietapa ($c_j=C_\star H_{j-1}^{-9/16}$)

El paso $j$ desplaza los puntos $\kappa^{(j-1)}_k$, que ya no son cruces de nivel de $N_0$. Para el paso 3 hay que muestrear en $\kappa^{(j-1)}$ y no en $\tau_k$:

$$\sum_kh(\kappa^{(j-1)}_k)=\sum_kh(\tau_k)+\sum_kh'(\tau_k)\bigl(\kappa^{(j-1)}_k-\tau_k\bigr)+\cdots$$

Esto es la misma maquinaria de los pasos 1–3 aplicada recursivamente. (A), sin obstáculo nuevo visible: todos los cortes son $\le T^{c_1}$, con $c_1<1$. B′2 vale tal cual para la multietapa, porque los cortes siguen creciendo con la altura.
