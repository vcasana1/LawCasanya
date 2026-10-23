# Pendiente para la siguiente versión de Paper I — universalidad de la energía del transporte

Estado: anotado el 2026-10-23. No crear versión hasta que Doktor lo ordene. Las demostraciones completas están en `work/notes/2026-10-23_transporte_rouche_turing_c_mayor_un_medio.md` (§7.6–7.10), y cada paso se ha verificado contra enunciados de la v14. Al redactar hay que revisar las hipótesis de uniformidad (rango de $c$, $T\ge T_0$) del teorema B, del lema de transporte y de la ortogonalidad del reloj.

Propuesta del texto 07 (`work/display/2026-10-23_aportes_externos_transporte/07_…`): un teorema nuevo en Paper I, de 3–5 páginas. Se reservaría un artículo propio para cuando se tenga la cota inferior.

## Enunciados (para $X=T^c$, $B_c(T)=\langle\mathfrak t_k(T^c)^2\rangle_{\mathcal I_T}$)

1. **Universalidad.** Para $0<a<b\le\frac12$ fijos, $\bigl|\sqrt{B_b(T)}-\sqrt{B_a(T)}\bigr|=O_{a,b}(1)$. Por tanto $B_a-B_b=O_{a,b}(\sqrt{\log\log\log T})$: todos los exponentes fijos tienen los mismos $\liminf$ y $\limsup$ de $B_c/\log\log\log T$, y la pregunta `q:fixed_c` tiene la misma respuesta para todo $c$.
2. **Cota superior explícita.** $B_c(T)\le\frac1{\pi^2}\log\log\log T+O_c(\sqrt{\log\log\log T})$, que fija la constante implícita de D″.
3. **Fórmula de respuesta.** Con $\omega_T=(\log V_T)^{1/8}$, $\theta_T=\omega_T/\sqrt{V_T}$ y $V_T=\frac{\log\log T}{2\pi^2}$:
$$B_c(T)=\frac1{\pi^2}\sum_{T^{\theta_T}<p\le T^c}\frac{1-\Rt_p}{p}+o(\log\log\log T),$$
   que relaciona el teorema B (defecto) con el teorema C (respuesta $\Rt_p$). Forma equivalente: $B_c=2L(1-\langle W(\gamma),W(\tau)\rangle/L)+o(L)$.
4. **Consecuencias que conviene enunciar.** Si $B_c=O(1)$, entonces $\overline{\mathcal R}_c\to1$; lo contrario no se sigue. Si $B_c\to\infty$, entonces $\langle r^2\rangle\sim B_c$ y la fracción compensada tiende a 0.
5. **Pregunta abierta nueva**, que sustituiría o precisaría a `q:fixed_c`: ¿es $\limsup\overline{\mathcal R}_c(T)<1$? Es decir, ¿se pierde correlación entre $W(\gamma_k)$ y $W(\tau_k)$ en la banda $\theta\ge\omega_T/\sqrt{V_T}$? Una respuesta afirmativa da $\liminf B_c/\log\log\log T>0$. Los segundos momentos solos no lo deciden ($U=\pm V$).
6. **Observación numérica.** La banda solo existe si $\log\log T>2\pi^2\omega_T^2/c^2$; con $c=\frac12$, a partir de $T>e^{e^{79}}$. La compensación de la Tabla 7 está por completo en el régimen previo.

## Atribución
Los textos 05–07 (ChatGPT, aportados por el autor) proponen la reducción (A), la universalidad, la cota explícita y la forma de correlación. Claude añadió la fórmula con $\Rt_p$, la cancelación diagonal con el paso por Mertens corregido, la escala $e^{e^{79}}$ y la verificación término a término.
