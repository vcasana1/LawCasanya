# transport_energy_theorem v5 — fusión con el v4 de ChatGPT y revisión completa (2026-10-24)

Fuente externa, verbatim: work/display/2026-10-23_aportes_externos_transporte/13_transport_energy_theorem_v4_chatgpt.tex. Está hecho sobre la v3 de Claude: no lleva las correcciones de la introducción ni de Sobolev de la v4 de Claude.

## Tomado del v4 de ChatGPT
- Lema 4.7 (muestreo) en su redacción: Δ_f = (2‖f‖_1)^{4q}N^{4q}/T explícito, ecuación (eq:sampling_corrected) con las dos formas (σ_f^{2q}+Δ_f^{1/2}) y (σ_f^{2q}+T^{-1/4}), error de tiempo (eq:sampling_time_error). Matemáticamente igual a la v4 de Claude; está más detallado.
- Observación 4.8 (aplicaciones del muestreo): q∈{1,2}, N=X_2², ‖f‖_1 ≤ 2X_2 log X_2², σ_f² ≪ H_0 uniformemente en m (≪ H_0 log² X_2² para Q^♭′).
- Menciones del error aditivo en los Lemas 7.1 y 7.3.

## Mantenido de la v4 de Claude
- Introducción: Theorem D [Thm 7.3] da solo ≪ log log T a c fijo (en el v4 de ChatGPT seguía la cita falsa "Theorem D'' [Thm 7.5]" y los porcentajes de la Tabla 7).
- Sobolev en el reloj con prueba propia (en el v4 de ChatGPT seguía "[proof of Lemma 5.11]", que no contiene esa desigualdad).

## Correcciones nuevas de la revisión completa
| Sitio | Problema | Corrección |
|---|---|---|
| Lema 4.4 (Hoeffding) | Enunciado solo para f_p con senos; el lema de muestreo lo aplica a polinomios con cosenos y senos. | f_p(θ) = Σ_{m≥1}(b cos mθ + b′ sin mθ), real; la prueba no cambia (media cero y acotado). |
| Lema 4.9 (medias cuadráticas en el reloj) | ⟨W²⟩ = ⟨W_pr²⟩ + O(√(L/Y)): el término cruzado da √L·Y^{-1/4}, no √(L/Y). | O(√L Y^{-1/4}) + O(Y^{-1/2}); sigue siendo o(1). |
| Lema 4.6 (multiplicidad) | |y_k| ≤ T^{1/2} no basta para ϱ_k ∈ [T−T^{1/2}, 2T+T^{1/2}] (τ_k ∈ [T−1, 2T+1]). | |y_k| ≤ ½T^{1/2} para T ≥ T_0. |
| Lema 7.1(iii) | σ²(P_2) acotado escribiendo Σ p^{-m}, que no es la varianza auxiliar definida. | σ²(P_2) ≤ π(Z)(3.5/(πZ))² ≤ 2/Z. |

Revisado línea a línea el resto: pasos A y B, Lemas 4.1–4.3, 4.5, 4.6, 7.2–7.5, prueba final y corolario; constantes 100e², 8e²s/J_0, ξ̂²σ_1² ≤ 24, rangos de momentos (q ≤ H_0²/40 para P_0, q ≤ √H_0/40 para P_1), altura T^{c+η_T}, función característica de P_0 y L = H_1/(4π²)+O(log H_1). Sin más cambios. Enunciado del teorema sin cambios.
