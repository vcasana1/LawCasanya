# Auditoría previa de la construcción de `zCasanya1.bin`

Fecha: 2026-10-18

## Fuente verificada

- Manuscrito: `source/ordinal_prime_cutoff_v13.tex`
- SHA-256 del manuscrito: `3b3c4c8fa27ce251ef77aba8f2ad86b234f097567f6cd8e00c5220971073f999`
- ZIP v13: `source/ordinal_prime_cutoff_v13.zip`
- SHA-256 del ZIP: `b6eca909bc3e047cb35612b88ca57fd001059c1b41ee85cb0947253b1647d501`
- El `.tex` expandido del ZIP y la copia del manuscrito tienen el mismo SHA-256.

Esta auditoría leyó `inputs/zLamb.bin` y el fichero de primos únicamente para verificar el rango y sus hashes. No abrió `inputs/zeross.bin`.

## Construcción escrita en v13

Con

\[
N_0(t)=\frac{t}{2\pi}\log\frac{t}{2\pi e}+\frac78,
\qquad
L(t)=N_0'(t)=\frac1{2\pi}\log\frac{t}{2\pi},
\]

el manuscrito define

\[
S_X(t)=-\frac1\pi\sum_{p\le X}\arg(1-p^{-1/2-it})
=-\frac1\pi\sum_{p\le X}\sum_{m\ge1}\frac{\sin(mt\log p)}{m p^{m/2}},
\]

y la recurrencia

\[
x_k^{(0)}=\tau_k,\qquad
x_k^{(j)}=x_k^{(j-1)}-
\frac{N_0(x_k^{(j-1)})+S_{X_j}(x_k^{(j-1)})-(k-\tfrac12)}
{L(x_k^{(j-1)})}.
\]

En un bloque de altura `(T,2T]`, los cortes del Teorema 8.10 son `X_j=T^{c_j}`, con

\[
H_0=\log\log T,\quad c_1=H_0^{-1/2},\quad H_1=\log H_0,
\quad c_2=H_1^{-1/2},
\]

y, para `j>=3`,

\[
c_j=C_\star H_{j-1}^{-9/16},\qquad
H_j=2\log(1/c_j).
\]

El número de pasos es el primer índice `m` para el que `H_m<H^*`.

## Por qué el teorema no determina el binario solicitado

1. El manuscrito declara expresamente que `C_star`, `H^*`, `B` y `C_6` son constantes absolutas no calculadas. Por tanto no determina numéricamente los cortes desde el tercer paso ni `m^*(T)`.
2. La demostración exige `H^* >= 160^2*4 = 102400`, además de otras cotas con constantes no calculadas. En los datos, `H_0` nunca supera `2.6293`; la regla de parada queda fuera del régimen no vacío de iteración.
3. En todos los bloques diádicos cubiertos por `zLamb.bin`, `c_1>0.616`; el Teorema 8.9 exige `c_i<=1/2`. El segundo exponente es mayor que `1` donde está definido y no es real en el primer bloque. En el último bloque `T=2^20`, por ejemplo, `c_1=0.6167179511` y `c_2=1.0170845701`.
4. El propio manuscrito dice en su línea 1596 que los cortes asintóticos no son alcanzables en `T=2^19`; el programa `opc_iteration_v13.py` repite esa advertencia y usa ternas ilustrativas `(1/5,1/3,1/2)`, `(1/3,1/2,1/2)` y `(1/10,1/5,1/3)`. Elegir una de ellas sería una convención finita ajena al Teorema 8.10.
5. El teorema se formula por bloques `I_T={k:T<gamma_k<=2T}`. Construir un único archivo para todos los índices sin usar `zeross.bin` exige además fijar una partición basada solo en `tau_k` o un corte local. El Teorema 8.10 no especifica esa extensión global.

## Decisión

No se generó `zCasanya1.bin`. Cualquier salida no trivial requeriría escoger valores o convenciones que no están especificados por el Teorema 8.10, en contradicción con la instrucción de no sustituir constantes ausentes por valores arbitrarios. Tampoco se abrió `zeross.bin`, porque aún no existe un archivo construido y congelado que comparar.

Una ejecución reproducible necesita que se suministren, fuera del teorema, `C_star`, `H^*`, una regla de bloques basada únicamente en `zLamb.bin` y una regla explícita para las alturas donde `H_1<=0` o los exponentes incumplen las hipótesis.

## Auditoría de efectividad de las constantes

### Dependencias externas

La prueba no contiene una cadena de constantes numéricas cerrada. Sus entradas son:

| Entrada | Uso en 8.9--8.10 | Estado en v13 |
|---|---|---|
| Constante absoluta de la aproximación de Selberg--Fujii, Teorema 3.5 | Lema 8.2: momentos de `E_X` y de `u_k(X)` hasta orden creciente | Se llama `C`; no se da valor ni umbral efectivo |
| `C_1^{Fujii}`, `C_2^{Fujii}` y umbral de Fujii, Teorema 3.6 | Lema 8.8: momentos segundo y cuarto de `S(t+h)-S(t)` | Solo existen `C_k` y `T_0`; no se dan valores |
| Constante del error `O(n)` de Montgomery--Vaughan, Teorema 3.7 | Momentos de polinomios de Dirichlet y derivadas de `S_X` | Absoluta, pero no numerada en el manuscrito |
| Constantes de Mertens | Control de `V`, sumas sobre primos y derivadas | Escritas como `O(1)` o `ll`, sin valores |
| `A_p` del maximal de Hardy--Littlewood | Lema 8.4: muestreo en puntos de multiplicidad acotada | Solo se afirma que `A_p` está acotada para `p>=2` |
| Constantes de `S(t)=O(log t)`, huecos acotados y conteo local | Lema 8.8 y términos de borde | No efectivas en la formulación usada |
| Comparaciones `#I_T asymp T/b_T`, `L(tau) asymp log T` y todos los `o(1)` | Conversión de integrales en medias discretas y absorción de términos | Sin módulos de convergencia ni umbral común |

El bound explícito de Bellotti--Wong sí permite hacer efectiva la cota puntual usada para mantener los puntos cerca del bloque, pero no sustituye los momentos de Selberg--Fujii ni los momentos de incrementos de Fujii.

### Constantes internas y su grafo de dependencia

La dependencia que realmente aparece en la demostración es:

1. Los resultados externos anteriores producen una constante de momentos `C_mom`, una constante de muestreo `C_samp`, una constante base `C_0` y los constantes de pares cercanos `C_1,C_2`.
2. El Teorema 8.9 permite tomar, tras posibles ampliaciones para cubrir `Lambda_0>=2`,

   \[
   C_3=2\sqrt{260\,C_1\sqrt{C_2}}.
   \]

3. La desigualdad de un paso de la prueba de 8.10 reúne `C_mom`, `C_samp`, las comparaciones asintóticas y `C_3` en constantes llamadas `C` y `C_5`. El manuscrito no escribe una fórmula numérica para `C_5`.
4. Solo después se fija

   \[
   C_\star=\min\{1,(4\pi C C_3^{1/8})^{-1}\}.
   \]

5. Se define

   \[
   B=\max(2C,C_0,1),\qquad
   C_6=\left(\frac{4C}{B}+\frac{4C_5(4B)^{9/8}}B\right)^2.
   \]

6. `H^*` puede ser cualquier constante que satisfaga

   \[
   H^*\ge\max(4C_6,4\cdot160^2)
   \]

   y, para todo `H>=H^*`,

   \[
   \exp\!\left(\frac89(H-2\log(1/C_\star))\right)\ge4H,
   \qquad e^H\ge4H.
   \]

7. `T_0` debe dominar simultáneamente los umbrales externos, los umbrales de todos los `o(1)`, las comparaciones del reloj, las cotas de soporte, `X_j>=2` y las restricciones de longitud de todos los polinomios de Dirichlet. El manuscrito no lo define como un máximo explícito.

Por tanto, `C_star` y `H^*` serían calculables si se proporcionaran versiones numéricas de todas las constantes anteriores y módulos efectivos para los `o(1)`. Con el texto actual no lo son. `T_0` tampoco puede recuperarse del manuscrito, porque varias entradas externas están en forma asintótica.

## Altura efectiva

No existe un valor numérico de `T_efectiva` deducible de v13. Sí existen dos cotas inferiores necesarias, independientes de las constantes desconocidas:

1. El Lema 8.2 exige `2<=X<=T^(1/(160r))`. Ya para `r=1` esto requiere

   \[
   T\ge2^{160}\approx1.46\cdot10^{48}.
   \]

2. La elección escrita en la prueba exige `H^*>=4*160^2=102400`. Para que haya siquiera un primer paso uniforme hay que tener `H_0=log log T>=H^*`; por tanto

   \[
   T\ge\exp(\exp(102400)).
   \]

Esta segunda cota domina a la primera y sigue siendo solo una cota inferior: las constantes `C_6`, `C_star` y `T_0` pueden elevarla. En forma manejable,

\[
\log_{10}\log_{10}T\ge 44471.3927\ldots.
\]

Para obtener dos pasos se necesitaría además `H_1=log H_0>=H^*`, es decir, una torre exponencial adicional.

## Comprobación sobre `zLamb.bin`

El preflight reproducible `zCasanya1_v13_preflight.py` usa solamente `zLamb.bin` y los primos. Sus resultados están en `zCasanya1_v13_preflight.json`.

- `zLamb.bin` contiene 2.001.052 valores y termina en `1.132.490,7225876215`.
- En el bloque superior basado en el reloj, `T=2^20`, se obtiene `H_0=2.62921935297`, `c_1=0.61671795110` y `c_2=1.01708457005`.
- En todos los bloques cubiertos, `c_1>1/2`; `c_2` es no real en el primer bloque y mayor que `1/2` en los demás.
- El mayor valor de `T^(1/160)` en todos los bloques es `1.09050773267<2`; por tanto el intervalo del Lema 8.2 está vacío incluso para `r=1`.
- El déficit frente al requisito mínimo `H_0>=102400` no es marginal: `H_0` no llega a `2.63`.

Conclusión inequívoca: el Teorema 8.10 no es aplicable numéricamente a ninguna altura de este archivo. Sus garantías asintóticas no justifican ningún paso de Newton de la iteración uniforme en el rango disponible.

## Especialización finita

No hay una especialización finita no trivial justificada por los mismos lemas a estas alturas. El motivo no es solo que falten valores de constantes: la hipótesis estructural `2<=X<=T^(1/(160r))` deja vacío el conjunto de cortes. Las ternas del programa v13 son ilustraciones expresamente declaradas fuera del régimen asintótico.

La recurrencia de Newton sí puede evaluarse aritméticamente para cualquier secuencia de cortes predeclarada, pero eso solo produce puntos computables; no hereda la estimación del Teorema 8.10.

### Qué resultado adicional haría posible una versión finita

- **[LIT, en la cadena de v13]** Una versión totalmente explícita de la aproximación de Selberg--Fujii y del teorema de incrementos de Fujii, con constantes numéricas y umbrales válidos para los órdenes requeridos, permitiría calcular `C_1,C_2,C_3,C_star,H^*` y un `T_0`. Aun así, con el exponente `1/(160r)` conservado, no alcanzaría las alturas actuales.
- **[DED]** Para trabajar hasta `1.132.491` haría falta reemplazar el Lema 8.2 por un teorema finito de momentos que admita algún `X>=2` en ese rango, además de versiones explícitas del muestreo maximal y de la multiplicidad. Ese reemplazo es matemáticamente nuevo respecto de la demostración escrita; no se deduce ajustando las constantes actuales.
- **[DED, ruta de certificación finita]** Se podría predeclarar una regla aritmética de cortes sin consultar los ceros, congelar los puntos, y después certificar con aritmética de intervalos las identidades, momentos y multiplicidades del conjunto finito. Esto produciría un teorema computacional finito, no una instancia del Teorema 8.10, y requeriría usar ordenadas certificadas solo en la fase posterior de prueba.

Se han identificado tres rutas: una procede de la literatura empleada por v13 y dos son deducciones para hacer finita la verificación. Ninguna permite llamar a una salida en la altura actual “la construcción del Teorema 8.10” sin un nuevo resultado o una convención adicional.
