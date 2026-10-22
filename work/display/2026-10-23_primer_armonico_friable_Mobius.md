## 1. Auditoría del documento 4

Acepto estas correcciones:

- **Condición por índice.** La condición correcta es la suya:
$$|\varepsilon_k|<\tfrac12\quad\text{para cada }k,\qquad \varepsilon_k=F_X(c_k)-k+\tfrac12.$$
Mi «$\sup_t|S_c-S_X|<1$» es solo suficiente. En $[c_k,c_{k+1})$ la diferencia $F_X-N_c$ va de $\varepsilon_k-\tfrac12$ a $\varepsilon_{k+1}+\tfrac12$ sin alcanzar este último valor, así que todos los $|\varepsilon_k|<\tfrac12$ son compatibles con $\sup=1$.
- **Convergencia del producto.** Hace falta $\sum_k c_k^{-2}<\infty$ para definir $\Xi_c$.
- **(1.6).** En los saltos, la serie de Fourier de $\psi_1$ da el valor medio.
- **P3.** Escribí «solo si» y es «si»: la ventana es suficiente, no necesaria. Además, con $X=X(t)$ la entrada brusca de un primo hace saltar $S_{X(t)}$; hace falta un peso de entrada continuo.
- **P2.** Fuera de la banda, $E_X$ es meromorfa: los polos de $\chi$ están en $s=1,3,5,\dots$ y los de los factores completos incluyen $j=0$. Junto a un polo simple $s_j$ ($j\neq0$) escribo $\chi_X=R/(s-s_j)+g$. La ecuación $\chi_X=-1$ da
$$s-s_j=-\frac R{1+g},$$
que tiene solución única si $|g|<1$, lo cual se cumple para $t\ge t(X)$. El orden $|R|\asymp t^{-1/2}$ sí requiere no degeneración diofántica.
- **§3, en forma sin $\zeta$.** Si se cumple (T), entonces en $\operatorname{Re}s>1$
$$B^c_X=C_c^{-1}\sum_{P^-(n)>X}\mu(n)n^{-s},\qquad C_c=\lim_{\sigma\to+\infty}\zeta_c(\sigma).$$
Que (T) implique la identidad para $\zeta_c'/\zeta_c$ necesita una hipótesis de crecimiento sobre $c$ que no está demostrada. No uso su referencia a $\xi$: no hace falta y queda fuera de tu regla.
- **(B)–(E).** Las he comprobado y son correctas. (E) es la cota estándar de primera derivada por integración por partes. (T) es objetivo, no ruta; de acuerdo.

**Error mío, que el documento 4 da por bueno («la resonancia es real»).** En §4 apliqué fase estacionaria a la fase $ut-2\pi F_X(t)$ como si su curvatura fuera la del reloj. No lo es:
$$-2\pi F_X''=-\frac1t-2\pi S_X'',\qquad |S_X''|\le\frac1\pi\sum_{p\le X}\sum_{r\ge1}r\log^2p\;p^{-r/2}.$$
Para $X\ge2$ y $t$ grande, el término primo domina a $1/t$. La ecuación $u=2\pi F_X'(t)$ tiene entonces muchas soluciones, y la fórmula con $e^{2\pi i(e^u-S_X(2\pi e^u))}$ es falsa salvo para $X=1$. Lo correcto es desarrollar exactamente la fase prima.

## 2. Desarrollo exacto del primer armónico [DED]

Notación:
- $P(X)=\prod_{p\le X}p$;
- $q=n/d$ recorre los racionales con $n$ $X$-friable (todos sus primos $\le X$), $d\mid P(X)$ y $(n,d)=1$;
- $c_X(d)=\prod_{p\le X,\ p\nmid d}(1-1/p)$.

**Desarrollo de la fase prima.** Para cada primo $p$ se tiene
$$\frac{1-p^{-1/2}p^{-it}}{1-p^{-1/2}p^{it}}=-p^{-1/2}p^{-it}+(1-\tfrac1p)\sum_{k\ge0}p^{-k/2}p^{ikt}.$$
Multiplicando sobre $p\le X$,
$$e^{-2\pi iS_X(t)}=\sum_q b_X(q)\,q^{it},\qquad b_X(n/d)=\frac{\mu(d)\,c_X(d)}{\sqrt{nd}},\qquad \sum_q|b_X(q)|=\prod_{p\le X}\big(1+2p^{-1/2}\big).$$
La serie converge absolutamente. Derivándola término a término,
$$F_X'\,e^{-2\pi iF_X}=e^{-2i\theta(t)}\sum_q b_X(q)\Big(N_0'(t)-\frac{\log q}{2\pi}\Big)q^{it}.$$

**Teorema.** Sean $T\ge t_0(X)$, $w\in C_c^\infty((T,2T))$ con $w^{(j)}\ll_jT^{-j}$, $u>0$ y $x=e^u$. Entonces
$$\int w\,F_X'\,e^{i(ut-2\pi F_X(t))}\,dt=u\sqrt x\sum_q\frac{\mu(d)\,c_X(d)}{d}\;w(2\pi qx)\,e^{2\pi iqx}+O_w\Big(u\,T^{-1/2}\prod_{p\le X}\big(1+2p^{-1/2}\big)\Big).$$

**Prueba.** El término $q$ tiene fase $(u+\log q)t-2\theta(t)$, con punto estacionario $t_q$ dado por $2\theta'(t_q)=u+\log q$, es decir,
$$t_q=2\pi qx\,\big(1+O(t^{-2})\big).$$
En ese punto la amplitud es exactamente
$$N_0'(t_q)-\frac{\log q}{2\pi}=\frac u{2\pi},$$
la curvatura es $1/t_q$ y el valor de la fase, menos $\pi/4$, es $t_q+O(1/t)$. El factor $b_X(q)\sqrt q$ que sale de $\sqrt{2\pi t_q}$ vale
$$b_X(q)\sqrt q=\frac{\mu(d)\,c_X(d)}{d}.$$
El resto por término lo da el lema estándar de fase estacionaria con peso; las constantes están sin escribir. ∎

El primer armónico de (D), con $h(t)=w(|t|)\cos(ut)$, es menos la parte real de esta integral, más términos no estacionarios acotados por (E). Para $X=1$ queda solo $u\sqrt x\,w(2\pi x)e^{2\pi ix}$.

## 3. Consecuencias

1. **Atenuación de la resonancia principal.** La resonancia del reloj en $t=2\pi x$ ($q=1$) queda multiplicada por
$$\prod_{p\le X}\Big(1-\frac1p\Big),$$
que es la densidad de los enteros $X$-rugosos.
2. **Möbius aparece por sí solo.** El resto del peso se reparte en resonancias en $t=2\pi x\,n/d$, con coeficiente $\mu(d)\,c_X(d)/d$ para $d\mid P(X)$. Es una estructura de criba de Legendre que la fase prima produce sin añadir nada. Responde a la pregunta del §7 del documento 4: la inversión de Möbius ya actúa, pero solo con $d\mid P(X)$.

## 4. El obstáculo, cuantificado

Las dos restricciones analíticas coinciden. El resto del teorema y la monotonía de $F_X$ exigen
$$\prod_{p\le X}\big(1+2p^{-1/2}\big)\ll T^{1/2}\quad\text{y}\quad 2\sigma_X<\log\frac T{2\pi},$$
y ambas dan $X\le(\log T)^{2+o(1)}$.

Para que los pesos $\mu(d)/d$ actúen como la criba de Eratóstenes en el entero resonante $x\approx T/2\pi$, harían falta todos los $d\le\sqrt x$ libres de cuadrados [heurística]. Es decir,
$$X(T)\ge\sqrt{T/2\pi}.$$

El reloj regularizado D′ resuelve la monotonía, pero la proyección sobre pendientes rompe el desarrollo exacto. El problema concreto queda así: construir un reloj monótono con
$$X(T)\ge\sqrt{T/2\pi},$$
cuyo primer armónico conserve el desarrollo
$$\sum_q\frac{\mu(d)\,c_X(d)}{d}\,w(2\pi qx)\,e^{2\pi iqx}$$
controlando su masa por cancelación, no por la cota absoluta $\prod_{p\le X}(1+2p^{-1/2})$.
