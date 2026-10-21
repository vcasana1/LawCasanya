# Variante cuadrática L2 basada en v14: ejecución sin ajuste post hoc

Protocolo fijado antes de evaluar el nuevo predictor: `PROTOCOL.json`, SHA256 `dc895477e4be3351e691d7b358a67987e1647371e248d451235ad72e77162872`. No se han elegido cortes ni coeficientes mirando los errores. Los bloques de referencia ya se habían visto: comparación retrospectiva/exploratoria, no validación independiente.

El constructor minimiza exactamente el objetivo L2 de la nota analítica, mediante cargas analíticas de sombreros y un QP con restricciones de pendiente. Usa X=sqrt(T/2) y todos los factores de Euler de primos p<=X. Las potencias se suman hasta un resto absoluto certificado de carga <=1e-12: esto es una tolerancia aritmética, no un corte del modelo elegido con ceros. Los nodos extremos tienen cargas propias. La parte suave se integra con una serie estable y resto <=1e-13. ADMM usa factorización tridiagonal y criterios de parada primal/dual, sin gamma. El backend Accelerate se reutiliza de `../localgap_v1/fastphase.{py,cpp,dylib}`.

La cota asintótica teórica no proporciona aquí constantes efectivas o un T0 explícito. Los bloques bajos son experimentos finitos. La construcción es monótona DENTRO de cada bloque; las uniones diádicas no se reparan ni ordenan y deben comprobarse por separado. Los niveles son siempre k-1/2, con los k originales. No se confunde el ordinal de todas las raíces de otro modelo con estos niveles.

## Reanudar y evaluar

1. `python3 construct.py > outputs/run.log 2>&1` (para conservar el log anterior al reanudar, usar `>>`). Omite bloques completos; recupera checkpoints de iteración. El audit hook prohíbe abrir zeross en el constructor.
2. `python3 verify.py` comprueba cargas por cuadratura y un QP pequeño contra SLSQP sin ceros verdaderos.
3. Solo tras terminar el constructor: `python3 evaluate_results.py`. Este programa abre los ceros exclusivamente para evaluar. Conserva el criterio principal de celda sintética propia y el mínimo simétrico como criterio más fuerte separado.

`outputs/progress.json` es el estado actual atómico; `block_T.npz` conserva cada bloque terminado; `checkpoint_T.npz` guarda y,z,dual e iteración cada50 pasos durante el QP. `predictions.npz` se escribe antes de abrir gamma. No basta la existencia de un script para declarar un resultado: ver métricas y auditorías ejecutadas.

Las comparaciones históricas de Gonek/LeClair/c667 están en `../localgap_v1/outputs/matched_final_directional.csv`. Su presupuesto constante97/309/1028 no coincide exactamente con el presupuesto diádico variable de esta variante; no se presenta como comparación a igual número de primos.

No se modifica v14 ni ningún binario original. Esta variante no hereda el cuarto momento ni el transporte D′(d), y sus pruebas de identidad no demuestran precisión individual.

## Resultados ejecutados

| Región | N | RMS | MAE | Máximo absoluto (k) | Incumplen celda propia | Peor cociente (k) |
|---|---:|---:|---:|---:|---:|---:|
| first1000 | 1000 | 0.165337752 | 0.106938484 | 1.608451350 (4) | 0 | 0.920395818 (997) |
| fixed_pilot1000 | 1000 | 0.117951133 | 0.054014105 | 1.608451350 (4) | 0 | 0.983372004 (1400794) |
| pilot_last300 | 300 | 0.054906724 | 0.041499060 | 0.227507090 (1700904) | 0 | 0.983372004 (1400794) |
| high_consecutive_last300 | 300 | 0.055295187 | 0.039988239 | 0.263009268 (2000792) | 0 | 0.996009278 (2000792) |
| final600316 | 600316 | 0.054724036 | 0.040751268 | 0.429706070 (1663325) | 881 | 1.654767703 (1489071) |
| all2001052 | 2001052 | 0.058624996 | 0.043233707 | 1.608451350 (4) | 2763 | 1.654767703 (1489071) |

Todos los2.001.052 índices están cubiertos, sin inversiones (también en las17 uniones diádicas). La evaluación por puntos medios independiente reproduce exactamente los recuentos del evaluador por cocientes. Todos los18 QP alcanzaron las tolerancias fijadas. Las tolerancias son numéricas; no hay certificación por intervalos.

En los600.316 finales:599.435 cumplen y881 incumplen. Frente a c667+PAV:938 incumplimientos y RMS0.040388891, esta variante reduce57 incumplimientos (6.08%) pero empeora RMS a0.054724036 (+35.49%). No demuestra una mejora global ni que la regularización aproxime cada cero. El piloto de300 no detectó ninguno de los881 fallos del tramo completo.

El presupuesto final es97 o128 primos según el bloque, no el mismo presupuesto que todos los comparadores. Gonek97 tiene228 fallos/RMS0.053599006 y LeClair97 tiene189/RMS0.044761300; ambos tenían menos fallos en la comparación histórica, pero no son una comparación exacta a igual presupuesto con el esquema diádico. A309/1028 primos los resultados históricos siguen siendo72/29 para Gonek y81/31 para LeClair. Se reutilizan, no se recalculan ni se atribuyen al nuevo predictor. No se ha hecho un barrido nuevo del exponente tras ver gamma.

Los coeficientes de carga provienen de integrales exactas y no de un ajuste a ceros. Esto da una construcción reproducible y analíticamente motivada; no garantiza que sea precisa. Los datos vistos no se convierten en un test independiente por prohibir zeross en el código. Ningún parámetro se ha cambiado después de esta evaluación.

Auditoría final: los18 QP repetidos producen exactamente las mismas raíces (diferencia máxima 1.4210854715202004e-14). Estacionariedad máxima 5.34e-11; violación de pendiente en variables centradas máxima 9.43e-11. La brecha dual se informa en el primal aproximado: puede ser levemente negativa por tolerancia y no se presenta como certificado exacto de factibilidad o intervalo.
