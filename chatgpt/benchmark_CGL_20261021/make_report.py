#!/usr/bin/env python3
"""Produce the initial benchmark delivery from measured output files."""
import csv,json
from pathlib import Path

HERE=Path(__file__).resolve().parent;OUT=HERE/'results_v2'
rows=list(csv.DictReader((OUT/'benchmark_resumen.csv').open()))
meta=json.loads((OUT/'constructor_metadata.json').read_text())
checks=json.loads((OUT/'same_equation_checks.json').read_text())
repro=json.loads((OUT/'c667_reproduction.json').read_text())
hp=json.loads((OUT/'high_precision_checks.json').read_text())
mem=json.loads((OUT/'constructor_complete.json').read_text())
def row(n,s='pilot1000',r='all'):return next(x for x in rows if x['method']==n and x['scope']==s and x['region']==r)
def fmt(x):return f'{float(x):.10f}'
text=r'''# Benchmark Casaña / Gonek / LeClair: entrega inicial ejecutada

Fecha: 21 de octubre de 2026. Motor: Python, float64; comprobaciones independientes con mpmath a 60 dígitos.

Se completaron el inventario, las definiciones y el piloto de 1.000 índices. También se evaluaron Lambert y c667 en los 2.001.052 registros y se reconstruyó c667 por completo. **No se ha ejecutado la comparación completa M1–M4 ni seleccionado un ganador global.** La enumeración global de raíces de los modelos sigue pendiente y la ecuación de LeClair ya muestra dos raíces para un mismo nivel en el piloto. Esta entrega se detiene en la puerta de control prevista en el benchmark, antes del ensayo masivo.

## 1. Archivos y fuentes

Datos originales: `/Users/vcasana/Documents/·.· MATLAB/·.· bin_unicos/`.

| Archivo | Formato verificado | Registros | Tamaño |
|---|---|---:|---:|
| zeross.bin | float64 little-endian | 2.001.052 | 16.008.416 bytes |
| zLamb.bin | float64 little-endian | 2.001.052 | 16.008.416 bytes |
| zCasanya.bin | float64 little-endian | 2.001.052 | 16.008.416 bytes |
| primoss.bin | uint64 little-endian | 455.052.511 | 3.640.420.088 bytes |

El fichero de primos acaba en 9.999.999.967: no está limitado a dos millones. Se verificó por criba el prefijo de 148.933 primos hasta 1.999.993; el registro siguiente es 2.000.003. Se comprobó en bloques la monotonía del fichero entero; no se verificó la primalidad de cada registro fuera del prefijo. Las dos referencias de ordenadas son finitas y estrictamente crecientes. `inventory.json` contiene las rutas, primeros y últimos valores y SHA-256 completos de datos y fuentes.

Acceso confirmado mediante el conector GitHub a [vcasana1/LawCasanya](https://github.com/vcasana1/LawCasanya), commit `24d9d84862bced814fea8b9a8cae8bf97ac4b5a7`. Se leyeron AGENTS.md y las últimas entradas del registro; se obtuvieron la especificación v17 y los programas originales Stage A/R1/R2. No se modificó el repositorio remoto. Los artículos locales fueron identificados por su primera página; las extracciones y los hashes están conservados.

## 2. Fórmulas y normalizaciones

Sea \(N_0(t)=t(\log(t/(2\pi))-1)/(2\pi)+7/8\), \(L(t)=\log(t/(2\pi))/(2\pi)\). Todos los resultados conservan el índice de entrada \(k\); no se ordenan ni se emparejan con el cero verdadero más cercano.

| Método | Definición implementada | Fuente |
|---|---|---|
| M0 Lambert | lectura de zLamb.bin, sin corrección | binario original |
| M1 LeClair 2016 | \(N_0(t)+1/(48\pi t)-\pi^{-1}\Im\sum_{p\le b}\log(1-p^{-1/2-\delta-it})=k-1/2\), \(\delta=10^{-6}\) | arXiv:1601.00914v1, PDF pp.18–19, (48), (49), Tabla I |
| M2 Gonek | \(1+\vartheta(t)/\pi+S_X(t)=k-1/2\), \(S_X=-\pi^{-1}\sum_{p^m\le X^2} w_X(p^m)\sin(mt\log p)/(m p^{m/2})\) | Trans. AMS 2012, PDF pp.5,13,15–16, (3.4), (5.2), (7.4) |
| M3 c667 | tres pasos con denominador \(L(t)\), fase de potencias primas con corte sharp y techos [8,8,512]; corte real diádico \(\min(X_{max},\max(8,\lfloor\sqrt{2^{\lfloor\log_2\tau_k\rfloor}}\rfloor))\) | selected.json y zCasanya_build.py originales |
| M4 v17 | Stage A: raíz por bisección con cota analítica de monotonía; R1/R2: seis niveles, diez pasos por nivel y comprobación de derivadas en cinco puntos de cada segmento | v17, sección 10; work/v15_prep/opc_task3_analytic_rule.py |

Para Gonek se usa exactamente \(w_X(n)=1\) si \(n\le X\), \(2-\log n/\log X\) si \(X<n\le X^2\), y cero fuera. La fase corresponde a \(\zeta_X=P_X+\chi\overline{P_X}\) en la recta crítica, con \(\chi=e^{-2i\vartheta}\). Se calcula \(\vartheta=\Im\log\Gamma(1/4+it/2)-(t/2)\log\pi\), con la rama continua de loggamma. No se evalúa zeta.

M1 es la variante finita **de LeClair 2016**, desarrollada a partir de la ecuación França–LeClair. No se atribuye a los artículos de 2014 un algoritmo distinto. Cada factor tiene parte real positiva: se suman sus argumentos individuales, sin envolver el argumento del producto entero. Se ejecutaron la continuación primo a primo descrita en el artículo y un solver directo de la misma ecuación, etiquetado como diagnóstico numérico separado.

Fuentes: [LeClair 2016, versión implementada](https://arxiv.org/abs/1601.00914v1), [Gonek 2012, publicación](https://doi.org/10.1090/S0002-9947-2011-05546-7). `references_verified.json` corrige los localizadores preliminares de Gonek del manifiesto congelado: los pesos son la definición sin número que sigue a (3.4), en la página 5 del PDF; (3.5) define E2 y no interviene en el código.

**Comparabilidad de presupuesto.** El sufijo P de los identificadores de fichero denota el corte numérico b; el presupuesto efectivo es la columna `prime_count`. Para b=7,31,127,511,2047,8191 se utilizan 4,11,31,97,309,1028 primos. En Gonek se fija \(X=\sqrt{b+1}\): su soporte llega a b+1, con peso cero en el extremo, y usa los mismos primos distintos que M1. M1 incluye infinitas potencias mediante el logaritmo de cada factor; Gonek y c667 tienen soporte finito en potencias. C667 utiliza como máximo 97 primos, hasta 509, y 117 potencias hasta 512. Igual número de primos no significa igual trabajo. Los CSV contabilizan términos con peso, operaciones trigonométricas y derivadas por separado.

## 3. Piloto, evaluación y referencias

Muestra determinista: 400 índices de entrenamiento, 300 de validación y 300 del tramo final. Cada región combina tres ventanas de 64 índices consecutivos y puntos distribuidos. El piloto sobrerrepresenta los primeros índices y su RMS no estima directamente el RMS de los dos millones. Las configuraciones se congelaron antes del evaluador. No hubo selección mediante gamma ni ajuste sobre el test. El tramo final ya se había inspeccionado en trabajos anteriores: no se denomina muestra nunca vista.

El constructor tiene una lista de entradas aritméticas y un audit hook que bloquea `zeross.bin` y `zCasanya.bin`; se comprobó que ambos accesos fallan. El evaluador es otro proceso. Los originales permanecen intactos.

| Referencia completa | RMS global | RMS tramo final | Saltos no positivos globales |
|---|---:|---:|---:|
'''
for name,label in [('M0_Lambert','Lambert'),('M3_c667','c667')]:
    a=row(name,'full','all');b=row(name,'full','test')
    text+=f"| {label} | {fmt(a['rms'])} | {fmt(b['rms'])} | {a['nonpositive_gaps']} |\n"
text+=f'''
La reconstrucción c667 es **idéntica byte a byte**: SHA-256 `{repro['frozen_sha256']}`. Tiempo de construcción completa: {meta['M3_c667']['seconds']:.3f} s.

| Método/configuración | Primos máximos | Cobertura piloto 1000 | RMS piloto 1000 | RMS test piloto 300 |
|---|---:|---:|---:|---:|
'''
for name,label,pr in [('M0_Lambert','Lambert',0),('M3_c667','c667',97),('M1_LeClair_P511','LeClair b=511',97),('M2_Gonek_level_P511','Gonek b=511',97),('M1_LeClair_P8191','LeClair b=8191',1028),('M2_Gonek_level_P8191','Gonek b=8191',1028),('M4_v17_R1','v17 R1',meta['M4_v17_R1']['prime_count']),('M4_v17_R2','v17 R2',meta['M4_v17_R2']['prime_count'])]:
    a=row(name);b=row(name,r='test')
    text+=f"| {label} | {pr} | {a['n_covered']}/1000 | {fmt(a['rms'])} | {fmt(b['rms'])} |\n"
text+='''
M1/M2 tienen cobertura de resolución completa, pero **la enumeración ordinal global del modelo no está validada**: estos son errores de predicciones con etiqueta k, no un ranking definitivo de las raíces k-ésimas de los modelos. M4 R1/R2 no son comparables como salidas de cobertura completa en el piloto: falta k=2; su RMS de la columna 1000 usa las 999 salidas disponibles. En el test piloto cubren 300/300. La extensión a índices bajos no estaba evaluada por el programa v17 original, restringido al tramo final. La continuación de v17 comprueba cinco puntos; eso no certifica la positividad en todo el segmento.

A 97 primos, las predicciones c667 tienen menor RMS en los 300 índices finales del piloto. Con 1.028 primos, el RMS de nivel de Gonek es menor en esa misma muestra. No se deduce superioridad universal ni se mezclan los dos presupuestos. Los resultados de todos los cortes, incluidos los desfavorables, están en `benchmark_resumen.csv` y `benchmark_presupuesto.csv`; incluyen MAE, mediana, P95, P99, máximo, RMS en separaciones locales, mejora/empeoramiento frente a Lambert, cobertura y saltos.

La muestra consecutiva del piloto no detectó los cruces de c667. El cálculo completo sí detectó 962, de ellos 274 en el tramo final: el piloto no sirve para certificar el orden global.

## 4. Coste y solvers de la misma ecuación

| Corte b | Primos | LeClair primo a primo, s/1000 | Misma ecuación directa, s/1000 | Gonek, s/1000 |
|---|---:|---:|---:|---:|
'''
for c in checks:
    b=c['cutoff'];text+=f"| {b} | {c['prime_count']} | {c['prime_continuation_seconds']:.6f} | {c['direct_seconds']:.6f} | {meta[f'M2_Gonek_level_P{b}']['seconds']:.6f} |\n"
mx=max(c['max_difference_on_common'] for c in checks)
text+=f'''
Los dos solvers de LeClair coinciden a menos de {mx:.3g} en altura sobre las salidas comunes; no son dos métodos matemáticos distintos. En el corte mayor la diferencia de tiempo es aproximadamente un factor {checks[-1]['prime_continuation_seconds']/checks[-1]['direct_seconds']:.1f}. No se declara una ventaja matemática a partir de esta diferencia de implementación.

Extrapolación lineal a 2.001.052 índices, **no medida**, para b=8191: LeClair primo a primo {checks[-1]['prime_continuation_seconds']*2001.052/3600:.2f} h; LeClair directo {checks[-1]['direct_seconds']*2001.052/3600:.2f} h; Gonek {meta['M2_Gonek_level_P8191']['seconds']*2001.052/3600:.2f} h. Estas cifras excluyen la enumeración global de raíces y no representan una comparación validada a igual tiempo. Para b=511, las mismas extrapolaciones son {checks[3]['prime_continuation_seconds']*2001.052:.0f}, {checks[3]['direct_seconds']*2001.052:.0f} y {meta['M2_Gonek_level_P511']['seconds']*2001.052:.0f} segundos, respectivamente. Los bloques limitan las matrices temporales; no hay motivo medido para cambiar a MATLAB.

Pico de memoria medido del proceso constructor, incluida la reconstrucción completa c667: {mem['maxrss_bytes']/1024**2:.1f} MiB. No se aisló el pico por método; se declara esta limitación en el CSV de coste. La extrapolación del tiempo de c667 no hace falta: su ejecución completa ya está medida. Las evaluaciones y la auditoría de raíces se registran separadamente.

## 5. Bloqueos concretos y control de precisión

1. **Ambigüedad de nivel en LeClair.** Para k=1, b=8191 y delta=1e-6 hay dos raíces en el intervalo aritmético ensayado: t=6.2833126333488335164 y t=14.1719591504838939883. Ambas se comprobaron a 60 dígitos. La continuación selecciona la segunda. Resolver una ecuación de nivel y enumerar todas sus raíces son operaciones distintas; no se puede dar por verificada la correspondencia ordinal global.
2. **Enumeración Gonek pendiente.** Se enumeraron las raíces críticas en [6.3,1421.5177645721906] con pasos 0.04 y 0.02 para cada corte: ambos pasos detectan 1.001 raíces, sin cruces descendentes. No es una enumeración hasta la altura máxima de los dos millones ni una certificación por intervalos. La inspección local del piloto no detectó etiquetas con múltiples raíces para Gonek. El número de errores ordinales globales se conserva como desconocido, no como cero.
3. **Dominio v17.** La extensión del Stage A del programa original deja sin cubrir k=2 al verificar el intervalo positivo y la cota de monotonía. No se rellena con otra receta. Las cinco comprobaciones de continuación no se sustituyen por una supuesta certificación de todo el intervalo.

Por estos motivos no se amplió a 10.000/100.000 índices ni se lanzó el ensayo completo M1–M4. No se ha congelado una configuración ganadora mediante entrenamiento/validación. Los umbrales de RMS se reportan como alcanzados o no **en el piloto**; c667 sí demuestra globalmente los umbrales 0.10, 0.075, 0.050 y 0.044, y no alcanza 0.040.

Los fallos iniciales de Newton no se ocultaron: dos fallos de LeClair en el primer primo (k=18,60) y los fallos de Gonek se recuperaron mediante una raíz única en un intervalo positivo, sin consultar gamma. Los conteos y los parámetros del solver están guardados. El fichero `benchmark_fallos.csv` conserva las incidencias, el k=2 de v17 y el estado desconocido de la indexación global.

Errores máximos frente a mpmath: fase {hp['maxima']['phase_abs_error']:.3g}, derivada {hp['maxima']['derivative_abs_error']:.3g}, theta {hp['maxima']['theta_abs_error']:.3g}. Son comprobaciones finitas de implementación, no cotas uniformes ni pruebas de RH.

**Causa del error MATLAB adjunto.** El registro muestra que fzero explora t negativos. En N0(t) eso produce log(t/(2pi)) complejo; su parte imaginaria es t/2, coincidente con los mensajes. El paso de Newton original tampoco mantiene el dominio t>2pi. El posterior atan2 recibe argumentos complejos. El código Python construye el reloj real con la rama principal de Lambert W (también para k=1) y usa salvaguardas de dominio e intervalos positivos; no aplica `real()` para tapar el problema.

## 6. Entrega y reproducción

Programas propios: `constructors.py`, `build.py`, `evaluate.py`, `verify_precision.py`, `solver_comparison.py`, `audit_ambiguity.py`, `make_report.py`. Las configuraciones congeladas contienen hashes. `results_v2/code_at_execution/` conserva el código de construcción ejecutado. Los binarios originales y los manuscritos no se alteraron.

Los datos grandes no se incluyen en el ZIP; se usan las rutas originales inventariadas. Desde el directorio de esta entrega, para repetir el piloto en otro subdirectorio nuevo:

```sh
OPENBLAS_NUM_THREADS=1 python3 build.py --output results_repeated
MPLCONFIGDIR=/private/tmp/cgl_mpl python3 evaluate.py --output results_repeated
python3 verify_precision.py --output results_repeated
```

`solver_comparison.py`, `audit_ambiguity.py` y `make_report.py` usan la ruta de la entrega `results_v2`; son diagnósticos reproducibles sobre esa salida. Los scripts necesitan NumPy, SciPy, mpmath y Matplotlib. Las versiones exactas están en `environment.json`. Los CSV obligatorios, los diagnósticos de raíces, las gráficas y los registros están incluidos. La comparación de fuentes sirve para implementar este ensayo; no valida las demostraciones de los manuscritos.

![RMS frente a primos y tiempo](results_v2/rms_primes_time.png)

![Altura, errores y cruces](results_v2/height_distribution_failures.png)

![Ambigüedad de la ecuación finita](results_v2/phase_ambiguity_k1.png)
'''
(HERE/'INFORME_INICIAL.md').write_text(text)
(HERE/'STATUS.json').write_text(json.dumps(dict(initial_delivery_complete=True,full_benchmark_complete=False,
    stages_completed=['inventory','formula_audit','python_pilot1000','full_frozen_baselines','high_precision_checks'],
    full_stage_gate_passed=False,blockers=['global_model_root_ordinal_enumeration_not_validated','LeClair_two_roots_k1_b8191','v17_low_index_k2_not_covered'],
    no_manuscripts_or_original_binaries_modified=True),indent=2))
print(HERE/'INFORME_INICIAL.md')
