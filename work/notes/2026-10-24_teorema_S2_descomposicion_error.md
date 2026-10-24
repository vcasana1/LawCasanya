# Teorema S2: descomposición exacta del error de cualquier reloj sin ceros, y el suelo con corte variable

Nota de Claude, 24-oct-2026. Sustituye a §2 de `2026-10-24_respuesta_transporte_y_suelo.md`. **Se retira la comparación con el corte fijo 512**, que no corresponde al método (cortes variables por índice). Sin ejecuciones numéricas; solo cuadraturas de constantes. Ningún manuscrito cambiado.

**Fuentes.** [v14] `manuscript/ordinal_prime_cutoff_v14.tex`:
- Prop. `almost_orthogonal`: $\|G-I\|_{\rm op}\ll_b(\log T)^{-1/4}+T^{b-1}\log T$ para primos $p\le T^b$, $b<1$;
- Prop. `spectral_energy`;
- Thm `computable_response` (11.14)(ii): $\mathcal D^{(m)}_p=\mathbf 1_{p\le X_m}+o(1)$;
- Thm `variable_cutoff`: $X_k=(\tau_k/2\pi)^c$;
- Thm `projection`.

## Notación

- $M=\#\mathcal I_T$, $\langle\cdot\rangle$ la media sobre $\mathcal I_T$.
- Para prime powers $n\le T^b$: $v_n(k)=\sqrt{2/M}\,\sin(\tau_k\log n)$ y $V_b=\mathrm{span}\{v_n\}$.
- $P_b$ es la proyección ortogonal sobre $V_b$.
- Construcción sin ceros $x_k$, con corrección $y_k=\Lambda(\tau_k)(\tau_k-x_k)$ y error $r_k=\Lambda(\tau_k)(x_k-\gamma_k)$, de modo que $s_k=y_k+r_k+O(1/T)$.
- Respuestas
$$R^\tau_n=\frac2{a_n}\langle s_k\sin(\tau_k\log n)\rangle,\qquad \mathcal A_n=\frac2{a_n}\langle y_k\sin(\tau_k\log n)\rangle\ \ (\text{computable}),\qquad a_{p^m}=-\frac1{\pi mp^{m/2}}.$$

## Teorema S2 (T, incondicional)

Para todo $b<1$ y toda construcción $x_k$ calculada con el reloj y los primos:

$$\langle r_k^2\rangle=\bigl(1+O_b((\log T)^{-1/4})\bigr)\sum_{n\le T^b}\frac{a_n^2}2\,\bigl|R^\tau_n-\mathcal A_n\bigr|^2\;+\;\Omega_b[x], \tag{S2}$$

con

$$\Omega_b[x]=\frac1M\bigl\|(I-P_b)\,r\bigr\|^2\ \ge0 .$$

Si la corrección es lineal en las fases ($y\in V_b$), entonces $(I-P_b)r=(I-P_b)s$ y

$$\Omega_b[x]=\Omega_b[s]:=\frac1M\|(I-P_b)s\|^2,$$

**que no depende de la construcción**.

*Prueba.* Por Pitágoras, $\|r\|^2=\|P_br\|^2+\|(I-P_b)r\|^2$. Sea $w_n=\langle r,v_n\rangle_{\mathbb R^M}=\sqrt{2M}\,\langle r_k\sin(\tau_k\log n)\rangle$. Por las definiciones, $w_n=\sqrt{2M}\,\tfrac{a_n}2(R^\tau_n-\mathcal A_n)$. Para una familia con Gram $G$, $\|P_br\|^2=w^{\mathsf T}G^{-1}w$, y

$$w^{\mathsf T}G^{-1}w=\bigl(1+O(\|G-I\|_{\rm op})\bigr)\|w\|^2 .$$

Por Prop. `almost_orthogonal` de v14, $\|G-I\|_{\rm op}\ll_b(\log T)^{-1/4}$. Se divide por $M$. $\square$

*Estado:* v14 demuestra la Prop. `almost_orthogonal` para **primos**. Su extensión a las potencias de primo $p^m$, $m\ge2$, sigue la misma prueba (cocientes por Kusmin–Landau, productos en la banda estacionaria contados por su escasez), pero está **sin escribir línea a línea**. Las potencias hay que incluirlas: su contenido $\frac1{2\pi^2}\sum_{p,m\ge2}\frac1{m^2p^m}\approx0.006$ no es despreciable.

## Corolario S2′: corte variable $X_k=(\tau_k/2\pi)^c$, un paso, $0<c<1$

(i) **Respuesta computable.** $\mathcal A_n=\mathbf 1_{n\le X}+o(1)$ uniformemente para $n\le T^b$ con $nX\le T^{1-\varepsilon}$. Es el Thm 11.14(ii) de v14; con $X_k$ variable en la ventana diádica, $X_-\le X_k\le X_+\le2X_-$, el borde $(X_-,X_+]$ tiene masa armónica $O(1/\log T)$, como en la prueba del Thm `variable_cutoff`. Para $c<\tfrac12$ y $n\le T^{1-c-\varepsilon}$ vale tal cual. Para $c\ge\tfrac12$ aparecen resonancias de pares $nX\approx T$, de masa $O(1/\log T)$ por el Teorema C1.

(ii) **(T) bajo la ley en el reloj.** Supongamos (H1): $R^\tau_p=1-\Phi(\theta_p)+o(1)$ uniformemente en compactos de $(0,1)$. Por Mertens y suma parcial, con $\theta\to0$ cubierto por el Thm `projection` ($R\to1$, $\Phi\to0$),

$$\boxed{\ \langle r_k^2\rangle=\frac1{2\pi^2}\Bigl[\int_0^{c}\frac{\Phi(\theta)^2}{\theta}\,d\theta+\int_{c}^{1}\frac{(1-\Phi(\theta))^2}{\theta}\,d\theta\Bigr]+\Omega_{1^-}[s]+o(1),\ } \tag{S2'}$$

con $\Omega_{1^-}[s]:=\lim_{b\uparrow1}\limsup_T\Omega_b[s]\ge0$, universal. Las potencias de primo tienen $R^\tau_n\to1$ ($n$ fijo) y $\mathcal A_n=1$, y no aportan nada al primer sumando.

(iii) **Corte óptimo y pesos óptimos.**
- Con peso 1 sobre $p\le X$, la derivada del corchete respecto de $c$ es $\bigl(\Phi(c)^2-(1-\Phi(c))^2\bigr)/c=(2\Phi(c)-1)/c$. Como $\Phi'(\theta)=\log\frac{1+\theta}{1-\theta}>0$, $\Phi$ es creciente: la derivada es negativa antes de $c^*$ y positiva después, así que $c^*$ es un **mínimo**. Se anula en $\Phi(c)=\tfrac12$, es decir $c^*=0.6758$. **Usar primos más allá de $\theta=0.676$ con peso 1 empeora el error.** Corrige el valor $0.58$ dado en `2026-10-24_empuje_sin_RH_tauC.md` §3.
- Con pesos $\lambda_p=1-\Phi(\theta_p)$ sobre todo $p\le T^{1-\varepsilon}$ (filtro de Wiener), el primer sumando de (S2) desaparece y queda

$$\langle r_k^2\rangle=\Omega_{1^-}[s]+o(1):$$

el mínimo absoluto de toda corrección lineal, independiente de cortes.

Valores del corchete (cuadratura):

| $c$ | $\frac1{2\pi^2}[\cdots]$ |
|---|---|
| 0.25 | 0.0341 |
| 0.50 | 0.0087 |
| 0.58 | 0.0058 |
| $c^*=0.676$ (mínimo con peso 1) | 0.0047 |
| 1 (peso 1) | 0.0178 |
| todo $p\le T^{1-\varepsilon}$ con pesos de Wiener | 0 |

(iv) **Multietapa (no lineal).** (S2) vale igual con $\mathcal A_n=\mathcal D_n+\mathcal B_n$. Ahí $\Omega_b[x]\ne\Omega_b[s]$: el transporte no lineal puede bajar la parte ortogonal. **Es el único mecanismo por el que una construcción sin ceros puede bajar de $\Omega_{1^-}[s]$.**

## Qué queda abierto

1. (H1), la ley en el reloj, para (S2′). Ver la nota de la ley.
2. **El valor de $\Omega_{1^-}[s]$**: el contenido de $s_k$ ortogonal a todas las fases primas $\le T$. Bajo tu objetivo, error $\to0$, tiene que ser $0$ o recuperable por la no linealidad (iv).
3. **Contraste sin cortes arbitrarios**: tus construcciones con continuación hasta $(\tau/2\pi)^c$, $c=1,1.15,1.30$ (AGENTS §5), comparadas con (S2′) a ese $c$. Ese es el contraste pertinente; **no** zCasanya.

---

## Addenda (24-oct, tras la revisión de ChatGPT relayada por el autor)

**A0. Precisiones aceptadas.**
- La estimación relativa $w^{\mathsf T}G^{-1}w=(1+O(\varepsilon))\|w\|^2$ no necesita que $\|w\|^2/M$ esté acotado. Retiro esa frase de la respuesta del chat.
- La casi ortogonalidad para potencias de primo $p^m\le T^b$ sigue pendiente de escribir. Es el único hueco del error relativo de S2.

**A1. Defecto exacto $\chi_k$.** Por v14 (l. 1158–1159), $s_k=\Lambda(\tau_k)\delta_k-\chi_k$ con

$$\chi_k=\frac{\gamma_k}{2\pi}\Bigl(\frac{\tau_k}{\gamma_k}-1-\log\frac{\tau_k}{\gamma_k}\Bigr),\qquad 0\le\chi_k\le\frac{\delta_k^2}{4\pi\min(\gamma_k,\tau_k)}\ll\frac1T$$

($\delta_k$ acotado). Entonces $r=s-y+\chi$ **exactamente**, y en (S2) hay que poner $R^\tau_n-\mathcal A_n+R^\chi_n$, con $R^\chi_n=\frac2{a_n}\langle\chi_k\sin(\tau_k\log n)\rangle$ y $|R^\chi_n|\ll m\sqrt n/T$. Su contribución a la suma es

$$\sum_{n\le T^b}\frac{a_n^2}2|R^\chi_n|^2\ll\sum_{n\le T^b}\frac{1}{T^2}\ll T^{b-2},$$

y a $\Omega$, $\langle\chi^2\rangle\ll T^{-2}$. La identidad exacta queda corregida y el enunciado asintótico no cambia.

**A2. Lema Ω (independencia de $\Omega$ para corte dependiente del índice).** Sean un paso, $X_k=(\tau_k/2\pi)^{c(\tau_k)}$ con $c\le c_0<b<1$ (ley A, $c$ fijo, o ley B, $c(\tau)=(\log\log\tau)^{-1/2}$), y $y_k=S_{X_k}(\tau_k)$. Entonces

$$\Omega_b[x]=\Omega_b[s]+O\Bigl(\sqrt{\Omega_b[s]\,\varepsilon_T}+\varepsilon_T\Bigr),\qquad \varepsilon_T\ll\frac1{\log T}+T^{c_0-1}\log T,$$

y como $\Omega_b[s]\le\langle s_k^2\rangle\ll\log\log T$,

$$\Omega_b[x]=\Omega_b[s]+O\Bigl(\sqrt{\tfrac{\log\log T}{\log T}}\Bigr)\to0 .$$

*Prueba.*
1. Sean $X_\pm$ los valores extremos del corte en la ventana, como en la prueba del Thm `variable_cutoff`. Se tiene $X_+/X_-\le2^{c}(1+o(1))$ con $c$ fijo, y lo mismo con $c(\tau)$ lento.
2. Se separa $y=y^-+y^{\rm e}$, con $y^-_k=S_{X_-}(\tau_k)$, que está en $V_b$, y el **borde**
$$y^{\rm e}_k=\sum_{X_-<n\le X_k}a_n\sin(\tau_k\log n).$$
Entonces $(I-P_b)r=(I-P_b)s-(I-P_b)y^{\rm e}+(I-P_b)\chi$, y por la desigualdad triangular
$$\bigl|\sqrt{\Omega_b[x]}-\sqrt{\Omega_b[s]}\bigr|\le\langle(y^{\rm e})^2\rangle^{1/2}+\langle\chi^2\rangle^{1/2}.$$
3. *Cota de $\langle(y^{\rm e})^2\rangle$.* Como $X_k$ es creciente en $k$, $\mathbf 1[n\le X_k]=\mathbf 1[k\ge k_n]$ para un índice $k_n$. Así

$$\langle(y^{\rm e})^2\rangle=\frac1M\sum_{X_-<n,n'\le X_+}a_na_{n'}\sum_{k\ge\max(k_n,k_{n'})}\sin(\tau_k\log n)\sin(\tau_k\log n') .$$

La suma interior recorre un **intervalo de índices consecutivos**. Kusmin–Landau y van der Corput valen sobre cualquier intervalo de índices consecutivos con la misma cota, así que la prueba de la Prop. `almost_orthogonal` de v14 se aplica término a término:
- *diagonal:* $\le\frac1{2\pi^2}\sum_{X_-<p\le X_+}\frac1p=\frac{V_\pm}{2\pi^2}\ll\frac1{\log T}$ (Mertens: $V_\pm=\log\frac{\log X_+}{\log X_-}+O(\frac1{\log X_-})$);
- *cocientes* $n\ne n'$: $\ll T^{c_0-1}\log T$;
- *productos* $nn'$: con $c_0<\tfrac12$ caen fuera de la banda estacionaria, $\ll T^{-1}$. Con $\tfrac12<c<1$, $nn'\asymp T^{2c}$ tiene $\log(nn')/\log(\tau/2\pi)\to2c\in(1,2)$, a distancia fija de los enteros, y Kusmin–Landau da $O(1)$ por par. En el caso límite $2c\to1$, la banda estacionaria contiene $\ll T/\sqrt{\log T}$ pares (conteo de la Prop. `almost_orthogonal`), restringidos aquí al borde, cuya masa armónica es $O(1/\log T)$;
- *potencias* $p^m$, $m\ge2$, en el borde: $\sum a_n^2\ll X_-^{-1}$.

Por tanto $\varepsilon_T:=\langle(y^{\rm e})^2\rangle+\langle\chi^2\rangle\ll1/\log T+T^{c_0-1}\log T$. Elevando al cuadrado la desigualdad del paso 2 se obtiene el enunciado. $\square$

*Estado:* el caso $c$ cerca de $\tfrac12$, con el conteo de pares del borde en la banda, está **esbozado**. El resto usa enunciados de v14 sobre intervalos de índices, que valen tal cual.

**A3. Consecuencia.** Para el reloj de un paso con corte dependiente del índice (leyes A y B), $\Omega_b[x]$ es, salvo $o(1)$, la cantidad universal $\Omega_b[s]$. (S2′) vale con $\Omega_{1^-}[s]$ universal. Para la multietapa no lineal, $\Omega_b[x]\ne\Omega_b[s]$ en general: ahí puede bajar, y es el mecanismo de §(iv).

---

## Addenda B (24-oct): los dos puntos que quedaban

### B1. Independencia de $\Omega$ para un corte general: qué regularidad hace falta y por qué

**Teorema B1.** Sea un paso con corte $k\mapsto X_k\in[X_-,X_+]\subset[2,T^{c_0}]$, $c_0<b<1$, tal que en la ventana $\mathcal I_T$:
- **(R1)** $k\mapsto X_k$ es monótona a trozos con $J=J(T)$ trozos;
- **(R2)** $V_\pm=\sum_{X_-<p\le X_+}1/p\to0$, equivalentemente $\log X_+/\log X_-\to1$.

Entonces

$$\bigl|\sqrt{\Omega_b[x]}-\sqrt{\Omega_b[s]}\bigr|^2\ \ll\ \varepsilon_T:=V_\pm+J\Bigl(T^{c_0-1}\log T+\frac{X_+}{\sqrt T\log^2T}\Bigr)+T^{-2}.$$

En particular $\Omega_b[x]=\Omega_b[s]+o(1)$ si $\varepsilon_T\log\log T\to0$.

*Prueba.* Es la del Lema Ω, sin maximal y sin Carleson–Hunt. En cada trozo monótono, $\mathbf 1[n\le X_k]$ es el indicador de un **intervalo de índices consecutivos**, y las cotas de Kusmin–Landau (cocientes, $\ll1/(T|\log(n/n')|)$) y de van der Corput (productos en la banda estacionaria, $|\sum_{k\in J}e^{i\tau_k\log n}|\ll\sqrt T\log T$) **no dependen de la longitud del intervalo**. Término a término en $\langle(y^{\rm e})^2\rangle$:
- **diagonal:** $\le V_\pm/2\pi^2$. Las fracciones de ventana suman $\le1$, así que no se multiplica por $J$;
- **cocientes:** $\le J\cdot T^{c_0-1}\log T$;
- **productos:** fuera de la banda, $O(J/T)$. Dentro de la banda (solo si $2c\approx1$), con cota $\ell^1$:
$$J\Bigl(\sum_{X_-<n\le X_+}|a_n|\Bigr)^2T^{-1/2}\ll J\,\frac{X_+}{\sqrt T\log^2X_+}.$$

El borde es corto, porque $\sum_{\rm borde}|a_n|\ll\sqrt{X_+}/\log X_+$. Por eso el caso $c=\tfrac12$ **no necesita** estimación maximal: con $X_+\asymp\sqrt T$ este término es $\ll J/\log^2T$. Las potencias $p^m$, $m\ge2$, del borde aportan $\ll X_-^{-1}$, y $\chi$ aporta $T^{-2}$ (Addenda A1). $\square$

**Leyes A y B.** $J=1$ (monótonas), y $V_\pm\ll1/\log T$:
- ley A: $\log X_+/\log X_-=1+O(1/\log T)$;
- ley B: $c(\tau)\log(\tau/2\pi)$ varía en $c\log2+O(1/\log\log T)$ en la ventana.

Así $\varepsilon_T\ll1/\log T$ para todo $c\le c_0<1$, **incluido $c=\tfrac12$**, y se recupera

$$|\Omega_b[x]-\Omega_b[s]|\ll\sqrt{\frac{\log\log T}{\log T}} .$$

Sobre la objeción relayada de ChatGPT de que "la casi ortogonalidad término a término no basta para un corte variable": sí basta, porque las cotas se aplican a **sumas sobre intervalos de índices** y el corte monótono solo trunca esos intervalos. La ruta maximal de Carleson–Hunt que propone es otra prueba posible. Pero aplicar Carleson–Hunt a frecuencias $\log p$ no armónicas exige una transferencia que no veo justificada en su texto; la prueba de arriba no la necesita.

**Las condiciones son necesarias (contraejemplo).** Sea $X_k=T^{c_1}$ para $k$ par y $X_k=T^{c_2}$ para $k$ impar, $c_1<c_2<b$. Entonces $J\asymp M$ y $V_\pm\to\log(c_2/c_1)\ne0$, y

$$y^{\rm e}_k=\tfrac12\bigl(1-(-1)^k\bigr)\sum_{T^{c_1}<n\le T^{c_2}}a_n\sin(\tau_k\log n).$$

El factor $(-1)^k=e^{i\pi k}$ desplaza cada frecuencia $\log n$ en $\pm\pi\cdot2\pi\Lambda=\pm\tfrac12\log(\tau/2\pi)$ (aliasing en el reloj). La mitad de la energía del borde sale de $V_b$:

$$\Omega_b[x]-\Omega_b[s]\to\frac1{4\pi^2}\Bigl(\log\frac{c_2}{c_1}\Bigr)\ne0$$

(salvo la correlación con $(I-P_b)s$, que no cancela de forma genérica; *sin escribir con detalle*). Sin (R1)–(R2), $\Omega$ depende de la construcción.

### B2. S2′: la hipótesis exacta y la uniformidad al sumar sobre primos

H1 "en compactos de $(0,1)$" **no basta**. Falta el tramo $(\log T)^{2-\varepsilon}<p<T^{a}$ ($\theta\to0$), y un $o(1)$ no cuantificado multiplicado por la masa armónica $\log\log T$ no tiende a 0. La hipótesis correcta y mínima es la forma $L^2(dn/n)$:

$$\textbf{(H1}_{L^2}\textbf{)}\qquad \sum_{(\log T)^{2-\varepsilon}<n\le T^b}a_n^2\,\bigl|R^\tau_n-(1-\Phi(\theta_n))\bigr|^2\longrightarrow0,\qquad \theta_n=\frac{\log n}{\log(T/2\pi)},$$

sobre potencias de primo $n$. Para $m\ge2$ el peso $a_n^2=1/(\pi^2m^2n)$ es sumable, así que basta con que $R^\tau_{p^m}$ esté acotado ahí.

**Teorema B2.** Para las leyes A y B con exponente $c\le c_0<b<1$ (en la ley B, $c\to0$ y el primer integrando desaparece), bajo (H1$_{L^2}$):

$$\boxed{\ \langle r_k^2\rangle=\Omega_b[s]+\frac1{2\pi^2}\Bigl[\int_0^{c}\frac{\Phi(\theta)^2}{\theta}\,d\theta+\int_{c}^{b}\frac{(1-\Phi(\theta))^2}{\theta}\,d\theta\Bigr]+o(1)\ }$$

para **cada** $b$ fijo. Los primos de $(T^b,T]$ quedan dentro de $\Omega_b[s]$, de modo que **no hace falta el límite $b\uparrow1$**.

*Prueba.*
1. S2 con Addenda A1 y Lema Ω/B1: $\langle r^2\rangle=(1+o(1))\Sigma+\Omega_b[s]+o(1)$, con

$$\Sigma=\sum_{n\le T^b}\frac{a_n^2}2|R^\tau_n-\mathcal A_n|^2,\qquad \mathcal A_n=\mathbf 1_{n\le X_k}+o(1)$$

(Thm 11.14(ii) de v14, con la variación del corte en la ventana absorbida por B1).

2. Se parte $\Sigma$ en tres tramos.
   - (a) $n\le(\log T)^{2-\varepsilon}$: Thm `projection` de v14 da $R^\tau_n=1+O\bigl(\frac{\sqrt n\log n\log\log T}{\log T}\bigr)$. Como $\mathcal A_n=1$, el aporte es
   $$\ll\frac{(\log\log T)^2}{\log^2T}\sum_{n\le Y_0}\log^2n\ll(\log T)^{-\varepsilon}(\log\log T)^3\to0 .$$
   - (b) $(\log T)^{2-\varepsilon}<n\le T^b$: se escribe $R^\tau_n-\mathcal A_n=(1-\Phi(\theta_n)-\mathcal A_n)+\epsilon_n$. Por Cauchy–Schwarz,
   $$\Sigma_b=\sum\frac{a_n^2}2(1-\Phi-\mathcal A)^2+O\Bigl(\bigl(\textstyle\sum a_n^2\epsilon_n^2\bigr)^{1/2}\bigl(\sum a_n^2(1-\Phi-\mathcal A)^2\bigr)^{1/2}+\sum a_n^2\epsilon_n^2\Bigr).$$
   La primera suma está acotada: $(1-\Phi-\mathcal A)^2$ es $\Phi^2=O(\theta^4)$ si $n\le X$ y $(1-\Phi)^2\le1$ si $n>X$, sobre masa $\log(b/c)$. Por (H1$_{L^2}$), el error tiende a 0.
   - (c) Mertens y suma parcial (como en Prop. `spectral_energy`(d) de v14): para $F$ continua a trozos en $[0,b]$ con $F(\theta)=O(\theta^2)$ en 0,
   $$\sum_{p\le T^b}\frac{F(\theta_p)}p\to\int_0^bF(\theta)\frac{d\theta}\theta .$$
   La variación $\theta_p$ entre $\log(T/2\pi)$ y $\log(\tau_k/2\pi)$ en la ventana es $O(1/\log T)$. Las potencias $m\ge2$ aportan $o(1)$ porque su masa por encima de $Y_0$ es $\ll Y_0^{-1/2}$. $\square$

**B3. Comprobación y equivalencia parcial.** Por B2, la diferencia $\langle r^2\rangle(c)-\langle r^2\rangle(c')$ entre dos cortes $c<c'$ no depende de $\Omega$:

$$\langle r^2\rangle(c')-\langle r^2\rangle(c)=\frac1{2\pi^2}\int_c^{c'}\frac{2\Phi(\theta)-1}{\theta}\,d\theta+o(1).$$

Recíprocamente, sin H1, esa diferencia es exactamente

$$\frac1{2\pi^2}\sum_{T^c<p\le T^{c'}}\frac{1-2\,\Re R^\tau_p}p+o(1)$$

(S2 con Lema Ω). **Las diferencias de error entre cortes miden las medias armónicas por bandas de $\Re R^\tau_p$**, sin hipótesis y sin $\Omega$. Es un contraste de la ley que solo usa tus construcciones de corte variable, con dos o más valores de $c$, y en el que $\Omega$ se cancela.
