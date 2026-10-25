# Auditoría completa de CasanyaLawI_v15 (chatgpt/manuscripts, commits 5717e64 y 61849d7)

Nota de Claude, 25-oct-2026. Lectura completa del material nuevo y comparación línea a línea con v12 y v13. No he compilado: falta `lmodern.sty` en el contenedor. Las referencias cruzadas sí están comprobadas: todas resuelven y no hay etiquetas duplicadas. Sin ejecuciones numéricas.

## 0. Estructura

- **Líneas 1–3371:** idénticas a v12, salvo el título y el abstract. El cuerpo de v12 (§§1–17, con las siete refutaciones de §17) se hereda sin cambios.
- **Líneas 3372–4485:** material nuevo, unas 1110 líneas en seis secciones: C1; completado sintético y canales de alias; certificados de multiplicidad; transportes de Perron con Euler finito; tres objetivos de transferencia; conclusiones.
- **v13:** queda superado. Lo único que v15 no conserva de v13 es la redacción de sus conclusiones, que se reescriben.

## 1. §C1, resonancia de productos (Thm `thm:C1`): correcta y completa

He comprobado:
- **Poisson (Lema `C1Poisson`).** Titchmarsh, Lema 4.7, con un único alias $\nu=1$, porque $F_u'=1+O(1/L)$ en $[N/2,8\pi N]$.
- **Datos de la fase.** $\varphi_n(x_n)=2\pi n-\tfrac{11\pi}4$, con $x_n=n(\log n-1)+\tfrac{11}8$; $\varphi''=-2\pi/(n\log^2n)$; $|\varphi'''|\asymp(T^2L^3)^{-1}$.
- **Taylor en $|x-x_n|\le H=T^{3/5}L$.** Cuesta $H^4/(T^2L^3)=T^{2/5}L$. Las colas gaussianas y las reales cuestan $1/(\lambda H)=T^{2/5}L$.
- **Pares de borde.** Son $O(T^{3/5})$ y aportan $O(T^{-2/5})$. Los interiores aportan $O(T^{-1/10}L^{C-1})$; los exteriores, $O(T^{-1/2}\log T)$.
- **Conteo.** $\int_{1-c}^c du/(u(1-u))=2\log\frac c{1-c}$.

**Esto cierra el punto que yo había dejado pendiente:** el exponente del error de tercera derivada queda resuelto con un Taylor explícito.

## 2. §Completado sintético y alias: correcto

- **Prop. `xiSynthetic`.** Correcta: $\Xi_\kappa(1)=\tfrac12$, residuo 1 en $s=1$, ecuación funcional completada. La hipótesis $\kappa_k-\tau_k=O(\tau_k^{\sigma_0})$ se cumple con corte variable: $|S_X|\le\sqrt X$ da $\sigma_0=c/2$.
- **Thm `synthetictransport`.** Identidad correcta (diferencia de $2z\sum(z^2+h_k^2)^{-1}$).
- **Prop. `notanalytic`.** Correcta: un corte que depende de la altura no es holomorfo.
- **Prop. `reciprocalgap`.** Correcta: $f=e^{-\sqrt{s+1}}$, con $|1/f|=e^{(1+o(1))\sqrt{|t|/2}}$.
- **Lema `higheraliases`.** Correcto:
  $$\varphi(x_\nu)=2\pi\nu v-\tfrac{11\pi\nu}4,\qquad \text{amplitud }\sqrt{v/\nu}\,\log v .$$
- **Cor. `resonancechannels`.** Correcto.
  - Alias de cociente: $-\log(p/q)\,e^{2\pi ip/q}/q$ (con pesos), que exige $p>Nq$.
  - Alias de producto: $\frac{(pq)^{1/4}}{\sqrt2}\log\sqrt{pq}\,e^{i(4\pi\sqrt{pq}-23\pi/4)}$, que exige $pq\in(N^2,4N^2)$.

  **Es el contenido de investigación más importante de v15:** concreta los dos términos aritméticos del régimen $c\ge1$, que es el objeto pendiente en la vía M y en $E_T\to0$.
- **Lema `phaseamplification`.** Correcto.

## 3. §Certificados de multiplicidad: correcto

- **Thm `blockcount`.** Correcto, ya con la corrección $B_T\le\sum$ (no $=$).
- **Cor. `thresholds`.** Umbrales correctos: 0.145675; 0.0125 para el 95 %; 0.0025 para el 99 %; suma no normalizada $<\tfrac12$ para que no haya bloques.
- **Thm `blockmoments`.** Correcto, por Jensen: $(1/r)\sum(u+j)^2\ge(r^2-1)/12\ge\tfrac14$. El factor $4^m$ es óptimo.
- **Prop. `mingapcertificate`.** Correcta: $\sum_{i<j}(j-i)^2=r^2(r^2-1)/12$. Usa monotonía, que se sigue de que los huecos son $\ge h_T>0$.
- **Prop. `smallgapcertificate`.** Correcta, sin monotonía.
- **Thm `collisionpartition`.** Correcto. Es nuevo y útil: un certificado computable solo con los $\kappa_k$, por programación dinámica.

## 4. §Perron con Euler finito y §objetivos: correctos como implicaciones

- **Thm `Eulerarith`.** Exacto.
- **Thm `PerronMfixed` y `PerronPsifixed`.** Correctos con sus hipótesis: $J_X<\infty$ y $M_{C,X}$ definida sobre la recta $\sigma$.
- **Cor. `bothtransfersRH`, Props. `piRHtarget`, `MRHtarget` y `zetaRHtarget`.** Correctos.

**Corrección a mi propia nota de la vía M (§0).** Allí escribí que la uniformidad en $X$ "equivale literalmente" a $M\ll x^{1/2+\varepsilon}$. Lo correcto es "implica"; v15 lo formula bien, como condición suficiente.

## 5. Defectos de redacción que hay que corregir en la próxima versión

1. **Incoherencia interna.** La subsección heredada de v12 "Endpoint phase stationary points and **unproved** scalar asymptotics" y su observación final, que dice que la fórmula de Cr "must be treated as unverified", contradicen el Thm `thm:C1`. Hay que cambiar el título y remitir a `thm:C1`.
2. **`thm:goodcount` ($1-4d_T$, lista y huecos) frente a `thm:blockcount` ($1-4E_T$, función).** El segundo supera al primero, y falta la referencia cruzada.
3. **Bibliografía.**
   - Faltan DOI en Carleson 1966, Hunt 1968, Kinnunen 1997 y Fujii 1981; Selberg 1946, Stein 1970 y Titchmarsh 1986 no los tienen o no son fáciles de encontrar. **Hay que verificarlos; no los añado de memoria.**
   - No hay backrefs a páginas ni tooltips de previsualización. La configuración canónica del autor (la de excursion_area_section_v39) los exige.
4. **Material de Claude que no está incorporado y que encaja como lemas.**
   - La descomposición exacta $\sum u^2=\sum_\gamma m_\gamma(N^*-F)^2+\sum_\gamma m_\gamma(m_\gamma^2-1)/12$. Da `blockcount` en una línea y separa lo que controla $F$ de lo que no.
   - La forma integral L′ y la equivalencia $E_T\to0\iff\frac1M\int(N-F)^2dF\to\frac1{12}$.

## 6. Conclusiones

- **v15 no contiene ningún error matemático en el material nuevo.** No hay ninguna afirmación de RH ni de porcentaje no demostrada; el estado declarado es correcto.
- **Lo que se gana sobre v12:**
  - C1 queda demostrado del todo;
  - certificados de multiplicidad que no necesitan monotonía y son computables sin ceros;
  - el completado sintético canónico;
  - los dos canales de alias en $c\ge1$, explícitos.
- **Los tres caminos a RH siguen dependiendo de lo mismo:**
  - control uniforme del defecto, o de su cola (ordenadas);
  - compatibilidad analítica uniforme en $X\ge x$ (para $\pi$ y $M$).

  El primer objeto concreto que hay que sumar son los dos canales de alias de `cor:resonancechannels`. Con eso está escrito, por fin, el paso más allá de la resonancia.
