# Traspaso a un chat nuevo: demostrar que las tauc son GUE

Nota de Claude, 25-oct-2026. Es el documento de arranque de un chat nuevo. Sin ejecuciones numéricas nuevas. Ningún manuscrito cambiado.

## 0. Reglas del repositorio (resumen; AGENTS.md manda)

- Claude escribe solo en `work/` (no en `work/shared/`, `work/drafts_autor/` ni `chatgpt/`). Los manuscritos del autor los redacta solo ChatGPT.
- Nada en GitHub sin "sube git". "sube git" = todo lo pendiente, más el display, la entrada en `work/LOG.md` (append-only), `git pull --rebase`, prefijo `[claude]` y nunca force-push.
- Sin cálculos numéricos salvo orden expresa. Ninguna construcción usa los $\gamma_k$; solo se leen para evaluar. Conjunto de test intocable: $k=1\,400\,737,\dots,2\,001\,052$.
- Estilo: directo, LaTeX en display, atribuciones en línea, sin párrafos de "procedencia".

## 1. Objeto

**Tauc** = la mejor aproximación sin ceros (AGENTS §5): red de Lambert más primos.
- Etapa A: raíz monótona certificada con $X=16$.
- Continuación hasta $X=(\tau/2\pi)^{c}$, con $c=1.30$.
- Con datos (bloque 3, $c=1.30$): RMS $0.01276$ en $t$ ($\approx0.025$ espaciados), máximo $0.186$, gap1 $0.0396$ y sin inversiones.

Sea $\{t_k\}$ la sucesión tauc, desplegada con $\Lambda(t)=\frac1{2\pi}\log\frac t{2\pi}$. El objetivo es la correlación de pares de $\{t_k\}$:

$$R_2(f;T)=\frac1{M_T}\sum_{\substack{j\ne k\\ T<t_j,t_k\le2T}}f\bigl(\Lambda(T)(t_j-t_k)\bigr)\ \longrightarrow\ \int f(x)\Bigl(1-\Bigl(\frac{\sin\pi x}{\pi x}\Bigr)^2\Bigr)dx,$$

y, en forma de Fourier, el factor de forma $F_{\rm tauc}(\alpha)\to\min(|\alpha|,1)$, más el término $\delta$.

**Ventaja clave:** las tauc son explícitas y no usan ceros. El enunciado "tauc es GUE" no presupone RH.

## 2. Ya demostrado (y dónde está)

- **Teorema de robustez** (`work/notes/2026-10-25_robustez_GUE_tauc_a_gammas.md`). Hipótesis:
  - (H0) finitud local;
  - (H1) emparejamiento tauc–$\gamma$ casi completo: errores $o(M)$, error $\to0$ en densidad, se permiten desplazamientos de etiqueta.

  Conclusión: $R_n(\gamma)-R_n(\text{tauc})\to0$. Versión cuantitativa:
  $$|R_2(f;\gamma)-R_2(f;\text{tauc})|\le2\,\mathrm{Lip}(f)\,C_A\,\langle e^2\rangle^{1/2}.$$
- **Teorema L** (`2026-10-25_via_M_localizacion_uniforme.md`): $|u_k|<\tfrac12$ para todo $k$ alto $\Rightarrow$ RH y ceros simples.
- **Descomposición exacta** (`2026-10-25_ET_a_cero_estado.md` §5):
  $$\sum u^2=\sum_\gamma m_\gamma(N^*-F)^2+\sum_\gamma\frac{m_\gamma(m_\gamma^2-1)}{12}.$$
- **Jerarquía:**

  | Cota sobre el error tauc–$\gamma$ | Da |
  |---|---|
  | $\langle u^2\rangle<\tfrac14$ | proporción positiva |
  | $\langle e^2\rangle\le\varepsilon^2$ | GUE$(\gamma)$ + $O(\varepsilon)$ |
  | $\to0$ en densidad | 100 % simples y críticos |
  | $\sup<\tfrac12$ | RH |

**Por tanto, GUE para las $\gamma$ = (A) tauc es GUE + (B) emparejamiento en media.** Este chat ataca **(A)**, que no involucra ceros.

## 3. Por qué (A) es plausible y abordable

Hay que descartar el modelo de un paso. Linealizado y de banda limitada, da una red perturbada sin repulsión, y **es falso para la tauc real**: con los datos, la fluctuación es casi idéntica a la de $\gamma$. La multietapa no lineal genera $\alpha>1$.

Estructura del factor de forma de tauc:
1. **Parte prima** ($|\alpha|<c$). Los términos $\sum_{p\le X}p^{-1/2}\cos(t\log p)$ dan la contribución diagonal de Montgomery, $|\alpha|$ (Mertens y el TNP). Es incondicional, porque las frecuencias son $\log p$ conocidas.
2. **Pico de Bragg** de la red de Lambert en $\alpha\in\mathbb Z$, amortiguado por $\prod_{p\le X}J_0(2/\sqrt p)\sim C/\log X$ (Mertens; por ahora un modelo).
3. **Canales de alias** (de la no linealidad, desarrollo de Bessel), que pueblan $\alpha>1$:
   - cociente $p/q\in(N,2N)$ con fase $e(p/q)$: primos en progresiones, sumas de Ramanujan y **Bombieri–Vinogradov** para $c<2$;
   - producto $e(2\sqrt{pq})$: Vaughan más van der Corput.

## 4. Plan de demostración propuesto

- **Teorema (a).** $F_{\rm tauc}(\alpha)=|\alpha|+o(1)$ uniformemente para $|\alpha|\le c-\delta$. Incondicional, solo con primos.
  - Pasos: escribir $t_k$ mediante Newton/Lagrange alrededor de la red de Lambert; desarrollar $\sum_k e(\alpha\Lambda t_k)$ por Poisson y Bessel; aislar la diagonal $p=q$.
- **Teorema (b).** Para $1\le|\alpha|\le c$, la suma de los canales de alias tiende a $1$ (la meseta).
  - Pasos: cociente con BV y producto con van der Corput; comprobar la cancelación exacta frente al pico de Bragg.
- **Teorema (c).** Con $c=c(T)\to\infty$, se pasa de (a) y (b) a $F_{\rm tauc}=\min(|\alpha|,1)$ en todo $\alpha$, y de ahí a GUE para $R_2$. Para $R_n$, usar cumulantes y la combinatoria de Rudnick–Sarnak sobre los mismos canales.
- **Obstáculo previsible.** Las sumas sobre primos más allá de $\alpha=2$ requieren distribución de primos en progresiones por encima de BV (Elliott–Halberstam) o sumas bilineales tipo Type I/II. Hay que identificar el $c$ máximo alcanzable incondicionalmente. Ese $c$ fija hasta dónde se demuestra GUE para las tauc.

## 5. Ficheros

- Construcción: `work/v15_prep/` (opc_common, opc_task3, opc_task4) y `data/zLamb.bin`.
- Test de huecos (en marcha, sin subir): `work/gaps_tauc/opc_gaps_build_tauc.py` y `opc_gaps_eval.py`.
  - Bloques $k=1\,380\,001$ ($n=20\,000$) y $k=300\,001$ ($n=40\,000$), con $c=1.30$.
  - Métricas: KS frente a $\gamma$, la pendiente de la CDF de huecos pequeños (GUE da 3) y el surmise.
- Literatura de contexto: Montgomery 1973; Rudnick–Sarnak 1996; Gallagher–Mueller 1978; GLSS 2025; Goldston–Suriajaya arXiv:2511.20059.

## 6. Primera tarea del chat nuevo

Enunciar y demostrar con detalle el **Teorema (a)**:
- definición exacta de $t_k$ (de AGENTS §5);
- la fórmula de $\sum_{T<t_k\le2T}e(\alpha\Lambda t_k)$;
- la extracción de la diagonal con el error explícito.

Después, el Teorema (b) con Bombieri–Vinogradov.

## 7. Resultado del test de huecos (25-oct; c = 1.30; 60 000 huecos; work/gaps_tauc/outputs/gaps_eval.txt)

- Global: varianza de huecos γ 0.167, tauc 0.172 (surmise GUE 0.178); RMS(s_tauc − s_γ) = 0.039; KS(γ, tauc) = 0.035, significativo (crítico al 5 %: 0.008).
- **Suelo duro:** ningún hueco de tauc por debajo de 0.17. Los 25 huecos verdaderos más pequeños (0.029–0.071) pasan todos a 0.17–0.22. La pendiente log-log de la CDF en [0.05, 0.3] es γ 2.79 frente a tauc 11.8 (GUE da 3).
- **Explicación (T, elemental):** si F es C¹ con F′ ≤ A·Λ en el bloque, entonces todos los huecos desplegados de la tauc cumplen s ≥ 1/A. Con c fijo, F tiene banda limitada (frecuencias log p ≤ c log(t/2π)) y F′/Λ queda acotado, así que el suelo es positivo. Los huecos pequeños de γ corresponden a α grande, fuera de la banda.
- **Consecuencia para el plan:** con c fijo la tauc **no** es GUE en la cola de huecos pequeños; coincide con γ en la escala de varianza, no en la de repulsión. El Teorema (c), c(T) → ∞, es imprescindible, y hay que cuantificar el suelo 1/sup(F′/Λ) como función de c. Para el emparejamiento (B), los pares cercanos de γ son exactamente donde la tauc falla (error ≈ 0.10 en huecos < 0.15, frente a 0.039 global).
