# transport_energy_theorem v2 — cambios respecto a v1 (respuesta a la auditoría de ChatGPT, 2026-10-23)

Auditoría literal: work/display/2026-10-23_aportes_externos_transporte/10_auditoria_transport_energy_theorem_v1.txt

| # | Punto de la auditoría | Comprobación | Cambio en v2 |
|---|---|---|---|
| 1 | N_0 definido como θ/π+1 | Correcto: la v14 (manuscript/ordinal_prime_cutoff_v14.tex, eq. (2.2)) usa N_0 = Θ_0/π+1 = (t/2π)log(t/2πe)+7/8. La prueba solo usaba N_0(τ_k)=k−1/2 y dτ/dx = 2π/log(τ/2π) (eq. (2.5)), que son las de la v14. | §1: N_0(t) = (t/2π)log(t/2πe)+7/8 [PaperI, eq. (2.2)]. |
| 2 | Lema 7.3: 2(8e²s/J_0)^{J_0/2} ≤ 2^{1−J_0} falsa con J_0=⌈24e²s⌉ | Correcto (da 3^{−J_0/2}). | J_0 = ⌈32e²s⌉: (8e²s/J_0)^{J_0/2} ≤ 4^{−J_0/2} = 2^{−J_0}; cota 2^{1/8}·2^{−J_0} ≤ 2^{1−J_0}. J_0 ≍ H_0/H_1 sin cambio; rangos de momentos y altura (Lema 7.4) siguen valiendo. En el Lema 7.5 la cota del resto del modelo se escribe explícita: √2(16e)^{−J_0/2} ≤ 2^{1−J_0}. |
| 3 | Prop. 8.17 (I5) no está en la v14 | La auditoría miró work/paper1/v14/…/prime_corrected_clock_v14.tex. La Prop. 8.17 sí está en manuscript/ordinal_prime_cutoff_v14.tex (línea 1803), que es el fichero que cita la bibliografía. | Aun así se elimina la dependencia: nuevo Lema 4.3 (casi ortogonalidad, 0<b≤1/2) con prueba completa (Kusmin–Landau + segunda derivada de van der Corput [GK, Thm 2.2] + conteo de pares). Da ‖G−I‖ ≪ T^{b−1}log T + 1/log T (mejor que (log T)^{−1/4}). Entradas de Paper I: (I1)–(I5). |
| 4 | O(R_1^{−1/2}) en (4.2) no justificado | Correcto: el error de Mertens es O(1/log R_1). | (4.3) [antes (4.2)]: O(1/log R_1), con la deducción escrita. Solo se usa como cota superior con O(1). |
| 5 | ε_{p,m} deben ser reales | Correcto. | Definición: ε_{p,m} ∈ [−1,1] reales. Todos los Π usados (S_{X_1}, P_0+uP_1, P_0+P_1+v(P_2+E_1), uP_0) cumplen. |

Revisión adicional de los Lemas 4.6 (multiplicidad), 4.7 (muestreo) y 7.3 (restos), pedida por la auditoría (§6): recorridas todas las desigualdades; sin más cambios. Nota: las condiciones de altura de los Lemas 4.7 y 7.1 exigen T ≥ T_0(c) con T_0 muy grande (por ejemplo (4X_2)^8 X_2^{16} ≤ T^{1/2} pide H_1 > 2304); el teorema es asintótico y no se modifica.

Numeración: los lemas 4.3–4.7 de v1 pasan a 4.4–4.8; (4.2) pasa a (4.3).
