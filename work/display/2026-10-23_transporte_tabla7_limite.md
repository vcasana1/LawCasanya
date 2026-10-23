He analizado el transporte con los datos de tu tabla 7 de la v14 y hay dos resultados.

**1. Corrección a la v14: el transporte no es anómalamente pequeño**

El texto de la tabla 7 dice que $\langle\mathfrak t_k^2\rangle$ es entre 21 y 35 veces menor que $c^2\log\log T$. Esa comparación omite el factor $\frac1{2\pi^2}$. El tamaño esperado es $c^2\langle s_k^2\rangle$, donde $s_k=S(\gamma_k)$ y $\langle s_k^2\rangle\approx\frac1{2\pi^2}\log\log T$. He calculado $\langle s_k^2\rangle$ sobre la misma ventana ($2^{19}<\gamma_k\le2^{20}$, los 977 804 ceros) y da $0{,}1128$:

| $c$ | $c^2\langle s_k^2\rangle$ | $\langle\mathfrak t_k^2\rangle$ observado | cociente |
|---|---|---|---|
| 1/5 | 0,00451 | 0,00491 | 1,09 |
| 1/3 | 0,01253 | 0,01139 | 0,91 |
| 1/2 | 0,02820 | 0,01828 | 0,65 |

El transporte tiene el tamaño ingenuo. Lo que sí es real es la **cancelación** $2\langle u_k\mathfrak t_k\rangle\approx-\langle\mathfrak t_k^2\rangle$. Por eso $\langle r_k^2\rangle\approx\langle u_k^2\rangle$, ya que $r_k=u_k+\mathfrak t_k+\chi_k$.

**2. Mecanismo, y límite de lo que el transporte puede bajar**

Uso un modelo local con $S_X$ lineal entre $\gamma_k$ y $\tau_k$. Las variables son:
- $a=S_X(\gamma_k)$;
- $\sigma=S_X'/\Lambda$, con $\Lambda$ la densidad de ceros, que tiene $\langle\sigma^2\rangle\approx c^2$;
- $K=S_X(\tau_k)$, el valor que conoce el reloj.

Como $s_k=a+u_k$ y $K=a+\sigma s_k$, sale exactamente

$$s_k=\frac{K+u_k}{1+\sigma}.$$

Para cualquier punto $x$ calculado con el reloj y los primos $p\le X$,

$$\Lambda(x-\gamma_k)=\underbrace{\Lambda(x-\tau_k)+\frac{K}{1+\sigma}}_{\text{conocido}}+\frac{u_k}{1+\sigma}.$$

- **Origen de la anticorrelación.** La media sobre ceros pesa con $dN=(\Lambda+S')\,dt$, es decir, con un factor $1+\sigma+\dots$. Con ese peso, $\langle u\,\mathfrak t\rangle\approx-c^2\langle u^2\rangle$. El modelo da el signo correcto y entre el 40 % y el 70 % del tamaño observado. El resto no está explicado.
- **Límite.** El defecto $u_k$ entra siempre como $u_k/(1+\sigma)$, y la única información sobre $u_k$ al alcance del reloj es $K$, cuya correlación con $u_k$ es del orden de $c^2\langle u^2\rangle/\langle a^2\rangle$. Por tanto la mejor corrección posible desde el reloj da
$$\langle r^2\rangle\ \ge\ \langle u^2\rangle\,\bigl(1-O(c^2\langle u^2\rangle/\langle a^2\rangle)\bigr).$$
Eso es unos 3 % por debajo de $\langle u^2\rangle$ con $c=\tfrac12$.

**Consecuencia**

El transporte no puede bajar el error por debajo del defecto $u_k$. Puede impedir que crezca (la pregunta `q:fixed_c` de tu paper, error acotado con $c$ fijo), pero no reducirlo. Para bajar el error de verdad hay que reducir $u_k$, y eso solo se consigue con más primos, es decir, con $c$ mayor. Volvemos a $c>\tfrac12$ como único camino.

La corrección del factor $\frac1{2\pi^2}$ debería ir a la lista de pendientes de la próxima versión. No he tocado el paper. ¿Lo anoto en `work/paper1/pendiente_siguiente_version/` y lo subo?
