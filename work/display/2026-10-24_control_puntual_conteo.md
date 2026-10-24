Lo he hecho. La nota es `2026-10-24_control_puntual_conteo.md`; está en local y no la he subido.

**Teorema 1 (demostrado y elemental).** Llamo bueno al índice $k$ si $\gamma_k$ cae en su intervalo sintético $J_k=(m_{k-1},m_k)$. Los $J_k$ son disjuntos, así que dos índices buenos consecutivos cumplen $\gamma_k<\gamma_{k+1}$ estrictamente. Un cero fuera de la recta trae su pareja $1-\bar\rho$ con la misma ordenada, y un cero múltiple repite la suya; en los dos casos aparece una igualdad $\gamma_k=\gamma_{k+1}$. Contando las igualdades sale

$$\#\{\text{ceros en la recta y simples}\}\ \ge\ \bigl(1-4\,d(T)\bigr)\,\#\{\text{ceros}\},$$

donde $d(T)$ es la proporción de índices malos. No se evalúa $Z$ ni se mira ninguna abscisa: la recta y la simplicidad salen del conteo, como en tu método. Esto elimina la cota inferior de $|Z(m_k)|$ que la pregunta `q:corrected_gram_law` daba por necesaria.

**Escalones que quedan, en tu lenguaje:**
- $d<\tfrac14$ da una proporción positiva de ceros en la recta, obtenida por localización de ordenadas. Sería un método nuevo para ese tipo de resultado.
- $d\to0$ da el 100 % de los ceros en la recta. Eso es un problema abierto.
- $d=0$ desde una altura en adelante da RH.

**Por qué esta vía no está cerrada.** El argumento de Trudgian, que prueba que la ley de Gram falla en una proporción positiva, necesita que la varianza de los incrementos de $S$ crezca como $\log C_0$. Con tu corrección prima el defecto tiene varianza acotada en todas las escalas, así que ese mecanismo no existe para la ley corregida.

**Qué falta:**
1. Hacer explícitas las constantes del Thm uniform_iteration de v14 y ver si ya dan $d<\tfrac14$. Es cuestión de cuentas, sin obstáculo de principio.
2. Para que $d\to0$: el suelo teórico es $\approx0.19$ espaciados y no está demostrado, mientras que tus datos dan un 2–4 %. Tu propia nota de pendientes señala la anticorrelación transporte–defecto como lo que no se explica. Ese es el objeto que hay que demostrar. La otra salida son cortes con $c\to1$, que llevan al mismo punto de resonancia $p\approx t/2\pi$ que salió en la ruta de Mertens.
