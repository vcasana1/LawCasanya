# Consecuencias para los transportes $\zeta_{\RVM}\to\zeta$, $\zeta_{\tau^C}\to\{\gamma_k\}$, $\pi_{\tau^C}\to\pi$ y $M_{\tau^C},\pi_{\RVM}\to\pi,M$

Nota de Claude, 24-oct-2026. Reúne lo que se sigue de los resultados de hoy:
- Teorema A′ y Teorema B′ (notas de corte fijo y de corte variable);
- Teorema 1 de conteo;
- Teorema C1;
- Teorema S2 con el lema Ω del autor (Addenda C).

Clases: (T) demostrado; (R) reducción que implica el objetivo; (A) abierto. Sin ejecuciones numéricas. Ningún manuscrito cambiado.

**Notación.**
- $\kappa_k$ es cualquier lista sin ceros (reloj corregido $\tau^C$, un paso o multietapa, corte por índice con $V_T\to0$), ordenada.
- $r_k=\Lambda(\tau_k)(\kappa_k-\gamma_k)$.
- $\zeta_C=\mathcal P_C/G$ es el producto de Hadamard sobre los $\kappa_k$: sus ceros no triviales son exactamente $\tfrac12\pm i\kappa_k$.
- $\psi_C$ y $\pi_C$ vienen de la fórmula explícita con los ceros de $\zeta_C$; $M_C$ es Perron de $1/\zeta_C$.

---

## 1. $\zeta_{\RVM}\to\zeta$: factorización del transporte a través de $\zeta_C$

**1.1 (T).** Por A′ (corte $c<1$) más Titchmarsh §11.9 (11.9.1): para cada $\sigma_0>\tfrac12$,

$$\log\zeta(s)-\log\zeta_C(s)\to\text{cte}$$

en medida en $t$ (fuera de un conjunto de medida $<\eta'T$), uniformemente en $\sigma\in[\sigma_0,\sigma_1]$. Para $\zeta_{\RVM}$ esto es falso, porque $\log\zeta_{\RVM}\to\log\varpi$ es constante y $\log\zeta$ no. **El transporte $\zeta_{\RVM}\to\zeta$ se factoriza**:

$$\zeta=\underbrace{\zeta_{\RVM}}_{\text{reloj}}\cdot\underbrace{\frac{\zeta_C}{\zeta_{\RVM}}}_{\approx\,E_{X(t)}(s)\ \text{(primos, sin ceros)}}\cdot\underbrace{\frac{\zeta}{\zeta_C}}_{\to\ \text{cte en medida}} .$$

Todo el contenido de producto de Euler del transporte lo aporta el paso computable. El último factor solo falla en un conjunto excepcional, que contiene los entornos de los ceros de $\zeta$ fuera de la recta, si los hay.

**1.2 (T). Energía del transporte residual.** En la familia $\lambda$ de v26 se sustituye el extremo $\tau_k$ por $\kappa_k$:

$$\gamma_k(\lambda)=(1-\lambda)\gamma_k+\lambda\kappa_k .$$

La energía del desplazamiento pasa de

$$\langle\Lambda^2(\tau_k-\gamma_k)^2\rangle=\tfrac1{2\pi^2}\log\log T\,(1+o(1))$$

a $\langle r_k^2\rangle=O(1)$ con la multietapa (v14, Thm `uniform_iteration`). Con un paso y corte por índice, S2 + lema Ω dan la descomposición exacta

$$\langle r_k^2\rangle=\sum_{n\le T^b}\frac{a_n^2}2|R^\tau_n-\mathcal A_n|^2\,(1+o(1))+\Omega_b[s]+o(1).$$

**Consecuencia para v26:** todo criterio de v26 (rigidez, atomización, ruta B con listas $C$-admisibles) cuya hipótesis o error dependa de la energía del desplazamiento respecto del reloj mejora de $\log\log T$ a $O(1)$ si se toma $\kappa_k$ como extremo. Esto es aplicable ya. No he repasado criterio a criterio cuáles de v26 dependen de esa energía; es la tarea siguiente si se quiere usar.

---

## 2. $\zeta_{\tau^C}\to\{\gamma_k\}$: los ceros de la zeta Casaña frente a las ordenadas

**2.1 (T).** S2 y el lema Ω (autor) para un corte arbitrario índice a índice con $V_T\to0$: el error cuadrático medio de los ceros de $\zeta_C$ se parte en
- la respuesta no reproducida, $\sum a_n^2|R^\tau_n-\mathcal A_n|^2/2$;
- el resto universal $\Omega_b[s]$.

**2.2 (T bajo H1$_{L^2}$).** La mejor lista lineal es el filtro de Wiener $\lambda_p=1-\Phi(\theta_p)$ sobre todo $p\le T^b$. Su error es $\Omega_b[s]+o(1)$. Con peso 1, el mínimo está en $c^*=0.6758$ y vale $0.0047+\Omega$.

**2.3 (T). Ceros fuera de la recta, por conteo.** Teorema 1:

$$\#\{\rho:\ T<\gamma\le2T,\ \beta\ne\tfrac12\ \text{o múltiple}\}\le4\,d(T)\,\#\mathcal I_T ,$$

donde $d(T)$ es la proporción de índices con $|\kappa_k-\gamma_k|\ge\tfrac12\min(\text{huecos adyacentes})$. Con S2, $d(T)$ queda acotado por las colas de $r_k$, cuya energía está descompuesta arriba. **(A):** hace falta una cota de cola (subgaussiana o de cuarto momento con constantes explícitas) para que $1-4d>0$. Chebyshev en segundo momento no basta con los valores de 2.2.

---

## 3. $\pi_{\tau^C}\to\pi$ y $\pi_{\RVM}\to\pi$: comparación aritmética, sin ceros

*(Corrección. La versión anterior comparaba por la fórmula explícita con los ceros de $\zeta$. Esa no es la comparación del método y queda retirada.)*

**3.1 (T). Identidad de Perron en $\Re s=c>1$.** Por Perron con altura $U$,

$$\psi(x)-\psi_C(x)=\frac1{2\pi i}\int_{c-iU}^{c+iU}\Bigl[-\frac{\zeta'}{\zeta}(s)+\frac{\zeta_C'}{\zeta_C}(s)\Bigr]\frac{x^s}s\,ds+O\Bigl(\frac{x\log^2(xU)}U\Bigr).$$

En $\Re s>1$, $-\zeta'/\zeta=\sum\Lambda(n)n^{-s}$ exactamente. $\zeta_C$ está definida solo por $\kappa_k$, el reloj y los primos. Ningún cero de $\zeta$ interviene.

**3.2 (T, por A′ en el régimen $t$ grande).** $\log\zeta_C(s)=\mathrm{cte}+\log E^\natural_{X(t)}(s)+$ resto en media. Derivando en el sentido de A′,

$$-\frac{\zeta_C'}{\zeta_C}(s)\approx\sum_{n\le X(t)}\frac{\Lambda(n)}{n^s}+\bigl(\text{término del reloj }\zeta_{\RVM}\bigr).$$

La diferencia del integrando es la **cola prima rugosa a la altura $t$**:

$$-\frac{\zeta'}{\zeta}+\frac{\zeta_C'}{\zeta_C}\ \approx\ \sum_{n>X(|t|)}\frac{\Lambda(n)}{n^s}-\Bigl(\frac{-\zeta_{\RVM}'}{\zeta_{\RVM}}\Bigr)(s).$$

Lo segundo es la parte del reloj desnudo, con límite vertical $0$ por v26.

**3.3 (T). Qué exige Perron.** El cálculo de B′ (3.2) da: el término $n$ produce su indicador $\mathbf 1_{n<x}$ en las alturas $|t|\lesssim1/|\log(x/n)|$. Si a esas alturas $X(t)<n$, el término $n$ está en la cola rugosa y $\psi_C$ no lo contiene. Por tanto:

$$\psi(x)-\psi_C(x)\ \text{pequeño}\iff\text{el reloj Casaña contiene los }n\le x\text{ en las alturas donde Perron los resuelve.}$$

Con un corte que crece con la altura, $X(t)\le t^{c}$ con $c<1$, esto falla para los $n$ grandes. Hace falta $X\ge x$ en esas alturas, lo que da $c\ge1$: la **resonancia del reloj** $p\approx t/2\pi$ (Teorema C1 y nota de la ley). Es un objeto aritmético del reloj y de los primos, sin ceros.

**3.4 ($\pi_{\RVM}$).** Para $\zeta_{\RVM}$ el integrando lleva toda la serie $\sum\Lambda(n)n^{-s}$ como diferencia, porque no hay ningún primo en el reloj desnudo. La identificación con $\pi$ por esta vía es enteramente la tarea de los primos que faltan. Coincide con v26: $\pi_{\RVM}$ es otra función, con $\pi_{\RVM}-\mathrm{li}$ de tamaño raíz.

---

## 4. $M_{\tau^C}\to M$: comparación aritmética, sin ceros

*(Corrección. Se retira la versión anterior con residuos $x^\rho/(\rho\zeta'(\rho))$: en $M_{\tau^C}$ no intervienen los ceros de $\zeta$.)*

**4.1 (T). Identidad en $\Re s=c>1$.** Con $1/\zeta=\sum\mu(n)n^{-s}$ exactamente,

$$M(x)-M_C(x)=\frac1{2\pi i}\int_{c-iU}^{c+iU}\Bigl[\frac1{\zeta(s)}-\frac1{\zeta_C(s)}\Bigr]\frac{x^s}s\,ds+O\Bigl(\frac{x\log x}U\Bigr).$$

**4.2 (T, A′ y B′).** A altura $t$, $1/\zeta_C\approx L_C\,E^\natural_{X(t)}(s)^{-1}=L_C\sum_{P^+(n)\le X(t)}\mu^\natural(n)n^{-s}$. La diferencia del integrando es

$$\frac1\zeta-\frac1{\zeta_C}\approx\sum_{P^+(n)>X(|t|)}\frac{\mu(n)}{n^s}+(1-L_C)\sum_{P^+(n)\le X(|t|)}\frac{\mu(n)}{n^s}+\cdots,$$

**la cola de Möbius rugosa a la altura $t$** más el defecto de la constante $L_C$. Aquí no aparece ningún cero.

**4.3 (T). Teorema B′ en esta forma.** El coeficiente $\mu(n)$ entra en $M_C$ solo en las alturas $|t|\ge t_n=X^{-1}(P^+(n))$, donde Perron aporta $O\bigl((x/n)^c/(t_n|\log(x/n)|)\bigr)$. Con corte creciente en altura, $M_C$ no contiene $\sum_{n\le x}\mu(n)$, y la diferencia 4.1 es toda la cola rugosa.

**4.4 (A). La construcción que sí iguala a $M$.** Por 4.2–4.3, para que $M_C$ se iguale a $M$:
- el reloj Casaña debe contener a altura $t$ todos los primos $p\le x$ en las alturas donde Perron resuelve $\mu(n)$;
- la constante debe ser $L_C=1$.

Con corte fijo $X\ge x$ esto es la identidad exacta de la nota de corte fijo ($\varpi_XM_{C,X}=M^*+O_X(x^{1/2+\varepsilon})$ para $x\le X$), cuyo único problema es la **uniformidad en $X$**: el reloj Casaña de corte $X$ es monótono solo si $X\ll(\log t)^2$. Con corte variable, hace falta $c\ge1$ a las alturas bajas, otra vez la resonancia $p\approx t/2\pi$.

El objeto pendiente es **uno solo y sin ceros**: el paso de Newton del reloj con primos hasta $t/2\pi$ a la altura $t$, donde el aliasing del reloj resuena y hay que calcularlo en vez de acotarlo.

---

## 5. Resumen

| Transporte | Lo que dan los resultados de hoy | Lo que falta |
|---|---|---|
| $\zeta_{\RVM}\to\zeta$ | (T) factorización por $\zeta_C$; coincidencia del log en medida en $\Re s>\tfrac12$; energía del residual $O(1)$ frente a $\log\log T$ | conjunto excepcional vacío |
| $\zeta_{\tau^C}\to\gamma_k$ | (T) S2 + lema Ω: descomposición exacta; filtro de Wiener; índices malos $\le4d$ | colas de $r_k$ ($d<\tfrac14$); $d=0$ |
| $\pi_{\tau^C}\to\pi$ | (T) diferencia $=$ Perron de la cola prima rugosa $\sum_{n>X(t)}\Lambda(n)n^{-s}$, sin ceros | reloj con primos hasta $x$ a las alturas de Perron: resonancia $c\ge1$ |
| $M_{\tau^C}\to M$ | (T) diferencia $=$ Perron de la cola de Möbius rugosa más el defecto $1-L_C$, sin ceros; identidad exacta con corte fijo $X\ge x$ | uniformidad en $X$, o resonancia $c\ge1$; $L_C=1$ |

**Línea común, sin ceros:** para $\pi$ y $M$ la comparación es aritmética. Lo que separa los objetos Casaña de $\pi$ y $M$ es la **cola de primos que el reloj no contiene a la altura donde Perron los necesita**. El paso que falta es el reloj con primos hasta $t/2\pi$, en la resonancia $p\approx t/2\pi$, calculada en lugar de acotada. Para $\zeta\to\gamma_k$ (§2) el objeto es la proporción de índices malos, en lenguaje de ordenadas.
