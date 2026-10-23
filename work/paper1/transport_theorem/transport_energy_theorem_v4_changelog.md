# transport_energy_theorem v4 — cambios respecto a v3 (auditoría de ChatGPT de la v3, 2026-10-24)

Auditoría literal: work/display/2026-10-23_aportes_externos_transporte/12_auditoria_transport_energy_theorem_v3.txt (la llama "lema 4.6"; en v3/v4 es el Lema 4.7).

| Punto | Comprobación | Cambio en v4 |
|---|---|---|
| Lema de muestreo falso tal como estaba: con coeficientes ε→0 la condición de longitud admite N enorme y fases casi iguales (K primos en (N(1−T^{-2}),N]), y ⟨f²⟩ ≍ K²ε² frente a σ_f² = Kε² | Correcto. La prueba da un error aditivo (comparación tiempo/modelo, Lema 4.5) que no escala con σ_f; el enunciado lo había convertido en multiplicativo. | Enunciado: ⟨f(ϱ)^{2q}⟩ ≪ κ^{1/2}(σ_f^{2q}+T^{-1/4})(1+𝔟_T log N). Prueba con los dos errores aditivos escritos (2T^{-1/2} para f^{4q} y (log N)^{4q}·2T^{-1/2} para f'^{4q}). En §7.1: cada aplicación solo usa σ_f² ≪ H_0 (≪ H_0 log² X_2 para Q^♭′), y T^{-1/4} se absorbe. Con la nueva forma el contraejemplo no contradice: la condición da K²ε² ≤ T^{1/4}N^{-4}/4 ≤ T^{-31/4}. |
| Comprobar (I1)–(I4) contra la v14 | Hecho contra manuscript/ordinal_prime_cutoff_v14.tex: Thm 5.1 (constantes absolutas, todo 2≤X≤T^{1/2}), Lemma 7.2 (todo 2≤X≤T^{1/2}), Prop 8.1 (j=2, requiere x^{(1)}>2π: se cumple por |y_k|≤T^{1/2}), Thm 8.5 (mismos X_1=T^{H_0^{-1/2}}, X_2=T^{H_1^{-1/2}}; la cota de χ_2 sale de su prueba vía la cuarta potencia de e_1). Ecuaciones (2.2), (2.5), (2.10), (7.1) y Lemma 8.3 con esos números. | Sin cambio. |
| (al comprobar las citas) | La introducción de v1–v3 decía "The upper bound of the same order is Theorem D'' [PaperI, Thm 7.5]": falso. En la v14, 7.5 es el Corolario "A cutoff read off the clock" (corte local variable), y Theorem D (Thm 7.3) para c fijo solo da ⟨r²⟩ ≪ log log T. Las cifras 87–98% de la Tabla 7 tampoco se usan. | Frase sustituida: Theorem D [Thm 7.3] da solo ≪ log log T a c fijo; la Question 13.2 pregunta si el transporte cancela al defecto, como sugiere la Tabla 7; el Teorema 1.1 dice que no en media cuadrática. |
| (al comprobar las citas) | "[PaperI, proof of Lemma 5.11]" para la desigualdad de Sobolev en el reloj: el Lema 5.11 de la v14 es lem:maximal_primes, no contiene esa desigualdad. | Sustituida por su prueba de una línea. |

Enunciado del teorema sin cambios.
