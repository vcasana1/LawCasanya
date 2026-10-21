# Benchmark Casaña–Gonek–LeClair: evaluación por índice y separación propia

Continuación de la entrega inicial, que se conserva. Fecha: 2026-10-21. Ningún manuscrito ni binario original se modifica. Los ceros verdaderos se leen únicamente en los evaluadores. Los nuevos constructores tienen una prohibición de abrir `zeross`.

## Corrección del criterio pedida por el autor

Para CADA método por separado, sea `x[k]` su cero sintético con el índice original k y `e[k]=x[k]−gamma[k]`. Nunca se reasigna k a un cero verdadero más próximo ni se ordenan las salidas para ocultar inversiones. Sean `a_izq=x[k]−x[k−1]` y `a_der=x[k+1]−x[k]`, usando siempre los vecinos originales k±1, aunque el piloto sea disperso.

El criterio PRINCIPAL es `−a_der/2 < e[k] < a_izq/2`. Equivale, para una sucesión sintética estrictamente creciente, a que gamma[k] esté dentro de la celda de x[k] delimitada por los puntos medios sintéticos. Si e>0 se usa a_izq; si e<0 se usa a_der. El cociente direccional es `2|e|/a_lado`, y debe ser <1. Una igualdad con el punto medio incumple la desigualdad estricta. En k=1 y k=N las celdas exteriores son ilimitadas por el lado sin vecino. Los extremos de ventanas interiores usan los vecinos externos reales, nunca se tratan como extremos globales.

El antiguo `2|e|<min(a_izq,a_der)` se conserva como **condición suficiente más exigente**, NO necesaria para esa pertenencia. Ejemplo: a_izq=10, a_der=1, e=4 cumple el criterio direccional (cociente .8), pero incumple el simétrico (cociente 8). La discrepancia se prueba en `localgap_metrics.py`.

El ejemplo real k=53 de c667_PAV_a010 tiene e=0.41229293562059866, a_izq=3.225234006948881 y a_der=0.20822912372284463: el cociente direccional es 0.2556669901981059, frente al simétrico 3.9599929947298373. Los primeros 1.000 índices tienen cero incumplimientos direccionales, frente a 65 simétricos. Este resultado finito no se extrapola al tramo final.

Esta definición comprueba qué cero SINTÉTICO es el más próximo a gamma[k]. No se cambia por el problema inverso de buscar qué cero VERDADERO es el más próximo a x[k]. Tampoco verifica por sí sola que una celda contenga exactamente un cero de zeta no incluido en la referencia. Los fallos de orden (algún vecino sintético con separación ≤0) se separan de los incumplimientos de proximidad. El total de fallos suma ambas clases disjuntas; los casos sin vecinos conocidos se declaran sin cobertura. No se usa separación media para ninguna decisión de proximidad.

## Métodos y presupuesto

* c667: los tres pasos originales con cortes efectivos (8,8,512), históricamente seleccionados con validación. Se conserva su binario local exacto.
* c667_PAV_a010: el código de proyección suministrado, aplicado globalmente a los 2.001.052 índices: PAV(x−.1*tau)+.1*tau. No añade primos y produce cero inversiones. La monotonía impuesta no prueba proximidad individual.
* Barrido Casaña constante: los mismos tres pasos, ahora (8,8,X), X=512,2048,8192, y sus proyecciones globales con alpha=.10. Es un experimento fijo distinto del c667 diádico en alturas bajas. No se optimizan parámetros con los ceros de prueba.
* Gonek: ecuación de fase del producto suavizado, theta exacta, peso 1 hasta X y 2−log(n)/log(X) hasta X². Para igualar presupuestos se toma X=sqrt(512),sqrt(2048),sqrt(8192), con 97,309,1028 primos activos, respectivamente. El corte nominal y el número de primos son magnitudes distintas.
* LeClair: la misma ecuación (49) de la entrega inicial, producto de Euler finito, delta=1e−6, término de Stirling 1/(48t), con exactamente esos 97,309,1028 primos. No se sustituye la fase por zeta verdadera.

Las referencias precisas y páginas verificadas están en `SOURCES_VERIFIED.md` y en los textos fuente de la entrega anterior. `sources/README.md` es una copia histórica del README auxiliar recibido, no la validación de esta continuación. La igualdad de número de primos NO implica igual coste: los tres pasos de Casaña y resolver una raíz convergida son operaciones distintas. `same_equation_solver_diagnostic.csv` compara además los tres pasos y la raíz convergida de la MISMA ecuación sharp para separar error de iteración y cambio de fórmula. En el piloto, aumentar el corte de los tres pasos puede empeorar la proximidad; no se atribuye todo al corte sin este control.

## Índices y control de raíces

Se conservan los 1.000 índices del piloto anterior y sus predicciones ya calculadas; se añaden los primeros 1.000 consecutivos, los últimos 300 consecutivos y los vecinos k±1 necesarios: 3.026 índices de contexto en total. Los «últimos 300 del piloto» son los últimos 300 índices de la selección original, no los últimos 300 consecutivos del archivo.

Antes de ampliar se barre la familia regular t≥6.3 desde el principio hasta k=2.001.052 en mallas .08 y .04. Sus resultados son evidencia numérica, NO una certificación por intervalos ni una enumeración de todos los artefactos del modelo cerca de t=0. Los artefactos de pequeña altura se conservan en los diagnósticos de prefijo. La familia e índice se fijan por niveles k−1/2 de la ecuación, con continuación desde el reloj; no se confunden con el ordinal de TODOS los ceros del modelo finito.

**Error de solver encontrado:** en LeClair con 97 primos, el nivel k=1.886.677 tiene tres raíces regulares, verificadas también a 55 dígitos: 1072977.38424057018577…, 1072977.58273231720711…, 1072977.67472109501003…. Newton desde Lambert converge a la segunda; la continuación primo a primo usada en la entrega original escoge la primera, sin consultar gamma. Se conserva esta última selección. Los índices vecinos y sus intervalos se comprueban antes de ampliar ese caso. Los tres ceros NO se convierten en tres nuevos índices ni se corre el resto de la secuencia dos posiciones. Véanse `multiroot_audit.json` y `*_selection_gate.json`. Por ello, el antiguo requisito de raíz única falla para esa configuración; el control posterior valida explícitamente la selección por índice, no una unicidad inexistente.

## Primeros 1.000 índices consecutivos

| Método | Primos | n | RMS | MAE | Máx. abs. (k) | Fallos direccionales | Estructurales | Peor cociente (k) | Fallos simétricos |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Gonek_X512 | 97 | 1000 | 0.0283659167 | 0.0215259809 | 0.103172632 (923) | 0 | 0 | 0.571030688 (923) | 0 |
| LeClair_X512 | 97 | 1000 | 0.0311027003 | 0.0243912302 | 0.0945956249 (368) | 0 | 0 | 0.446068086 (923) | 0 |
| Gonek_X2048 | 309 | 1000 | 0.0185171631 | 0.0126562377 | 0.0679879796 (922) | 0 | 0 | 0.465544353 (922) | 0 |
| LeClair_X2048 | 309 | 1000 | 0.0200179081 | 0.0160889322 | 0.0722166166 (485) | 0 | 0 | 0.357760222 (923) | 0 |
| Gonek_X8192 | 1028 | 1000 | 0.0120105627 | 0.00776670897 | 0.0474025562 (922) | 0 | 0 | 0.373024233 (922) | 0 |
| LeClair_X8192 | 1028 | 1000 | 0.0140842272 | 0.0113112014 | 0.0443721383 (2) | 0 | 0 | 0.204100718 (922) | 0 |
| c667_PAV_a010 | 97 | 1000 | 0.145188729 | 0.102853796 | 1.35755097 (2) | 0 | 0 | 0.87278814 (997) | 65 |
| c667_original | 97 | 1000 | 0.146419705 | 0.103715429 | 1.35755097 (2) | 0 | 4 | 0.87278814 (997) | 66 |

## Últimos 300 del piloto original

| Método | Primos | n | RMS | MAE | Máx. abs. (k) | Fallos direccionales | Estructurales | Peor cociente (k) | Fallos simétricos |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Gonek_X512 | 97 | 300 | 0.0517516633 | 0.0399592466 | 0.167738127 (1400763) | 0 | 0 | 0.811798702 (1883155) | 0 |
| LeClair_X512 | 97 | 300 | 0.0460844725 | 0.0369488808 | 0.128973038 (1400761) | 0 | 0 | 0.786499137 (1400794) | 0 |
| Gonek_X2048 | 309 | 300 | 0.0367569146 | 0.0268657032 | 0.123137942 (1883155) | 0 | 0 | 0.786433424 (1883155) | 0 |
| LeClair_X2048 | 309 | 300 | 0.0365230075 | 0.0293051179 | 0.108603232 (1709306) | 0 | 0 | 0.618118475 (1883155) | 0 |
| Gonek_X8192 | 1028 | 300 | 0.0279008085 | 0.0214568422 | 0.0945451448 (1883155) | 0 | 0 | 0.675840763 (1883155) | 0 |
| LeClair_X8192 | 1028 | 300 | 0.0314381316 | 0.0257553559 | 0.0783461538 (1400778) | 0 | 0 | 0.502118862 (1400794) | 0 |
| c667_PAV_a010 | 97 | 300 | 0.0421002802 | 0.0342338391 | 0.138429698 (1883155) | 1 | 0 | 1.04452072 (1883155) | 7 |
| c667_original | 97 | 300 | 0.0423563787 | 0.0343838355 | 0.138429698 (1883155) | 1 | 1 | 1.04452072 (1883155) | 7 |

## Tramo final completo: k=1.400.737…2.001.052

Presupuestos completos en esta actualización: [512, 2048, 8192]. Estado de los tres presupuestos: **completo**.

| Método | Primos | n | RMS | MAE | Máx. abs. (k) | Fallos direccionales | Estructurales | Peor cociente (k) | Fallos simétricos |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Gonek_X512 | 97 | 600316 | 0.0535990056 | 0.0416375716 | 0.220859385 (1457942) | 228 | 0 | 1.43477151 (1489071) | 308 |
| LeClair_X512 | 97 | 600316 | 0.0447613004 | 0.0355427446 | 0.20590767 (1497473) | 189 | 0 | 1.28213947 (2000644) | 500 |
| Casanya_constant_X512 | 97 | 600316 | 0.0405544549 | 0.0313986658 | 0.313494604 (1976421) | 926 | 548 | 2.60256864 (1873931) | 11586 |
| Casanya_constant_X512_PAV_a010 | 97 | 600316 | 0.0403888912 | 0.0313322462 | 0.262265848 (1603078) | 938 | 0 | 2.00978544 (1447313) | 11374 |
| c667_original | 97 | 600316 | 0.0405544549 | 0.0313986658 | 0.313494604 (1976421) | 926 | 548 | 2.60256864 (1873931) | 11586 |
| c667_PAV_a010 | 97 | 600316 | 0.0403888912 | 0.0313322462 | 0.262265848 (1603078) | 938 | 0 | 2.00978544 (1447313) | 11374 |
| zCasanya0_existing | 97 | 600316 | 0.0401522926 | 0.0312051607 | 0.262265848 (1603078) | 897 | 0 | 1.87742387 (1592499) | 9823 |
| Gonek_X2048 | 309 | 600316 | 0.0383228323 | 0.0289872863 | 0.175866735 (1457943) | 72 | 0 | 1.29718197 (1489073) | 77 |
| LeClair_X2048 | 309 | 600316 | 0.0361429158 | 0.029143734 | 0.15238085 (1468582) | 81 | 0 | 1.22173994 (1855472) | 171 |
| Casanya_constant_X2048 | 309 | 600316 | 0.047222364 | 0.0378212343 | 0.278475339 (1626217) | 1063 | 4606 | 33.7710755 (1747534) | 51997 |
| Casanya_constant_X2048_PAV_a010 | 309 | 600316 | 0.0464647438 | 0.0373243812 | 0.263023093 (1421860) | 1153 | 0 | 4.03540086 (1506174) | 49492 |
| Gonek_X8192 | 1028 | 600316 | 0.0288968807 | 0.0220945009 | 0.145293158 (1668774) | 29 | 0 | 1.22156312 (1489073) | 30 |
| LeClair_X8192 | 1028 | 600316 | 0.0304208143 | 0.024745793 | 0.133793916 (1790602) | 31 | 0 | 1.13298475 (1441606) | 52 |
| Casanya_constant_X8192 | 1028 | 600316 | 0.060938395 | 0.0501873696 | 0.299291126 (1783577) | 856 | 26098 | 92.0475538 (1870065) | 123211 |
| Casanya_constant_X8192_PAV_a010 | 1028 | 600316 | 0.0574326659 | 0.0475785897 | 0.236882226 (1836329) | 1336 | 0 | 4.32081769 (1537772) | 115033 |

## Qué cambia al aumentar el presupuesto

* Gonek: 97 primos: 228 fallos, RMS 0.0535990056; 309 primos: 72 fallos, RMS 0.0383228323; 1028 primos: 29 fallos, RMS 0.0288968807.
* LeClair: 97 primos: 189 fallos, RMS 0.0447613004; 309 primos: 81 fallos, RMS 0.0361429158; 1028 primos: 31 fallos, RMS 0.0304208143.
* Casanya_constant: 97 primos: 938 fallos, RMS 0.0403888912; 309 primos: 1153 fallos, RMS 0.0464647438; 1028 primos: 1336 fallos, RMS 0.0574326659.

El barrido fijo de los tres pasos de Casaña + PAV empeora el recuento direccional del tramo final al aumentar X. El piloto de la raíz convergida sharp, con idéntica ecuación, separa este efecto de truncamiento/iteración del mero número de primos. No se ha reconstruido esa raíz sharp en todo el tramo final, por lo que no se extrapola su resultado piloto.


## Otras versiones ya existentes, evaluadas sin reconstruirlas

| Método | Primos | n | RMS | MAE | Máx. abs. (k) | Fallos direccionales | Estructurales | Peor cociente (k) | Fallos simétricos |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| v17_StageA | per-index: see original cutoffs | 600316 | 0.104585509 | 0.0845142248 | 0.409801926 (1972068) | 7263 | 0 | 1.7835759 (1855472) | 11538 |
| v17_R1 | per-index: see original cutoffs | 600316 | 0.0473036203 | 0.0375148077 | 0.284300588 (1508942) | 215 | 0 | 1.31979011 (2000644) | 593 |
| v17_R2 | per-index: see original cutoffs | 600316 | 0.0331440146 | 0.0268751437 | 0.274647164 (1766631) | 58 | 0 | 1.17311952 (1489073) | 95 |

v17 R2 usa un presupuesto por índice diferente y una regla heurística de continuación; no se inserta en la clasificación de igual número de primos. Sus controles de segmentos muestrean puntos, no intervalos completos. Solo se reconstruyó el vecino k=1.400.736 ausente en el archivo final: el cálculo coincide exactamente en los tres puntos de solapamiento para Stage A, R1 y R2. Las variantes c=.85,1,1.15,1.30 preexistentes están en `other_versions_summary.csv`: sus bloques sin vecinos exteriores tienen cobertura incompleta expresamente declarada, y c=1.30 solo cubre un bloque. No se extrapola un bloque a 600.316 índices.

El archivo local zCasanya0 tiene cero inversiones. Con el criterio direccional tiene 3.039 fallos globales y 897 finales, frente a 3.092 y 938 de c667+PAV .10, aunque su RMS global es peor (.04560758 frente a .04382589). Por tanto, la afirmación preliminar de que «no mejora» debe limitarse al RMS global y al antiguo criterio simétrico; no describe el nuevo recuento direccional. El barrido aritmético encuentra compatibilidad con X=512, alpha=.20, diferencia máxima 6.984919309616089e−10, pero NO identidad de bytes ni un manifiesto histórico que pruebe su configuración exacta. Su script optimiza corte/alpha con ceros de validación: es una construcción aritmética con hiperparámetros seleccionados con referencia, que se informa por separado. No equivale al ajuste supervisado por cero `zCasanyaX_ideal.txt`, excluido del ranking aritmético. No se localizó aquí ese archivo ideal.

## Procedencia, errores y límites

* El c667 local tiene SHA256 `64d1de134e920c1eb89f61ba5d93c7f949b343bfa0d9ebf5da6fb647c2d790d9`; la proyección global fija tiene `01cc32b9775dd5d46f9d88c11291a79c568521e9bab1bea7022d3c8f8e6710e1`. No son los hashes `dc8d…`/`2857…` de los binarios citados en la incidencia. Las métricas de la proyección coinciden con las allí impresas a su precisión, pero eso no demuestra identidad de archivos. Cuatro reconstrucciones documentadas con dos relojes y dos aritméticas NO resuelven la procedencia de aquellos binarios. Se publica la discrepancia, no una equivalencia inventada.
* La antigua localización bibliográfica del peso de Gonek era imprecisa. `SOURCES_VERIFIED.md` identifica su definición tras (3.4), y el modelo (5.2), sin modificar el informe inicial congelado.
* La identidad `a_k−(e[k+1]−e[k])=gamma[k+1]−gamma[k]` se comprueba como identidad de evaluación. Usa los ceros verdaderos; no se vende como certificado predictivo independiente.
* Un piloto sin incumplimientos no implica ausencia global. Los recuentos del tramo completo se calculan por separado. No se ajustan parámetros sobre ese tramo después de ver los errores.
* `verify_final_tables.py` recalcula las pertenencias comparando gamma directamente con los puntos medios en altura, sin reutilizar la decisión del evaluador principal. Guarda también la distancia más pequeña del cociente a 1 para advertir posibles decisiones sensibles al redondeo. Esta comprobación independiente no es aritmética de intervalos.
* La proyección opcional de Gonek/LeClair es REGIONAL, con halo 1024 contrastado con halo 512, y se identifica así. No se presenta como una proyección global de dos millones de puntos. Esas filas auxiliares se excluyen de la tabla principal de métodos originales.
* Ninguna de estas comprobaciones finitas demuestra RH ni simplicidad global, ni una garantía individual para todos los k. El criterio de puntos medios es una definición operacional de proximidad; no es una demostración de identificación de todo cero de zeta.

## Archivos y reproducción

`outputs/primary_directional_summary.csv` y `matched_final_directional.csv` son las tablas principales con nombres explícitos; las tablas antiguas conservan columnas del criterio simétrico y añaden columnas `directional_*`. Las tablas por cero incluyen ambos cocientes. `outputs/pilot_index_sets.npz` fija los índices y sus contextos. `outputs/global_index/*enumeration.json` guarda el control de niveles; `multiroot_audit.json` documenta la selección excepcional; los archivos `*_final_constructor.json` guardan residuos y presupuestos. Los checkpoints de barrido son reconstruibles, no datos originales.

Orden: `construct_baselines.py`; `evaluate_baselines.py`; `pilot_models.py` (reutiliza caché inicial); `evaluate_pilot.py`; `enumerate_global.py Gonek` y `enumerate_global.py LeClair`; `audit_multiroots.py`; `refine_final.py METODO CORTE` únicamente cuando pasa su control de índices; `evaluate_final.py`; `recover_v17_neighbor.py`; `evaluate_other_versions.py`; `build_report.py`. Las rutas de los datos son las rutas originales del Mac, declaradas en cada script. El núcleo `constructors.py` está en la entrega inicial, un nivel por encima.

Opcional macOS: compilar `fastphase.cpp` con `clang++ -O3 -dynamiclib -framework Accelerate fastphase.cpp -o fastphase.dylib`, ejecutar `fastphase.py` y usar `enumerate_global.py METODO --fast`. Usa la MISMA fórmula, validada frente a NumPy; los checkpoints atómicos permiten reanudar sin repetir los barridos terminados. La compilación y los checkpoints no alteran ningún binario original.
