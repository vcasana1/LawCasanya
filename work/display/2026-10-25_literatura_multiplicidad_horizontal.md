# Quién ha intentado la ruta "ordenadas repetidas ⇒ en la recta y simples" y quién tiene el $1/12$ (respuesta literal de Claude, 25-oct-2026)

Nota completa: `work/notes/2026-10-25_literatura_multiplicidad_horizontal_y_un_doceavo.md`.

Hay un antecedente directo en la biblioteca y hay que citarlo.

**Quién ha intentado eso.**

- **Goldston–Lee–Schettler–Suriajaya, *Pair Correlation Conjecture I: simple and critical zeros*, arXiv:2503.15449 (v4, marzo 2026), biblioteca 122.** Definen la **multiplicidad horizontal** $H(\gamma)=\#\{\rho':\gamma'=\gamma\}$, idea que atribuyen a Soundararajan: es exactamente nuestro $m_\gamma$. Su Teorema 2: si $\sum_\rho H(\gamma)=(1+o(1))TL$ (HMH), el 100 % de los ceros son simples y están en la recta, porque
  $$\#\{\text{simples y críticos}\}\ \ge\ \sum_\rho\bigl(2-H(\gamma)\bigr),\quad\text{es decir}\quad B_T\le\sum_\gamma m_\gamma(m_\gamma-1).$$
  Su Teorema 1: PCC sin RH ⇒ HMH, por el método de Gallagher–Mueller 1978 (dos cálculos de $\int(\Delta_UN)^2$: por $S$ con Fujii, y por pares de ceros). Su Remark 4: con $N^\circledast\le(C+o(1))TL$ salen proporciones parciales (Goldston–Suriajaya, arXiv:2511.20059, no está en la biblioteca).

- **Comparación con lo nuestro.** La mitad de conteo del teorema de bloques, "ordenadas repetidas ⇒ fuera de la recta o múltiples", es suya y anterior (marzo 2025). Para $m=2$ las cotas coinciden; para $m\ge3$ la suya, $\sum m(m-1)$, es mejor que nuestra $\tfrac13\sum m(m^2-1)$. Lo nuevo en lo nuestro: la cota se escribe con una función $F$ sin ceros, $B_T\le4\sum u_k(F)^2$, de modo que la hipótesis pasa de PCC a un único segundo momento $E_T(F)<\tfrac14$; la descomposición exacta $\mathsf A_T(F)+\mathsf V_T$; y la identidad integral con el $1/12$.

- **Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh 2025, biblioteca 018:** correlación de pares bajo "caja estrecha" ($|\beta-\tfrac12|\le b/\log T$), 1/3 simples y en la recta. Recogen los récords: PRZZ 2020, **41.72 %** en la recta y **40.75 %** en la recta y simples. Corrige mi 41.73: el umbral de bloques es $(1-0.4172)/4=0.1457$.

**El mismo muro.** GLSS usan la Prop. 2 (Fujii 1974/81, Tsang 1984/86): $\int_0^T(\Delta_US)^2=\frac{T}{\pi^2}\log(2+UL)+O(T\sqrt{\log(2+UL)})$. Ese $O(T\sqrt{\log})$ es exactamente el error del Thm main de v14 y lo que impide pasar de $1-4E_T$ a un porcentaje. Ellos lo esquivan porque asumen PCC, que fija el lado de los pares. Bajo RH la constante la tiene Goldston 1987 (no está en la biblioteca); sin RH, nadie.

**Quién demostró el $1/12$.** En la forma que usamos, como término exacto de la identidad discreta–continua
$$\sum u_k^2=\int(N-F)^2\,dF-\frac{n}{12}-\text{borde},$$
**es del autor**: v14 Thm `identity_general` ($\Psi_1(u)=u^2+\tfrac1{12}$) y v16 Thm `exact-counting-integral`. No está en la biblioteca en esa forma. El número es la varianza del diente de sierra, $\int_0^1(x-\tfrac12)^2dx$; en Gallagher–Mueller el papel equivalente lo hace el término $UN^\circledast$ de su expansión por pares, sin $1/12$ porque usan diferencias finitas en vez de una función $F$. Fujii 1975 (biblioteca 114) tiene momentos de diferencias de $r$ ordenadas consecutivas, no la identidad.

**Para v20:** citar GLSS y GM78 en el teorema de bloques y en la descomposición; enunciar las dos cotas (la lineal de GLSS y la cuadrática con $F$); corregir 41.73 → 41.72 y el umbral a 0.1457; y decir que lo que GLSS obtienen bajo PCC nosotros lo obtendríamos bajo $E_T(F)\to0$, y que ambas chocan con la misma constante de segundo orden.
