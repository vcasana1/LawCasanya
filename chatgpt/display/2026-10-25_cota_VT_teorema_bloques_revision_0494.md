# Demostración de la tasa de banda armónica y auditoría del commit 9724b05

Respuesta completa de ChatGPT, 25 de octubre de 2026, a la revisión del commit de Claude y a la pregunta por una condición suficiente más fuerte que V_T \to 0.

## 1. La cota fuerte V_T log log T -> 0 queda demostrada

No necesitamos imponer monotonía a X_k.

Sea T<tau_k<=2T, con 2<=X_-<=X_k<=X_+<=T^{c_0}, c_0<b<1, y definamos

$$
V_T=\sum_{X_-<p\le X_+}\frac1p,\qquad
u_T=\log X_-,\qquad
\Delta_T=\log\frac{X_+}{X_-}.
$$

Por el teorema de Mertens para la suma de recíprocos de primos,

$$
V_T=\log\left(1+\frac{\Delta_T}{u_T}\right)+O\left(\frac1{u_T}\right)
\ll\frac{\Delta_T+1}{u_T}.
$$

Por tanto, hemos demostrado el criterio suficiente

$$
\boxed{
\frac{(\Delta_T+1)\log\log T}{u_T}\longrightarrow0
\quad\Longrightarrow\quad V_T\log\log T\longrightarrow0.
}
$$

El resultado permite variaciones arbitrarias entre índices, siempre que se respete la banda indicada.

Para los cortes concretos:

| Corte dependiente de k | Cota para V_T log log T |
|---|---|
| X_k=(tau_k/2pi)^c exp(h_k), abs(h_k)<=A | O(log log T/log T) |
| c(k)=c_*+a sin(log log(tau_k/2pi)) | O(log log T/log T) |
| c(k)=(log log tau_k)^(-1/2) | O((log log T)^(3/2)/log T) |

Las tres cotas tienden a cero. En consecuencia, utilizando el lema de estabilidad de Omega_b,

$$
\boxed{\Omega_b[x]-\Omega_b[s]\longrightarrow0}
$$

para esas familias de cortes realmente variables.

También se obtiene un criterio explícito para exponentes arbitrarios con 0<c_-<=c(k)<=c_+<b. Si

$$
d_T=\max_{k\in\mathcal I_T}c(k)-\min_{k\in\mathcal I_T}c(k),
$$

entonces

$$
V_T\log\log T\ll_{c_-,c_+}
\left(d_T+\frac1{\log T}\right)\log\log T.
$$

Basta que d_T log log T -> 0, sin ninguna condición de monotonía.

Límite exacto: V_T -> 0 por sí solo no implica esta tasa más fuerte.

## 2. Revisión del commit 9724b05: el nuevo teorema de conteo es válido

Fuente: https://github.com/vcasana1/LawCasanya/commit/9724b05523fe8f9aca7cdb7a3f0bfcda216bb75f

La desigualdad

$$
\boxed{B_T\le4\sum_{k\in\mathcal I_T}
\left(k-\frac12-F(\gamma_k)\right)^2}
$$

es incondicional y correcta. No requiere que F sea monótona ni conocer las partes reales de los ceros. La desigualdad finita solo necesita que F(\gamma_k) tenga un valor real bien definido.

Para un bloque de longitud m>=2 con ordenadas repetidas, sus defectos son u,u+1,...,u+m-1 y

$$
\sum_{j=0}^{m-1}(u+j)^2\ge\frac{m(m^2-1)}{12}\ge\frac m4.
$$

CORRECCIÓN NECESARIA: La prueba de Claude dice que un cero es malo si y solo si su ordenada se repite. La implicación inversa no está demostrada: podría existir un cero simple sobre la recta con la misma ordenada que una pareja fuera de ella. La afirmación suficiente es que todo cero fuera de la recta o múltiple pertenece a un bloque de ordenadas repetidas. B_T es A LO SUMO la suma de los tamaños de esos bloques; no necesariamente igual. La prueba y la constante 4 se conservan.

También se conserva

$$
B_T\le2\,\#\{k\in\mathcal I_T:|u_k|\ge\tfrac12\}.
$$

No hay pérdida de borde porque la ventana está definida mediante las ordenadas verdaderas y contiene cada bloque completo.

El umbral de proporción positiva es <u^2><1/4. Para superar el 41,73%, la condición exacta es

$$
\boxed{\langle u^2\rangle<0.145675,}
$$

no 0.14568, redondeo ligeramente demasiado permisivo.

## 3. La cifra 0.494: problema matemático real

Se cotejó con manuscript/ordinal_prime_cutoff_v14.tex, demostración de thm:main y ecuaciones J_asymptotic, main_step1 y main_step2.

Claude calcula

$$
B=\frac{\log80}{2\pi^2}=0.22199606\ldots
$$

y

$$
\left(\sqrt B+\sqrt{\frac1{12}}\right)^2-\frac1{12}
=0.49402306\ldots.
$$

La aritmética es correcta, pero no la justificación de esa cifra como un límite matemático de la demostración.

PRIMER PROBLEMA: UNA COTA INFERIOR NO ES UNA SUPERIOR.

Si

$$
A=\frac1T\int_T^{2T}|E_0(t)|^2\,dt,
$$

Cauchy--Schwarz da solamente

$$
\frac1T\int_T^{2T}|E_0+\mathcal W|^2dt
\le(\sqrt A+\sqrt B)^2.
$$

Aunque A>=1/12 estuviera demostrado, esto implicaría

$$
(\sqrt A+\sqrt B)^2-\frac1{12}\ge0.494023\ldots,
$$

no una cota superior 0.494 para el error real.

Interpretación permisible: dentro de esta estimación concreta por desigualdad triangular, y suponiendo A>=1/12, ni siquiera el valor mínimo de la cota superior sirve para llegar a 1/4. No es una barrera universal de v14.

SEGUNDO PROBLEMA: EL TÉRMINO 1/12 APARECE CON OTRA MEDIDA.

La identidad de v14 utiliza

$$
\int_T^{2T}E_0(t)^2\,dF_{Y_0}(t)
$$

mientras Selberg--Fujii controla momentos respecto a dt. Como

$$
dF_{Y_0}(t)=(N_0'(t)+S'_{Y_0}(t))\,dt,
$$

se debe controlar el término con S'_{Y_0} antes de deducir la desigualdad sobre A. Citar 1/12 de la identidad discreta no basta. A X=T^{1/2}, la estimación separada del término con S'_X tampoco desaparece automáticamente.

DICTAMEN: 0.494 NO queda aceptada como barrera rigurosamente demostrada de v14. Sí es un diagnóstico numérico de la pérdida causada por una estimación concreta de Cauchy--Schwarz.

Sigue abierto probar

$$
\limsup_{T\to\infty}\langle u_k(T^{1/2})^2\rangle<\frac14.
$$

Con el teorema de bloques esto produciría una proporción positiva incondicional de ceros simples sobre la recta crítica. No está demostrado.

## 4. Consecuencias para el próximo manuscrito

| Resultado | Alcance |
|---|---|
| thm:goodcount de v12 | Proporción >=1-4d_T, dependiente de una lista corregida |
| Nuevo teorema de bloques | Proporción >=1-4<u^2>, sin controlar huecos de una lista |
| S2 | Descomposición mediante proyección y resto ortogonal |
| Lema Omega | Estabilidad del resto para cortes dependientes de k en bandas armónicas estrechas |

La desigualdad de conteo elimina hipótesis geométricas que necesitaba thm:goodcount.

La prueba C1 contiene una estimación de fase estacionaria cuyo exponente está señalado como pendiente de cotejo con la fuente original. Las consecuencias para zeta, pi y M deben distinguir las identidades exactas de Perron de las aproximaciones que necesitan uniformidad y derivación justificada.

RESULTADO: se conserva la desigualdad de conteo corrigiendo la prueba; se afina el umbral del 41,73%; se retira la afirmación de que v14 tiene una barrera 0.494 demostrada.

No se creó otra versión del manuscrito ni se modificó GitHub al redactar esta respuesta; el presente archivo se archiva por la orden posterior «sube git».
