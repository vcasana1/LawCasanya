# Cota de multiplicidad de GLSS y discusión centroide/pares (25-oct-2026)

- Nota para ChatGPT con la cota mejor publicada: `work/notes/2026-10-25_para_chatgpt_cota_GLSS_multiplicidad.md`. Cadena: $B_T\le\sum m(m-1)$ (GLSS, Thm 2) $\le4\mathsf V_T=\frac13\sum m(m^2-1)$ $\le4\sum u_k(F)^2$.
- Dos posiciones sobre el centroide y los pares, con la resolución tras la revisión de ChatGPT: `work/notes/2026-10-25_centroide_pares_dos_posiciones.md`.
- Nuevos experimentos del centroide (k < 1 400 737): fundir pares + compensar con vecinos (`opc_centroid_compensate.py`, `opc_centroid_compensate2.py`): el desajuste baja ×10–×140 pero no por debajo del error de convergencia 3e-5; ruido ±h en todos los ceros (`opc_centroid_noise.py`): ±0.001 cambia el centroide 0.3–0.9.
- Contexto clásico: flujo de de Bruijn–Newman (Csordas–Smith–Varga 1993; Rodgers–Tao 2020, Λ ≥ 0, cuya prueba usa que sin pares cercanos los ceros serían una progresión aritmética).
