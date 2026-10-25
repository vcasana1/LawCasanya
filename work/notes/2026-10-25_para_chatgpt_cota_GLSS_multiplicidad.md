# → chatgpt: cota de multiplicidad de Goldston–Lee–Schettler–Suriajaya para la próxima versión de CasanyaLawI

Nota de Claude, 25-oct-2026, a petición del autor, para incorporar en la próxima versión (ChatGPT redacta; Claude no toca el manuscrito). Cotejado en la biblioteca: n.º 122.

## Referencia

D. A. Goldston, J. Lee, J. Schettler, A. I. Suriajaya, *Pair Correlation Conjecture I: simple and critical zeros*, arXiv:2503.15449 (v4, 30-mar-2026).

## Enunciado (su Teorema 2, con nuestra notación)

$m_\gamma$ = multiplicidad horizontal de la ordenada $\gamma$ (número de ceros $\rho$ con $\Im\rho=\gamma$, todas las abscisas; GLSS la llaman $H(\gamma)$). Con
$$N^\circledast(T)=\sum_{\rho}H(\gamma)=\sum_{\gamma\ \text{distintas}}m_\gamma^2,$$
$$\#\{\rho:\ \rho\ \text{simple y }\Re\rho=\tfrac12\}\ \ge\ 2N(T)-N^\circledast(T),\qquad\text{equivalentemente}\qquad B_T\le\sum_\gamma m_\gamma(m_\gamma-1),$$
donde $B_T$ = número de ceros de la ventana que no son simples y críticos.

## Comparación con el teorema de bloques actual

Nuestro teorema da $B_T\le4\mathsf V_T=\frac13\sum_\gamma m_\gamma(m_\gamma^2-1)\le4\sum_ku_k(F)^2$.

Para todo $m\ge2$: $m(m-1)\le\frac{m(m^2-1)}3$ (equivale a $m+1\ge3$), con igualdad solo en $m=2$. Por tanto
$$B_T\ \le\ \sum_\gamma m_\gamma(m_\gamma-1)\ \le\ 4\mathsf V_T\ \le\ 4\sum_k u_k(F)^2 .$$

**Propuesta de texto:** enunciar la cadena completa. La primera desigualdad es de GLSS (Teorema 2) y se cita así; las dos siguientes son nuestras (descomposición exacta $\sum u^2=\mathsf A_T(F)+\mathsf V_T$ con $\mathsf A_T\ge0$). Para $m\ge3$ la cota de GLSS es estrictamente mejor (crece como $m^2$, no como $m^3$); la nuestra aporta que la cota final se expresa con una $F$ construida sin ceros.

## Otros puntos de atribución en el mismo sitio

- La implicación "ordenadas repetidas ⇒ fuera de la recta o múltiples" y la noción de multiplicidad horizontal son de GLSS (y la idea de $H(\gamma)$ la atribuyen a Soundararajan).
- Su Teorema 1 (PCC ⇒ $N^\circledast\sim N$) usa el método de Gallagher–Mueller 1978 (J. reine angew. Math. 303/304, 205–220): el término $UN^\circledast$ de $\int(\Delta_UN)^2$ es el análogo de nuestro $\mathsf V_T$.
- Récords citados por ellos (y en Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh 2025, n.º 018): PRZZ 2020, 41.72 % en la recta, 40.75 % simples y en la recta. Bajo RH, Bui–Heath-Brown: al menos 19/27 ≈ 70.37 % simples (arXiv:1302.5018; dato aportado por ChatGPT, no cotejado en la biblioteca).
