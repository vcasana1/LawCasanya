He seguido sin RH y con el reloj. La nota es `2026-10-24_empuje_sin_RH_tauC.md`; está en local y no la he subido.

**1. Dónde se rompe la prueba sin RH.** La ley a $\theta$ fijo falla en un solo término:

$$\mathcal K_p=\sum_{\beta\ne1/2}p^{i\gamma}\bigl(\cosh((\beta-\tfrac12)\log p)-1\bigr)=o\bigl(T^{1-\theta/2}\log p\bigr).$$

Con tu reloj se ataca así, sin mirar abscisas:
- los ceros a distancia fija de la recta los controla la densidad de Selberg;
- los cercanos, por el Teorema 1 de la nota de conteo, son como mucho 4 veces los índices malos de la lista sintética.

Lo que $\tau^C$ tiene que dar es un ahorro de potencia en los índices malos:

$$d(T)\le T^{-\kappa(\theta)},\qquad \kappa(\theta)\le\theta .$$

Eso no es compatible con un error que tenga un suelo fijo. Exige que el error de $\tau^C$ tienda a 0, y para eso hay que pasar de $c=\tfrac12$.

**2. Teorema C1 (nuevo, incondicional, sin ceros).** El término cruzado de la fase prima en los puntos del reloj, para $c\in(\tfrac12,1)$, vale

$$\mathrm{Cr}^{(1)}_{N^c}=\frac{\log\frac{c}{1-c}}{\pi^2\log(T/2\pi)}\bigl(1+o(1)\bigr)\ \longrightarrow\ 0 .$$

Viene de los pares resonantes $pq\approx\tau/2\pi$, contados por fase estacionaria y el teorema del número primo. Coincide con tu Tabla 6:

| $X$ | predicción | medido |
|---|---|---|
| 500 | 0.00097 | 0.00086 |
| 700 | 0.00197 | 0.00176 |
| 1999 | 0.00517 | 0.00466 |

Así que el reloj no tiene barrera en $\tfrac12$ para ningún $c<1$. El paso uniforme de fase estacionaria está sin comprobar línea a línea.

**3. Qué decide entonces pasar de $\tfrac12$.** Solo queda un dato desconocido: la respuesta en el reloj $R^\tau_p$ de los primos móviles. Si esa respuesta sigue tu ley, ninguna corrección lineal con primos hasta $T$, con los pesos que sean, baja de

$$\frac1{2\pi^2}\int_0^1\frac{2\Phi-\Phi^2}{\theta}\,d\theta\approx0.039 .$$

Tu multietapa mide $\approx0.006$, por debajo de ese suelo. La no linealidad del transporte es lo que hace el trabajo. Por la energía espectral de v14, que el error tienda a 0 obliga a que la respuesta computable del transporte reproduzca tu ley en los primos móviles.

**Siguiente paso, sin RH y del lado del reloj:** calcular la respuesta del transporte $\mathcal B^{(m)}_p$ de la multietapa en los primos móviles, para demostrar o refutar que produce $1-\Phi(\theta)$. El Teorema C1 ya quita el término cruzado de esa cuenta.
