# Huecos de la tauc, pares cercanos, fases de primos y centroide (25-oct-2026)

Respuestas de Claude en el chat de esta sesión, resumidas. Programas y salidas: `work/gaps_tauc/`. Bloques k < 1 400 737 (el conjunto de test no se ha tocado); los γ solo se leen para evaluar.

## 1. Test de huecos, tauc c = 1.30 (opc_gaps_build_tauc.py, opc_gaps_eval.py; outputs/gaps_eval.*, gaps_hist.png)
- 59 998 huecos (k = 300 001…340 000 y 1 380 001…1 400 000). Varianza de huecos: γ 0.167, tauc 0.172 (surmise 0.178). RMS(s_tauc − s_γ) = 0.039; KS = 0.035.
- Suelo duro: ningún hueco de tauc < 0.17. Pendiente de la CDF de huecos pequeños: γ 2.79, tauc 11.8 (GUE 3).
- Suelo: s ≥ 1/sup(F′/Λ) con banda de primos fija; es el argumento de Gonek 2012, §10 (no es nuevo).
- La tauc usada es la de c = 1.30 (AGENTS §5), no un c óptimo; el c óptimo no se puede fijar analíticamente sin conocer F(α) para α > 1.

## 2. La tauc detecta los pares cercanos (opc_gaps_detect.py; outputs/gaps_detect.*)
- Con s_tauc < 0.25 (1.9 % de los huecos) se recuperan el 100 % de los huecos de γ < 0.15; con s_tauc < 0.19, 20 de 23 señalados tienen s_γ < 0.15 (enriquecimiento ×260).
- Identidad exacta: s_γ = s_tauc + e_k − e_{k+1}. Mecanismo (bajo RH, primer orden): F ≈ N * K_X con núcleo de anchura δ ≍ 1/(2πc) espaciados; da a la vez el suelo y la detección.

## 3. Fases de primos en los pares cercanos (opc_phases_close.py; outputs/phases_close.txt)
- Media de cos(γ log p) en el punto medio: todos los huecos −0.04…−0.07 (Landau–Gonek exacto a 4 decimales); s < 0.15: −0.20…−0.29 para p = 2…23; control x = e (Λ(e) = 0): sin sesgo.

## 4. Landau–Gonek para pares (opc_pair_landau.py; outputs/pair_landau.txt)
- Fórmula explícita: Σ_{γ≠γ'} p^{iγ} h(γ'−γ) ≈ b_p N [∫h + ĥ(α_p)] − autotérmino. Acierta al 1–13 % con ventanas sinc²(x/a), a ≥ 1 (rango de Montgomery); falla para a < 1. Por debajo de un espaciado faltan los términos fuera de la diagonal (pares de primos).
- Literatura: Ford–Soundararajan–Zaharescu 2009 (n.º 102): "Even assuming RH, we are unable to establish Conjectures 1 and 2". No se conoce a nadie que conjeture RH ⇒ PCC.

## 5. Centroide y pares (opc_centroid_pairs.py, opc_centroid_subspacing.py; outputs/centroid_*.txt)
- C_N(1) con γ: 0.7769 + 0.7679i (límite bajo RH e^{-1/2}V_+(1), v24 Thm 5.15).
- Separar hasta s = 1 los 4256 pares con s < 0.15: el centroide se va a 2.38 + 3.21i; max|S| sube de 4.7 a 10.8.
- Fundir esos mismos pares en ceros dobles: el centroide cambia 0.06; max|S| 4.67. Con s < 0.30 cambia 0.55; con s < 0.50, 3.68.
- Conclusión: el centroide fuerza la estructura de pares a escala ≥ 0.3 espaciados (la que RH controla vía Montgomery, |α| < 1) y es ciego por debajo de ~0.15. No sirve para deducir GUE desde RH; bajo RH solo se garantiza ≥ 2/3 de ceros simples.

## 6. Traspaso
- `work/notes/2026-10-25_HANDOFF_tauc_es_GUE.md` (también en el proyecto como claude/HANDOFF-tauc-es-GUE.md) y `work/notes/2026-10-25_robustez_GUE_tauc_a_gammas.md` (teorema de robustez).
