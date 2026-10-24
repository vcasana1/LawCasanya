# Teorema C1: prueba completa, con la transición de borde

**Enunciado.** Sean $N=T/2\pi$, $L=\log N$, la ventana del reloj $\mathcal J_T=\{k:T\le\tau_k<2T\}$ con $M=|\mathcal J_T|=NL(1+O(1/L))$, y $X=N^c$ con $\tfrac12<c<1$ fijo. Sea

$$S^{(1)}_X(t)=-\frac1\pi\sum_{p\le X}p^{-1/2}\sin(t\log p),\qquad \mathrm{Cr}^{(1)}_X=\bigl\langle S^{(1)}_X(\tau_k)^2\bigr\rangle_{\mathcal J_T}-\frac1{2\pi^2}\sum_{p\le X}\frac1p .$$

Entonces

$$\mathrm{Cr}^{(1)}_X=\frac{\log\frac{c}{1-c}}{\pi^2L}\bigl(1+o(1)\bigr).$$

**Notación.** $C_T(u)=\frac1M\sum_{k\in\mathcal J_T}e^{i\tau_k\log u}$. $x\mapsto\tau_x$ es la inversa lisa de $N_0$. Para $u>1$, $F_u(x)=\tau_x\log u/2\pi$, y por v12 (pp:eq:derivs)

$$F_u'(x)=\frac{\log u}{\log(\tau_x/2\pi)},\qquad F_u''(x)=-\frac{2\pi\log u}{\tau_x\log^3(\tau_x/2\pi)} .$$

## Paso 0: expansión exacta

Con $2\sin A\sin B=\cos(A-B)-\cos(A+B)$,

$$\bigl\langle S^{(1)2}\bigr\rangle=\frac1{2\pi^2}\sum_{p,q\le X}(pq)^{-1/2}\Bigl[\Re C_T(p/q)-\Re C_T(pq)\Bigr].$$

Los términos $p=q$ de la primera parte dan exactamente $\frac1{2\pi^2}\sum_{p\le X}1/p$. Por tanto

$$\mathrm{Cr}^{(1)}_X=\underbrace{\frac1{2\pi^2}\sum_{p\ne q}\frac{\Re C_T(p/q)}{\sqrt{pq}}}_{\mathcal D}\;-\;\underbrace{\frac1{2\pi^2}\sum_{p,q}\frac{\Re C_T(pq)}{\sqrt{pq}}}_{\mathcal H}.$$

## Paso 1: cocientes

Por v12, Lema pp:lem:quotient, $|C_T(p/q)|\ll\max(p,q)/(T|p-q|)$. Con $\max(p,q)/\sqrt{pq}\le\sqrt{\max/\min}$ y separando $q\in[p/2,2p]$ del resto,

$$|\mathcal D|\ll\frac1T\sum_{p\le X}\sum_{q\ne p}\frac{1}{|p-q|}+\frac1T\Bigl(\sum_{p\le X}p^{-1/2}\Bigr)^2\ll\frac{X\log X}{T}\ll N^{c-1}\log N .$$

Es $o(1/L)$ porque $c<1$.

## Paso 2: productos no resonantes

Si $u=pq\notin[T/4\pi,4T]$, por v12, Lema pp:lem:product, $|C_T(u)|\ll1/T$ (con $pq\le N^{2c}$, $2c<2$). La contribución a $\mathcal H$ es

$$\ll\frac1T\Bigl(\sum_{p\le X}p^{-1/2}\Bigr)^2\ll\frac{X}{T\log^2X}=o(1/L).$$

## Paso 3: productos resonantes, evaluación exacta por Poisson truncado

Sea $u=n=pq\in[T/4\pi,4T]$. Ahí $F_u'(x)=1+O(1/L)$ en toda la ventana. Por el lema de van der Corput–Poisson (Titchmarsh, Lema 4.7: $F'$ monótona en $[\alpha,\beta]$, $0<\eta<1$), con $\eta=\tfrac14$ el único entero en $(\alpha-\eta,\beta+\eta)$ es $\nu=1$, y

$$\sum_{k\in\mathcal J_T}e^{i\tau_k\log n}=I(n)+O(1),\qquad I(n)=\int_{a}^{b}e^{i\varphi_n(x)}\,dx,\qquad \varphi_n(x)=\tau_x\log n-2\pi x ,$$

uniformemente en $n$, con $\tau_a=T$ y $\tau_b=2T$.

**Datos de la fase.** Sea $x_0=x_0(n)$ con $\tau_{x_0}=2\pi n$. Entonces:
- $\varphi_n'(x_0)=0$;
- $\varphi_n''(x_0)=-\dfrac{2\pi}{n\log^2n}$, de modo que $\lambda:=|\varphi_n''|\asymp\dfrac1{TL^2}$ en toda la ventana;
- $|\varphi_n'''|\asymp\dfrac1{T^2L^2}$;
- $\varphi_n(x_0)=2\pi n-\tfrac{11\pi}4$ (v14, l. 1770), luego $e^{i\varphi_n(x_0)-i\pi/4}=-1$;
- $\sqrt{2\pi/\lambda}=\sqrt n\log n$.

**Tres casos según $d=\mathrm{dist}(x_0,\{a,b\})$.** Sea $D_0=\lambda^{-1/2}\asymp\sqrt T\,L$.

- **(a) Interior, $x_0\in(a,b)$, $d\ge D_0$.** Fase estacionaria con extremos (Titchmarsh, Lema 4.6, o Graham–Kolesnik, Lema 3.4):
$$I(n)=-\sqrt n\log n+O\Bigl(\frac1{|\varphi'(a)|}+\frac1{|\varphi'(b)|}\Bigr)+O\bigl(\lambda^{-4/5}|\varphi'''|^{1/5}\bigr).$$
Como $|\varphi'(a)|,|\varphi'(b)|\gg\lambda d$, el error de borde es $\ll TL^2/d$, y el de tercera derivada es $\ll T^{2/5}L^{6/5}$.

- **(b) Cerca del borde, $d<D_0$.** No se usa ninguna fórmula asintótica. Por la segunda derivada para integrales, $|I(n)|\ll\lambda^{-1/2}\asymp\sqrt T\,L$; y el término principal $\sqrt n\log n$ es del mismo orden. *(Aquí es donde el Lema 17.8 de v12 da media gaussiana; esta prueba no lo necesita.)*

- **(c) Fuera, $x_0\notin(a,b)$, $n$ resonante.** Sin punto estacionario: $|I(n)|\ll\min\bigl(\lambda^{-1/2},\,1/(\lambda d)\bigr)$.

**Paso a la variable $n$.** La distancia $d$ en índices corresponde a una distancia $m$ en $n$ al extremo más cercano ($N$ o $2N$), con $d\asymp Lm$ porque $dx=\Lambda\,d\tau$ y $\tau=2\pi n$. El caso (b) es $m\ll\sqrt T$, y en (a) y (c) el error de borde es $\ll TL/m$.

**Conteo trivial clave.** Un entero $n$ tiene a lo sumo dos factorizaciones ordenadas $n=pq$ en dos primos. Por tanto el número de pares ordenados con $pq$ en un intervalo de longitud $H$ es $\le2(H+1)$. No hace falta Brun–Titchmarsh en intervalos cortos.

**Suma con pesos $(pq)^{-1/2}/M\asymp T^{-1/2}/(TL)$:**
- término $O(1)$ de Poisson: $\ll\#\{\text{pares resonantes}\}\cdot T^{-1/2}/(TL)\ll(T/L)\,T^{-3/2}/L=T^{-1/2}/L^2$;
- caso (b): $\ll\sqrt T\cdot\sqrt TL\cdot T^{-1/2}/(TL)=T^{-1/2}$;
- bordes de (a) y (c): $\ll\sum_{m\ge\sqrt T}\frac{TL}{m}\cdot\frac{T^{-1/2}}{TL}\ll T^{-1/2}\log T$;
- tercera derivada: $\ll\frac TL\cdot T^{2/5}L^{6/5}\cdot\frac{T^{-1/2}}{TL}=T^{-1/10}L^{-4/5}$;
- el término principal de los pares de (b), contado en la fórmula final con $\mathbf 1_{T<2\pi n<2T}$ y no realmente presente, cuesta $\ll T^{-1/2}$ por la misma cuenta.

**Resultado del paso 3:**

$$-\mathcal H_{\rm res}=\frac{1}{2\pi^2M}\sum_{\substack{p,q\le X\\ N<pq<2N}}\log(pq)+O\bigl(T^{-1/10}\bigr).$$

## Paso 4: conteo de los pares

Para $p<N^{1-c}$ no hay $q\le N^c$ con $pq>N$. Para $p\in[2N^{1-c},N^c]$, $q$ recorre $(N/p,2N/p]$. Por el TNP y suma parcial,

$$\#\{(p,q)\}=\sum_{N^{1-c}<p\le N^c}\frac{N}{p\log(N/p)}\bigl(1+o(1)\bigr)=\frac NL\int_{1-c}^{c}\frac{du}{u(1-u)}\bigl(1+o(1)\bigr)=\frac{2N}{L}\log\frac{c}{1-c}\bigl(1+o(1)\bigr).$$

El tramo $p\in[N^{1-c},2N^{1-c}]$ tiene masa armónica $O(1/L)$. Como $\log(pq)=L+O(1)$,

$$\sum\log(pq)=2N\log\frac{c}{1-c}\bigl(1+o(1)\bigr).$$

## Conclusión

Con $M=NL(1+O(1/L))$:

$$\mathrm{Cr}^{(1)}_X=\mathcal D-\mathcal H_{\rm nores}-\mathcal H_{\rm res}=\frac{2N\log\frac c{1-c}}{2\pi^2NL}\bigl(1+o(1)\bigr)+o(1/L)=\frac{\log\frac c{1-c}}{\pi^2L}\bigl(1+o(1)\bigr).\qquad\square$$

**Sobre la refutación (6) de v12.** El Lema 17.8 es correcto: un producto con el punto estacionario en el borde da media gaussiana, no la gaussiana completa más $O(1)$. Esta prueba no usa la gaussiana completa en esos pares. Los acota uniformemente por $\lambda^{-1/2}$, y son $\ll\sqrt T$ pares, que aportan $O(T^{-1/2})$. En el interior el error no es $O(1)$ sino $O(TL^2/d)$, y su suma es $O(T^{-1/2}\log T)$. La fórmula promedio C1 queda demostrada.

**Lo que se usa:**
- Titchmarsh, Lemas 4.6 y 4.7;
- v12, Lemas pp:lem:quotient y pp:lem:product;
- el TNP;
- la fase $\varphi_n(x_0)$ de v14, l. 1770.

*Sin comprobar contra el PDF:* el exponente exacto del error de tercera derivada en el lema de fase estacionaria citado. Basta que ese error sea $o(\lambda^{-1/2})=o(\sqrt T\,L)$ por par, uniformemente: hay $\asymp T/L$ pares, cada uno con peso $T^{-1/2}/(TL)$, así que el total es $o(1/L)$. La forma $\lambda^{-4/5}|\varphi'''|^{1/5}\asymp T^{2/5}L^{6/5}$ lo cumple con margen.
