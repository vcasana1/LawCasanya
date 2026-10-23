# Corrección vigente de terminología y rutas hacia RH — 23/10/2026

Esta nota rectifica las denominaciones inexactas utilizadas por ChatGPT. Las entregas anteriores siguen como registro histórico y no deben reutilizarse sin esta corrección.

## Objeto matemático

El objeto definido por

\[
B_X^c(s)=\frac{P_X(s)}{\zeta_c(s)}
\]

es un **cociente meromorfo sintético de fase prima**. Su restricción a \(s=1/2+it\) es una curva parametrizada compleja. No se ha demostrado que describa una espiral geométrica (monotonía radial, estructura de vueltas u otra geometría que justifique ese nombre). No llamarlo «espiral Casaña», «espiral espectral» o «espiral meromorfa» en afirmaciones científicas. Los nombres históricos de ficheros contienen «spiral/espiral», pero no prueban ninguna propiedad.

La identidad

\[
B_X^c(1/2+it)
=\frac{|P_X(1/2+it)|}{Z_c(t)}
e^{i\pi(F_X(t)-1)}
\]

vale donde los cocientes estén definidos y codifica una **fase**; el cambio de signo del factor real \(1/Z_c(t)\) afecta al argumento. También está demostrada la identidad de residuos sintéticos

\[
\operatorname{Res}_{s=1/2+ic_k}B_X^c(s)
=\frac{|P_X(1/2+ic_k)|}{|\zeta_c'(1/2+ic_k)|}
e^{i\pi\varepsilon_k},
\qquad
\varepsilon_k=F_X(c_k)-k+\frac12.
\]

Ninguna de ellas demuestra por sí misma la geometría de espiral ni excluye ceros no críticos de \(\zeta\).

## Denominaciones que se retiran

- Un rectángulo, disco o contorno usado en el principio del argumento **no es** una «espiral» ni una innovación geométrica Casaña.
- El criterio de momentos de Hankel, los cambios de signo y Rouché son técnicas de certificación distintas; no describirlas como «la espiral».
- La identidad obtenida por derivación implícita para una interpolación de funciones no es un resultado especial del cociente \(B_X^c\).
- **No reactivar la vía \(\zeta_\lambda=(1-\lambda)\zeta_c+\lambda\zeta\), \(0\le\lambda\le1\), como mecanismo de demostración de RH**: las estimaciones de transporte propuestas no controlan el extremo \(\lambda=1\); volver al extremo sin tal control no supone avance.
- Una comparación por contornos se etiquetará como tal: **principio del argumento / recuento clásico**, nunca como «espiral».

## Rutas que permanecen separadas

**Casaña–Rouché:** centros aritméticos, certificación local y problema de cobertura.

**Casaña–Loewner–Pick:** investigación de positividad aritmética de un cociente con referencia Casaña, sin descartarlo por ser más fuerte que RH.

**Comparación por contornos:** técnica clásica auxiliar, si aporta una desigualdad demostrada, sin denominación geométrica nueva.

El cociente meromorfo \(B_X^c\) puede estudiarse como objeto auxiliar de fase y residuos. Para presentarlo como ruta hacia RH debe existir una **desigualdad nueva y demostrada que conecte sus datos con los ceros verdaderos de \(\zeta\)**.

## Reglas expresas del autor

No disfrazar resultados clásicos con nombres nuevos; no inventar una geometría para justificar trabajo previo; no reintroducir vías previamente descartadas sin una reparación demostrada de su defecto; evitar advertencias elementales repetidas y señalar solo obstáculos matemáticos sustantivos. No crear nuevas versiones ni editar manuscritos congelados sin orden expresa. Las notas históricas se consultarán junto a esta corrección.
