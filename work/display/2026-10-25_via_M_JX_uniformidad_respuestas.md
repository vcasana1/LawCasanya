# Vía M, 25-oct-2026: respuestas literales de Claude (v19, $J_X$, Newton, uniformidad)

Notas completas: `2026-10-25_v19_cota_Mc_y_M_que_falta.md`, `2026-10-25_JX_un_paso_diverge.md`, `2026-10-25_JX_Newton_completo.md`, `2026-10-25_texto_v20_PerronMfixed_incondicional.md`, `2026-10-25_uniformidad_X_igual_x_obstruccion.md`. El teorema completo está en `2026-10-25_teorema_PerronMfixed_incondicional_X_fijo.md` (display).

## A. v19: ¿tiene $M_C$ la cota $x^{1/2+\varepsilon}$? ¿y $M$?

| Objeto | ¿$\ll x^{1/2+\varepsilon}$? | Estado |
|---|---|---|
| $M_{C,X}$, $X$ fijo, lista de raíces exactas | Sí, para todo $x$, con constante que depende de $X$ | demostrado (Teoremas A y B) |
| $M_{C,X}$, $X$ fijo, lista de un paso $\tau_k^X$ (candidato de v19) | no | $J_X=\infty$ (B) |
| $M_{C,X}$ uniforme en $X\ge x$ | no | es RH en otra forma (D) |
| $M$ | $\ll x^{1/2+\varepsilon}\iff$ RH | Littlewood |

A $X$ fijo la cota existe porque $M_X^*$ es una suma finita ($|M_X^*|\le2^{\pi(X)}$, $=0$ para $x\ge P(X)$): es vacía para RH. La hipótesis `eq:JMfixed` de v19 está demostrada para la lista de raíces exactas (Teorema A). Faltan: redacción en v20 (candidato correcto), cuantificar $J_X$, corte $c\ge1$ con los dos canales de alias, o la alternativa por ordenadas (Teorema L).

## B. $J^{(1)}_X$ para la lista de un paso de v19: diverge

$\epsilon_k=\kappa^{(1)}_k-\kappa^{\rm ex}_k=-\frac{(S_X^2)'(\tau_k)}{2\Lambda^2}+O_X(\Lambda^{-3})$ (primer orden, porque el paso divide por $\Lambda$ y no por $N_X'$). Entonces
$$\Delta(s)-\Delta_\infty=-\frac{\pi i\,P^-(t)}{\Lambda(t)}+O_X(\log^{-2}t),\qquad P^-(t)=\sum_{\omega<0}c_\omega e^{\omega\sigma'}e^{i\omega t}\not\equiv0,$$
luego $|D^{(1)}_X|\gg|\mathscr E_X^{-1}||P^-|/\log t$ en medida positiva y $J^{(1)}_X=\infty$. Ninguna constante $\varpi$ lo arregla. El Perron simétrico no converge en $x=d\,q^{m'}/p^m$.

## C. El paso que funciona, prueba completa (sin Poisson)

$\kappa^N_k=\tau_k-S_X(\tau_k)/(\Lambda+S_X')(\tau_k)$. Taylor con resto: $\epsilon_k=\frac{h_k^2N_X''(\xi_k)}{2N_X'(\tau_k)}=\frac{S_X^2S_X''}{2\Lambda^3}(\tau_k)+O(\Lambda^{-4})$. Paridad: $S_X$ impar ⇒ $S_X^2S_X''$ y $S_X^2S_X''S_X'$ sin término constante. Identidad exacta $\Delta-\Delta_\infty=-\int\nu g_w$, $g_w=\frac1{\tau-w}+\frac1{\tau+\bar w}$; reducción a la lista exacta con $n^{\rm ex}=\lfloor N_X+\tfrac12\rfloor$; parte diente de sierra por partes; parte continua por $\int_{\mathbb R}\frac{e^{i\omega\tau}}{\tau-w}d\tau=-2\pi ie^{i\omega w}\mathbf1_{\omega<0}$. Resultado: $|\Delta-\Delta_\infty|\le C_2(X,\sigma')/\log^2t$, luego $J^N_X<\infty$ y $\varpi^N_XM^N_{C,X}(x)=M_X^*(x)+O(J^N_Xx^{1/2+\sigma'})$ para todo $x$.

Corrección a mi nota anterior: con cotas absolutas el resto $O(\Lambda^{-3})$ solo da $O(1/\log t)$; el $\log^{-2}$ sale de la cancelación por paridad.

## D. Uniformidad en $X=x$ y control independiente de $M^N_{C,x}(x)$: no, y por qué

1. Constantes: $\tau'(X)=\exp(cX^{1/2+Y})$ por el lema de banda; $J_{\rm low}$ sin cota demostrada; con $X=x$, $|\mathcal R_x|\le J_xx^{1/2+\sigma'}$ es vacío.
2. **Teorema E (T):** $|\log\mathscr E_X(s_0)|\le C$ para todo $X$, con $\Re s_0=\sigma_0>\tfrac12$, implica $\zeta\ne0$ en $\Re s>\sigma_0$ (sumación parcial ⇒ la serie de $\log\zeta$ converge en $\Re w>\sigma_0$). "Cotas uniformes para $X=x$" es RH en otra forma.
3. Aliasing (T en lo que afirma): $|w_X|=|\chi||\mathscr E_X(1-s)/\mathscr E_X(s)|(1+O(1/t))$, con $\log|\mathscr E_X(1-s)/\mathscr E_X(s)|$ de media cuadrática $\asymp X^{2\sigma'}/\log X$; para $X=x$, $|t|\le x^{1+\epsilon}$, $|w_x|\ge1$ en medida positiva. Allí $1/\zeta_{C,x}\not\approx\mathscr E_x^{-1}$ (Gonek 2012, p. 2169: $P_X+\chi\overline{P_X}$ solo con $X\lesssim\sqrt{t/2\pi}$).
4. Incompatibilidad (T): identidad friable ⇒ $X\ge x$; Perron ⇒ $U\ge x^{1+\epsilon}$ (y con $X\ge x$, $U\ge e^{cX^{1/2-\sigma'}}$); Teorema A ⇒ $t\ge e^{cX^{1/2+Y}}$. Ningún corte fijo cierra la vía; y con corte en altura $X(t)\lesssim\sqrt t$, los $n\le x$ nunca están dentro del corte a las alturas en que Perron los necesita.

Conclusión: a $X$ fijo, todo el Corolario es teorema; uniforme en $X$, nada, y está demostrado que nada puede salir de ahí sin información de ceros. La información tiene que entrar por las ordenadas.
