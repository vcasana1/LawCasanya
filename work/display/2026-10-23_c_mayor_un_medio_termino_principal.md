Lo que sigue lo he derivado a mano y no está verificado línea a línea. Tampoco he comprobado si ya figura en la literatura. Una parte es un resultado limpio y la otra queda reducida a un problema concreto.

**1. Media en $t$: el término principal correcto vale hasta $c<1$**

Sea $E_X=S-S_X$, con $S_X$ la suma sobre primos $p\le X$ de la v14. Sea $w$ una ventana suave en $[T,2T]$ y $\|f\|_w^2=\int w\,f^2\,dt$. Para $X'<X\le T^{1-\varepsilon}$ pongo $W=S_X-S_{X'}$, un polinomio sobre los primos de $(X',X]$.

Como $S_{X'}\perp W$ (primos distintos, ventana suave), se tiene

$$\|E_{X'}\|_w^2=\|E_X\|_w^2+2\langle S,W\rangle_w-\|W\|_w^2 .$$

Hay que calcular dos cosas:

- **$\|W\|_w^2$.** Los términos no diagonales llevan $\hat w\bigl(T\log(p/q)\bigr)$. Dos primos distintos cumplen $|\log(p/q)|\ge 1/X\ge T^{-1+\varepsilon}$, así que la ventana suave los hace $O(T^{-A})$. Queda solo la diagonal:
$$\|W\|_w^2=\frac{\hat w(0)\,T}{2\pi^2}\sum_{X'<p\le X}\frac1p\,(1+o(1)).$$
- **$\langle S,W\rangle_w$.** Aquí se aplica la fórmula explícita de Weil con la función de prueba $h(r)=w\bigl((r-T)/H\bigr)\,e^{ir\log p}$. Su transformada $\hat h$ se concentra en $|\log n-\log p|\lesssim 1/H$. Para $p\le T^{1-\varepsilon}$ solo sobrevive $n=p$ (las demás $n$ están a distancia $\ge1/p$). Los términos de polos $h(\pm i/2)$ se anulan con una ventana ancha, de anchura $T/\log T$. El resultado es $\langle S,W\rangle_w=\|W\|_w^2\,(1+o(1))$.

Por tanto $\|E_{X'}\|_w^2=\|E_X\|_w^2+\|W\|_w^2$, y con Mertens,

$$\boxed{\;\frac{1}{T}\bigl(\|E_{T^{c'}}\|_w^2-\|E_{T^{c}}\|_w^2\bigr)=\frac{\hat w(0)}{2\pi^2}\log\frac{c}{c'}+o(1),\qquad 0<c'<c<1.\;}$$

Es decir, existe una constante $A_T$ **independiente de $c$** con

$$\frac1T\|S-S_{T^c}\|_w^2=A_T+\frac{\hat w(0)}{2\pi^2}\log\frac1c+o(1)\qquad(0<c<1).$$

El teorema B solo da esto salvo $O(1+\sqrt{\log(1/c)})$ y no ve diferencias. La constante $A_T$ es la varianza de la parte de $S$ ortogonal a todos los primos $\le T$. Corresponde a la oscilación en diente de sierra de $S$ en cada cero. La conjetura GUE indica que $A_T\to A$ con $A$ una constante, pero no la identifico.

**2. La media sobre los ceros ($u_k$): queda reducida a un problema concreto**

Para el cuadrado medio en las ordenadas hay que tratar $\int E_X^2\,S_X'\,dt$, que es lo que te frena en $c>\tfrac12$. Dos observaciones sobre ese término:

- $S_X^2S_X'=\tfrac13(S_X^3)'$, así que $\int S_X^2S_X'$ es solo un término de borde.
- Queda $\int S^2S_X'-2\int S\,S_X\,S_X'$. Con $S'=-\Lambda(t)+\sum_\gamma\delta_\gamma$ (con $\Lambda$ la densidad de ceros), integrando por partes ambos términos se convierten en **sumas sobre ceros** $\sum_\gamma S_X(\gamma)^2$ y $\sum_\gamma S(\gamma)S_X(\gamma)$. Estas llevan la correlación de pares $F(\alpha)$ de Montgomery, con $\alpha\le c$. Para $c<1$ eso cae dentro del rango $\alpha<1$ donde $F(\alpha)=\alpha+o(1)$ (bajo RH, que en esta forma habría que quitar usando la versión de Landau–Gonek para todos los ceros $\rho$).

Mi lectura es que, para $\tfrac12<c<1$, el término principal de $\langle u_k^2\rangle$ vuelve a ser $\frac1{2\pi^2}\log\frac1c$ más una constante $A'$ independiente de $c$. Eso es lo que **conjeturo**. Lo que falta para demostrarlo es controlar esa suma de ceros sin RH. Para $c>1$ la fórmula $\frac1{2\pi^2}\log(1/c)$ se vuelve negativa, así que ahí cambia sí o sí.

**Resumen**

| Cantidad | Rango | Estado |
|---|---|---|
| Media en $t$ de $E_X^2$ | $0<c<1$ | Ley de diferencias, derivada arriba |
| Media sobre ceros, $u_k$ | $0<c\le\tfrac12$ | Teorema B (v14), salvo $O(1+\sqrt{\log(1/c)})$ |
| Media sobre ceros, $u_k$ | $\tfrac12<c<1$ | Reducida a sumas sobre ceros con $F(\alpha)$, $\alpha<1$ |
| Cualquiera | $c>1$ | Otra fórmula, sin determinar |

Si me lo pides, lo dejo como nota en `work/` con la prueba completa de la parte 1, para que revises los pasos de la fórmula explícita y de la ventana.
