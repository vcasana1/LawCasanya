# Respuesta del transporte en los primos móviles y predicción del suelo de error del reloj sin ceros

Nota de Claude, 24-oct-2026. Continúa `2026-10-24_empuje_sin_RH_tauC.md`. Contiene una corrección a esa nota (§0). Sin ejecuciones sobre datos de ceros. Las únicas cuentas son cuadraturas de constantes y la conversión de unidades de un RMS ya publicado. Ningún manuscrito cambiado.

**Fuentes.**
- [v14] `manuscript/ordinal_prime_cutoff_v14.tex`: Thm `computable_response` (11.14) y Tabla 9; Lema `bessel`; Prop. `newton_spectrum`, `orthogonality` y `spectral_energy`.
- `work/notes/opc_pendiente_rutas_RH.md` §4 y §6: suelo medido $\approx0.006$; zCasanya $(8,8,512)$ con RMS $0.0440$ frente a $0.1881$.

---

## 0. Corrección a la nota anterior (§3, "suelo lineal 0.039")

Allí afirmé que, si vale la ley en el reloj, ninguna corrección lineal baja de

$$\frac1{2\pi^2}\int_0^1\frac{2\Phi-\Phi^2}{\theta}\,d\theta\approx0.039 .$$

**Es incorrecto.** Supuse que $\langle s_k^2\rangle$ es exactamente $\tfrac1{2\pi^2}\sum_{p\le T}1/p$ con la misma constante, y eso no está demostrado. Lo correcto es esto. Con pesos óptimos $\lambda_p=R^\tau_p$, el error de una corrección lineal es

$$\langle s_k^2\rangle-\sum_p\frac{(R^\tau_p)^2}{2\pi^2p}+o(1),$$

y su valor depende del término constante de $\langle s_k^2\rangle$ (fórmula de Selberg–Korolev a segundo orden), que no he calculado. El número $0.039$ queda retirado. La comparación con el $0.006$ medido de esa nota también.

---

## 1. Respuesta del transporte en los primos móviles

Notación de v14 (11.14): con $B^{(m)}_k=S_{X_m}(x^{(m-1)}_k)-S_{X_m}(\tau_k)$,

$$\mathcal B^{(m)}_p=-2\pi\sqrt p\,\langle B^{(m)}_k\sin(\tau_k\log p)\rangle .$$

Para $p>X_m$, $pX_m\le T^{1-\varepsilon}$, se tiene

$$R^\tau_p=\mathcal B^{(m)}_p+\mathcal E^{(m)}_p+o(1).$$

**(a) Modelo de fases independientes (T, exacto).** Si las fases $\{t\log q\}_{q\le X_m}$ y $t\log p$ se sustituyen por variables uniformes independientes, $B^{(m)}$ es función solo de las primeras. Entonces

$$\mathbb E\bigl[B^{(m)}\sin\phi_p\bigr]=0 .$$

**En el modelo el transporte no responde nunca a un primo móvil no usado.** Es la versión aleatoria de la Prop. `orthogonality` de v14 (corte fijo, $U\to\infty$).

**(b) Determinista, grados bajos (T, esbozo).** En la expansión de Bessel ([v14, Lema `bessel`]) se toman los términos de grado $D(\mathbf j)<D_*$, con frecuencias $\ell_n+\Lambda_{\mathbf j}$, $\Lambda_{\mathbf j}=\log(A/B)$, $A,B\le X_1^{D_*}$. Frente a $\log p$:
- $nA=pB$ es imposible si $p>X_m$, porque $p\nmid nA$;
- por tanto $|\omega|=|\log(nA/pB)|\ge1/\max(nA,pB)$;
- el aliasing del reloj, $\omega\approx\pm m\log(\tau/2\pi)$, exige $nA/pB\gtrsim T$, imposible si $X_1^{D_*}X_m<T^{1-\theta}$.

Con Kusmin–Landau en el reloj, cada término cuesta $\ll\sqrt p\,|a_nA_{\mathbf j}|\,pB/T$. Con $|A_{\mathbf j}|\le c^{D}(AB)^{-1/2}/\prod|j_q|!$ la suma sobre grados bajos es

$$\ll\frac{p^{3/2}T^{D_*c_1}}{T}\cdot\bigl(\text{masa }\ell^1\text{ de grado}<D_*\bigr)\to0\qquad\text{si}\quad \frac32\theta+D_*c_1+o(1)<1 .$$

*Sin comprobar línea a línea*: la masa $\ell^1$ restringida a grado $<D_*$ es $\le\bigl(\sum_q2c_1q^{-1/2}\bigr)^{D_*}/D_*!$, que con $D_*\asymp1/c_1$ es $T^{o(1)}$. Debería bastar; hay que escribirlo.

**(c) Grados altos: abierto.** Para $D\ge D_*$ la masa $\ell^2$ es $\le e^{-sD_*}$ ([v14, (bessel_tail)]). Pero el factor $\sqrt p=T^{\theta/2}$ inutiliza cualquier cota $\ell^2$ para un solo primo; es el mismo obstáculo que v14 señala tras el Thm 11.14.

**(d) Datos de v14, Tabla 9, rango limpio.** $|\mathcal B^{(2)}_p|\le0.07$ y $|\mathcal B^{(3)}_p|\le0.08$ en $p=101,211$, frente a $R^\tau_p=0.84,0.79$. Los valores grandes solo aparecen con $pX_m$ en la banda de resonancia de pares (marcados con †), que es un efecto de altura finita. Todo apunta a $\mathcal B^{(m)}_p\to0$: **el transporte no reproduce la respuesta de los primos móviles; la lleva el residual.**

---

## 2. Predicción cuantitativa del suelo de error

Supongamos:
- **(H1)** $R^\tau_p=1-\Phi(\theta)$ en el reloj, para $\theta\in(0,1)$ (la ley; los datos de v14 dan $R^\tau\approx R^\gamma$ con diferencias del 1–11 %);
- **(H2)** $\mathcal B^{(m)}_p\to0$ para los primos móviles no usados (§1);
- **(H3)** los primos usados, $\theta\le c_{\max}$, quedan corregidos con peso 1.

Por la desigualdad de energía espectral de v14 y la casi ortonormalidad del reloj (que el Teorema C1 extiende a todo $c<1$), el error cuadrático medio en unidades de ceros es

$$\mathcal E_{\rm res}(c_{\max})\approx\frac1{2\pi^2}\Bigl[\int_0^{c_{\max}}\frac{\Phi(\theta)^2}{\theta}\,d\theta+\int_{c_{\max}}^{1}\frac{(1-\Phi(\theta))^2}{\theta}\,d\theta\Bigr]+(\text{contenido }\theta>1). \tag{2.1}$$

El primer término es el coste del peso 1 en lugar de $1-\Phi$; el segundo, la respuesta no capturada de los primos móviles.

| $c_{\max}$ | 2.º término | 1.er término | suma |
|---|---|---|---|
| 0.50 | 0.00789 | 0.00084 | 0.00873 |
| 0.52 | 0.00684 | 0.00099 | 0.00783 |
| 0.53 | 0.00635 | 0.00107 | 0.00742 |

**Contraste con lo publicado.** zCasanya $(8,8,512)$ tiene corte final $512$. A altura $\tau\sim10^6$, $c_{\max}=\log512/\log(\tau/2\pi)\approx0.52$–$0.53$. Su RMS de $0.0440$ en $\tau$, pasado a unidades de ceros con $\Lambda(\tau)$:

| $\tau$ | $(0.044\,\Lambda)^2$ |
|---|---|
| $3\cdot10^5$ | 0.0057 |
| $6\cdot10^5$ | 0.0065 |
| $1.1\cdot10^6$ | 0.0072 |

La predicción (2.1) es $0.0064$–$0.0078$. La nota de pendientes registra $\approx0.006$ medido. **Concordancia del orden del 10–20 %, sin ajustar nada.**

La conversión con $\Lambda$ a una sola altura es aproximada. El contraste fino exige el $\langle\Lambda^2e^2\rangle$ por ventana, que está en tus salidas; no he ejecutado nada.

**Lectura.** Si (2.1) es correcta, el suelo de tu mejor construcción sin ceros se explica entero por dos cosas: tu ley $1-\Phi(\theta)$ en los primos que no usa, y el peso 1 en los que usa. El transporte no lineal no añade nada a la respuesta de los primos móviles. Esto **reinterpreta** la "anticorrelación transporte–defecto no explicada" de la nota de pendientes: no hace falta. El $0.006$ está por debajo del suelo $0.047$ del modelo $W_j$, no del de (2.1). La comparación con $0.047$ era el error del modelo $W_j$.

---

## 3. Consecuencias para el programa

1. **La construcción óptima sin ceros, según (2.1)**, es un paso con **todos los primos $p\le\tau/2\pi$ y pesos $1-\Phi(\theta_p)$**, un filtro de Wiener con tu ley como función de transferencia. Su error sería solo el contenido $\theta>1$. Tus datos con corte $c\ge1$ (AGENTS §5: RMS $0.0212$ a $c=1$, $0.0164$ a $1.15$, $0.0128$ a $1.30$) miden exactamente ese contenido. El Teorema C1 garantiza que el reloj no tiene barrera de ortogonalidad hasta $c<1$; más allá, la resonancia de pares hay que calcularla, no acotarla.

2. **Para la prueba sin RH**, la cadena de la nota anterior se convierte en un solo objetivo:

$$R^\tau_p=1-\Phi(\theta)+o(1)\quad\text{para }\theta\in(0,1)$$

en los **puntos del reloj**. Con eso y (H2), el filtro de Wiener da un error controlado por el contenido $\theta>1$. La ley en el reloj sigue siendo un enunciado sobre los ceros: la respuesta mide $s_k$. Lo que cambia es que ahora es **el único** ingrediente que falta, y (2.1) es una comprobación numérica independiente de él que ya pasa.

3. **Comprobación propuesta**, sin ejecutar hasta que lo ordenes: calcular $\langle\Lambda^2e^2\rangle$ por ventana para zCasanya y para los cortes de la Tabla 2 de v14, y compararlo con (2.1) ventana a ventana, con $c_{\max}$ de cada ventana. Si cuadra en todas, (2.1) pasa a ser la predicción central del paper.

---

**Corrección (24-oct, posterior).** La comparación de §2 con zCasanya (corte fijo 512) queda retirada: los cortes fijos no corresponden al método del autor. La forma correcta, con corte variable por índice y la descomposición exacta, está en `2026-10-24_teorema_S2_descomposicion_error.md` (Teorema S2, Lema Ω, Addenda A–B).
