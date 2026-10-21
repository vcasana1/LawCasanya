# Qué mejoraría primero en Casaña

Esta nota continúa el benchmark publicado, sin modificar constructores congelados ni los datos originales. No se eligen parámetros nuevos con los ceros verdaderos.

## Diagnóstico [DED]

Para la ecuación sharp propia `F_X(t;k)=N0(t)+S_X(t)−(k−1/2)`, c667 usa un denominador `L(t)=N0'(t)` y solo tres pasos, con cambio de corte entre pasos. Si se repitiera el último paso con corte fijo, su mapa sería `G(t)=t−F_X(t;k)/L(t)`. Derivando:

`G'(t)=1−F_X'(t;k)/L(t)+F_X(t;k)L'(t)/L(t)^2`.

En una raíz r, `G'(r)=−S_X'(r)/L(r)`. Por tanto, si `|S_X'(r)|>L(r)`, ese mapa no es localmente contractivo en la raíz. Es una limitación comprobable del denominador suave; no demuestra que todo resultado tras tres pasos sea malo, ni que la fase sharp no pueda aproximar zeta.

`diagnose.py` evalúa el factor en las raíces numéricas ya calculadas del piloto, sin abrir los ceros verdaderos. En los últimos 300 del piloto, el factor supera 1 en 15/300 casos a X512, 32/300 a X2048 y 58/300 a X8192. Las derivadas completas son positivas en esos puntos muestreados; eso NO certifica todo el intervalo ni toda una continuación.

## Primera mejora: resolver y continuar la misma ecuación [ADAPT]

Procedencia: el Newton con derivada completa ya implementado en `localgap_v1/pilot_models.py`, junto con la continuación existente de v17. No se presenta como un método nuevo.

Usar `N0'+S_X'`, con intervalos de búsqueda positivos y conservación explícita de la rama al aumentar el corte; detener por residuo y anchura del intervalo, no por un número fijo de tres pasos. No introducir PAV para ocultar una selección equivocada de raíz. Si una rama pierde la condición de continuación, registrar el fallo.

Comprobación existente, mismos últimos 300 del piloto, mismos cortes sharp, mismo índice k:

| X | Tres pasos + PAV: RMS | Raíz convergida: RMS | Incumplimientos direccionales: antes → después |
|---:|---:|---:|---:|
|512|0.0421002802|0.0462038482|1 → 0|
|2048|0.0463437635|0.0362277407|1 → 0|
|8192|0.0577734614|0.0315778559|1 → 0|

Fuente: `../localgap_v1/outputs/pilot_localgap_summary.csv`. Esto no afirma mejora universal del RMS: a X512 empeora. La raíz sharp convergida aún no se ha evaluado en los 600.316 índices finales. Ese es el siguiente experimento discriminante, preservando el criterio principal y el índice original; no repetir el barrido ya hecho de tres pasos.

La versión v17 R2 existente ya mejora a c667+PAV en el tramo final (RMS .0331440 frente a .0403889; 58 incumplimientos direccionales frente a938), aunque usa otro presupuesto por índice y no es una comparación de igual coste. Debe ser la referencia interna actual, en vez de tratar c667 como la mejor versión disponible.

## Segunda dirección: presupuesto adaptativo por estabilidad aritmética [DED, propuesta no validada]

Una vez resuelta la ecuación con precisión, comparar la MISMA rama en X,2X,4X. Evaluar desplazamientos entre esas raíces respecto a las separaciones sintéticas propias y vigilar la positividad del Jacobiano en la continuación. Esto podría concentrar el cálculo en los índices donde los nuevos primos todavía producen cambios grandes, en lugar de imponer el mismo corte a todos.

Es una propuesta experimental, no un criterio ya validado de proximidad a zeta. Dos cortes pueden concordar y estar ambos sesgados. Si en un intervalo que contiene la raíz se certifica `F_X' >= m > 0`, entonces `|t−r_X| <= |F_X(t)|/m` por el teorema del valor medio: esa cota controla el error de resolver el MODELO, no el error `r_X−gamma_k`. No se afirma haber encontrado una cota aritmética independiente para este último. No se ha investigado la novedad bibliográfica de la regla adaptativa propuesta.

Prioridad: separar error del solver, error de rama y error de truncamiento antes de diseñar otra fórmula o ajustar parámetros. Dos direcciones: una adaptación de programas existentes y una deducción/propuesta experimental; ninguna se reclama como novedad establecida ni como prueba de RH.
