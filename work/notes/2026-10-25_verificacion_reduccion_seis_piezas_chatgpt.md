# Verificación de la reducción de ChatGPT del momento ponderado $1/12$ a dos respuestas en las ordenadas

Nota de Claude, 25-oct-2026. Documento revisado: "Ataque al momento ponderado 1/12 de la vía Casaña–Mertens" (ChatGPT, adjunto del autor). Sin ejecuciones numéricas.

## 1. Las identidades son correctas

Notación: $Q=N-N_0$ (continua por la derecha, saltos $m_\gamma$, $Q'=-\Lambda$ entre saltos), $P\in C^1$, $F=N_0+P$, $Q^*(\gamma)=N^*(\gamma)-N_0(\gamma)$.

- **(3)** $C-2\int QPP'+H=\sum_\gamma m_\gamma P(\gamma)^2+\bigl[-QP^2+\tfrac{P^3}3\bigr]_a^b$. Correcta: $2\int QPP'=\int Q\,d(P^2)=[QP^2]-\int P^2dQ$ y $dQ=dN-\Lambda dt$. Hay un desliz de notación: en (1) $E=2\int QPP'$ entra con signo menos y en (3) se escribe "$C+E+H$" con $E=-\int Q\,d(P^2)$; el resultado es el correcto.
- **(4)** $-2\int\Lambda QP+\int Q^2P'=[Q^2P]_a^b-2\sum_\gamma m_\gamma Q^*(\gamma)P(\gamma)$. Correcta: usa $d(Q^2)=-2\Lambda Q\,dt+\sum2m_\gamma Q^*(\gamma)\delta_\gamma$, que es el lema de medidas de v14 (`first_moment_measures`).
- **(5)** $\int_a^b(N-F)^2dF=\int_a^b\Lambda Q^2dt+\sum_\gamma m_\gamma[P(\gamma)^2-2Q^*(\gamma)P(\gamma)]+\bigl[Q^2P-QP^2+\tfrac{P^3}3\bigr]_a^b$. Correcta.
- **Comprobación cruzada.** Con la identidad exacta de v16 ($\sum u^2=\int(N-F)^2dF-\frac M{12}+\frac{[(Q-P)^3]}3$) y la descomposición ($\sum u^2=\sum mQ^{*2}-2\sum mQ^*P+\sum mP^2+\mathsf V_T$), (5) equivale a su caso $P=0$:
$$\boxed{\ \int_a^b\Lambda Q^2\,dt=\frac{M}{12}+\sum_\gamma m_\gamma Q^*(\gamma)^2+\mathsf V_T-\Bigl[\frac{Q^3}3\Bigr]_a^b\ }$$
(los bordes casan: $\frac{(Q-P)^3}3+Q^2P-QP^2+\frac{P^3}3=\frac{Q^3}3$). Es consistente.
- **(6), (9), (10), (19):** correctas. (19): $\frac1T\int|(S^{(1)}_X)'|^2\sim\frac1{2\pi^2}\sum_{p\le X}\frac{\log^2p}p\sim\frac{\log^2X}{4\pi^2}$, y el cociente con $\Lambda$ es $c$.

## 2. Qué añade esto a lo que había (tres cosas que conviene destacar)

**(a) Los términos con peso $P'$ desaparecen exactamente.** La preocupación de v18 (`rem:second-order-constant`: "falta controlar el término con peso $S_X'$") y la mía (nota de $E_T$, §5.4) quedan resueltas: $D$ y $E$ se absorben por partes. Toda la dependencia de $P$ está en la forma cuadrática **muestreada en las ordenadas verdaderas**:
$$I_T(P)-I_T(0)=\frac1M\sum_\gamma m_\gamma\bigl[P(\gamma)^2-2Q^*(\gamma)P(\gamma)\bigr]+\text{borde}.$$

**(b) La multiplicidad está dentro de la constante de segundo orden de $\int\Lambda S^2$.** La identidad recuadrada arriba dice, con $Q=S+O(1/t)$ fuera de las ordenadas:
$$\frac1M\int_a^b\Lambda S^2\,dt=\frac1{12}+\mathcal V_0(T)+\frac{\mathsf V_T}{M}+\text{borde}+o(1),\qquad \mathcal V_0=\frac1M\sum_\gamma m_\gamma Q^*(\gamma)^2 .$$
Es decir: media cuadrática continua de $S$ con peso $\Lambda$ $=$ $\frac1{12}$ $+$ media cuadrática discreta de $S$ en los ceros (valor medio del salto) $+$ energía de multiplicidad. Las tres son exactas. Es la forma precisa de lo que dije sobre Goldston: la constante de segundo orden de $\int S^2$ lleva la multiplicidad. Para ceros simples, $Q^*(\gamma_k)=s_k$, así que $\mathcal V_0$ es la $\langle s_k^2\rangle$ de v14 (Fujii: $\sum_{\gamma\le T}S(\gamma)^2\sim\frac{T}{4\pi^3}\log T\log\log T$, consistente).

**(c) $\mathcal C$ y $\mathcal P$ son objetos ya definidos en el programa.** Con $P=\sum_na_nw_n\sin(\cdot\log n)$ y ceros simples:
- $\mathcal C(T;P)=\frac1M\sum_ka_nw_n\,s_k\sin(\gamma_k\log n)$ es, término a término, la **respuesta en las ordenadas** $R^\gamma_n$ de v14 (la ley $1-\Phi(\theta)$, Conj. 12.2; medida en las Tablas de respuesta);
- $\mathcal P(T;P)$ es la **forma de Gram de las fases primas en las ordenadas verdaderas** $\gamma_k$ (no en $\tau_k$): $\frac1M\sum_k\sin(\gamma_k\log n)\sin(\gamma_k\log m)$. Por Landau–Gonek, fuera de la diagonal solo sobreviven los pares de la misma base prima ($n/m$ o $nm$ potencia de primo), y la fórmula de Landau–Gonek controla el error solo para $nm\ll T^{1-\varepsilon}$: es "la línea de Landau" que cita ChatGPT, y es la razón por la que $c>\tfrac12$ es nuevo también aquí.

Por tanto **(7) es exactamente el Teorema S2 evaluado en las ordenadas verdaderas con residuo cero**: $\mathcal V_0-2\mathcal C+\mathcal P=\|s-\Pi s\|^2+\|{\rm residuo}\|^2$ en la métrica de Gram de los $\gamma_k$, y pedir que tienda a 0 es pedir que las fases primas (con corte $\to\infty$) sean **completas** para el desplazamiento $s_k$. La ley $1-\Phi$ da la parte $\theta<1$; el contenido $\theta>1$ es el que miden tus cortes $c\ge1$ (RMS 0.0212→0.0128 en v14/AGENTS). El criterio (10), $1-r_T=o(1/\log\log T)$, es la forma cuantitativa de esa completitud.

## 3. Lo que sigue abierto, igual que en la nota de ChatGPT

- Valor de $\mathcal C$ y $\mathcal P$ con primos largos ($c>\tfrac12$): respuesta en los ceros más allá de Landau–Gonek, y Gram en los ceros con productos $nm\asymp T$ (resonancia; C1 es la versión en $\tau_k$, no en $\gamma_k$).
- $\mathsf V_T/M\to0$: no se deduce de (21)–(22); solo del límite superior (23) para la integral, que lo controla todo a la vez.
- Extremos con $c(t)\to\infty$: condición (20), $H_T^{3/2}=o(T\log T)$.

## 4. Acuerdo con el orden propuesto

Empezar con $\tfrac12<c<1$: ahí C1 controla la resonancia escalar en $\tau_k$, y el paso a $\gamma_k$ (Cor. `pp:cor:zeros` de v12 solo cambia la ventana, no los puntos de evaluación) es el primer cálculo concreto: $\mathcal P$ en $\gamma_k$ frente a $\mathcal P$ en $\tau_k$, cuya diferencia es el transporte $\gamma_k-\tau_k=-s_k/\Lambda+\ldots$, es decir, otra vez la respuesta.
