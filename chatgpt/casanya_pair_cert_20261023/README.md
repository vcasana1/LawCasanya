# Casanya: certificados locales 23/10/2026

Este directorio almacena el programa de reproducción como material técnico, no como archivo destinado al usuario.

- `verify_pair.py`: implementación original procedente del ensayo local, sin usar `zeross.bin` para construir los centros.
- `tabla_certificados_locales.csv`: valores resumen transcritos de las salidas archivadas `pair_1283.out` y `pair_1290.out`. Se han conservado las salidas originales dentro del ZIP de la conversación; el resumen no equivale a una nueva ejecución.
- `README.txt`: condiciones, fórmulas, reservas sobre el motor intervalar y los intervalos.

**Estado:** las dos pruebas numéricas satisfacen desigualdades suficientes de Rouché según `mpmath.iv`, pero requieren una auditoría independiente con Arb/FLINT y revisión del control de errores antes de declararlas certificaciones definitivas de publicación.

**Alcance:** dos parejas localmente certificables, ninguna atribución ordinal global, ninguna prueba de RH. El teorema de parejas infinitas con discos adaptables NO es el teorema de aislamiento cuártico.

Continuación: [documento de traspaso](../handoff/CASANYA_RH_HANDOFF_20261023.md).
