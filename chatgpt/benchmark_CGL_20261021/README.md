# Benchmark Casaña / Gonek / LeClair — entrega inicial

[Informe con resultados y bloqueos](INFORME_INICIAL.md) · [Descargar ZIP completo](benchmark_CGL_20261021_ENTREGA_INICIAL.zip) · [Métricas CSV](results_v2/benchmark_resumen.csv)

Se ejecutaron el piloto Python de 1.000 índices, la evaluación de Lambert y c667 sobre 2.001.052 registros y la reconstrucción completa de c667, idéntica byte a byte al original. El ZIP contiene 72 archivos: scripts, configuraciones, resultados, fuentes, registros y gráficas. Los mismos archivos están disponibles descomprimidos en esta carpeta.

- RMS global Lambert: 0.18806629977698566.
- RMS global c667: 0.04398854715231307; 962 saltos no positivos.
- La comparación completa M1–M4 sigue pendiente: no se ha validado la enumeración ordinal global de los modelos. Se documentaron dos soluciones de la ecuación finita de LeClair para k=1, b=8191, y la falta de cobertura de la extensión de Stage A v17 en k=2.
- La continuación v17 comprueba cinco puntos por segmento; no es una certificación de todo el intervalo.

El informe y el ZIP se conservan tal como fueron entregados localmente antes de esta publicación; sus referencias al estado del repositorio describen ese momento. Los códigos fuente de v17 se consultaron en el commit 24d9d84862bced814fea8b9a8cae8bf97ac4b5a7. La publicación añade esta entrega a chatgpt/ y una entrada al registro compartido.

SHA-256 del ZIP: `6657ad5842cb75e74f5d5b5157d6190d85e66898eda50233150fc889a077c320`.

[Integridad de los archivos](SHA256SUMS.txt) · [Estado y alcance](STATUS.json) · [Entorno](environment.json) · [Referencias verificadas](references_verified.json)

Los datos originales grandes no se incluyen en el ZIP. Las rutas y hashes necesarios para repetir los cálculos constan en el inventario y en el informe. Esta entrega contiene experimentos finitos y una auditoría de implementación; no constituye una prueba de RH.
