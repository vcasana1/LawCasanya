# v20: qué queda publicable y qué no

Nota de Claude, 25-oct-2026. Lectura de `CasanyaLawI_v20.tex` (5485 líneas; diff con v19: nueva §"Fixed-cutoff Newton geometry and the weighted sawtooth target", l. 4684–5197, remark sobre GLSS/GM78, corrección 41.72/0.1457, bibliografía con GLSS, GM78, Baluyot et al., Baker–Wüstholz). Sin ejecuciones numéricas.

## 0. Dos cosas de v20 que hay que reconocer

1. **Corrección a mi nota del Newton completo.** $S_X$ lleva todas las potencias $m\ge1$, así que $S_X^2S_X''$ **no** es un polinomio trigonométrico finito sino una serie casi periódica con frecuencias $\sum_pj_p\log p$ que pueden acumularse en 0. v20 lo repara bien: coeficientes con decaimiento exponencial (analiticidad en la poli-banda) + cota de Baker–Wüstholz para formas lineales en logaritmos ⇒ primitiva acotada (Lema `v20FourierPrimitive`). Mi prueba vale tal cual si se trunca $S_X$ en $m\le m_0$ (polinomio finito) y se trata la cola $m>m_0$ como $O_X(2^{-m_0/2})$ en norma uniforme con derivadas; con todas las potencias hace falta el paso de v20. Acepto la corrección.
2. v20 deja $J^{\rm root}_X<\infty$ como hipótesis (`cor:v20ConditionalJTransfer`) en vez de usar mi Teorema A; es conservador y correcto. La lista de un paso con $\Lambda$ queda sin sentencia; mi argumento de divergencia sigue valiendo (una función casi periódica no nula está acotada inferiormente en un conjunto de densidad positiva), pero v20 prefiere no afirmarlo. Bien.

## 1. Lo publicable, por orden de valor

**(A) Núcleo analítico incondicional: el reloj corregido y sus primos.** Un artículo, JNT/Acta Arith., con:
- Thm main de v14 / `thm:primedefect` (segundo momento uniforme del defecto, $c\le\tfrac12$);
- la ley de energía de transporte $\frac1{2\pi^2}\log\log\log T$ (v8–v12), **si** se certifican las reparaciones de v10 a las cinco lagunas de v9 (yo no lo he hecho sobre el texto);
- casi ortogonalidad en norma de operador de las fases de potencias de primo en el reloj, $b<1$ (v12 §16; verificada);
- Teorema C1, primera resonancia de productos con bordes (v15; verificada);
- Teorema A de transición (zeta sintética $=\varpi\mathscr E_X(1+w)(1+\mathcal E)$) como realización analítica del modelo $P_X+\chi\overline{P_X}$ de Gonek, con el Newton completo y Baker–Wüstholz como complemento.
Es nuevo, es incondicional y nadie lo bate "en dos pasos" porque no es un número sino un objeto.

**(B) Nota corta: criterio de defecto ordinal.** Teorema de bloques con $F$ arbitraria ($B_T\le4\sum u_k(F)^2$), descomposición exacta $\mathsf A_T(F)+\mathsf V_T$, identidad integral con el $\tfrac1{12}$, corolario de extremos desplazados ($c\le\tfrac53$), y la reducción de las seis piezas a dos respuestas en las ordenadas. Citando GLSS (horizontal multiplicity) y GM78 como antecedentes, y diciendo que lo nuevo es sustituir PCC/HMH por un segundo momento de un reloj de primos. Elemental, honesto, útil: 8–10 páginas. Riesgo: un referee diga "es GLSS con otra notación"; la defensa es la función $F$ y el $\tfrac1{12}$ exacto.

**(C) Matemática experimental.** La ley de respuesta $1-\Phi(\theta)$ con las tablas, zCasanya y los RMS por corte. Como conjetura con datos, en una revista de experimentación (Exp. Math.) o como sección de (A).

## 2. Lo que no debe ir, o solo como observación de una página

- Toda la vía M: Perron con Euler finito, `prop:v20AllxM`, `cor:v20DiagonalRH`, los "tres objetivos de transferencia". Son implicaciones triviales o vacías (el propio v20 lo dice en cada enunciado). Una observación de media página basta: "a $X$ fijo el Mertens sintético es $\varpi^{-1}M^*_X+O_X(x^{1/2+\varepsilon})$ y esto no informa sobre $M$".
- Las secciones "what is not implied", contraejemplos y refutaciones (§17 de v12): son actas de la discusión, no matemáticas para un lector; reducir a observaciones breves donde haga falta.
- La fase amortiguada con $c(t)\to\infty$ y sus derivadas: definiciones sin ningún teorema. Fuera.
- Los certificados geométricos (hueco mínimo, partición de colisiones): computables pero sin cota de entrada; una observación en (B) como mucho.

## 3. Forma

v20 tiene 5485 líneas y unas 18 referencias, 8 con DOI. Tal como está es un diario, no un artículo: un referee no lo lee. Hay que partirlo en (A) y (B), con la mitad de la longitud actual en total, y completar DOI y la configuración de hiperenlaces del autor.
