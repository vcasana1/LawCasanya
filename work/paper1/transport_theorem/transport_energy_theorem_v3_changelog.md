# transport_energy_theorem v3 — cambios respecto a v2 (segunda auditoría de ChatGPT, 2026-10-24)

Auditoría literal: work/display/2026-10-23_aportes_externos_transporte/11_segunda_auditoria_transport_energy_theorem_v1.txt (hecha sobre v1; numeración de v1).

| Punto | Comprobación | Cambio en v3 |
|---|---|---|
| Lema de muestreo (4.6 en v1, 4.7 en v2/v3) falso tal como estaba enunciado: f(t)=cos(t log 6) da σ_f=0 | Correcto. La prueba usa la representación de f en el modelo como Σ_p f_p(θ_p), que solo existe si f está soportado en potencias de primos. | Hipótesis añadida: f soportado en potencias de primos p^m ≤ N, sin término constante, con coeficientes reales; la prueba dice dónde se usa y que f' es de la misma clase. Frase explícita en §7.1: Q^♭, Q^{♭(m)} y Q̃^{(m)} pertenecen a esa clase. Los demás usos de σ² (P_0, P_1, P_2 y Π en el Lema 4.6) ya eran sumas sobre potencias de primos. |
| J_0 = ⌈32e²s⌉ | Ya corregido en v2. | — |
| N_0, Mertens, ε reales | Ya corregidos en v2. | — |
| I5 | Ya resuelto en v2 (Lema 4.3 con prueba propia; la Prop. 8.17 está en manuscript/ordinal_prime_cutoff_v14.tex). | — |

Enunciado del teorema sin cambios.
