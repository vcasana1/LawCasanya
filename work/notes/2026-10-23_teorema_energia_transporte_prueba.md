# Teorema: la energía del transporte del reloj de un paso diverge como $\frac1{2\pi^2}\log\log\log T$

Redacción: Claude, 2026-10-23, en `work/` (AGENTS.md §2). Ningún manuscrito modificado.
Base: Paper I v14 (`manuscript/ordinal_prime_cutoff_v14.tex`), cuyos enunciados se citan por etiqueta.
Antecedentes en este repositorio: `work/notes/2026-10-23_transporte_rouche_turing_c_mayor_un_medio.md` (§5–§7) y `work/display/2026-10-23_aportes_externos_transporte/`.
**Sustituida por la prueba completa en `work/paper1/transport_theorem/transport_energy_theorem_v1.{tex,txt,pdf}`, donde A1–A4 están escritas (Lemas 4.5, 4.6, 4.7 y 7.1).** La auditoría de rigor de esta versión previa está en §6. Lo que allí figura como «adaptación» es un paso que no está escrito aquí línea a línea.

## 0. Enunciado

Para $c\in(0,\frac12]$ fijo, $X=T^c$, y con la notación de la v14 ($\tau_k$ reloj RvM del punto medio, $s_k=N_0(\tau_k)-N_0(\gamma_k)$, $u_k(X)=s_k-S_X(\gamma_k)$, $\mathfrak t_k(X)=S_X(\gamma_k)-S_X(\tau_k)$, $r_k(X)=\Lambda(\tau_k)(\tau_k^X-\gamma_k)$, medias $\langle\cdot\rangle$ sobre $\mathcal I_T=\{k:T<\gamma_k\le2T\}$):

> **Teorema.** $B_c(T):=\langle\mathfrak t_k(T^c)^2\rangle=\dfrac1{2\pi^2}\log\log\log T\,(1+o(1))$, y por tanto $\langle r_k(T^c)^2\rangle=\dfrac1{2\pi^2}\log\log\log T\,(1+o(1))$.

**Consecuencia.** La pregunta `q:fixed_c` de la v14 tiene respuesta negativa para el reloj de un paso: con exponente de corte fijo, el error en unidades de espaciado no está acotado. Crece en el orden exacto que permitía D″, con constante $\frac1{2\pi^2}$, la misma para todo $c$. La compensación del 87–98 % de la Tabla 7 es un efecto de altura finita: la banda de primos que la destruye solo existe a partir de $\log\log T>2\pi^2\omega_T^2/c^2$.

## 1. Parámetros y notación

- $H_0=\log\log T$, $H_1=\log H_0$, $H_2=\log H_1$.
- Cortes del segundo paso de la v14: $X_1=T^{H_0^{-1/2}}$, $X_2=T^{H_1^{-1/2}}$.
- $V=\frac{H_0}{2\pi^2}$, $\omega=\omega_T=(\log V)^{1/8}$, $\theta_T=\omega/\sqrt V$, $Y=T^{\theta_T}$, $Z=T^{H_0^{-2}}$.
- Para $T\ge T_0$: $Z<X_1<Y<X_2<X=T^c\le T^{1/2}$. En concreto, $X_1<Y$ porque $\theta_T\sqrt{H_0}=\pi\sqrt2\,\omega\to\infty$, e $Y<X_2$ porque $\theta_T\sqrt{H_1}\to0$.
- $\Lambda(t)=\frac1{2\pi}\log\frac t{2\pi}$; $\Lambda_0=\Lambda(T)$; en la ventana, $\Lambda(\tau_k)=\Lambda_0+O(1)$.
- $S_X(t)=\sum_{p\le X}\sum_{m\ge1}\beta_{p^m}\sin(mt\log p)$ con $\beta_{p^m}=-\frac1{\pi m p^{m/2}}$ (eq. `SX_def`). Se escribe $a_p=\beta_p$.
- $W=S_X-S_Y$ y $L=L_T=\frac1{2\pi^2}\log\frac c{\theta_T}=\frac{H_1}{4\pi^2}+O(\log H_1)$.
- Primer punto corregido $\rho_k=x^{(1)}_k=\tau_k-S_{X_1}(\tau_k)/\Lambda(\tau_k)$ (exacto, porque $N_0(\tau_k)=k-\frac12$), y $Q=S_{X_2}$.
- **Modelo de fases independientes.** $\theta_r$ uniformes e independientes para cada primo $r$; la fase de $r^m$ es $m\theta_r$. Su esperanza es $\mathbb E_{\rm mod}$.

## 2. Lemas auxiliares

**L1 (sumas del reloj).** Sea $\omega\in\mathbb R$ con $0<|\omega|\le\frac34\log T$, y sea $w$ una sucesión en $\mathcal I_T$ de variación acotada. Entonces
$$\Bigl|\sum_{k\in\mathcal I_T}w_ke^{i\omega\tau_k}\Bigr|\ll(\|w\|_\infty+\operatorname{Var}w)\Bigl(\frac{\log T}{|\omega|}+1\Bigr).$$
*Prueba.* La fase $\Omega(x)=\omega\tau_x/2\pi$ tiene $\Omega'=\omega/\log(\tau_x/2\pi)$, monótona, con $|\Omega'|\le\frac34+o(1)$; por tanto $\|\Omega'\|\ge\min(|\omega|/\log 3T,\frac15)$. Se aplica Kusmin–Landau (`thm:known_KL`, como en `lem:clock_equidistribution`) y sumación parcial. $\square$

Para $\omega=\log(a/b)$ con $a\ne b$ enteros $\le T^{\beta}$ se tiene $|\omega|\ge T^{-\beta}/2$, así que la media normalizada es $\ll(\|w\|+\operatorname{Var}w)\,T^{\beta-1}$.

**L2 (momentos en el reloj = momentos del modelo).** Sean $F,G$ polinomios trigonométricos con frecuencias $\log n$, $n\le T^{\beta}$, $\beta\le\frac38$, y sea $\|F\|_1$ la suma de los valores absolutos de sus coeficientes. Entonces $|\langle F(\tau_k)\overline{G(\tau_k)}\rangle-\mathbb E_{\rm mod}[F\bar G]|\ll\|F\|_1\|G\|_1T^{2\beta-1}$. *Prueba.* Se desarrolla en exponenciales: la diagonal coincide con $\mathbb E_{\rm mod}$ por factorización única, y lo demás se acota con L1. $\square$

**L3 (subgaussianidad del modelo).** Si $P=\sum_rf_r(\theta_r)$ con $f_r(\theta)=\sum_m\beta_{r^m}\sin(m\theta)$ y $|f_r|\le c_r:=\sum_m|\beta_{r^m}|$, Hoeffding da $\mathbb P(|P|>x)\le2e^{-x^2/2\sigma^2}$ con $\sigma^2=\sum_rc_r^2$, y de ahí $\mathbb E|P|^{2q}\le2\,q!\,(2\sigma^2)^q$. Además $\sigma^2(r\le R)=\frac1{\pi^2}\log\log R+O(1)$. $\square$

**L4 (sampleo en puntos de multiplicidad acotada).** Sea $f$ un polinomio trigonométrico con frecuencias $\le\log N$, $N^{8r}\le T$, y coeficientes $f_n$, y sean $\varrho_k$ puntos con $\int\tilde n^2\le\kappa\,\mathfrak b_TM$ (notación de `lem:sampling_rho`). Entonces
$$\|f(\varrho_k)\|_{4r,\mathcal I_T}\ll_r\kappa^{1/8r}\bigl(1+\mathfrak b_T\log N\bigr)\Bigl(\sum|f_n|^2\Bigr)^{1/2}.$$
*Prueba.* Es la prueba de `lem:sampling_rho` con $F=|f|^{4r}$ en lugar de $\mathcal M(\varphi S_X')^{4r}$. Solo cambia la entrada: $\int|f|^{8r}$ e $\int|f|^{8r-2}|f'|^2$ se acotan por Montgomery–Vaughan (`thm:known_MV`). **[Adaptación A1]**

**L5 (multiplicidad de los puntos desplazados).** Para $u\in[0,1]$ y $\Pi\in\{P_0+uP_1,\ uP_0\}$ (definidos en §4), los puntos $\tau_k-\Pi(\tau_k)/\Lambda(\tau_k)$ cumplen $\int\tilde n^2\ll\mathfrak b_TM$ uniformemente en $u$. *Prueba.* Es la prueba de `lem:multiplicity`, que solo usa (i) $\int|\Pi'|^2\ll T(c_1\log T)^2$ por Montgomery–Vaughan y (ii) $\langle\Pi(\tau_k)^4\rangle\ll(1+H_0)^2$. Las dos valen para $\Pi$ porque sus coeficientes están acotados por los de $S_{X_1}$. **[Adaptación A2]**

## 3. Paso A: reducción a la respuesta lineal

Identidades exactas: $\mathfrak t_X=\mathfrak t_Y+W(\gamma)-W(\tau)$ y $W(\gamma)=u_Y-u_X$. Datos de la v14:
- $\langle u_X^2\rangle=O_c(1)$ (`thm:main`);
- $\langle u_Y^2\rangle=\frac1{2\pi^2}\log\frac1{\theta_T}+O(1+\sqrt{H_1})=L+O(\sqrt L)$ (`thm:main` con $c=\theta_T$);
- $\langle\mathfrak t_Y^2\rangle\ll\theta_T^2\log\log T=2\pi^2\omega^2$ (`lem:transport`).

Ortogonalidad en el reloj (`prop:almost_orthogonal`, con $b=c\le\frac12$): $\langle W(\tau)^2\rangle=L+o(1)$ y $\langle S_Y(\tau)W(\tau)\rangle=o(1)$. **[Adaptación A3:** la proposición está enunciada para primos; las potencias $p^m$ ($m\ge2$) de $W$ tienen masa $\ell^2$ $\ll Y^{-1/2}$ y se tratan con la misma prueba o con el sampleo de Sobolev en los intervalos disjuntos $\mathcal U_k$.**]**

Desarrollando $\|\mathfrak t_Y+W(\gamma)-W(\tau)\|_2^2$ y usando Cauchy–Schwarz en los términos con $\mathfrak t_Y$ (que son $\ll\omega\sqrt L=o(L)$):
$$B_c=\langle W(\gamma)^2\rangle+\langle W(\tau)^2\rangle-2\langle W(\gamma)W(\tau)\rangle+o(L)=2L-2\langle s\,W(\tau)\rangle+o(L).$$
En el último paso se usa $W(\gamma)=s-S_Y(\gamma)-u_X$ y $S_Y(\gamma)=S_Y(\tau)+\mathfrak t_Y$. $\square$

## 4. Paso B: eliminación de los ceros

Por `prop:recursion` con $j=2$, $\Lambda(\rho_k)e_{2,k}=u_k(X_2)+S_{X_2}(\gamma_k)-S_{X_2}(\rho_k)+\chi_{2,k}=s_k-Q(\rho_k)+\chi_{2,k}$. El teorema `thm:second_step` da $\langle\Lambda(\rho)^2e_2^2\rangle=\frac{H_2}{4\pi^2}+O(1+\sqrt{H_2})$ y $\langle\chi_2^2\rangle\ll T^{-2}$. Por tanto
$$\langle s\,W(\tau)\rangle=\langle Q(\rho)\,W(\tau)\rangle+O\bigl((1+\sqrt{H_2})\sqrt L\bigr)=\langle Q(\rho)\,W(\tau)\rangle+o(L).$$
Desde aquí ya no intervienen los ceros. $\square$

## 5. Paso C: $\langle Q(\rho)W(\tau)\rangle=o(L)$

### 5.1 Truncaciones
- $Q\to Q^\flat$ (términos $p^m\le X_2^2$) y $W\to W^\flat$ ($p^m$ con $m\le2$): el error es uniforme $\ll1/\log X_2$, o $\ll Y^{-1/2}$ en $L^2$; contribuye $o(1)$.
- Los cuadrados de primos de $W$ llegan a frecuencias $\log X^2\le\log T$, que pueden caer en la banda estacionaria. Su norma $L^2$ en el reloj se acota por Sobolev en los $\mathcal U_k$ y Montgomery–Vaughan (longitud $\le T$) por $\ll\sum_{p>Y}p^{-2}$, así que su contribución es $o(1)$. Queda $W_{\rm pr}=\sum_{Y<p\le X}a_p\sin(t\log p)$, con frecuencias $\le\frac12\log T$.
- $S_{X_1}=P_0+P_1+P_2+E_1$:
  - $P_0$: $p\le Z$, $p^m\le Z^2$;
  - $P_1$: $Z<p\le X_1$, $p^m\le X_1^2$;
  - $P_2$: $p\le Z$, $Z^2<p^m\le X_1^2$, con masa $\ell^2$ $\ll Z^{-1}$;
  - $E_1$: los demás términos, $|E_1|\ll1/\log X_1$ uniformemente.

  Quitar $P_2+E_1$ del punto $\rho$ desplaza $\rho$ en $\ll(|P_2|+|E_1|)/\Lambda$. Por el valor medio, con el maximal de $Q'$ en radio $<\mathfrak b_T$ (Sobolev en los intervalos disjuntos $\mathcal U_k$) y con L2 para $\|P_2\|_4$, el coste es $\ll\frac{\sqrt{H_0}\log X_2}{\Lambda_0}\bigl(Z^{-1/2}+\frac1{\log X_1}\bigr)\to0$. **[Adaptación A4: la cuenta está esbozada aquí, no detallada.]**

  Queda $\rho^\flat_k=\tau_k-(P_0+P_1)(\tau_k)/\Lambda(\tau_k)$.

### 5.2 Desarrollo agregado
Sean $\xi_{n,k}=\log n/\Lambda(\tau_k)$, $e_J(z)=\sum_{j<J}z^j/j!$ y $R_J=e^z-e_J$. Para cada $n$, con $a=-i\xi P_0$ y $b=-i\xi P_1$,
$$e^{a+b}=e_{J_0}(a)\,e_{J_1}(b)+e^{a}R_{J_1}(b)+R_{J_0}(a)\,e_{J_1}(b)\qquad\text{(identidad exacta)}.$$
Con $R_J(z)=\frac{z^J}{(J-1)!}\int_0^1(1-u)^{J-1}e^{uz}du$ y sumando $\sum_n\beta_n\Im(n^{i\tau}\,\cdot)$:
$$Q^\flat(\rho^\flat)=\underbrace{\sum_{j<J_0,\,l<J_1}\frac{(-P_0)^j(-P_1)^l}{j!\,l!\,\Lambda^{j+l}}Q^{\flat(j+l)}(\tau)}_{\rm Main}+\mathrm{Rem}_{\rm I}+\mathrm{Rem}_{\rm II},$$
$$\mathrm{Rem}_{\rm I}=\frac{(-P_1)^{J_1}}{(J_1-1)!\Lambda^{J_1}}\int_0^1(1-u)^{J_1-1}Q^{\flat(J_1)}\Bigl(\tau-\frac{P_0+uP_1}{\Lambda}\Bigr)du,$$
$$\mathrm{Rem}_{\rm II}=\sum_{l<J_1}\frac{(-P_1)^l(-P_0)^{J_0}}{l!\,(J_0-1)!\Lambda^{l+J_0}}\int_0^1(1-u)^{J_0-1}Q^{\flat(l+J_0)}\Bigl(\tau-\frac{uP_0}{\Lambda}\Bigr)du.$$
Todo $P,\Lambda$ se evalúa en $\tau_k$. Esto es **agregado**: no aparece ninguna suma de $|\beta_n|$. El factor de varianza grande, $e^{-i\xi P_0}$, queda dentro del punto de evaluación de $\mathrm{Rem}_{\rm I}$ con módulo 1.

### 5.3 Los restos
Sean $\hat\xi=\log X_2^2/\min\Lambda=\frac{4\pi}{\sqrt{H_1}}(1+o(1))$ y $\tilde Q^{(m)}=Q^{\flat(m)}/(\log X_2^2)^m$, cuyos coeficientes son $\le|\beta_n|$ en valor absoluto.
- **$\mathrm{Rem}_{\rm I}$.** Por Jensen en $u$ y Hölder,
$$\|\mathrm{Rem}_{\rm I}\|_2\le\sup_u\Bigl\|\frac{(\hat\xi|P_1|)^{J_1}}{J_1!}\Bigr\|_4\,\bigl\|\tilde Q^{(J_1)}(\tau-(P_0+uP_1)/\Lambda)\bigr\|_4 .$$
  - El segundo factor es $\ll H_0^{1/2}$ por L4 y L5, con $\mathfrak b_T\log X_2^2\to0$.
  - El primero: por L2 y L3 con $q=2J_1$, $\sigma_1^2=\frac1{\pi^2}\cdot\frac32H_1+O(1)$ y $\hat\xi^2\sigma_1^2\le25$,
$$\Bigl\|\frac{(\hat\xi|P_1|)^{J_1}}{J_1!}\Bigr\|_4\le\frac{\bigl(2(2J_1)!\bigr)^{1/4}(2\hat\xi^2\sigma_1^2)^{J_1/2}}{J_1!}\le2\Bigl(\frac{100e^2}{J_1}\Bigr)^{J_1/2}.$$
    Para que L2 aplique hace falta longitud $(X_1^2)^{4J_1}\le T^{3/8}$, que se cumple.
  - Con $J_1=H_1$: $\|\mathrm{Rem}_{\rm I}\|_2\ll H_0^{1/2}(740/H_1)^{H_1/2}=H_0^{1/2-(\log H_1)/2+O(1)}\to0$.
- **$\mathrm{Rem}_{\rm II}$.** Con Hölder $L^6\times L^6\times L^6$:
  - $\sum_{l<J_1}\|(\hat\xi P_1)^l/l!\|_6=O(1)$;
  - $\|(\hat\xi|P_0|)^{J_0}/J_0!\|_6\le\frac{(2(3J_0)!)^{1/6}(2s)^{J_0/2}}{J_0!}\le2\bigl(6e^2s/J_0\bigr)^{J_0/2}$ con $s=\hat\xi^2\sigma_0^2\le\frac{16H_0}{H_1}(1+o(1))$; tomando $J_0=\lceil24e^2s\rceil\asymp H_0/H_1$ queda $\le2^{1-J_0}$. La longitud es $(Z^2)^{6J_0}=T^{12J_0/H_0^2}=T^{O(1/(H_0H_1))}$, válida;
  - $\|\tilde Q(\tau-uP_0/\Lambda)\|_6\ll H_0^{1/2}$.

  Por tanto $\|\mathrm{Rem}_{\rm II}\|_2\ll2^{-J_0}H_0^{1/2}\to0$.

En conjunto, $|\langle\mathrm{Rem}\,W(\tau)\rangle|\le\|\mathrm{Rem}\|_2\sqrt{L+o(1)}=o(1)$.

### 5.4 Término principal: frecuencias no nulas
Cada sumando de $\mathrm{Main}\cdot W_{\rm pr}$ es un polinomio trigonométrico en $\tau_k$ con peso $\Lambda(\tau_k)^{-(j+l)}$ (monótono y de variación pequeña). Sus frecuencias son $\log(a/b)$ con $ab\le(Z^2)^{J_0}(X_1^2)^{J_1}X_2^2T^{1/2}=T^{1/2+o(1)}$.
- La norma $\ell^1$ total es $\le T^{1/4+o(1)}$, porque cada suma truncada se acota por su término máximo: $(2Z\hat\xi)^{J_0}=T^{o(1)}$ y $(2X_1\hat\xi)^{J_1}=T^{H_1/\sqrt{H_0}}$.
- Por L1 con $\beta=\frac12+o(1)$, cada media es $\ll T^{-1/2+o(1)}$.

Contribución total: $T^{-1/4+o(1)}$.

### 5.5 Término principal: frecuencia nula (diagonal)
Los primos de $P_0,P_1$ son $\le X_1<Y<p$, y los de $W_{\rm pr}$ son $>Y$. Por factorización única, la frecuencia nula solo aparece si $n=p$ (primo de la banda con $p\le X_2$) y la parte de $P$ tiene exponente neto nulo. Esto da exactamente
$$\mathrm{Diag}=\sum_{Y<p\le X_2}\frac{a_p^2}2\Bigl\langle\Re\,\mathbb E_{\rm mod}\bigl[e_{J_0}(-i\xi_{p,k}P_0)\bigr]\,\mathbb E_{\rm mod}\bigl[e_{J_1}(-i\xi_{p,k}P_1)\bigr]\Bigr\rangle_k+T^{-1/4+o(1)} .$$
- $|\mathbb E\,e_J(z)-\mathbb E\,e^z|\le\mathbb E|z|^J/J!$, que es despreciable por §5.3.
- Para cada primo $r\le Z$ se tiene $|\xi f_r|<1$, y $|\mathbb Ee^{-i\xi f_r}|\le1-\frac{\xi^2}{4\pi^2r}+O(\xi^3r^{-3/2})$. Por tanto $|\mathbb E_{\rm mod}e^{-i\xi P_0}|\le\exp\bigl(-\frac{\xi^2}{4\pi^2}(H_0-2H_1+O(1))+O(\xi^3)\bigr)$.
- En la banda, $\xi_{p,k}\ge2\pi\theta_T(1+O(1/\log T))$, así que $\frac{\xi^2H_0}{4\pi^2}\ge2\pi^2\omega^2(1+o(1))$.

Luego $|\mathrm{Diag}|\le\frac1{2\pi^2}\sum_{Y<p\le X_2}\frac1p\,e^{-2\pi^2\omega^2(1+o(1))}+o(1)=o(L)$.

### 5.6 Conclusión
$\langle Q(\rho)W(\tau)\rangle=o(L)$. Por B, $\langle sW(\tau)\rangle=o(L)$, y por A, $B_c=2L+o(L)=\frac1{2\pi^2}H_1(1+o(1))$. Finalmente $|\sqrt{\langle r^2\rangle}-\sqrt{B_c}|\le\sqrt{\langle u_X^2\rangle}+\|\chi\|_2=O_c(1)$. $\blacksquare$

## 6. Auditoría de rigor

| Paso | Estado | Qué falta |
|---|---|---|
| Teoremas de la v14 usados: `thm:main`, `lem:transport`, `prop:recursion`, `thm:second_step`, `prop:almost_orthogonal`, `lem:multiplicity`, `lem:sampling_rho`, KL, MV | Se toman como demostrados | Revisión externa de la v14: 10 de 11 observaciones cerradas; constantes no explícitas, lo que basta para un enunciado asintótico |
| L1, L2, L3 | Demostrados aquí (estándar) | — |
| L4 (sampleo de $\lvert f\rvert^{4r}$) | **Adaptación A1** de `lem:sampling_rho` | Escribir la prueba con $F=\lvert f\rvert^{4r}$ y comprobar las condiciones de longitud ($N^{8r}\le T$) |
| L5 (multiplicidad de $\tau-\Pi/\Lambda$ uniforme en $u$) | **Adaptación A2** de `lem:multiplicity` | Rehacer la prueba con $\Pi$ en lugar de $S_{X_1}$; usa solo cotas de coeficientes, pero no está escrita |
| Paso A | Demostrado salvo A3 | **A3:** potencias de primos en la ortogonalidad del reloj (la proposición de la v14 es solo para primos) |
| Paso B | Demostrado (exacto, más `thm:second_step`) | — |
| §5.1 truncaciones | Esbozado | **A4:** escribir las cotas de los desplazamientos por $P_2$ y $E_1$ con el maximal de radio $<\mathfrak b_T$ |
| §5.2 identidad agregada | Demostrada (identidad exacta) | — |
| §5.3 restos | Demostrados con los parámetros indicados | Comprobar las constantes de Hoeffding con los términos $m\ge2$ (afectan solo a $O(1)$ en $\sigma^2$) |
| §5.4 frecuencias no nulas | Demostrado | — |
| §5.5 diagonal | Demostrado | — |
| Uniformidad en $c\in(0,\frac12]$ y caso $c=\frac12$ | Cubierto: frecuencias $\le\frac12\log T+o(\log T)$; cuadrados de $W$ por Sobolev | Revisar el borde $c=\frac12$ en `prop:almost_orthogonal` (banda estacionaria, $\ll(\log T)^{-1/4}$) |

**Lo no demostrado rigurosamente son las adaptaciones A1–A4.** Las cuatro rehacen pruebas ya existentes en la v14 con otros polinomios. No introducen ninguna estimación nueva y no veo en ellas riesgo de fallo, pero no están escritas línea a línea. Todo lo demás está demostrado aquí o es un enunciado de la v14.

**Novedad.** No he hecho búsqueda bibliográfica. El enunciado trata objetos propios de la v14, así que es nuevo en ese sentido. La técnica de §5.2–5.3 (truncar la exponencial y controlar el resto con momentos) es de tipo Radziwiłł–Soundararajan.

**Atribución.**
- Reducción (A), universalidad y cota superior: textos 05–07 de ChatGPT.
- Uso del segundo paso para eliminar los ceros: texto de ChatGPT del 2026-10-23 (`…/f9d61fc3`).
- Fórmula con la respuesta $\mathcal R^\tau_p$, partición $P_0/P_1$ con el orden (I)/(II), forma agregada con resto integral, sampleo en puntos desplazados (sin máximos de radio aleatorio), diagonal y auditoría: Claude.
