# Literatura: quién ha intentado la ruta "ordenadas repetidas ⇒ en la recta y simples" y quién tiene el $1/12$

Nota de Claude, 25-oct-2026. Cotejado en la biblioteca (122, 018, 113, 114, 241). Sin ejecuciones numéricas.

## 1. Quién ha intentado eso

**Goldston–Lee–Schettler–Suriajaya, *Pair Correlation Conjecture I: simple and critical zeros*, arXiv:2503.15449 (v4, 30-mar-2026) — biblioteca 122.** Es el antecedente directo, y hay que citarlo.
- Definen la **multiplicidad horizontal** $H(\gamma)=\#\{\rho':\gamma'=\gamma\}$ (idea que atribuyen a Soundararajan): exactamente nuestro $m_\gamma$, la multiplicidad total sobre la recta horizontal $t=\gamma$, contando todas las abscisas. $N^\circledast(T)=\sum_\rho H(\gamma)=\sum_{\gamma\ \rm distintas}m_\gamma^2$.
- **HMH:** $N^\circledast(T)=(1+o(1))TL$, es decir $\sum_\gamma m_\gamma(m_\gamma-1)=o(N(T))$.
- **Teorema 2:** HMH ⇒ 100 % de ceros simples y en la recta. Prueba: $\#\{\text{simples y críticos}\}\ge\sum_\rho(2-H(\gamma))=2N-N^\circledast$. Es decir, $B_T\le N^\circledast-N=\sum_\gamma m_\gamma(m_\gamma-1)$.
- **Teorema 1:** PCC (sin RH) ⇒ HMH, por el método de Gallagher–Mueller 1978: el segundo momento $\int_0^T(\Delta_UN)^2dt$ se evalúa de dos maneras, por $S$ (Fujii) y por pares de ceros, y la comparación aísla $UN^\circledast$.
- **Remark 4:** con $N^\circledast\le(C+o(1))TL$, $1\le C<2$, salen proporciones parciales (Goldston–Suriajaya, arXiv:2511.20059, no está en la biblioteca).

**Comparación con el teorema de bloques (v15–v19) y la descomposición (v16).** La mitad "de conteo" de nuestro teorema está en GLSS: ordenadas repetidas ⇒ fuera de la recta o múltiples; eso es prioridad suya (marzo de 2025). Las constantes: GLSS dan $B_T\le\sum m(m-1)$; nosotros $B_T\le4\mathsf V_T=\frac13\sum m(m^2-1)$. Para $m=2$ coinciden (2 por bloque); para $m\ge3$ la de GLSS es mejor. **Lo que es nuevo en lo nuestro:** (i) la cota se expresa con una función $F$ construida sin ceros, $B_T\le4\sum u_k(F)^2$, de modo que la hipótesis pasa de PCC/HMH (estadística de pares de ceros) a un **único segundo momento** del defecto ordinal, $E_T(F)<\tfrac14$; (ii) la descomposición exacta $\sum u^2=\mathsf A_T(F)+\mathsf V_T$ con $\mathsf V_T=\frac1{12}\sum m(m^2-1)$, que separa reloj y multiplicidad; (iii) la identidad integral con el $1/12$. En v20 hay que citar GLSS y GM78 y decir exactamente esto.

**Gallagher–Mueller 1978**, J. reine angew. Math. 303/304, 205–220 (no está en la biblioteca; citado por GLSS): el dispositivo de los dos cálculos de $\int(\Delta_UN)^2$, con $\int(\Delta_UN)^2=UN^\circledast+2\int_0^UN(T,u)du+O(L^2)$ (GLSS (5.3)–(5.4)). Es el análogo de nuestra identidad: su término $UN^\circledast$ es nuestro $\mathsf V_T$, y su $\int(\Delta_US)^2$ es nuestro $\int(N-F)^2dF$.

**Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh 2025, arXiv:2501.14545 — biblioteca 018.** Método de pares de Montgomery bajo "caja estrecha" ($|\beta-\tfrac12|\le b/\log T$, $b\to0$): 2/3 simples, 2/3 en la recta, 1/3 simples y en la recta. Recogen los récords: PRZZ 2020, **41.72 %** en la recta y **40.75 %** en la recta y simples; Heath-Brown 1979 y Selberg, 34.74 % simples y en la recta. (Corrige mi cifra 41.73 → 41.72; el umbral de bloques pasa de 0.145675 a 0.1457.)

## 2. La constante de segundo orden: el mismo muro

GLSS, Prop. 2 (Fujii 1974/1981, Tsang 1984/1986): $\int_0^T(\Delta_US)^2dt=\frac{T}{\pi^2}\log(2+UL)+O\bigl(T\sqrt{\log(2+UL)}\bigr)$, incondicional. El error $O(T\sqrt{\log})$ es el mismo que en el Thm main de v14 ($C(1+\sqrt{\log(1/c)})$) y el que impide pasar de $1-4E_T$ a un porcentaje. GLSS lo esquivan porque **asumen** PCC, que fija el lado de los pares exactamente. Nuestra ruta no asume nada y por eso necesita la constante. Bajo RH, Goldston 1987 (*On the function $S(T)$…*, J. Number Theory 27; no está en la biblioteca) da esa constante con $\int_1^\infty F(\alpha)\alpha^{-2}d\alpha$. Sin RH nadie la tiene.

## 3. Quién demostró el $1/12$

- **El $1/12$ exacto como término de la identidad discreta–continua, $\sum u_k^2=\int(N-F)^2dF-\frac{n}{12}-\text{borde}$, es del autor:** v14 Thm `identity_general` ($\Psi_1(u)=u^2+\frac1{12}$) y v16 Thm `exact-counting-integral` (extremos arbitrarios, saltos incluidos). No lo he encontrado en la biblioteca en esa forma.
- El número es $\int_0^1(x-\tfrac12)^2dx=\frac1{12}$, la varianza del diente de sierra; en la literatura clásica aparece en la fórmula de Euler–Maclaurin y en las estimaciones de $\sum\psi(x)$, no como término de un segundo momento de ceros.
- En Gallagher–Mueller el papel equivalente lo hace el término $UN^\circledast$ de la expansión de $\int(\Delta_UN)^2$ por pares; es el mismo fenómeno (parte discreta frente a continua), sin el $1/12$ porque usan diferencias finitas $\Delta_U$ en lugar de la función $F$.
- Fujii 1975 (Proc. Japan Acad. 51, biblioteca 114) y Fujii 1981 (biblioteca 116) tienen los momentos de diferencias de $r$ ordenadas consecutivas y de $S(t+h)-S(t)$; no la identidad.

## 4. Consecuencia para v20

1. Citar GLSS (arXiv:2503.15449) y GM78 en el teorema de bloques y en la descomposición: la multiplicidad horizontal y la implicación "repetidas ⇒ fuera o múltiples" son suyas; la constante $4$ es óptima para la cota cuadrática con $F$, pero para $m\ge3$ su cota lineal $\sum m(m-1)$ es mejor y conviene enunciar las dos.
2. Corregir 41.73 % → 41.72 % (PRZZ 2020) y el umbral a $(1-0.4172)/4=0.1457$.
3. La frase honesta sobre el estado: lo que GLSS obtienen bajo PCC nosotros lo obtendríamos bajo $E_T(F)\to0$; ambas hipótesis chocan con la misma constante de segundo orden de Fujii/Selberg.
