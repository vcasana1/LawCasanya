# Umbrales de proporción con cota exacta: la proporción se controla con $\langle u_k^2\rangle$, sin $d_T$

Nota de Claude, 25-oct-2026. Sin ejecuciones numéricas: los números de §4 son cuadraturas y los de §5 son lecturas de la Tabla `tab:direct` de v14. Ningún manuscrito cambiado. Notación de v14:
- $u_k(F)=k-\tfrac12-F(\gamma_k)$ para cualquier función real continua $F$ construida sin ceros;
- $u_k(X)=u_k(F_X)$ con $F_X=N_0+S_X$;
- $\mathcal I_T=\{k:T<\gamma_k\le2T\}$, con ordenadas contadas con multiplicidad y $M_T=\#\mathcal I_T$.

## 1. Teorema (T, exacto, incondicional)

Sea $B_T$ el número de ceros con $T<\gamma\le2T$ que están fuera de la recta o no son simples. Para **toda** $F$ continua (sin monotonía, sin lista, sin huecos):

$$B_T\ \le\ 4\sum_{k\in\mathcal I_T}u_k(F)^2,\qquad B_T\ \le\ 2\,\#\{k\in\mathcal I_T:\ |u_k(F)|\ge\tfrac12\}.$$

Por tanto la fracción de ceros en la recta y simples es

$$\ \ge\ 1-4\,\langle u_k(F)^2\rangle_{\mathcal I_T},\qquad\text{y también}\qquad \ge\ 1-2\Pr_{k\in\mathcal I_T}\bigl(|u_k(F)|\ge\tfrac12\bigr).$$

No hay término de borde.

*Prueba.*

1. **Bloques.** Un cero cuenta en $B_T$ si y solo si su ordenada se repite en la lista. En efecto, un cero fuera de la recta tiene pareja $1-\bar\rho$ con la misma ordenada, y uno múltiple se repite. Así, $B_T$ es la suma de los tamaños $r\ge2$ de los bloques $\gamma_j=\dots=\gamma_{j+r-1}=\gamma$. Cada bloque está entero dentro de $\mathcal I_T$, porque la ventana se define por $\gamma$.
2. **Valores de $u$ en un bloque.** Dentro del bloque, $u_{j+i}=u_j+i$ para $i=0,\dots,r-1$, porque $F(\gamma)$ es el mismo para todos sus índices.
3. **Primera cota.** Para todo $u$ real,
$$\sum_{i=0}^{r-1}(u+i)^2\ \ge\ \frac{r(r^2-1)}{12}\ \ge\ \frac r4\qquad(r\ge2).$$
Hay igualdad en $r=2$, $u=-\tfrac12$. Sumando sobre los bloques y añadiendo los términos $u_k^2\ge0$ de los demás índices se obtiene la primera cota.
4. **Segunda cota.** Una progresión de paso 1 tiene a lo sumo un punto en $(-\tfrac12,\tfrac12)$. Por tanto al menos $r-1\ge r/2$ índices del bloque cumplen $|u|\ge\tfrac12$. $\square$

**Relación con v12.** El Teorema `thm:goodcount` de v12 da $1-4d_T$, con $d_T$ la fracción de índices malos de una *lista* $\kappa_k$. Esta forma sustituye la lista por una *función*. En $u$ el "hueco" es exactamente 1 para todos los índices, así que desaparecen el control de huecos y el transporte que exigía la ruta por $d_T$.

**Procedencia.** El argumento de bloques es el de v12 (pareja fuera de la recta y bloques de ordenadas iguales), al que se añade la observación de que $u$ avanza exactamente en 1 dentro de cada bloque. No lo he encontrado en la biblioteca; no he hecho una búsqueda exhaustiva.

## 2. Umbrales exactos

$$\text{proporción}>0\iff\ \text{basta}\ \langle u^2\rangle<\tfrac14,\qquad \text{proporción}>0.4173\iff\ \text{basta}\ \langle u^2\rangle<0.14568 .$$

En forma de probabilidad: basta $\Pr(|u|\ge\tfrac12)<\tfrac12$ (proporción positiva) o $<0.29135$ (más de 41.73 %).

Por la identidad exacta de v14 (Thm A, $g(x)=x^2$),
$$\sum_k\bigl(u_k^2+\tfrac1{12}\bigr)=\int(N-F)^2\,dF+\text{borde}.$$
En la media continua de $E=N-F$ con peso $dF$, los umbrales equivalentes son $\langle E^2\rangle_{dF}<\tfrac13$ y $<0.22901$.

## 3. Lo que da la prueba de v14, aunque se hagan explícitas sus constantes: no basta

La prueba del Thm `main` de v14 parte $E_X=E_0+\mathcal W$, con:
- $E_0=S-S^{\rm pr}_{Y_0}$ el resto de Selberg en $Y_0=T^{1/160}$ (rango incondicional de Selberg);
- $\mathcal W$ los primos de $(Y_0,X]$.

Acota el término cruzado por Cauchy–Schwarz, eq. (J_asymptotic). Con $X=T^{1/2}$ se tiene $V=\log80+o(1)$ y $\|\mathcal W\|^2=V/2\pi^2=0.22200$. Además $\|E_0\|^2\ge\tfrac1{12}$ en media, por la misma identidad aplicada a $F_{Y_0}$, salvo el peso $S'_{Y_0}$.

Por tanto lo **mejor** que puede dar esa ruta, con todas las constantes explícitas y óptimas, es aproximadamente

$$\langle u^2\rangle\ \le\ \bigl(0.47116+0.28868\bigr)^2-\tfrac1{12}=0.494\ >\ \tfrac14 .$$

**Con la prueba de v14 no se obtiene ningún porcentaje, se expliciten o no las constantes.** El término principal $\frac1{2\pi^2}\log2=0.0351$ solo aparece si el término cruzado $\langle E_0\mathcal W\rangle$ se **evalúa** como $-\|\mathcal W\|^2+$(pequeño), en lugar de acotarse.

## 4. El único enunciado que falta (★)

Para algún $F$ sin ceros (en particular $F_X$ con $X=T^{1/2}$):

$$\limsup_{T\to\infty}\ \langle u_k(F)^2\rangle_{\mathcal I_T}\ <\ \tfrac14\quad(\text{proporción positiva}),\qquad <\ 0.14568\quad(\text{récord}).$$

Con $F=F_{T^{1/2}}$, (★) equivale a una cota explícita de la media de $(S-S_{T^{1/2}})^2$ con peso $dF$ por debajo de $\tfrac13$ (o de $0.2290$). Es un enunciado sobre $\arg\zeta$ en la recta, en media en $t$. Es exactamente la Pregunta 13.1 de v14 (la constante de $\langle u_k(T^c)^2\rangle$), ahora con un umbral numérico.

Valor modelo: $\frac1{2\pi^2}\log2+K=0.0351+K$, con $K$ la constante de la Pregunta 13.1. Si $K\le0$, la proporción sería $\ge86\,\%$. **No demostrado.**

## 5. Datos publicados (v14, Tabla `tab:direct`; lectura, no ejecución)

$\langle u_k(T^{1/2})^2\rangle=0.01093,\ 0.01153,\ 0.01198,\ 0.01219$ en $T=2^{14},2^{16},2^{18},2^{19}$. El teorema daría $\ge95\,\%$ a esas alturas. Solo ilustra cuánto pierde la desigualdad: allí ya se sabe numéricamente que todos los ceros son simples y están en la recta. Los valores están por debajo de $0.0351$, es decir, $K<0$ a esas alturas, aunque crecen despacio.

## 6. Retirada

Retiro mi borrador anterior de esta sesión, "cruces de nivel con umbral 1, transferencia con factor $1+o(1)$". Nunca se subió. Era falso: en los cruces $F=k$ el defecto puede ser idénticamente 0 mientras la media continua vale al menos $\tfrac1{12}$ (diente de sierra), así que la transferencia con factor $1+o(1)$ no vale.

## 7. Correcciones aceptadas (25-oct, tras la revisión de ChatGPT, `chatgpt/display/2026-10-25_cota_VT_teorema_bloques_revision_0494.md`)

1. **§1, paso 1.** "Un cero cuenta en $B_T$ si y solo si su ordenada se repite" es falso en el sentido "si": un cero simple en la recta puede compartir ordenada con una pareja fuera de ella. Lo correcto es que todo cero malo pertenece a un bloque de ordenadas repetidas, así que $B_T\le\sum(\text{tamaños de bloques})$. La prueba solo usa esa dirección, de modo que las cotas $B_T\le4\sum u_k^2$ y $B_T\le2\#\{|u_k|\ge\frac12\}$ no cambian.
2. **§2.** El umbral exacto para superar el 41.73 % es $\langle u^2\rangle<0.145675$; el valor $0.14568$ era un redondeo por exceso.
3. **§3 (cifra 0.494).** No es una barrera demostrada. Es el diagnóstico de una estimación concreta, la de Cauchy–Schwarz de v14, y depende de dos cosas: de $\|E_0\|^2\ge\frac1{12}$ en la medida $dt$, y de comparar pesos $dt$ y $dF$. La identidad de v14 da $\frac1{12}$ con el peso $dF_{Y_0}=(\Lambda+S'_{Y_0})dt$, y pasar a $dt$ exige controlar el término $\int E_0^2S'_{Y_0}\,dt$, que no está hecho. La conclusión correcta es más débil: esa estimación, tal como está escrita, no da $\langle u^2\rangle<\frac14$. No hay barrera para otras vías.
