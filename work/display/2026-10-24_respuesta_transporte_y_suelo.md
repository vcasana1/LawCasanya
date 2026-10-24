Subido. Primero una corrección: el "suelo lineal 0.039" de la nota anterior era incorrecto. Daba por buena una constante de $\langle s_k^2\rangle$ que no está demostrada. Lo he retirado en la nota y en el LOG.

**Respuesta del transporte en los primos móviles** (nota `2026-10-24_respuesta_transporte_y_suelo.md`):
- **Modelo de fases independientes:** la respuesta es exactamente 0. El transporte depende solo de los primos usados y no puede responder a un primo móvil que no usa.
- **Determinista, grados bajos de la expansión de Bessel:** también tiende a 0 si $\tfrac32\theta+D_*c_1<1$. La razón es que $p\nmid nA$, así que no hay resonancia exacta, y el aliasing del reloj exige productos de tamaño $\gtrsim T$. Está esbozado; falta escribir la masa $\ell^1$.
- **Grados altos:** abierto. El factor $\sqrt p$ inutiliza las cotas $\ell^2$.
- **Tu Tabla 9 en el rango limpio:** $|\mathcal B|\le0.08$ frente a $R^\tau\approx0.8$. La respuesta de los primos móviles la lleva el residual, no el transporte.

**Predicción del suelo de error.** Con tu ley en los primos no usados y peso 1 en los usados:

$$\mathcal E_{\rm res}(c_{\max})\approx\frac1{2\pi^2}\Bigl[\int_0^{c_{\max}}\frac{\Phi^2}{\theta}\,d\theta+\int_{c_{\max}}^{1}\frac{(1-\Phi)^2}{\theta}\,d\theta\Bigr].$$

Para zCasanya, con corte final 512 a $\tau\sim10^6$, es decir $c_{\max}\approx0.52$:
- predicción: $0.0064$–$0.0078$;
- tu RMS publicado de $0.0440$, pasado a unidades de ceros: $0.0057$–$0.0072$ según la altura;
- tu nota de pendientes registra $\approx0.006$.

Concuerda entre un 10 y un 20 % sin ajustar nada. Es una comprobación independiente de tu ley. Además deshace el misterio de la "anticorrelación no explicada": el $0.006$ no estaba por debajo de ningún suelo real; el suelo de $0.047$ era un error del modelo $W_j$.

**Consecuencias:**
1. La construcción óptima sin ceros sería un solo paso con todos los primos $p\le\tau/2\pi$ y pesos $1-\Phi(\theta_p)$, un filtro de Wiener con tu ley como función de transferencia. Su error sería solo el contenido $\theta>1$, que es lo que miden tus cortes $c\ge1$ (RMS 0.0212, 0.0164, 0.0128).
2. Para la prueba sin RH, todo se reduce a un solo ingrediente: tu ley en los **puntos del reloj**, $R^\tau_p=1-\Phi(\theta)$.

¿Ejecuto el contraste de (2.1) ventana a ventana con tus salidas? Sería con un programa nuevo en `work/`, sin tocar el conjunto de test.
