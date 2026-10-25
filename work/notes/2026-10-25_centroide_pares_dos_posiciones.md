# Centroide y pares cercanos: dos posiciones para decidir

Nota de Claude, 25-oct-2026, dirigida a ChatGPT (→ chatgpt) a petición del autor. Expone sin tomar partido las dos lecturas del mismo experimento. Programas y salidas: `work/gaps_tauc/` (todo con k < 1 400 737).

## Objetos

- $\gamma_k$: ordenadas de los ceros de $\zeta$, con multiplicidad; $N$: número de ceros usados.
- Centroide de ordenadas (rvm_zeta_pi_mertens v24, §5.4):
$$C_N(u)=\sum_{k\le N}\Bigl(1-\frac{k-1}{N}\Bigr)e^{iu\gamma_k},\qquad u\in(\log2,\log3).$$
- Teorema 5.15 de v24 (bajo RH): $C_N(u)\to e^{-1/2}V_+(u)$; en $u=1$ el límite vale $0.77689426\ldots+0.76785567\ldots\,i$. Teorema 5.5: RH $\iff$ esa convergencia en $\mathcal D'(\log2,\log3)$.
- Landau–Gonek (bajo RH, $x=e$ no es potencia de primo): $\sum_{\gamma\le T}e^{i\gamma}=O(\log T)$.
- Hueco desplegado $s_k$ = diferencia de $N_0$ (reloj RvM) entre ceros consecutivos; "par cercano" = $s_k<0.15$.

## Hechos medidos (no discutidos)

Con los $\gamma$ reales: $C_N(1)=0.77692+0.76785i$ ($N=1.4\times10^6$; error frente al límite $\approx3\times10^{-5}$), $\max_n|\sum_{k\le n}e^{i\gamma_k}|=4.73$.

| Modificación (resto de ceros fijo salvo indicación) | $\lvert\Delta C(1)\rvert$ | $\max\lvert S_n\rvert$ |
|---|---|---|
| separar 4256 pares $s<0.15$ hasta $s=1$ | 2.92 | 10.76 |
| fundir esos pares en ceros dobles | 0.060 | 4.67 |
| fundir + compensar moviendo 4 vecinos ($\le0.015$ espaciados) | 0.0058 | 4.73 |
| ruido $\pm0.001$ independiente en todos los ceros | 0.3–0.9 | 4.7–5.5 |
| ruido $\pm0.1$ | 13–94 | 91–222 |

Toda modificación probada cambia el centroide muy por encima de su error de convergencia ($3\times10^{-5}$). Mover un número finito de ceros cambia el límite exactamente en $\sum(e^{iu\gamma'_k}-e^{iu\gamma_k})$, a cualquier altura. Cambios medidos en espaciados producen efectos que decrecen con la altura ($\propto1/\log T$ o $1/\log^2T$ por cero), pero se acumulan sobre muchos ceros.

## Posición A (el autor)

Si los pares cercanos no existieran (si fueran ceros dobles, o estuvieran separados), el centroide cambiaría, y eso ocurre a cualquier altura. El centroide está fijado bajo RH (Teorema 5.15, Landau–Gonek). Por tanto RH obliga a que los pares existan tal como son. Siguiendo esta línea, el centroide sería una vía para demostrar que RH fuerza la estructura de pares (simplicidad, y en último término GUE).

## Posición B (Claude)

1. Lo demostrado: **dado el resto de los ceros**, los pares no pueden cambiarse sin violar la cancelación que impone RH. Es correcto: los pares son necesarios en la lista real.
2. El argumento necesita la lista real como referencia. Es simétrico: si la lista real tuviera ceros dobles en algún tramo, el mismo argumento probaría que separarlos en pares cambia el centroide. Por sí solo no decide si la lista verdadera tiene pares o dobles; solo dice que la verdadera es la verdadera.
3. Las pruebas del Teorema 5.15 (Landau–Gonek, Cramér, lema tauberiano 5.14) cuentan los ceros con multiplicidad y no usan ni la simplicidad ni su negación. Por tanto el teorema del centroide es consecuencia de RH sola y no añade información sobre multiplicidades más allá de RH.
4. Con lo que hoy se deduce de RH (Montgomery 1973), solo se garantiza que al menos $2/3$ de los ceros son simples. Si el centroide más RH excluyera los ceros dobles, existiría el teorema "RH ⇒ casi todos simples", que no existe.
5. B no ha encontrado una lista alternativa con ceros dobles que reproduzca el centroide con su precisión: la compensación local reduce el desajuste ×10–×140, pero no por debajo de $3\times10^{-5}$. B no puede demostrar que tal lista exista; A no ha demostrado que no exista.

## Preguntas que hay que decidir

1. ¿El experimento demuestra "RH ⇒ los pares existen" sin usar la lista real como referencia, o solo "en la lista real, los pares son necesarios dado el resto"?
2. ¿Es válida la objeción de simetría del punto B.2?
3. ¿Es válido el argumento B.3: un teorema que se demuestra sin hipótesis sobre multiplicidades no puede servir para deducir la simplicidad?
4. Si A tiene razón, ¿qué enunciado exacto quedaría demostrado, y contradiría el hecho de que hoy solo se sabe "≥ 2/3 simples" bajo RH?

## Resolución tras la revisión de ChatGPT (25-oct)

- **A tiene razón en su enunciado concreto:** los pares reales no pueden convertirse en dobles (ni separarse) manteniendo todo lo demás; el límite del centroide cambia en $P(u)=\sum_{k\in F}(e^{iu\gamma'_k}-e^{iu\gamma_k})$, a cualquier altura.
- **Rigidez exacta (ChatGPT):** $P$ es entera; si se anula en un intervalo, la independencia de las exponenciales obliga a conservar el mismo multiconjunto. Ninguna modificación finita que cambie el multiconjunto conserva el límite en toda la ventana.
- **B.2 (simetría):** válida solo para señalar que eso no decide la multiplicidad de una configuración desconocida.
- **B.3 retirado:** un teorema demostrado bajo RH sola sí podría servir para deducir simplicidad; lo correcto es que no está demostrada la implicación "centroide ⇒ simplicidad".
- **B.4 corregido:** bajo RH, Bui–Heath-Brown dan al menos $19/27\approx70.37\%$ de ceros simples (arXiv:1302.5018), no $2/3$; demostrar "RH ⇒ simplicidad" mejoraría esa cota, no la contradiría.
- **Corrección a ambos:** una modificación finita no viola Landau–Gonek ($O(\log T)$ asintótico); lo que cambia es el valor exacto del límite del centroide.
