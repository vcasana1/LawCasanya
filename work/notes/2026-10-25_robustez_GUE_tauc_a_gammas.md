# Robustez: si las tauc tienen estadística GUE y aciertan salvo un conjunto de densidad cero, los $\gamma$ también

Nota de Claude, 25-oct-2026. Sin ejecuciones numéricas en esta nota. Objetivo pedido por el autor: un teorema que cierre con "aunque las tauc pierdan algunos ceros, incluso infinitos pero pocos, los $\gamma$ siguen siendo GUE".

## 1. Marco

Ventana $T<t\le2T$; posiciones desplegadas $g=N_0(\gamma)$ (ceros, con multiplicidad) y $y=N_0(\kappa)$ (tauc). Para $n\ge2$ y $f:\mathbb R^{n-1}\to\mathbb R$ acotada, lipschitziana, con soporte en $[-A,A]^{n-1}$, la correlación de $n$ niveles de un conjunto finito $P$ de $M_P$ puntos es
$$R_n(f;P)=\frac1{M}\sum_{\substack{p_1,\dots,p_n\in P\\ \text{distintos}}}f(p_2-p_1,\dots,p_n-p_1),\qquad M=N(2T)-N(T).$$
Conteo local: $n_A(p;P)=\#\{q\in P:|q-p|\le A\}$.

## 2. Teorema de robustez (T)

**Hipótesis.**
- **(H0) Finitud local en media.** $\frac1M\sum_{p\in P}n_{A+2}(p;P)^{2n-2}\le C(n,A)$ para $P$ = ceros y $P$ = tauc.
- **(H1) Emparejamiento casi completo.** Existe una biyección $\varphi:P'\to Q'$ entre subconjuntos $P'\subset\{\text{ceros}\}$ y $Q'\subset\{\text{tauc}\}$ tal que
$$\#(\text{ceros}\setminus P')+\#(\text{tauc}\setminus Q')\le\eta_TM,\quad \eta_T\to0,\qquad \frac1M\sum_{p\in P'}\min\bigl(1,|p-\varphi(p)|\bigr)\to0 .$$
$\varphi$ **no** tiene por qué respetar los índices: se permite que las tauc pierdan o dupliquen ceros (desplazamiento de etiquetas), siempre que los no emparejados sean $o(M)$, y que algunos emparejados estén lejos, siempre que lo estén en densidad cero.

**Conclusión.** Para cada $n$ y cada $f$ como arriba,
$$R_n(f;\text{ceros})-R_n(f;\text{tauc})\longrightarrow0 .$$
En particular, si las correlaciones de las tauc convergen a los determinantes del núcleo seno, las de los ceros también. Lo mismo vale para la distribución de huecos entre vecinos (distancia de Lévy $\to0$): los huecos que involucran un punto no emparejado o mal emparejado son $o(M)$, y los demás difieren en $o(1)$ en media.

**Prueba.**
1. *Tuplas con algún punto no emparejado.* Contribuyen a lo sumo $\|f\|_\infty\frac nM\sum_{p\ \rm no\ empar.}n_A(p)^{n-1}\le\|f\|_\infty\,n\,\eta_T^{1/2}\bigl(\tfrac1M\sum_pn_A(p)^{2n-2}\bigr)^{1/2}=O(\eta_T^{1/2})$ por Cauchy–Schwarz y (H0), en cada uno de los dos conjuntos.
2. *Tuplas totalmente emparejadas.* Sea $\delta_p=\min(1,|p-\varphi(p)|)$. Si $f(\Delta)\ne f(\Delta')$ para las diferencias de una tupla y de su imagen, todos sus puntos están a distancia $\le A+2$ del primero (en uno de los dos conjuntos), y $|f(\Delta)-f(\Delta')|\le\min\bigl(2\|f\|_\infty,\ 2\,{\rm Lip}(f)\sum_j\delta_{p_j}\bigr)$, usando la cota $2\|f\|_\infty$ cuando algún $|p-\varphi(p)|>1$. Sumando, la diferencia es $\ll_{n,f}\frac1M\sum_p\delta_p\,n_{A+2}(p)^{n-1}\le\bigl(\tfrac1M\sum\delta_p\bigr)^{1/2}\bigl(\tfrac1M\sum n_{A+2}^{2n-2}\bigr)^{1/2}\to0$ (usando $\delta_p\le1$).
3. Las dos normalizaciones $M$ coinciden salvo $O(\eta_TM)$. $\square$

**(H0) ya está demostrada para lo que importa.**
- Ceros: incondicional, por los momentos de Fujii de $S(t+h)-S(t)$ (v14, Thm `known_fujii_difference`; Fujii 1974, p. 225), porque $N(t+h)-N(t)=\Lambda h+S(t+h)-S(t)+O(1/t)$.
- Tauc: para $n=2$ (correlación de pares y huecos), v14 Thm `multiplicity_all` da el segundo momento de los conteos locales de los puntos de Newton, con cortes $c_i\le\tfrac12$. Para la continuación hasta $c=1.30$ y para $n\ge3$ hace falta escribir la extensión (los puntos son raíces de $F_Y=k-\tfrac12$, y el conteo local está acotado por la variación total de $F_Y$, controlable con Montgomery–Vaughan en $\int|S_Y'|^2$); no está escrita.

## 3. Lo que hay que meter en el teorema para que diga "los $\gamma$ son GUE"

**(A) Las tauc son GUE.** Es un enunciado **sin ceros**: solo Lambert y primos.
- Para $0<|\alpha|<c$ en el factor de forma es la parte prima; demostrable con casi ortogonalidad y respuesta computable.
- Para $|\alpha|\ge1$, que es donde está la repulsión del núcleo seno, hay que sumar los canales de alias de v15 (cocientes $p/q\in(N,2N)$ con fase $e^{2\pi ip/q}$; productos $pq\asymp N^2$ con fase $e^{4\pi i\sqrt{pq}}$) y los términos de Bessel de grado alto del transporte. Son correlaciones de pares de primos: el análogo para tauc del argumento de Bogomolny–Keating (los ceros son GUE si valen las correlaciones de Hardy–Littlewood). Abierto, pero bien planteado y sin ceros.

**(B) El emparejamiento (H1).** Pide que el error de la tauc tienda a 0 **en densidad**, no en media cuadrática: se admiten $o(M)$ fallos de cualquier tamaño y pérdidas de etiqueta. Es más débil que $E_T\to0$. Pero sigue implicando que casi todos los ceros son simples y están en la recta, siempre que las tauc no se aglomeren (por ejemplo, si cumplen (A)): un cero doble necesitaría dos tauc a distancia $\to0$, o quedarse sin emparejar. Abierto.

## 4. Lo que da el teorema y lo que no

- (A) + (B) ⇒ los ceros tienen todas las correlaciones de GUE **y** casi todos son simples y están en la recta. No es RH: el conjunto excepcional puede ser infinito, de densidad cero, que es exactamente lo que pedía el autor.
- (A) sola ya sería un resultado: una sucesión determinista construida solo con Lambert y primos con estadística de núcleo seno.
- El test numérico en curso (`work/gaps_tauc/`) mide justamente cuánto de (B) se cumple a escala de huecos: el error en densidad de la mejor tauc y la cola de huecos pequeños.
