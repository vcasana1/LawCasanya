# Auditoría de CasanyaLawI_v18 (adjunto del autor)

Nota de Claude, 25-oct-2026. Comparación línea a línea con v16 (v17 no la he visto). Referencias cruzadas comprobadas. Sin compilar. Sin ejecuciones numéricas. Fujii 1974 cotejado sobre el PDF de la biblioteca (113), pp. 232–233.

## 0. Cambios respecto a v16

1. Hiperenlaces: `backref=page` y tooltips `\CASpreview` con `pdfcomment`. Cumple la configuración canónica del autor en lo esencial. DOI enlazados en los que ya había; **siguen faltando** los de Carleson 1966, Hunt 1968, Kinnunen 1997 y Fujii 1981.
2. Prueba reconstruida de la entrada de Selberg–Fujii (l. 420–477).
3. Los dos defectos de coherencia señalados en v15 **quedan corregidos**: título de la subsección de borde (l. 2955) y remisión explícita a `thm:C1` (l. 3009–3018); referencia de `thm:goodcount` a `thm:blockcount` (l. 2868–2873).
4. Nueva Prop. `prime-endpoint-range` y dos observaciones (l. 4044–4129).

## 1. Reconstrucción de Fujii (l. 420–477): correcta, cotejada

- Fujii 1974, p. 232: la fórmula de Selberg que imprime es
  $$S(t,\chi)-\frac1\pi\Im\sum_{p<x^3}\frac{\chi(p)}{p^{1/2+it}}=\sum_{i=1}^5O(B_i(t)),$$
  con $p^{1/2+it}$ en el término principal y $\sigma_x(t)$ solo dentro de los $B_i$. **La afirmación de v18 es exacta.**
- p. 233: $\|B_i\|\ll k^{c_i}H^{1/2k}$ para $i=1,\dots,5$ (con $c_i\in\{\tfrac12,2,\tfrac32\}$), $x=T^{a_2/60k}$, de donde $\|A_{x^3}\|\ll k^2H^{1/2k}$. Es decir, $\int_T^{T+H}|A_{x^3}|^{2k}\ll k^{4k}H$. **Correcto.** Observación: la constante de Fujii es explícita en $k$ ($k^{4k}$), no solo "$\ll_h$".
- La ampliación de $R_h=T^{1/(100h)}$ a $Y_h=T^{1/(80h)}$ por Montgomery–Vaughan: $V_h=\log\frac{100}{80}+O(1)$, longitud $Y_h^h=T^{1/80}<T$. Correcto.
- Las restricciones $T^{1/2+a_2}\le H\le T$, $q<T^{1/4-a_1}$: no cotejadas con el enunciado de la p. 225; son las de Fujii según recuerdo.

## 2. Prop. `prime-endpoint-range`: correcta

$|N-F_X|\ll\log T+\sqrt X/\log X+\log\log X$, de donde el término cúbico de borde es $o(M_T)$ si $X\le T^{2/3}$. Correcto. Coincide con lo que señalé en la auditoría de v16.

## 3. Rem. `no-unit-endpoint-selection`: tiene razón en lo que critica; la solución correcta es otra

Mi sugerencia (auditoría de v16) era elegir los extremos en $[T,T+1]$ y $[2T,2T+1]$ usando $\frac1T\int_T^{2T}G^2\ll\log\log T$. **La inferencia era inválida tal como la escribí:** una media cuadrática global no dice nada de un intervalo unidad. Acepto la objeción.

Lo que sí vale, y resuelve el problema para los cortes grandes:

**(T) Elección de extremos en tramos de longitud $\asymp T$.** Por Montgomery–Vaughan, para $X=T^c$,
$$\int_T^{2T}S_X^{(1)}(t)^2\,dt\ll T\log\log X+\frac{X}{\log X},$$
y los armónicos superiores aportan $O(T)$. Con $N-N_0=S+O(1/T)$ y $\int_T^{2T}S^2\ll T\log\log T$,
$$\frac1T\int_T^{2T}G_X^2\,dt\ll\log\log T+T^{c-1}.$$
Luego existen $a\in[T,\tfrac32T]$ y $b\in[2T,3T]$ con $|G_X(a)|^2+|G_X(b)|^2\ll\log\log T+T^{c-1}$, y el término cúbico es $o(T\log T)=o(M_T)$ siempre que
$$c<\tfrac53 .$$
La ventana $(a,b]$ tiene $\asymp T\log T$ ceros, y una sucesión de tales puntos $a_j\in[2^j,\tfrac32 2^j]$ da ventanas consecutivas $(a_j,a_{j+1}]$ que cubren todo. **No hace falta volver a $(T,2T]$:** la equivalencia del diente de sierra ($E\to0\iff\frac1M\int(N-F)^2dF\to\frac1{12}$) se enuncia sobre esas ventanas, que es todo lo que se necesita. Esto cubre $c\in[1,\tfrac53)$, el régimen de la resonancia. Para $c\ge\tfrac53$ haría falta un momento más alto de $S_X$ o una cota puntual mejor.

Así que la observación de v18 es correcta como crítica a mi frase y demasiado pesimista en su conclusión ("open quantitative boundary-control issue"): el control de borde está resuelto hasta $c<5/3$ con MV y ventanas elegidas.

## 4. Rem. `second-order-constant`: correcta

Cierto que la constante de segundo orden de $\int S^2$ no basta sola: hacen falta también la covarianza con $S_X$ y el término con peso $S_X'$. Mi nota de $E_T$ lo decía como "además de la parte prima"; v18 lo desglosa mejor.

## 5. Conclusión

- Ningún error matemático nuevo. La prueba de Fujii está bien reconstruida y cotejada con el original.
- Los defectos de coherencia de v15/v16 están corregidos. Faltan cuatro DOI.
- Corrección mía aceptada (§3) y sustituida por el argumento válido: extremos elegidos por MV en tramos de longitud $\asymp T$, que resuelve el borde para $X\le T^{5/3-\varepsilon}$. Propongo incorporarlo como corolario de `prop:prime-endpoint-range`.
