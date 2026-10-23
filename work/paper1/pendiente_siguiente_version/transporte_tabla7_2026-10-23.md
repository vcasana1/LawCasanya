# Pendiente para la siguiente versión de Paper I — transporte (Tabla 7, Remark 7.7)

Estado: anotado el 2026-10-23 por orden de Doktor. No crear versión hasta que lo ordene.

## 1. Corrección: el transporte no es 21–35 veces menor que lo esperado
- Texto actual (tras `tab:transport`): "The transport is smaller than $c^2\log\log T$ ($=0.103$, $0.287$, $0.644$) by factors $21$--$35$".
- La comparación omite el factor $1/(2\pi^2)$. El tamaño esperado de la Observación `rem:newton` es $c^2\langle s_k^2\rangle$, con $\langle s_k^2\rangle\approx\frac1{2\pi^2}\log\log T$.
- Sobre la misma ventana ($2^{19}<\gamma_k\le2^{20}$, 977 804 ceros), $\langle s_k^2\rangle=0.11279$ (programa `work/paper1/transport_note/s2_window_2p19.py`, salida `.out`/`.json`).
- $\langle\mathfrak t_k^2\rangle/(c^2\langle s_k^2\rangle)$ = 1.087 ($c=1/5$), 0.909 ($c=1/3$), 0.648 ($c=1/2$). El transporte tiene el tamaño ingenuo; solo con $c=1/2$ queda algo por debajo.
- Lo real es la cancelación $2\langle u_k\mathfrak t_k\rangle\approx-\langle\mathfrak t_k^2\rangle$, que hace $\langle r_k^2\rangle\approx\langle u_k^2\rangle$. Reescribir la frase en esos términos.

## 2. Modelo local (no es teorema; solo para orientar)
Con $S_X$ lineal entre $\gamma_k$ y $\tau_k$, $a=S_X(\gamma_k)$, $\sigma=S_X'/\lL$, $K=S_X(\tau_k)$: $s_k=(K+u_k)/(1+\sigma)$ exactamente, y para todo punto $x$ calculado con el reloj y los primos $p\le X$,
$$\lL(x-\gamma_k)=\Bigl[\lL(x-\tau_k)+\frac K{1+\sigma}\Bigr]+\frac{u_k}{1+\sigma}.$$
- La media sobre ceros pesa con $dN=(\lL+S')dt$; con ese peso $\langle u\mathfrak t\rangle\approx-c^2\langle u^2\rangle$: signo correcto, 40–70 % del tamaño observado (corr. predichas −0.115, −0.157, −0.204 frente a −0.171, −0.336, −0.533). El resto no está explicado.
- Límite: el defecto entra siempre como $u_k/(1+\sigma)$; la única información sobre $u_k$ al alcance del reloj es $K$, con correlación $O(c^2\langle u^2\rangle/\langle a^2\rangle)$. La mejor corrección desde el reloj no baja $\langle r^2\rangle$ más que un $O(c^2\langle u^2\rangle/\langle a^2\rangle)$ relativo por debajo de $\langle u^2\rangle$ (≈3 % con $c=1/2$).
- Consecuencia: el transporte puede, como mucho, impedir que el error crezca (pregunta `q:fixed_c`), no bajarlo por debajo del defecto. Bajar el error exige reducir $u_k$, es decir, más primos ($c>\tfrac12$).
