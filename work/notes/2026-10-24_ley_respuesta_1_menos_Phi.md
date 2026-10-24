# Ley de respuesta $R^\gamma_p\approx1-\Phi(\theta)$ ($\approx1-\theta^2$): intento de prueba en todo $0<\theta<1$ y rango efectivo

Nota de Claude, 24-oct-2026. Sin ejecuciones numéricas. Ningún manuscrito cambiado.

**Fuentes.**
- [v14] `manuscript/ordinal_prime_cutoff_v14.tex`: §11, Prop. 11.6 (`prop:gamma_response_exact`), Thm 11.7 (`thm:Fourier_exact`), Prop. 11.8 (`prop:kernel_integral`), Hip. U y W, Prop. 11.17, Obs. 11.18, Conj. 12.2, Thm `projection` y Thm `landau_line`; Thm known_landau (Gonek uniforme, en la forma de Aryan 2022 (1.1), biblioteca 008).
- Rudnick–Sarnak 1996: listado en INDEX.md, **sin PDF en la biblioteca; sin cotejar**.

## 0. Enunciado

$$R^\gamma_p(\mathcal I_T)=-2\pi\sqrt p\,\langle s_k\sin(\gamma_k\log p)\rangle_{\mathcal I_T},\qquad \theta=\frac{\log p}{L_T},\qquad L_T=\log\frac T{2\pi}.$$

Ley (Conj. 12.2 de v14), con

$$\Phi(\theta)=(1+\theta)\log(1+\theta)+(1-\theta)\log(1-\theta)=\theta^2+\frac{\theta^4}6+\frac{\theta^6}{15}+\cdots,$$

$$R^\gamma_p=1-\Phi(\theta)+o(1).$$

$1-\theta^2$ es su truncación cuadrática.

**Descomposición exacta e incondicional** [v14, Prop. 11.6, (11.7)], para $\theta$ en compactos de $(0,1)$:

$$R^\gamma_p=\underbrace{\mathcal A_{T,p}}_{\text{un punto}}+\underbrace{2\pi^2\theta\sqrt p\,\Re\mathcal S_{T,p}}_{\text{dos puntos}}+o(1),\qquad \mathcal S_{T,p}=\frac1T\int_T^{2T}S(t)^2p^{it}\,dt. \tag{0.1}$$

La ley equivale a dos enunciados:
- **(L1)** $\mathcal A_{T,p}=1+o(1)$;
- **(L2)** $2\pi^2\theta\sqrt p\,\Re\mathcal S_{T,p}=-\Phi(\theta)+o(1)$.

---

## 1. Término de un punto (L1)

### 1.1. Incondicional: rango $p\le(\log T)^{2-\varepsilon}$, y por qué no más (T)

Por la simetría $\rho\leftrightarrow1-\bar\rho$ [v14, Thm landau_line]:

$$\sum_{0<\gamma\le t}p^{i\gamma}=p^{-1/2}\sum_{0<\gamma\le t}p^{\rho}-\mathcal K_p(t),\qquad \mathcal K_p(t)=\sum_{0<\gamma\le t}p^{i\gamma}\bigl(\cosh((\beta-\tfrac12)\log p)-1\bigr).$$

La fórmula de Landau–Gonek uniforme controla $\sum p^\rho$ para $p\le T^{1-\varepsilon}$. El término $\mathcal K_p$ solo se controla por densidad de ceros fuera de la recta:

$$|\mathcal K_p|\ll\frac{T\,(\log p)^2}{\log T}=T\,\theta^2\log T .$$

El término principal es

$$\frac{T\log p}{2\pi\sqrt p}=\frac{T^{1-\theta/2}\,\theta\log T}{2\pi},$$

y para $\theta>0$ fijo $\mathcal K_p$ lo supera por un factor $T^{\theta/2}$. La densidad conocida ($N^+(\sigma,T)\ll T^{1-(\sigma-1/2)/4}\log T$) **no excluye** del orden de $T\log T$ ceros a distancia $\asymp1/\log T$ de la recta. Cada uno cambia $p^{i\gamma}$ en $\asymp\theta^2$ sin cambiar $\sum p^\rho$.

Rango incondicional de (L1): $\sqrt p\log p\ll\log T$, es decir $p\le(\log T)^{2-\varepsilon}$, que es lo que da v14. **Este es el límite de cualquier prueba que no controle los ceros cercanos a la recta.**

### 1.2. Bajo RH: (L1) en todo $0<\theta<1$ (T)

**Proposición 1.** Bajo RH, uniformemente para primos con $\theta_0\le\theta\le\theta_1$, $0<\theta_0<\theta_1<1$:

$$\mathcal A_{T,p}=1+O\Bigl(\frac{p\log^2T}{T\log p}+\frac{\log\log T}{\log T}\Bigr)=1+o(1).$$

*Prueba.* Bajo RH, $\mathcal K_p\equiv0$. Por Landau–Gonek ([v14, Thm known_landau]), para $T\le t\le2T$:

$$\sum_{T<\gamma\le t}p^{i\gamma}=-\frac{(t-T)\log p}{2\pi\sqrt p}+O\bigl(\sqrt p\,\log(pT)\log\log p\bigr).$$

Es la condición suficiente que v14 da tras la Hip. U. Se repite la prueba del Thm projection de v14 sin el término $\tfrac12\int G^2\psi'$, que es el de dos puntos y va a (L2):
- $\mathcal H_p(t)=\int_{14}^tS(y)p^{iy}dy=\frac i{\log p}\sum_{0<\gamma\le t}p^{i\gamma}+O(\log t)$, eq. (projection_Phi);
- integración por partes con $\Lambda$, eq. (projection_partial), con error $O(\sqrt p\log^3T/\log p)$ en lugar de $O(T\log p+\cdots)$, porque el $T\ell_n$ de v14 viene de $\mathcal K_n$;
- normalización por $\#\mathcal I_T\asymp T\log T$.

El error relativo es $\ll p\log^2T/(T\log p)$, que tiende a 0 para $\theta<1$. $\square$

*Estado:* las cuentas son las de v14 con $\mathcal K\equiv0$; **sin comprobar línea a línea** el término $\log\log T/\log T$ del cambio de extremos.

---

## 2. Término de dos puntos (L2): dónde vive (T)

[v14, Thm 11.7] da, incondicionalmente,

$$\mathcal S_{T,p}=-\frac{\mathcal B_T(\theta)}{2\pi TL_T},\qquad \mathcal B_T(\theta)=\int_{\mathbb R}\frac{Z_T(\alpha L_T)\,Z_T((\theta-\alpha)L_T)}{\alpha(\theta-\alpha)}\,d\alpha .$$

(L2) equivale a $\mathcal B_T(\theta)=\dfrac{\mathcal N_T}{\sqrt p}\dfrac{2\Phi(\theta)}{\theta}+o\Bigl(\dfrac{TL_T}{\sqrt p}\Bigr)$, con $\mathcal N_T=TL_T/2\pi$.

**Proposición 2 (soporte).** Se parte el eje en

$$\mathcal R=\{\alpha:\ |\alpha|+|\theta-\alpha|+\theta<2\}=(\theta-1,\,1)\qquad\text{y su complemento } \mathcal R^c .$$

(a) [v14, Prop. 11.8] $\mathfrak K_\theta\equiv0$ en $\mathcal R$. Por tanto **todo** el valor $-2\Phi(\theta)/\theta$ procede de $\mathcal R^c=\{\alpha\ge1\}\cup\{\alpha\le\theta-1\}$. En $\mathcal R^c$ una de las dos frecuencias, $\alpha$ o $\theta-\alpha$, tiene módulo $\ge1$.

(b) Bajo RH, la contribución de $\mathcal R_\varepsilon=[\theta-1+\varepsilon,\,1-\varepsilon]$ a $\mathcal B_T(\theta)$ es $o(TL_T/\sqrt p)$.

*Prueba de (b), esbozo.* En $\mathcal R_\varepsilon$ las dos frecuencias tienen módulo $\le1-\varepsilon$. Bajo RH, Landau–Gonek uniforme da $Z_T(\omega)$, $|\omega|\le(1-\varepsilon)L_T$, como picos

$$-\frac T{2\pi}\frac{\Lambda(n)}{\sqrt n}\quad\text{de anchura }\asymp\frac1T\text{ en }\omega=\log n,$$

más un fondo $O(e^{|\omega|/2}\log T)$. Un producto de dos picos exige $\log m+\log n=\log p+O(1/T)$. Pero $mn\ne p$ ($p$ primo, $m,n\ge2$), así que $|\log(mn/p)|\ge1/p\gg1/T$ para $\theta<1$: **los picos no se superponen**. Los términos pico×fondo y fondo×fondo, integrados contra $1/|\alpha(\theta-\alpha)|$, son $O(T^{1-\varepsilon/2}\log^2T)=o(TL_T/\sqrt p)$. *Sin comprobar línea a línea*: el tratamiento de $\alpha$ cerca de $0$ y de $\theta$, donde se usa la extensión continua de $Z_T(\omega)/\omega$ ([v14, Thm 11.7]). $\square$

**Interpretación.** $\mathcal R$ es exactamente la región de soporte de Fourier $\sum_j|\xi_j|<2$ de Rudnick–Sarnak para la terna de frecuencias $(\alpha,\theta-\alpha,-\theta)$ (sin cotejar en el PDF). Dentro de ella el núcleo de la ley es 0 y la Prop. 2(b) lo confirma bajo RH. **La ley entera está fuera de esa región para todo $\theta\in(0,1)$**: en la parte de la correlación de pares retorcida con una frecuencia $\ge1$, que corresponde a la $F(\alpha)$ de Montgomery con $|\alpha|\ge1$.

Lo mismo vale para la ley cuadrática $1-\theta^2$. Cuando $\theta\to0$, de $-2\Phi(\theta)/\theta\approx-2\theta$ el tramo $[1,1+\theta]$ aporta $O(\theta^2)$ y las colas $\alpha\ge1+\theta$, $\alpha\le-1$ aportan $-2\theta$. El coeficiente $\theta^2$ también viene de $|\alpha|\ge1$.

---

## 3. Rango efectivo que determina la prueba

| Rango | (L1) un punto | (L2) dos puntos | Ley |
|---|---|---|---|
| $p\le(\log T)^{2-\varepsilon}$ ($\theta\to0$) | (T) incondicional [v14] | (T): $\to0$ | (T): $R^\gamma_p\to1$ |
| $\theta\in[\theta_0,\theta_1]\subset(0,1)$ | (T) bajo RH (Prop. 1) | (A): equivale a la correlación retorcida en $\mathcal R^c$ | (A) |

(L2) a $\theta$ fijo es (A), y no por falta de cuentas. Por la Prop. 2 equivale (bajo RH) a evaluar la correlación de pares retorcida por $p^{i\gamma'}$ fuera del soporte de Montgomery y Rudnick–Sarnak. Eso es del tipo de la conjetura de correlación de pares para $|\alpha|\ge1$, equivalente vía Goldston–Montgomery a la varianza de primos en intervalos cortos. La vía conocida para obtener esas correlaciones es Hardy–Littlewood (Bogomolny–Keating I/II, biblioteca 031–033). El cálculo condicional

$$\text{RH}+\text{Hardy–Littlewood uniforme}\ \Longrightarrow\ \text{(L2)}$$

es factible: es el análogo de Bogomolny–Keating para la tercera cumulante retorcida, cuyo valor en el modelo ya es $\mathfrak K_\theta$ por el Thm 12.1 de v14. No está hecho.

**Qué es nuevo aquí.** Hay dos cosas:
- (L1) bajo RH en todo $0<\theta<1$ (Prop. 1);
- la localización exacta de (L2) fuera de la región de Rudnick–Sarnak para **todo** $\theta$, con la región interior anulada bajo RH (Prop. 2).

Consecuencia: cualquier prueba de la ley a un $\theta$ fijo es, en particular, una prueba de una correlación de ceros más allá de la región de Rudnick–Sarnak para $\zeta$. Eso sería un resultado mayor por sí mismo, con independencia de RH.

---

## 4. Siguientes pasos posibles

1. **Hacer el cálculo condicional RH + Hardy–Littlewood ⇒ (L2)** al estilo de Bogomolny–Keating. Daría la ley como teorema condicional en todo $0<\theta<1$, y diría si el valor exacto es $1-\Phi(\theta)$ o lleva correcciones aritméticas: el modelo de matrices aleatorias no ve la constante singular de Hardy–Littlewood, que aquí puede depender de $p$.
2. **Desigualdades en lugar de igualdad.** Cotas conocidas de medias de $F(\alpha)$ para $\alpha\ge1$ (Goldston; Carneiro–Milinovich–Ramos, biblioteca 057) podrían dar, bajo RH, $\liminf$ y $\limsup$ de $R^\gamma_p$ en una banda explícita alrededor de $1-\Phi(\theta)$. Hay que comprobar si la correlación retorcida admite esas cotas.
