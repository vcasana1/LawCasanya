#!/usr/bin/env python3
"""Build explicit-criterion tables and report only from executed outputs."""
import csv,json,os
from pathlib import Path
os.environ.setdefault('MPLCONFIGDIR','/private/tmp/cgl_matplotlib')
os.environ.setdefault('XDG_CACHE_HOME','/private/tmp/cgl_cache')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
HERE=Path(__file__).resolve().parent;OUT=HERE/'outputs'
def read(name):
    return list(csv.DictReader((OUT/name).open())) if (OUT/name).exists() else []
def normalized(r):
    return dict(method=r['method'],region=r['region'],prime_count=r['prime_count'],
      requested=r['requested'],covered=r['covered'],missing=r['missing_neighbors_or_outputs'],
      RMS=r['rms'],MAE=r['mae'],max_abs_error=r['max_abs'],max_abs_error_k=r['max_abs_k'],
      successes=r['directional_pass_count'],directional_proximity_failures=r['directional_ratio_violation_count'],
      structural_failures=r['structural_failure_count'],total_failures=r['directional_all_failure_count'],
      max_directional_ratio=r['directional_max_R'],worst_directional_k=r['directional_max_R_k'],
      symmetric_total_failures=r['all_failure_count'],symmetric_max_ratio=r['max_R'],symmetric_worst_k=r['max_R_k'],
      rejections_due_only_to_symmetric_min=r['symmetric_only_rejections'],nonpositive_gaps=r['nonpositive_gaps'],
      provenance=r['provenance'])
def save(name,rows):
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def table(rows):
    s='| Método | Primos | n | RMS | MAE | Máx. abs. (k) | Fallos direccionales | Estructurales | Peor cociente (k) | Fallos simétricos |\n'
    s+='|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|\n'
    for r in rows:
        s+=f"| {r['method']} | {r['prime_count']} | {r['covered']} | {float(r['rms']):.9g} | {float(r['mae']):.9g} | {float(r['max_abs']):.9g} ({r['max_abs_k']}) | {r['directional_ratio_violation_count']} | {r['structural_failure_count']} | {float(r['directional_max_R']):.9g} ({r['directional_max_R_k']}) | {r['all_failure_count']} |\n"
    return s
def main():
    pilot=read('pilot_localgap_summary.csv');full=read('full_localgap_summary.csv');other=read('other_versions_summary.csv')
    selected=['c667_original','c667_PAV_a010']+[f'{m}_X{x}' for x in [512,2048,8192] for m in ['Gonek','LeClair']]
    rows=[r for r in pilot if r['method'] in selected and r['region'] in ['first1000','pilot_last300','fixed_pilot1000','high_consecutive_last300']]
    rows += [r for r in full if r['method'] in selected and r['region']=='final600316']
    save('primary_directional_summary.csv',[normalized(r) for r in rows])
    matched=[r for r in full if r['region']=='final600316' and not r['method'].endswith('_regional_PAV_a010')]
    save('matched_final_directional.csv',[normalized(r) for r in matched])
    additional=[r for r in other if r['region']=='final600316_existing_variant']
    save('other_versions_directional.csv',[normalized(r) for r in other])
    status=json.loads((OUT/'final_evaluation_status.json').read_text())
    text=r'''# Benchmark Casaña–Gonek–LeClair: evaluación por índice y separación propia

Continuación de la entrega inicial, que se conserva. Fecha: 2026-10-21. Ningún manuscrito ni binario original se modifica. Los ceros verdaderos se leen únicamente en los evaluadores. Los nuevos constructores tienen una prohibición de abrir `zeross`.

## Corrección del criterio pedida por el autor

Para CADA método por separado, sea `x[k]` su cero sintético con el índice original k y `e[k]=x[k]−gamma[k]`. Nunca se reasigna k a un cero verdadero más próximo ni se ordenan las salidas para ocultar inversiones. Sean `a_izq=x[k]−x[k−1]` y `a_der=x[k+1]−x[k]`, usando siempre los vecinos originales k±1, aunque el piloto sea disperso.

El criterio PRINCIPAL es `−a_der/2 < e[k] < a_izq/2`. Equivale, para una sucesión sintética estrictamente creciente, a que gamma[k] esté dentro de la celda de x[k] delimitada por los puntos medios sintéticos. Si e>0 se usa a_izq; si e<0 se usa a_der. El cociente direccional es `2|e|/a_lado`, y debe ser <1. Una igualdad con el punto medio incumple la desigualdad estricta. En k=1 y k=N las celdas exteriores son ilimitadas por el lado sin vecino. Los extremos de ventanas interiores usan los vecinos externos reales, nunca se tratan como extremos globales.

El antiguo `2|e|<min(a_izq,a_der)` se conserva como **condición suficiente más exigente**, NO necesaria para esa pertenencia. Ejemplo: a_izq=10, a_der=1, e=4 cumple el criterio direccional (cociente .8), pero incumple el simétrico (cociente 8). La discrepancia se prueba en `localgap_metrics.py`.

El ejemplo real k=53 de c667_PAV_a010 tiene e=0.41229293562059866, a_izq=3.225234006948881 y a_der=0.20822912372284463: el cociente direccional es 0.2556669901981059, frente al simétrico 3.9599929947298373. Los primeros 1.000 índices tienen cero incumplimientos direccionales, frente a 65 simétricos. Este resultado finito no se extrapola al tramo final.

Esta definición comprueba qué cero SINTÉTICO es el más próximo a gamma[k]. No se cambia por el problema inverso de buscar qué cero VERDADERO es el más próximo a x[k]. Tampoco verifica por sí sola que una celda contenga exactamente un cero de zeta no incluido en la referencia. Los fallos de orden (algún vecino sintético con separación ≤0) se separan de los incumplimientos de proximidad. El total de fallos suma ambas clases disjuntas; los casos sin vecinos conocidos se declaran sin cobertura. No se usa separación media para ninguna decisión de proximidad.

## Métodos y presupuesto

* c667: los tres pasos originales con cortes efectivos (8,8,512), históricamente seleccionados con validación. Se conserva su binario local exacto.
* c667_PAV_a010: el código de proyección suministrado, aplicado globalmente a los 2.001.052 índices: PAV(x−.1*tau)+.1*tau. No añade primos y produce cero inversiones. La monotonía impuesta no prueba proximidad individual.
* Barrido Casaña constante: los mismos tres pasos, ahora (8,8,X), X=512,2048,8192, y sus proyecciones globales con alpha=.10. Es un experimento fijo distinto del c667 diádico en alturas bajas. No se optimizan parámetros con los ceros de prueba.
* Gonek: ecuación de fase del producto suavizado, theta exacta, peso 1 hasta X y 2−log(n)/log(X) hasta X². Para igualar presupuestos se toma X=sqrt(512),sqrt(2048),sqrt(8192), con 97,309,1028 primos activos, respectivamente. El corte nominal y el número de primos son magnitudes distintas.
* LeClair: la misma ecuación (49) de la entrega inicial, producto de Euler finito, delta=1e−6, término de Stirling 1/(48t), con exactamente esos 97,309,1028 primos. No se sustituye la fase por zeta verdadera.

Las referencias precisas y páginas verificadas están en `SOURCES_VERIFIED.md` y en los textos fuente de la entrega anterior. `sources/README.md` es una copia histórica del README auxiliar recibido, no la validación de esta continuación. La igualdad de número de primos NO implica igual coste: los tres pasos de Casaña y resolver una raíz convergida son operaciones distintas. `same_equation_solver_diagnostic.csv` compara además los tres pasos y la raíz convergida de la MISMA ecuación sharp para separar error de iteración y cambio de fórmula. En el piloto, aumentar el corte de los tres pasos puede empeorar la proximidad; no se atribuye todo al corte sin este control.

## Índices y control de raíces

Se conservan los 1.000 índices del piloto anterior y sus predicciones ya calculadas; se añaden los primeros 1.000 consecutivos, los últimos 300 consecutivos y los vecinos k±1 necesarios: 3.026 índices de contexto en total. Los «últimos 300 del piloto» son los últimos 300 índices de la selección original, no los últimos 300 consecutivos del archivo.

Antes de ampliar se barre la familia regular t≥6.3 desde el principio hasta k=2.001.052 en mallas .08 y .04. Sus resultados son evidencia numérica, NO una certificación por intervalos ni una enumeración de todos los artefactos del modelo cerca de t=0. Los artefactos de pequeña altura se conservan en los diagnósticos de prefijo. La familia e índice se fijan por niveles k−1/2 de la ecuación, con continuación desde el reloj; no se confunden con el ordinal de TODOS los ceros del modelo finito.

**Error de solver encontrado:** en LeClair con 97 primos, el nivel k=1.886.677 tiene tres raíces regulares, verificadas también a 55 dígitos: 1072977.38424057018577…, 1072977.58273231720711…, 1072977.67472109501003…. Newton desde Lambert converge a la segunda; la continuación primo a primo usada en la entrega original escoge la primera, sin consultar gamma. Se conserva esta última selección. Los índices vecinos y sus intervalos se comprueban antes de ampliar ese caso. Los tres ceros NO se convierten en tres nuevos índices ni se corre el resto de la secuencia dos posiciones. Véanse `multiroot_audit.json` y `*_selection_gate.json`. Por ello, el antiguo requisito de raíz única falla para esa configuración; el control posterior valida explícitamente la selección por índice, no una unicidad inexistente.

## Primeros 1.000 índices consecutivos

'''
    text+=table([r for r in rows if r['region']=='first1000'])
    text+='\n## Últimos 300 del piloto original\n\n'+table([r for r in rows if r['region']=='pilot_last300'])
    text+='\n## Tramo final completo: k=1.400.737…2.001.052\n\n'
    text+=f"Presupuestos completos en esta actualización: {status['complete_tiers']}. Estado de los tres presupuestos: **{'completo' if status['all_required_tiers_complete'] else 'en ejecución; no presentar como comparación terminada'}**.\n\n"
    text+=table(matched)
    text+='\n## Qué cambia al aumentar el presupuesto\n\n'
    for family in ['Gonek','LeClair','Casanya_constant']:
        values=[]
        for tier in [512,2048,8192]:
            name=f'{family}_X{tier}'+('_PAV_a010' if family=='Casanya_constant' else '')
            found=[r for r in matched if r['method']==name]
            if found:values.append(f"{found[0]['prime_count']} primos: {found[0]['directional_all_failure_count']} fallos, RMS {float(found[0]['rms']):.9g}")
        text+=f"* {family}: "+'; '.join(values)+'.\n'
    text+='\nEl barrido fijo de los tres pasos de Casaña + PAV empeora el recuento direccional del tramo final al aumentar X. El piloto de la raíz convergida sharp, con idéntica ecuación, separa este efecto de truncamiento/iteración del mero número de primos. No se ha reconstruido esa raíz sharp en todo el tramo final, por lo que no se extrapola su resultado piloto.\n\n'
    text+='\n## Otras versiones ya existentes, evaluadas sin reconstruirlas\n\n'+table(additional)
    text+=r'''
v17 R2 usa un presupuesto por índice diferente y una regla heurística de continuación; no se inserta en la clasificación de igual número de primos. Sus controles de segmentos muestrean puntos, no intervalos completos. Solo se reconstruyó el vecino k=1.400.736 ausente en el archivo final: el cálculo coincide exactamente en los tres puntos de solapamiento para Stage A, R1 y R2. Las variantes c=.85,1,1.15,1.30 preexistentes están en `other_versions_summary.csv`: sus bloques sin vecinos exteriores tienen cobertura incompleta expresamente declarada, y c=1.30 solo cubre un bloque. No se extrapola un bloque a 600.316 índices.

El archivo local zCasanya0 tiene cero inversiones. Con el criterio direccional tiene 3.039 fallos globales y 897 finales, frente a 3.092 y 938 de c667+PAV .10, aunque su RMS global es peor (.04560758 frente a .04382589). Por tanto, la afirmación preliminar de que «no mejora» debe limitarse al RMS global y al antiguo criterio simétrico; no describe el nuevo recuento direccional. El barrido aritmético encuentra compatibilidad con X=512, alpha=.20, diferencia máxima 6.984919309616089e−10, pero NO identidad de bytes ni un manifiesto histórico que pruebe su configuración exacta. Su script optimiza corte/alpha con ceros de validación: es una construcción aritmética con hiperparámetros seleccionados con referencia, que se informa por separado. No equivale al ajuste supervisado por cero `zCasanyaX_ideal.txt`, excluido del ranking aritmético. No se localizó aquí ese archivo ideal.

## Procedencia, errores y límites

* El c667 local tiene SHA256 `64d1de134e920c1eb89f61ba5d93c7f949b343bfa0d9ebf5da6fb647c2d790d9`; la proyección global fija tiene `01cc32b9775dd5d46f9d88c11291a79c568521e9bab1bea7022d3c8f8e6710e1`. No son los hashes `dc8d…`/`2857…` de los binarios citados en la incidencia. Las métricas de la proyección coinciden con las allí impresas a su precisión, pero eso no demuestra identidad de archivos. Cuatro reconstrucciones documentadas con dos relojes y dos aritméticas NO resuelven la procedencia de aquellos binarios. Se publica la discrepancia, no una equivalencia inventada.
* La antigua localización bibliográfica del peso de Gonek era imprecisa. `SOURCES_VERIFIED.md` identifica su definición tras (3.4), y el modelo (5.2), sin modificar el informe inicial congelado.
* La identidad `a_k−(e[k+1]−e[k])=gamma[k+1]−gamma[k]` se comprueba como identidad de evaluación. Usa los ceros verdaderos; no se vende como certificado predictivo independiente.
* Un piloto sin incumplimientos no implica ausencia global. Los recuentos del tramo completo se calculan por separado. No se ajustan parámetros sobre ese tramo después de ver los errores.
* `verify_final_tables.py` recalcula las pertenencias comparando gamma directamente con los puntos medios en altura, sin reutilizar la decisión del evaluador principal. Guarda también la distancia más pequeña del cociente a 1 para advertir posibles decisiones sensibles al redondeo. Esta comprobación independiente no es aritmética de intervalos.
* La proyección opcional de Gonek/LeClair es REGIONAL, con halo 1024 contrastado con halo 512, y se identifica así. No se presenta como una proyección global de dos millones de puntos. Esas filas auxiliares se excluyen de la tabla principal de métodos originales.
* Ninguna de estas comprobaciones finitas demuestra RH ni simplicidad global, ni una garantía individual para todos los k. El criterio de puntos medios es una definición operacional de proximidad; no es una demostración de identificación de todo cero de zeta.

## Archivos y reproducción

`outputs/primary_directional_summary.csv` y `matched_final_directional.csv` son las tablas principales con nombres explícitos; las tablas antiguas conservan columnas del criterio simétrico y añaden columnas `directional_*`. Las tablas por cero incluyen ambos cocientes. `outputs/pilot_index_sets.npz` fija los índices y sus contextos. `outputs/global_index/*enumeration.json` guarda el control de niveles; `multiroot_audit.json` documenta la selección excepcional; los archivos `*_final_constructor.json` guardan residuos y presupuestos. Los checkpoints de barrido son reconstruibles, no datos originales.

Orden: `construct_baselines.py`; `evaluate_baselines.py`; `pilot_models.py` (reutiliza caché inicial); `evaluate_pilot.py`; `enumerate_global.py Gonek` y `enumerate_global.py LeClair`; `audit_multiroots.py`; `refine_final.py METODO CORTE` únicamente cuando pasa su control de índices; `evaluate_final.py`; `recover_v17_neighbor.py`; `evaluate_other_versions.py`; `build_report.py`. Las rutas de los datos son las rutas originales del Mac, declaradas en cada script. El núcleo `constructors.py` está en la entrega inicial, un nivel por encima.

Opcional macOS: compilar `fastphase.cpp` con `clang++ -O3 -dynamiclib -framework Accelerate fastphase.cpp -o fastphase.dylib`, ejecutar `fastphase.py` y usar `enumerate_global.py METODO --fast`. Usa la MISMA fórmula, validada frente a NumPy; los checkpoints atómicos permiten reanudar sin repetir los barridos terminados. La compilación y los checkpoints no alteran ningún binario original.
'''
    (HERE/'README.md').write_text(text)
    fig,axes=plt.subplots(1,2,figsize=(11,4),layout='constrained')
    for family,label in [('Gonek','Gonek'),('LeClair','LeClair'),('Casanya_constant','Casanya: tres pasos + PAV .10')]:
        rr=[]
        for tier in [512,2048,8192]:
            name=f'{family}_X{tier}'+('_PAV_a010' if family=='Casanya_constant' else '')
            found=[r for r in matched if r['method']==name]
            if found:rr.append(found[0])
        axes[0].plot([int(r['prime_count']) for r in rr],[int(r['directional_all_failure_count']) for r in rr],'o-',label=label)
        axes[1].plot([int(r['prime_count']) for r in rr],[float(r['rms']) for r in rr],'o-',label=label)
    for a in axes:a.set_xscale('log');a.set_xlabel('Primos activos');a.grid(alpha=.25)
    axes[0].set_ylabel('Incumplimientos direccionales');axes[1].set_ylabel('RMS en altura');axes[0].legend(fontsize=8)
    fig.suptitle('Tramo final: 600.316 índices, sin reajuste con los ceros de prueba')
    fig.savefig(HERE/'prime_budget_final.png',dpi=170);plt.close(fig)
    print('Report built; complete tiers',status['complete_tiers'],flush=True)
if __name__=='__main__':main()
