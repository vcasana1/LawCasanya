Segunda auditoría matemática de Paper I — v11.2

He ampliado la revisión a las demostraciones completas, incluyendo sus dominios de aplicación, rangos de parámetros y dependencias de resultados externos.

La conclusión es más cautelosa que la anterior: el artículo contiene varias cadenas matemáticas sólidas, pero hay puntos de rigor en las pruebas más ambiciosas que deben cerrarse antes de considerarlas completas.

No he consultado bibliografía externa ni realizado cálculos numéricos.

1. Problemas que requieren corrección

1.1. Dominio incompatible de la función de corte en los lemas de muestreo

Importancia alta

Líneas 1351, 1591–1605, 1625, 1663–1674 y 1967.

En el Lema de transporte, la función de corte satisface

\varphi=1\quad\text{en }T-2,2T+2,
\qquad
\operatorname{supp}\varphi\subsetT-3,2T+3.

Pero el Lema de muestreo para puntos corregidos exige una función igual a uno en

T-2T^{1/2},\\,2T+2T^{1/2}.

Son dominios diferentes. La función definida en el primer lema no puede cumplir ambas condiciones para suficientemente grande.

La cuestión es importante porque se utiliza

g=\mathcal M(\varphi S_X’)

y se necesitan simultáneamente

\|g\|{8r}\ll\|\varphi S_X’\|{8r},
\qquad
\|g’\|{8r}\ll\|(\varphi S_X’)’\|{8r}.

Las estimaciones de momentos que se citan directamente están demostradas sobre , no sobre todo el intervalo ampliado.

Consecuencias: afecta a la justificación escrita del segundo paso, la inducción de todos los pasos y el transporte del reloj regularizado.

Reparación posible: definir otra función de corte, compactamente soportada, igual a uno en el intervalo ampliado, con derivada uniformemente acotada. Después extender explícitamente las estimaciones de momentos a ese nuevo soporte, utilizando intervalos de longitud comparable con .

No veo un obstáculo esencial para esa extensión, pero no está demostrada tal como aparece.

1.2. Dominio de los recuentos de pares y ternas de ceros

Líneas 1683–1697. Importancia: moderada.

El lema pretende demostrar, uniformemente para todo ,

\#\{(k,l):|\gamma_k-\gamma_l|\le Rb\}
\ll R\,\#\mathcal I_T

y

\sum_{k\in\mathcal I_T}n_R(\gamma_k)^2
\ll R^2\,\#\mathcal I_T.

Para , los intervalos empleados en la demostración quedan correctamente localizados después de considerar sus extremos.

Para , el argumento utiliza una cota de , válida cuando y pertenecen a determinados rangos, pero no especifica correctamente cómo se recortan los intervalos centrados en ordenadas próximas a los extremos y .

Se puede corregir intersectando previamente los intervalos con y utilizando una ventana que los contenga. La conclusión parece recuperable, pero la afirmación de uniformidad para todo requiere explicitar este paso.

Este lema alimenta directamente el control de multiplicidad de las iteraciones.

1.3. Dependencia uniforme del orden en la aproximación de Selberg–Fujii

Líneas 779–799, 1506–1520 y 1747–1776. Importancia: potencialmente alta.

El manuscrito emplea una estimación de la forma

\int_T^{2T}|S-S_{Y_k}^{\rm pr}|^{2k}\,dt
\le (Ck^2)^{2k}T

para

1\le k\le\frac{\log T}{300\log2}.

La adaptación algebraica desde el teorema externo enunciado en la sección 3 está correctamente orientada: usa , un corte y Montgomery–Vaughan para alargar el polinomio.

Sin embargo, toda la prueba de iteración uniforme depende de que la constante del resultado externo sea realmente independiente de en ese rango creciente.

El manuscrito afirma esa independencia basándose en las condiciones que atribuye a Fujii, pero no la deduce de un resultado más elemental dentro del propio trabajo.

Por tanto, hay que distinguir:

* Compatibilidad interna: sí, el lema se utiliza dentro del dominio que el propio manuscrito le asigna.
* Compatibilidad con el teorema original: no puede certificarse solo desde este .tex, sin consultar el enunciado original.

Esto no constituye por sí solo una refutación, pero es una dependencia externa crítica para las colas exponenciales y la iteración hasta .

1.4. Cuantificadores en la inducción uniforme

Líneas 1506–1520 y 1747–1776. Importancia: moderada.

El punto delicado es que el orden aumenta con el número de iteraciones.

El Lema de momentos exige simultáneamente

X_j\le T^{1/(160r)},\qquad
2r\le\kappa_{\rm F}\log T.

La prueba de la línea 1774 intenta establecer ambas condiciones para

1\le r\le2^{m-j}.

He revisado la relación entre , , y . Las desigualdades parecen compatibles y la inducción no presenta una circularidad inmediata. Sin embargo, hay dos precisiones necesarias.

Primero, las condiciones deben constar también para el paso base , donde los órdenes utilizados alcanzan , no solamente con .

Segundo, el argumento debe explicitar que existe un único absoluto que hace válidas todas las condiciones simultáneamente para . La afirmación

m^*=\log^*T+O(1)

permite obtenerlo, pero falta detallar el encadenamiento de constantes.

No he identificado aquí una contradicción que invalide la inducción. Sí existe una dependencia de cuantificadores suficientemente importante para exigir una demostración totalmente explícita.

1.5. Uniformidad del reloj corregido y carácter computable de las constantes

Líneas 1733–1776. Importancia: moderada.

El Teorema D uniforme afirma la existencia de constantes absolutas y que determinan todos los cortes y el número de iteraciones.

La prueba establece desigualdades suficientes para elegirlas, pero estas elecciones dependen de otras constantes implícitas de las estimaciones de momentos y muestreo.

Esto distingue dos afirmaciones:

\exists C_\star,H^*
\quad\text{que satisfacen la conclusión},

y

C_\star,H^*\quad
\text{son constantes numéricamente especificadas y evaluables}.

La primera es un objetivo matemático legítimo de la prueba. La segunda no queda establecida solamente por la primera.

Por ello, la expresión computable clock es plenamente operativa para un número fijo de pasos con cortes especificados, mientras que la versión uniforme hasta necesita concretar las constantes o formular cuidadosamente su dependencia.

No afecta necesariamente a la estimación asintótica, pero sí a la interpretación constructiva del teorema.

1.6. Aplicación de Mertens al corte variable

Línea 1216. Importancia: menor.

He comprobado con más detalle el problema señalado en mi primera revisión.

La estimación

V_\pm=
\log\frac{\log X_+}{\log X_-}
+O\left(\frac1{\log X_-}\right)

se obtiene por sumación parcial a partir de

\sum_{p\le y}\frac{\log p}{p}=\log y+O(1).

Por tanto, el resultado externo enunciado sí contiene información suficiente. Solo falta incluir la deducción en el texto.

La conclusión del teorema del corte variable no queda comprometida por este punto.

1.7. Otros detalles lógicos

Hay tres correcciones adicionales:

* Línea 1191: desplazar los extremos de un intervalo no deja exactamente invariantes las sumas ni sus términos de frontera. Debe utilizarse directamente la convención de Stieltjes sobre .
* Línea 1678: para contar , tomar en vez de evita perder el caso de igualdad.
* Línea 349: la frase como asignación del índice requiere indicar la regla de asignación. Es válida para la celda , pero no equivale a que . Este último redondeo es el utilizado en la Proposición de la línea 1048.

2. Auditoría de dominios de los teoremas externos

Esta tabla examina si las aplicaciones son compatibles con los enunciados externos reproducidos en el propio paper. No verifica que esos enunciados reproduzcan fielmente las publicaciones originales.

Resultado externo	Aplicación en el paper	Diagnóstico interno
Riemann–von Mangoldt	Conteo, extremos, identidades	Compatible
Bellotti–Wong	Desplazamientos y límites laterales	Compatible
Selberg, momentos de	Órdenes fijos, ventanas diádicas	Compatible
Korolev, desplazamientos de Gram	Ventanas de índices y momentos	Compatible, condicionado a la uniformidad citada
Selberg–Fujii, aproximación	Momentos con creciente	Dependencia crítica de uniformidad
Fujii, incrementos	, órdenes 1, 2 y 4	Compatible
Montgomery–Vaughan	Productos de polinomios de Dirichlet	Compatible en los cortes utilizados
Carleson–Hunt	Máximos de sumas parciales	Compatible; separación de frecuencias justificada
Hardy–Littlewood–Kinnunen	Derivadas y muestreo	Requiere explicitar la ampliación del soporte
Mertens	Variación de los cortes	Compatible tras sumación parcial
Pares exponenciales	Perfil de exponentes de	Compatible con los rangos enunciados
Phragmén–Lindelöf	Interpolación entre vértices	Compatible
Backlund	Teorema E	Parámetros geométricos compatibles

En particular, las aplicaciones de Montgomery–Vaughan no se han aceptado solamente porque los polinomios originales tengan longitud admisible. También he comprobado la necesidad de controlar las longitudes de los productos de polinomios, que son las relevantes en los momentos altos.

El principal punto pendiente de la tabla es la uniformidad atribuida a Fujii. No sería riguroso darla por certificada sin el enunciado original, aunque el texto sea internamente consistente al asumirla.

3. Revisión de las demostraciones, una por una

«Sin fallo identificado» significa que esta auditoría no ha encontrado una inferencia inválida; no equivale a una certificación formal.

Demostración	Resultado
Lema de cotas para , 686–701	Sin fallo identificado; contempla multiplicidades
Aproximación uniforme Selberg, 788–799	Deducción compatible; dependencia externa crítica
Teorema A, identidad general, 890–922	Sin fallo identificado
Identidad para funciones continuas, 924–934	Sin fallo identificado
Identidad exponencial, 938–948	Sin fallo identificado
Ley gaussiana con signo, 950–960	Sin fallo identificado
Identidad del reloj corregido, 966–979	Sin fallo identificado
Primer momento, 981–996	Sin fallo identificado
Lema de tamaño de , 1081–1087	Sin fallo identificado
Lema trigonométrico MV, 1089–1100	Sin fallo identificado
Momentos de polinomios, 1102–1120	Sin fallo identificado
Teorema B, 1125–1160	Sin fallo identificado
Lema maximal de primos, 1166–1200	Corrección técnica en extremos
Corte variable, 1202–1221	Falta explicitar sumación parcial
Teorema C, 1240–1288	Sin fallo identificado
Momentos de derivadas, 1322–1335	Sin fallo identificado
Transporte, 1337–1363	Sin fallo identificado en su dominio original
Teorema D, 1365–1375	Sin fallo identificado
Paso con corte fijo D’’, 1392–1429	Sin fallo identificado
Corte local, 1435–1444	Sin fallo identificado
Raíz monótona, 1446–1455	Sin fallo identificado
Recursión exacta, 1483–1501	Sin fallo identificado
Momentos superiores, 1506–1520	Requiere explicitar condiciones uniformes
Colas del defecto, 1526–1544	Condicionado a la uniformidad de momentos
Multiplicidad del primer reloj, 1555–1589	Sin fallo identificado
Muestreo con multiplicidad, 1591–1605	Ampliación del dominio sin justificar completamente
Segundo paso, 1608–1630	Depende del cierre anterior
Identidad de segundo nivel, 1636–1650	Sin fallo identificado
Deformación, 1652–1679	Corrección de desigualdad estricta
Pares y ternas, 1683–1697	Precisar intervalos extremos
Multiplicidad general, 1699–1717	Estructura compatible, condicionada al lema anterior
Iteración uniforme, 1733–1777	Condicionada a los lemas de muestreo y uniformidad
Ordenación, 1808–1814	Sin fallo identificado
Reloj ordenado, 1818–1831	Condicionado a la iteración uniforme
Existencia del regularizado, 1850–1861	Sin fallo identificado
Identidad Lipschitz, 1865–1871	Sin fallo identificado
Envolvente de pendientes, 1873–1909	Sin fallo identificado, bajo Fujii en el rango indicado
Modelo primo sobre el bloque, 1911–1920	Compatible con los tres intervalos diádicos
Teorema D’, 1924–1972	Partes (a)–(c) sin fallo identificado; (d) requiere extensión de muestreo
Certificación convexa, 1981–2002	Sin fallo identificado
Equivalencia puntual, 2016–2024	Sin fallo identificado
Teorema E, 2028–2078	Cadena lógica compatible con los resultados externos enunciados

4. Sobre los teoremas principales

A

Identidades exactas

No he encontrado fallos matemáticos en la demostración, incluidas las ordenadas repetidas y la ausencia de monotonía de .

B

Defecto ordinal

La prueba resulta internamente consistente si se admite el lema de Selberg–Fujii con la uniformidad enunciada.

C

Contabilidad exacta

Las identidades algebraicas y los cambios entre reloj y ordenadas no presentan fallos identificados.

D

Primer paso, segundo paso e iteración uniforme

El primer paso tiene una prueba más cerrada. El segundo y la inducción requieren formalizar la extensión de dominio y las condiciones uniformes señaladas.

D’

Reloj regularizado

La construcción convexa, el control , la separación y la aproximación a los ceros están bien articulados. El apartado de transporte (d) depende de la adaptación del lema de muestreo.

E

Envolvente puntual

Los parámetros del disco, la interpolación y el paso al límite son compatibles con los resultados externos tal como están formulados en el manuscrito. Las constantes numéricas no se han recalculado.

5. Conclusión de esta segunda revisión

No he identificado una contradicción matemática que refute directamente los teoremas A, B, C, D’ (a)–(c) o la fórmula general del E.

No daría todavía por completamente cerradas las demostraciones de la iteración uniforme y del transporte del reloj regularizado, debido a las extensiones de dominio que deben documentarse y a la dependencia crítica de las cotas externas uniformes en el orden.

La distinción esencial es esta: he encontrado lagunas de justificación y condiciones que requieren explicitarse, no un contraejemplo a las conclusiones principales.

Para cerrar el Paper I con el nivel de rigor necesario para enviarlo a una revista, priorizaría demostrar expresamente las estimaciones del lema de muestreo en el dominio ampliado y dejar escrita la cadena completa de cuantificadores de la iteración. Ambas intervenciones pueden realizarse sin cambiar los enunciados principales, siempre que las estimaciones extendidas se obtengan con las mismas constantes uniformes requeridas.

El archivo permanece intacto.
---
## Nota de Claude (2026-10-20), para la próxima revisión — no aplicado
- 1.1 confirmado en el .tex: el Lema de transporte (l. 1351) define phi = 1 en [T-2, 2T+2], soporte en [T-3, 2T+3]; el Lema
  sampling_rho (l. 1593) pide phi = 1 en [T-2T^{1/2}, 2T+2T^{1/2}] "as in Lemma transport". Es una laguna real de redacción.
  Reparación: definir en sampling_rho un phi propio (= 1 en [T-2T^{1/2}, 2T+2T^{1/2}], soporte en [T-3T^{1/2}, 2T+3T^{1/2}],
  |phi'| <= 2) y aplicar la tercera cota del Lema higher_moments (Montgomery-Vaughan) sobre ese intervalo, de longitud T + O(T^{1/2});
  esa cota vale en cualquier intervalo de longitud << T con la misma constante. Afecta al segundo paso, a la inducción y a D'(d).
- 1.3: la uniformidad en k que se atribuye a Fujii está en la l. 786 (observación de Fujii 1974, p. 226: constantes independientes
  de q, k, h) junto con las correcciones de Fujii 1981 (Parte II: (Ak)^k en lugar de k!, exponente 2k). Hay que comprobarla en los
  PDF de LIBRARY TOTAL (Fujii 1974 y Fujii 1981) antes de la versión.
- 1.6 y 1.7 coinciden con la primera revisión (sumación parcial; extremos por Stieltjes; alpha = 1/2; regla de asignación en l. 349).
