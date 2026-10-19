# Para Claude: incorporación a v11, no a v10

El autor ordenó preparar en detalle y subir este material para que Claude lo incorpore a **v11**. Su corrección expresa: «no, a la v11, ya está haciendo una v10 con tu ultima correccion». Este directorio no crea ninguna versión del artículo y no modifica v9/v10.

## Qué leer

1. **`v11_delta.tex` y su copia byte a byte `.txt`: fragmento preferido para incorporar**, porque durante esta tarea apareció el borrador v10 y ya incorpora la construcción. Este suplemento amplía esa sección, sin duplicarla: corte hasta `sqrt(T/2)`, momentos y transporte en la ventana del reloj, tolerancia y certificado dual explícito. Conserva los nombres que v10 ya asignó a los mismos objetos.
2. `regularized_clock_insert.tex` y su copia byte a byte `.txt`: demostración completa de respaldo en inglés, desde la construcción. No insertar además de la sección existente: es una prueba alternativa de consulta, con un espacio de nombres conservador revisado contra v9. Usa L(T) en lugar de log(T)/(2pi), una normalización asintóticamente equivalente; **el suplemento preferido mantiene exactamente la construcción de v10**.
3. `display_mejoras.md`: respuesta anterior del chat archivada literalmente, con las cuatro mejoras solicitadas. El desarrollo detallado del TEX precisa su alcance.
4. `verify_handoff.py` y `verification.json`: verificaciones estructurales, referencias contra v9/v10, ausencia de colisiones de etiquetas y de los nombres nuevos auditados, identidades algebraicas y compilación de arneses mínimos. No son una certificación automática de la prueba ni de las fuentes externas.

Base leída: `work/paper1/manuscript/prime_corrected_clock_v9.tex`, commit `2d8e702855192f2d959f66598a0289c31c4bfb28`, blob `59edc0050ab390132870358a8091ddf754a3c8fe`.

**Actualización durante la tarea:** se leyó también el borrador v10 de `work/paper1/v10/manuscript/prime_corrected_clock_v10.tex`, commit `149d1ee794c1d51022ee1ddee92e42a621ef2d0a`, blob `d30ca6441cbbe2c6494c46e0c83a245d8e16a184`. Ya contiene `def:regularized`, `lem:slope_envelope`, `lem:block_fourth` y `thm:regularized_clock`. La ampliación exacta respecto a ese borrador es:

- Sustituir `2<=X<=T^(1/3)` por **`2<=X<=sqrt(T/2)`** en el lema de bloque y la parte de aproximación de Theorem D'. Esto conserva constantes absolutas y la dependencia explícita `(1+log(1/c))^2`. En particular cubre todo `c<1/2` fijo para T suficientemente grande; no se afirma el extremo X=sqrt(T) con esta cobertura concreta.
- Enunciar y probar también los momentos en `I_T^tau`, no únicamente la existencia de esos puntos. Mantener los resultados sobre `I_T`.
- Mantener el rango separado `X<=T^(1/4)` del transporte, extendiendo su promedio a `I_T^tau`.
- Añadir la tolerancia certificada del problema convexo, ausente del borrador inspeccionado.
- Añadir la forma de la identidad con extremos arbitrarios; evita estimaciones asimétricas de defectos en las ordenadas de borde.

No sustituir el teorema uniforme de v10 por una afirmación más débil solo para c fijo. `v11_delta.tex` conserva su uniformidad y mejora su rango.

**Reconciliación final antes de publicar:** apareció la v10 terminada en `c2ffecc309f9503eda8fc12855b6f80725524110`. Se leyeron sus cambios y se repitió la auditoría contra ese TEX. Claude había renombrado la malla para evitar colisiones: `mathsf M_T -> mathsf L_T`, `eta_T -> varsigma_T`, `t_i -> mathsf t_i`. El suplemento preferido usa **los nombres finales**; en particular `h=varsigma_T`, no `eta_T`. Mantiene `Lambda_T=log(T)/(2pi)` con su mismo significado ya establecido en v10. El archivo `verification.json` identifica esa base final.

## Resultados que se entregan y alcance exacto

- Para cada exponente **fijo** `0<c<1/2`, construir el minimizador cuártico sobre interpolantes con pendiente entre `L(T)/2` y `2L(T)` y malla con paso como máximo `1/L(T)`. Se obtiene un cuarto momento del error en alturas `O_c(log(T)^(-4))` y, por tanto, segundo momento `O_c(log(T)^(-2))`.
- La construcción y la selección de índices usan únicamente el reloj y los primos: se usa la ventana existente `I_T^tau={k:T<=tau_k<2T}`. Las ordenadas y el conteo verdadero se usan en la demostración.
- Para `0<c<1/4`, el transporte desde los **nuevos puntos regularizados** tiene segundo momento `O_c(1)`. El rango menor procede del muestreo y de los octavos momentos de las derivadas, no de la aproximación principal.
- La salida tiene orden estricto y separación entre `1/(2L(T))` y `2/L(T)`. Es una propiedad impuesta por la construcción: no afirmar que reproduce GUE o espaciados finos de zeta.
- Para una solución admisible cuyo objetivo exceda el óptimo en como máximo `eta_reg*T`, con `0<=eta_reg<=1`, se conserva el error cuadrático `O_c((1+sqrt(eta_reg))/log(T)^2)`. El TEX incluye una cota dual computable que certifica esa tolerancia, sin ceros.
- No se demuestra que el transporte del **paso original desde tau** sea acotado. No sustituir la fórmula del paso original por la del nuevo reloj sin indicarlo.
- El resultado es por bloques en `T`. No se ha construido un único reloj global independiente del bloque. No se afirma novedad histórica ni un resultado sobre RH.

## Colisiones de nombres comprobadas contra v9

| Nombre usado aquí | Motivo |
|---|---|
| `\lL(T)` (ya existente) | Sustituye el `Lambda_T` del display; `\Lambda` ya designa von Mangoldt. No introducir otro significado de Lambda. |
| `\mathcal J_T^{\mathrm{reg}}` | Intervalo de regularización; no es la `\mathcal J` de primos entre cortes. |
| `\mathcal C_T^{\mathrm{reg}}` | Clase admisible; no usar `\mathcal P_T`, pues `\mathcal P` es el conjunto de pares de exponentes de Theorem E. |
| `\mathsf m_T^{\mathrm{reg}}`, `\mathsf h_T^{\mathrm{reg}}`, `\mathsf t_{T,j}^{\mathrm{reg}}` | Número de celdas, paso y nodos; no son el orden de momento, `m^*` ni los puntos de Gram `t_n`. |
| `\mathsf a_T^{\mathrm{reg}}`, `\mathsf b_T^{\mathrm{reg}}` | Pendientes; no son los coeficientes `a_n` ni el paso de muestreo `\mathfrak b_T`. |
| `\mathsf H_T^{\mathrm{reg}}` | Comparador en la prueba; no es la escala iterada `H_j`. |
| `\mathsf D_{T,j}^{\pm,\mathrm{reg}}` | Incrementos de S; no son los polinomios de Dirichlet `\mathcal D`. |
| `\widehat F_{T,c}`, `\widehat x_{T,c,k}`, `\widehat u_{T,c,k}` | Nuevos objetos; no reasignar `x_k^{(j)}`, `u_k(X)` o `r_k(X)`. |
| `\eta_{\mathrm{reg}}` | Tolerancia; no son los coeficientes `eta_n` del polinomio de Dirichlet. |
| Etiquetas `reg:*` | Espacio de etiquetas nuevo; sin coincidencias en v9. Repetir auditoría contra v10 antes de incorporar. |

No se añaden macros globales. Se mantienen las convenciones de v9 para `\NO`, `\lL`, `\IT`, `N`, `S_X` y `\Psi_j`.

## Dependencias que hay que mantener explícitas

La demostración necesita solamente órdenes **fijos**:

- `eq:R_fourth`: cuarto momento continuo de `N-F_X`, con un mismo corte `X=T^c` en `[T/2,3T]`; cubrir por un número fijo de intervalos diádicos. Para `c<1/2` fijo, su exponente relativo sigue por debajo de `1/2` para T suficientemente grande.
- `thm:known_fujii_difference`: momento octavo de incrementos de S, **k=4**, para desplazamientos <=1. Para desplazamientos mayores se usan los momentos octavos individuales de S (`thm:known_selberg_moments`), no una nueva uniformidad en desplazamientos grandes.
- `thm:identity_general`: extensión por cadena absolutamente continua a interpolantes lineales; se da la identidad con extremos arbitrarios, con el signo de los extremos escrito y probado.
- La separación del reloj regularizado da directamente multiplicidad acotada: `n_tilde<=3` y `integral n_tilde^2 <= 3*b_T*#I`. La v10 ya utiliza esta simplificación; conservarla. No hacen falta pares/ternas de ceros para este paso.
- `lem:sampling_rho`: orden fijo r=1, con octavos momentos de derivadas. Usar la constante uniforme corregida por la revisión anterior, no el 7 no uniforme de versiones antiguas.

**Cambio editorial imprescindible:** junto a `thm:known_fujii_difference`, v9 dice «Only k=1,2 ... are used». Con esta incorporación también se usa **k=4**. Actualizar la frase y añadir la remisión a `reg:count_comparator`; no ampliar silenciosamente el rango `k=1,2` de `eq:fujii_difference`, que sigue siendo la forma usada en la prueba anterior de pares.

Las fuentes originales de Fujii/Korolev no se han vuelto a leer en esta tarea. Este desarrollo usa sus formulaciones registradas y revisadas por Claude en v9. El supuesto externo adicional respecto al uso anterior es el caso fijo k=4 del teorema de incrementos ya enunciado para todo k. Claude debe conservar su comprobación de fuente al integrar.

## Certificación del minimizador y constantes de precisión

El TEX proporciona un certificado suficiente: vector factible, multiplicadores no negativos y una cota dual explícita `B_reg`. Si `E(v)-B_reg <= eta_reg*T`, la tolerancia queda probada. Para una implementación real hay que encerrar integrales, gradientes y desigualdades con redondeo dirigido. No se ha ejecutado aquí un solver ni se presentan datos de ceros.

La contabilidad analítica de constantes es:

```
Z_4 = sum_{j>=1} log(2+j)^4/j^4
C_H = 5120 + 4096*C_D*Z_4
C_cmp = 8*C_H + 320
C_reg(c) = 64*C_cmp + 72*C_pr(c)
C_reg_eta(c) = C_reg(c) + 8*eta_reg
```

`C_D` es la constante del momento octavo de incrementos en el dominio ampliado; `C_pr(c)` la del cuarto momento continuo de la aproximación por primos. Se prueba que son finitas. **No se han calculado sus valores numéricos ni un umbral numérico T0.** No anunciar una constante de precisión certificada a las alturas del autor a partir de esta nota. El certificado de optimización controla la aproximación del minimizador, no sustituye esas constantes analíticas.

La construcción sí queda definida con parámetros explícitos una vez elegidos T y c, sin depender de `C_star` o `H^*` ni de evaluar los ceros. La efectivización numérica de la garantía analítica sigue siendo un trabajo distinto que requiere las constantes de los resultados externos.

## Integración sugerida en v11

- Ampliar la sección regularizada de v10 usando **`v11_delta.tex`**; no insertar una segunda construcción regularizada ni cambiar silenciosamente su normalización. El fragmento completo de respaldo documenta la prueba anterior; no es una sección adicional obligatoria. Conservar los resultados previos y Theorem E.
- Presentar como aporte la construcción finita, el corte fijo, el cuarto momento y su demostración. No presentar únicamente la tasa aislada `O(log(T)^(-2))`, que el autor ya pidió no promover por sí sola.
- Actualizar resumen, tabla de estado y comparación: el nuevo reloj usa primos y un problema convexo finito; no evalúa zeta ni ceros, y no requiere buscar ramas.
- Añadir los nombres nuevos a la tabla de notación. Conservar numeración a la derecha, TOC, hipervínculos y el mecanismo real de hover de la versión de Claude. Regenerar los tooltips tras integrar, no reutilizar texto antiguo para etiquetas nuevas.
- La compilación del arnés aquí solo comprueba sintaxis del fragmento. Claude compila y revisa el PDF de v11 completo y su navegación/hover con su pipeline.
- No modificar v9 o v10 desde esta entrega; solo material de incorporación para v11.
