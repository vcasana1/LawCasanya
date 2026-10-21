## Verificación individual de las correcciones v11.2 → v14

He contrastado los puntos de las dos auditorías anteriores con el código LaTeX de la v14, no solo con sus enunciados.

Respecto de Fujii, la v14 contiene en las líneas 824–852 una explicación detallada de los rangos, las constantes independientes de \\(k\\), las correcciones de 1981 y una vía alternativa mediante Korolev. Dado que indicas que Claude ya cotejó esas afirmaciones con los originales, no mantengo la objeción de falta de verificación bibliográfica. Mi examen se limita a comprobar que la aplicación interna respeta las hipótesis declaradas.

### Resultado de las 11 observaciones anteriores

| Nº | Observación de la v11.2                                           | Estado en v14                                             |
| -- | ----------------------------------------------------------------- | --------------------------------------------------------- |
| 1  | Interpretación de \\(\lvert u_k\rvert<1/2\\) como índice correcto | &#x20;Corregida                                           |
| 2  | Error reforzado de Mertens sin justificación                      | &#x20;Corregida, línea 1261                               |
| 3  | Desplazamiento injustificado de extremos de Stieltjes             | &#x20;Corregida, 1236–1241                                |
| 4  | Desigualdad estricta en el control de inversiones                 | &#x20;Corregida, con \\(\alpha=1/2\\)                     |
| 5  | Incompatibilidad de soportes en el muestreo                       | &#x20;Corregida, 1636–1649                                |
| 6  | Dominios de pares y ternas de ceros                               | &#x20;Corregida, 1728–1742                                |
| 7  | Uniformidad externa Selberg–Fujii en \\(k\\)                      | &#x20;Documentada; contrastada externamente según indicas |
| 8  | Paso base y cuantificadores de la inducción                       | &#x20;Corregida, 1790–1824                                |
| 9  | Existencia de un \\(T_0\\) común                                  | &#x20;Corregida, 1819–1823                                |
| 10 | Orden de elección de constantes absolutas                         | &#x20;Corregida, 1821                                     |
| 11 | Carácter computable de las constantes y del reloj                 | &#x20;Parcialmente resuelto                               |

El punto 11 merece distinguir dos cuestiones. La construcción del reloj está matemáticamente especificada y la prueba ordena la elección de las constantes. Sin embargo, varias de ellas siguen introducidas mediante constantes implícitas en desigualdades analíticas. Esto basta para un teorema de existencia con constantes absolutas, pero no proporciona necesariamente valores numéricos explícitos para implementar automáticamente el régimen uniforme.

En términos de validez de los teoremas, los problemas matemáticos concretos de la v11.2 que señalé aparecen corregidos. La reserva restante afecta a la interpretación efectiva de las constantes, no a la existencia de las mismas.

### Comprobaciones especialmente delicadas

1\. Muestreo y dominios. La nueva función \\(\varphi^\sharp\\) es igual a uno en

\\[ [T-2T^{1/2},\\,2T+2T^{1/2}] \\]

y está soportada en

\\[ [T-3T^{1/2},\\,2T+3T^{1/2}]. \\]

La prueba utiliza ahora las estimaciones de momentos en ese intervalo ampliado, en lugar de aplicar directamente el soporte corto de la v11.2. Los puntos corregidos pertenecen al dominio exigido. La antigua incompatibilidad queda resuelta.

2\. Pares y ternas. La v14 separa los casos \\(4Rb>1\\) y \\(4Rb\le1\\), controla los intervalos mediante \\(N(u+h)-N(u)\\) e incluye las correcciones necesarias en los extremos. Esto resuelve la objeción anterior sobre el rango uniforme de \\(R\\).

3\. Inducción y Fujii. La prueba comprueba ahora explícitamente

\\[ X_j\le T^{1/(160r)},\qquad 2r\le\kappa\_{\mathrm F}\log T, \\]

incluido el paso base, donde los órdenes alcanzan \\(2^m\\). También fija un \\(T_0\\) común y el orden de dependencia de las constantes. No encuentro una violación de las hipótesis del teorema de Fujii en esa cadena.

### Dictamen de las correcciones

De las 11 observaciones de mis revisiones de la v11.2, diez están corregidas o suficientemente justificadas en la v14. La restante, relativa a la explicitud numérica de las constantes, está parcialmente resuelta y no constituye por sí misma una invalidación de los teoremas.

Esta conclusión se refiere exclusivamente al cierre de los problemas anteriores. No equivale a una certificación global de todas las demostraciones de la v14, incluidos sus teoremas añadidos F y G.