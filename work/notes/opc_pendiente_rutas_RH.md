# ordinal_prime_cutoff — material pendiente para una versión futura: rutas más allá de la media cuadrática

Estado: guardado el 2026-10-18 por orden de Doktor ("incluye esas rutas para una futura version"). No crear versión hasta que lo ordene.

## Regla de nombres (orden de Doktor, 2026-10-18)

- **"Ley de Casaña" / "Casaña law"** (en LaTeX `Casa\~na law`) queda **reservada** para el método completo: el que, partiendo de $\tau_k$, llega a $\gamma_k$ de la forma más exacta posible, idealmente exacta. No usarla para resultados parciales ni para la alternancia de signo de $Z$.
- La alternancia $Z(m_{k-1})Z(m_k)<0$ en los puntos medios del reloj corregido se llama **corrected Gram law** (ley de Gram corregida); pregunta `q:corrected_gram_law`.
- Los ficheros y la construcción numérica concreta siguen llamándose zCasanya / Casanya (configuración (8,8,512)); eso es el nombre del dato, no la ley.

## SÍNTESIS PARA LA PRÓXIMA VERSIÓN (conclusiones consolidadas, 2026-10-18; aplicar solo cuando Doktor lo ordene)

Esta síntesis manda sobre las notas acumuladas más abajo, que quedan como material de trabajo.

### 1. Conclusión central
La aproximación del reloj corregido tiene tres defectos distintos, gobernados por objetos distintos; ninguna regla de cortes que optimice uno controla automáticamente los otros:
- **Energía (RMS de ordenadas):** el defecto de los primos no usados, $u_k(X)$; Teorema B.
- **Alternancia (huecos, factor de forma cerca de $\alpha=\tfrac12$):** el borde $1-c$ del espectro plegado; con $X=\sqrt{\tau/2\pi}$ (Nyquist) cae en $\tfrac12$.
- **Deriva del paseo $\sum e^{ix_k}$ (centroide):** la parte cuadrática de $e^{-iD}$: saltos estacionarios de las frecuencias producto $n=q r\approx e^{\pm1}\tau/2\pi$ y cuasirresonancias lentas de las frecuencias cociente $q/r\approx e^{\pm1}$.

### 2. Resultados exactos e incondicionales (entran como lemas/teoremas, sin ceros)
1. **Monotonía certificada.** $B(X)=\sum_{n\le X}\Lambda(n)n^{-1/2}<\tfrac12\inf_{t\in I}\log(t/2\pi)$ ⇒ $F_X$ estrictamente creciente en $I$, a lo sumo una raíz de $F_X=k-\tfrac12$. Versión con margen $\eta$. Kronecker: óptima para corte fijo.
2. **Raíz certificada.** En una región con $F_X'\ge d_k>0$: $|x-x^*|\le|F_X(x)-(k-\tfrac12)|/d_k$; bisección elimina el residuo de Newton $E^{(m)}$.
3. **Continuación sin cambio de rama** (homotopía $F_\lambda=(1-\lambda)F_X+\lambda F_Y$): si $F_X',F_Y'\ge d$ en $I$ y los signos en los extremos son correctos, rama única con $dx/d\lambda=-(S_Y-S_X)/F_\lambda'$ y $|x(1)-x(0)|\le\sup_I|S_Y-S_X|/d$. La condición es local en $I_k$ y se certifica con aritmética de intervalos de la suma finita.
4. **Identidad del residuo:** $N_0(\gamma_k)-N_0(x_k)=\bigl(S_X(x_k)-S_X(\gamma_k)\bigr)-u_k(X)-E_k$.
5. **Descomposición del defecto de centroide** respecto de $\gamma$ (angular $A_N$ / radial $B_N$) y respecto del reloj (lineal / cuadrática / orden superior).
6. **Descomposición producto/cociente:** con $H_X(t)=\sum_{q\le X}a_qe^{it\log q}$, $a_q=1/(\pi m\sqrt q)$: $-\tfrac12D_1^2=\frac{\Re H_X^2}{4\lL^2}-\frac{|H_X|^2}{4\lL^2}$; frecuencias $1\pm\log(qr)$ y $1\pm\log(q/r)$.
7. **Saltos de fase estacionaria** (a escribir con cotas de error vía Theorem known_vdC2): término $b_ne^{-i\tau\log n}$ ⇒ salto $|b_n|\lL\sqrt{2\pi\tau}$ en $\tau_n=2\pi e^{\mp1}n$, anchura $\lL\sqrt{2\pi\tau}$ índices; primer orden: $e^{-1/2}/m$; pares: $1/(\sqrt e\log(\tau/2\pi))$ y $\sqrt e/\log(\tau/2\pi)$. **Lema:** con $X\le\sqrt{\tau}$ no hay resonancias de primer orden ($e\tau/2\pi>\sqrt\tau$).
8. **Cuasirresonancias cociente:** periodo ordinal $P_{q,r}=\log(T/2\pi)/|1\mp\log(q/r)|$ (19/7: ≈7700; 11/4: ≈970; 8/3: ≈590 en $T=5\cdot10^5$); contribución exacta calculable $R_{q,r}(N)=-\frac{a_qa_r}4\sum_k w_{k,N}e^{i\tau_k(1+\log(q/r))}\lL(\tau_k)^{-2}$ y banda lenta $R_N^{\rm slow}(\delta)$. Ningún cociente es exactamente $e$; para corte fijo cada modo oscila acotado; el problema aparece cuando los cortes crecen y producen cocientes cada vez más próximos a $e$.
9. **Nyquist:** $X=\sqrt{\tau/2\pi}\iff\alpha=\tfrac12$.

### 3. Regla analítica de cortes por índice (sustituye a la selección empírica (8,8,512))
- Etapa A: $X_{\rm mon}(k)$ por el criterio 1 con margen, raíz por bisección (sin número de pasos que elegir).
- Etapa B: continuación certificada (resultado 3) hasta $Y_{\max}(k)=(\tau_k/2\pi)^{c_\varphi}$, $c_\varphi=\sqrt{2\log2}/(2\pi\tilde\sigma)$; si la certificación falla en $I_k$ se para en el último corte certificado (sin capturas; solo ganancia no obtenida).
- $(8,8,512)$ queda en el paper solo como experimento inicial, declarado como selección por validación.
- Estado: la regla es explícita y no usa ceros; su ventaja sobre (8,8,512) no está comprobada. Requiere el programa en el apéndice y comparación en el 30 % final intacto antes de redactarla como método.

### 4. Modelo (se enuncia como modelo, no como teorema)
- Ganancia gaussiana por término $\frac{w_n}{2\pi^2}(2\varphi_n-1)$, $\varphi_n=\exp(-2\pi^2\tilde\sigma^2(\log n/\ell)^2)$; corte $c_\varphi$.
- Recurrencia $W_j=2\log(1/c_j)+c_j^2W_{j-1}$, dos ramas ($1+\log W$; $2\log2+W/4$), suelo $V_*=2\log2/(3\pi^2)\approx0.047$. Lo medido (≈0.006) está por debajo: la anticorrelación transporte–defecto es esencial y no está explicada (problema abierto declarado).
- La probabilidad de captura requiere la covarianza $K_X(h)=\frac1{2\pi^2}\sum_{n\le X}\frac{\Lambda(n)^2}{n}\cos(h\log n)$; se evita con la certificación determinista.

### 5. Hipótesis (sección de pendientes, sin presentarlas como demostradas)
- Alternancia: (a) residuo $E^{(m)}$ modulado por $S_X'$ (bandas $1-c\pm\alpha_q$); (b) factor $(1+S_X'/\lL)^{-1}$; (c) aliasing de la cola. Demostrada la localización de frecuencias candidatas, no sus amplitudes. (a) se elimina con la raíz certificada; (b),(c) son la huella del corte y solo desaparecen al cruzar Nyquist (por índice, donde la continuación se certifica) y, del todo, cuando $u\to0$.
- Deriva lenta: las cuasirresonancias cociente explican las excursiones con retorno; los saltos de productos no bastan (suma de 6858 saltos $2.70+9.34i$ frente a $11.20+16.94i$ observado sobre $\tau\ge2^{16}$, con cancelación 409→9.7 que amplifica errores de fase del 4 %).

### 6. Datos numéricos utilizables (solo con programa en el apéndice)
zCasanya (8,8,512): RMS 0.0440 frente a 0.1881; 86.8 % de índices mejorados; test intocado 0.0406; 962 cruces. Centroides: Zeta $0.7769+0.7678i$, RvM $0.0416+1.7575i$, Casanya $2.7412+17.7391i$. $iA_N=-0.3333+14.4893i$, $B_N=2.2977+2.4820i$. Respecto de RvM: lineal $-2.236-5.557i$, cuadrática $5.242+20.593i$, superior $-0.306+0.946i$. Saltos: 80 modos, cociente de amplitudes 0.963, error angular mediano 0.042 rad. Corrección angular máx. 0.0027 rad sin cambio de RMS. Cola 512–2048 añadida: RMS 0.0440→0.0568, cruces 962→3348. Espectros por bloque (picos 0.38–0.50). Autocorrelaciones del residuo −0.63, +0.32, −0.20.

### 7. Ley de Casaña (nombre reservado): objetivo, no teorema
$\gamma_k=\lim_{m\to\infty}\mathcal C_m(k,\tau_k;X_1(k),\dots,X_m(k))$, con $\mathcal C_m$ construido solo con el reloj y los primos. Abiertos: (i) continuación hasta cortes arbitrariamente grandes; (ii) convergencia del error ordinal a 0; (iii) identificación del límite con $\gamma_k$; (iv) cancelación del paseo como consecuencia, no como ajuste.

### 8. Cálculos previos a redactar (en este orden; ninguno ejecutado)
1. Periodograma de $E^{(3)}_k$ frente al de $r_k$ (decide (a)).
2. $R_N^{\rm slow}(\delta)$ y término cociente completo (Fratio) frente a la deriva observada.
3. Construcción con la regla de la sección 3 y comparación en el 30 % final intacto (RMS, huecos, alternancia, paseo).

## Dónde va

- Nueva subsección en Conclusions, inmediatamente después de `\subsection{What is missing for a complete prediction of the zeros from the clock}` (`subsec:missing`) y antes de `\subsection{Why a finer knowledge of $\tau_k-\gamma_k$ matters}`.
- Tres preguntas nuevas al final de `\subsection{Future work}` (después de `q:prime_bridge`).
- Cinco entradas bibliográficas nuevas (con DOI), y "pages cited" según la convención del manuscrito.
- Reglas de la versión: paper entregable, sin historia de versiones, sin mencionar revisores; lo no demostrado va como pregunta/pendiente, sin referencias a versiones.

## Requisitos previos para que el bloque sea correcto en la versión

1. Los datos de zCasanya (configuración (8,8,512), 962 cruces, RMS 0.0440 frente a 0.1881, correlaciones del residuo −0.63, +0.32, −0.20) solo pueden aparecer si el programa que los produce entra en el apéndice de programas (`zCasanya_build.py` + `reproduce_selected.py` + el análisis de residuos/paseos, portados a Python con la convención del paper). Si no se incluyen, quitar las frases marcadas `% DATA`.
2. Verificar en la fuente, antes de escribir la versión: Pratt–Robles–Zaharescu–Zeindler (proporción 5/12 > 41.7 %; DOI abajo, no comprobado en la biblioteca); Turing 1953 (DOI abajo, no comprobado en la biblioteca); França–LeClair 2015 ecuación del n-ésimo cero y su afirmación sobre unicidad de soluciones (está en la biblioteca: `103_Franca-LeClair_2015_Transcendental_Equations_Individual_Zeros_L_Functions_CNTP_Published.pdf`; localizar sección y página).
3. Berry 1988 ec. (13)–(21) y Bogomolny–Keating I/II/PRL: ya verificados en la biblioteca (`024_Berry_1988_…`, `028_…_1995_…_I_…`, `029_…_1996_Gutzwiller_…`, `030_…_1996_…_II_…`); citar páginas exactas al redactar.
4. Las afirmaciones del aliasing (frecuencia ordinal del primer primo omitido) son deducciones elementales; la predicción del pico del periodograma del residuo por bloque, α_pico = 1 − log X₃/log(τ/2π), no se ha comprobado numéricamente: en la versión, o se comprueba con un programa incluido o se enuncia como predicción.

## Bloque LaTeX (inglés, listo para insertar)

```latex
\subsection{Routes beyond the mean-square regime}
\label{subsec:routes}
Everything proved in this paper concerns the ordinates in mean square, and Proposition~\CGref{prop:envelope_equivalence} shows that pointwise control of any corrected clock is control of the extreme values of $S(t)$. A statement about the position of the zeros relative to the critical line needs a further ingredient. Three routes start from the results above; none is carried out here.

\paragraph{The arithmetic Newton path}
The iteration \CGeqref{eq:newton_iteration} defines, for each $m$, a point set $\{x^{(m)}_k\}$ computed from the clock and the primes alone,
\[
x^{(0)}_k=\tau_k,\qquad x^{(j)}_k=x^{(j-1)}_k-\frac{N_0(x^{(j-1)}_k)+S_{X_j}(x^{(j-1)}_k)-(k-\tfrac12)}{\lL(x^{(j-1)}_k)},
\]
whose distance to $\{\gamma_k\}$ is controlled by Theorem~\CGref{thm:uniform_iteration}. Two steps separate this path from the ordinates.

(i) \emph{From $O(1)$ to $o(1)$.} This requires cutoffs $X>T^{1/2}$ (item~3 of Section~\CGref{subsec:missing}). In that range the primes no longer act one at a time: the obstruction found in Theorem~\CGref{thm:computable_response} is the pair resonance $pq\approx T/2\pi$. In the semiclassical description of the zeros \cite{Berry1988,BogomolnyKeating1995,BogomolnyKeating1996PRL,BogomolnyKeating1996} the corresponding regime is the off-diagonal one, $\tau=r\log p/\log(E/2\pi)>\tau^*$ in the notation of \cite[(13)--(21)]{Berry1988}, where the contributions of pairs of primes are evaluated through the Hardy--Littlewood prime-pair conjecture and produce the GUE correlations \cite{BogomolnyKeating1996}. A Newton step beyond $T^{1/2}$ would therefore have to contain a term built on pairs of prime powers with Hardy--Littlewood weights, and not further single primes. Whether such a step reduces the mean square of Theorem~\CGref{thm:uniform_iteration} is open.

(ii) \emph{Identification of the end point.} With all primes, the fixed-point equation of the iteration is
\[
N_0(x)+\tfrac1\pi\arg\zeta(\tfrac12+ix)=k-\tfrac12,
\]
the equation of França and LeClair for the $k$-th zero \cite{FrancaLeClair2015}. For finite $X$ the number of solutions of $F_X(x)=k-\frac12$ beyond the first is the multiplicity function $\tilde n$ of Section~\CGref{sec:iteration}, controlled in mean square by Theorem~\CGref{thm:multiplicity_all}; $F_X=N_0+S_X$ ceases to be monotone as soon as $\sum_{p\le X}\log p/\sqrt p$ exceeds $\lL$, and the crossings of the corrected clock are the excess solutions. % DATA: (962 crossings for the dyadic clock with cutoffs (8,8,512) on the first 2\,001\,052 zeros)
The end point is identified when this excess tends to zero along the path.

\paragraph{The corrected Gram law}
Let $m_k=\frac12(x^{(m)}_k+x^{(m)}_{k+1})$. Say that the corrected clock satisfies the \emph{corrected Gram law} at $k$ if $Z(m_{k-1})Z(m_k)<0$; this is the analogue of Gram's law with the corrected clock in place of the Gram points. If the law holds for a proportion $p$ of the indices $k\in\IT$, then at least a proportion $p+o(1)$ of the zeros with $T<\gamma\le2T$ lie on the critical line and are separated by the points $m_k$. A proof of a positive proportion needs explicit constants in Theorem~\CGref{thm:uniform_iteration}, so that the final mean square is below $\frac1{16}$ in units of zeros, and a lower bound for $|Z(m_k)|$ of Selberg type \cite{Selberg1942}. Exceeding the proportion $\frac5{12}$ of \cite{PrattRoblesZaharescuZeindler2020} would be a new result; we do not know whether this is possible. The law also gives a variant of Turing's method \cite{Turing1953} with fewer exceptional blocks than Gram's law.

\paragraph{The excess-root function}
Let
\[
\mathcal E(X,T)=\#\{t\in(T,2T]:F_X(t)\in\mathbb Z+\tfrac12\}-\#\IT .
\]
$\mathcal E(X,T)=0$ for $X$ small, because $F_X$ is then increasing; $\mathcal E(X,T)>0$ in an intermediate range; and the limit staircase $N$ is monotone. If $\mathcal E(\cdot,T)$ were unimodal in $\log X$ with its maximum at the scale $\tau^*$ of \cite{Berry1988}, step~(ii) of the Newton path would reduce to the decrease of $\mathcal E$ above $T^{1/2}$, which is the pair regime of step~(i). We have neither a proof nor numerical evidence for this shape.

\paragraph{Aliasing of the cutoff}
A term $\sin(t\log n)$ sampled at the ordinates has ordinal frequency $\alpha_n=\log n/\log(\tau_k/2\pi)\pmod1$. The residual $r_k$ of a clock corrected with cutoff $X$ is dominated by the first omitted prime powers $n\gtrsim X$, of ordinal frequency $1-\log X/\log(\tau/2\pi)$ after folding; for $X=T^{1/2}$ this is close to $\frac12$. The residual therefore alternates in sign from one index to the next, and the windowed form factor of the corrected points shows a feature near $\alpha=\frac12$ that moves with the height. % DATA: (lag-1, 2, 3 autocorrelations -0.63, +0.32, -0.20 for (8,8,512))
The same resonance with the frequency of $e^{i\gamma_k}$ occurs for $n\approx\tau/2\pi e$ and displaces the centroid of the walk $\sum_{j\le k}e^{ix_j}$, although each phase $x_j-\gamma_j$ is small.
```

## Preguntas nuevas (al final de Future work)

```latex
\begin{question}\label{q:pair_newton}
Is there a Newton step with cutoff beyond $T^{1/2}$, built on pairs of prime powers with Hardy--Littlewood weights, whose mean square in Theorem~\CGref{thm:uniform_iteration} is $o(1)$?
\end{question}

\begin{question}\label{q:corrected_gram_law}
For which proportion of $k\in\IT$ does the corrected Gram law $Z(m_{k-1})Z(m_k)<0$ hold, and can a positive proportion be proved from Theorem~\CGref{thm:uniform_iteration} with explicit constants?
\end{question}

\begin{question}\label{q:excess}
What is the shape of the excess-root function $\mathcal E(X,T)$ as a function of $\log X/\log T$, and does it tend to zero along the arithmetic Newton path?
\end{question}
```

## Bibliografía nueva (con DOI)

```latex
\bibitem{Berry1988}
M.~V. Berry, Semiclassical formula for the number variance of the Riemann zeros, Nonlinearity 1 (1988) 399--407. \href{https://doi.org/10.1088/0951-7715/1/3/001}{https://doi.org/10.1088/0951-7715/1/3/001}.

\bibitem{BogomolnyKeating1995}
E.~B. Bogomolny, J.~P. Keating, Random matrix theory and the Riemann zeros I: three- and four-point correlations, Nonlinearity 8 (1995) 1115--1131. \href{https://doi.org/10.1088/0951-7715/8/6/013}{https://doi.org/10.1088/0951-7715/8/6/013}.

\bibitem{BogomolnyKeating1996PRL}
E.~B. Bogomolny, J.~P. Keating, Gutzwiller's trace formula and spectral statistics: beyond the diagonal approximation, Phys. Rev. Lett. 77 (1996) 1472--1475. \href{https://doi.org/10.1103/PhysRevLett.77.1472}{https://doi.org/10.1103/PhysRevLett.77.1472}.

\bibitem{BogomolnyKeating1996}
E.~B. Bogomolny, J.~P. Keating, Random matrix theory and the Riemann zeros II: $n$-point correlations, Nonlinearity 9 (1996) 911--935. \href{https://doi.org/10.1088/0951-7715/9/4/006}{https://doi.org/10.1088/0951-7715/9/4/006}.

\bibitem{PrattRoblesZaharescuZeindler2020}
K. Pratt, N. Robles, A. Zaharescu, D. Zeindler, More than five-twelfths of the zeros of $\zeta$ are on the critical line, Res. Math. Sci. 7 (2020), Paper No. 2. \href{https://doi.org/10.1007/s40687-019-0199-8}{https://doi.org/10.1007/s40687-019-0199-8}   % VERIFICAR (no está en la biblioteca)

\bibitem{Turing1953}
A.~M. Turing, Some calculations of the Riemann zeta-function, Proc. London Math. Soc. (3) 3 (1953) 99--117. \href{https://doi.org/10.1112/plms/s3-3.1.99}{https://doi.org/10.1112/plms/s3-3.1.99}   % VERIFICAR (no está en la biblioteca)

\bibitem{Selberg1942}
A. Selberg, On the zeros of Riemann's zeta-function, Skr. Norske Vid. Akad. Oslo I 1942, no. 10, 1--59.   % sin DOI; VERIFICAR
```

---

## Añadido (2026-10-18, también para la versión futura): deriva del paseo de los puntos corregidos

Material del análisis de Doktor (MATLAB, sin binarios modificados). Entra en la versión solo con programa incluido en el apéndice (portado a Python) para cada cifra; si no, solo las identidades.

### A. Descomposición exacta angular/radial del defecto de centroide (identidad, incondicional)
Con $\varepsilon_k=x_k-\gamma_k$ y $w_{k,N}=(N-k+1)/N$:
```latex
C_{x}-C_{\gamma}=\sum_{k\le N}w_{k,N}e^{i\gamma_k}\bigl(e^{i\varepsilon_k}-1\bigr)
= i\underbrace{\sum_{k\le N}w_{k,N}e^{i\gamma_k}\sin\varepsilon_k}_{A_N}
+\underbrace{\sum_{k\le N}w_{k,N}e^{i\gamma_k}(\cos\varepsilon_k-1)}_{B_N}.
```
Datos (8,8,512), N=2 001 052: $iA_N=-0.333329+14.489273i$, $B_N=2.297658+2.481961i$, suma $1.964329+16.971234i$ (cierre $2.4\cdot10^{-12}$); parte angular ≈ 85 % de la parte imaginaria. $B_N$ (módulo 3.38) no es despreciable: $\varepsilon_k^2$ contiene $\cos(\gamma\log(m/n))$ y resuena con $e^{i\gamma}$ si $m/n\approx e$.

### B. Identidad del residuo ordinal (sustitución directa; comprobada)
Con $E^{(m)}_k=N_0(x^{(m)}_k)+S_X(x^{(m)}_k)-(k-\tfrac12)$ (computable sin ceros), $s_k=k-\tfrac12-N_0(\gamma_k)$ (= la $s_k$ del paper salvo el término de curvatura $O(\delta_k^2/T)$) y $r_k=N_0(\gamma_k)-N_0(x^{(m)}_k)$:
```latex
r_k=\bigl(S_X(x^{(m)}_k)-S_X(\gamma_k)\bigr)-\bigl(s_k-S_X(\gamma_k)\bigr)-E^{(m)}_k .
```
Transporte − defecto directo $u_k(X)$ − residuo de la ecuación. Es la forma del paper (eq. recursion_identity) con el término $E^{(m)}$ explícito: el paso usa denominador $L$, no $L+S_X'$, así que tras $m$ pasos la ecuación no queda resuelta. Para cuasi-Newton, al primer orden
```latex
E^{(m)}_k\approx-\frac{S_X'(x^{(m-1)}_k)}{L(x^{(m-1)}_k)}\,E^{(m-1)}_k .
```

### C. Corrección angular de bloque (sin ceros)
Perturbación de fases con $\max_k|\tilde x_k-x_k|=0.0027$ que hace coincidir el paseo con el del reloj $\tau_k$ en los extremos de 489 bloques: centroide $2.741+17.739i\to0.063+1.782i$ (RvM: $0.0416+1.7575i$); RMS de alturas $0.04398855\to0.04398386$, error de huecos $h=1$ sin cambio, 962 inversiones sin cambio. Usa solo $\tau_k$: es legítima (no usa ceros), pero impone la geometría del reloj, no explica la causa aritmética. Mostrar en el paper como: el paseo detecta una componente coherente de amplitud $\sim10^{-3}$ invisible para el RMS.

### D. Resultado negativo: añadir la cola de primos 512–2048 aislada empeora
$x^{(3)}-(S_{2048}-S_{512})(x^{(3)})/L$: RMS $0.0440\to0.0568$, inversiones $962\to3348$, Im centroide $17.7\to28.2$. No es un cuarto paso de Newton (falta $E^{(3)}$). No se ha probado el cuarto paso auténtico con corte 512 ni con 2048.

### E. Espectro del residuo: la predicción del aliasing falla en lo fino
| bloque | 1−log512/log(τ/2π) | pico observado | correlación con plantilla de primos omitidos |
|---|---|---|---|
| 2^16–2^17 | 0.3483 | 0.3833 | 0.308 |
| 2^17–2^18 | 0.3922 | 0.4434 | 0.329 |
| 2^18–2^19 | 0.4305 | 0.4890 | 0.365 |
| 2^19–2^20 | 0.4643 | 0.4748 | 0.463 |
| 2^20–fin  | 0.4943 | 0.4969 | 0.511 |
Correlación global 0.416 (≈17 % de la varianza). Observaciones para la redacción:
1. La predicción usaba X=512 en todos los bloques, pero el corte diádico efectivo es √(2^⌊log₂τ⌋): 256 en 2^16–2^17, 362 en 2^17–2^18. Con el corte efectivo: 0.422, 0.428, 0.432, 0.464, 0.494. Tampoco ajusta.
2. Plegado: los primos omitidos $n>X$ tienen $\alpha_n\in(a,1)$, $a=\log X/\log(\tau/2\pi)$, que pliega a $(0,1-a)$. La masa de la cola está por **debajo** de $1-a$; un pico **por encima** de $1-a$ (tres primeros bloques) no puede venir de la cola. La explicación del pico cerca de ½ por la cola sola es incorrecta.
3. Hipótesis falsable, sin ceros: por B, $E^{(3)}\approx-(S_X'/L)E^{(2)}$; $S_X'$ está dominada por $p\lesssim X$ (frecuencia plegada ≈ $1-a$) y $E^{(2)}$ lleva las frecuencias de $X_2=8$ ($\alpha_q=\log q/\log(\tau/2\pi)$, $q\in\{2,3,4,5,7,8\}$; $\alpha_2\approx0.06$–$0.07$). Predicción: picos laterales en $1-a\pm\alpha_q$ en el periodograma de $E^{(3)}_k$, el desplazamiento observado (+0.035, +0.05, +0.06, +0.01, +0.003) del orden de $\alpha_2$ en los bloques bajos y decreciente donde $X_3$ satura. No comprobado.

### F. Orden de experimentos propuesto (ninguno ejecutado aún)
1. $E^{(3)}_k$: RMS, autocorrelaciones, periodograma por bloque diádico (comprueba E.3).
2. Residuo menos $E^{(3)}$ frente a la plantilla de primos omitidos.
3. Cuarto paso auténtico de Newton con corte 512 (completa la ecuación sin primos nuevos); después con 2048.
4. Mantener separados tres criterios: alturas, huecos, deriva del paseo.

### Bloque LaTeX sugerido (si entran A, B y C)
```latex
\paragraph{Phase coherence of the corrected points}
The mean square of Theorem~\CGref{thm:uniform_iteration} does not control the coherent part of the error at a fixed frequency. For the centroid of the walk $\sum_{j\le k}e^{ix_j}$ one has the exact decomposition
\[
C_{x}-C_{\gamma}=i\sum_{k\le N}w_{k,N}e^{i\gamma_k}\sin\varepsilon_k+\sum_{k\le N}w_{k,N}e^{i\gamma_k}(\cos\varepsilon_k-1),\qquad \varepsilon_k=x_k-\gamma_k,\ w_{k,N}=\tfrac{N-k+1}{N},
\]
and a weighted mean of $e^{i\gamma_k}(e^{i\varepsilon_k}-1)$ of order $10^{-5}$ displaces the centroid by $O(10)$ over $2\cdot10^6$ zeros. The residual of the corrected count splits exactly as
\[
N_0(\gamma_k)-N_0(x^{(m)}_k)=\bigl(S_X(x^{(m)}_k)-S_X(\gamma_k)\bigr)-u_k(X)-E^{(m)}_k,\qquad E^{(m)}_k=N_0(x^{(m)}_k)+S_X(x^{(m)}_k)-(k-\tfrac12),
\]
where $E^{(m)}_k$ is computable from the clock and the primes.
```

---

## Añadido (2026-10-18): elección analítica de los cortes (sustituir la selección por validación de (8,8,512))

Orden de Doktor: los cortes deben elegirse analíticamente, no por rejilla + validación con ceros.

Regla propuesta (sin parámetros ajustados; no probada numéricamente todavía):

1. Pasos monótonos. $X_{\rm mon}(\tau)=\max\{X:\ \sum_{n\le X}\Lambda(n)n^{-1/2}\le\tfrac12\log(\tau/2\pi)\}$. Es la condición suficiente para que $F_X=N_0+S_X$ sea estrictamente creciente cerca de $\tau$ ($|S_X'|\le\frac1\pi\sum_{n\le X}\Lambda(n)n^{-1/2}<\lL$); por Kronecker es también necesaria en rangos largos. Con ella: raíz única por índice, ningún cruce. Valores: 0 primos en $\tau<\approx 30$; $X=8$ desde $\tau\approx3570$; $X=16$ en $\tau=2^{19}$; $X=17$ en $\tau\approx1.1\cdot10^6$. Asintóticamente $X_{\rm mon}\sim(\tfrac14\log(\tau/2\pi))^2$, la escala $(\log T)^2$ de prop:envelope_equivalence.
2. Número de pasos monótonos: el transporte de cada paso multiplica la energía previa por $c_{\rm mon}^2=(\log X_{\rm mon}/\log(\tau/2\pi))^2\approx0.03$; con $V_0\approx\frac1{2\pi^2}\log\log T$, un paso deja $c^2V_0\approx4\cdot10^{-3}$ (del orden del error final), dos pasos $c^4V_0\approx10^{-4}$: dos pasos bastan, el tercero no aporta.
3. Paso grande: $X_3(\tau)=\lfloor\sqrt{\tau/2\pi}\rfloor$ (límite del Teorema B, $X^2\le T$; el óptimo del modelo de energía $c^*=1/(2\pi\sqrt{V_2})\approx0.5$ queda en el tope). Si se exige paseo sin resonancias de pares: $X_3=\lfloor\sqrt{\tau/2\pi e}\rfloor$.
4. La ley asintótica del paper ($c_1=H_0^{-1/2}$, $c_2=H_1^{-1/2}$, $c_j=C_\star H_{j-1}^{-9/16}$) tiene la misma forma creciente pero no es usable a $T\le10^6$ ($H_0\le2.6$, $c_2>1$, constantes $C_\star,H^*$ no calculadas).

Comparación con la selección empírica: (8,8) frente a $X_{\rm mon}\in[8,17]$ en el grueso del fichero; 512 frente a $\sqrt{\tau/2\pi}\approx289$–$420$ en $2^{19}$–$2^{20}$ (dentro de la resolución ×4 de la rejilla). Sobre-corrección observada de (8,8) en $16<\tau\le32$ (RMS 1.10 frente a 0.53): la regla 1 da $X<2$ allí.
Límite honesto: el modelo de energía sin correlaciones predice $\langle s^2\rangle\approx0.06$ tras el paso grande, frente a 0.006 medido; la anticorrelación transporte–defecto (Tabla transport) no está explicada, así que la regla 3 se apoya en el rango del Teorema B, no en una minimización cuantitativa.
Prueba pendiente (programa Python en apéndice): construir con la regla 1–3 y comparar con (8,8,512) en el 30 % final intacto.

### Corrección (orden de Doktor): la regla debe valer para todo k, no ajustada al rango del fichero
- Válido para todo $k$ (funciones explícitas de $\tau_k$, sin números del fichero): $X_{\rm mon}(\tau)$ y el tope $\sqrt{\tau/2\pi}$.
- Ley de energía para todo $k$ (modelo gaussiano, constantes explícitas): $W_j=4\pi^2V_j$, $W_0=2\log\log(\tau/2\pi)$, $c_j=\min(\tfrac12,W_{j-1}^{-1/2})$, $W_j=1+\log W_{j-1}$ mientras $c_j<\tfrac12$; pasos $m(\tau)=\log^*\tau+O(1)$. Es la ley del paper ($c_1=H_0^{-1/2}$, $c_2=H_1^{-1/2}$, exponentes $9/16$ por Hölder) con constantes explícitas.
- Conflicto: en $\tau=2^{19}$ esa ley da primer corte $(\tau/2\pi)^{0.45}\approx164$; la validación descartó primeros pasos grandes ((128,512) perdió frente a (8,512)). Causa propuesta: captura de raíz equivocada cuando el error de partida es una fracción grande del espaciado y $F_X$ no es monótona en $[x,\gamma]$ (colas pesadas, máx 1.36), fenómeno fuera del modelo $L^2$.
- Falta derivar (analíticamente, sin datos) la regla de transición: probabilidad de que $\lL+S_X'$ no cambie de signo en un intervalo de longitud $|e_{j-1}|$ (modelo gaussiano de Selberg para $S_X'$), y elegir $X_j$ maximizando ganancia de defecto menos pérdida por captura. Hasta entonces la regla para todo $k$ no está cerrada.

### Ecuación explícita de los cortes para todo k (versión a redactar)
Notación: $\ell=\log(\tau/2\pi)$, $w_n=\Lambda(n)^2/(n\log^2n)$, $\tilde\sigma_j$ = RMS del error tras el paso $j$ en unidades de ceros, $\theta=\log n/\ell$.
- Respuesta de un término de fase al error entrante (modelo gaussiano, cada primo pesa poco en el error): residuo del término $n$ tras un paso que lo incluye: $2\frac{w_n}{2\pi^2}(1-\varphi_n)$, $\varphi_n=\exp(-2\pi^2\tilde\sigma_{j-1}^2\theta^2)$; sin incluirlo: $\frac{w_n}{2\pi^2}$. Ganancia neta $\frac{w_n}{2\pi^2}(2\varphi_n-1)$.
- Ganancia del paso: $G_j(X)=\frac1{2\pi^2}\sum_{n\le X}w_n\bigl(2e^{-2\pi^2\tilde\sigma_{j-1}^2(\log n/\ell)^2}-1\bigr)$; máximo en $2\varphi=1$: $c_\varphi=\sqrt{2\log2}/(2\pi\tilde\sigma_{j-1})=0.1874/\tilde\sigma_{j-1}$.
- Captura: el transporte es reparable por pasos posteriores; caer en una raíz espuria de $F_X=k-\frac12$ no lo es. Raíces espurias solo si $F_X$ no es monótona. Por tanto: pasos no finales con $X_j\le X_{\rm mon}(\tau)$ (pérdida por captura nula); paso final $c_m=\min(\frac12,c_\varphi)$.
- Actualización: $\tilde\sigma_j^2=\frac1{2\pi^2}\bigl[\sum_{X_j<n\le\tau/2\pi}w_n+\sum_{n\le X_j}2w_n(1-\varphi_n)\bigr]$.
- Número de pasos monótonos: $n_0=\lceil\log\eta/(2\log c_{\rm mon})\rceil$, $c_{\rm mon}=\log X_{\rm mon}/\ell$, $\eta$ tolerancia relativa del punto fijo (no ajustada a datos); $n_0=2$ en $2^{19}$ con $\eta=10^{-3}$, $n_0\to1$ cuando $\tau\to\infty$.
- Rango: mientras $\tilde\sigma_{n_0}<\sqrt{2\log2}/\pi\approx0.375$ el paso final está en el tope $X=\sqrt{\tau/2\pi}$; con $\tilde\sigma^2\approx\frac1{2\pi^2}(\log\ell-\log\log X_{\rm mon})$ eso vale hasta $\tau\sim10^{30}$. Más arriba, cadena de pasos grandes con $c_j=c_\varphi(\tilde\sigma_{j-1})$ y restricción de captura $\Phi(-1/c_j)\le\eta$; asintóticamente $c_1\asymp(\log\log T)^{-1/2}$, la ley del paper.
- Contraste (resultados de validación ya existentes, región k 800421–1400736): un paso [8] 0.1234, [32] 0.0966, [128] 0.0774, [512] 0.0657; dos pasos [8,8] 0.1202, [512,512] 0.0634, [128,512] 0.0563, [8,512] 0.0426. Coherente con: paso grande primero deja capturas no reparables ([512,512] apenas mejora [512]); paso monótono primero reduce $\tilde\sigma$ de ≈0.33 a ≈0.22 (los primos 2–7 llevan ~la mitad de la varianza) y el paso final gana más.
- Pendiente: constante de muestreo en ceros (término −1/12 de eq:identity_LeClair y peso $L+S_X'$) en $\tilde\sigma$; la decisión "tope" es robusta a ella mientras $\tilde\sigma<0.375$. Construir zCasanya con esta regla y comparar en el 30 % final intacto.

### Alternancia del residuo (corr. −0.63, +0.32, −0.20): mecanismo y solución (2026-10-18)
- Tres fuentes, todas con frecuencia ordinal cerca de $1-c$, $c=\log X_{\rm final}/\ell$:
  (a) residuo de la ecuación no resuelta $E^{(m)}\approx-(S_X'/\lL)E^{(m-1)}$; la densidad espectral de $S_X'$ crece con $\alpha$ hasta el borde $\alpha=c$ (pesos $\log^2p/p$), plegada a $1-c\approx0.45$–$0.48$;
  (b) en la raíz exacta, $x^*-\gamma\approx u/(\lL+S_X')$: el factor $(1+S_X'/\lL)^{-1}$ modula el defecto con la misma frecuencia;
  (c) aliasing del propio defecto $u$ (primos $>X$, $\alpha\in(c,1)$, densidad $\propto1/\alpha$, plegado a $(0,1-c)$ con máximo en el borde $1-c$).
- Con el corte diádico efectivo ($256$, $362$, $512$, …) el borde $1-c$ vale 0.42, 0.43, 0.43, 0.47, 0.48 por bloque; observados 0.38, 0.44, 0.49, 0.475, 0.497. Acuerdo en los dos bloques altos; en los bajos falta (a) (bandas laterales $1-c\pm\alpha_q$).
- Solución en la arquitectura nueva: resolver la ecuación truncada exactamente (bisección / continuación) elimina (a) ($E\equiv0$). (b) y (c) son la huella del corte final: irreducibles a $c$ fijo (la raíz exacta es casi el estimador óptimo en media cuadrática, porque $u$ es desconocido), con amplitud $\sim c\sqrt{V_u}$; solo desaparecen cuando los cortes crecen y $u\to0$ (ley de Casaña completa).
- Predicciones sin ceros: tras resolver exactamente, desaparecen las bandas laterales y la autocorrelación a desfase 1 pierde magnitud; el pico restante se sitúa en $1-c(\tau)$.
- Deriva del paseo, término que faltaba: frecuencias cociente $q_i/q_j\approx e^{\pm1}$ son resonantes a toda altura ($\theta=1\mp\log(q_i/q_j)\approx0$), no saltos localizados: órbitas lentas de amplitud $\sim a_{q_i}a_{q_j}/(4\lL^2)\cdot\ell/(2\pi|\theta|)$. Ejemplos: $19/7$ ($\log=0.99853$, $\approx0.8$ de amplitud, periodo ≈7700 índices), $8/3$ (0.9808), $11/4$ (1.0116). Hipótesis: explican la parte de la deriva que no recogen los saltos de productos (comprobar con Fratio del código de Doktor).
- Revisión aceptada: dos pasos monótonos resuelven la misma ecuación (son convergencia a su raíz, no dos ganancias aritméticas) → sustituir por bisección certificada; la recurrencia gaussiana tiene segunda rama $W_j=2\log2+W_{j-1}/4$ con suelo $V_*=2\log2/(3\pi^2)\approx0.0468$ (el modelo no da convergencia exacta; lo medido, 0.0059, está por debajo: anticorrelación no modelada); la probabilidad de captura exige la covarianza $K_X$, no solo la varianza; el teorema de continuación (homotopía con $F'\ge d$) es correcto y la certificación de $F_Y'\ge d$ es local en $I_k$ (aritmética de intervalos de la suma finita), así que permite pasar de $X_{\rm mon}$ donde la pendiente local es positiva.

### Nyquist y la alternancia (2026-10-18, tras la nota de Doktor)
- $X=\sqrt{\tau/2\pi}$ es exactamente la frecuencia de Nyquist del reloj ($\alpha=\log X/\ell=\tfrac12$). Con el tope analítico $c=\tfrac12$ el borde del defecto plegado $1-c$ cae en $\tfrac12$: la alternancia es máxima justo en el tope. No es un defecto del método sino el precio de parar en Nyquist.
- Corregir con la cola vía continuación (4) equivale a subir el corte por encima de Nyquist (la raíz de $F_Y$ deja $r\approx u_Y/(1+S_Y'/\lL)$, borde en $1-c_Y<\tfrac12$).
- Ganancia: con $\tilde\sigma\approx0.22$ tras la raíz monótona, $c_\varphi=0.1874/\tilde\sigma\approx0.85$: el modelo pide pasar de Nyquist. Costes: fuera del Teorema B; fracción no monótona $\Phi(-1/c)$ (0.05 en $c=0.6$, 0.12 en $c=0.85$); resonancias de pares en el paseo.
- Regla por índice: con continuación certificada no hay capturas; si la certificación falla en $I_k$ se detiene en el último corte certificado y la pérdida es solo ganancia no obtenida. Por tanto $X_{\rm final}(k)=\sup\{Y\le(\tau_k/2\pi)^{c_\varphi}:\ \text{continuación certificada en }I_k\}$. Predicción: la alternancia queda solo en la fracción ≈$\Phi(-1/c)$ de índices no certificados y el pico se desplaza a $1-c_\varphi$.
- $n_0$ con $X_{\rm mon}=16$ en $2^{19}$ es 3, no 2 (yo usé $c$ de $X=8$); irrelevante con bisección.

## RESULTADOS DE LOS TRES CÁLCULOS (2026-10-18; programas en work/opc/v15_prep, opc_task1/2/3_*.py; salidas en outputs/)
Referencia de error: siempre $\gamma_k$ (zeta). RvM solo como herramienta intermedia (orden de Doktor).

1. **Residuo de Newton $E^{(3)}$ (todo el fichero).** RMS 0.106 (unidades de ceros), explica el 17 % de la varianza de $r_k$; espectros de $r$ y $E^{(3)}$ correlación 0.96–0.98 por bloque y mismos picos. Raíz exacta de la ecuación truncada con los mismos cortes (Newton con derivada completa, 99.996 % de índices): correlaciones del residuo −0.63/+0.32/−0.20 → −0.48/+0.08/−0.03; potencia en $[0.4,0.5]$ 0.58 → 0.38–0.44; cruces 962 → 0; el escalón espectral por encima de $1-c$ desaparece (era $E^{(3)}$). Coste: RMS altura 0.0440 → 0.0456, error de hueco $h=2$ 0.090 → 0.109. Conclusión: mecanismo (a) confirmado; la alternancia a desfase 1 que queda (−0.48) es (b)+(c).
2. **Deriva del paseo (descomposición exacta respecto del reloj, sin ceros).** Identidad producto/cociente exacta (error 3e-16). Modelo cuadrático $7.06+16.33i$ = producto $-2.32+10.72i$ + cociente $9.38+5.61i$; banda cociente lenta $|\theta|\le0.02$: $8.19+10.68i$. **Un solo par domina: $(71,193)$, $193/71=2.718310$, $|1-\log(193/71)|=1.03\cdot10^{-5}$, contribución $7.17+12.01i$ (módulo 14.0, frente a 16.2 de toda la deriva).** Siguientes: $19/7$ (1.92), $5/2$ (0.65), $8/3$ (0.34), $11/4$ (0.32), $443/163$ (0.25). $8/3,11/4,19/7,193/71$ son **convergentes de la fracción continua de $e$** cuyos dos términos son potencias de primo; el siguiente con esa propiedad es $49171/18089$ ($\theta\approx10^{-10}$). La forma lenta de la excursión (máximo $k\approx0.45\cdot10^6$, mínimo $\approx1.0\cdot10^6$) es la del par $(71,193)$ (periodo ≈1.1·10^6 índices). Como $|C_{\rm RvM}-C_\zeta|=1.23$, la misma resonancia separa Casanya de zeta (17.08): en zeta está compensada, en la construcción truncada no.
3. **Regla analítica (sin ceros, sin parámetros ajustados), test intacto $k=1\,400\,737$–$2\,001\,052$, todo respecto de $\gamma_k$:**

| método | RMS | p99 | máx | mejora vs reloj | hueco $h{=}1$ | corr. desfase 1 / 2 | cruces | potencia [0.4,0.5] | defecto centroide paseo | máx paseo |
|---|---|---|---|---|---|---|---|---|---|---|
| reloj RvM | 0.1774 | 0.440 | 0.689 | — | 0.409 | +0.26 / +0.04 | 0 | 0.12 | 1.11 | 2.86 |
| zCasanya (8,8,512) | 0.0406 | 0.116 | 0.313 | 86.9 % | 0.140 | −0.64 / +0.33 | 274 | 0.58 | 14.72 | 29.8 |
| A: raíz monótona ($X=16$) | 0.1046 | 0.257 | 0.410 | 69.2 % | 0.347 | −0.52 / −0.16 | 0 | 0.32 | 0.92 | 2.05 |
| R1: continuación a $\sqrt{\tau/2\pi}$ | 0.0473 | 0.123 | 0.284 | 85.0 % | 0.158 | −0.54 / +0.17 | 0 | 0.47 | 14.08 | 26.7 |
| **R2: continuación a $(\tau/2\pi)^{c_\varphi}$** | **0.0331** | **0.081** | 0.275 | **88.4 %** | **0.106** | **−0.40 / −0.01** | **0** | **0.35** | **7.75** | **17.6** |

R2: $c_\varphi$ mediano 0.696 (99.94 % de índices pasan Nyquist), continuación aceptada en ≥99.98 % por nivel, $\tilde\sigma$ modelo 0.269 frente a 0.199 real tras la etapa A (el modelo sobreestima, luego $c_\varphi$ queda corto). Certificación por muestreo (5 puntos, umbral $0.1L$), no aritmética de intervalos; constantes a priori: $\eta=0.1$, 6 niveles.
Conclusión: la regla analítica supera a la selección empírica en todas las medidas respecto de zeta: RMS −18 %, p99 −30 %, hueco −24 %, sin cruces, alternancia a desfase 2 eliminada, defecto del paseo a la mitad. El paseo sigue lejos del de zeta (7.75 frente a 1.11 del reloj): las cuasirresonancias cociente (convergentes de $e$) siguen dentro de los cortes.
