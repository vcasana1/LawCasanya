# Archivo de investigación del chat — τCasanya, pesos primos y localización ordinal
Fecha de archivo: 2026-11-02
Estado: **RECONSTRUCCIÓN CRONOLÓGICA, NO TRANSCRIPCIÓN LITERAL COMPLETA**.
Origen: conversación actual del proyecto Möbius. El sistema no proporciona una API de exportación del historial íntegro. No confundir este documento con el texto exacto de todos los mensajes.
Política: no modificar manuscritos; referencia zeta, jamás utilizar los ceros verdaderos en la construcción de τCasanya.

## Alcance e intención del usuario
El usuario solicita investigar la cercanía de las ordenadas sintéticas τCasanya a las verdaderas γ_k, junto con primos, π, M, ζ sintéticos, centroides y sus conexiones hacia RH. La investigación es **ordinal**, centrada en distancias y localización de ordenadas, no en construir ceros a priori sobre Re(s)=1/2. El usuario pidió ejecutar programas, no detenerse en propuestas. En último turno pidió subir **el chat completo** a GitHub; esto requiere exportación literal que aún no está disponible.

## 1. Tres secuencias de ordenadas
- Verdaderas: γ_k, fuente `zeross(6).bin` (archivo aportado en la conversación, 2.001.052 doubles).
- Fondo RvM: γ_k^{RvM}, definido por N_0(γ_k^{RvM})=k-1/2, N_0(t)=t/(2π) log(t/(2πe))+7/8.
- Ordenadas τCasanya del manuscrito IJNT v5, mediante subniveles: τ_k^C = meas{t≥0: N_0(t)+clip_H(Φ(t))< k-1/2}. La fase original utiliza primeros m_j=floor(2^{j/2}) primos e interpolación diádica. Nunca confundir estos τ con el binario histórico zCasanya.bin.

## 2. Primeros 100 y 10.000
En los 100 primeros el chat reportó RMS RvM ~0,463260, RMS τC original ~0,080621; mejora punto a punto 95/100; excepciones k=1,16,40,78,82. Se generaron `zTaucs.bin` (10.000 doubles), tabla de cruces y un script. Posteriormente se probó m_j(a)=floor(a 2^{j/2}) con distintos a y versiones dependientes de k. Las cifras se deben tratar como reportes del chat, no como auditoría formal. Los programas y datos son parte de los entregables anexos, que no se incluyen en este archivo de texto.

## 3. Criterio operacional de distancias ensayado
Se examinó |τ_k^C−γ_k| < (γ_{k+1}−γ_k)/2, k≤10000. El usuario busca una **ley coherente** de selección de primos, no un ajuste arbitrario por cero. Es una condición de precisión ordinal finita, NO existe todavía un teorema demostrado que haga esta desigualdad suficiente para RH.

Primero 300/300 cumplieron con a=8. En 10000, cifras reportadas:
- a=1: 18 incumplimientos, RMS 0,044586.
- a=8: 5 incumplimientos, RMS 0,023422; k=1496,3777,4765,5700,6709.
- a=12: 4, RMS 0,020587.
- a=16: 4, RMS 0,019154.
- a=24 corregido: 3, RMS 0,017406.
- a=32 corregido: 3, RMS 0,016633.
Los primeros resultados a=24/32 tuvieron error por truncamiento de la lista de primos; después fueron recalculados con suficientes primos.

Se probaron ventanas desplazadas, núcleo más ventana, leyes exponenciales y saturadas. Ventanas que eliminan primos pequeños rindieron mucho peor que conservar primeros primos; esto no prueba optimalidad de cada primo pequeño.
Una ley saturada a_j=32−31 exp(−0,18j) reportó 2 fallos y RMS 0,017800; otra a_j=64−63 exp(−0,35j), 2 fallos y RMS 0,015300.

## 4. Parejas persistentes
Los índices críticos k=4765/4766 y k=6709/6710 tienen:
- γ_4765 ≈5229,198557; γ_4766≈5229,241811, gap verdadero≈0,043254.
- γ_6709≈7005,062866; γ_6710≈7005,100565, gap≈0,037698.
- Gaps RvM ≈0,934418 y 0,895480.
- Con ley saturada 64: e_4765≈−0,060059, e_4766≈+0,061492; e_6709≈−0,060656, e_6710≈+0,058939.
- Errores de centros ≈+0,000717 y −0,000858; gaps sintéticos≈0,164805 y 0,157293.

Importante: usuario **no quiere limitar el análisis a gaps**, sino estudiar fallos de localización individuales de τC respecto a γ. El gap es solo umbral/diagnóstico. También k=1 tiene un error absoluto considerable.

## 5. Pesos de fase Euler
Se introdujo la fase ponderada y compensada
Φ_X^W(t)=−(1/π)∑_p∑_{r≥1} W(log(p^r)/log X) sin(rt log p)/(r p^{r/2}) − Π_X^W(t).
Es indispensable verificar el término del polo Π_X^W(t), omitido en varios experimentos exploratorios.

Peso Selberg: W(u)=1 hasta 1, W(u)=2−u en (1,2), cero después.
Familia continua: W_b(u)=1 hasta 1; para v=u−1 ∈(0,1), W_b(u)=1−v+b v(1−v); cero desde 2. Candidato b=1/4, con experimentos en fase que mejoraron Selberg. Una validación con X=200 sobre ordinales reportó 0 incumplimientos en 5001–5500, pero 1 en 4700–4800 y 1 en 6650–6760.

Se propuso DBSRH(W): lim_{X→∞}τ_k^C(X)=γ_k para todo k. El paso de convergencia puntual de fase a medidas de subnivel requiere controlar correctamente recorte, soporte y conteo, así como el término del polo; la equivalencia DBSRH↔RH es una pregunta abierta, NO teorema.

## 6. Fundamento del teorema IJNT
Cadena declarada por el usuario: transferencia determinista de subniveles, lema de momentos cúbicos de gaps y cuarto momento de F−N. Resultado original medio-cuadrático ≪1/log²T. El número de primeros primos m_j~√U entra en el cuarto momento. Para a fijo, extender a m_j(a) puede conservar el orden del teorema con constantes dependientes de a, siempre que las estimaciones concretas se verifiquen. Para W suave con X=T^δ, δ<1/4, el argumento de Montgomery–Vaughan, Mertens y Fujii sugiere extensión del cuarto momento; compensador exacto y potencias primas pendientes de cerrar.

## 7. Forense de fases y localización
Con X=200 en las dos parejas, F'_W en centro ~5; para reproducir un salto de uno sobre el gap real se requeriría pendiente media ~23 y ~27 (guía local, no identidad puntual). W_{1/4} mejora el error de conteo central: cerca de −0,002704 y −0,003848, frente a Selberg −0,007303 y −0,008300.
Se analizaron bandas de potencias primas hasta 40000; las fases y derivadas de primos pequeños e intermedios contribuyen a la pendiente de forma variable. Ejemplos de signos en 4765: primos 5,7,19,23,29,59,79 favorecen la compresión, 17,31,107 se oponen localmente. Esto no autoriza selección universal de esos primos.
Optimización LP de pesos continuos por siete bandas logró pendientes ~5,85–6,21 y gaps sintéticos ~0,16–0,18, pero elevó el defecto del conteo fuera de muestra ~3–4 veces. No sustituir el peso W_{1/4} por estos perfiles.

## 8. Estudio global de localización
Definiciones e_k=τ_k^C−γ_k; c_k=(e_k+e_{k+1})/2; d_k=(e_{k+1}−e_k)/2. Identidad e_k²+e_{k+1}²=2(c_k²+d_k²). El chat reportó que RMS(d_k)>RMS(c_k) para cinco construcciones, entre ellas saturada 64 con RMS de centro ~0,008372 y deformación ~0,012006. Señal puramente sintética R_k^C=(τ_{k+1}^C−τ_k^C)/(2π/log(τ_k^C/(2π))) detectó ambos incumplimientos en el 1% de gaps sintéticos más pequeños, pero predice peor los errores absolutos grandes (AUC reportado ~0,623).
Bajo cruces simples y transversales y sin cambio topológico de cruces:
∂τ_k/∂a_ν=−∑_j (∂_{a_ν}F(t_{k,j}))/|F'(t_{k,j})|.
Esta derivada completa de subniveles, frente al cálculo de raíz única, permite formar una matriz de sensibilidad de posiciones individuales a bandas de primos.
Prioridad posterior: encontrar una señal aritmética que indique **dirección de corrección** sin consultar γ, conservando el cuarto momento.

## 9. Archivos referenciados por el historial
Durante el chat se generaron múltiples archivos locales bajo /mnt/data, incluyendo:
- zTaucs.bin; zTaucs_a8_10000.bin; zTaucs_sat_1_64_c035_refinado.bin;
- generar_zTaucs_10000.py; generar_zTaucs_alpha.py; seleccion_primos_dependiente_k.py;
- ley_saturada_10000/comparacion_10000.csv, ensayos_saturados_10000.zip;
- DBSRH_pesos_pruebas.zip;
- forense_pares/prime_powers_full.csv, summary_bands_rvm.csv, top_contributions.csv, optimizar_bandas.py, validar_pesos_lp.py;
- estudio_10000_localizacion.csv, estudio_10000_resumen.csv, estudio_10000_senales_sinteticas.csv, estudio_sensibilidad_bandas_X200.csv.
Estos archivos no deben considerarse adjuntos a este registro solo por mencionarse; su subida íntegra requiere archivos presentes accesibles y una operación de GitHub específica.

## 10. Advertencia de integridad del archivo
Este documento conserva la cronología, fórmulas, cifras y límites clave, pero NO es una reproducción literal de los mensajes completos y NO incluye cada tabla, cada frase del usuario ni los archivos binarios. No publicar ni presentar como «chat completo». Para el archivo literal se requiere el export original de la conversación.
