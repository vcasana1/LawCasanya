**Esto corrige mi conclusión anterior y concreta el mecanismo: la parte cociente compensa la resonancia lenta, mientras que la parte producto introduce una contribución grande por el muestreo en el reloj.** El orden dos completo no mejora por el mero hecho de contener esa compensación.

He leído los programas y salidas de `f9620b2`; no he ejecutado nuevos cálculos ni modificado el manuscrito.

Los resultados confirman dos mejoras del punto explícito \(x_k^q\) respecto al orden uno:

- La distancia del paseo baja de \(13.676\) a \(2.126\): **un 84.5 %**.
- El RMS de posición baja de \(0.1231\) a \(0.1066\) espaciados medios: **un 13.4 %**.

La segunda mejora responde directamente a tu objetivo de acercar los puntos. También se reproduce en el otro tramo: \(0.1207\to0.1043\). Las cifras están en las [salidas del test](https://github.com/vcasana1/LawCasanya/blob/f9620b2/work/notes/checks/opc_quotient_second_order_check.txt) y del [otro tramo](https://github.com/vcasana1/LawCasanya/blob/f9620b2/work/notes/checks/opc_quotient_second_order_check_train.txt).

Además, **la fórmula de \(Q\) puede calcularse sin recorrer todos los pares**. Definiendo
\[
H_X(t)=\sum_i c_i e^{if_it},
\qquad
J_X(t)=\sum_i c_i f_i e^{if_it},
\]
se tiene exactamente
\[
\boxed{Q_X(t)=\frac12\operatorname{Im}
\bigl(H_X(t)\overline{J_X(t)}\bigr).}
\]
Así, tu corrección sigue siendo explícita en \(\tau_k\), y su evaluación cuesta dos sumas simples en lugar de una suma doble.

Quedan cuatro precisiones matemáticas que conviene dejar bien cerradas:

1. **Convergencia de Lagrange.** Los órdenes uno a seis demuestran el deterioro numérico a corte 512. No bastan para demostrar divergencia de la serie infinita. Tampoco \(|S'(\tau_k)|/\mathcal L(\tau_k)<1\) demuestra su convergencia: ese cociente es un diagnóstico local, mientras que el radio de convergencia depende de la continuación compleja de la raíz. A corte 16, la propia salida todavía muestra diferencias entre orden seis y raíz; hay que verificar la convergencia por separado.

2. **Poisson necesita el desplazamiento de medio entero.** Como \(N_0(\tau_k)=k-\tfrac12\), la fórmula, con ventanas y extremos tratados correctamente, lleva
   \[
   \sum_k g(\tau_k)
   =
   \sum_{m\in\mathbb Z}(-1)^m
   \int g(t)\mathcal L(t)e^{2\pi imN_0(t)}\,dt.
   \]
   La condición estacionaria que señalas es correcta. El factor \((-1)^m\) importa para la fase y el signo.

3. **La identidad continua sigue siendo exacta.** Lo que pierde los modos producto es aproximar la suma discreta conservando únicamente el término continuo de Poisson. La cancelación lenta medida es casi completa; el `0.000` de la salida es redondeo.

4. **Combinar con R2 exige evitar contar dos veces la corrección.** R2 ya resuelve una ecuación que incorpora interacciones de orden superior. Añadirle directamente \(Q/\mathcal L^2\) necesita una nueva derivación.

**El avance concreto es una selección algebraica explícita de interacciones entre primos que mejora tanto el paseo como la posición respecto al orden uno.** El siguiente obstáculo está localizado: conservar esa mejora y reducir los cruces, sin recuperar la contribución producto que deteriora el resultado.
