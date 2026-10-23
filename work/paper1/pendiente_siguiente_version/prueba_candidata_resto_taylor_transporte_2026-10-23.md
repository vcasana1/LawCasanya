# Energía del transporte: prueba candidata mediante el segundo reloj y Taylor en dos escalas

**Fecha:** 2026-10-23. **Destino:** nota técnica para auditoría, **no** una nueva versión del manuscrito.  
**Autoría de la línea:** Rotkiv Aynäsac, con comprobación y desarrollo en ChatGPT.  
**Estado:** demostración propuesta; los lemas de muestreo para todos los órdenes y la transferencia de momentos deben someterse a auditoría independiente antes de elevar la conclusión a teorema publicado. No se han efectuado cálculos numéricos.

## A. Enunciado que se intenta demostrar

Para $0<c\le1/2$ fijo, $\mathcal I_T=\{k:T<\gamma_k\le2T\}$, y la fase prima completa
\[
S_X(t)=-\frac1\pi\sum_{p\le X}\sum_{m\ge1}
\frac{\sin(mt\log p)}{mp^{m/2}},
\quad
\mathfrak t_k(X)=S_X(\gamma_k)-S_X(\tau_k),
\]
se propone
\[
\boxed{ B_c(T):=\langle\mathfrak t_k(T^c)^2\rangle_{\mathcal I_T}
\sim \frac{\log\log\log T}{2\pi^2}. }\tag{A.1}
\]
A diferencia del modelo estadístico, la prueba propuesta usa el teorema B, el teorema del segundo paso y el lema de multiplicidad de v14; la única media final que hay que evaluar contiene únicamente $\tau_k$ y primos.

Pongamos
\[
H=\log\log T,\quad h=\log H,\quad h_2=\log h,\qquad
X_1=T^{H^{-1/2}},\ X_2=T^{h^{-1/2}},
\quad V=\frac{H}{2\pi^2},\quad \omega=h^{1/8},
\quad \vartheta=\frac{\omega}{\sqrt V},\quad Y=T^\vartheta .
\]
Para $T$ suficientemente grande, $X_1<Y<X_2<T^{1/4}$. Sea
\[
P=S_{X_1},\quad Q=S_{X_2}-S_{X_1},\quad
W=S_{X_2}-S_Y,\quad
x_k^{(1)}=\tau_k-\frac{P(\tau_k)}{\Lambda(\tau_k)},
\quad L=\frac1{2\pi^2}\sum_{Y<p\le X_2}\frac1p.
\]
Entonces
\[
L=\frac{h}{4\pi^2}+o(h),\qquad
\langle(s_k-S_{X_2}(x_k^{(1)}))^2\rangle=O(h_2),
\tag{A.2}
\]
por el teorema del segundo paso, usando la identidad exacta de recursión. La reducción ya auditada de v14 implica
\[
B_{h^{-1/2}}(T)=2L-2\langle s_k W(\tau_k)\rangle+o(h).\tag{A.3}
\]
El objetivo concreto queda:
\[
\boxed{\langle S_{X_2}(x_k^{(1)})W(\tau_k)\rangle=o(h).}\tag{A.4}
\]
En virtud de (A.2), esto implica $\langle s W(\tau)\rangle=o(h)$. Finalmente,
\[
\|\mathfrak t(T^c)-\mathfrak t(X_2)\|_2^2=O_c(h_2)
\tag{A.5}
\]
por la identidad $[S_{T^c}-S_{X_2}](\gamma)=u(X_2)-u(T^c)$, el teorema B y la ortogonalidad RvM; por tanto (A.1) se sigue de (A.3)–(A.4).

## B. Lemas deterministas de muestreo que se deben emplear

Escribamos $M_T=\#\mathcal I_T\asymp T\log T$ y $\lambda=\log(T/2\pi)/(2\pi)$. Los $\tau_k$ son $1/\lambda$-separados a escala local (con constantes absolutas). Sea $F$ un polinomio trigonométrico en frecuencias $\log n$ cuyo módulo máximo de frecuencia sea $\le C\log X_2=o(\log T)$; basta que sus coeficientes satisfagan momentos continuos de orden cuatro:
\[
\frac1T\int_{T-O(1)}^{2T+O(1)}|F^{(j)}(t)|^4dt
\ll A^4(\log X_2)^{4j},\quad j=0,1.
\]
La desigualdad de Sobolev en los intervalos
$I_k=[\tau_k-(D+1)/\lambda,\tau_k+(D+1)/\lambda]$,
la separación de los puntos RvM y Hölder proporcionan
\[
\left\|\sup_{|v|\le D/\lambda}|F(\tau_k+v)|\right\|_{4,\mathcal I_T}
\ll (1+D)^{C_0}A.\tag{B.1}
\]
En efecto, $\sup_I|F|^4\ll |I|^{-1}\int_I|F|^4+\int_I|F|^3|F'|$; al sumar en $k$, la multiplicidad de cobertura es $O(1+D)$ y $\lambda^{-1}\|F'\|_4\ll \|F\|_4$ en la estimación buscada. Se admite cualquier potencia absoluta de $1+D$; no es necesaria una constante óptima.

Para el polinomio **solo de primos**
\[
Q^\mathrm{pr}(t)=-\pi^{-1}\sum_{X_1<q\le X_2}q^{-1/2}\sin(t\log q)
\]
Montgomery–Vaughan aplicado al cuadrado, pues $X_2^2<T$, y la suma $\sum_{X_1<q\le X_2}q^{-1}\ll h$ implican, **uniformemente para todos los enteros $j\ge0$**,
\[
\frac1T\int |(Q^\mathrm{pr})^{(j)}|^4
\ll h^2(\log X_2)^{4j},\qquad
\left\|\sup_{|v|\le D/\lambda}
|(Q^\mathrm{pr})^{(j)}(\tau+v)|\right\|_4
\ll (1+D)^{C_0}\sqrt h\,(\log X_2)^j .
\tag{B.2}
\]
La uniformidad en $j$ se debe a $|(\log q/\log X_2)^j|\le1$ y a que la longitud del polinomio **no crece al derivarlo**. Éste es el sustituto de sumar individualmente los restos sobre $q$.

Para cualquier polinomio racional de Dirichlet $F(t)=\sum_{a,b\le T^\eta}c_{a,b}(a/b)^{it}$, $\eta=o(1)$, con $\sum|c_{a,b}|\le T^{o(1)}$, se tiene
\[
\langle F(\tau_k)\rangle
=\sum_{a=b}c_{a,b}+O(T^{-1+o(1)}).\tag{B.3}
\]
La prueba usa $d\tau/dk=1/\Lambda(\tau)$, la desigualdad de primera derivada para las sumas en $k$, y $|\log(a/b)|\gg T^{-\eta}$ para $a\ne b$; las derivadas normalizadas están lejos de enteros distintos de cero porque $\eta=o(1)$. El mismo argumento vale para momentos de orden cuatro y para momentos de orden $2m$, siempre que $2m$ veces el exponente de longitud siga siendo $o(1)$.

Para los puntos no monótonos $x_k^{(1)}$, el lema de multiplicidad y el lema de muestreo de la v14, aplicados a un polinomio $F$ (en vez de a la función maximal del manuscrito), dan
\[
\|Q^\mathrm{pr}(x_k^{(1)})\|_4\ll\sqrt h.\tag{B.4}
\]
Para auditar (B.4), reutilizar literalmente la estimación de v14 con
$\tilde n(u)=\#\{k:u-b\le x_k^{(1)}\le u\}$,
$\|\tilde n\|_2^2\ll bM_T$, $b\asymp1/\log T$,
$F=(Q^\mathrm{pr})^4$, y los momentos de orden ocho de $Q^\mathrm{pr}$ y su derivada. Éstos son válidos porque $X_2^4<T$ para $T$ grande.

## C. Truncar las potencias primas y controlar dos bloques de primos

Por el valor absoluto del desarrollo de Euler, para todo $M\ge3$,
\[
\sup_t\left|S_X(t)+\frac1\pi
\sum_{p\le X}\sum_{1\le m\le M}
\frac{\sin(mt\log p)}{mp^{m/2}}\right|
\ll 2^{-M/2}.\tag{C.1}
\]
Elegimos $M=\lceil100h\rceil$. Se separa la fase prima truncada
\[
P^{[M]}=P_0+P_1,\quad
P_0:\ p\le Z=T^{H^{-2}},\quad
P_1:\ Z<p\le X_1 .
\]
Los factores de cada primo constituyen variables trigonométricas independientes bajo la medida de Haar del toro de fases. Son centradas y están acotadas por $C/\sqrt p$. En particular, con constantes absolutas y para órdenes $2m$ permitidos por (B.3),
\[
\|P_0\|_{2m}\ll\sqrt{mH},
\qquad
\|P_1\|_{2m}\ll\sqrt{mh}.\tag{C.2}
\]
Esto incluye las potencias primas, agrupadas por **primo base**; no se necesita tratarlas como independientes de ese primo.

Sean
\[
D_0=H^{3/4},\quad D_1=h^2,\quad
J_0=\left\lceil K H/h\right\rceil,\quad
J_1=\lceil K h^2\rceil,\tag{C.3}
\]
donde $K$ es una constante absoluta suficientemente grande. Por Markov y (C.2), el suceso
$\mathcal G=\{|P_0(\tau_k)|\le D_0,\ |P_1(\tau_k)|\le D_1\}$
satisface
\[
\mathbb P_{\mathcal I_T}(\mathcal G^c)
\ll e^{-c\sqrt H}+e^{-ch^3},\tag{C.4}
\]
eligiendo órdenes $m\asymp\sqrt H$ y $m\asymp h^3$ respectivamente. Son órdenes admisibles: sus polinomios de momentos tienen longitud
$T^{O(M\sqrt H/H^2+Mh^3/\sqrt H)}=T^{o(1)}$.
Para $Q^\mathrm{pr}$, (B.4) y (C.4) hacen
$\langle1_{\mathcal G^c} Q^\mathrm{pr}(x^{(1)})W(\tau)\rangle=o(1)$, por Hölder y $\|W(\tau)\|_4\ll\sqrt h$.

Reemplazar $\Lambda(\tau_k)$ por la constante $\lambda$ en el desplazamiento cuesta $o(1)$ en la correlación con $W$: en la ventana, $|\Lambda(\tau)^{-1}-\lambda^{-1}|\ll(\log T)^{-2}$ y se aplica (B.1), (C.2) y Hölder. El rabo de (C.1) se trata de igual manera sobre $\mathcal G$; fuera de ella se usa (B.4). Ninguno requiere estimar suma a suma los coeficientes de $Q^\mathrm{pr}$.

## D. El resto de Taylor de la suma completa

Consideremos primero $Q^\mathrm{pr}(t-(P_0(t)+P_1(t))/\lambda)$.
El **orden correcto** es: expandir primero el desplazamiento $P_1$, después el desplazamiento $P_0$.

Definamos el polinomio en $t$
\[
\mathcal Q_J(t)=
\sum_{0\le j_1<J_1}\sum_{0\le j_0<J_0}
\frac{(-P_1(t)/\lambda)^{j_1}}{j_1!}
\frac{(-P_0(t)/\lambda)^{j_0}}{j_0!}
(Q^\mathrm{pr})^{(j_0+j_1)}(t).
\tag{D.1}
\]
Por el resto integral de Taylor, para $k\in\mathcal G$ y $D=D_0+D_1+2$,
\[
|Q^\mathrm{pr}(x_k^{(1)})-\mathcal Q_J(\tau_k)|
\ll \frac{(D_1/\lambda)^{J_1}}{J_1!}
\sup_{|v|\le D/\lambda}|(Q^\mathrm{pr})^{(J_1)}(\tau_k+v)|
\]
\[
\qquad\qquad+
\sum_{j_1<J_1}\frac{(D_1/\lambda)^{j_1}}{j_1!}
\frac{(D_0/\lambda)^{J_0}}{J_0!}
\sup_{|v|\le D/\lambda}
|(Q^\mathrm{pr})^{(J_0+j_1)}(\tau_k+v)|
+\text{rabo de (C.1)}.\tag{D.2}
\]
Por (B.2), el lado derecho, en norma $L^2(\mathcal I_T)$ restringida a $\mathcal G$, es a lo sumo
\[
C(1+D)^{C_0}\sqrt h\left[
\frac{(C D_1/\sqrt h)^{J_1}}{J_1!}
+
e^{CD_1/\sqrt h}
\frac{(C D_0/\sqrt h)^{J_0}}{J_0!}
\right]+o(1).\tag{D.3}
\]
Con (C.3), Stirling da
\[
\frac{(CD_1/\sqrt h)^{J_1}}{J_1!}
\le e^{-c h^2\log h},
\quad
e^{CD_1/\sqrt h}
\frac{(CD_0/\sqrt h)^{J_0}}{J_0!}
\le e^{-c H}.
\]
Por tanto,
\[
\boxed{\|1_{\mathcal G}(Q^\mathrm{pr}(x^{(1)})-\mathcal Q_J(\tau))\|_2=o(1).}\tag{D.4}
\]
Esta es la estimación uniforme buscada: el resto se controla **después de sumar sobre todos los primos**, porque (B.2) se aplica a la derivada del polinomio entero.

La elección $J_1=O(1)$ del primer esquema NO permitiría (D.4). Asimismo, expandir primero $P_0$ introduciría un factor exponencial mucho mayor en el otro resto.

## E. Momentos del polinomio truncado y cola excepcional

Bajo el modelo de fases primas independientes, los términos de $\mathcal Q_J$ se reagrupan exactamente como
\[
\mathcal Q_J(t)
=-\frac1\pi\sum_{X_1<q\le X_2}\frac1{\sqrt q}
\Im\!\left(q^{-it}
F_{0,\xi_q}(P_0(t))\,F_{1,\xi_q}(P_1(t))\right),
\quad
\xi_q=\frac{\log q}{\lambda},
\tag{E.1}
\]
donde $F_{i,\xi}(x)=\sum_{j<J_i}(i\xi x)^j/j!$ (con el signo consistente con (D.1)).

Los bloques $P_0,P_1$ tienen primos base $\le X_1$, y cada $q$ de (E.1) es $>X_1$. Por independencia de las fases $q$ y el método de momentos de cuarto orden (o Khintchine, condicionado en los primos bajos),
\[
\mathbb E_{\rm Haar}|\mathcal Q_J|^4
\ll\left(\sum_{X_1<q\le X_2}\frac1q\right)^2
\sup_{q}\mathbb E_{\rm Haar}|F_{0,\xi_q}F_{1,\xi_q}|^4.\tag{E.2}
\]
La fórmula integral del resto para $e^{i\xi x}$ con $x$ real da, **sin factor $e^{|\xi x|}$**,
\[
\left|e^{i\xi x}-F_{i,\xi}(x)\right|\le \frac{|\xi x|^{J_i}}{J_i!}.
\]
Por (C.2), Hölder y $J_i! \ge (J_i/e)^{J_i}$,
\[
\sup_{|\xi|\le C/\sqrt h}
\|e^{i\xi P_i}-F_{i,\xi}(P_i)\|_{8,\mathrm{Haar}}
\le \left(C\sqrt{\frac{\xi^2 V_i}{J_i}}\right)^{J_i}
=e^{-\Omega(J_i)}
\tag{E.3}
\]
para $K$ suficientemente grande, $V_0\asymp H$, $V_1\ll h$.
Las dos variables proceden de rangos disjuntos de primos, luego son independientes bajo Haar y $\sup_q\mathbb E_{\rm Haar}|F_0F_1|^4=O(1)$. Así, por (E.2),
\[
\mathbb E_{\rm Haar}|\mathcal Q_J|^4\ll h^2.
\tag{E.4}
\]
Cada monomio de $\mathcal Q_J$ tiene numerador y denominador $\le T^{\eta_T}$, con
\[
\eta_T\ll
h^{-1/2}+
\frac{M J_0}{H^2}
+\frac{M J_1}{\sqrt H}=o(1).
\]
La suma absoluta de sus coeficientes es $T^{o(1)}$ (acotar las sumas $\ell^1$ de los factores, aplicar el factorial y observar que $\log \ell^1\ll (M J_0/H^2+M J_1/\sqrt H+h^{-1/2})\log T+O(J_0\log J_0+J_1\log J_1)$).
Aplicando (B.3) a $\mathcal Q_J^4$ se deduce
\[
\|\mathcal Q_J(\tau)\|_4\ll\sqrt h.
\tag{E.5}
\]
Por (C.4), (B.4), (E.5) y $\|W(\tau)\|_4\ll\sqrt h$, la contribución de $\mathcal G^c$ a la correlación con $W$ es $o(1)$, tanto para $Q^\mathrm{pr}(x^{(1)})$ como para $\mathcal Q_J(\tau)$.
Con (D.4),
\[
\langle Q^\mathrm{pr}(x^{(1)})W(\tau)\rangle
=\langle\mathcal Q_J(\tau)W(\tau)\rangle+o(h).
\tag{E.6}
\]

## F. La diagonal es pequeña; fuera de la diagonal desaparece

Por (B.3), la media de $\mathcal Q_J(\tau)W(\tau)$ es, con error $o(1)$, la media Haar sobre fases primas. Por factorización única, un término de frecuencia cero necesita que el primo $q$ de $Q^\mathrm{pr}$ sea el mismo primo $p$ de $W$; las potencias de los primos base $\le X_1$ deben cancelarse. Los términos con fase $pq$ no tienen frecuencia cero. Se obtiene
\[
\langle\mathcal Q_J(\tau)W(\tau)\rangle
=\frac1{2\pi^2}\sum_{Y<p\le X_2}\frac1p
\Re\mathbb E_{\rm Haar}[F_{0,\xi_p}(P_0)F_{1,\xi_p}(P_1)]
+o(1).
\tag{F.1}
\]
Por (E.3), esa esperanza difiere de $\mathbb E_{\rm Haar}e^{i\xi_p(P_0+P_1)}$ en $o(1)$ uniformemente. Como cada sumando local de $P_0$ tiene media cero, amplitud $\ll p^{-1/2}$ y varianza $\asymp 1/p$, para $|\xi|\le C/\sqrt h$,
\[
|\mathbb E_{\rm Haar}e^{i\xi P_0}|
\le\exp\left(-c\xi^2\sum_{p\le Z}\frac1p\right)
\le \exp(-c'\xi^2H).
\tag{F.2}
\]
Los $p$ de $W$ satisfacen $\xi_p\ge (2\pi+o(1))\vartheta$, luego $\xi_p^2H\gg\omega^2\to\infty$. Se deduce
\[
\sup_{Y<p\le X_2}
|\mathbb E_{\rm Haar}F_{0,\xi_p}F_{1,\xi_p}|=o(1),
\quad
\langle\mathcal Q_J(\tau)W(\tau)\rangle=o(h).
\tag{F.3}
\]
Éste es el control ponderado fuera de la diagonal: no se toma una suma de valores absolutos individuales de errores sobre $p\ne q$, sino que se transfiere la **suma entera** a una media Haar de un polinomio corto. 

## G. Retirar la parte de primos bajos y concluir

La parte $S_{X_1}=P$ de $S_{X_2}$ no requiere Taylor. Para $x^{(1)}=\tau-P(\tau)/\Lambda(\tau)$, el argumento de transporte de v14 (función maximal de $P'$ sobre el intervalo entre $\tau$ y $x^{(1)}$) y los cuartos momentos de $P(\tau)$ y $P'$ dan
\[
\|P(x^{(1)})-P(\tau)\|_2
\ll \frac{\|P(\tau)\|_4}{\log T}\|{\cal M}P'(\tau)\|_4
\ll \sqrt H\,H^{-1/2}=O(1).
\tag{G.1}
\]
La ortogonalidad RvM entre $P(\tau)$ y $W(\tau)$ implica
$\langle P(\tau)W(\tau)\rangle=o(1)$; por Cauchy,
\[
\langle P(x^{(1)})W(\tau)\rangle=O(\sqrt h)=o(h).\tag{G.2}
\]
Las potencias primas en $Q=S_{X_2}-S_{X_1}$ y en $W$ tienen colas $o(1)$ en $L^4$ al estar sus primos base $\ge X_1\to\infty$, por ortogonalidad y las estimaciones de muestreo; reemplazarlas por sus partes solo primas no altera la correlación al orden $h$.

Combinando (E.6), (F.3) y (G.2),
\[
\langle S_{X_2}(x^{(1)})W(\tau)\rangle=o(h).
\]
Por (A.2)–(A.5),
\[
\boxed{B_c(T)=\left(\frac1{2\pi^2}+o(1)\right)\log\log\log T,}
\]
para todo $c\in(0,\tfrac12]$ fijo, **si la auditoría acepta todos los lemas uniformes y su aplicación a la versión exacta de $S_X$ de v14**. Se obtendría asimismo, porque $\|u(T^c)\|_2=O_c(1)$ y la curvatura es negligible,
\[
\langle r_k(T^c)^2\rangle\sim\frac{\log\log\log T}{2\pi^2},
\]
lo que resolvería negativamente la pregunta \`q:fixed_c\` para el reloj de un paso.

## H. Auditoría obligatoria antes de afirmar «demostrado»

1. **Verificar (B.1) para todo orden de derivada y la banda completa:** la potencia de $1+D$ debe ser absoluta, independiente de $j$; comprobar que las constantes de los cuartos momentos son uniformes al ponderar por $(\log q)^j$.
2. **Verificar (B.4) directamente contra el lema de multiplicidad v14:** sustituir $g$ por $Q^\mathrm{pr}$ y controlar su derivada en el muestreo $x^{(1)}$.
3. **Truncación de todas las potencias primas:** escribir las desigualdades $L^4$ de las colas en $Q,W$ y el error causado por reemplazar $P$ por $P^{[M]}$ dentro del desplazamiento; la cota determinista (C.1) no basta por sí sola sin controlar la derivada de $Q$.
4. **Congelar $\Lambda(\tau)$:** cuantificar el error con un maximal de $Q'$ sobre desplazamientos de tamaño $O(H^{3/4}/\log T)$, y con tratamiento separado de $\mathcal G^c$.
5. **Transferencia (B.3) para los momentos de $\mathcal Q_J$:** dar una cota explícita $\ell^1$ de los coeficientes y verificar cada exponente de longitud para los productos cuádruples, también cuando las potencias primas llegan a $m=M$.
6. **Teorema del segundo paso:** revisar de nuevo la conversión exacta entre $s_k-S_{X_2}(x^{(1)}_k)$ y $\Lambda(x^{(1)}_k)e_{2,k}$, incluyendo $\chi_{2,k}$, y su uniformidad para las dos ventanas de índices.
7. **Normalización:** en toda fórmula de $\xi_q$ usar $\log q/\lambda$, no $2\pi\theta_q$ literalmente, hasta haber absorbido el error $O(1/\log T)$.

Los puntos 1–7 son verificaciones matemáticas que deben cerrarse línea por línea. Esta nota conserva el argumento y las cotas propuestas y **no debe incorporarse como teorema validado a Paper I antes de ese control**. Tampoco se ha creado una versión nueva ni se han alterado manuscritos.
