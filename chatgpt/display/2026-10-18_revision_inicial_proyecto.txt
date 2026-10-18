He recuperado el estado directamente de GitHub, leyendo los archivos en el orden indicado y contrastando programas y salidas. **No he modificado archivos ni ejecutado experimentos.**

1. **Último commit de `main`:** [`f9c437c`](https://github.com/vcasana1/LawCasanya/commit/f9c437c6a45cd44e8a78e1c3f54662dcf8b3a6b5), del **18 de octubre, 17:01:55 hora española**, sobre el protocolo de publicación. El último avance numérico está en [`9df20d6`](https://github.com/vcasana1/LawCasanya/commit/9df20d6cb1a9511504bbe40f0eddb2f286d686ed).

2. **Trabajos terminados:** los tres cálculos —residuo de Newton, deriva por cocientes y regla analítica de cortes— están ejecutados y publicados. También la continuación hasta \(c=1{,}30\) y su comparación en el bloque de **10.000 índices \(1.636.863\)–\(1.646.862\)**:

   | Método | RMS frente a \(\gamma_k\) |
   |---|---:|
   | zCasanya | 0,040281 |
   | R2 | 0,033225 |
   | \(c=1{,}00\) | 0,021238 |
   | \(c=1{,}15\) | 0,016436 |
   | \(c=1{,}30\) | **0,012760** |

   Son resultados de ese bloque. La evaluación R2 sobre los **600.316 índices finales completos** da RMS **0,033144**, sin cruces. [Resultados publicados](https://github.com/vcasana1/LawCasanya/tree/main/work/v15_prep/outputs).

3. **Resultado matemático más avanzado:** en la [v14](https://github.com/vcasana1/LawCasanya/blob/main/manuscript/ordinal_prime_cutoff_v14.tex), el teorema de iteración uniforme establece, incondicionalmente y sin ordenadas en la construcción, que tras \(m^*=\log^*T+O(1)\) pasos,
   \[
   \frac1{\#I_T}\sum_{k\in I_T}
   \bigl(x_k^{(m^*)}-\gamma_k\bigr)^2
   \ll\frac1{\log^2T}.
   \]
   Es control de **\(O(1)\) espaciados medios en media cuadrática**. También figura la cota puntual asintótica \( \limsup_k|\gamma_k^{\mathrm{RvM}}-\gamma_k|<0{,}60832\). He localizado sus enunciados y demostraciones; esta revisión inicial no constituye una nueva auditoría completa.

4. **Problemas abiertos:** continuación rigurosa hasta cortes arbitrarios; error ordinal tendiendo a cero; identificación del límite con cada \(\gamma_k\); control de extremos y deriva del paseo. El posible suelo RMS cercano a \(0{,}006\) es **un ajuste de cuatro puntos**, no un teorema. Además, los programas actuales comprueban pendientes por muestreo: **la certificación por intervalos sigue pendiente**. Algunas notas antiguas aún dicen «no ejecutado»; el LOG y las salidas posteriores aclaran su estado.

5. **Acceso:** lectura comprobada y permisos actuales de escritura confirmados por GitHub (`push: true`). No he realizado un commit de prueba, respetando tu orden de revisión exclusivamente de lectura.

La **v14 permanece congelada** y no he creado v15.
