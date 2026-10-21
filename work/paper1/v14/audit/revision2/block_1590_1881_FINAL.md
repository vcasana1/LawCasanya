# Revisión 2, bloque 1590–1881 (informe final)
Sin lagunas. Pendientes:
1. l.1794: "$C'$ absolute since $H_j\ge H^*\ge1$" -> "$C'=K+1$ absolute whenever $H_j\ge1$, which holds for $j<m^*$ because $H_j\ge H^*$ and $H^*\ge1$ is imposed independently of $C$".
2. l.1798 "Then, for all $j\ge1$ and $r\ge1$," -> "Then, for $1\le j\le m^*$ and $r\ge1$,"; l.1769 "$\log H_{j-1}\le H_j$ for all $j$" -> "for all $j$ with $H_{j-1}\ge1$".
3. l.1773 tras "iterated logarithm.": añadir prueba de m^*=log^*T+O(1) (a=2log(1/C_⋆), K=a+1, H_j≤(9/8)log^{(j)}H_0+K mientras log^{(j-1)}H_0≥K; luego O(1) pasos por H_{j-1}≥4H_j; H_j≥log^{(j)}H_0).
4. l.1716: "case $r=2$ of the third bound" -> "case $r=4$" (||g_2||_16 necesita 4r=16).
5. l.1646 sampling_rho: ||F'||_2 ≤ 12r(1+log X)(C√r(1+log X))^{4r}T^{1/2}; 17 -> 49.
6. l.1662 second_step: tras "with $r=2$" añadir "(admissible: $c_1=H_0^{-1/2}\le\frac1{320}$ and $4\le\kappa_{\rm F}\log T$ for $T\ge T_0$)".
7. l.1792 base: "with $X=2$ (admissible, since $2r\le\kappa_{\rm F}\log T$ gives $2\le T^{1/(160r)}$)".
8. second_identity: c_0:=0 (j=1, y^{(0)}=0, r_{1,k}=0); tercer término (L(τ)/L(x))χ'' ≤ (1+o(1))y²/(4π(T−T^{1/2})); "for $k$ with $\tau_k\ge T-1$".
9. l.1816 H^*≥max(4C_6,160^2·4) -> max(4C_6,160^2).
10. multiplicity: "for almost every $t$"; eq:SX_derivative en [T−1,2T+1] cubriendo con [T−1,2T−1],[T+1,2T+1]; punto final de display; l.1630 "pairs $(j,k)$" -> "$(k,l)$".
11. l.1738 zero_pairs Hölder: T^{1/4} -> (T+1)^{1/4}.
Comprobado correcto: localización, one-step, inducción r^{3/4}, cutoff law, orden de constantes, zero_pairs, deformation, sorted_clock (BW_pointwise para todo k), tower remark.
