# Verificación de las correcciones v13 → v14 (derivaciones propias)

Cada corrección que toca una demostración se deriva aquí antes de aplicarse. Las referencias de línea son a la v13.

## 1. Lema 8.2 (higher_moments), segunda cota

Hipótesis: $X\le T^{1/(160r)}$, $2r\le\kappa_F\log T$, $k_1=N(T)$, $k_2=N(2T)+1$ (así la suma de la identidad recorre exactamente $\mathcal I_T$).

1. $(|E_X|+T^{-1})^{2r}\le 2^{2r-1}(E_X^{2r}+T^{-2r})$ (convexidad de $x\mapsto x^{2r}$).
2. Hölder: $\int_T^{2T}E_X^{2r}\le T^{1/2}\mathcal E_{4r}^{1/2}$.
3. Cauchy–Schwarz con (eq:SX_derivative), $\int_T^{2T}S_X'^2\le C_d T(1+\log X)^2$:
   $\int E_X^{2r}|S_X'|\le \mathcal E_{4r}^{1/2}\,\sqrt{C_d}\,T^{1/2}(1+\log X)$.  **(v13 escribía $C_d$: error.)**
4. $\int T^{-2r}(\mathcal L+|S_X'|)\le T^{-2r}\bigl(T\mathcal L(2T)+\sqrt{C_d}\,T(1+\log X)\bigr)=T^{1/2}\cdot T^{-2r+1/2}(\mathcal L(2T)+\sqrt{C_d}(1+\log X))$.
5. Suma: integral $\le 2^{2r-1}(\mathcal L(2T)+\sqrt{C_d}(1+\log X))\,T^{1/2}(\mathcal E_{4r}^{1/2}+T^{-2r+1/2})$.
6. $\mathcal L(2T)\le2\mathcal L(T)$, $1+\log X\le 2\pi\mathcal L(T)$ (pues $X\le T^{1/2}$ y $T\ge T_0$): el paréntesis es $\le(2+2\pi\sqrt{C_d})\mathcal L(T)$.
7. $\#\mathcal I_T\ge\frac12T\mathcal L(T)$: el cociente es $\le 2^{2r}(2+2\pi\sqrt{C_d})\,T^{-1/2}(\mathcal E_{4r}^{1/2}+T^{-2r+1/2})$.
8. Término de contorno: $\le 9\pi C_b(Cr^2)^{2r}\#\mathcal I_T$ (texto). Total:
   $\langle u_k^{2r}\rangle\le 2^{2r}(2+2\pi\sqrt{C_d})T^{-1/2}(\mathcal E_{4r}^{1/2}+T^{-2r+1/2})+9\pi C_b(Cr^2)^{2r}$.
9. Primera cota: $\mathcal E_{4r}\le Z^{4r}T$, $Z=C(r^2+\sqrt{r(1+V)})$, con $C\ge1$, luego $Z\ge1$. Entonces $T^{-1/2}\mathcal E_{4r}^{1/2}\le Z^{2r}$ y $T^{-2r}\le1\le Z^{2r}$; $(Cr^2)^{2r}\le Z^{2r}$.
10. $\langle u_k^{2r}\rangle\le(2^{2r}K_1+K_2)Z^{2r}$ con $K_1=4+4\pi\sqrt{C_d}$, $K_2=9\pi C_b+1$ (el $+1$ asegura $K_2\ge1$).
11. $2^{2r}K_1+K_2\le2^{2r}(K_1+K_2)\le(2(K_1+K_2))^{2r}$ porque $K_1+K_2\ge1$.
12. Conclusión: la segunda cota vale con $2(K_1+K_2)C=2(5+4\pi\sqrt{C_d}+9\pi C_b)\,C$ en lugar de $C$.  **(v13 decía $2(4+2\pi\sqrt{C_d}+9\pi C_b)C$, que no sale de la desigualdad citada.)**

## 2. $V$ con el corte $Y_{2r}$ (Lema 8.2 y Teorema 8.3)

$V=\sum_{X<p\le Y_{2r}}p^{-1}$ con $Y_{2r}=T^{1/(160r)}\ge X$. Mertens ($\sum_{p\le y}1/p=\log\log y+M+O(1/\log y)$, $y\ge2$): $V=\log\frac{\log Y_{2r}}{\log X}+O(1)=\log\frac1{160rc}+O(1)$, con $O(1)$ absoluto (no depende de $r$) y $160rc\le1$. El Lema V_size sólo cubre $Y_0$; se cita ahora Mertens directamente.

## 3. Teorema 8.11 (uniform_iteration)

### 3a. Absorción de $C'$ (paso)
$1+V\le\log\frac1{c_j}+K=\frac12H_j+K\le(K+1)H_j$ si $H_j\ge1$; $K$ es la constante de Mertens de 2. Entonces $C(r^2+\sqrt{r(1+V)})\le\sqrt{K+1}\,C(r^2+\sqrt{rH_j})$: se reemplaza $C$ por $\sqrt{K+1}\,C$, que es absoluta y se fija antes que $C_\star$ y $H^*$. $H_j\ge1$ se usa sólo para $j\le m-1<m^*$, donde $H_j\ge H^*\ge1$; $H^*\ge1$ es una condición sobre $H^*$, que se fija después: no hay circularidad.

### 3b. Rango de la recursión (eq:uniform_recursion)
Se enuncia para $1\le j<m^*$ (donde $H_j\ge H^*\ge1$). En el último paso $j=m\le m^*$ se usa sólo el término de transporte, que requiere $H_{j-1}\ge1$ ($j-1<m^*$).

### 3c. $\log H_{j-1}\le H_j$
Para $j=1,2$: $H_j=\log H_{j-1}$. Para $j\ge3$: $H_j=\frac98\log H_{j-1}+a$ con $a=2\log(1/C_\star)\ge0$ ($C_\star\le1$), luego $H_j\ge\log H_{j-1}$ cuando $\log H_{j-1}\ge0$, es decir $H_{j-1}\ge1$.

### 3d. $m^*=\log^*T+O(1)$
Sea $L_j=\log^{(j)}H_0$ ($H_0=\log\log T$) y $K=a+1$.
- Cota superior. Si $L_{j-1}\ge K$ para todo $j\le J$, entonces $H_j\le\frac98L_j+K$ para $1\le j\le J$. Para $j=1,2$, $H_j=L_j\ge0$. Para $j\ge3$, por inducción, $H_j\le\frac98\log(\frac98L_{j-1}+K)+a\le\frac98(L_j+\log\frac{17}8)+a\le\frac98L_j+K$, porque $\frac98L_{j-1}+K\le\frac{17}8L_{j-1}$ y $\frac98\log\frac{17}8=0.848<1$.
- Sea $J$ el primer índice con $L_J<K$; entonces $J\le\log^*T+O_K(1)$ y $H_J\le\frac{17}8K$. Para $j\ge J$, mientras $H_{j+1}\ge H^*$ se tiene $H_{j+1}\le H_j/4$ (paso "three conditions": $H_{j}\ge4H_{j+1}$ cuando $H_{j+1}\ge H^*$). Así hay a lo sumo $1+\log_4(\frac{17}8K/H^*)_+$ índices más con $H\ge H^*$, y $m^*\le\log^*T+O_{C_\star,H^*}(1)$.
- Cota inferior. Por 3c, $H_j\ge L_j$ mientras $L_{j-1}\ge1$, luego $m^*\ge\log^*T-O_{H^*}(1)$.

Sólo la cota superior se usa ($2^{m^*+1}\le\kappa_F\log T$).

### 3e. Base: $X=2$ admisible
$2r\le\kappa_F\log T=\log T/(300\log2)$ implica $160r\log2\le\frac{160}{600}\log T<\log T$, es decir $2\le T^{1/(160r)}$.

### 3f. Umbral de $H^*$
$H_{j-1}\ge4^{m-j}H^*\ge160^2\,4^{m-j}$ basta con $H^*\ge160^2$, de modo que el factor 4 sobra (corrección cosmética; se deja $\max(4C_6,160^2)$).

### 3g. Constantes del enunciado
La prueba da $\|\mathcal L e_j\|_4\le4B_\star\sqrt{H_j}$ y $O(1+\sqrt{H_m})$ en el último paso, con constante implícita absoluta. La $C$ del enunciado no es la $C$ de los lemas. Se llama ahora $C_4$, el máximo de $4B_\star$ y de esa constante implícita, y la $C'$ de (eq:final_clock) pasa a ser $C_7$.

## 4. Proposición 8.8 (deformation): caso del Lema 8.2
$\|\mathsf g_2\|_{16}$ y $\|\mathsf g_2'\|_{16}$ requieren $\int|\partial_t^\nu S_{X_2}|^{16}$, es decir $4r=16$, $r=4$, que exige $X_2\le T^{1/(2r)}=T^{1/8}$. **(v13 decía "caso $r=2$" con la condición de $r=4$.)**

## 5. Lema 8.5 (sampling_rho): constante de $\|\mathsf F'\|_2$
Tercera cota con $2r$: $\|\partial_t^\nu S_X\|_{L^{8r}(\Omega)}\le(2Cr)^{1/2}T^{1/(8r)}(1+\log X)^\nu$. Entonces $\|(\varphi^\sharp S_X')'\|_{8r}\le2\|S_X'\|+\|S_X''\|\le3(2Cr)^{1/2}T^{1/(8r)}(1+\log X)^2$, y $\|\mathsf F'\|_2\le4r\|g\|_{8r}^{4r-1}\|g'\|_{8r}\le12r(1+\log X)(C'\sqrt r(1+\log X))^{4r}T^{1/2}$. Además $b\cdot12r(1+\log X)<48$, porque $b\cdot4r(1+\log X)<16$, así que el factor $17$ pasa a $49$.

## 6. Teorema 8.6 (second_step): admisibilidad de $r=2$
Hace falta $X_1\le T^{1/320}$: $c_1=H_0^{-1/2}=(\log\log T)^{-1/2}\le\frac1{320}$ para $T\ge T_0$. Además $4\le\kappa_F\log T$.

## 7. Lema 8.7 (second_identity)
$\mathcal L(\tau)y^{(j)}=\mathcal L(\tau)(1-\frac{\mathcal L(\tau)}{\mathcal L(x)})y^{(j-1)}+\frac{\mathcal L(\tau)}{\mathcal L(x)}(S_{X_j}(x)+\tilde\chi)$, luego
$\mathfrak r=\mathcal L(\tau)(1-\frac{\mathcal L(\tau)}{\mathcal L(x)})y^{(j-1)}+(\frac{\mathcal L(\tau)}{\mathcal L(x)}-1)S_{X_j}(x)+\frac{\mathcal L(\tau)}{\mathcal L(x)}\tilde\chi$. El tercer término lleva el factor $\mathcal L(\tau)/\mathcal L(x)=1+o(1)$. Las cotas son $T^{c_{j-1}-1}$, $T^{(c_{j-1}+c_j)/2-1}$ y $T^{c_{j-1}-1}$, todas $\le T^{\max(c_{j-1},c_j)-1}$. Para $j=1$, $x^{(0)}=\tau$, de modo que $y^{(0)}=0$ y $\mathfrak r_{1,k}=0$ (se pone $c_0:=0$). La cota $\tilde\chi\le y^2/(4\pi(T-T^{1/2}))$ necesita $\min(\tau_k,x^{(j-1)}_k)\ge T-T^{1/2}$, que vale para $\tau_k\ge T-1$ y $|y^{(j-1)}|\le T^{1/2}-1$. Se renombra $\chi''$ como $\tilde\chi$.

## 8. Lema 8.4 (multiplicity)
- Un punto $t$ está en a lo sumo $m$ de los intervalos cerrados $J_{k,m}=[\tau_k,\tau_{k+m}]$ salvo $t=\tau_i$ (puede estar en $m+1$): "para casi todo $t$", suficiente para la integral.
- (eq:SX_derivative) está enunciada en $[T,2T]$ y se aplica en $[T-1,2T+1]\subset[T-1,2T-2]\cup[T+1,2T+2]$, con $T'=T-1$ y $T'=T+1$, $X_1\le T'^{1/2}$. Es lo mismo que en la prueba del Teorema 7.5.

## 9. Lema 8.9 (zero_pairs), Hölder
$\int_{T-1}^{2T}f^3\le(T+1)^{1/4}(\int f^4)^{3/4}$: la medida es $T+1$. **(v13: $T^{1/4}$.)**

## 10. Lema 5.11 (maximal_primes)
$\sum_{X_-<p\le X_+}p^{-2}\le V_\pm/X_-\le4V_\pm/X_+\le4V_\pm^2$. El último paso usa $V_\pm\ge1/X_+$, que vale porque en este caso $(X_-,X_+]$ contiene un primo $p\le X_+$.

## 11. Proposición 8.1 (recursion)
La cota en normas promedia sobre $k\in I$, así que hace falta $x^{(i)}_k>2\pi$ para $0\le i\le j-1$ y todo $k\in I$ (para que $\mathcal L(x^{(i)}_k)>0$ y los iterados estén definidos).

## 12. Teorema E, observación (b)
El programa v9 rotulaba "published + ABA", pero calculaba sólo el casco de ABA. El v10 calcula el casco de la unión; su salida (outputs/envelope_best_profile_v10.txt) se comprueba antes de cambiar el texto.

## 13. Resumen e introducción (afirmaciones mayores que los teoremas)
- Colas: el Teorema 8.3 da $2^{2-\sqrt{\lambda/C_8}}$ (exponencial estirada), en un rango de $c$ que depende de $\lambda$. El Corolario clock_tails da momentos para $1\le j<m^*$, $q\le2^{m^*-j}$ y $T\ge T_0(j,q)$.
- D′: unicidad sobre la malla fija $\mathcal K_T$.
- E: hipótesis de continuidad, $\mathfrak e(1)=0$ y cota uniforme.
- F: suma sobre $T<\gamma_k\le2T$, $j\ge1$.

## 14. Correcciones tras la comprobación de los pasajes cambiados (audit/revision3)
- Resumen (A): $\mathfrak g$, $\mathfrak G$ en toda la frase.
- Observación (c) del Teorema E: $2\pi\mathsf C_L$.
- Observación (b) del Teorema E: sea $s_{\rm c}<3\cdot10^{-7}$ el cruce con la cota de Heath-Brown $\kappa(1-\sigma)^{3/2}$, $\kappa=\frac8{63}\sqrt{15}=0.4918$. Por convexidad, $\mathfrak e_{\mathcal P}$ queda bajo la cuerda de $(1-s_{\rm c},\kappa s_{\rm c}^{3/2})$ a $(1,0)$, de pendiente $a=\kappa\sqrt{s_{\rm c}}$.
  - Parte directa: $\int_{1-s_{\rm c}}^1 a(1-\sigma)/\sqrt{\sigma(2-\sigma)}\le a s_{\rm c}^2$.
  - Parte reflejada: $\int_0^{s_{\rm c}}a\sigma/\sqrt{\sigma(2-\sigma)}\le\frac23 a s_{\rm c}^{3/2}$, usando $\sqrt{\sigma(2-\sigma)}\ge\sqrt\sigma$.
  - Total: $\le a(s_{\rm c}^2+\frac23s_{\rm c}^{3/2})/(2\pi\log2)=6.8\cdot10^{-15}<10^{-14}$. La v14 enuncia $<10^{-14}$; el $10^{-15}$ de la v13 no estaba justificado por el argumento escrito.
- $V=\sum_{X<p<Y_{2r}}$: el conjunto $\mathcal J$ de (eq:D_def) es abierto en $Y_0$.
- Corolario sorted_clock: la localización se usa sólo para $k\in\mathcal I_T^\tau$ ($\tau_k\ge T$), dentro de la nueva hipótesis $\tau_k\ge T-1$ del Lema 8.7.
- Introducción G: no se nombran $t_1$, $k_0$ antes de definirlos.
- $J\to j_\circ$ en el argumento de $m^*$; $\mathsf C_{\mathcal P'}$, $\mathsf C_{\mathcal P''}$ para los conjuntos ampliados.
