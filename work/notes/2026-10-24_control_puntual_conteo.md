# Del control en media al control puntual: criterio de conteo y lo que falta

Nota de Claude, 24-oct-2026. Ruta 6.1 f del traspaso. Todo en lenguaje de ordenadas y conteo. No se evalúa $Z$ ni se usa ninguna abscisa. Sin ejecuciones numéricas.

**Fuentes.**
- [v14] `manuscript/ordinal_prime_cutoff_v14.tex`: Thm main, Thm uniform_iteration (8.x), ley de cortes (l. 1558).
- `work/notes/opc_pendiente_rutas_RH.md`: pregunta `q:corrected_gram_law`.
- [Tr] Trudgian, *Gram's law fails a positive proportion of the time*, arXiv:0811.0883, biblioteca 298: §2, pp. 2–5, Thm 1.

Notación:
- $\gamma_1\le\gamma_2\le\cdots$ son las ordenadas positivas con multiplicidad, indexadas por $N(T)$.
- $\kappa_k$ es cualquier lista construida sin ceros (reloj, primos, pasos de Newton) **ordenada**. Ordenar no aumenta ningún error $\ell^q$: Lema 8.19 de v14.
- $g_k:=\kappa_{k+1}-\kappa_k$ y $m_k:=\tfrac12(\kappa_k+\kappa_{k+1})$; error $e_k:=\kappa_k-\gamma_k$.

**Índice bueno.** $k$ es *bueno* si

$$|e_k|<\tfrac12\min(g_{k-1},g_k),\qquad\text{equivalentemente}\quad \gamma_k\in J_k:=(m_{k-1},m_k). \tag{0}$$

Los intervalos $J_k$ son disjuntos dos a dos.

---

## 1. Criterio de conteo (T)

**Lema 1.** Si $k$ y $k+1$ son buenos, entonces $\gamma_k<\gamma_{k+1}$ estrictamente.

*Prueba.* $\gamma_k\in J_k$, $\gamma_{k+1}\in J_{k+1}$ y $J_k\cap J_{k+1}=\emptyset$. $\square$

**Lema 2.** Supongamos que un cero $\rho=\beta+i\gamma$ con $\gamma\in(T,2T]$ está fuera de la recta ($\beta\ne\tfrac12$) o es múltiple. Entonces hay un índice $k$ con $\gamma_k=\gamma_{k+1}=\gamma$:
- si $\rho$ está fuera de la recta, $1-\bar\rho$ es otro cero con la misma ordenada;
- si $\rho$ es múltiple, su ordenada aparece repetida en el conteo con multiplicidad.

**Teorema 1.** Sea $d(T)$ la proporción de índices malos con $\gamma_k\in(T,2T]$. La proporción de ceros con ordenada en $(T,2T]$ que están en la recta y son simples es

$$\ \ge\ 1-4\,d(T)+o(1). \tag{1}$$

*Prueba.* Cada cero fuera de la recta o múltiple pertenece a un bloque de ordenadas iguales. Un bloque de $r\ge2$ ceros da $r-1\ge r/2$ igualdades consecutivas $\gamma_k=\gamma_{k+1}$. Por el Lema 1, cada igualdad tiene un índice malo en $\{k,k+1\}$, y cada índice malo cubre a lo sumo 2 igualdades. Por tanto el número de ceros malos es $\le2\cdot\#\text{igualdades}\le4\cdot\#\text{índices malos}$. $\square$

**Qué aporta frente a `q:corrected_gram_law`.** Allí la proporción se obtenía con la alternancia de signo de $Z$ en los $m_k$, y hacía falta una cota inferior de $|Z(m_k)|$ de tipo Selberg. El Teorema 1 **no la necesita**: solo usa ordenadas, conteo con multiplicidad y la simetría $\rho\leftrightarrow1-\bar\rho$. La recta y la simplicidad salen del conteo, que es el mecanismo de tu método.

**Consecuencias.**
- $\liminf_T(1-4d(T))>0$: una proporción positiva de ceros en la recta, demostrada por localización de ordenadas. Esto sería un método nuevo para ese tipo de teorema.
- $1-4d>\tfrac5{12}$: supera a Pratt–Robles–Zaharescu–Zeindler (referencia sin cotejar en la biblioteca).
- $d(T)\to0$: el 100 % de los ceros en la recta y simples. Es un problema abierto, más débil que RH.
- $d(T)=0$ para $T\ge T_0$: RH (más la comprobación finita) y simplicidad.

---

## 2. Qué da la teoría actual para $d(T)$ (T)

Un índice malo cumple $|e_k|\ge\eta/\Lambda$ o bien un hueco adyacente cumple $\Lambda g<2\eta$. Para todo $\eta\in(0,\tfrac12)$:

$$d(T)\ \le\ \Pr\bigl(\Lambda|e_k|\ge\eta\bigr)+2\Pr\bigl(\Lambda g_k<2\eta\bigr). \tag{2}$$

**Error.** Thm uniform_iteration de v14 da $\langle\Lambda^2e_{m^*}^2\rangle\le C'$ con $C'$ absoluta pero **no explícita**, y $\|\Lambda e_j\|_4\le C\sqrt{H_j}$. Con Chebyshev en cuarto momento,

$$\Pr\bigl(\Lambda|e|\ge\eta\bigr)\le\frac{\langle\Lambda^4e^4\rangle}{\eta^4}.$$

**Huecos.** En el último paso, con corte $X=T^{c}$, se tiene $\Lambda g_k=1-S_X'(\xi)/\Lambda+\ldots$ y

$$\Bigl\langle\Bigl(\frac{S_X'}{\Lambda}\Bigr)^2\Bigr\rangle=\frac{\tfrac12\sum_{p\le X}(\log p)^2/(\pi^2p)}{\log^2T/(4\pi^2)}\sim c^2 .$$

La fluctuación de los huecos tiene RMS $\sim c$ en unidades de espaciado. Es pequeña porque los cortes finales de la ley multietapa son pequeños.

**Conclusión.** (1)+(2) da una proporción positiva **en cuanto las constantes de v14 sean explícitas y bastante pequeñas**. Para que $1-4d>0$ hace falta $d<\tfrac14$. Ese es el trabajo concreto pendiente: explicitar $C'$, $C_\star$, $C_3$ y $C_5$ en la prueba del Thm uniform_iteration y añadir una cota de cola mejor que Chebyshev. No es un obstáculo de principio.

**Escala numérica (sin ejecutar nada nuevo).** AGENTS.md §5 da un RMS de $0.0128$–$0.0212$ en $\tau$ en el bloque de test. A altura $\sim10^6$ el espaciado medio es $2\pi/\log(10^6/2\pi)\approx0.52$, así que el error es del 2–4 % del espaciado. Si las colas son razonables, la $d$ observada es muy pequeña. La brecha está entre las constantes demostradas y las observadas, no en el método.

---

## 3. Por qué el argumento de Trudgian no se aplica a tu reloj (T)

[Tr, §2] prueba que la ley de Gram falla en una proporción positiva. Si la ley vale en una racha de intervalos, el incremento $S(t+h)-S(t)$ está acotado por 2 dentro de la racha. Pero por Fujii

$$\int_T^{2T}|S(t+h)-S(t)|^2\,dt=\pi^{-2}T\log(3+h\log T)+O\bigl(T\sqrt{\log(3+h\log T)}\bigr),$$

que con $h=C_0/\log T$ **crece como $\log C_0$**. Tomando $C_0$ grande se fuerza una proporción positiva de fallos (pp. 3–5, (13)–(21)).

Para el reloj corregido el análogo es el defecto ordinal corregido $u_k(X)$. Por el Thm main de v14 su media cuadrática está acotada uniformemente en la escala:

$$\langle u_k^2\rangle\le V_c=\frac1{2\pi^2}\log\frac1c+C\Bigl(1+\sqrt{\log\frac1c}\Bigr)\quad\Longrightarrow\quad\langle(u_{k+j}-u_k)^2\rangle\le4V_c\quad\text{para todo }j .$$

**No hay crecimiento con $C_0$.** El mecanismo que mata la ley de Gram no existe para la ley de Gram corregida. La corrección prima elimina exactamente la deriva a gran escala (los primos pequeños) que fuerza los fallos de Gram. El argumento de Trudgian no puede dar una proporción positiva de fallos de la ley corregida, y ninguna cota inferior de fallos conocida le cierra el paso a (1) con $d\to0$.

---

## 4. Lo que queda para $d(T)\to0$ (A, preciso)

La ley de v14 tiene suelo: $H_j=2\log(1/c_j)$ y $c_j\le\tfrac12$ dan $H\ge2\log2$. Si el término principal domina, $\langle\Lambda^2e^2\rangle\gtrsim\log2/(2\pi^2)\approx0.035$, que es RMS $\approx0.19$ espaciados. Con media no nula fija, $d$ no tiende a 0. Hay dos salidas:

1. **El suelo no está demostrado.** El Thm uniform_iteration da $H_m/4\pi^2+\vartheta C(1+\sqrt{H_m})$ y el error $O(1)$ domina. Los datos están muy por debajo de $0.19$ espaciados. La nota `opc_pendiente_rutas_RH.md` §4 registra un valor medido $\approx0.006$, por debajo del suelo de modelo $0.047$, con "anticorrelación transporte–defecto esencial y no explicada". **Esa anticorrelación es el objeto clave**: si se demuestra, baja el suelo.
2. **Cortes $c_j\to1$** en el último paso, con primos hasta $\approx t/2\pi$. Es el mismo punto de resonancia $p\approx t/2\pi$ que apareció en la ruta de Mertens (nota `2026-10-24_mertens_sintetico_corte_variable.md`, Teorema B′). Las dos rutas, conteo y Mertens, convergen en el mismo objeto.

**Siguiente paso concreto que propongo.** Explicitar las constantes del Thm uniform_iteration de v14 con colas de cuarto orden y evaluar si (1)+(2) da ya $d<\tfrac14$, es decir, una proporción positiva demostrada. Es trabajo de cuentas, sin obstáculo de principio conocido.
