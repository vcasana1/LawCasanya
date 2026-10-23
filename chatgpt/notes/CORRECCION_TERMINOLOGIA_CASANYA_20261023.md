# Corrección vigente de terminología y rutas hacia RH — 23/10/2026

Esta nota sustituye, para cualquier trabajo posterior, las denominaciones inexactas de ChatGPT en sus notas y respuestas anteriores. El usuario ordenó corregirlas. Las entregas y manuscritos históricos siguen como registro, pero no deben reutilizarse sin esta rectificación.

## 1. Qué objeto tenemos realmente

Se define el **cociente meromorfo sintético de fase prima**
[
B_X^c(s)=rac{P_X(s)}{zeta_c(s)}.
]
Su restricción a (s=1/2+it) es una trayectoria parametrizada en el plano complejo. La fórmula de fase y las identidades de residuos registran la fase del reloj y los polos sintéticos. **No se ha probado que su traza sea una espiral geométrica** (radio monótono, patrón de vueltas o geometría equivalente); no llamarla espiral ni «espiral espectral», «espiral Casaña» o «espiral meromorfa» como hecho demostrado. Los archivos históricos con «spiral/espiral» en el nombre conservan su nombre de referencia, no constituyen evidencia geométrica.

Identidad previamente establecida, sin interpretación geométrica añadida:
[
B_X^c(1/2+it)=rac{|P_X(1/2+it)|}{Z_c(t)}
,e^{ipi(F_X(t)-1)}
]
cuando todos los factores están definidos. Los saltos de signo de (1/Z_c(t)) deben respetarse al hablar del argumento. En el polo (s_k=1/2+ic_k):
[
operatorname{Res}_{s=s_k}B_X^c(s)
=rac{|P_X(s_k)|}{|zeta_c'(s_k)|}e^{ipiarepsilon_k},
quad arepsilon_k=F_X(c_k)-k+	frac12.
]
Esto codifica residuos sintéticos; no es por sí solo una exclusión de ceros no críticos de zeta.

## 2. Qué cosas NO deben llamarse espiral

- Rectángulos, discos y contornos del principio del argumento son geometrías de certificación clásicas, no la supuesta espiral.
- Momentos de Hankel, cambios de signo y Rouché tampoco constituyen una propiedad de espiral.
- La identidad de transporte de raíces obtenida diferenciando una interpolación de funciones no es una propiedad especial de (B_X^c); no usarla para presentar una nueva ruta.
- **Descartar como ruta RH la interpolación (zeta_lambda=(1-lambda)zeta_c+lambdazeta), (0lelambdale1)**: sin control del extremo (lambda=1), el transporte anterior no cierra el problema. No volver a proponerlo como avance recuperado.
- La vía de defecto por contornos se debe etiquetar como *principio del argumento / recuento clásico*; no atribuirle novedad geométrica.

## 3. Programa activo sin cambio ficticio de nombre

A. Casaña–Rouché: construir centros aritméticos, certificar realidad local y buscar una propiedad global de cobertura. No atribuir a los certificados locales una cobertura que no han demostrado.

B. Casaña–Loewner–Pick: investigar si puede demostrarse una propiedad de Pick de un cociente construido con una referencia Casaña; es independiente de A y no debe descartarse solo por ser más fuerte que RH.

C. Comparación espectral por contornos: si se usa, identificarla honestamente como técnica clásica y no como una tercera vía «de espiral».

La función (B_X^c) puede mantenerse como **cociente meromorfo auxiliar** si se encuentra una desigualdad nueva que utilice realmente sus coeficientes aritméticos o residuos y los vincule rigurosamente con (zeta). No presuponer que esos datos suministran tal desigualdad.

## 4. Reglas del usuario

No reciclar reformulaciones clásicas como nuevas demostraciones; no inventar ventajas para un objeto solo para justificar su nombre. Avisar solo de obstáculos sustantivos, sin advertencias elementales repetidas. Sin crear versiones de manuscritos ni modificar ficheros congelados salvo orden expresa. Cualquier trabajo posterior debe leer esta rectificación junto a los archivos históricos.
