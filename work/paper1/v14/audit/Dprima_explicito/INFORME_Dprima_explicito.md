# Teorema D′ explícito: la cuenta (21 oct 2026)

## Entradas y versiones explícitas existentes
- Aproximación de Selberg en $L^{2k}$, incondicional y explícita: Simonič–Trudgian–Turnage-Butterbaugh, Trans. AMS 375 (2022), Teorema 5 (arXiv:2010.10675; leído en v1). Vale para $T\ge\max\{x_0^{k/\varepsilon},2T_0\}$ con $\varepsilon\le1/88$, $x_0\ge e^{16}$ y $T_0\ge\frac12e^{1408}$, es decir $T\ge e^{1408k}$.
- Momentos de $S(t+h)-S(t)$: STTB22, Teorema 6 ($k=1,2$); Zhao, arXiv:2603.17334, Prop. 10 (todo $k$, con $T_0$ no declarado; se deduce de STTB22).
- Montgomery–Vaughan (constante de Preissmann), Mertens (Rosser–Schoenfeld) y la función maximal (Grafakos–Montgomery-Smith): explícitos, sin problema.
- Detalle: literatura_web.md y literatura_biblioteca.md.

## Constante de STTB22 (fórmula cerrada (17)–(21), $L=642.86$, $x_0=e^{16}$; sttb22_C.py)

| $k$ | $C(1/88,k,e^{16})$ | umbral |
|---|---|---|
| 2 | $2.25\cdot10^{19}$ | $T\ge e^{2816}$ |
| 3 | $3.64\cdot10^{27}$ | $T\ge e^{4224}$ |
| 4 | $3.59\cdot10^{37}$ | $T\ge e^{5632}$ |

Comprobación: con $x_0=e^{20000}$ la fórmula da $1.29\cdot10^{11}$ y $1.57\cdot10^{18}$ para $k=1,2$, por debajo de las cotas $1.44\cdot10^{11}$ y $2.70\cdot10^{21}$ de su Corolario 2.

## Propagación por la prueba de D′ (orden de magnitud; propagacion.py)
Se conservan solo los términos dominantes: el resultado es una estimación de la constante final, no una cota certificada.
- Prueba tal como está, con octavos momentos en el Lema slope_envelope: $T_0\ge e^{5632}$, $C_{\rm r}\approx1.2\cdot10^{44}$, error en $L^4$ de unos $3\cdot10^{11}$ espaciados medios.
- Variante con sextos momentos, usando $(z-j/4)_+^4\le16z^6/j^2$ (cambio de prueba no aplicado): $T_0\ge e^{4224}$, $C_{\rm r}\approx3\cdot10^{32}$, error de unos $4\cdot10^8$ espaciados medios.
- Comparación con la cota trivial del reloj sin corregir, $|\delta_k|\le0.6331$, que en espaciados es $0.6331\cdot\frac{\log T}{2\pi}$. D′ explícito solo la mejora si $\log T\gtrsim4\cdot10^9$ (variante) o $\log T\gtrsim3\cdot10^{12}$ (tal como está).

## Conclusión
D′ se puede hacer explícito con la literatura existente, pero el teorema resultante es peor que la cota trivial para todo $T$ por debajo de $e^{4\cdot10^9}$, aproximadamente. No da números utilizables a alturas calculables. El cuello de botella es la constante de la aproximación explícita de Selberg: su término principal es $(12a_2k/\varepsilon)^{2k}/6$, con $\varepsilon=1/88$ y $a_2\approx14$. Según STTB22, ni siquiera RH ($L=0$) la mejora de forma significativa. Bajar de ahí exige una aproximación explícita de Selberg nueva y mucho más fina: es un problema de investigación, no una revisión.
