# TRASPASO — Casanya, ceros próximos, certificados locales y ruta hacia RH

**Fecha:** 23 de octubre de 2026. **Estado:** investigación abierta; **no hay demostración de RH**. Este documento sirve para comenzar un nuevo chat autónomo.

## 1. Objetivo y reglas de trabajo

El objetivo final es demostrar la hipótesis de Riemann (RH), investigando una ley aritmética Casanya, relojes Riemann–von Mangoldt (RvM), primos y espirales/factores espectrales. No sustituir resultados nuevos por equivalencias clásicas con RH. Identificar expresamente cada **muro matemático conocido**, sin confundirlo con una imposibilidad demostrada. Priorizar garantías **individuales para todo índice** y no únicamente RMS o porcentajes. No usar las ordenadas verdaderas para construir o ajustar centros; usarlas sólo como referencia posterior en evaluaciones. No crear versiones del manuscrito ni editar archivos congelados sin orden expresa. Para cualquier `.tex`, entregar también `.txt` idéntico. Evitar búsquedas web si no son necesarias.

Repositorio: https://github.com/vcasana1/LawCasanya . Leer `AGENTS.md` y `work/LOG.md` antes de cambios; ChatGPT escribe en `chatgpt/`, no en `work/` (salvo apéndices de registro autorizados). A 23/10 el repositorio contiene la revisión de Claude v3 en `work/prime_spiral/v3/`, mientras la síntesis inicial está en `chatgpt/casanya_prime_spiral_short_20261023/`. No mezclar automáticamente las dos redacciones.

**Preferencia del usuario:** No entregar scripts Python como producto de lectura. Subirlos a GitHub con resultados y ofrecer aquí tablas, figuras, teoremas y archivos de lectura.

## 2. Punto matemático fundamental: próximo ≠ idéntico

Sea `F(z)=xi(1/2+i z)`, entera y real sobre el eje real. Para un cero fuera de la recta crítica, `rho=beta+i gamma` con `beta != 1/2`, su simétrico `1-conj(rho)` tiene **exactamente la misma ordenada gamma**. Por el contrario, una pareja de ceros críticos simples próximos posee dos ordenadas distintas. Un cero crítico múltiple también puede tener ordenada repetida sin contradecir RH: **RH no implica simplicidad**.

La conjetura estadística GUE (ley límite habitual de espacios) presenta repulsión y ninguna masa atómica en la separación normalizada cero; implica a lo sumo **densidad cero** de coincidencias exactas, no su ausencia en todos los índices. Por tanto, GUE no prueba simplicidad ni RH ni permite ignorar un porcentaje residual de ceros.

## 3. Construcción Casanya y límites actuales

Definir `N_0(t)=theta(t)/pi+1`, `tau_k=N_0^{-1}(k-1/2)`, una fase prima `S_X(t)` y el reloj `F_X=N_0+S_X`. Los centros de una ley de flujo aritmética pueden permanecer estrictamente ordenados porque el flujo de una EDO escalar regular conserva el orden. **Orden sintético no implica localizar todos los ceros de zeta**. La inversión de centros se evita, pero la corrección puede deteriorar la precisión local.

La espiral `B_X^c(s)=P_X(s)/zeta_c(s)` y la función entera del espectro sintético codifican discrepancias de fase y permiten identidades exactas de residuos/Poisson. No identifican automáticamente el espectro sintético con el verdadero. Claude corrigió en su v2/v3 coeficientes y normalizaciones: distinguir `b_X(n/d)=mu(d)c_X(d)/sqrt(n d)` de su peso estacionario `b_X(n/d)*sqrt(n/d)=mu(d)c_X(d)/d`. Revisar la versión más reciente antes de citar fórmulas como teoremas.

Dos rutas globales que resultaron circulares o conocidas:
- Pedir una fórmula explícita de trazas exacta, con todos los primos y para todas las funciones de prueba, reconstruye en esencia el espectro completo de zeta.
- Pedir que el recuento completo de ceros coincida universalmente con todos los cambios de signo conocidos vuelve al muro clásico de RH; un criterio de certificación local no proporciona por sí solo esa desigualdad.

## 4. Teorema local de Rouché verificable sin introducir ordenadas verdaderas

Para la función real-entera `f=F` y dos racionales `b` y `h>0`, sea

`Q(z) = f''(b)/2 * ((z-b)^2-h^2)`,  `M_3 = sup_{|z-b|<=3h/2} |f'''(z)|`.

Si `f''(b)!=0` y

```
|f(b)+f''(b)h^2/2| + (5h/4)|f'(b)| + (125/384)M_3 h^3
    < (7/32)|f''(b)| h^2,                                   (I)

|f(b)+f''(b)h^2/2| + (3h/2)|f'(b)| + (9/16)M_3 h^3
    < (5/8)|f''(b)| h^2,                                    (II)
```

entonces Rouché da un único cero en cada disco `|z-(b±h)|<h/4` y exactamente dos en `|z-b|<3h/2`, todos contados con multiplicidad. Por simetría conjugada, ambos son **reales, distintos y simples**. Se comprueba la cota en círculos completos del plano complejo; no basta muestrear puntos aislados. El teorema es incondicional y local, no garantiza que los discos agoten todos los ceros.

**Distinción exacta con otro test:** si `f'(b)=0`, `f(b) != 0` y el resto cúbico está suficientemente controlado, las raíces del cuadrático local son `b±h` si `f(b)f''(b)<0` (pareja real) y `b±i h` si `f(b)f''(b)>0` (pareja conjugada no real). Si `f(b)=f'(b)=0` y `f''(b)!=0`, hay cero real doble. Nunca asumir que el signo por sí solo clasifica sin la condición de Rouché.

## 5. Resultados numéricos archivados (sin usar zeross.bin en la construcción)

Dos experimentos en alturas aproximadas 1283 y 1290. Los límites proceden del programa archivado y sus salidas; falta **auditoría independiente en Arb/FLINT** antes de publicarlos como certificación formal definitiva.

| Cantidad (tras escala positiva de F) | Altura ~1283 | Altura ~1290 |
|---|---:|---:|
| Centro `b` | 1283.159048033 | 1290.255802206 |
| Semiseparación propuesta `h` | 0.164715498 | 0.154422788 |
| `|f''(b)|` cota inferior | 52.0346348075 | 18.9905819705 |
| `M_3` cota superior | 180.855125215 | 63.282575959 |
| `eta=h*M_3/|f''(b)|` | 0.572497 | 0.514586 |
| Umbral conservador `84/125` | 0.672 | 0.672 |
| Rouché pequeños: lado izq. < lado der. | 0.263096 < 0.308822 | 0.075858 < 0.099062 |
| Rouché exterior: lado izq. < lado der. | 0.454629 < 0.882351 | 0.131082 < 0.283035 |
| Salida almacenada | `pair_1283.out` | `pair_1290.out` |

Intervalos reales certificados en los cálculos archivados:

| Pareja | Intervalo izquierdo | Intervalo derecho |
|---|---|---|
| 1283 | (1282.9531536605, 1283.0355114095) | (1283.2825846565, 1283.3649424055) |
| 1290 | (1290.062773721, 1290.139985115) | (1290.371619297, 1290.448830691) |

El código, el registro de ejecución y el detalle de truncamientos deben permanecer juntos en GitHub; no se necesita presentar el código al usuario como archivo principal. No hay prueba de índices ordinales exactos ni de ausencia de otros ceros fuera de esos discos.

## 6. Familias infinitas: lo probado y lo que NO se deduce

Un resultado clásico incondicional afirma que una proporción positiva de los ceros es **simple sobre la recta crítica**, `N_simple,line(T) >> T log T`. De ello se sigue que existen infinitas parejas de ceros críticos simples con **distancia absoluta que tiende a cero**, porque de lo contrario habría `O(T)` raíces simples hasta T. Cada cero simple admite un disco racional arbitrariamente pequeño con certificado de Rouché por la primera derivada. La búsqueda por racionales puede ser exhaustiva sin recibir las ordenadas como entrada.

**Esto NO demuestra** que existan infinitas parejas **relativamente aisladas**, ni que el método de Taylor de cuarto orden tenga éxito para infinitas parejas, ni que la separación normalizada tienda a cero. `h -> 0` por sí solo no implica `h/R -> 0`: las separaciones medias también disminuyen con la altura.

La hipótesis más fuerte que interesa para una familia de parejas aisladas es

`h/R <= 1/(1000 B)`, con `B=sup_{|z-m|<=R}|H(z)|/inf_{|z-m|<=R}|H(z)|`, donde `f(z)=((z-m)^2-h^2)H(z)` y `H` no se anula. Bajo regularidad y control explícito del factor `H`, los errores relativos del desarrollo de cuarto orden pueden ser `O(B(h/R)^3)`. Los coeficientes y dominios del teorema deben tomarse de la v3 revisada y comprobarse; **la hipótesis de aislamiento no está probada para una familia infinita de zeta**.

Incluso si se demostrase para infinitas parejas, ello probaría sólo que el método cuártico localiza una familia infinita de ceros críticos simples. **No demostraría RH.** Tampoco excluiría ceros adicionales no reales o un conjunto excepcional de densidad cero.

## 7. PASOS NECESARIOS DESDE AQUÍ HASTA RH — sin atajos lógicos

1. **Cerrar los certificados locales efectivamente:** reproducir los dos experimentos con biblioteca intervalar independiente, cotas rigurosas de funciones especiales y resultados de salida reproducibles. Un ejemplo finito valida la técnica, no su generalidad.
2. **Familia infinita no trivial del método cuártico:** demostrar, usando solo datos analíticos de `Xi` y/o construcción Casanya, que infinitas parejas satisfacen condiciones de aislamiento y cotas de `H`, con un enunciado de altura arbitraria. Resultado autónomo potencialmente publicable, pero todavía no RH.
3. **Pasar de parejas aisladas a todos los conglomerados:** cubrir también las regiones donde `h/R` no es pequeño, casos de tres o más raíces y multiplicidades; no imponer que todos los ceros sean simples, pues RH sólo exige realidad de las coordenadas `z`.
4. **Teorema universal de REALIDAD:** derivar una desigualdad nueva que certifique que **cada bloque espectral, incluido cualquier bloque hipotéticamente no real**, sólo contiene ceros reales. Posibles herramientas: momentos firmados, cotas de restos complejos, fase prima y geometría de la espiral. El test de Hankel semidefinido es una equivalencia algebraica, **no** su demostración.
5. **Cobertura exhaustiva sin presuponer RH:** justificar que los bloques cubren todo el semiplano de ordenadas positivas de ceros no triviales, incluyendo posibles ceros fuera de la recta y zonas sin cambios de signo. No basta contar solamente los ceros reales encontrados. Se necesitan estimaciones independientes o una propiedad estructural que **excluya** otros ceros; convertirlo sin más en igualdad de recuentos es el muro clásico conocido.
6. **Tramo inicial + todas las alturas:** una vez demostrados los pasos universales, verificar por métodos rigurosos el tramo finito que quede y controlar fronteras/transiciones. No se necesita un margen positivo uniforme en el índice si hay un teorema aplicable a cada índice.
7. **Concluir RH:** si se demuestra que todo cero de `F(z)=xi(1/2+i z)` en la banda `|Im z|<1/2` tiene `Im z=0`, entonces todo cero no trivial `rho=beta+i gamma` satisface `beta=1/2`. La simplicidad es una cuestión adicional y no imprescindible.

**Barrera conocida:** GUE estadística, infinitas parejas reales certificadas y una tasa de fallos que tienda a cero NO bastan para los pasos 4–5. Tampoco basta el argumento de contorno con defectos pares `N-v<2` para todos los bloques si no se demuestra una nueva desigualdad analítica, pues el problema vuelve a ser RH.

## 8. Tarea de investigación inmediata para el nuevo chat

Prioridad A: buscar una propiedad de `F` que **distinga y certifique** en el plano complejo una pareja de ordenadas iguales procedente de ceros no críticos frente a dos ceros críticos muy cercanos; las cotas locales de Rouché distinguen ambos casos donde son aplicables. Prioridad B: estudiar si el factor `H` se controla de manera no trivial para infinitas parejas **relativamente** aisladas y, más difícil, qué método cubre los conglomerados restantes. Prioridad C: demostrar una **desigualdad universal nueva** que excluya raíces no reales sin recurrir al mismo recuento clásico de ceros con otro nombre.

**Advertencia de prioridad:** No afirmar que un teorema «válido a cualquier altura bajo hipótesis» verifica sus hipótesis a todas las alturas. No afirmar que un número infinito de ejemplos o una proporción 1 de ceros críticos prueban RH. Diferenciar pruebas exactas, experimentos numéricos y conjeturas.

## 9. Ubicaciones de continuidad

- Repositorio: https://github.com/vcasana1/LawCasanya
- Artículo revisado por Claude: `work/prime_spiral/v3/`.
- Síntesis inicial ChatGPT: `chatgpt/casanya_prime_spiral_short_20261023/`.
- Documentos complementarios: `work/display/2026-10-22_espiral_momentos_hankel_transporte.txt`, `2026-10-22_revision_veredicto_defecto_par.txt`, `2026-10-22_extremo_espectral_taylor_cuarto_orden.txt`, `2026-10-22_auditoria_F_X_zeta_sintetica_espiral_B.txt`, `2026-10-23_primer_armonico_friable_Mobius.md`.
- Certificados locales y resultados: `chatgpt/casanya_pair_cert_20261023/` (véase README y `.out`).
- **No crear una nueva versión de artículo sin orden del autor.**
