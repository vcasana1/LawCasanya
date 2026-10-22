# Índice de dos hilos de Casanya (no son transcripciones completas)

Resumen sacado de la búsqueda en los chats del proyecto "Möbius Total". Solo se incluye lo técnico; el contenido de los resultados ya está en este repositorio (work/paper1, work/notes, work/LOG.md).

## Hilo 1: "Casaña method for prime approximation"
- Enlace: https://claude.ai/chat/b2ed7b2e-dac0-4a17-afef-d5742ee02a63 (última actualización 2026-10-21)
- Comparación en Octave de π, π_RVM y π_tauc, con τ^c construidos por el método v17 (raíz monótona certificada más continuación), K = 17 061 ceros. RMS 0.0219 frente a los ceros verdaderos; primos a medio nivel dentro de 0.5 de los verdaderos en 123/168 primos, frente a 20/168 con el reloj RvM solo. Sumas de Landau: π_tauc reproduce el término −(T/2π)Λ(n)/√n en potencias de primo; el reloj solo no.
- Resultado analítico: |π(x) − π_tauc(x)| ≤ C_ε x^{1/2+ε} para todo ε > 0 implica RH (representación de Mellin; Φ = log ζ − log ζ_tauc se extiende holomorfa más allá de Re s = 1/2).
- Identidad exacta para corte fijo Y: log ζ_κ(s) = log ζ_RVM(s) + log P_Y(s) − log P_Y(1) + H_Y(s), con H_Y holomorfa y sin ceros en Re s > 1/2. El término principal de log ζ_tauc es el producto de Euler finito de los primos que usa la construcción. Versión híbrida con Y_k = (τ_k/2π)^{1.30} solo esbozada (pendiente para la siguiente versión; ver work/notes/opc_pendiente_siguiente_version.md).
- Paper I (prime_corrected_clock): v11.2 → v14 en work/paper1/vNN; Teorema F (ceros simples a partir del defecto ordinal) y Teorema G (producto de Euler finito).

## Hilo 2: "Casañá I conecat"
- Enlace: https://claude.ai/chat/67b502a5-40dd-4d26-8c31-955eaf5ea770 (última actualización 2026-10-20)
- Estado: v11 (61 pp., commit dc021ad), Teoremas A–E, reloj regularizado D′ y corte fijo D″. Sin v12 sin orden expresa.
- Renumeración de LIBRARY TOTAL (310 PDFs) por autor; INDEX.md único.
- Cota de constantes (H*, C, exponente 160 del lema de muestreo): no da índice correcto para casi todos los ceros con los métodos actuales; la identidad exacta del Teorema A reduce la cuestión a acotar Q₂, medido en los índices de entrenamiento (k ≤ 1 400 736): Q₂ ≈ 0.095–0.115 según el corte c.
- Ruta incondicional hacia proporción positiva de ceros simples en la recta a partir del defecto u_k; comparada con los resultados incondicionales de 2026 de "más de dos tercios" (arXiv:2608.13637, 2609.02882, 2610.08965); optimización SLSQP: el certificado del autor domina para b < 2.597. Cota tipo Selberg explícita con Hiary–Zhao (arXiv:2512.14907): cierta pero muy débil.
- Nota LaTeX "Simple zeros on the critical line from the Euler-phase defect": material pendiente, sin integrar.
- Dos revisiones externas de v11.2 y las correcciones de estilo del autor, guardadas en work/paper1/pendiente_siguiente_version/, sin aplicar.

## No copiado
Las transcripciones completas de ambos hilos. Para subirlas hay que pegarlas aquí o pedir que se lean por páginas, lo que gasta bastante.
