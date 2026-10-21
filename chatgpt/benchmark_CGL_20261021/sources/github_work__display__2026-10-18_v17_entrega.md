La v17 está hecha, compilada (143 páginas, sin errores ni referencias indefinidas, con el hover regenerado) y subida a `main` en `work/v17`.

**Corrección de unidades.** Las cifras de error se daban "en separaciones medias" cuando en realidad estaban en unidades de altura. Ahora se dan en las dos unidades. La separación media en el tramo intacto es 0.526.

| Método | Altura | Separaciones medias |
|---|---|---|
| Reloj RvM | 0.177 | 0.337 |
| zCasanya | 0.0406 | 0.077 |
| Stage A | 0.105 | 0.199 |
| R1 | 0.047 | 0.090 |
| R2 | 0.0331 | 0.063 |
| Continuación $c=0.85$ (bloque) | 0.0266 | 0.050 |
| Continuación $c=1.00$ (bloque) | 0.0212 | 0.040 |
| Continuación $c=1.15$ (bloque) | 0.0164 | 0.031 |
| Continuación $c=1.30$ (bloque) | 0.0128 | 0.024 |

Esto está corregido en el resumen, en la introducción, en las conclusiones (punto 6, "What is missing" y la vía de la Casaña Law) y en el ajuste cuadrático, que ahora indica que es en altura. Además, las leyendas de las Tablas 11 y 12 dicen ya que los errores son en altura.

Las cifras en separaciones salen del programa nuevo `opc_units_v17.py` (en `work/v17/code`, con su salida en `work/v17/outputs`), que está en el apéndice. Las afirmaciones que ya estaban en unidades de ceros, como el $O(1)$ del Teorema D y el "error menor que una décima de separación" de la ley de Gram corregida, eran correctas y no han cambiado.

El zip compila tal cual (lo he probado descomprimido) y el `.tex` también compila suelto.
