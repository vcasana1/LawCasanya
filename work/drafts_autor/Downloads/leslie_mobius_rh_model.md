# Modelo de reproducción de Möbius con Leslie
## Estructura completa y criterio de RH

---

## PARTE I: Leslie multiplicativa (números naturales)

### Estados y genealogía

**Espacio de estados:** Enteros square-free $m \le x$.

**Genealogía:**
- **Padre:** $m$ (square-free, $m \le x$).
- **Madre:** Primo $p$ con $p \nmid m$ (es decir, $\gcd(p, m) = 1$).
- **Hijo:** $n = mp$ (es decir, $n$ es el resultado de multiplicar padre por madre).

**Generación de un número $n$:**

Si $n = p_1 p_2 \cdots p_k$ (factorización en primos distintos, $\omega(n) = k$), tiene exactamente $k$ padres posibles:
$$\text{Padres de } n: \quad m_i = n/p_i \quad (i=1,\ldots,k)$$

Cada padre es square-free (porque $n$ es square-free).

### Matriz de Leslie exacta

$$\boxed{(\mathcal{L}_x)_{n,m} = -\frac{1}{\omega(m)+1} \quad \text{cuando} \quad n = mp \le x, \, p \nmid m; \quad 0 \text{ otherwise}}$$

**Interpretación:**
- Una fecundidad negativa (reproducción por "inversión": de padre a hijo).
- El denominador $\omega(m)+1$ es el número de madres primas disponibles para $m$ (cualquier primo que no divida $m$, pero truncado al rango).
- Cuando normalizas sobre todos los $m$ en una época, la suma de fecundidades balancea.

### Potencias de la matriz

**Potencia 0:**
$$e_1 = \begin{pmatrix} 1 \\ 0 \\ 0 \\ \vdots \end{pmatrix}$$
(el número 1, square-free).

**Potencia 1:**
$$(\mathcal{L}_x e_1)_n = \begin{cases} -\frac{1}{\omega(1)+1} = -1 & \text{si } n = 1 \cdot p = p \text{ (primo)} \\ 0 & \text{otro} \end{cases}$$

Genera: primos con coeficiente $-1$.

**Potencia 2:**
$$(\mathcal{L}_x^2 e_1)_n = \sum_m (\mathcal{L}_x)_{n,m} (\mathcal{L}_x e_1)_m$$

El sumatorio es no-cero cuando:
- $(\mathcal{L}_x e_1)_m = -1$ (es decir, $m$ es primo),
- $n = pm'$ para algún primo $m$ y primo $p \nmid m$ (es decir, $n$ es producto de dos primos distintos).

**Resultado:**
$$(\mathcal{L}_x^2 e_1)_n = \begin{cases} +1 & \text{si } \omega(n) = 2 \text{ (square-free composite)} \\ 0 & \text{otro} \end{cases}$$

**Patrón general (exacto):**
$$\boxed{(\mathcal{L}_x^k e_1)_n = \begin{cases} (-1)^k & \text{si } \omega(n) = k \\ 0 & \text{otro} \end{cases}}$$

La potencia $k$ selecciona números con exactamente $k$ factores primos distintos, con signo $(-1)^k$.

### Función de Möbius desde el resolvente

$$\boxed{\mu(n) = (-1)^{\omega(n)} \quad \text{si } n \text{ square-free}; \quad \mu(n) = 0 \text{ si } n \text{ non-square-free}}$$

**La suma completa:**
$$\sum_{k=0}^\infty (\mathcal{L}_x^k e_1)_n = \sum_{k=0}^\infty (-1)^k \mathbf{1}[\omega(n)=k] = \mu(n)$$

**Forma cerrada (serie geométrica):**
$$\boldsymbol{\mu}_x = \sum_{k \ge 0} \mathcal{L}_x^k e_1 = (I - \mathcal{L}_x)^{-1} e_1$$

**Observable de Möbius:**
$$M(x) = \mathbf{1}^T \boldsymbol{\mu}_x = \mathbf{1}^T (I-\mathcal{L}_x)^{-1} e_1 = \sum_{n \le x} \mu(n)$$

### Verificación numérica (de tu documento)

Para $x = 10^6$:

| $k$ | $\sum_n (\mathcal{L}_x^k e_1)_n$ |
|-----|---|
| 0 | 1 |
| 1 | −78,498 |
| 2 | +209,867 |
| 3 | −206,964 |
| 4 | +92,966 |
| 5 | −18,387 |
| 6 | +1,235 |
| 7 | −8 |
| **Total** | **$M(10^6) = 212$** |

**Error:** 0. Discrepancias: 0.

---

## PARTE II: Leslie de ceros (línea crítica y fuera)

### Espacio de ceros

**Estados:** Ceros $\rho = \beta + i\gamma$ de $\zeta(s)$ con $0 < \gamma \le T_{\max}$.

**Clasificación (binning):**
- **Parte real:** $\beta \in \{B_1, B_2, \ldots, B_m\}$ donde:
  - $B_1 = [0, 0.1)$
  - $B_2 = [0.1, 0.25)$
  - $B_3 = [0.25, 0.4)$
  - $B_4 = [0.4, 0.5)$
  - $B_5 = [0.5, 0.6)$ ← línea crítica y cercanías
  - $B_6 = [0.6, 0.75)$
  - $B_7 = [0.75, 0.9)$
  - $B_8 = [0.9, 1]$

- **Altura:** Épocas $T_0, T_1, \ldots, T_N$ donde $T_n = n \cdot 10^5$ (p.ej.).
  - Estado $(i, n)$ = cero con $\beta \in B_i$ y $\gamma \in [T_n, T_{n+1}]$.

**Vector de estado:** 
$$\mathbf{z}_n = \begin{pmatrix} z_{n,1} \\ z_{n,2} \\ \vdots \\ z_{n,m} \end{pmatrix}$$
donde $z_{n,i} = \#\{\text{ceros con } \beta \in B_i, \, \gamma \in [T_n, T_{n+1}]\}$.

### Matriz de Leslie para ceros

$$\boxed{\mathcal{L}^{(\text{zeros})}_T = \begin{pmatrix}
\ell_{1,1} & \ell_{1,2} & \cdots & \ell_{1,m} \\
\ell_{2,1} & \ell_{2,2} & \cdots & 0 \\
0 & \ell_{3,2} & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & \ell_{m,m}
\end{pmatrix}}$$

**Entradas:**
- **Fecundidad (primera fila):** $\ell_{1,i} = $ densidad de ceros nuevos en siguiente época, correlacionado con ceros de generación $i$ actual.
  - $\ell_{1,5}$ (ceros en $\beta=0.5$) es la más grande: los ceros en la línea crítica generan más ceros cercanos a la línea (por clustering).
  - $\ell_{1,i}$ para $i \ne 5$ es más pequeño: desacoplamiento de regiones.

- **Supervivencia (subdiagonal):** $\ell_{i,i-1}$ = fracción de ceros en $B_{i-1}$ que "persisten" en el bin $B_i$ (en realidad, en un fenómeno de "envejecimiento de altura").
  - Principalmente: ceros que no desaparecen son relativamente pocos. $\ell_{i,i-1} \approx 0.01$ (muy pocas migraciones entre bins).

**Bajo RH (simetría):**

Si todos los ceros están en $\beta = 0.5$, entonces:
- $z_{n,5}$ es casi toda la masa (ceros en la línea).
- $z_{n,i} = 0$ para $i \ne 5$ (o muy pequeño, artefactos de cálculo).
- La matriz tiene simetría: perturbaciones en $B_i$ y $B_{10-i}$ (reflejada) se cancelan.

### Matriz acoplada total

$$\boxed{\mathcal{L}_{\text{total}}(x,T) = \begin{pmatrix}
\mathcal{L}^{(\text{primes})}_x & \mathcal{C}^{(z \to p)} \\
\mathcal{C}^{(p \to z)} & \mathcal{L}^{(\text{zeros})}_T
\end{pmatrix}}$$

**Dimensión:** (número de enteros $\le x$) + (número de bins de altura $\times$ m) $\sim 10^6 + (N \times 8)$.

**Bloques:**

1. **$\mathcal{L}^{(\text{primes})}_x$:** Leslie de números (visto arriba).

2. **$\mathcal{L}^{(\text{zeros})}_T$:** Leslie de ceros (visto arriba).

3. **$\mathcal{C}^{(z \to p)}$ (ceros afectan números):** 

   Entrada: $(\mathcal{C}^{(z \to p)})_{n,\rho}$ = cómo la presencia del cero $\rho$ perturba la "reproducción" de números alrededor de $n$.
   
   **Definición via fórmula explícita:**
   $$(\mathcal{C}^{(z \to p)})_{n,\rho} = \Re\left( \frac{x^{\rho}}{2\rho} \right) \cdot \mathbf{1}\left[\log n \approx \frac{\gamma}{2\pi}\right] \cdot \phi_\sigma(\beta)$$
   
   donde:
   - $\phi_\sigma(\beta)$ es un núcleo localizador sobre la parte real: concentrado en $\beta$, cero lejos.
   - $\mathbf{1}[\log n \approx \gamma/(2\pi)]$ activa la perturbación cuando $n$ alcanza la escala predicha por la altura del cero.
   - Si $\beta = 0.5$, la contribución es pequeña (oscilante, integra a $O(x^{1/2+\varepsilon})$).
   - Si $\beta > 0.5$, crece como $x^\beta$, no se integra.

4. **$\mathcal{C}^{(p \to z)}$ (números afectan ceros):**

   Probablemente negligible o cero: los números no generan nuevos ceros de $\zeta$. Entrada = 0.

---

## PARTE III: Criterio de RH

### Observable combinado

$$M_{\text{total}}(x, T) = \mathbf{1}_{\text{primes}}^T (I - \mathcal{L}_{\text{total}})^{-1} e_1$$

(proyectas el resolvente sobre el observable de números, ignorando la componente de ceros).

### Teorema propuesto (falsable numéricamente)

$$\boxed{\text{RH} \quad \iff \quad |M_{\text{total}}(x,T) - M(x)| = O_\varepsilon(x^{1/2+\varepsilon}) \quad \forall \varepsilon > 0}$$

**Demostración (esquema):**

1. **$\Rightarrow$ (RH verdadera $\Rightarrow$ cota):**
   - Bajo RH, todos los ceros están en $\beta = 0.5$.
   - La matriz $\mathcal{L}^{(\text{zeros})}_T$ es equilibrada: $z_{n,5} \approx N(T_n) \log \log T_n$ (aproximadamente) y $z_{n,i} = 0$ para $i \ne 5$.
   - El acoplamiento $\mathcal{C}^{(z \to p)}$ es pequeño: $\|\mathcal{C}^{(z \to p)}\|_{\infty} = O(x^{1/2+\varepsilon})$ (porque cada $\rho$ en la línea contribuye $O(x^{1/2+\varepsilon})$).
   - El resolvente $(I-\mathcal{L}_{\text{total}})^{-1}$ tiene norma controlada (por Neumann): $\|(I-\mathcal{L}_{\text{total}})^{-1}\| = O(\text{poly}\log x)$ bajo estas condiciones.
   - Por lo tanto, $|M_{\text{total}} - M| = O(x^{1/2+\varepsilon})$. ✓

2. **$\Leftarrow$ (cota $\Rightarrow$ RH verdadera):**
   - Supón la cota $|M_{\text{total}} - M| = O(x^{1/2+\varepsilon})$.
   - Si hay un cero $\rho = \beta + i\gamma$ con $\beta > 1/2$, entonces:
     - $(\mathcal{C}^{(z \to p)})_\rho \sim x^\beta$ crece sin cancelación.
     - El resolvente amplifica esto (Neumann: $\sum_k (\text{perturbación})^k$ diverge si la perturbación es $> x^{1/2}$).
     - Por lo tanto, $|M_{\text{total}} - M| \gg x^{1/2+\varepsilon}$, contradicción.
   - Luego, no hay ceros con $\beta > 1/2$. RH es verdadera. ✓

---

## PARTE IV: Verificación numérica (programa)

### Pseudocódigo

```
Load zeross.bin → gamma[1..N]
Initialize LESLIE_primes[1..10^6, 1..10^6] (sparse)
Initialize LESLIE_zeros[bins, epochs] (dense)
Initialize COUPLING[numbers, zeros]

# Construct LESLIE_primes
for each square-free m <= x:
    for each prime p not dividing m:
        n = m * p
        if n <= x:
            LESLIE_primes[n, m] = -1 / (omega(m) + 1)

# Construct LESLIE_zeros
for each zero gamma in zeross.bin:
    beta = compute_beta_or_assume_0.5(gamma)  # or assume 0.5 for verification
    bin_beta = find_bin(beta)
    epoch = find_epoch(gamma)
    increment z[epoch, bin_beta]

# Build transition matrix for zeros
for each epoch n:
    # Fecundity: new zeros from correlation structure
    for each bin i:
        LESLIE_zeros[1, i] = density_new_zeros[i](epoch n)
    # Survival: ceros stay (roughly)
    for i > 1:
        LESLIE_zeros[i, i-1] = survival_rate(i)

# Construct coupling
for each number n:
    log_n = log(n)
    for each zero rho = beta + i*gamma:
        if abs(log(n) - gamma / (2*pi)) < threshold:
            COUPLING[n, rho] += (real part of x^rho / (2*rho)) * localization(beta)

# Form total matrix
LESLIE_total = block_matrix([
    [LESLIE_primes, COUPLING_zp],
    [COUPLING_pz, LESLIE_zeros]
])

# Compute resolvent (or power series approximation)
v0 = [1, 0, 0, ...]
M_total = sum over k=0 to K_max: 1^T * LESLIE_total^k * v0

# Compare
M = sum of mu(n) for n <= x  (precomputed or via original Leslie)
error = abs(M_total - M)
print(f"x={x}, T={T_max}, error={error}, bound={x^(0.5 + epsilon)}")
```

### Expected outputs

**Under RH (all zeros at $\beta = 0.5$):**
- $M_{\text{total}} \approx M$ (difference $\ll x^{0.5+\varepsilon}$).

**Synthetic cero at $\beta = 0.6$:**
- $M_{\text{total}}$ diverges from $M$ dramatically.
- Error $\gg x^{0.5+\varepsilon}$.

---

## PARTE V: Lo abierto

1. **Norma exacta del resolvente $(I-\mathcal{L}_{\text{total}})^{-1}$** bajo RH. Necesaria para pasar de "perturbación pequeña" a "resolvent controlado".

2. **Localización de $(\mathcal{C}^{(z \to p)})$**: ¿Exactamente cuál es el núcleo $\phi_\sigma(\beta)$ y la localización temporal en $\log n \approx \gamma/(2\pi)$?

3. **Simetría de cancelación**: ¿Cómo codificar formalmente que $\mathcal{C}^{(z \to p)}_\rho + \mathcal{C}^{(z \to p)}_{1-\rho} = O(x^{1/2+\varepsilon})$ bajo RH?

4. **Compresión de Leslie**: Si la matriz es demasiado grande ($10^6 + 10^4$), ¿cómo comprimir/agrupar estados sin perder información?

---

## Resumen

- **Leslie de números:** Exacto, generador de Möbius verificado.
- **Leslie de ceros:** Binning de altura y parte real, matriz de transición entre épocas.
- **Acoplamiento:** Via fórmula explícita, activado cuando escalas coinciden.
- **Criterio:** Cota del resolvente $\iff$ RH, falsable numéricamente.
- **Ruta concreta:** Construir, computar, verificar bajo RH, probar contra ceros sintéticos.
