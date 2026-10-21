# Checkpoint de trabajo

Solicitud activa: ejecutar los tests de la variante cuadrática basada en v14 y entregar resultados; guardar parciales reanudables por si se corta la sesión.

## Estado confirmado

* La nota teórica está publicada en `chatgpt/benchmark_CGL_20261021/analytic_v14_basis_v1/`, commit92c9bcb562d3984daa0807d1d73b863c20107d84.
* La especificación matemática y el protocolo de evaluación están en `PROTOCOL.json`; deben fijarse antes de leer los errores del nuevo predictor.
* NumPy, SciPy y mpmath están disponibles. OSQP y CVXPY no están instalados. Se implementará ADMM con solución tridiagonal exacta y certificado residual/dual; nada se ajustará con gamma.
* Todavía NO se ha construido ni evaluado el nuevo predictor cuadrático. No confundir los resultados de identidad de la nota con un benchmark.

## Diseño de implementación pendiente

1. Constructor con prohibición de abrir `zeross`; leer solo zLamb para etiquetas y bloques diádicos. Cada T fija X=sqrt(T/2), Lambda, malla y pendientes de v14.
2. Variables centradas y=P-N0 para evitar pérdida de precisión al resolver con valores nodales de millones. A=G/h tiene diagonal2/3 (1/3 extremos) y sub/superdiagonal1/6. Restricciones l=Lambda*h/2-diff(N0), u=2*Lambda*h-diff(N0).
3. Carga de primos interior normalizada: sum a_pm*sinc(m*h*log(p)/2)^2*sin(m*t_i*log(p)). Potencias completas con resto absoluto<=1e-12. Extremos por integrales de semisombrero, no por sinc².
4. Carga suave estable: en cada segmento [a,a+h], R(u)=a/(2pi)*(g(r*u)-u*g(r)), r=h/a, g(z)=(1+z)log(1+z)-z=sum_{m>=2}(-1)^m z^m/[m(m-1)]. Contribuciones izquierda/derecha: integrar (1-u)R(u), uR(u). Coeficientes exactos [1/((m+1)(m+2))-1/6] y [1/(m+2)-1/3]. Usar resto geométrico, no restar primitivas enormes.
5. ADMM: solve(A+rho D'D)y = d + rho D'(z-dual); z=clip(Dy+dual,l,u); dual+=Dy-z. Checkpoints atómicos cada50 iteraciones y por bloque; verificar restricciones, KKT y gap dual. Polishing de conjunto activo si hace falta, sin consultar errores verdaderos.
6. Modelo P=N0(nodes)+y; raíces por nivel k-1/2 e interpolación. No ordenar raíces entre bloques ni ocultar fallos en sus uniones. Guardar predicciones por bloque y array final antes de evaluar.
7. Evaluador separado importa `../localgap_v1/localgap_metrics.py`; compara mismos k, vecinos reales, primer1000, piloto fijo/últimos300 y600316 finales. Comparar c667/PAV/v17 y Gonek/LeClair existentes; registrar presupuesto variable y carácter retrospectivo.
8. Publicar programas, protocolo, logs, tablas y conclusiones en una nueva subcarpeta GitHub; añadir entrada a work/LOG e incidencia1. No modificar originales/manuscritos ni entregas anteriores. Usar conexión GitHub; no gh(token inválido). main compartido avanza: refrescar head/log, git pull y lease expected_sha; preservar cambios de Claude.

## Referencias locales

`../localgap_v1/fastphase.cpp` y `fastphase.dylib`: backend macOS Accelerate ya contrastado con NumPy; phase_vec admite suma de senos con frecuencias/coeficientes suministrados. `../localgap_v1/outputs/` contiene resultados comparadores. El directorio local LawCasanya no es checkout independiente; para git pull existe `/private/tmp/lawcasanya_publish_20261021`.

## Actualización: ejecución en marcha

Código implementado: construct.py, verify.py, evaluate_results.py. Protocolo dc895477e4be3351e691d7b358a67987e1647371e248d451235ad72e77162872. Cargas verificadas con error1.99e-14 y QP pequeño con SLSQP. Bloques hasta524288 terminados/convergidos; mayor1048576 en cargas. Consultar outputs/progress.json y run.log para estado real. Todavía no se ha abierto gamma en este experimento. Comentario incidencia6317583715 publica protocolo y estado.

## Resultado completado

Constructor terminó todos los bloques: outputs/predictions.npz, sin faltantes. Evaluación separada terminada: metrics.json/csv y evaluación por cero. Final600316 RMS0.054724035583361565,881 fallos direccionales,0 inversiones; global2763 fallos. Sin reajustes. Se está repitiendo solo el QP para auditar KKT y reproducir exactamente raíces, sin gamma (audit_solver.py). Publicación GitHub pendiente; no declarar subida hasta confirmar commit/ref.

Auditoría final terminada:18 bloques, mismas raíces exactas. Solo falta publicación/verificación remota. Para continuar no ejecutar de nuevo los tests: usar resultados guardados.
