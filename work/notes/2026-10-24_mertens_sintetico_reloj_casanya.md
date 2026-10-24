# Mertens sintético del reloj Casaña de corte fijo: construcción, teorema de transición con factor de Euler e identidad con la $M$ friable

Nota de Claude, 24-oct-2026. Tarea 6.3 del traspaso (`work/notes/2026-10-24_traspaso_nuevo_chat_claude.txt`, §8.3). Sin ejecuciones numéricas. No se usan los ceros $\gamma_k$ en ninguna construcción ni prueba. Ningún manuscrito cambiado.

Fuentes leídas: `work/drafts_autor/Downloads/rvm_zeta_pi_mertens_v26.tex` (citado [v26]: §3 reloj, §4 Thm canónico, §8 Prop. Mcrit-poles, §9 Thm transition y su prueba, Thm unsmoothed-RVM, §11.4 Step 3, §15.2 Route B setting); `manuscript/ordinal_prime_cutoff_v14.tex` (Lema 8.19); biblioteca 125: S. M. Gonek, *Finite Euler products and the Riemann hypothesis*, Trans. AMS 364 (2012) 2157–2191, DOI 10.1090/S0002-9947-2011-05546-7 (leído: §3 pp. 2160–2161, §5 pp. 2168–2170, §6 Thm 6.2 p. 2170, §9 pp. 2179–2181).

Clases: **(T)** demostrado aquí o en la fuente citada; **(R)** reducción que implica el objetivo; **(A)** abierto.

---

## 0. Una aclaración previa sobre el Lema 8.19

El Lema 8.19 (*Sorted Newton steps*) de `ordinal_prime_cutoff_v14.tex` (l. 1852) es una desigualdad de reordenamiento: ordenar una lista no aumenta $\sum|z_k-\gamma_k|^q$. El "orden $\tau^C_k<\tau^C_{k+1}$" de los puntos Casaña se obtiene **reetiquetando**, no se demuestra que la aplicación $\tau\mapsto\tau-S_X(\tau)/\Lambda(\tau)$ sea creciente. Esto importa abajo: el teorema de transición necesita que los puntos sean los cruces de nivel de una función holomorfa **creciente**, y eso es una condición sobre $X$ frente a la altura (§1.2).

---

## 1. Construcción (sin ceros)

### 1.1. Fase de Euler y reloj Casaña de corte fijo

Fijo $X\ge2$. Producto de Euler finito completo (todas las potencias de los primos $p\le X$):

$$E_X(s):=\prod_{p\le X}(1-p^{-s})^{-1},\qquad \frac1{E_X(s)}=\sum_{n\mid P(X)}\frac{\mu(n)}{n^s},\qquad P(X):=\prod_{p\le X}p. \tag{1.1}$$

$1/E_X$ es un **polinomio de Dirichlet finito** con coeficientes $\mu(n)$ sobre los libres de cuadrados $X$-friables. Fase:

$$S_X(\tau):=\frac1{2\pi i}\Bigl(\log E_X(\tfrac12+i\tau)-\log E_X(\tfrac12-i\tau)\Bigr)=\sum_{p\le X}\sum_{m\ge1}\beta_{p^m}\sin(m\tau\log p),\qquad \beta_{p^m}=-\frac1{\pi m p^{m/2}}, \tag{1.2}$$

con la rama $\log E_X(w)=\sum_{p\le X}\sum_m p^{-mw}/m$. Es la fase prima del traspaso (mismos $\beta_{p^m}$), con todas las potencias de $p\le X$ en lugar de $p^m\le X$. $S_X$ es real en $\mathbb R$ y **holomorfa en la banda $|\Im\tau|<\tfrac12$** (las dos series convergen allí absolutamente). Reloj Casaña:

$$N_X(\tau):=N_0(\tau)+S_X(\tau),\qquad N_0(\tau)=\frac{\tau}{2\pi}\log\frac{\tau}{2\pi e}+\frac78. \tag{1.3}$$

### 1.2. Monotonía en la banda (lema clave, (T))

Para $0\le Y<\tfrac12$ sea

$$A_X(Y):=\frac1\pi\sum_{p\le X}\log p\,\frac{p^{Y-1/2}}{1-p^{Y-1/2}}\ \ \Bigl(\ge\sup_{x\in\mathbb R,\,|y|\le Y}|S_X'(x+iy)|\Bigr). \tag{1.4}$$

**Lema 1.** Sea $\tau'$ con $\Lambda(\tau')\ge2A_X(Y)$, $\Lambda(t)=\frac1{2\pi}\log\frac t{2\pi}$. Para $x\ge\tau'$ y $0\le y\le Y$:

$$\Im N_X(x+iy)\ \ge\ \tfrac12\,y\,\Lambda(x),\qquad \Im N_X(x-iy)\le-\tfrac12\,y\,\Lambda(x). \tag{1.5}$$

*Prueba.* $\partial_y\Im N_X(x+iy)=\Re N_X'(x+iy)$; $\Re N_0'(x+iy)=\frac1{2\pi}\log\frac{|x+iy|}{2\pi}\ge\Lambda(x)$, $|S_X'|\le A_X(Y)\le\frac12\Lambda(x)$; integrar de $0$ a $y$ ($\Im N_X(x)=0$). La segunda por conjugación. $\square$

En particular $N_X'(x)\ge\frac12\Lambda(x)>0$ en $[\tau',\infty)$. Como $A_X(Y)\asymp_Y\sqrt X$ por el teorema de Chebyshev, la condición es

$$\log\frac{\tau'}{2\pi}\ \ge\ 4\pi A_X(Y),\qquad\text{i.e. } X\ \ll_Y\ (\log\tau')^2. \tag{1.6}$$

Este es el **régimen de corte en que el reloj Casaña es un reloj** (cruces de nivel de una función creciente). Con $X=T^c$ (el $\tau^C$ de la teoría del transporte) se tiene $|S_X'|\asymp\sqrt X\gg\Lambda$ y la monotonía falla; ver §6.

### 1.3. La lista y la zeta Casaña

Fijo $0<\sigma_2'<\tfrac12$, $Y:=\tfrac12(\tfrac12+\sigma_2')$, y $\tau'=\tau'(X,\sigma_2')$ con $\Lambda(\tau')\ge2A_X(Y)$ y $N_X(\tau')+\tfrac12\notin\mathbb Z$. Sea $K':=\lfloor N_X(\tau')+\tfrac12\rfloor$.

**Definición.** $\kappa^X_1\le\dots\le\kappa^X_{K'}$ son $K'$ reales cualesquiera de $[2\pi,\tau')$ (por ejemplo equiespaciados); para $k>K'$, $\kappa^X_k$ es la única solución en $(\tau',\infty)$ de

$$N_X(\kappa^X_k)=k-\tfrac12. \tag{1.7}$$

La única restricción sobre los puntos bajos es su **número** $K'$; es lo que hace que el límite vertical sea constante (§2, paso 1). Entonces, exactamente,

$$n_X(\tau):=\#\{k:\kappa^X_k\le\tau\}=\bigl\lfloor N_X(\tau)+\tfrac12\bigr\rfloor\qquad(\tau\ge\tau'). \tag{1.8}$$

Relación con el reloj de un paso: de (1.7), $\kappa^X_k=\tau_k-\dfrac{S_X(\tau_k)}{\Lambda(\tau_k)}+O_X\bigl(\log^{-2}\tau_k\bigr)$; $\kappa^X_k$ es la **raíz exacta** del reloj corregido, a la que converge la iteración de Newton para $X$ fijo. $|\kappa^X_k-\tau_k|\le C(X)$: la lista es $C$-admisible en el sentido de [v26, Def. rb-lists].

$$\mathcal P_X(s):=\prod_{k\ge1}\Bigl(1+\frac{q(s)}{\frac14+(\kappa^X_k)^2}\Bigr),\qquad \zeta_{C,X}(s):=\frac{\mathcal P_X(s)}{G(s)},\qquad q(s)=s(s-1),\ G(s)=s(s-1)\Gamma(\tfrac s2)\pi^{-s/2}. \tag{1.9}$$

(T) por [v26, Thm canonical] y [v26, §15.2]: $\mathcal P_X$ entero, $\mathcal P_X(1-s)=\mathcal P_X(s)$, ceros exactamente en $\tfrac12\pm i\kappa^X_k$ (simples para $k>K'$); $\zeta_{C,X}$ tiene polo simple de residuo 1 en $s=1$; $F_{C,X}:=1/\zeta_{C,X}$ es holomorfa en $\Re s>\tfrac12$. **Todos los ceros no triviales en $\Re s=\tfrac12$ por construcción.** Para $X<2$ ($E_X\equiv1$, $S_X\equiv0$) se recupera $\zeta_{\RVM}$.

---

## 2. Teorema A: transición del producto Casaña (T)

**Teorema A.** Sean $X\ge2$ y $0<\sigma_2'<\tfrac12$ fijos. Existen $\varpi_X>0$ (que depende solo de $X$ y de la lista), $t_0=t_0(X,\sigma_2')$ y $C=C(X,\sigma_2')$ tales que, para $s=\tfrac12+\sigma'+it$, $0<\sigma'\le\sigma_2'$, $t\ge t_0$:

$$\zeta_{C,X}(s)=\varpi_X\,E_X(s)\,\bigl(1+w_X(s)\bigr)\bigl(1+\mathcal E_X(s)\bigr),\qquad |\mathcal E_X(s)|\le C\,t^{-\delta}\log t,\quad \delta=\tfrac{1+2\sigma_2'}8, \tag{2.1}$$

$$w_X(s):=e^{-2\pi i N_X(\tau_*)},\qquad \tau_*=t-i\sigma',\qquad |w_X(s)|\le\Bigl(\frac t{2\pi}\Bigr)^{-\sigma'/2}<1. \tag{2.2}$$

Además, con $\chi$ el factor de la ecuación funcional,

$$w_X(s)=\chi(s)\,\frac{E_X(1-s)}{E_X(s)}\bigl(1+O(t^{-1})\bigr),\qquad \zeta_{C,X}(s)=\varpi_X\bigl[E_X(s)+\chi(s)E_X(1-s)\bigr]+O_{X,\sigma_2'}\bigl(t^{-\delta}\log t\bigr). \tag{2.3}$$

**Prueba.** Sigue la de [v26, §9.1] con tres cambios. Notación: $z=\sigma'+it$, $f(\tau)=\operatorname{Log}(1+z^2/\tau^2)$, $f'(\tau)=-\frac2\tau+\frac1{\tau-iz}+\frac1{\tau+iz}$; el polo $\tau_*=-iz$ está en el semiplano inferior, $iz=-t+i\sigma'$ tiene parte real negativa.

*Paso 1 (corte en $\tau'$ y normalización).* Por (1.8), $n_X=N_X-\psi(N_X+\tfrac12)$ en $[\tau',\infty)$ y $n_X(\tau')=K'$. Stieltjes e integración por partes como en [v26, (transition-split)]:

$$\log\frac{\mathcal P_X(s)}{\mathcal P_X(\frac12)}=\sum_{k\le K'}\bigl[f(\kappa_k)-f(\tau')\bigr]-\int_{\tau'}^\infty N_Xf'\,d\tau+\int_{\tau'}^\infty\psi\bigl(N_X+\tfrac12\bigr)f'\,d\tau. \tag{2.4}$$

El término de frontera es $f(\tau')\bigl[K'-N_X(\tau')+\psi(N_X(\tau')+\tfrac12)\bigr]=0$. La suma finita vale $\sum_{k\le K'}2\log(\tau'/\kappa_k)+O(t^{-2})$: constante. Si el número de puntos bajos no fuera $K'$, aparecería un factor $z^{2j}$ y el límite vertical no sería constante.

*Paso 2 (parte lisa: aquí sale $E_X$).* $-\int N_Xf'=-\int N_0f'-\int S_Xf'$. El primer sumando es [v26, Lemma TR-smooth] con $\tau_0\to\tau'$: $\log G(s)+\nu_3'+O(t^{-1})$ (la $\tfrac78$ da $\tfrac74\operatorname{Log}z$, que casa con $G$). Para el segundo, término a término en $n=p^m$, $\ell=\log n$ (la serie en $m$ converge absolutamente y $\int_{\tau'}^\infty|f'|\ll\log t$):

$$I(\ell):=\int_{\tau'}^\infty\sin(\tau\ell)f'(\tau)\,d\tau=c_\ell+\pi\,e^{-i\tau_*\ell}+O\Bigl(\frac1{t\ell}\Bigr),\qquad e^{-i\tau_*\ell}=n^{1/2}n^{-s}.$$

$c_\ell$ viene de $-2/\tau$ (independiente de $z$, $|c_\ell|\le4/(\tau'\ell)$). El término $\pi e^{-i\tau_*\ell}$ viene de $-\frac1{2i}e^{-i\tau\ell}\cdot\frac1{\tau+iz}$, girando $[\tau',\infty)$ hacia el rayo $\tau'-iy$: el residuo en $\tau_*$, con la orientación de [v26, (lower-contour)], da $-\frac1{2i}(-2\pi i)e^{-i\tau_*\ell}$. Los otros tres trozos y el rayo son $O(1/(t\ell))$, porque $|\tau\pm iz|\ge t-\tau'$ en los contornos. Con $\beta_n=-1/(\pi m n^{1/2})$:

$$-\int_{\tau'}^\infty S_Xf'=-\sum_n\beta_nI(\ell_n)=\sum_{p\le X}\sum_{m\ge1}\frac{p^{-ms}}m+\nu_X+O_X(t^{-1})=\log E_X(s)+\nu_X+O_X(t^{-1}). \tag{2.5}$$

*Paso 3 (dientes de sierra: aquí sale $1+w_X$).* Regularización de Abel $\psi_r$ y $I^\pm_m=\int_{\tau'}^\infty e^{\pm2\pi imN_X}f'$, como en [v26, Lemma TR-harmonic]. **Cambio:** $e^{\pm2\pi imN_X}$ crece en vertical (porque $S_X$ crece fuera de la banda), así que los rayos verticales al infinito de v26 no sirven. Se usan contornos dentro de la banda: el segmento $[\tau',\tau'\pm iY]$ y la recta horizontal $\Im\tau=\pm Y$, con $Y>\sigma'$, de modo que el polo $\tau_*$ (de altura $-\sigma'$) queda dentro del contorno inferior. Por (1.5), en todo el contorno $|e^{\pm2\pi imN_X(x\pm iy)}|\le(x/2\pi)^{-my/2}$. El residuo da, como en v26, $R_m^--I_m^-=2\pi i\,w_X^m$, y $\sum_m-(-rw_X)^m/m=\operatorname{Log}(1+rw_X)$ porque $|w_X|<1$ por (1.5) en $\tau_*$. Esto también prueba la cota de (2.2).

La parte $-2/\tau$ de $f'$ da una constante real $\nu_{4,X}$, con mayorante $\sum_m m^{-2}$ uniforme en $r$. Queda $g_z=\frac{2\tau}{\tau^2+z^2}$ en la recta $\Im\tau=-Y$ ($x=\Re\tau$):
- $|g_z|\ll x/t^2$ si $x\le t/2$;
- $|g_z|\ll1/\max(|x-t|,Y-\sigma')$ si $t/2\le x\le2t$;
- $|g_z|\ll 1/x$ si $x\ge2t$.

Con el peso $x^{-mY/2}$, cada tramo es $\ll t^{-mY/2}\log t/(Y-\sigma')$. Sumando con $r^m/m$: $O(t^{-Y/2}\log t)$, uniforme en $r$. En los segmentos verticales, $|g_z|\ll1/t$. Por tanto

$$\int_{\tau'}^\infty\psi\bigl(N_X+\tfrac12\bigr)f'=\operatorname{Log}(1+w_X)+\nu_{4,X}+O_{X,\sigma_2'}(t^{-Y/2}\log t). \tag{2.6}$$

Se usa $Y-\sigma'\ge\tfrac12(\tfrac12-\sigma_2')$ y $Y/2=\delta$.

*Paso 4 (montaje).* Exponenciando (2.4)–(2.6) y dividiendo por $G$ se obtiene (2.1), con $\varpi_X:=\mathcal P_X(\tfrac12)e^{\nu'}$, donde $\nu'$ reúne las constantes reales de los pasos 1–3.

*Paso 5 ((2.3)).* Por (1.2), en $\tau_*$ se tiene $\tfrac12+i\tau_*=s$ y $\tfrac12-i\tau_*=1-s$, luego **exactamente**

$$e^{-2\pi iS_X(\tau_*)}=\frac{E_X(1-s)}{E_X(s)}.$$

Y $e^{-2\pi iN_0(\tau_*)}=\chi(s)(1+O(t^{-1}))$ es [v26, (w-chi)]. En $0<\sigma'<\tfrac12$, $E_X(s)$ y $E_X(1-s)$ están acotados en términos de $X$, y $|\chi|\le1$; de ahí la forma aditiva. $\square$

*Estado:* todos los pasos están escritos; las dominaciones uniformes en $r$ sobre las rectas horizontales del paso 3 están esbozadas (cotas por tramos) y **sin comprobar línea a línea**.

**Lectura de (2.3).** En la recta crítica, $E_X(\tfrac12-it)=\overline{E_X(\tfrac12+it)}$, luego

$$\zeta_{C,X}(\tfrac12+it)\approx\varpi_X\bigl[E_X(\tfrac12+it)+\chi(\tfrac12+it)\overline{E_X(\tfrac12+it)}\bigr].$$

Esto es, salvo la constante $\varpi_X$, el modelo $\zeta_X=P_X+\chi\overline{P_X}$ de Gonek (2012, §5, p. 2169), con el producto de Euler **sin pesos** en lugar del $P_X$ ponderado de Gonek. Los $\kappa^X_k$ son los ceros de ese modelo para $t\ge\tau'$: $1+w_X=0$ en la recta equivale a $N_X\in\tfrac12+\mathbb Z$, que es el análogo de que los ceros de Gonek sean las soluciones de $F_X(t)\equiv\pi\ (2\pi)$ (Gonek, Thm 6.2, p. 2170, y §9, p. 2180). La diferencia con Gonek es que aquí el objeto es **analítico**, un producto de Hadamard sobre los puntos del reloj, y en $\sigma'>0$ es $E_X(s)+\chi(s)E_X(1-s)$, que es precisamente la forma (5.2) que Gonek descarta como aproximación de $\zeta$ (p. 2169) porque $|E_X(1-s)|$ alcanza $\exp(X^{\sigma'}/\log X)$. Para $X$ fijo eso es una constante; para $X$ creciente es el obstáculo de §5.

---

## 3. Teorema B: Mertens Casaña $=$ Mertens friable $+$ raíz cuadrada (T)

**Definición.** Para $x>1$ y $c\in(\tfrac12,1)$:

$$M_{C,X}(x):=\lim_{U\to\infty}\frac1{2\pi i}\int_{c-iU}^{c+iU}\frac{x^s}{s\,\zeta_{C,X}(s)}\,ds. \tag{3.1}$$

Es la misma naturaleza de objeto que $M^{\rm crit}_{\RVM}$ de [v26, Thm unsmoothed-RVM]: transformada de Perron simétrica del recíproco de una zeta sintética. No es una función de saltos. (Advertencia 6.3 d del traspaso.)

**Teorema B.** Para $X\ge2$ y $\varepsilon\in(0,\tfrac12)$, el límite (3.1) existe, no depende de $c\in(\tfrac12,1)$, y

$$M_{C,X}(x)=\frac1{\varpi_X}\,M_X^*(x)+R_X(x),\qquad M_X^*(x):=\sideset{}{^*}\sum_{\substack{n\le x\\ n\mid P(X)}}\mu(n),\qquad |R_X(x)|\le\mathcal I_X(\varepsilon)\,x^{1/2+\varepsilon}, \tag{3.2}$$

donde $\sum^*$ da peso $\tfrac12$ al término $n=x$ y

$$\mathcal I_X(\varepsilon):=\frac1{2\pi\varpi_X}\int_{-\infty}^{\infty}\Bigl|\varpi_XF_{C,X}(\tfrac12+\varepsilon+it)-E_X(\tfrac12+\varepsilon+it)^{-1}\Bigr|\frac{dt}{|\tfrac12+\varepsilon+it|}<\infty. \tag{3.3}$$

**Prueba.** Se separa $F_{C,X}=\varpi_X^{-1}E_X^{-1}+(F_{C,X}-\varpi_X^{-1}E_X^{-1})$.

Por (1.1), $E_X^{-1}$ es un polinomio de Dirichlet finito, y la integral de Perron simétrica de $(x/n)^s/s$ vale $1$, $\tfrac12$ o $0$ según sea $n<x$, $n=x$ o $n>x$ (Davenport, cap. 17, como en [v26]). Esto da $\varpi_X^{-1}M^*_X(x)$.

El resto se controla con (2.1)–(2.2) en $\sigma'=c-\tfrac12\in(0,\tfrac12)$:

$$\varpi_XF_{C,X}-E_X^{-1}=E_X^{-1}\bigl[(1+w_X)^{-1}(1+\mathcal E_X)^{-1}-1\bigr]=O_{X,c}\bigl(t^{-\min(\sigma'/2,\,\delta)}\log t\bigr),$$

que es integrable contra $|s|^{-1}$. Para $|t|\le t_0$, $F_{C,X}$ es continua y no tiene polos en $\Re s=c$. La independencia de $c$ y el paso a $c=\tfrac12+\varepsilon$ son literalmente la prueba de [v26, Thm unsmoothed-RVM]. $\square$

**Comprobaciones.**
- Si $X<2$, entonces $E_X=1$, $M_X^*=1$, y (3.2) es $M^{\rm crit}_{\RVM}=L+O(x^{1/2+\varepsilon})$ de v26.
- Para $X$ fijo, $M_X^*(x)=\sum_{n\mid P(X)}\mu(n)=0$ en cuanto $x>P(X)$. Por tanto $M_{C,X}(x)=O_{X,\varepsilon}(x^{1/2+\varepsilon})$ y el término friable solo pesa en $x\le P(X)$.

### 3.1. La identidad con $M$ (el puente pedido)

Para todo $x\le X$, los $n\le x$ libres de cuadrados son $X$-friables, luego $M^*_X(x)=M^*(x):=\sum^*_{n\le x}\mu(n)$. De (3.2):

$$\boxed{\ M^*(x)=\varpi_X\,M_{C,X}(x)-\varpi_X R_X(x),\qquad |\varpi_XR_X(x)|\le\varpi_X\,\mathcal I_X(\varepsilon)\,x^{1/2+\varepsilon}\qquad(2\le x\le X).\ } \tag{3.4}$$

Es una **identidad**, no una aproximación en media. El lado derecho solo contiene:
- los puntos $\kappa^X_k$ del reloj Casaña de corte $X$;
- los primos $p\le X$;
- $\chi$ y $\Gamma$.

No interviene ningún cero de $\zeta$. Esto es lo que el autor pedía: una $M$ sintética del reloj corregido que coincide con la de Möbius, con error de raíz cuadrada.

---

## 4. Qué parte de (TR) se traslada y con qué hipótesis (punto (ii) del traspaso)

| Ingrediente de [v26, Thm transition] | Con $\kappa^X_k$ | Hipótesis exacta |
|---|---|---|
| Representación $n=N-\psi(N+\frac12)$ | (1.8), en $[\tau',\infty)$ | $N_X$ creciente en $[\tau',\infty)$; $K'=\lfloor N_X(\tau')+\frac12\rfloor$ puntos bajos |
| Parte lisa $=\log G+$ cte | $=\log G+\log E_X(s)+$ cte | $S_X$ holomorfa en $\lvert\Im\tau\rvert<\frac12$ (producto de Euler **completo** en $p\le X$) |
| Lema TR-clock ($\Im N\ge c\,\Im\tau$ en el cuadrante) | Lema 1, solo en la banda $\lvert\Im\tau\rvert\le Y<\frac12$ | $\Lambda(\tau')\ge2A_X(Y)$, i.e. (1.6) |
| Rayos verticales al infinito | segmento + recta horizontal $\Im\tau=\pm Y$ | $\sigma'<Y<\frac12$; error $t^{-Y/2}\log t$ en vez de $t^{-2}$ |
| $w=\chi(1+O(1/t))$ | $w_X=\chi\,E_X(1-s)/E_X(s)\,(1+O(1/t))$ | ninguna adicional |
| Banda $0<\sigma'\le B$ cualquiera | solo $0<\sigma'\le\sigma_2'<\frac12$ | la banda de holomorfía de $S_X$; basta para Perron en $c\in(\frac12,1)$ |

Separación de ordenadas: solo se usa que $N_X$ sea creciente; los ceros $\tfrac12\pm i\kappa_k$ son simples porque $\frac{d}{dt}w_X=-2\pi N_X'(\tau_*)w_X\ne0$ (análogo de [v26, Lemma TR-boundary]). Densidad: $N_X-N_0=S_X=O_X(1)$. $\varpi_X$: existe y es positiva; su valor no interviene.

---

## 5. Clasificación del puente y el obstáculo exacto (puntos (iii)–(iv))

La diferencia $M-M_C$, escrita como identidad (iii):

$$M^*(x)-\varpi_XM_{C,X}(x)=\underbrace{\bigl(M^*(x)-M_X^*(x)\bigr)}_{=0\ \text{si }X\ge x\ \ (T)}\;-\;\underbrace{\frac1{2\pi i}\int_{(\frac12+\varepsilon)}\bigl(\varpi_XF_{C,X}-E_X^{-1}\bigr)\frac{x^s}{s}\,ds}_{\varpi_XR_X(x)}. \tag{5.1}$$

**Cuidado con la circularidad.** Acotar $R_X$ no basta: en (3.4) el término principal de $\varpi_XM_{C,X}$ **es** $M^*_X$. En v26 el análogo era la constante $L$, que no tenía contenido. Aquí hacen falta dos cotas independientes, y la segunda es donde actúa que los polos de $F_{C,X}$ están todos en $\Re s=\tfrac12$.

**(R) Criterio.** Supongamos que, para cada $\varepsilon>0$ y con constantes independientes de $X$, para $2\le x\le X$:
- **(a)** $\varpi_X|R_X(x)|\ll_\varepsilon x^{1/2+\varepsilon}$, por ejemplo vía $\varpi_X\mathcal I_X(\varepsilon)\ll_\varepsilon x^{o(1)}$;
- **(b)** $\varpi_X|M_{C,X}(x)|\ll_\varepsilon x^{1/2+\varepsilon}$.

Entonces, por (3.4) con $X=x$, $M(x)=O_\varepsilon(x^{1/2+\varepsilon})$, es decir RH.

(b) es el mecanismo "no hay ceros que mirar": se desplaza (3.1) a $\Re s=-a<0$. Los residuos en $\tfrac12\pm i\kappa^X_k$ tienen $|x^{\rho}|=x^{1/2}$. A la izquierda se usa $\zeta_{C,X}(1-s)=\zeta_{C,X}(s)G(s)/G(1-s)$, porque $\mathcal P_X$ es simétrico. Se necesita además:
- cota inferior de $|\zeta_{C,X}|$ en rectas horizontales entre los $\kappa_k$ (por (2.1), en $\sigma'$ pequeño, lejos de $1+w_X=0$);
- cota de $\zeta'_{C,X}(\tfrac12+i\kappa_k)$, análogo de [v26, Cor. derivative-zeros]:

$$\zeta_{C,X}'(\tfrac12+i\kappa_k)\approx\varpi_X\,E_X(\tfrac12+i\kappa_k)\cdot2\pi N_X'(\kappa_k).$$

Para $X$ fijo es una adaptación directa de las pruebas de v26 (no escrita aquí; el tramo $t<\tau'$ es compacto): (b) con constante $C(X)$. La uniformidad en $X$ es (A).

La cantidad a controlar en (a) es explícita:

$$\varpi_X\mathcal I_X(\varepsilon)=\frac1{2\pi}\int_{\mathbb R}\Bigl|\frac1{E_X(s)}\Bigl[\frac1{(1+w_X(s))(1+\mathcal E_X(s))}-1\Bigr]\Bigr|\frac{dt}{|s|},\qquad s=\tfrac12+\varepsilon+it, \tag{5.2}$$

y su término principal es la **correlación firmada en la frecuencia del contador** que pedía 6.3 g:

$$-\frac{w_X}{E_X(1+w_X)}\approx-\frac{\chi(s)E_X(1-s)}{E_X(s)^2}\cdot\frac1{1+w_X(s)}.$$

Un solo objeto con primos $\le X$ y el reloj; ningún cero de $\zeta$.

**(A) Obstáculo concreto, uniformidad en $X$.** Las constantes del Teorema A dependen de $X$ por dos vías:
1. el umbral $\tau'$ de (1.6), $\log\tau'\gg A_X\asymp\sqrt X$;
2. los tamaños $|E_X(s)^{\pm1}|,|E_X(1-s)|\le\exp(O(X^{1/2+\varepsilon}/\log X))$ en $\Re s=\tfrac12\pm\varepsilon$.

Para $X=x$, el Teorema A no dice nada en alturas $|t|<\exp(c\sqrt x)$. La integral (5.2) en ese tramo no está controlada por la prueba actual: allí $N_x$ no es monótono, los puntos ya no son cruces de nivel de una función creciente y la representación (1.8) falla.

Es un **obstáculo de prueba y de uniformidad**, no una imposibilidad demostrada. La comprobación grosera de §2 no muestra divergencia de (5.2): en los $t$ donde $|E_X(1-s)|$ es máximo (fases $t\log p$ casi alineadas, Kronecker), $t$ es del orden de $\delta^{-\pi(X)}$ y $|\chi|\asymp t^{-\varepsilon}$ amortigua por $\exp(-\varepsilon\,\pi(X)\log(1/\delta))$. Como $\pi(X)\gg X^{1/2+\varepsilon}$, ese amortiguamiento domina al crecimiento puntual $\exp(X^{1/2+\varepsilon}/\log X)$. *Sin comprobar*: la medida de esos $t$ y el resto del integrando.

**Tabla de clases.**

| Paso | Clase |
|---|---|
| Construcción §1 (lista, $\mathcal P_X$, $\zeta_{C,X}$, ceros en $\frac12$) | (T) |
| Lema 1 (monotonía en la banda) | (T) |
| Teorema A, (2.1)–(2.3), $X$ fijo | (T), paso 3 sin comprobar línea a línea |
| Teorema B, (3.2) | (T) dado A |
| Identidad (3.4) para $x\le X$ | (T) dado B |
| (a) y (b) uniformes en $X$ $\Rightarrow$ RH | (R) |
| (b) para $X$ fijo (residuos en $\frac12\pm i\kappa_k$) | (A) no escrita; adaptación directa de v26 |
| Teorema A con constantes uniformes para $X\le(\log t)^2$ | (A), alcanzable: las constantes son explícitas en $A_X$ |
| Tramo $t<e^{c\sqrt X}$ (reloj no monótono) | (A), obstáculo de prueba |

---

## 6. Qué dice esto del $\tau^C$ con $X=T^c$ y siguiente paso propuesto

1. **Los $\tau^C$ con $X=T^c$ quedan fuera del Teorema A.** Ahí $|S_X'|\asymp\sqrt X\gg\Lambda$, no hay reloj monótono y el Lema 8.19 solo reordena. La aproximación en media del transporte ($\langle r^2\rangle\sim H_1/2\pi^2$) no entra en la prueba de A ni de B: lo que entra es la **estructura exacta** (1.8) más la holomorfía de $S_X$ en la banda. Por eso el puente (3.4) es una identidad y no una estimación en media.

2. **Construcción por bloques (A, prioridad alta, es la ruta IV del traspaso).** Usar corte $X_j$ constante en bloques de altura $[T_j,T_{j+1}]$, con $X_j\asymp(\log T_j)^2/C$, para que el reloj sea monótono en cada bloque, y repetir la prueba de A bloque a bloque. En los saltos de corte, $N$ tiene discontinuidades acotadas; hay que fijar el número de puntos en cada salto para que no aparezcan factores $z^{2j}$, como en el paso 1. Resultado esperado, sin comprobar:

$$\zeta_C\approx\varpi\,E_{X(t)}(s)\bigl(1+w\bigr)\quad\text{en el bloque de }t.$$

La $M_C$ asociada sería entonces la transformada de Perron de $E_{X(t)}(s)^{-1}$ con corte dependiente de la altura. Hay que identificar esa transformada con $M$ por una identidad tipo (3.4). El punto delicado es que Perron mezcla alturas: los primos $\in((\log t)^2,x]$ faltan en alturas $t<e^{\sqrt x}$.

3. **Alternativa sin monotonía (A).** Tomar como lista todos los cruces de $N_X\in\tfrac12+\mathbb Z$ (los ceros del modelo de Gonek con producto sin pesos, que están en la recta para $t\ge C_0$ por el argumento de Gonek, Lema 6.1 y Thm 6.2, p. 2170, que solo usa $P_X\ne0$). Entonces $X$ ya no está limitado por la altura. Falta una representación de $n(\tau)$ sustituta de (1.8) que permita el paso 3.

**Lo que tengo listo para escribir si se ordena:** la versión con constantes explícitas del Teorema A en función de $A_X(Y)$, y con ella la cota de $\varpi_X\mathcal I_X(\varepsilon)$ restringida a $|t|\ge\tau'(X)$; es el primer trozo cuantitativo de (5.2).
