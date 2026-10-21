# Corrector analítico desde la v14: sistema cuadrático, factores completos y criterio por cero

Base solicitada por el autor: `/Users/vcasana/Downloads/prime_corrected_clock_v14.tex`, SHA256 `d2ffdb9703f0e6040dc12cb2eda1396a038d3f4b9e248ce263aa171208a4ac31`. Esta nota no modifica el manuscrito ni crea una nueva versión del artículo. No se leen datos de ceros ni se ajusta ningún parámetro a sus errores.

La discusión y revisión transmitidas por el autor están archivadas por Claude en `work/display/2026-10-21_variante_cuadratica_D_prima.md` (commit67ea340). Esta nota incorpora sus tres comprobaciones solicitadas para el segundo momento: alturas buenas L2, contorno o(#I) y constante absoluta. No se atribuye a esta variante una mejora teórica sobre D′.

## 1. Rectificación del punto de partida

La secuencia empírica (8,8,512) no se deduce de la ley de cortes de la v14. Mejorar el solver de esa secuencia no aporta la justificación analítica que el autor solicita. El diagnóstico anterior se conserva como diagnóstico de un algoritmo histórico, no como solución de este problema teórico.

La v14 NO contiene esos cortes manuales: B y D usan sus cortes teóricos y D′ un único corte de exponente fijo. La presente propuesta sustituiría la receta de c667; respecto a D′, cambia únicamente el objetivo variacional de L4 a L2. Mi anuncio de que se «sustituyen los tres cortes» debía explicitar que se refería a c667.

Hay además dos fases diferentes. La v14, ecuación `eq:SX_def`, define

\[
S_X(t)=-\frac1\pi\sum_{p\le X}\sum_{m\ge1}
 \frac{\sin(mt\log p)}{mp^{m/2}}.
\]

c667 corta por **potencia** p^m≤X. No se transfieren sin prueba los resultados de una fase a la otra. La presente nota usa literalmente los factores completos de la v14. Tampoco introduce el desplazamiento delta=10^-6 del benchmark LeClair.

El teorema `thm:main` y su corolario `cor:fixed_cutoff` afirman que un corte fijo deja un defecto cuadrático medio creciente como (2π²)^−1 log log T. Son afirmaciones asintóticas sobre el defecto en las ordenadas, no una cota puntual de sus distancias ni un resultado numérico a T≈10^6. La ley local `cor:local_clock` no justifica recortar su exponente a mano: su prueba necesita T suficientemente grande y el rango de corte correspondiente. La v14 tampoco da valores numéricos de todas las constantes de la iteración uniforme.

## 2. Construcción propuesta [ADAPT de D′ de la v14]

El teorema D′ aproxima F_X=N0+S_X en L4 mediante funciones con pendiente controlada. Aquí se propone su **variante L2**, para obtener ecuaciones cuadráticas/lineales y cargas expresadas analíticamente. No se afirma que tenga menor error real que la variante L4; se demuestra abajo que conserva su orden de error cuadrático medio, bajo los resultados de la v14 que se indican.

Se fijan exactamente la ventana y malla de la v14:

\[
\Lambda=\frac{\log T}{2\pi},\quad J=[T/2,3T],\quad
M=\left\lceil\frac52T\Lambda\right\rceil,\quad h=\frac{5T}{2M},\quad t_i=T/2+ih.
\]

Sea K el conjunto de interpolantes lineales con pendientes entre a=Λ/2 y b=2Λ. Para 2≤X≤√(T/2), definir

\[
P_2=\arg\min_{P\in K}\int_J|P(t)-F_X(t)|^2dt,
\qquad P_2(x_k)=k-\tfrac12.
\tag{A}
\]

Todos los datos de (A) son el reloj, los primos y la altura. Una especificación sin un exponente libre es X=√(T/2), el mayor corte admitido por el lema de bloque utilizado: esto minimiza el factor de la **cota superior disponible**, no se declara minimizador del error real. No hay secuencia de tres cortes ni coeficientes aprendidos de ceros. Definir un objeto por un problema variacional justificado no significa ajustar a una tabla de ordenadas.

La definición es por bloque. No se reclama orden global al pegar resultados de minimizadores de bloques diferentes: esa unión requeriría un argumento adicional.

### Ecuaciones determinadas por los primos

Sean B_i las funciones sombrero, P_v=Σ_i v_i B_i, G_ij=∫_J B_i B_j y d_i=∫_J B_i F_X. La función objetivo, salvo una constante independiente de v, es vᵀGv−2dᵀv. G es definida positiva porque vᵀGv=∫P_v²>0 si v≠0. Sus únicas entradas no nulas son

\[
G_{ii}=2h/3\ (0<i<M),\quad G_{00}=G_{MM}=h/3,
\qquad G_{i,i+1}=h/6.
\]

Con Dv=(v_i−v_{i−1})_i, las condiciones necesarias y suficientes son

\[
Gv-d+D^T(\mu_+-\mu_-)=0,\qquad ah\le Dv\le bh,
\tag{B}
\]
\[
\mu_\pm\ge0,\quad
\mu_{+,i}((Dv)_i-bh)=0,\quad
\mu_{-,i}(ah-(Dv)_i)=0.
\]

Los multiplicadores corresponden al objetivo dividido por dos. Existen por factibilidad estricta (un interpolante afín de pendiente (a+b)/2), y G definida positiva asegura un único v. En un conjunto activo fijado, (B) es un sistema lineal; determinar ese conjunto forma parte de resolver las ecuaciones, no de seleccionar parámetros contra gamma.

## 3. Cargas cerradas mediante trilogaritmos [DED]

Poner z_p(t)=p^−1/2 exp(it log p) y

\[
\mathcal V_X(t)=\frac1\pi\sum_{p\le X}
 \frac{\operatorname{Im}\operatorname{Li}_3(z_p(t))}{(\log p)^2}.
\tag{C}
\]

La serie Li_s(z)=Σ_{m≥1}z^m/m^s converge absolutamente para |z|<1, como aquí. Derivando dos veces, **V_X″=S_X**, con el mismo signo y todos los factores completos de la v14. Para un nodo interior:

\[
d_i^{\rm primes}=\int_JB_iS_X
=\frac{\mathcal V_X(t_i-h)-2\mathcal V_X(t_i)+\mathcal V_X(t_i+h)}h.
\tag{D}
\]

Equivalentemente,

\[
d_i^{\rm primes}
=-\frac h\pi\sum_{p\le X}\sum_{m\ge1}
\frac{\sin(mt_i\log p)}{mp^{m/2}}
\operatorname{sinc}^2\!\left(\frac{mh\log p}2\right),
\quad\operatorname{sinc}z=\frac{\sin z}z.
\tag{E}
\]

Estos pesos sinc² proceden exactamente de integrar una función sombrero; no son pesos elegidos para mejorar un RMS observado. Son cargas del sistema (B), no una autorización para ignorar G y multiplicar directamente los coeficientes de la predicción.

**Alcance exacto.** Las fórmulas (C)–(E) para las cargas son válidas tanto con restricciones activas como inactivas: el vector d no depende del conjunto activo. No son una fórmula cerrada del minimizador. Solo sin restricciones activas se obtiene v=G^−1 d; con restricciones activas hay que resolver (B). No se da una forma cerrada global para v ni se estima aquí la medida de la región activa.

En una malla uniforme infinita o periódica, el símbolo interior de G/h es (2+cos(ωh))/3. La respuesta de los VALORES NODALES del problema no restringido es entonces sinc²(ωh/2)/((2+cos(ωh))/3), no sinc² solo. Por ejemplo, en ωh=π esa ganancia nodal es12/π²>1, aunque sinc²(π/2)=4/π². La reconstrucción lineal a trozos también interviene: no se identifica esa ganancia nodal con la amplitud continua de una única sinusoide. En un bloque finito intervienen además los extremos. Con restricciones activas no hay un único multiplicador de Fourier que describa el corrector.

En los dos extremos las fórmulas correctas son

\[
d_0^{\rm primes}=-\mathcal V_X'(t_0)
+\frac{\mathcal V_X(t_0+h)-\mathcal V_X(t_0)}h,
\]
\[
d_M^{\rm primes}=\mathcal V_X'(t_M)
-\frac{\mathcal V_X(t_M)-\mathcal V_X(t_M-h)}h,
\qquad
\mathcal V_X'(t)=\frac1\pi\sum_{p\le X}
\frac{\operatorname{Re}\operatorname{Li}_2(z_p(t))}{\log p}.
\]

La parte suave tampoco requiere cuadratura empírica. Con N0(t)=t(log(t/(2π))−1)/(2π)+7/8, dos primitivas son

\[
A_0(t)=\frac{t^2}{4\pi}\log\frac t{2\pi}-\frac{3t^2}{8\pi}+\frac{7t}8,
\qquad
A_1(t)=\frac{t^3}{6\pi}\log\frac t{2\pi}-\frac{2t^3}{9\pi}+\frac{7t^2}{16},
\]

con A_0′=N0 y A_1′=tN0. Las cargas interiores suaves son

\[
d_i^0=\frac{[A_1-(t_i-h)A_0]_{t_i-h}^{t_i}
+[(t_i+h)A_0-A_1]_{t_i}^{t_i+h}}h;
\]

en los extremos se conserva el único término presente. Por tanto, (B) es una especificación mediante ecuaciones cuyos coeficientes están dados por logaritmos, primos, Li2 y Li3; no utiliza ninguna gamma.

## 4. Garantía analítica que sí se conserva [DED, condicionada a los lemas citados de v14]

**Proposición.** Tomando como base `lem:slope_envelope`, `lem:block_fourth` y la identidad para modelos Lipschitz `lem:identity_lipschitz` de la v14, existen constantes absolutas C,T0 tales que, para T≥T0 y 2≤X≤√(T/2), el corrector (A) tiene puntos definidos para todos los índices de I_T y de I_T^tau, crecientes dentro del bloque, con

\[
\frac\pi{\log T}\le x_{k+1}-x_k\le\frac{4\pi}{\log T},
\qquad
\langle|x_k-\gamma_k|^2\rangle_{\mathcal I}
\le \frac{C(1+\log(1/c))}{\log^2T},\quad c=\frac{\log X}{\log T},
\tag{F}
\]

donde I es cualquiera de esos dos conjuntos de índices. No se afirma aquí la garantía de cuarto momento de la variante L4 ni una mejor constante que ella.

**Prueba.** Escribir W=1+log(1/c)≥1. El lema de envolvente da P_N∈K con ∫|P_N−N|⁴≤C T; Hölder da ||P_N−N||₂≤C√T. El lema de bloque da ∫|F_X−N|⁴≤C T W² y, de nuevo por Hölder, ||F_X−N||₂≤C√(TW). La minimalidad en (A) implica

\[
\|P_2-N\|_2\le\|P_2-F_X\|_2+\|F_X-N\|_2
\le\|P_N-N\|_2+2\|F_X-N\|_2,
\]

por lo que ∫_J|P_2−N|²≤D T W. Más explícitamente, si los dos lemas citados tienen constantes absolutas C_N y C_F en sus cotas de cuarto momento, basta tomar

\[
D=\left((5C_N/2)^{1/4}+2(5C_F/2)^{1/4}\right)^2.
\]

En efecto, las dos normas L2 se acotan respectivamente por (5C_N/2)^{1/4}√T y (5C_F/2)^{1/4}√(TW), y W≥1. Por tanto D es absoluta, no depende del conjunto activo ni de c, y no se obtiene ajustando datos.

Tomar K0²=16DW. Chebyshev en L2 da meas{|P_2−N|>K0}≤T/16. Los intervalos [T/2+C_g,3T/4] y [9T/4,3T−C_g−1] tienen longitud mayor que T/16 para T suficientemente grande; por tanto existen t_flat y t_sharp en ellos con |P_2−N|≤K0. No se usan alturas elegidas mediante una cota L4 del minimizador. Aquí C_g es la cota uniforme para gaps usada en la v14.

Como K0=O(√(1+log log T)), P_2(T/2)≤N(3T/4)+K0 y P_2(3T)≥N(9T/4)−K0, mientras N(T)−N(3T/4) y N(9T/4)−N(2T) tienen orden T log T. Para los índices del reloj se usa además N−N0=O(log T). Esto prueba P_2(T/2)<k−1/2<P_2(3T) para ambos conjuntos centrales. Las mismas holguras de orden T log T incluyen los niveles de los vecinos k±1. Las ordenadas de I_T^tau están en [T−C_0,2T+C_0] por la cota de desplazamiento de la v14, por lo que también pertenecen al intervalo entre las dos ordenadas de contorno para T grande.

Poner k1=N(t_flat), k2=N(t_sharp)+1 y u_k=k−1/2−P_2(gamma_k). Como en la prueba de D′, u_k1≥−K0−1/2 y u_k2≤K0+1/2. La identidad de v14 con j=1, válida para P_2 Lipschitz, da exactamente

\[
\sum_{k_1<k<k_2}(u_k^2+1/12)
=\int_{\gamma_{k_1}}^{\gamma_{k_2}}(N-P_2)^2P_2'\,dt
-\frac{(1/2+u_{k_1})^3+(1/2-u_{k_2})^3}3.
\]

Así, para cualquiera de los dos conjuntos centrales I,

\[
\sum_{k\in\mathcal I}u_k^2\le2\Lambda\int_J(N-P_2)^2dt+2K0^3/3.
\]

El contorno superior usado es 2K0³/3=O(W^{3/2})=O((1+log log T)^{3/2})=o(#I), uniformemente en 2≤X≤√(T/2). Esta es una cota superior para su posible contribución, no una afirmación de que el término exacto tenga signo positivo. Dividir por #I≈T log T da ⟨u²⟩≤C W, con un contorno normalizado o(1). Como P_2′≥Λ/2 y gamma_k,x_k∈J, |x_k−gamma_k|≤2|u_k|/Λ, lo que prueba (F). Las separaciones se deducen de \(1=P_2(x_{k+1})-P_2(x_k)\) y de las dos cotas de pendiente. Fin de la prueba.

Los datos de ceros aparecen en esta demostración, no en (A)–(E). No se han evaluado C,T0 ni se ha afirmado que el régimen efectivo empiece a las alturas del benchmark. La demostración es una deducción a partir de los resultados indicados del manuscrito suministrado, no una revisión independiente completa de todas sus fuentes externas.

Esta prueba usa los lemas de la v14 para la fase ORIGINAL F_X y la compara con el minimizador: no aplica el Teorema B directamente a una fase filtrada ni conserva su término principal. La estimación depende de la minimalidad sobre TODA K, válida cualquiera que sea el conjunto activo; no requiere controlar la medida de ese conjunto para esta cota O(W/log²T). Para afirmar un término principal preciso o una mejora de constantes sí haría falta un análisis adicional. El apartado (d) de D′ y su control de transporte por cuartos momentos NO quedan demostrados para P_2.

## 5. Vínculo exacto con el criterio individual del autor [DED]

Para cualquier P creciente con a≤P′≤b y P(x_k)=q_k=k−1/2, sean \(m_k^-=(x_{k-1}+x_k)/2\), \(m_k^+=(x_k+x_{k+1})/2\) y

\[
\theta_k^-=q_k-P(m_k^-),\qquad \theta_k^+=P(m_k^+)-q_k.
\]

Entonces la pertenencia del cero verdadero a SU celda sintética es exactamente

\[
m_k^-<\gamma_k<m_k^+
\quad\Longleftrightarrow\quad
-\theta_k^+<u_k<\theta_k^-,\qquad u_k=q_k-P(\gamma_k).
\tag{G}
\]

Además,

\[
\frac a{a+b}\le\theta_k^\pm\le\frac b{a+b}.
\tag{H}
\]

Para probarlo, dividir un intervalo entre x_k−1 y x_k en sus dos mitades. Las integrales de P′ en las mitades suman1; su cociente está entre a/b y b/a porque tienen igual longitud. Una de ellas, theta_k^-, está por ello entre a/(a+b) y b/(a+b). El argumento a la derecha es idéntico. Las cotas se alcanzan poniendo pendiente a en una mitad y b en la otra; no son parámetros ajustados.

Con las pendientes de v14 se obtiene 1/5≤theta_k^±≤4/5. En particular, |u_k|<1/5 es suficiente para acertar la celda y |u_k|≥4/5 obliga a incumplirla. Entre ambos valores se aplica (G), no el mínimo de las separaciones. Estas son condiciones por índice, con los vecinos del propio modelo.

Este puente no convierte (F) en una garantía para todos los k. Solo da, por ejemplo, #fallos/#I≤25⟨u²⟩, que puede ser totalmente vacua con las constantes disponibles. Una afirmación uniforme |u_k|<1/5 para todos los ceros contados con multiplicidad sería muchísimo más fuerte: excluiría ordenadas repetidas (dos índices repetidos dan defectos que difieren en1), y por simetría implicaría RH y simplicidad. No se asume tal afirmación ni se pretende haberla demostrado.

## 6. Decisión y límites

Se abandona (8,8,512) como fundamento teórico de una nueva ley. La candidata de esta nota es (A)–(E), con el corte del rango demostrado, y la tarea analítica es mejorar el control del defecto relevante para (G). No se propone seleccionar cortes, pesos o ramas mirando gamma, ni usar como constructor la regresión de `rem:matrix_projection` de v14: su vector b contiene s_k y por tanto información de los ceros verdaderos.

Dependencias: fase completa y lemas de v14 → cargas analíticas y minimizador único → cota L2 del modelo contra N → identidad de defectos → (F). Por otra parte, pendientes y niveles → (G)–(H). La primera afirmación que faltaría para convertirlo en identificación universal es un control uniforme del defecto en cada cero; no lo aporta la cota de momentos. El mecanismo específico de zeta entra por los lemas de aproximación de primos y de la función contadora, no por la geometría de una curva creciente.

Lo obtenido es una variante cuadrática con cargas analíticas y una deducción de segundo momento condicionada a los lemas indicados de v14; **no** una mejora establecida de la v14. No se ha demostrado una mejora de precisión frente a D′, Gonek o LeClair, ni un nuevo orden asintótico, ni un criterio individual que se cumpla siempre. El cuarto momento, el transporte de D′(d), la descripción del conjunto activo y la unión de bloques no se dan por resueltos. No se ha hecho una búsqueda de prioridad: no se reclama novedad bibliográfica. Una ruta de construcción [ADAPT] y dos deducciones de sus ecuaciones/criterio [DED]; ninguna se declara exterior a la literatura conocida.

## 7. Regla del autor: ninguna selección post hoc

La receta (8,8,512) se conserva únicamente como configuración numérica histórica. Haber escogido unos parámetros tras comparar sus errores no constituye una deducción de esos valores a partir de v14. La nueva propuesta no usa esa secuencia como referencia para elegir los suyos.

La especificación matemática presentada fija: factores completos (sin delta), (A) como objetivo, la malla y pendientes de v14, y X=√(T/2) como máximo corte del rango cubierto por el lema de bloque. No se declara óptimo para el error real. El bloque T de una eventual prueba se deberá determinar mediante alturas/índices del reloj antes de consultar las ordenadas; no se ha fijado todavía un nuevo experimento independiente ni se ha ejecutado el predictor cuadrático.

Los valores de tolerancia y todos los detalles de implementación que falten se deberán fijar y registrar ANTES de evaluar un nuevo bloque. No se escogerán a partir del RMS, del número de violaciones o de los peores ceros observados. Verificar identidades de integración con datos artificiales no elige parámetros de predicción ni reemplaza la prueba.

Los bloques del benchmark ya se han visto. Una futura comparación sobre ellos será retrospectiva/exploratoria y no se llamará una nueva validación independiente o ciega. La propuesta surgió durante una discusión posterior a ese benchmark: declarar que sus fórmulas no usan gamma no convierte ese historial en información no observada. Se preservarán y reportarán también los resultados desfavorables; cualquier cambio posterior será otra versión con una nueva evaluación independiente. No se presenta la variante como más precisa antes de demostrarlo o comprobarlo bajo ese protocolo.
