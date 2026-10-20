# Revisión matemática de Paper I — v11.2

Archivo: `prime_corrected_clock_v11_2.tex` Extensión: 2.238 líneas.

La revisión se limita a la lógica matemática: identidades, cuantificadores, hipótesis, inferencias y suficiencia de las demostraciones. No he repetido cálculos numéricos ni contrastado las referencias bibliográficas.

## 1. Errores y problemas detectados

### 1.1. Error en la interpretación del defecto ordinal — línea 349

Importancia: moderada. Error matemático concreto.

El manuscrito afirma:

> \\(|u_k(X)|<1/2\\) means that the corrected count assigns to \\(\gamma_k\\) its correct index.

Sin embargo, se ha definido

\\[ u_k(X)=k-\frac12-F_X(\gamma_k). \\]

Si el índice se obtiene redondeando el valor de \\(F_X\\) mediante

\\[ \widehat N_X(t)=\left\lfloor F_X(t)+\frac12\right\rfloor, \\]

como ocurre en la Proposición sobre redondeo (líneas 1048–1059), entonces

\\[ \widehat N_X(\gamma_k)=\lfloor k-u_k(X)\rfloor. \\]

Por tanto, para un cero simple,

\\[ \boxed{\widehat N_X(\gamma_k)=k \iff -1\<u_k(X)\le0.} \\]

La condición \\(|u_k(X)|<1/2\\) no garantiza la asignación correcta.

Corrección necesaria: describir \\(u_k\\) como el residuo de la ecuación corregida, sin atribuirle automáticamente una asignación correcta por redondeo. Los resultados sobre su media cuadrática no dependen de esa interpretación.

Para ceros múltiples, además, debe distinguirse el índice \\(k\\) de \\(N(\gamma_k)\\), que cuenta toda la multiplicidad.

### 1.2. Hipótesis insuficiente para justificar una estimación — líneas 1216–1220

Importancia: moderada. Laguna demostrativa reparable.

En la demostración del teorema del corte variable se escribe

\\[ V\_\pm= \log\frac{\log X\_+}{\log X\_-} +O\left(\frac1{\log X\_-}\right). \\]

Pero el resultado de Mertens enunciado en las líneas 829–831 solamente proporciona

\\[ \sum\_{p\le y}\frac1p=\log\log y+O(1). \\]

Restando dos expresiones con errores \\(O(1)\\) no se obtiene automáticamente un error \\(O(1/\log X\_-)\\).

La estimación utilizada es válida con información más fuerte sobre la distribución de los primos, pero no se deduce del teorema tal como está enunciado.

Esto importa especialmente para la conclusión

\\[ \left\langle (\widetilde u_k-u_k(X\_-))^2 \right\rangle\_{\mathcal I_T}\longrightarrow0 \\]

con \\(c\\) fijo.

Se puede cerrar utilizando una versión suficientemente precisa de Mertens o una estimación de primos en intervalos multiplicativos acotados. No exige cambiar la estrategia de la demostración.

### 1.3. Tratamiento de los extremos del intervalo — línea 1191

Importancia: menor.

La demostración propone desplazar \\(T\\) y \\(2T\\) cuando coinciden con ordenadas, afirmando que eso no cambia ninguno de los dos miembros de la identidad.

Literalmente es incorrecto: desplazar un extremo puede cambiar el conjunto de índices y los términos de frontera.

No obstante, la integración de Lebesgue–Stieltjes que utiliza el artículo permite tratar directamente los extremos con la convención de continuidad por la derecha ya establecida.

Solución: eliminar el desplazamiento y formular directamente la integración sobre \\((T,2T]\\), con sus términos de frontera.

### 1.4. Desigualdad estricta en el control de inversiones — líneas 1655–1679

Importancia: menor.

La Proposición sobre deformación concluye que

\\[ \\#\\{k:d\_{2,k}\le0\\}\ll\frac{\\#\mathcal I_T}{H_1^2}. \\]

La demostración dice obtenerlo tomando \\(\alpha=1\\) en una estimación para

\\[ \left|\frac{d\_{2,k}}{d\_{0,k}}-1\right|>\alpha. \\]

Pero si \\(d\_{2,k}=0\\), la expresión vale exactamente \\(1\\), por lo que no satisface la desigualdad estricta.

Solución: tomar \\(\alpha=1/2\\). Se obtiene la misma cota, incluyendo las coincidencias. La conclusión del teorema permanece válida.

### Matización sobre el punto 1.2

La estimación reforzada de Mertens sí puede deducirse del primer resultado de la línea 830, que da

\\[ \sum\_{p\le y}\frac{\log p}{p}=\log y+O(1), \\]

mediante sumación parcial. Por tanto, no hace falta añadir una hipótesis externa. Lo que falta en la línea 1216 es explicitar esa deducción; no constituye un obstáculo matemático de fondo.

## 2. Resultados cuya cadena lógica no presenta un fallo identificado

| Bloque                     | Resultado de la revisión lógica                                                                                                                                     |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A. Identidades exactas     | Correcta la descomposición por intervalos, incluyendo ceros múltiples y modelos no monótonos.                                                                       |
| B. Defecto y cortes primos | La transferencia de momentos continuos a momentos ordinales y el control del término derivado están justificados.                                                   |
| C. Contabilidad finita     | Las identidades algebraicas, el término \\(\chi_k\\) y la separación diagonal/cruzada son coherentes.                                                               |
| D. Primer y segundo paso   | No he identificado un fallo en el uso de Hölder, la función maximal o las escalas de transporte.                                                                    |
| D. Iteración uniforme      | La inducción incorpora explícitamente la multiplicidad, los momentos altos y sus restricciones de corte. No he encontrado una circularidad lógica.                  |
| D'. Regularización convexa | La existencia y unicidad del minimizador, la envolvente de pendientes y el paso del error \\(L^4\\) a las ordenadas tienen una justificación consistente.           |
| D''. Corte fijo            | La comparación con el corte auxiliar y la cota \\(O(1+\log\log\log T)\\) mantienen la dirección correcta de las desigualdades.                                      |
| E. Envolvente puntual      | La equivalencia entre el limsup del desplazamiento y el de \\(S(t)\\), así como el argumento de paso al límite, no presentan una contradicción lógica identificada. |

Estos juicios son sobre las deducciones internas, condicionados a que los resultados externos utilizados sean válidos exactamente en las formas enunciadas. No constituyen una verificación independiente de esos resultados.

## 3. Dictamen

Errores matemáticos concretos identificados

1 principal + 2 técnicos

Lagunas de exposición reparables

1

Demostraciones principales refutadas por esta revisión

Ninguna

La corrección más importante es la de la línea 349, porque confunde residuo ordinal con asignación de un índice mediante redondeo.

En cuanto a los dos resultados más fuertes del manuscrito, el reloj iterado con error cuadrático \\(O(\log^{-2}T)\\) y el reloj regularizado con corte fijo y error de cuarto momento \\(O(\log^{-4}T)\\), no he localizado una inferencia inválida que los desmonte.

Eso no equivale a certificar sus demostraciones: una auditoría lógica de este tipo tampoco demuestra que los lemas externos admitan exactamente la uniformidad en el orden y en los intervalos que necesitan las pruebas.

Conclusión: en el ámbito solicitado, el Paper I presenta una estructura matemática internamente consistente, con correcciones localizadas. No encuentro motivo lógico demostrado para retirar los teoremas principales, pero tampoco sería correcto declararlos formalmente verificados sin comprobar por separado sus hipótesis externas.

No he modificado el archivo ni generado otra versión.
---
## Nota de Claude (2026-10-20), para aplicar en la próxima revisión — no aplicado
- 1.1: el cálculo del revisor es correcto para el redondeo de ⌊F_X+1/2⌋ (índice correcto ⇔ −1<u≤0). |u_k|<1/2 equivale a
  k−1<F_X(γ_k)<k, es decir, a la regla k̂ = ⌊F_X(γ_k)⌋+1 (nivel semientero k−1/2 más cercano, convención del punto medio).
  Corrección: enunciar en la línea 349 qué regla de asignación se usa; con esa regla la frase es correcta. Para ceros múltiples,
  distinguir k de N(γ_k), como pide el revisor.
- 1.2: de acuerdo; explicitar la sumación parcial desde Σ_{p≤y} log p/p = log y + O(1) (línea 830).
- 1.3: de acuerdo; formular la integración sobre (T,2T] con los términos de frontera, sin desplazar extremos.
- 1.4: de acuerdo; α = 1/2.
- El lema de multiplicidades del material pendiente (defect_certificate_pending.tex) no depende de la interpretación de 1.1.
