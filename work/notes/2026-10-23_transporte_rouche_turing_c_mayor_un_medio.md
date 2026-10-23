# Hilo del 2026-10-23: Rouché + Turing, cortes c > 1/2 y energía del transporte

Autor de la investigación: V. Casaña-Giner (Doktor). Redacción: Claude, en `work/` (AGENTS.md §2).
Ningún manuscrito se ha creado ni modificado. Todo lo que aquí figura como «demostrado» se apoya en enunciados de la v14 de Paper I (`manuscript/ordinal_prime_cutoff_v14.tex`) que se citan por etiqueta; lo que es modelo o derivación sin verificar se marca así en línea.

Notación (la de la v14): $\gamma_k$ ordenadas de los ceros con multiplicidad; $\tau_k$ el reloj RvM del punto medio, $N_0(\tau_k)=k-\tfrac12$; $s_k=N_0(\tau_k)-N_0(\gamma_k)$; $\Lambda(t)=\frac1{2\pi}\log\frac t{2\pi}$ la densidad (en la v14, $\lL$); $S_X$ la fase prima con potencias de primos hasta $X$; $a_p=-\frac1{\pi\sqrt p}$, $a_p^2=\frac1{\pi^2p}$; defecto $u_k(X)=s_k-S_X(\gamma_k)$; reloj de un paso $\tau_k^X=\tau_k-S_X(\tau_k)/\Lambda(\tau_k)$; error $r_k(X)=\Lambda(\tau_k)(\tau_k^X-\gamma_k)$; transporte $\mathfrak t_k(X)=S_X(\gamma_k)-S_X(\tau_k)$; $r_k=u_k+\mathfrak t_k+\chi_k$ con $0\le\chi_k\ll1/T$ (eq. `r_decomposition`). Medias $\langle\cdot\rangle$ sobre $\mathcal I_T=\{k:T<\gamma_k\le2T\}$. Para $X=T^c$: $A=\langle u^2\rangle$, $B_c(T)=\langle\mathfrak t^2\rangle$, $R=\langle r^2\rangle$. $V_T=\frac{\log\log T}{2\pi^2}$.

## Índice de ficheros de este hilo

| Fichero | Contenido |
|---|---|
| `work/paper1/rouche_cert/rouche_one_zero.py` | Certificado de Rouché de un cero con índice por Turing (Arb) |
| `work/paper1/rouche_cert/block_k1400737_n300.{csv,json,log}`, `block_k1000055_n300.{csv,json,log}` | Dos bloques de 300 índices |
| `work/paper1/transport_note/s2_window_2p19.{py,out,json}` | $\langle s_k^2\rangle=0.11279$ en la ventana de la Tabla 7 |
| `work/paper1/pendiente_siguiente_version/transporte_tabla7_2026-10-23.md` | Corrección del factor $1/(2\pi^2)$ y modelo local |
| `work/paper1/pendiente_siguiente_version/universalidad_transporte_2026-10-23.md` | Material propuesto para Paper I: teorema de universalidad del transporte |
| `work/display/2026-10-23_c_mayor_un_medio_termino_principal.md` | Respuesta verbatim: término principal para $c>1/2$ |
| `work/display/2026-10-23_transporte_tabla7_limite.md` | Respuesta verbatim: transporte y Tabla 7 |
| `work/display/2026-10-23_aportes_externos_transporte/01–07` | Textos aportados por el autor durante el hilo, copia literal (ver §10) |
| `work/paper1/rouche_cert/v4check_k*_n300.{json,log}` | Primera ejecución del validador corregido de la v4 |
| `work/prime_spiral/v4/` | v4 de ChatGPT (tex, txt idénticos al archivo de `chatgpt/`) y PDF compilado por Claude |
| `work/library/INDEX.md`, `work/library/_renumeracion_2026-10-23.tsv` | Espejo del índice de LIBRARY TOTAL y tabla de renumeración |
| este fichero | Informe completo |

---

## 1. Certificado de Rouché de un cero y asignación de índice (Turing)

### 1.1 Enunciado
$f(z)=\xi(\tfrac12+iz)$ es entera y real en el eje real. En la práctica se usa $Z(t)=e^{i\vartheta(t)}\zeta(\tfrac12+it)$, analítica y real cerca del eje y con los mismos ceros que $f$ en discos pequeños con $t>0$. Para un centro $b$ y un radio $r$, sea $Z(b+w)=\sum_{j<K}z_jw^j+R_K(w)$ con $|R_K|\le\sup_{|w|\le r}|z_K(b+w)|\,r^K$. Si

$$|z_0|+\sum_{2\le j<K}|z_j|r^j+\sup_{\rm disco}|z_K|\,r^K<|z_1|\,r,\qquad\text{(R)}$$

Rouché (comparando con $z_0+z_1w$) da exactamente un cero de $Z$ en $|w|<r$. El disco es simétrico respecto del eje real y los ceros no reales vienen en pares conjugados, así que ese cero es real y simple.

### 1.2 Implementación (`rouche_one_zero.py`)
- Aritmética de bolas de Arb vía `python-flint` 0.9.0, a 120 bits; $K=7$; jet de Taylor exacto en el centro. El coeficiente $z_K$ se acota evaluando la serie sobre una bola que contiene el disco.
- **Por qué no se acota $Z''$ directamente.** Evaluar $\zeta$ sobre una bola a altura $6\cdot10^5$ sobrestima por un factor del orden de $\sqrt N\log N$ (se suman valores absolutos de $n^{-s}$). Con $Z''$ la cota salía $\approx1.3\cdot10^5$ frente al valor real $\approx50$. El resto de Taylor de orden 7 multiplica esa sobrestimación por $r^7$ y la hace inofensiva.
- **Re-centrado de Newton.** Si (R) falla en $x_k$, se re-centra en $b_1=x_k-Z/Z'$ y se toma $r=r_1+|b_1-x_k|$. Es lícito: es verificación, no construcción.
- **Radio máximo** 0.2; el espaciado medio a $t\approx6\cdot10^5$ es $\approx0.55$.
- **Índice.** `acb.zeta_zero(k)` de Arb devuelve el $k$-ésimo cero con índice certificado por el método de Turing con cotas rigurosas. Turing **no se ha reimplementado**. Se comprueba que esa bola cae dentro del disco.
- Los centros $x_k$ salen de `work/data/zCasanya.bin`. El programa no lee `zeross.bin`, que solo se usó después para comparar.

### 1.3 Resultados

| Bloque | Certificados | Fallos de (R) | Índice no coincidente | Discos consecutivos solapados | $r$ medio | Error real medio | Mediana $r/\text{error}$ |
|---|---|---|---|---|---|---|---|
| $k=1\,400\,737$–$1\,401\,036$ (30 % final, intacto) | 292 | 8 | 0 | 2 | 0.0430 | 0.0336 | 1.46 |
| $k=1\,000\,055$–$1\,000\,354$ | 292 | 8 | 0 | 0 | 0.0385 | 0.0289 | 1.49 |

- En los 584 discos certificados, el error real $|\gamma_k-x_k|$ (medido con `zeross.bin`) quedó por debajo de $r_k$.
- Los 16 fallos son índices con error real entre 0.06 y 0.17, de los mayores del bloque pero muy por debajo del espaciado. Un fallo de (R) **no** indica que $x_k$ esté mal: (R) es solo una condición suficiente.
- Coste: 2–3 s por índice.
- **Alcance:** es una verificación finita. No es un teorema para todo $k$ y no es un paso hacia RH. Además usa $\zeta$ para verificar; la construcción de los $x_k$ no la usa.

### 1.3 bis Fallo en la comprobación del índice (señalado por ChatGPT en la v4) y nueva ejecución
- **El fallo.** En los casos re-centrados por Newton, el programa certifica un único cero en $D(b_1,r_1)$, pero comprobaba que la bola de `acb.zeta_zero(k)` estuviera en el disco **ampliado** $D(x_k,r_1+|b_1-x_k|)$, que contiene a $D(b_1,r_1)$ y puede contener otros ceros. En esos casos no queda probado que el cero certificado sea el de índice $k$. Afecta a 238 de los 584 éxitos (130 en el bloque de $k=1\,400\,737$ y 108 en el de $k=1\,000\,055$). Los 346 casos centrados en $x_k$ no tienen el problema. La cota $|\gamma_k-x_k|<r_k$ sí es correcta en todos, porque la bola de Arb cae dentro de $D(x_k,r_k)$; lo que no queda probado es que ese cero sea el certificado por Rouché.
- **Corrección.** ChatGPT escribió `chatgpt/casanya_prime_spiral_short_v4_20261023/rouche_one_zero_v4.py`, que comprueba la pertenencia al propio disco de Rouché, con comparaciones de bola por los dos lados y 160 bits. No lo había podido ejecutar. Aquí se ejecuta por primera vez sobre los mismos dos bloques; las salidas están en `work/paper1/rouche_cert/v4check_k*_n300.{json,log}` y los resultados en §1.3 ter.
- El programa original queda sin tocar, como registro.

### 1.3 ter Resultados del validador corregido
En curso al hacer el primer commit de este informe (unos 10 índices cada 3 minutos por bloque). Se añadirán aquí en un commit posterior.

### 1.4 Por qué no hay versión analítica «para todo $k$»
Para que (R) valga para todo $k$ harían falta dos cosas:
1. $|Z(x_k)|$ pequeño para todo $k$, lo que equivale a controlar $S(t)$ punto a punto (`prop:envelope_equivalence`).
2. $|Z'(x_k)|$ lejos de 0 para todo $k$, lo que excluye las parejas cercanas.

Ninguna de las dos se conoce sin RH. El resto de Taylor, en cambio, sí se puede acotar para todo $t$ con cotas de convexidad. La versión «para casi todo $k$» tampoco sale: los teoremas B, D′ y D″ dan momentos y colas (cotas de cola, del tipo $\#\{|r_k|>w\}\ll w^{-2}$) y no la cota de bola pequeña $\#\{|r_k|<\theta\}\ge p\,\#\mathcal I_T$ que haría falta. Con $c\le\frac12$ el error medio es del orden de un espaciado, y la constante del teorema B no es explícita.

---

## 2. Cortes $c>\frac12$ y RH

- **Para todo $k$, implicaría RH.** Si para un $c$ fijo se demostrara $|x_k^{(c)}-\gamma_k|<\frac12(x_{k+1}^{(c)}-x_k^{(c)})$ para todo $k\ge k_0$, con los $x_k$ estrictamente crecientes (D′ da separación $\ge\pi/\log T$), no podría haber ordenadas repetidas. Un cero $\rho$ fuera de la recta lleva siempre $1-\bar\rho$ con la misma ordenada. Por tanto: RH, y además simplicidad de todos los ceros. El enunciado es más fuerte que RH.
- **En media no implica RH.** Una media siempre deja un conjunto excepcional de densidad cero.
- **Para $c\le\frac12$, lo demostrado es en media** (B, D, D′, D″). Lo único «para todo $k$» es el teorema E, $\limsup|\tau_k-\gamma_k|<0.60832$, y es para el reloj sin corregir. Al ser una constante en unidades de ordenada (no de espaciado), no separa ceros: hay pares con separación menor que 0.1. Con el perfil de Lindelöf, el método de Backlund con disco no baja de 0.494.
- **Novedad del teorema E:** el método es el de Backlund (Trudgian; Hasanalizade–Shen–Wong; Bellotti–Wong). Lo propio es la fórmula general en términos del perfil $\mathfrak e(\sigma)$ y la constante con los pares de exponentes de Bourgain. No se ha comprobado si la constante 0.0968 ya aparece publicada.

---

## 3. Por qué la prueba del teorema B se para en $c=\frac12$

Identidad exacta para cualquier $X$ (`main_step1`):
$$\sum_k u_k(X)^2=\int_T^{2T}E_X^2\,\Lambda\,dt+\int_T^{2T}E_X^2\,S_X'\,dt-\frac{\#\mathcal I_T}{12}+O(T^{3/4}),\qquad E_X=S-S_X .$$

- **Primer término.** Usa el segundo momento de $W=S_X-S_{Y_0}$. Por Montgomery–Vaughan vale hasta $X\approx T^{1-\varepsilon}$.
- **Segundo término.** La prueba usa Cauchy–Schwarz con $\int E_X^4$, es decir, el segundo momento de $W^2$, un polinomio en $n=pp'\le X^2$. Montgomery–Vaughan da un error $\sum n|\eta_n|^2\approx X^2$, que supera a $T$ en cuanto $X>T^{1/2}$: se pierde una potencia $T^{2c-1}$.
- **Qué haría falta (sin comprobar).** Para $X^2>T$, los pares de semiprimos con $|pp'-qq'|\le h=X^2/T$ tendrían que cancelarse a través del núcleo de Fejér, lo que pide la varianza de los semiprimos en intervalos cortos de longitud $T^{2c-1}$. Sin ella solo se gana hasta $c=\frac12+O(\log\log T/\log T)$.
- Para $c>1$ la fórmula $\frac1{2\pi^2}\log\frac1c$ se vuelve negativa, así que el término principal tiene que cambiar.

### 3.1 Ley de diferencias en media en $t$ (derivada a mano; **sin verificar línea a línea; novedad sin comprobar**)
Sea $w$ una ventana suave en $[T,2T]$ y $X'<X\le T^{1-\varepsilon}$, $W=S_X-S_{X'}$.
- Como $S_{X'}\perp W$ (primos distintos, ventana suave), $\|E_{X'}\|_w^2=\|E_X\|_w^2+2\langle S,W\rangle_w-\|W\|_w^2$.
- **Diagonal de $W$.** Los términos no diagonales llevan $\hat w(T\log(p/q))$ con $|\log(p/q)|\ge1/X\ge T^{-1+\varepsilon}$ y son $O(T^{-A})$.
- **$\langle S,W\rangle_w$.** Por la fórmula explícita de Weil con $h(r)=w((r-T)/H)e^{ir\log p}$ y $H=T/\log T$, solo sobrevive $n=p$, y los términos de polos son despreciables. Resulta $\langle S,W\rangle_w=\|W\|_w^2(1+o(1))$.

Conclusión: para $0<c'<c<1$,
$$\frac1T\bigl(\|E_{T^{c'}}\|_w^2-\|E_{T^c}\|_w^2\bigr)=\frac{\hat w(0)}{2\pi^2}\log\frac c{c'}+o(1),$$
es decir, $\frac1T\|S-S_{T^c}\|_w^2=A_T+\frac{\hat w(0)}{2\pi^2}\log\frac1c+o(1)$ con $A_T$ independiente de $c$ (la parte de $S$ ortogonal a todos los primos $\le T$, el diente de sierra).

### 3.2 Media sobre los ceros para $\frac12<c<1$
- Por $S_X^2S_X'=\frac13(S_X^3)'$, la integral $\int S_X^2S_X'$ es solo un término de borde.
- Queda $\int S^2S_X'-2\int SS_XS_X'$. Con $S'=-\Lambda+\sum_\gamma\delta_\gamma$, ambos términos se convierten en sumas sobre ceros, $\sum_\gamma S_X(\gamma)^2$ y $\sum_\gamma S(\gamma)S_X(\gamma)$, que llevan la correlación de pares $F(\alpha)$ con $\alpha\le c$.
- Conjetura: el término principal sigue siendo $\frac1{2\pi^2}\log\frac1c+A'$.
- Las taucs no sirven para evaluar esas sumas con error $o(1)$: el transporte $S_X(\gamma_k)-S_X(x_k)$ es $O(1)$ en media, del mismo orden que el término principal; acotarlo con $c>\frac12$ vuelve a pedir cuartos momentos de longitud $X^2>T$; y el argumento es circular.

---

## 4. Transporte: corrección de la Tabla 7 y modelo local

### 4.1 Corrección (programa `s2_window_2p19.py`)
El texto de la v14 tras `tab:transport` dice que el transporte es «smaller than $c^2\log\log T$ ($=0.103,0.287,0.644$) by factors 21–35». Esa comparación omite el factor $\frac1{2\pi^2}$. En la misma ventana $2^{19}<\gamma_k\le2^{20}$ (977 804 ceros), $\langle s_k^2\rangle=0.11279$:

| $c$ | $c^2\langle s^2\rangle$ | $\langle\mathfrak t^2\rangle$ (Tabla 7) | cociente |
|---|---|---|---|
| 1/5 | 0.00451 | 0.004905 | 1.087 |
| 1/3 | 0.01253 | 0.011391 | 0.909 |
| 1/2 | 0.02820 | 0.018283 | 0.648 |

El transporte tiene el tamaño ingenuo. Lo real es la cancelación $2\langle u\mathfrak t\rangle\approx-\langle\mathfrak t^2\rangle$, con un porcentaje compensado de 98.1 %, 95.3 % y 87.0 %.

### 4.2 Modelo local (no es teorema)
Con $S_X$ lineal entre $\gamma_k$ y $\tau_k$, $a=S_X(\gamma_k)$, $\sigma=S_X'/\Lambda$ y $K=S_X(\tau_k)$, se tiene exactamente $s_k=(K+u_k)/(1+\sigma)$. Para todo punto $x$ calculable con el reloj y los primos $\le X$,
$$\Lambda(x-\gamma_k)=\Bigl[\Lambda(x-\tau_k)+\frac K{1+\sigma}\Bigr]+\frac{u_k}{1+\sigma}.$$
- Con el peso $dN=(\Lambda+S')dt$ propio de la media sobre ceros sale $\langle u\mathfrak t\rangle\approx-c^2\langle u^2\rangle$. El signo es correcto, pero explica solo el 40–70 % (correlaciones predichas −0.115, −0.157, −0.204 frente a las observadas −0.171, −0.336, −0.533).
- **Límite:** el defecto entra siempre como $u_k/(1+\sigma)$, y la única información sobre $u_k$ al alcance del reloj es $K$, con correlación $O(c^2\langle u^2\rangle/\langle a^2\rangle)$ (≈3 % con $c=\frac12$). El transporte puede impedir que el error crezca, pero no bajarlo por debajo del defecto. Bajar el error exige reducir $u$, es decir, más primos.

---

## 5. Energía del transporte $B_c(T)$: hechos elementales demostrados

Con $A=O_c(1)$ (teorema B) y $\|\chi\|_2\ll T^{-1}$:
- $|\sqrt R-\sqrt B|\le\sqrt A+\|\chi\|_2$, luego $R=O_c(1)\iff B=O_c(1)$.
- Si $B\to\infty$, entonces $R=B+O_c(\sqrt B+1)$ y $R/B\to1$.
- Por Cauchy–Schwarz, $|2\langle u\mathfrak t\rangle|\le2\sqrt{AB}=o(B)$ cuando $B\to\infty$: la fracción compensada tiende a 0. La compensación del 87–98 % y un transporte divergente no pueden coexistir hasta el infinito.
- La «proposición» del texto 01 ($\mathcal C_c=O(1)\Rightarrow\dots$) equivale a `q:fixed_c` y no aporta nada nuevo; el texto 02 la retira.

---

## 6. Modelo para $B_c(T)$ (predicción, no teorema)

Suponiendo las fases independientes de $s_k$ y usando Mertens ($\sum1/p\leftrightarrow d\theta/\theta$, $\theta_p=\log p/\log T$):
$$B_c(T)\approx\frac2{\pi^2}\mathbb E_s\!\int_0^c\sin^2(\pi\theta s)\frac{d\theta}\theta .$$
Con $s$ gaussiano de varianza $V_T$ esto es $\frac1{2\pi^2}\operatorname{Ein}(2\pi^2V_Tc^2)$ (forma cerrada del texto 03), y
- **régimen inicial:** $c^2V_T-\frac{\pi^2}2c^4V_T^2+\dots$;
- **asintótico:** $\frac{\log\log\log T}{2\pi^2}+\frac{\log c^2+\gamma_E}{2\pi^2}+o(1)$.

| $c$ | modelo | Tabla 7 | obs./modelo |
|---|---|---|---|
| 1/5 | 0.004413 | 0.004905 | 1.11 |
| 1/3 | 0.011798 | 0.011391 | 0.97 |
| 1/2 | 0.024713 | 0.018283 | 0.74 |

Con $c=\frac12$ el modelo sobrestima un 26 %: $s_k$ contiene las mismas fases, y la independencia supuesta falla justo donde aparece la cancelación.

**Error en el texto 03:** su cota (7), $B\ll1+\log(c^2H)$, no está en la v14 tal como se enuncia (D″ da $\ll1+\log\log\log T$ uniformemente).

---

## 7. Hacia la cota inferior $B_c(T)\gg\log\log\log T$

### 7.1 Proyección (rigurosa)
Para toda $g$, Cauchy–Schwarz da $B\ge\langle\mathfrak t\,g\rangle^2/\langle g^2\rangle$. Se toma $g_k=W(\tau_k)$, con $W$ la parte de $S_X$ con $\theta_p\in[\theta_T,c]$ y $\theta_T=\omega_T/\sqrt{V_T}$. Esta $g$ depende solo del reloj.

### 7.2 Lado del reloj (riguroso)
Para $x=\log(q/p)\ge T^{-\theta_T}$ las sumas del reloj valen $\sum_ke^{i\tau_kx}\ll\Lambda/x$. Por tanto
$$\langle W(\tau)^2\rangle=L_T+O_c(1),\qquad L_T=\frac1{2\pi^2}\log\frac c{\theta_T}\sim\frac1{4\pi^2}\log\log\log T,$$
y $\langle S_Y(\tau)W(\tau)\rangle=o(1)$. Con $c=\frac12$, la resonancia de borde $2\theta_p\approx1$ aporta solo $O(1)$.

### 7.3 Cancelación diagonal (demostrada)
**Lema.** Si $s_k/\sqrt{V_T}$ tiene ley límite sin átomo en 0 (lo garantiza `cor:signed_law`: $s_k/\mathfrak s_T\to N(0,1)$), entonces
$$\Bigl\langle\int_{\theta_T}^c\cos(2\pi\theta s_k)\frac{d\theta}\theta\Bigr\rangle=o\Bigl(\log\frac c{\theta_T}\Bigr).$$
*Prueba.* Integrando por partes, $\bigl|\int_{\theta_T}^c\cos(2\pi\theta s)\frac{d\theta}\theta\bigr|\le\frac1{\pi\theta_T|s|}$. Se separan los índices con $|s_k|<\sqrt{V_T}/\sqrt{\omega_T}$ (proporción $\to0$, cada uno aporta $\le\log(c/\theta_T)$); en los demás la cota es $\le1/\sqrt{\omega_T}\to0$.

**Paso a la suma sobre primos.** Por sumación parcial con Mertens,
$$\sum_{T^{\theta_T}<p\le T^c}\frac{g(\theta_p)}p=\int g\frac{d\theta}\theta+O\Bigl(\frac{\|g\|_\infty+\operatorname{Var}g}{\theta_T\log T}\Bigr),\qquad\operatorname{Var}\cos(2\pi\theta s)\le4c|s| .$$
Hay que usar la **media** $\langle|s_k|\rangle\ll\sqrt{V_T}$, que da un error medio $\ll V_T/(\omega_T\log T)\to0$. La cota puntual $|s_k|\ll\log T$, que es la que invoca el texto 04, no basta.

### 7.4 Dicotomía (demostrada; texto 04, verificada)
Con $\langle\mathfrak t\,W(\tau)\rangle=D_T+\mathcal O_T-L_T$ ($D_T=o(L_T)$ por 7.3):
$$B\ge\frac{(L_T-\mathcal O_T+o(L_T))^2}{L_T+o(L_T)} .$$
Si $B=O_c(1)$, entonces necesariamente $\mathcal O_T=L_T+o(L_T)$.

### 7.5 Régimen asintótico inalcanzable
La banda $\theta_T<c$ exige $\log\log T>2\pi^2\omega_T^2/c^2$; con $c=\frac12$ y $\omega_T=1$, $T>e^{e^{79}}$. A cualquier altura calculable la banda está vacía, de modo que la Tabla 7 vive entera en el régimen previo. Si se demuestra la cota inferior, el resultado sería del tipo de Odlyzko–te Riele: los datos sugieren compensación y el teorema demuestra lo contrario a alturas inalcanzables.

### 7.6 Reducción (A) (texto 05; **verificada término a término**)
Sean $\omega_T=(\log V_T)^{1/8}$, $\theta_T=\omega_T/\sqrt{V_T}$, $Y=T^{\theta_T}$, $X=T^c$ y $W=S_X-S_Y$. Identidades exactas: $\mathfrak t_X=\mathfrak t_Y+W(\gamma)-W(\tau)$ y $W(\gamma)=u_Y-u_X$.
- $\langle\mathfrak t_Y^2\rangle\ll\theta_T^2\log\log T=2\pi^2\omega_T^2=o(L_T)$ (lema de transporte de la v14).
- Términos cruzados con $\mathfrak t_Y$: $\ll\omega_T\sqrt{L_T}=O((\log V)^{5/8})=o(L_T)$.
- $\langle W(\gamma)^2\rangle=\langle u_Y^2\rangle+O(\sqrt{L_T})=L_T+O(\sqrt{L_T})$ (teorema B con $c=\theta_T$).
- $\langle W(\gamma)W(\tau)\rangle=\langle sW(\tau)\rangle-\langle S_Y(\gamma)W(\tau)\rangle-\langle u_XW(\tau)\rangle$, y los dos últimos son $o(L_T)$.

Resultado, sin RH ni modelo:
$$B_c(T)=2L_T-2\langle s_kW(\tau_k)\rangle+o(L_T).$$

### 7.7 Forma en términos de la respuesta del teorema C (nueva)
Con $\Rt_p=\frac2{a_p}\langle s_k\sin(\tau_k\log p)\rangle$, se tiene $\langle sW(\tau)\rangle=\frac1{2\pi^2}\sum_p\Rt_p/p$, y por tanto
$$\boxed{B_c(T)=\frac1{\pi^2}\sum_{T^{\theta_T}<p\le T^c}\frac{1-\Rt_p}p+o(\log\log\log T).}$$
Sea $\overline{\mathcal R}_c(T)$ la media de $\Rt_p$ con peso $1/p$ en la banda. La cota inferior equivale a $\overline{\mathcal R}_c\le1-\delta$.
- **Corrección de una afirmación mía:** dije que el error acotado con $c$ fijo equivale a $\overline{\mathcal R}_c\to1$. Es falso tal cual: $\overline{\mathcal R}_c\to1$ solo da $B=o(L_T)$. La implicación en el otro sentido (de $B=O(1)$ a $\overline{\mathcal R}_c\to1$) sí vale (texto 06).
- Por la identidad de transporte de la v14 (`thm:twist`), $\Rt_p$ es, salvo normalización, $\frac1T\int p^{it}e^{i\xi_pG}dt$ con $\xi_p=2\pi\theta_p$: una función característica de $S$ torcida por un primo. El modelo gaussiano–Bessel predice $\Rt_p\approx\mathbb E e^{i\xi_pS^{(p)}}\to0$ en la banda.

### 7.8 Universalidad en el exponente (texto 06; **verificada**)
Para $0<a<b\le\frac12$ fijos, con $W=S_{T^b}-S_{T^a}$: $\mathfrak t_b-\mathfrak t_a=W(\gamma)-W(\tau)$, $W(\gamma)=u(T^a)-u(T^b)$, $\langle W(\gamma)^2\rangle=O_{a,b}(1)$ (teorema B) y $\langle W(\tau)^2\rangle=O_{a,b}(1)$ (ortogonalidad en el reloj). Por tanto
$$\bigl|\sqrt{B_b(T)}-\sqrt{B_a(T)}\bigr|=O_{a,b}(1).$$
Consecuencias:
- `q:fixed_c` tiene la misma respuesta para todo $c\in(0,\frac12]$ fijo.
- Si $B_a\to\infty$, entonces $B_b/B_a\to1$.
- Junto con 7.9 (texto 07), $B_a-B_b=O_{a,b}(\sqrt{\log\log\log T})$. Todos los exponentes fijos comparten $\liminf$ y $\limsup$ de $B_c/\log\log\log T$, y basta demostrar la cota inferior para uno solo.

### 7.9 Cota superior con constante explícita (texto 06; **verificada**)
Sean $H=\log\log T$, $Y=T^{1/\sqrt H}$ y $L=\frac1{2\pi^2}\log(c\sqrt H)$. Entonces $\|\mathfrak t_Y\|_2=O(1)$ (lema de transporte con $c_Y^2H=1$), $\|W(\gamma)\|_2^2\le L+O(\sqrt L)$ y $\|W(\tau)\|_2^2=L+o(1)$. De ahí $\sqrt{B_c}\le2\sqrt L+O(1)$, es decir,
$$B_c(T)\le\frac1{\pi^2}\log\log\log T+O_c\bigl(\sqrt{\log\log\log T}\bigr).$$
D″ da el mismo orden con constante implícita; aquí la constante es explícita. Es el doble de la que predice el modelo, $\frac1{2\pi^2}$.

### 7.10 Forma de correlación y obstrucción (texto 06; verificada)
Con $U_k=W(\gamma_k)$ y $V_k=W(\tau_k)$ (banda de 7.6): $\overline{\mathcal R}_c=\langle U,V\rangle/L+o(1)$, $|\overline{\mathcal R}_c|\le1+o(1)$ y $B_c=2L(1-\langle U,V\rangle/L)+o(L)$. El objetivo $\limsup\langle U,V\rangle/L\le\frac12$ daría $B_c\ge(\frac1{4\pi^2}-o(1))\log\log\log T$. Los segundos momentos solos no bastan: tanto $U=V$ como $U=-V$ son compatibles con todo lo demostrado.

### 7.11 Lo que falta
Una sola desigualdad: que la correlación entre $W(\gamma_k)$ y $W(\tau_k)$ en la banda móvil no supere $\frac12$ (o $1-\delta$). Equivale a $\overline{\mathcal R}_c\le1-\delta$. Herramientas candidatas:
- el desacoplo multiescala de Arguin–Bourgade–Radziwiłł (`004_…FHK_I`, §7–8; `005_…FHK_II`), pero está hecho para $\log|\zeta|$ y no para $S(t)$ muestreado en los ceros;
- el lema de desacoplo para polinomios (Taylor truncado de $e^{-i\xi S_Y}$ con $Y=T^{1/(C\log\log T)}$, momentos gaussianos por Montgomery–Vaughan), que se sabe probar.

El factor no polinómico $e^{-i\xi E_Y}$ (primos altos y diente de sierra) sigue abierto. Cauchy–Schwarz sobre los primos pierde demasiado.

---

## 8. Estado

| Resultado | Estado |
|---|---|
| Certificados Rouché + Turing(Arb), 584/600 | Verificación numérica finita; índice no probado en los 238 casos de Newton (§1.3 bis); nueva ejecución con el validador de la v4 en §1.3 ter |
| Corrección del factor $1/(2\pi^2)$ (Tabla 7) | Errata de la v14, comprobada con programa |
| Ley de diferencias en media $t$, $0<c'<c<1$ | Derivada, **sin verificar**; novedad sin comprobar |
| Modelo $B\approx\frac1{2\pi^2}\operatorname{Ein}(2\pi^2V_Tc^2)$ | Modelo |
| Límite del transporte (modelo lineal local) | Modelo |
| Cancelación diagonal (7.3) | Demostrado |
| Dicotomía (7.4) | Demostrado |
| Reducción (A) y fórmula con $\Rt_p$ (7.6–7.7) | Demostrado a partir de la v14 |
| Universalidad en $c$ (7.8) | Demostrado a partir de la v14 |
| $B_c\le(\pi^{-2}+o(1))\log\log\log T$ (7.9) | Demostrado a partir de la v14 |
| $\overline{\mathcal R}_c=\langle U,V\rangle/L+o(1)$ (7.10) | Demostrado |
| $\limsup\overline{\mathcal R}_c\le\frac12$ / $B_c\gg\log\log\log T$ | **Abierto** |

Todo lo demostrado en §7 está escrito con los objetos del autor (reloj, defecto, transporte, respuesta $\Rt_p$) y es nuevo en ese sentido. «Demostrado a partir de la v14» significa que la prueba usa los teoremas B y D″, el lema de transporte y la ortogonalidad del reloj de la v14, y que conviene revisar sus hipótesis de uniformidad (rango de $c$, $T\ge T_0$) al redactar.

## 9. Aportes de ChatGPT en este hilo

**Textos aportados por el autor** (copia literal en `work/display/2026-10-23_aportes_externos_transporte/`):

| Nº | Contenido | Valoración |
|---|---|---|
| 01 | Cancelación del transporte; «proposición» $\mathcal C_c=O(1)\Rightarrow\dots$; compensación del 87–98 % | Cifras correctas; la proposición equivale a `q:fixed_c` y no aporta nada nuevo |
| 02 | $\lvert\sqrt R-\sqrt B\rvert=O(1)$, $R=O(1)\iff B=O(1)$, $R\sim B$ si $B\to\infty$ | Correcto (§5) |
| 03 | Modelo $\frac1{2\pi^2}\operatorname{Ein}(2\pi^2V_Tc^2)$ y comparación con la Tabla 7 | Coincide con el modelo de Claude; su cota (7) no está en la v14 (§6) |
| 04 | Cancelación diagonal, dicotomía, objeciones a Arguin–Bourgade–Radziwiłł | Correcto, salvo el paso por Mertens, que necesita la media de $\lvert s_k\rvert$ (§7.3–7.4) |
| 05 | Reducción (A) | Verificada término a término (§7.6); llegó con fórmulas perdidas al pegar |
| 06 | Universalidad, cota $1/\pi^2$, forma de correlación, obstrucción; corrige una afirmación de Claude | Verificado (§7.7–7.10) |
| 07 | $B_a-B_b=O(\sqrt{\log\log\log T})$; propuesta editorial | Correcto (§7.8); propuesta recogida en `pendiente_siguiente_version/universalidad_transporte_2026-10-23.md` |

**Artículo v4 de ChatGPT** (*Prime-Corrected Clocks and Synthetic Zeta Functions: Local Rouché Certificates and Rigorous Indexing*, autor Rotkiv Aynäsac). Archivado por ChatGPT en `chatgpt/casanya_prime_spiral_short_v4_20261023/` (commit b9b69f2) y copiado sin cambios en `work/prime_spiral/v4/` junto con el PDF compilado (17 páginas). Secciones:
- preliminares analíticos y aritméticos;
- teorema de separación por índice;
- zeta sintética, ecuación funcional y núcleos positivos;
- corrección prima analítica y flujo ordenado;
- fase aritmética exacta y resonancias racionales;
- zeta completada y clasificación de dos ceros;
- Rouché de un cero e indexado de Turing;
- momentos de Hankel, realidad por bloques y parejas cercanas aisladas;
- experimentos y comprobaciones;
- barreras globales;
- apéndices con los programas Arb y las limitaciones.

La v4 es anterior a la corrección de la Tabla 7 y a §5–§7 de este informe, y no los incluye. Su contribución directa a este hilo es haber detectado el fallo de §1.3 bis y haber escrito el validador corregido.

## 10. Biblioteca (fuera del repositorio)
- Añadidos `004_Arguin-Bourgade-Radziwill_2020_Fyodorov_Hiary_Keating_Conjecture_I.pdf` (arXiv:2007.00988v2) y `005_Arguin-Bourgade-Radziwill_2023_Fyodorov_Hiary_Keating_Conjecture_II.pdf` (arXiv:2307.00982v1). Los dos son incondicionales y están en la §10 del índice.
- LIBRARY TOTAL renumerada por completo (001–312, orden alfabético ASCII, sin excepciones). Tabla de equivalencias en `~/Documents/LIBRARY TOTAL/RENUMERACION_2026-10-23.md`. Las notas antiguas de este repositorio que citan la biblioteca por número usan la numeración anterior.
