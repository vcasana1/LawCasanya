# Truncación infinita: el paso de Newton con $S$ completo desde el reloj RvM (2026-10-24)

[I] = manuscript/ordinal_prime_cutoff_v14.tex; [T5] = work/paper1/transport_theorem/transport_energy_theorem_v5.tex.
Notación de [I]: $S=N-N_0-\varpi/\pi$ ([I] (2.1)–(2.2)), con $N$ continua por la derecha; $s_k=N_0(\tau_k)-N_0(\gamma_k)$; $\Lambda(\tau_k)\delta_k=s_k+\chi_k$ con $0\le\chi_k\le1/T$ ([I] Thm 6.1(a)); $u_k(X)=s_k-S_X(\gamma_k)$; $\mathfrak t_k(X)=S_X(\gamma_k)-S_X(\tau_k)$; $E_X=S-S_X$; $\mathfrak b=2\pi/\log(3T)$; $M=\#\mathcal I_T$; $\mathcal U_k=[\tau_k,\tau_k+\mathfrak b]$, disjuntos y contenidos en $[T-1,2T+2]$.

## Lema 1 (defecto en los puntos del reloj)
Para $2\le X\le T^{1/2}$, $c=\log X/\log T$ y $T\ge T_0$,
$$\Bigl\langle(S-S_X)(\tau_k)^2\Bigr\rangle_{\mathcal I_T}^{1/2}\le\Bigl(\frac1{2\pi^2}\log\frac1c\Bigr)^{1/2}+O(1).$$
En particular $\langle(S-S_{T^{1/2}})(\tau_k)^2\rangle=O(1)$.

**Prueba.** Sea $A_k(F)=\frac1{\mathfrak b}\int_{\mathcal U_k}F$.

*Paso 1 (identidad local).* Para $0\le y\le\mathfrak b$, como $S=N-N_0-\varpi/\pi$ y $\varpi'=O(t^{-2})$,
$$S(\tau_k)=S(\tau_k+y)-\bigl[N(\tau_k+y)-N(\tau_k)\bigr]+\bigl[N_0(\tau_k+y)-N_0(\tau_k)\bigr]+O(T^{-1}).$$
Se promedia en $y\in[0,\mathfrak b]$. El segundo corchete está en $[0,n_k]$, con $n_k=N(\tau_k+\mathfrak b)-N(\tau_k)$. El tercero está en $[0,\Lambda(2T+2)\mathfrak b]\subset[0,1]$. Para la parte lisa, $|S_X(\tau_k)-A_k(S_X)|\le\int_{\mathcal U_k}|S_X'|$. Por tanto
$$|E_X(\tau_k)|\le|A_k(E_X)|+n_k+1+\int_{\mathcal U_k}|S_X'|+O(T^{-1}),$$
y por Minkowski en $\ell^2(\mathcal I_T)$,
$$\|E_X(\tau)\|_2\le\|A(E_X)\|_2+\|n\|_2+1+\Bigl\|\int_{\mathcal U}|S_X'|\Bigr\|_2+o(1).$$

*Paso 2 (media de $E_X$).* Por Jensen y la disjunción de los $\mathcal U_k$, $\|A(E_X)\|_2^2\le\frac1{\mathfrak bM}\int_{T-1}^{2T+2}E_X^2$. Por [I] (5.10) (ec. J_asymptotic, que usa la aproximación de Selberg–Fujii [I] Thm 3.5 y Montgomery–Vaughan) y [I] Lema 5.8 ($V=\log(1/c)+O(1)$),
$$\int_T^{2T}E_X^2\,dt=\frac T{2\pi^2}\log\frac1c+O\Bigl(T\bigl(1+\sqrt{\log(1/c)}\bigr)\Bigr).$$
Los dos tramos de longitud $\le2$ fuera de $[T,2T]$ cuestan $\ll(\log T+T^{1/4})^2=O(T^{1/2})$, porque $|S|\ll\log T$ y $|S_X|\le T^{1/4}$. Como $\mathfrak bM=T(1+o(1))$,
$$\|A(E_X)\|_2^2\le\frac1{2\pi^2}\log\frac1c+O\bigl(1+\sqrt{\log(1/c)}\bigr).$$

*Paso 3 (parte lisa).* $\bigl\|\int_{\mathcal U}|S_X'|\bigr\|_2^2\le\frac{\mathfrak b}M\int_{T-1}^{2T+2}S_X'^2\ll\frac{\mathfrak b}MT(1+\log X)^2\ll1$, por [I] (5.8) (ec. SX_derivative).

*Paso 4 (pares de ceros cercanos).* Los intervalos $(\tau_k,\tau_k+\mathfrak b]$ son disjuntos, así que $\sum_kn_k^2\le P$, donde $P$ es el número de pares ordenados de ceros (con multiplicidad) con ordenadas en $(T-1,2T+3]$ y $|\gamma-\gamma'|\le\mathfrak b$. Sea $h=3\mathfrak b$. Para cada par así y cada $t\in[\gamma-\mathfrak b,\gamma+\mathfrak b]$, las dos ordenadas están en $(t-h,t+h]$. Por tanto
$$P\le\frac1{2\mathfrak b}\int_{T-2}^{2T+4}\bigl(N(t+h)-N(t-h)\bigr)^2dt .$$
Además, $N(t+h)-N(t-h)=[N_0(t+h)-N_0(t-h)]+[S(t+h)-S(t-h)]+O(T^{-1})$, y el primer corchete es $\le2h\Lambda(2T+5)\le7$. Con el cambio $s=t-h$ y el teorema de Fujii [I] Thm 3.6 ($k=1$, paso $2h=6\mathfrak b\le1$) en las ventanas diádicas $[T/2,T]$, $[T,2T]$ y $[2T,4T]$,
$$\int\bigl(S(s+2h)-S(s)\bigr)^2ds\ll T\log(2+6\mathfrak b\log 4T)\ll T .$$
Luego $P\ll T/\mathfrak b\asymp M$, y $\|n\|_2=O(1)$.

Los pasos 1–4 dan el lema. $\square$

## Teorema 2 (paso de Newton con la fase completa desde el reloj RvM)
Sea $\tau^\infty_k=\tau_k-S(\tau_k)/\Lambda(\tau_k)$, es decir, un paso de Newton sobre la ecuación verdadera $N(t)=k-\frac12$, linealizada con pendiente $\Lambda$. Entonces
$$\bigl\langle\Lambda(\tau_k)^2(\tau^\infty_k-\gamma_k)^2\bigr\rangle_{\mathcal I_T}=\frac1{2\pi^2}\log\log\log T+O\bigl((\log\log\log T)^{5/8}\bigr),$$
y por tanto $\langle(\tau^\infty_k-\gamma_k)^2\rangle\sim2\log\log\log T/\log^2T$.

Formulación sin primos: $r_k(\infty)=s_k-S(\tau_k)+\chi_k$. Para un cero simple, $s_k=S(\gamma_k)+O(1/T)$ (con la convención $N(\gamma_k)=k-\frac12$), y $r_k(\infty)$ es el incremento de $S$ entre cada cero y su punto del reloj. Su media cuadrática crece como $\frac1{2\pi^2}\log\log\log T$, lo que concuerda con la varianza de Fujii $\frac1{\pi^2}\log(h\Lambda)$ para incrementos de longitud $h\Lambda\asymp|s_k|\asymp\sqrt{\log\log T}$.

**Prueba.** $r_k(\infty)=\Lambda(\tau_k)(\tau_k-\gamma_k)-S(\tau_k)=s_k+\chi_k-S(\tau_k)$. Para todo $X$, con $v_k(X)=(S-S_X)(\tau_k)$, se cumple exactamente
$$r_k(\infty)=\mathfrak t_k(X)+u_k(X)-v_k(X)+\chi_k,$$
porque $\mathfrak t+u-v=S_X(\gamma)-S_X(\tau)+s-S_X(\gamma)-S(\tau)+S_X(\tau)=s-S(\tau)$. Con $X=T^{1/2}$: $\|u(X)\|_2=O(1)$ por el teorema B ([I] Thm 5.1, $c=\frac12$), $\|v(X)\|_2=O(1)$ por el Lema 1 y $\|\chi\|_2\le1/T$. Por Minkowski, $|\|r(\infty)\|_2-\|\mathfrak t(T^{1/2})\|_2|=O(1)$. Por [T5] Thm 1.1 con $c=\frac12$, $\|\mathfrak t(T^{1/2})\|_2^2=\frac{H_1}{2\pi^2}+O(H_1^{5/8})$. Luego $\langle r(\infty)^2\rangle=\frac{H_1}{2\pi^2}+O(H_1^{5/8})+O(\sqrt{H_1})$. $\square$

Con R1 de la nota 2026-10-24_distancia_tau_gamma_consecuencias_transporte.md el error baja a $O(\sqrt{H_1H_2})$.

**Consecuencia.** Ni siquiera con toda la información prima ($S$ completo, es decir, $\zeta$ misma) un solo paso de Newton desde el reloj RvM deja el error acotado en unidades de espaciado. La constante $\frac1{2\pi^2}$ es la misma que con corte $T^c$, $c\in(0,\frac12]$ fijo: el factor 2 respecto del corte óptimo $T^{1/\sqrt{\log\log T}}$ ([I] Cor 7.4) es intrínseco al paso único linealizado desde $\tau_k$, no a la truncación.
