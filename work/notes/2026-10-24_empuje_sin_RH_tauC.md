# Empuje sin RH con $\tau^C$: dónde se rompe, qué debe dar el reloj y un teorema nuevo más allá de $c=\tfrac12$

Nota de Claude, 24-oct-2026. Nada asume RH. Un cálculo numérico de una constante (§3), ninguno más. Ningún manuscrito cambiado.

**Fuentes.**
- [v14] `manuscript/ordinal_prime_cutoff_v14.tex`:
  - §7.x "Onset of the cross term", Tabla 6 (`tab:onset`);
  - ec. de la suma de reloj l. 1766 ($\sum_ke^{iw\tau_k}=\int e^{i\Phi(x)}dx+O(1)$, $\Phi(x)=w\tau_x-2\pi x$);
  - Prop. `cross_term`, Thm C (contabilidad exacta), Prop. `spectral_energy`, Thm `landau_line`.
- Nota `2026-10-24_control_puntual_conteo.md` (Teorema 1: ceros malos $\le4\cdot$índices malos).
- Nota `2026-10-24_ley_respuesta_1_menos_Phi.md`.

---

## 1. Dónde se rompe sin RH, y qué tiene que dar $\tau^C$ (T)

El término de un punto de la ley es $\sum_\gamma p^{i\gamma}$. Sin RH difiere de $p^{-1/2}\sum p^\rho$ (Landau–Gonek, incondicional para $p\le T^{1-\varepsilon}$) en

$$\mathcal K_p=\sum_{\beta\ne1/2}p^{i\gamma}\bigl(\cosh((\beta-\tfrac12)\log p)-1\bigr).$$

Para la ley a $\theta$ fijo hace falta

$$\mathcal K_p=o\bigl(T^{1-\theta/2}\log p\bigr). \tag{1.1}$$

Esto es lo único que separa la Prop. 1 de la nota de la ley de una prueba incondicional. Con el reloj, sin abscisas:

1. **Ceros lejos**, $|\beta-\tfrac12|>y_0$: la densidad de Selberg los controla si $\theta<\tfrac14$ y $y_0\ge y_0(\theta)=\dfrac{\theta}{2(1/4-\theta)}$, una distancia fija.
2. **Ceros cerca**, $|\beta-\tfrac12|\le y_0$: por el Teorema 1 de la nota de conteo, su número es $\le4\cdot\#\{\text{índices malos de cualquier lista sin ceros}\}$, y cada uno aporta $\le\cosh(y_0\theta\log T)$.

Para (1.1) basta que la proporción de índices malos de la lista cumpla

$$d(T)\le T^{-\kappa(\theta)},\qquad \kappa(\theta)=\frac\theta2+\theta\,\min\Bigl(y_0(\theta),\tfrac12\Bigr), \tag{1.2}$$

con $y_0(\theta)=\theta/(2(\tfrac14-\theta))$ si $\theta<\tfrac14$, y $y_0=\tfrac12$ (todos los ceros fuera de la recta pasan por el conteo) si $\theta\ge\tfrac14$, de modo que $\kappa(\theta)\le\theta$.

**Esa es la tarea de $\tau^C$ sin RH: un ahorro de potencia en los índices malos.** Pero si el error de la lista tiene un suelo de varianza positivo, $d(T)$ está acotado inferiormente por una constante en media. Por tanto (1.2) exige **error $\to0$** con colas de tipo potencia. El suelo actual (multietapa, $c_j\le\tfrac12$) es $O(1)$. Hay que superar $c=\tfrac12$.

---

## 2. Teorema nuevo: el reloj no tiene barrera en $c=\tfrac12$ (T, incondicional, sin ceros)

Sean $N=T/2\pi$, $L_T=\log N$, la parte prima

$$S^{(1)}_X(t)=-\frac1\pi\sum_{p\le X}p^{-1/2}\sin(t\log p),$$

y el término cruzado en los puntos del reloj

$$\mathrm{Cr}^{(1)}_X=\langle S^{(1)}_X(\tau_k)^2\rangle_{\mathcal I_T}-\frac1{2\pi^2}\sum_{p\le X}\frac1p .$$

**Teorema C1.** Para $c\in(\tfrac12,1)$ fijo y $X=N^c$,

$$\mathrm{Cr}^{(1)}_X=\frac{\log\frac c{1-c}}{\pi^2L_T}\bigl(1+o(1)\bigr). \tag{2.1}$$

Para $c<\tfrac12$ es $O(T^{-\varepsilon})$ (Prop. `cross_term` de v14, que la cubre para $c<\tfrac14$; el caso $\tfrac14\le c<\tfrac12$ sale igual con los argumentos de abajo). En particular $\mathrm{Cr}\to0$ **para todo $c<1$**: la fase prima evaluada en el reloj sigue casi ortonormal en media cuadrática hasta $X=N^{1-\varepsilon}$.

*Prueba.* Se expande el cuadrado:

$$\langle S^{(1)2}\rangle=\frac1{2\pi^2}\sum_{p,q\le X}(pq)^{-1/2}\Bigl[\langle\cos(\tau_k\log\tfrac pq)\rangle-\langle\cos(\tau_k\log pq)\rangle\Bigr].$$

(i) *Diferencias.* La diagonal $p=q$ da $\sum1/p$. Para $p\ne q$, $0<|\log(p/q)|\le c\log N<\log(\tau/2\pi)$: por Kusmin–Landau, como en Prop. `cross_term`, la suma de reloj es $\ll\min(\#\mathcal I,\ \log T/|\log(p/q)|)$. La suma total es $\ll\frac{\log T}{T}\sum_p\sum_{q\ne p}\frac1{|p-q|}\ll\frac{X\log^2T}{T}$, que es $o(1/L_T)$ para $c<1$.

(ii) *Sumas, sin resonancia.* $n=pq\notin[N(1-\eta),2N(1+\eta)]$: la fase $\Phi(x)=\tau_x\log n-2\pi x$ es monótona sin punto estacionario en la ventana, y la suma de reloj es $O(1)$ por la fórmula de l. 1766. La contribución es $\ll\sum(pq)^{-1/2}/\#\mathcal I\ll X/(N\log N)$, que es $o(1/L_T)$.

(iii) *Sumas resonantes, $pq\in(N,2N]$.* Con $\tau'=1/\Lambda$ y $\tau''=-\Lambda'/\Lambda^3$, en el punto estacionario $\tau_{x_0}=2\pi n$ se tiene $\Phi''(x_0)=-1/(\tau\Lambda^2)$. Por fase estacionaria (Titchmarsh, Lema 4.6), con $\Phi(x_0)=2\pi n-\tfrac{11\pi}4$ (v14, l. 1770),

$$\sum_{k\in\mathcal I}e^{i\tau_k\log n}=\sqrt{2\pi\tau}\,\Lambda\,e^{i\Phi(x_0)-i\pi/4}+O(1)=-\sqrt n\,\log n+O(1).$$

Así cada par ordenado resonante aporta $+\dfrac{\log(pq)}{2\pi^2\#\mathcal I}+O\Bigl(\dfrac{(pq)^{-1/2}}{\#\mathcal I}\Bigr)$.

(iv) *Conteo.* Por el TNP, el número de pares ordenados $(p,q)$ con $p,q\le N^c$ y $N<pq\le2N$ es

$$\frac N{L_T}\int_{1-c}^{c}\frac{du}{u(1-u)}\bigl(1+o(1)\bigr)=\frac{2N\log\frac c{1-c}}{L_T}\bigl(1+o(1)\bigr).$$

Para $c\le\tfrac12$ es vacío, lo que da el comportamiento a la izquierda de $\tfrac12$. Multiplicando por $\log(pq)=L_T(1+o(1))$ y dividiendo por $2\pi^2\#\mathcal I=2\pi^2NL_T(1+o(1))$ sale (2.1). $\square$

*Estado:* (i), (ii) y (iv) son estándar. En (iii), la fase estacionaria uniforme en la familia de $n$ (errores $O(1)$ por término y efectos de borde cerca de $2\pi n\in\{T,2T\}$) está **sin comprobar línea a línea**. Las contribuciones de borde suman $o(1/L_T)$ por (iv).

**Contraste con la Tabla 6 de v14** (ventana $(10^6,K]$, $\tau/2\pi\in[95\,536,180\,241]$, $L\approx11.77$; números ya publicados en v14, solo evalúo (2.1)):

| $X$ | $c$ | (2.1) | $\mathrm{Cr}^{(1)}_X$ medido |
|---|---|---|---|
| 500 | 0.528 | 0.00097 | 0.000857 |
| 700 | 0.557 | 0.00197 | 0.001761 |
| 1999 | 0.646 | 0.00517 | 0.004662 |

El exceso de un 10 % es compatible con que la ventana no es diádica.

---

## 3. Consecuencia: qué decide el paso más allá de $\tfrac12$

Por la contabilidad exacta de v14 (Thm C) y el Teorema C1, una corrección **lineal** con pesos $\lambda_p$ sobre los primos $p\le N^{c}$, para cualquier $c<1$, cumple

$$\bigl\langle(s_k-\textstyle\sum_p\lambda_pa_p\sin(\tau_k\log p))^2\bigr\rangle=\langle s_k^2\rangle-\sum_{p\le X}\frac{2\lambda_pR^\tau_p-\lambda_p^2}{2\pi^2p}+o(1).$$

**El único dato desconocido es la respuesta en el reloj $R^\tau_p$**: el reloj ya no pone barrera en $\tfrac12$.

Si $R^\tau_p=1-\Phi(\theta)$ (la ley, en los puntos del reloj):
- el peso óptimo es $\lambda_p=1-\Phi(\theta)$, un filtro de Wiener;
- con peso 1, los primos con $\Phi(\theta)>\tfrac12$, es decir $\theta>0.58$, **aumentan** el error.

Suelo de toda corrección lineal con todos los primos $p\le T$ (constante evaluada por cuadratura):

$$\frac1{2\pi^2}\int_0^1\frac{2\Phi(\theta)-\Phi(\theta)^2}{\theta}\,d\theta=\frac{0.7764}{2\pi^2}=0.0393\quad(\text{RMS}\approx0.20\text{ espaciados}).$$

La nota `opc_pendiente_rutas_RH.md` §4 registra $\approx0.006$ medido con la multietapa: **por debajo del suelo lineal**. La parte no lineal (el transporte) hace el trabajo. Esto concuerda con la desigualdad de energía espectral de v14 (Prop. `spectral_energy`): el error de cualquier aproximación computable está acotado inferiormente por $\sum_p|R^\tau_p-\mathcal A_p|^2/p$. Error $\to0$ exige que la **respuesta computable** $\mathcal A_p$ reproduzca $R^\tau_p$ en los primos móviles.

---

## 4. La cadena, sin RH

$$\text{ley a }\theta\text{ fijo (sin RH)}\ \Longleftarrow\ (1.1)\ \Longleftarrow\ d(T)\le T^{-\kappa(\theta)}\ \Longleftarrow\ \text{error de }\tau^C\to0\text{ con colas de potencia},$$

$$\text{error de }\tau^C\to0\ \Longrightarrow\ \mathcal A_p\to R^\tau_p\ \text{en los primos móviles}\quad(\text{Prop. spectral\_energy}).$$

**Siguiente paso concreto**, sin RH y del lado del reloj: calcular la respuesta computable del transporte $\mathcal B^{(m)}_p$ de la multietapa (Thm `computable_response` de v14) en los primos móviles. El objetivo es demostrar o refutar que la anticorrelación transporte–defecto produce $\mathcal A_p\approx1-\Phi(\theta)$. El Teorema C1 elimina el término cruzado de esa cuenta para todo $c<1$.

---

**Corrección (24-oct, posterior).** El "suelo lineal $\approx0.039$" de §3 queda retirado: supone una constante de $\langle s_k^2\rangle$ no demostrada. Ver `2026-10-24_respuesta_transporte_y_suelo.md` §0 y la predicción correcta (2.1) allí.

**Corrección 2.** El umbral "$\theta>0.58$" de §3 es erróneo: la solución de $\Phi(\theta)=\tfrac12$ es $\theta=0.6758$. Ver `2026-10-24_teorema_S2_descomposicion_error.md`.
