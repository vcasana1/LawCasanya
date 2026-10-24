# Umbrales con cota exacta: la proporción se controla con $\langle u_k^2\rangle$, sin $d_T$

Respuesta de Claude, 25-oct-2026. Nota completa: `work/notes/2026-10-25_umbrales_proporcion_cota_exacta.md`.

He demostrado los umbrales como implicaciones exactas e incondicionales. Pero **no tengo un valor explícito demostrado de $d_T$ (ni de su sustituto) que llegue a ellos**, y he comprobado que la cadena de v14 no puede darlo aunque se expliciten todas sus constantes.

## 1. Teorema (exacto, incondicional)

Sea $u_k(F)=k-\tfrac12-F(\gamma_k)$, con $F$ cualquier función continua construida sin ceros; por ejemplo $F_X=N_0+S_X$. No hace falta que $F$ sea monótona. Sea $B_T$ el número de ceros con $T<\gamma\le2T$ que están fuera de la recta o no son simples. Entonces

$$B_T\le 4\sum_{k\in\mathcal I_T}u_k^2,\qquad B_T\le 2\,\#\{k:|u_k|\ge\tfrac12\},$$

luego

$$\text{fracción en la recta y simples}\ \ge\ 1-4\langle u_k^2\rangle .$$

No hay término de borde.

**Prueba.**
- **Bloques.** Un cero es malo si y solo si su ordenada se repite: si está fuera de la recta tiene una pareja con la misma ordenada, y si es múltiple se repite. Dentro de un bloque de $r\ge2$ ordenadas iguales, $u$ avanza exactamente de 1 en 1, porque $F(\gamma)$ es el mismo para todos sus índices.
- **Cota cuadrática.** Para todo $u$ real, $\sum_{i<r}(u+i)^2\ge r(r^2-1)/12\ge r/4$, con igualdad en $r=2$, $u=-\tfrac12$.
- **Cota en probabilidad.** Una progresión de paso 1 tiene a lo sumo un punto en $(-\tfrac12,\tfrac12)$, así que al menos $r-1\ge r/2$ índices del bloque cumplen $|u|\ge\tfrac12$. $\square$

Esto sustituye $d_T$, la fracción de índices malos de una lista. Con una función $F$ el "hueco" vale exactamente 1, así que desaparecen el control de huecos y el transporte.

## 2. Umbrales exactos

$$\langle u^2\rangle<\tfrac14\ \Rightarrow\ \text{proporción}>0,\qquad \langle u^2\rangle<0.14568\ \Rightarrow\ \text{proporción}>41.73\,\%.$$

## 3. Por qué v14 no da el número

La prueba del Thm main de v14 acota por Cauchy–Schwarz el término cruzado entre dos piezas:
- el resto de Selberg en $T^{1/160}$, que tiene norma al cuadrado $\ge\tfrac1{12}$;
- los primos de $(T^{1/160},T^{1/2}]$, con norma al cuadrado $\log 80/2\pi^2=0.222$.

Con constantes explícitas y óptimas, lo mejor que da esa ruta es aproximadamente

$$\langle u^2\rangle\le(0.471+0.289)^2-\tfrac1{12}\approx0.494>\tfrac14 .$$

El valor $\frac{1}{2\pi^2}\log2=0.035$ solo aparece si ese término cruzado se **evalúa** en vez de acotarse.

## 4. Lo único que falta

Hay que demostrar

$$\limsup_T\langle u_k(T^{1/2})^2\rangle<\tfrac14\quad(\text{o }<0.1457\text{ para el récord}).$$

Es exactamente la Pregunta 13.1 de v14, ahora con un umbral numérico. Si la constante fuera $\le0$, la proporción sería $\ge86\,\%$; no está demostrado.

En la Tabla `tab:direct` de v14 (lectura, sin ejecutar nada) los valores son 0.0109–0.0122 para $T=2^{14}$–$2^{19}$, todos por debajo de 0.035. Eso solo mide cuánto pierde la desigualdad: a esas alturas ya se sabe numéricamente que todos los ceros son simples y están en la recta.

## 5. Corrección

Retiro un borrador anterior de Claude, que nunca se subió: el de los cruces de nivel con umbral 1. Su paso de la media continua a los cruces era falso, porque en los cruces el defecto puede ser 0 mientras la media continua vale al menos $\tfrac1{12}$.
