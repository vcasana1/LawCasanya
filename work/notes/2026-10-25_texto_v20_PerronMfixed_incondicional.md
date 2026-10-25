# Texto propuesto para v20: `thm:PerronMfixed` incondicional a $X$ fijo, con los dos candidatos admisibles

Nota de Claude, 25-oct-2026. Texto autocontenido (en inglés, listo para que ChatGPT lo inserte; Claude no edita el manuscrito). Cierra la cadena: Lema de banda → Teorema de transición (Thm A) → Teorema del residuo de Newton → Corolario ($J_X<\infty$, Perron sin hipótesis). Incluye la comprobación de la dominación uniforme en $r$ del paso 3 de Thm A, que estaba marcada "sin comprobar" en mi nota del 24-oct: ahora está hecha (se suma en $m$ antes de integrar). Único input externo: [v26, Lemma TR-smooth] (la parte $N_0$ del producto da $\log G$ + constante + $O(1/t)$), teorema del autor. Sin ejecuciones numéricas.

---

## Setting

Fix $X\ge2$. Let $P(X)=\prod_{p\le X}p$, $\mathscr E_X(s)=\prod_{p\le X}(1-p^{-s})^{-1}$, and
$$S_X(\tau)=\sum_{p\le X}\sum_{m\ge1}\beta_{p^m}\sin(m\tau\log p),\qquad \beta_{p^m}=-\frac1{\pi mp^{m/2}},\qquad N_X=N_0+S_X,\qquad \Lambda=N_0' .$$
$S_X$ extends holomorphically to the strip $|\Im\tau|<\tfrac12$. Put $A_j=\sup_{\tau\in\mathbb R}|S_X^{(j)}(\tau)|$ ($j=0,1,2,3$) and, for $0\le Y<\tfrac12$,
$$A_X(Y)=\frac1\pi\sum_{p\le X}\log p\,\frac{p^{Y-1/2}}{1-p^{Y-1/2}}\ \ \ge\ \sup_{|\Im\tau|\le Y}|S_X'(\tau)| .$$

**Lemma 1 (strip monotonicity).** Let $0<Y<\tfrac12$ and $\tau'$ with $\Lambda(\tau')\ge2A_X(Y)$ and $(\tau'/2\pi)^{-Y/2}\le\tfrac12$. For $x\ge\tau'$ and $0\le y\le Y$:
$$\Im N_X(x+iy)\ge\tfrac12y\Lambda(x),\qquad \Im N_X(x-iy)\le-\tfrac12y\Lambda(x),\qquad \tfrac12\Lambda(x)\le N_X'(x)\le\tfrac32\Lambda(x).$$
*Proof.* $\partial_y\Im N_X(x+iy)=\Re N_X'(x+iy)\ge\Re N_0'(x+iy)-A_X(Y)\ge\Lambda(x)-\tfrac12\Lambda(x)$; integrate from $y=0$ where $\Im N_X=0$. The real-axis bound is $|S_X'|\le A_X(0)\le A_X(Y)\le\tfrac12\Lambda$. $\square$

**Definition (the two admissible lists).** Let $K'=\lfloor N_X(\tau')+\tfrac12\rfloor$ and fix $K'$ conventional points $\kappa_1\le\dots\le\kappa_{K'}$ in $[2\pi,\tau')$, the same for both lists. For $k>K'$:
- *exact roots:* $\kappa^{\rm ex}_k$ is the unique solution in $(\tau',\infty)$ of $N_X(\kappa)=k-\tfrac12$;
- *full-derivative Newton step:* $\displaystyle\kappa^{N}_k=\tau_k-\frac{S_X(\tau_k)}{N_X'(\tau_k)}=\tau_k-\frac{S_X(\tau_k)}{\Lambda(\tau_k)+S_X'(\tau_k)}$, where $N_0(\tau_k)=k-\tfrac12$.

Both are explicit functions of the clock and the primes $p\le X$. For either list $\kappa$, $n_\kappa(\tau)=\#\{k:\kappa_k\le\tau\}$; for the exact list, $n^{\rm ex}(\tau)=\lfloor N_X(\tau)+\tfrac12\rfloor$ for $\tau\ge\tau'$. $\Xi_\kappa,\zeta_\kappa$ are as in `prop:xiSynthetic`; $\zeta_\kappa$ has its nontrivial zeros exactly at $\tfrac12\pm i\kappa_k$, so $1/\zeta_\kappa$ is holomorphic in $\Re s>\tfrac12$ except for the zero of $\zeta_\kappa$... (no: $1/\zeta_\kappa$ has poles only at the zeros of $\zeta_\kappa$, all on $\Re s=\tfrac12$ and at the trivial ones; it is holomorphic on $\Re s>\tfrac12$, and $\zeta_\kappa$ has a simple pole at $s=1$ so $1/\zeta_\kappa(1)=0$.)

Throughout, $s=\tfrac12+\sigma'+it$ with $0<\sigma'\le\sigma_2'<\tfrac12$ fixed, $z=s-\tfrac12$, $w=t-i\sigma'=-iz$ (so $\tfrac12+iw=s$, $\tfrac12-iw=1-s$), and $f(\tau)=\operatorname{Log}(1+z^2/\tau^2)$,
$$f'(\tau)=\frac{2z^2}{\tau(\tau^2+z^2)}=-\frac2\tau+\frac1{\tau-w}+\frac1{\tau+\bar w}.$$

## Theorem A (transition, exact list)

**Theorem A.** Fix $X$, $\sigma_2'$, $Y\in(\sigma_2',\tfrac12)$ and $\tau'$ as in Lemma 1. There are $\varpi^{\rm ex}_X>0$ and $C,t_0$ depending on $X,\sigma_2'$ such that for $t\ge t_0$ and $0<\sigma'\le\sigma_2'$,
$$\zeta^{\rm ex}_{C,X}(s)=\varpi^{\rm ex}_X\,\mathscr E_X(s)\,\bigl(1+w_X(s)\bigr)\bigl(1+\mathcal E_X(s)\bigr),\qquad w_X(s)=e^{-2\pi iN_X(w)},\quad |w_X|\le(t/2\pi)^{-\sigma'/2},\quad |\mathcal E_X|\le Ct^{-Y/2}\log t .$$

*Proof.* (Full version: Claude note 2026-10-24, §2; here the structure and the point previously left unchecked.)

(1) *Stieltjes form.* With $n^{\rm ex}=N_X-\rho$, $\rho(\tau)=N_X(\tau)-\lfloor N_X(\tau)+\tfrac12\rfloor=\psi(N_X+\tfrac12)$, $|\rho|\le\tfrac12$,
$$\log\frac{\Xi^{\rm ex}(s)}{C^{\rm ex}}=\sum_{k\le K'}f(\kappa_k)+\int_{\tau'}^\infty f\,dn^{\rm ex}
=\sum_{k\le K'}f(\kappa_k)+K'f(\tau')\cdot0-\int_{\tau'}^\infty N_Xf'\,d\tau+\int_{\tau'}^\infty\rho f'\,d\tau,$$
the boundary term at $\tau'$ vanishing because $n^{\rm ex}(\tau')=K'=N_X(\tau')-\rho(\tau')$. The finite sum is $2\sum_{k\le K'}\log(1/\kappa_k)+\log|z|^{2K'}\cdot$— more precisely $\sum_{k\le K'}f(\kappa_k)=\sum_{k\le K'}\bigl[2\operatorname{Log}z-2\log\kappa_k\bigr]+O(t^{-2})$; the $2K'\operatorname{Log}z$ cancels against the same term produced by $-\int N_0f'$ (this is why the number of low points must be exactly $K'$).

(2) *Smooth part.* $-\int_{\tau'}^\infty N_0f'$ is [v26, Lemma TR-smooth]: $\log G(s)-2K'\operatorname{Log}z+c_1+O(t^{-1})$, $G(s)=s(s-1)\Gamma(s/2)\pi^{-s/2}$ up to the normalization of `prop:xiSynthetic`. For $-\int S_Xf'$, termwise in $n=p^m$, $\ell=\log n$: $\int_{\tau'}^\infty\sin(\tau\ell)f'(\tau)d\tau=c_\ell+\pi e^{-iw\ell}+O(1/(t\ell))$, obtained by writing $\sin=\frac1{2i}(e^{i\ell\tau}-e^{-i\ell\tau})$ and rotating the $e^{-i\ell\tau}$ integral to the lower ray $\tau'-iy$ (picking the residue of $\frac1{\tau-w}$ at $w$) and the $e^{i\ell\tau}$ integral to the upper ray (no pole, since $-\bar w$ has negative real part). Since $e^{-iw\ell}=n^{1/2}n^{-s}$ and $\beta_n\pi n^{1/2}=-1/m$,
$$-\int_{\tau'}^\infty S_Xf'=\sum_{p\le X}\sum_m\frac{p^{-ms}}m+c_2+O_X(t^{-1})=\log\mathscr E_X(s)+c_2+O_X(t^{-1}),$$
the $m$-series converging absolutely ($\int|f'|\ll\log t$ and $\sum|\beta_n|<\infty$).

(3) *Sawtooth part — the step that gives $1+w_X$.* Let $\psi_r(y)=-\sum_{m\ge1}\frac{(-r)^m}{\pi m}\sin(2\pi my)$, $0<r<1$, be the Abel means of $\psi(y+\tfrac12)$. The Abel–Poisson kernel is positive, so $|\psi_r|\le\tfrac12$, and $\psi_r\to\psi(\cdot+\tfrac12)$ pointwise off the integers; since $f'\in L^1(\tau',\infty)$, dominated convergence gives $\int\rho f'=\lim_{r\to1}\int\psi_r(N_X)f'$. For fixed $r$ the series may be integrated termwise. Write $\sin(2\pi mN_X)=\frac1{2i}(e^{2\pi imN_X}-e^{-2\pi imN_X})$ and split $f'=-\frac2\tau+g$, $g=\frac1{\tau-w}+\frac1{\tau+\bar w}$.

*The $-2/\tau$ part* is independent of $z$. For each $m$, $\int_{\tau'}^\infty e^{\mp2\pi imN_X}\frac{d\tau}{\tau}=O\bigl(\frac{1}{m\Lambda(\tau')\tau'}\bigr)$ by one integration by parts ($N_X'\ge\tfrac12\Lambda$ and monotone phase), so $\sum_m\frac{r^m}{m}\cdot\frac1m$ converges uniformly in $r$: this part is a real constant $c_3$.

*The $g$ part, $e^{-2\pi imN_X}$.* **Sum over $m$ first:** for $\tau$ in the closed lower strip $-Y\le\Im\tau\le0$, $\Re\tau\ge\tau'$, Lemma 1 gives $|e^{-2\pi iN_X(\tau)}|\le(\Re\tau/2\pi)^{-|\Im\tau|/2}\le1$, so
$$\Phi_r(\tau):=\sum_{m\ge1}\frac{(-r)^m}{m}e^{-2\pi imN_X(\tau)}=-\operatorname{Log}\bigl(1+re^{-2\pi iN_X(\tau)}\bigr)$$
is holomorphic there. Apply Cauchy to $\Phi_r\,g$ on the rectangle with vertices $\tau',R,R-iY,\tau'-iY$. The only pole of $g$ inside is $w=t-i\sigma'$ (since $Y>\sigma_2'\ge\sigma'$ and $t>\tau'$), with residue $\Phi_r(w)=-\operatorname{Log}(1+rw_X)$. Bounds, uniform in $r$:
- bottom side $\Im\tau=-Y$: $|1+re^{-2\pi iN_X}|\ge1-(x/2\pi)^{-Y/2}\ge\tfrac12$, so $|\Phi_r(x-iY)|\le2(x/2\pi)^{-Y/2}$; and $|g(x-iY)|\ll x/t^2$ for $x\le t/2$, $\ll1/\max(|x-t|,Y-\sigma')$ for $t/2\le x\le2t$, $\ll1/x$ for $x\ge2t$; hence the side contributes $\ll t^{-Y/2}\log t$;
- right side $\Re\tau=R$: $|g|\ll t^2/R^3$, $|\Phi_r|\le\log 2$; $\to0$ as $R\to\infty$;
- left side $\Re\tau=\tau'$, $\tau=\tau'-iy$: $|g|\ll1/t$, and $\int_0^Y|\Phi_r(\tau'-iy)|dy\le\int_0^Y\bigl(\bigl|\log|1+re^{-2\pi iN_X}|\bigr|+\pi\bigr)dy$; since $|1+re^{-2\pi iN_X(\tau'-iy)}|\ge1-(\tau'/2\pi)^{-y/2}\ge c\,y$, the integrand is $\le|\log(cy)|+\pi$, integrable, uniformly in $r$: the side contributes $O_X(1/t)$.
Therefore $\int_{\tau'}^\infty\Phi_r(\tau)g(\tau)d\tau=-2\pi i\cdot\bigl(-\operatorname{Log}(1+rw_X)\bigr)\cdot(\text{orientation sign})+O(t^{-Y/2}\log t)$, and the orientation (real axis traversed left to right, pole below it) makes the residue term equal $+2\pi i\operatorname{Log}(1+rw_X)$ up to the overall factor; letting $r\to1$ (allowed since $|w_X|<1$) and restoring the factor $\frac1{2i}\cdot\bigl(-\frac1\pi\bigr)$ from $\psi_r$ gives exactly $\operatorname{Log}(1+w_X)$.

*The $g$ part, $e^{+2\pi imN_X}$:* same rectangle reflected to the upper strip; $g$ has no pole there ($-\bar w$ has real part $-t<\tau'$), and the same bounds give $O(t^{-Y/2}\log t)$.

(4) *Assembly.* Exponentiating (1)–(3) and dividing by $G$: $\zeta^{\rm ex}_{C,X}(s)=\varpi^{\rm ex}_X\mathscr E_X(s)(1+w_X)(1+\mathcal E_X)$ with $\varpi^{\rm ex}_X=C^{\rm ex}e^{c_1+c_2+c_3+\ldots}>0$ and $\mathcal E_X=O(t^{-Y/2}\log t)+O_X(t^{-1})$. The bound on $|w_X|$ is Lemma 1 at $\tau=w$, $\Im w=-\sigma'$. $\square$

## Theorem N (Newton residual)

**Theorem N.** With the notation above, for $k>K'$ put $\epsilon_k=\kappa^N_k-\kappa^{\rm ex}_k$. Then
$$\epsilon_k=\frac{h_k^2N_X''(\xi_k)}{2N_X'(\tau_k)}\quad(\kappa^{\rm ex}_k=\tau_k-h_k,\ \xi_k\text{ between }\tau_k\text{ and }\kappa^{\rm ex}_k),\qquad |\epsilon_k|\le\frac{C_1(X)}{\Lambda(\tau_k)^3},$$
$$\epsilon_k=\mathcal E(\kappa^{\rm ex}_k)+O_X\bigl(\Lambda(\tau_k)^{-4}\bigr),\qquad \mathcal E(\tau):=\frac{S_X(\tau)^2S_X''(\tau)}{2\Lambda(\tau)^3},$$
and the trigonometric polynomials $S_X^2S_X''$ and $S_X^2S_X''S_X'$ have **no constant term**, because $S_X$ is odd.

*Proof.* $N_X(\tau_k)=k-\tfrac12+S_X(\tau_k)$ and $N_X(\kappa^{\rm ex}_k)=k-\tfrac12$; Taylor with Lagrange remainder gives $0=S_X(\tau_k)-h_kN_X'(\tau_k)+\tfrac12h_k^2N_X''(\xi_k)$, whence the formula. $|h_k|\le2A_0/\Lambda(\tau_k)(1+o(1))$ by monotonicity ($N_X'\ge\tfrac12\Lambda$ between $\kappa^{\rm ex}_k$ and $\tau_k$), $|N_X''|\le A_2+1$, $N_X'\ge\tfrac12\Lambda$: this gives $C_1=4A_0^2(A_2+1)(1+o(1))$. The expansion follows from $h_k=S_X(\tau_k)/\Lambda+O_X(\Lambda^{-2})$, $N_X''(\xi_k)=S_X''(\tau_k)+O(A_3|h_k|+1/\tau_k)$, $N_X'(\tau_k)=\Lambda(1+O_X(\Lambda^{-1}))$, and $\mathcal E(\tau_k)-\mathcal E(\kappa^{\rm ex}_k)=O(|h_k|\sup|\mathcal E'|)=O_X(\Lambda^{-4})$. Parity: $S_X(-\tau)=-S_X(\tau)$, so $S_X'$ is even and $S_X''$ odd; products with an odd number of odd factors are odd and have zero mean. $\square$

## Theorem C (the two synthetic zetas differ by a constant up to $O(\log^{-2}t)$)

**Theorem C.** Let $\Delta(s)=\log\zeta^N_{C,X}(s)-\log\zeta^{\rm ex}_{C,X}(s)$ (continuous branch along $\Re s=\tfrac12+\sigma'$). The limit $\Delta_\infty=\lim_{t\to\infty}\Delta(\tfrac12+\sigma'+it)$ exists, is independent of $\sigma'$, and
$$|\Delta(\tfrac12+\sigma'+it)-\Delta_\infty|\le\frac{C_2(X,\sigma')}{\log^2t}\qquad(t\ge t_1(X,\sigma')).$$

*Proof.* Let $\nu=n^N-n^{\rm ex}$; $\nu=0$ on $[0,\tau']$ and outside $\bigcup_kI_k$, $I_k$ the interval between $\kappa^{\rm ex}_k$ and $\kappa^N_k$, on which $\nu=-\operatorname{sgn}\epsilon_k$; $|I_k|=|\epsilon_k|$. Since $\sum_k|\epsilon_k|/\kappa_k\ll_X\sum_k\Lambda(\tau_k)^{-3}/\tau_k<\infty$, integration by parts in $\int f\,d\nu$ is legitimate and
$$\Delta(s)=\log\frac{C^N}{C^{\rm ex}}+\int_{\tau'}^\infty\nu f'\,d\tau,\qquad \Delta_\infty:=\log\frac{C^N}{C^{\rm ex}}+2\int_{\tau'}^\infty\frac{\nu(\tau)}{\tau}d\tau,\qquad \Delta(s)-\Delta_\infty=-\int_{\tau'}^\infty\nu(\tau)\,g(\tau)\,d\tau,$$
with $g=\frac1{\tau-w}+\frac1{\tau+\bar w}$ (because $f'+\frac2\tau=g$). The last integral converges absolutely.

*Step 1 (to the exact list).* $-\int\nu g=\sum_k\int_{\kappa^{\rm ex}_k}^{\kappa^{\rm ex}_k+\epsilon_k}g=\sum_k\epsilon_kg(\kappa^{\rm ex}_k)+O\bigl(\sum_k\epsilon_k^2\sup_{I_k}|g'|\bigr)$. Gaps of the exact list lie in $[\frac2{3\Lambda},\frac2\Lambda]$, so $\#\{k:|\kappa^{\rm ex}_k-t|\in[j,j+1)\}\le2\Lambda(t)+2$ for $j\le t/2$. Hence the error is $\ll_X\Lambda^{-6}(\Lambda/\sigma'+\Lambda\log t)\ll\Lambda(t)^{-4}$, and replacing $\epsilon_k$ by $\mathcal E(\kappa^{\rm ex}_k)$ costs $\sum_k\Lambda(\tau_k)^{-4}|g(\kappa_k)|\ll\Lambda(t)^{-4}\Lambda(t)\log t+\Lambda(t)^{-3}+\Lambda(t)^{-2}\ll\Lambda(t)^{-2}$ (near, below and above $t$ respectively). So
$$\Delta(s)-\Delta_\infty=\int_{\tau'}^\infty\mathcal E\,g\,dn^{\rm ex}+O_X(\Lambda^{-2})=\int_{\tau'}^\infty\mathcal EN_X'g\,d\tau-\int_{\tau'}^\infty\mathcal Eg\,d\rho+O_X(\Lambda^{-2}),$$
both integrals understood as $\lim_{R\to\infty}\int_{\tau'}^R$ (the sum of the two converges absolutely; each one converges by the estimates below).

*Step 2 (sawtooth part).* $\int_{\tau'}^R\mathcal Eg\,d\rho=[\mathcal Eg\rho]_{\tau'}^R-\int_{\tau'}^R\rho(\mathcal Eg)'d\tau$. The boundary terms are $O_X(1/t)$ and $O(\Lambda(R)^{-3}/R)\to0$. With $|\mathcal E|,|\mathcal E'|\ll_X\Lambda^{-3}$,
$$\int_{\tau'}^\infty|(\mathcal Eg)'|\ll_X\int_{\tau'}^\infty\frac{\Lambda(\tau)^{-3}}{|\tau-w|}d\tau+\int\frac{\Lambda(\tau)^{-3}}{|\tau-w|^2}d\tau\ll\Lambda(t)^{-3}\log\frac t{\sigma'}+\Lambda(t)^{-3}+\Lambda(t)^{-2}+\frac{\Lambda(t)^{-3}}{\sigma'}\ll\Lambda(t)^{-2}$$
(the ranges $[t/2,2t]$, $[\tau',t/2]$, $[2t,\infty)$; the $\tau+\bar w$ terms have no singularity and are smaller).

*Step 3 (continuous part; here the parity is used).* $\mathcal EN_X'=\frac{S_X^2S_X''}{2\Lambda^2}+\frac{S_X^2S_X''S_X'}{2\Lambda^3}=\sum_{\omega\in\Omega}\frac{q_\omega e^{i\omega\tau}}{2\Lambda^2}+\sum_{\omega\in\Omega_1}\frac{q^1_\omega e^{i\omega\tau}}{2\Lambda^3}$ with finite $\Omega,\Omega_1\not\ni0$ (Theorem N). It suffices to show, for fixed $\omega\ne0$ and $m\in\{2,3\}$,
$$I_{\omega,m}(t)=\int_{\tau'}^\infty\frac{e^{i\omega\tau}}{\Lambda(\tau)^m}\frac{d\tau}{\tau-w}=O_{X,\omega,\sigma'}\bigl(\Lambda(t)^{-m}\bigr),$$
the $\frac1{\tau+\bar w}$ analogue being $O(1/(|\omega|t))$ by one integration by parts. Write $\Lambda(\tau)^{-m}=\Lambda(t)^{-m}+\delta(\tau)$. (a) $\Lambda(t)^{-m}\int_{\tau'}^\infty\frac{e^{i\omega\tau}}{\tau-w}d\tau$: for $\Im w<0$, $\int_{\mathbb R}\frac{e^{i\omega\tau}}{\tau-w}d\tau=-2\pi ie^{i\omega w}\mathbf 1_{\omega<0}$, of modulus $\le2\pi e^{|\omega|\sigma'}$, and $|\int_{-\infty}^{\tau'}|\le\frac2{|\omega|(t-\tau')}$; so (a) $\ll\Lambda(t)^{-m}$. (b) $\int\delta\frac{e^{i\omega\tau}}{\tau-w}$: with $|\Lambda(\tau)-\Lambda(t)|=\frac{|\log(\tau/t)|}{2\pi}$, on $[t/2,2t]$ one has $|\delta|\ll\frac{|\tau-t|}{t\Lambda^{m+1}}$ and $\frac{|\tau-t|}{|\tau-w|}\le1$, giving $O(\Lambda^{-m-1})$; on $[2t,\infty)$ and $[\tau',t/2]$ one integration by parts against $e^{i\omega\tau}$ gives $O(\frac{1}{|\omega|t})$. Hence $I_{\omega,m}=O(\Lambda(t)^{-m})$ and the continuous part is $O_X(\Lambda(t)^{-2})$.

Steps 1–3 give the theorem with $\Lambda(t)\asymp\log t$. Independence of $\Delta_\infty$ from $\sigma'$: $\Delta$ is holomorphic in $\Re s>\tfrac12$ and the bound is uniform on compact $\sigma'$-ranges. $\square$

## Corollary (unconditional `thm:PerronMfixed` at fixed $X$)

**Corollary.** Let $X\ge2$ and $\sigma=\tfrac12+\sigma'$, $0<\sigma'<\tfrac12$. For $\kappa\in\{\kappa^{\rm ex},\kappa^N\}$, with $\varpi_X=\varpi^{\rm ex}_X$ resp. $\varpi^N_X:=\varpi^{\rm ex}_Xe^{\Delta_\infty}$,
$$D_X(s):=\frac{\varpi_X}{\zeta_{C,X}(s)}-\mathscr E_X(s)^{-1}=\mathscr E_X(s)^{-1}\Bigl[(1+w_X)^{-1}(1+\mathcal E_X)^{-1}e^{-(\Delta-\Delta_\infty)}-1\Bigr]\ll_{X,\sigma'}t^{-\sigma'/2}+\frac1{\log^2t},$$
($\Delta\equiv\Delta_\infty\equiv0$ for the exact list), hence
$$J_X(\sigma)=\frac1{2\pi}\int_{-\infty}^{\infty}\frac{|D_X(\sigma+it)|}{|\sigma+it|}\,dt<\infty .$$
Consequently the symmetric Perron transform $M_{C,X}(x)$ of $1/\zeta_{C,X}$ on $\Re s=\sigma$ exists for every $x\ge2$ and
$$\varpi_XM_{C,X}(x)=M_X^*(x)+\mathcal R_X(x),\qquad|\mathcal R_X(x)|\le J_X(\sigma)\,x^{\sigma},\qquad M_X^*(x)=M^*(x)\ \ (2\le x\le X),$$
and $M_{C,X}(x)=O_{X,\sigma'}(x^{1/2+\sigma'})$ for all $x$, since $|M_X^*|\le2^{\pi(X)}$ and $M_X^*(x)=0$ for $x\ge P(X)$. No hypothesis is needed.

*Proof.* Theorem A gives the bracket for the exact list; Theorem C adds the factor $e^{-(\Delta-\Delta_\infty)}=1+O(\log^{-2}t)$ for the Newton list. $\mathscr E_X^{-1}$ is bounded on the line, $|w_X|\le(t/2\pi)^{-\sigma'/2}$, $|\mathcal E_X|\ll t^{-Y/2}\log t$. On $|t|\le t_1$, $D_X$ is continuous ($1/\zeta_{C,X}$ is holomorphic on $\Re s>\tfrac12$); $\int_{t_1}^\infty(t^{-1-\sigma'/2}+\frac1{t\log^2t})dt<\infty$; $t<0$ by symmetry. The Perron statements are `thm:PerronMfixed` and `thm:Eulerarith`. $\square$

**Remark (why the $\Lambda$-step list is excluded).** For $\kappa^{(1)}_k=\tau_k-S_X(\tau_k)/\Lambda(\tau_k)$ the same computation gives $\epsilon^{(1)}_k=-\frac{S_XS_X'}{\Lambda^2}(\tau_k)+O(\Lambda^{-3})$ and, by Step 3 with $m=1$ and the exact value in (a),
$$\Delta^{(1)}(s)-\Delta^{(1)}_\infty=-\frac{\pi i}{\Lambda(t)}\sum_{\omega<0}c_\omega e^{\omega\sigma'}e^{i\omega t}+O_X(\log^{-2}t),\qquad \tfrac12(S_X^2)'=\sum_\omega c_\omega e^{i\omega\tau},$$
a nonzero trigonometric polynomial divided by $\log t$. Then $|D^{(1)}_X|\gg|\mathscr E_X^{-1}|\,|P^-(t)|/\log t$ on a set of positive density and $J^{(1)}_X=\infty$; the symmetric Perron integral of $D^{(1)}_Xx^s/s$ fails to converge at $x=d\,e^{-\omega}$, $d\mid P(X)$. Hypothesis `eq:JMfixed` is false for that list.

---

## Estado

- Theorem A: completo; el paso 3 (dominación uniforme en $r$) queda hecho sumando en $m$ dentro de la banda. Input externo: [v26, Lemma TR-smooth].
- Theorem N, Theorem C, Corolario: completos (notas `2026-10-25_JX_Newton_completo.md` y esta).
- No se afirma nada uniforme en $X$: la constante del Corolario depende de $X$ (y crece al menos con $t_0(X)\asymp e^{c\sqrt X}$, nota `2026-10-25_v19_cota_Mc_y_M_que_falta.md`, §4).
