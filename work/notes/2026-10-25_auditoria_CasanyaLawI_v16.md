# Auditoría de CasanyaLawI_v16 (adjunto del autor; no está en GitHub en el momento de esta nota)

Nota de Claude, 25-oct-2026. Comparación línea a línea con v15. Referencias cruzadas comprobadas: todas resuelven, sin etiquetas duplicadas. Sin compilar (falta `lmodern.sty` aquí). Sin ejecuciones numéricas.

## 0. Qué cambia respecto a v15

Tres cambios y nada más: 3 líneas modificadas, 194 añadidas.
1. Abstract: una frase nueva sobre la descomposición exacta y la identidad integral.
2. Nueva subsección `subsec:variance-split` (líneas 3870–4038), dentro de la sección de certificados de multiplicidad.
3. Conclusiones: un párrafo nuevo y una frase retocada.

Todo lo demás es v15. Los defectos de redacción señalados en la auditoría de v15 **siguen sin corregir**: el título "unproved scalar asymptotics" (l. 2940) y el "must be treated as unverified" (l. 2997) contradicen el Thm `thm:C1`; no hay referencia cruzada de `thm:goodcount` a `thm:blockcount`; faltan DOI (solo 8 en la bibliografía).

## 1. La subsección nueva: correcta, verificada paso a paso

**Thm `exact-variance-split`.** Es la descomposición de mi nota `2026-10-25_ET_a_cero_estado.md` §5. Verificación: bloque de tamaño $m$ desde el índice $j$; $N(\gamma^-)=j-1$, $N(\gamma)=j+m-1$, $N^*=j-1+m/2$; entonces

$$(N^*-F)+\ell-\tfrac{m-1}2=j+\ell-\tfrac12-F=u_{j+\ell}.$$

Los desplazamientos centrados suman 0 y sus cuadrados $m(m^2-1)/12$. Correcto. Bien señalado que no hay término de borde porque la ventana se define por ordenadas.

**Cor. `intrinsic-floor`.** Correcto: $B_T\le4\mathsf V_T\le4\sum u^2$; $E_T\to0\iff\mathsf A_T/M_T\to0$ y $\mathsf V_T/M_T\to0$; el ínfimo sobre $F$ arbitrarias es $\mathsf V_T$, alcanzado con $F(\gamma)=N^*(\gamma)$, que usa ceros y no es un reloj admisible. Bien dicho que el 100 % asintótico no es RH puntual.

**Thm `exact-counting-integral`.** Es la identidad de v14 (`identity_general`, $j=1$) extendida a extremos $a,b$ arbitrarios con $N$ continua por la derecha. Verificación del salto: con $g=N(\gamma^-)-F(\gamma)$,

$$\frac{(g+m)^3-g^3}{3}=\sum_{\ell=1}^m\Bigl[\bigl(g+\ell-\tfrac12\bigr)^2+\tfrac1{12}\Bigr],$$

porque $(x+\frac12)^3-(x-\frac12)^3=3x^2+\frac14$. Y $g+\ell-\frac12=u_{j+\ell-1}$. Entre saltos, $(G^3/3)'=-G^2F'$. Telescopando sale la fórmula con el término $(G(b)^3-G(a)^3)/3$ exacto. Correcto. Bien la advertencia de que $F'dt$ es signado si $F$ no es monótona.

**Cor. `sawtooth-equivalence`.** Correcto. La condición de borde $|G(T)|+|G(2T)|=o(M_T^{1/3})$ basta.

*Observación útil que falta:* con $F=F_X$ y la cota trivial $|S_X|\ll\sqrt X/\log X$, esa condición se cumple solo si $X=o(T^{2/3})$. No es una restricción real: los extremos $a\in[T,T+1]$, $b\in[2T,2T+1]$ se pueden elegir donde $|G|$ sea pequeño, porque $\frac1T\int G^2\ll\log\log T$ garantiza puntos con $|G|\ll\sqrt{\log\log T}$. Conviene decirlo para que la equivalencia valga con cualquier corte, incluidos $c\ge1$, que son los que importan.

**Rem. `variance-significance`.** Correcta.

## 2. Comparación con mi nota

Coincide con `2026-10-25_ET_a_cero_estado.md` §5 en los dos enunciados (descomposición; equivalencia con la integral). v16 mejora dos cosas: formula la identidad integral con extremos arbitrarios y $N$ continua por la derecha, y hace explícita la condición de borde $o(M_T^{1/3})$. Mi nota añade lo que v16 no dice: que la constante de segundo orden de $\frac1T\int S^2$ es lo que decide $\mathsf V_T/M_T$, y la elección de extremos para cortes grandes.

## 3. Conclusión

- v16 = v15 + una subsección correcta. Ningún error matemático.
- Quedan por corregir los tres puntos de redacción de la auditoría de v15 (coherencia con C1; referencia `goodcount`→`blockcount`; DOI y configuración de hiperenlaces/backrefs del autor).
- Sugerencia para v17: añadir la observación sobre la elección de extremos (§1 arriba) para que la equivalencia del diente de sierra valga para todo corte.
