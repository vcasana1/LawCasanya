# Distancia $\tau_k-\gamma_k$: revisión de los teoremas y consecuencias del teorema de la energía del transporte (2026-10-24)

Referencias: [I] = manuscript/ordinal_prime_cutoff_v14.tex; [T5] = work/paper1/transport_theorem/transport_energy_theorem_v5.tex (numeración de lemas de la v5). Notación de [T5]: $H_0=\log\log T$, $H_1=\log H_0$, $H_2=\log H_1$, $L=\frac1{2\pi^2}\log\frac c{\theta_T}$, $W=S_{T^c}-S_Y$, $Q=S_{X_2}$, $\rho_k=x^{(1)}_k$. Respuestas de [I], (11.x): $\mathcal R^\tau_p=\frac2{a_p}\langle s_k\sin(\tau_k\log p)\rangle$, $\mathcal B^{(m)}_p=\frac2{a_p}\langle B^{(m)}_k\sin(\tau_k\log p)\rangle$, $B^{(m)}_k=S_{X_m}(x^{(m-1)}_k)-S_{X_m}(\tau_k)$, con $\frac2{a_p}=-2\pi\sqrt p$. Para una banda de primos $\mathcal J$, $\mu(\mathcal J)=\sum_{p\in\mathcal J}\frac1p$ y $W_{\mathcal J}=\sum_{p\in\mathcal J}a_p\sin(t\log p)$. Identidad básica: $\langle F_kW_{\mathcal J}(\tau_k)\rangle=\frac1{2\pi^2}\sum_{p\in\mathcal J}\frac{\mathcal F_p}p$ cuando $\mathcal F_p=\frac2{a_p}\langle F_k\sin(\tau_k\log p)\rangle$ (porque $a_p^2/2=1/(2\pi^2p)$).

## 1. Catálogo de lo que había sobre $\tau_k-\gamma_k$

| Resultado | Dónde | Tipo |
|---|---|---|
| $\limsup|\delta_k|\le0.6331$ (Bellotti–Wong) | [I] Thm 3.2 | puntual, conocido |
| $\langle\delta_k^2\rangle\sim2\log\log T/\log^2T$, $\langle s_k^2\rangle\sim\frac{H_0}{2\pi^2}$ | [I] (3.3), Selberg–Korolev | media cuadrática, conocido |
| Teorema B: $\langle u_k(T^c)^2\rangle=\frac1{2\pi^2}\log\frac1c+O(1+\sqrt{\log(1/c)})$ | [I] Thm 5.1 | nuevo en [I] |
| Teorema D: $\langle r_k(T^c)^2\rangle=\frac1{2\pi^2}\log\frac1c+O((1+\sqrt{\log(1/c)})(1+c^2H_0))$; con $c=H_0^{-1/2}$, $\langle(\tau^X_k-\gamma_k)^2\rangle=(H_1+O(\sqrt{H_1}))/\log^2T$ | [I] Thm 7.3, Cor 7.4–7.5 | nuevo en [I] |
| Segundo paso: $\langle\Lambda^2e_2^2\rangle=\frac{H_2}{4\pi^2}+O(1+\sqrt{H_2})$; $m^*$ pasos: $O(1)$ | [I] Thm 8.5, 8.10 | nuevo en [I] |
| Teorema E: $\limsup|\tau_k-\gamma_k|<0.60832$ | [I] Thm 9.3 | puntual |
| $\mathcal R^\tau_p\to1$ para $p\le(\log T)^{2-\varepsilon}$ | [I] Thm 11.3 | por primo |
| $\mathcal R^\tau_p=\mathcal B^{(m)}_p+\mathcal E^{(m)}_p+o(1)$ (primos móviles); $\sum_{p\le T^b}|\mathcal B^{(2)}_p|^2/p\ll H_0/H_1$ | [I] Thm 11.14 | descomposición sin ley |
| Transporte del reloj de un paso con $c$ fijo | [T5] Thm 1.1 | $B_c=\frac{H_1}{2\pi^2}+O_c(H_1^{5/8})$ |

Abiertos declarados en [I] §13 y en la nota del 23-10: q:fixed_c (resuelta por [T5]), $\limsup\overline{\mathcal R}_c\le\frac12$ (abierto en la nota del 23-10, §8), ley de diferencias en media (§3.1, sin verificar), $c>\frac12$, control casi para todo $k$, ley de $\mathcal R^\tau_p$ a $\theta$ fijo, Hipótesis 11.15–11.16.

## 2. Resultados que ahora salen demostrados

Todas las pruebas usan solo [I] (I1)–(I5) de [T5] y los lemas de [T5]. Observación usada varias veces (**uniformidad en la banda**): en los Lemas 7.1, 7.3, 7.4 de [T5] el polinomio $W_{\rm pr}$ solo interviene por $\|W_{\rm pr}(\tau)\|_2$, por $\|W_{\rm pr}\|_1\le2\sqrt X$ y por su soporte en primos $>X_1$; y en el Lema 7.5 solo por su soporte. Por tanto, para toda banda $\mathcal J\subset(X_1,T^{1/2}]$ (que puede depender de $T$), con $\|W_{\mathcal J}(\tau)\|_2^2=\frac{\mu(\mathcal J)}{2\pi^2}(1+O(\frac1{\log T}))$ (Lema 4.3, $b=\frac12$):
$$\langle Q(\rho_k)W_{\mathcal J}(\tau_k)\rangle=\sum_{p\in\mathcal J,\ p\le X_2}\frac{a_p^2}2\Phi^\sharp_T(p)+o\bigl(1+\sqrt{\mu(\mathcal J)}\bigr),\tag{2.1}$$
$$\Phi^\sharp_T(p)=\Bigl\langle\Re\,\mathbb E_{\rm mod}\bigl[e_{J_0}(-i\xi_{p,k}P_0)\bigr]\mathbb E_{\rm mod}\bigl[e_{J_1}(-i\xi_{p,k}P_1)\bigr]\Bigr\rangle_k .$$
Los errores son: Lema 7.1 (i) $\ll\sqrt\mu/\log X_2$, (iii) $\ll\frac{H_0}{\sqrt{H_1}\log T}\sqrt\mu$; Lema 7.3: $\ll(H_0^{1/2-(\log H_1)/2+O(1)}+2^{-J_0}H_0^{1/2})\sqrt\mu$; Lema 7.4: $\ll T^{-1/4+o(1)}$ (altura $\le T^{1/2+\eta_T}$, $\|W_{\mathcal J}\|_1\le2T^{1/4}$). La fórmula de la diagonal (Lema 7.5) solo usa que los primos de $\mathcal J$ son $>X_1$, es decir, que no aparecen en $P_0,P_1$.

Además, por el Lema 7.5 y la cota de su prueba, $|\Phi^\sharp_T(p)|\le2|\mathbb E e^{-i\xi P_0}|+2^{2-J_0}$ y
$$\Phi^\sharp_T(p)=\Phi_T(p)+O\bigl(2^{-J_0}+(50e/J_1)^{J_1/2}\bigr),\qquad \Phi_T(p)=\bigl\langle\mathbb E_{\rm mod}e^{-i\xi_{p,k}(P_0+P_1)}\bigr\rangle_k .\tag{2.2}$$

### R1. Error mejorado en el teorema del transporte
**Enunciado.** Para $c\in(0,\frac12]$ fijo,
$$B_c(T)=\frac1{2\pi^2}\log\log\log T+O_c\Bigl(\sqrt{\log\log\log T\cdot\log\log\log\log T}\Bigr),$$
y lo mismo para $\langle r_k(T^c)^2\rangle$.

**Prueba.** En [T5] sustituir $\omega=(\log V)^{1/8}$ por $\omega^2=\frac1{\pi^2}\log\log V$. Se mantienen $\theta_T\sqrt{H_0}=\pi\sqrt2\,\omega\to\infty$ y $\theta_T^2H_1=2\omega^2H_1/H_0\to0$, luego $Z<X_1<Y<X_2<X$. Proposición 5.1: error $O(\omega\sqrt L+\omega^2+\sqrt L)=O(\sqrt{H_1H_2})$. Proposición 6.1: $O(\sqrt{H_1H_2})$. Proposición 7.6: $O(Le^{-2\pi^2\omega^2(1+o(1))})+o(1)=O((\log V)^{-1+o(1)})+o(1)=o(1)$. Y $2L=\frac1{\pi^2}(\frac12\log V-\log\omega+\log c)=\frac{H_1}{2\pi^2}+O_c(1+\log H_2)$. Para $r_k$: $|\|r\|_2-\|\mathfrak t\|_2|=O_c(1)$. $\square$

### R2. Rango uniforme en $c$
**Enunciado.** Si $c=c(T)\le\frac12$ y $\log(1/c)=o(\log\log\log T)$ (por ejemplo $c=1/\log\log\log T$), entonces $B_c(T)\sim\langle r_k(T^c)^2\rangle\sim\frac1{2\pi^2}\log\log\log T$.

**Prueba.** (I1) es uniforme en $2\le X\le T^{1/2}$ con constantes absolutas, así que $\langle u(X)^2\rangle=\frac{\log(1/c)}{2\pi^2}+O(1+\sqrt{\log(1/c)})=o(H_1)$. En la Proposición 5.1: $\langle U^2\rangle=\langle u(Y)^2\rangle+O(\sqrt{H_1\langle u(X)^2\rangle}+\langle u(X)^2\rangle)=\frac{\log(1/\theta_T)}{2\pi^2}+o(H_1)=L+o(H_1)$, y $\langle u(X)V\rangle=o(H_1)$. Lo demás de [T5] no usa que $c$ sea fijo (Lema 4.3 con $b=c$; Lema 7.4 con $c\le\frac12$). Así $B_c=2L+o(H_1)\sim\frac{H_1}{2\pi^2}$ y $|\|r\|_2-\|\mathfrak t\|_2|\le\|u(X)\|_2+O(1/T)=o(\sqrt{H_1})$. $\square$

### R3. El reloj de un paso con exponente fijo, en ordenadas
**Enunciado.** Para $c\in(0,\frac12]$ fijo,
$$\bigl\langle(\tau^{T^c}_k-\gamma_k)^2\bigr\rangle=\frac{2\log\log\log T+O_c(\sqrt{H_1H_2})}{\log^2T},$$
el doble de lo que da el corte variable $T^{1/\sqrt{\log\log T}}$ de [I] Cor 7.4 ($\frac{\log\log\log T+O(\sqrt{H_1})}{\log^2T}$). Con el reloj desnudo, $\frac{\langle(\tau^{T^c}-\gamma)^2\rangle}{\langle(\tau-\gamma)^2\rangle}\sim\frac{\log\log\log T}{\log\log T}$.

**Prueba.** $(\tau^X_k-\gamma_k)^2=r_k^2/\Lambda(\tau_k)^2$ y $\Lambda(\tau_k)=\frac{\log T}{2\pi}(1+O(\frac1{\log T}))$ en $\mathcal I_T$; R1. $\square$

### R4. Cota inferior para todo corte $T^c$ con $c\ge\theta_T$ (también $c=c(T)$)
**Enunciado.** Uniformemente para $\theta_T\le c\le\frac12$,
$$\langle r_k(T^c)^2\rangle\ge\frac1{2\pi^2}\log\frac c{\theta_T}-O\bigl(\sqrt{H_1H_2}\bigr).$$
En particular, para $c=(\log\log T)^{-\alpha}$ con $0\le\alpha<\frac12$ fijo, $\langle r_k(T^c)^2\rangle\ge\frac{(1/2-\alpha)}{2\pi^2}\log\log\log T\,(1-o(1))$, y también $\langle r_k(T^c)^2\rangle\ll\log\log\log T$. En ese régimen intermedio [I] Thm 7.3 no da nada (su error contiene $c^2\log\log T=H_0^{1-2\alpha}$).

**Prueba.** $r_k=s_k+\chi_k-S_X(\tau_k)$ con $0\le\chi_k\le1/T$ ([I] eq. (2.6) y Thm 6.1(a)). Por la Proposición 6.1 y la Proposición 7.6 (válidas para $c\ge\theta_T$, véase la uniformidad de §2), $\langle sW_{\rm pr}(\tau)\rangle=O(\sqrt{H_1H_2})$ (el paso $W\to W_{\rm pr}$ cuesta $\|s\|_2\|W_{\rm pp}(\tau)\|_2\ll\sqrt{H_0}Y^{-1/4}$). Por el Lema 4.9, $\langle S_X(\tau)W_{\rm pr}(\tau)\rangle=\langle W_{\rm pr}^2\rangle+\langle S_YW_{\rm pr}\rangle+\langle W_{\rm pp}W_{\rm pr}\rangle=L+O(\sqrt L)$. Luego $|\langle rW_{\rm pr}(\tau)\rangle|\ge L-O(\sqrt{H_1H_2})$, y por Cauchy–Schwarz con $\langle W_{\rm pr}(\tau)^2\rangle=L(1+o(1))+o(1)$,
$$\langle r^2\rangle\ge\frac{\langle rW_{\rm pr}\rangle^2}{\langle W_{\rm pr}^2\rangle}\ge L-O(\sqrt{H_1H_2}).$$
Cota superior: $r=u(X)+\mathfrak t(Y)+U-V+\chi$ ([T5] Prop 5.1), $\langle u(X)^2\rangle\le\frac{\alpha H_1}{2\pi^2}+O(\sqrt{H_1})$, $\langle U^2\rangle\le2\langle u(Y)^2\rangle+2\langle u(X)^2\rangle\ll H_1$, $\langle V^2\rangle=L+o(1)$, $\langle\mathfrak t(Y)^2\rangle\ll\omega^2$. $\square$

### R5. Respuesta del reloj a los primos móviles: media logarítmica nula
**Enunciado.** Para $c\in(0,\frac12]$ fijo y $\theta_T\le\theta'<c$ (que pueden depender de $T$), con $\mu'=\sum_{T^{\theta'}<p\le T^c}\frac1p=\log\frac c{\theta'}+o(1)$,
$$\Bigl|\sum_{T^{\theta'}<p\le T^c}\frac{\mathcal R^\tau_p(\mathcal I_T)}p\Bigr|\ll1+\sqrt{\mu'(1+H_2)} .$$
En particular la media armónica de $\mathcal R^\tau_p$ en $(T^{\theta_T},T^c]$ es $O(\sqrt{H_2/H_1})\to0$. Esto cierra, con un resultado más fuerte, el abierto "$\limsup\overline{\mathcal R}_c\le\frac12$" de la nota del 23-10 (§8): $\overline{\mathcal R}_c\to0$. Contrasta con [I] Thm 11.3 ($\mathcal R^\tau_p\to1$ para $p\le(\log T)^{2-\varepsilon}$): la transición está entre $\theta\asymp\frac{\log\log T}{\log T}$ y $\theta_T\asymp\sqrt{H_2/H_0}$.

**Prueba.** Con $\mathcal J=(T^{\theta'},T^c]$: $\langle sW_{\mathcal J}(\tau)\rangle=\langle Q(\rho)W_{\mathcal J}(\tau)\rangle+O(\|s-Q(\rho)\|_2\|W_{\mathcal J}(\tau)\|_2)$, y $\|s-Q(\rho)\|_2\ll1+\sqrt{H_2}$ ([T5] Prop 6.1). Por (2.1), $\langle Q(\rho)W_{\mathcal J}\rangle=\sum\frac{a_p^2}2\Phi^\sharp_T(p)+o(1+\sqrt{\mu'})$, y para $p>Y$, $|\Phi^\sharp_T(p)|\ll e^{-2\pi^2\omega^2(1+o(1))}+2^{-J_0}$, cuya suma contra $a_p^2/2$ es $\ll H_1e^{-2\pi^2\omega^2}\to0$. Finalmente $\langle sW_{\mathcal J}(\tau)\rangle=\frac1{2\pi^2}\sum_{\mathcal J}\frac{\mathcal R^\tau_p}p$. $\square$

### R6. Ley de la respuesta del transporte del segundo reloj (sin ceros)
**Enunciado.** Para toda banda $\mathcal J\subset(X_1,T^{1/2}]$,
$$\sum_{p\in\mathcal J}\frac{\mathcal B^{(2)}_p}p=\sum_{p\in\mathcal J,\ p\le X_2}\frac{\Phi_T(p)-1}p+o\bigl(1+\sqrt{\mu(\mathcal J)}\bigr),$$
con
$$\Phi_T(p)=\exp\Bigl(-\theta_p^2\bigl(\log\log T-\tfrac12\log\log\log T+O(1)\bigr)+O(\theta_p^4)\Bigr)\bigl(1+O(\tfrac{\theta_p^2H_0}{\log T})\bigr),\qquad\theta_p=\frac{\log p}{\log T}.$$
Consecuencias:
- (a) En toda banda $\mathcal J\subset(X_2,T^{1/2}]$, en particular en toda banda de $\theta$ fijo en $(0,\frac12]$: $\sum_{\mathcal J}\mathcal B^{(2)}_p/p=o(1+\sqrt\mu)$. Con [I] Thm 11.14(iii), $\sum_{\mathcal J}(\mathcal R^\tau_p-\mathcal E^{(2)}_p)/p=o(1+\sqrt\mu)$: a $\theta$ fijo, la respuesta del reloj la lleva entera el residuo del segundo reloj. [I] Thm 11.14(iv) solo daba $\sum|\mathcal B^{(2)}_p|^2/p\ll H_0/H_1$.
- (b) En $(X_1,X_2]$, es decir $\theta\in(H_0^{-1/2},H_1^{-1/2}]$, la respuesta calculable del segundo reloj, $\mathcal A^{(2)}_p=\mathcal D^{(2)}_p+\mathcal B^{(2)}_p$, sigue en media logarítmica (en bandas de masa acotada) la ley gaussiana $\Phi_T(p)\approx e^{-\theta_p^2\log\log T}$. Es la ley que [I] tras (11.19) declara no demostrada ni siquiera en $L^2(dp/p)$ salvo error $O(1)$.

**Prueba.** $B^{(2)}_k=Q(\rho_k)-Q(\tau_k)$. Por (2.1), $\langle Q(\rho)W_{\mathcal J}(\tau)\rangle=\sum_{\mathcal J,\,p\le X_2}\frac{a_p^2}2\Phi^\sharp_T(p)+o(1+\sqrt\mu)$. Por otro lado, $\langle Q(\tau)W_{\mathcal J}(\tau)\rangle=\sum_{\mathcal J,\,p\le X_2}\frac{a_p^2}2+o(1+\sqrt\mu)$: la parte prima por el Lema 4.3 ($\ll\sqrt{H_0\mu}/\log T$); la de potencias de primos de $Q^\flat$ por el Lema 4.2 (sin frecuencia cero, altura $\le X_2^2T^{1/2}$, norma $\ll X_2T^{1/4}$, error $T^{-1/4+o(1)}$); y $Q-Q^\flat$ por (7.3). Restando y multiplicando por $2\pi^2$, con (2.2), se obtiene la fórmula.
Asintótica de $\Phi_T$: en el modelo, $P_0+P_1=\sum_{r\le X_1}f_r(\theta_r)$ con $f_r$ impar en $\theta_r$, así que $\mathbb Ee^{-i\xi f_r}=\mathbb E\cos(\xi f_r)=1-\frac{\xi^2}2\mathbb Ef_r^2+O(\xi^4c_r^4)$, con $|\xi c_r|<1$. Además $\mathbb Ef_r^2=\frac1{2\pi^2r}+O(r^{-2})$ y $\sum_{r\le X_1}\frac1r=H_0-\frac12H_1+O(1)$. Tomando logaritmos y sumando, $\log\mathbb Ee^{-i\xi(P_0+P_1)}=-\frac{\xi^2}{4\pi^2}(H_0-\frac12H_1+O(1))+O(\xi^4)$, con $\xi=\xi_{p,k}=2\pi\theta_p(1+O(\frac1{\log T}))$. $\square$

## 3. Lo que sigue sin salir, y por qué

| Cuestión | Obstáculo concreto |
|---|---|
| Ley de $\mathcal R^\tau_p$ (o de $\mathcal R^\gamma_p$, Conjetura 12.2) a $\theta$ fijo, por primo o en bandas de masa acotada | El paso B cuesta $\|s-Q(\rho)\|_2\|W_{\mathcal J}\|_2\asymp\sqrt{H_2\mu}$, mayor que la masa $\mu$ si $\mu\ll H_2$. Con $m^*$ pasos ([I] Thm 8.10) el coste es $O(\sqrt\mu)$, pero habría que hacer el desarrollo agregado de un reloj compuesto de $m^*$ niveles (modelo conjunto de polinomios compuestos). Sin hacer. |
| Constante exacta en el régimen intermedio $c=H_0^{-\alpha}$ (conjetura: $\frac{(1-\alpha)H_1}{2\pi^2}$) | Hace falta $\langle u(T^c)W(\gamma_k)\rangle=o(L)$ en las ordenadas: es la ley de diferencias de la nota del 23-10, §3.1, que está sin verificar. |
| Ventana $\sqrt{H_1/H_0}\lesssim c\lesssim H_0^{-1/2+o(1)}$: ¿$\langle r(T^c)^2\rangle\gg H_1$? | R4 da $\frac1{2\pi^2}\log(c/\theta_T)-O(\sqrt{H_1H_2})$, que allí no basta. [I] Thm 7.3 con $\|\mathfrak t\|_2\ll c\sqrt{H_0}$ cubre $c=o(\sqrt{H_1/H_0})$. |
| $c>\frac12$ | El Lema 4.3 y el Lema 7.4 se extienden hasta $c<\frac23$ (con [I] Prop 8.17), pero el paso A necesita $\langle u(T^c)^2\rangle=o(L)$, es decir el teorema B con $c>\frac12$: es la misma barrera de la nota del 23-10, §3. |
| Casi todo $k$, puntual, Teorema E | La técnica es en media cuadrática y no da cotas de bola pequeña ni de sup. |
| Error $O(1)$ en [I] Thm 7.3 (c óptimo) y Thm 8.5 | Haría falta el término cruzado $\langle u\,\mathfrak t\rangle$ en el régimen de transporte pequeño; la ruta pasaría por sustituir los ceros por el tercer reloj ([I] Cor 8.11). Sin hacer. |

## 4. Integración

R1 cambia un parámetro del artículo del transporte (v6 cuando se ordene). R2–R6 son corolarios con pruebas cortas a partir de [T5]; R5 y R6 encajan en [I] §11 (respuestas) y R3–R4 en [I] §7. Ningún manuscrito cambiado.
