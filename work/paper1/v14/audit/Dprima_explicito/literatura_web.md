# Literatura web: versiones explícitas incondicionales de I1–I6 (búsqueda 2026-10-21)

## Hallazgo 1 — Inoue–Kobayashi–Toma, arXiv:2510.14309 (2025) "Explicit extreme values of the argument of the Riemann zeta-function"
- Leído (HTML v1). Teoremas principales bajo RH (CONDICIONAL). Constantes C, c no numéricas. NO da versión explícita de la aproximación de Selberg, ni momentos de S(t), ni densidad de ceros. Irrelevante para I1–I3 incondicional.

## Hallazgo 2 — Hiary–Zhao, arXiv:2512.14907 (2025) "Unconditional estimates on the argument of Dirichlet L-functions with applications to low-lying zeros"
- Aspecto q (promedio sobre caracteres mod q primo), NO aspecto t. Plantilla de cómo hacer explícito Selberg 1946.
- Thm 2 (Selberg [Sel46, Thm 4] explícito): para 0<ε≤1/4, 0<κ<ε/2, q≥q0(κ), σ≥1/2+5/(8κ log q), |t1|,|t2|≤q^{1/4-ε}, t2−t1≥1.73/(κ log q):
  Σ_{χ≠χ0} N(σ;t1,t2;χ) < (4.79κ + 4.12/(2(t2−t1)log q − 1.73/κ)) q^{1−2κ(σ−1/2)} (t2−t1) log q.
- Prop 14 (Selberg [Sel46, Thm 7] explícito): media de |S(t,χ) − (1/π)Im Σ_{p<x^3} χ(p)p^{−1/2−it}|^{2k} < D(η,δ,κ,k,ε) explícita, x=q^{δκ}, 0<δ<2/(8k+3).
- ADVERTENCIA de los autores: "our results are not completely explicit ... when we state 'for q ≥ q0' we do not compute a specific value of q0". Es decir: constantes explícitas, umbral NO explícito.
- También cita Karatsuba–Korolëv, Uspekhi Mat. Nauk 60:3 (2005) 41–96 "The argument of the Riemann zeta function": cálculos explícitos análogos (puntuales) para ζ.

## Hallazgo 3 — T. Zhao, arXiv:2603.17334 (2026) "Density results for r-gaps between zeros of the Riemann zeta-function"
- Lemma 8 (= [STTB22, Thm 5] con hipótesis de densidad debilitada): si para σ∈[1/2,1/2+δ] y T suficientemente grande
  N(σ,2T)−N(σ,T) ≤ L·T^{1−(σ−1/2)/4} log T   (23),
  entonces para 0<ε≤1/88, v∈N:
  (1/T)∫_T^{2T} |S(t) + (1/π)Σ_{p≤T^{3ε/v}} sin(t log p)/√p|^{2v} dt ≤ C(ε,v) + o(1),
  C(ε,v) = (1/6)(1+Σ_{n=1}^4 R_n(ε,v)) (12 a2 a4(ε,v) v/ε)^{2v}, con a0=1.5435, a1=13+13/(5π)+13/(3πe), a2=13/2+9/(5π)+13/(6πe), a3=3πa1/2+139/75, a4=1+ε a3/(π v a2); R_n fórmulas explícitas (en el paper). C(ε,v) ~ (12 a2 a4 v/ε)^{2v} cuando v→∞.
  [OJO signo: aquí S^{pr} = −(1/π)Σ sin(t log p)/√p, coincide con nuestro S^{pr}_x; x = T^{3ε/v}, es decir a = 3ε ≤ 3/88 en x=T^{a/v}.]
- Lemma 9: (23) vale con L=3.276, σ0=0.549 [Simonič 2020, Thm 1]; también con L=642.86, σ0=1 [STTB22, Lemma 1].
- Prop 10: para 0≤h≤1, v≤ log T/(3 log log T): (1/T)∫_T^{2T}|S(t+h)−S(t)|^{2v} dt ≤ C̃(h,v)^{2v},
  C̃ = 2C(1/88,v)^{1/(2v)} + (2π)^{-1/2}((2v)!/v!)^{1/(2v)} · sqrt(2.021)  si 0≤h≤88v log2/(3 log T);
  C̃ = 2C(1/88,v)^{1/(2v)} + (2π)^{-1/2}((2v)!/v!)^{1/(2v)} · sqrt(log(h log T/(88v/3)) + 13.881) si 88v log2/(3logT)<h≤1.
  (Usa [STTB22, Lemma 6]: Σ_{p≤X}(1−cos(h log p))/p ≤ 2.02+3/log²X para h≤log2/logX; log(h log X) − Σ ≤ 13.88 + 3/log²X para log2/logX≤h≤1.)
- Lemma 11: si 0≤h≤1, h log T≤e^v, 30≤v≤logT/(3loglogT): C̃(h,v) < 10^5 v. Con v=30: 2C(1/88,v)^{1/(2v)} < 8.6·10^4 v.
- Todos "for T sufficiently large" (o(1)); T0 no explícito en este paper. Incondicional.
- Cita: [STTB22] Simonič, Trudgian, Turnage-Butterbaugh, Trans. AMS 375(5) (2022) 3239–3265, arXiv:2010.10675; [Sim20] Simonič, J. Math. Anal. Appl. 491(1) (2020) 124303.

## Hallazgo 4 (CLAVE) — Simonič, Trudgian, Turnage-Butterbaugh [STTB22], "Some explicit and unconditional results on gaps between zeroes of the Riemann zeta-function", Trans. Amer. Math. Soc. 375(5) (2022) 3239–3265; arXiv:2010.10675 (leído v1, 20 oct 2020, vía alphaXiv). INCONDICIONAL.
- **Theorem 5 (I1 explícito, con T0 explícito):** Sea k∈N, 0<ε≤1/88, x0≥e^16. Si
  N(σ,2T)−N(σ,T) ≤ L·T^{1−(σ−1/2)/4} log T  (15)  para T≥T0≥(1/2)e^{1408}, σ∈[1/2,1], L>0, entonces
  ∫_T^{2T} |S(t) + (1/π)Σ_{p≤T^{3ε/k}} sin(t log p)/√p|^{2k} dt ≤ C(ε,k,x0) T   para T ≥ max{x0^{k/ε}, 2T0},
  C(ε,k,x0)=Ĉ(ε,ε,k,x0), Ĉ(ε1,ε2,k,x0) = (1/6)(1+Σ_{n=1}^4 R̃_n(ε1,k,x0)) (12 a2(x0) a4(x0,ε2,k) k/ε2)^{2k},
  R̃1 = (8a0L/ε)(8ε)^{2k}(2k)!/k^{2k−1} + (3ε/(2π a2 a4 √(2k)))^{2k}(13+18^{−k}),
  R̃2 = √13 ((12e)^2 a1 ε/(a2 a4 √k))^{2k} sqrt(1 + (8a0L/ε)(8ε/e)^{8k}(8k)!/k^{8k−1}),
  R̃3 = √13 (24e^2 ε/(π a2 a4 √k))^{2k} sqrt(1 + (8a0L/ε)(8ε/e^2)^{4k}(4k)!/k^{4k−1}),
  R̃4 = √13 (6a1ε/(a2 a4 √k))^{2k} sqrt(1 + (8a0L/ε)(8ε)^{4k}(4k)!/k^{4k−1})  [en v1 sin sqrt visible en R̃4; comprobar versión publicada],
  a0=1.5453 (v1; Zhao 2026 cita 1.5435), a1=13+26/(10π)+13/(3πe), a2(x0)=13/2+18/(10π)+13/(6πe)+(2/log x0)(52+124/(10π)+52/(3πe)),
  a3(x0)=3πa1/2+139/75+62πa1/(75 log x0), a4(x0,ε,k)=1+(ε/k)(log2/log x0 + a3/(π a2)).
  Con nuestra notación: x = T^{a/k} con a=3ε ≤ 3/88; S − S^{pr}_x = S + (1/π)Σ sin/√p. T_0 explícito: T ≥ max{x0^{k/ε}, e^{1408}}; con ε=1/88, x0=e^16: T ≥ e^{1408k} (k=2: e^{2816}; k=4: e^{5632}).
- **Lemma 1 (densidad tipo Selberg explícita):** para T≥(1/2)e^{1408}, σ∈[1/2,1], (15) vale con L ≥ L0 = 642.86. (Prueba: [Sim20, Thm 1] para σ∈[1/2,0.646], T≥10^{23.75}; Ramaré [Ram16] corregido en [KLN18, eq. 1.5]: N(σ,T) ≤ 965(3T)^{8(1−σ)/3} log^{5−2σ}T + 51.5 log²T para σ≥0.646.)
- **Corollary 1:** misma cota para S(t+h), 0≤h≤1, con C′(ε,k,x0) = (1+x0^{−k/ε}) Ĉ(ε, ε/(1+ε x0^{−k/ε}/(k log x0)), k, x0).
- **Corollary 2:** ε=1/88, x0=e^{2·10^4}: C(ε,1,x0) < 1.44161·10^{11}, C(ε,2,x0) < 2.69927·10^{21} (idem C′). Para todo k∈N: C(ε,k,x0) ≤ (ω0 k)^{2k}, ω0 = e^{12.8471} (≈3.8·10^5). ⇒ k=4: C ≤ (4ω0)^{8} (cota cruda). [Con x0=e^{2·10^4} el umbral es T ≥ e^{1.76·10^6 k}.]
- Lemma 2 (Selberg [Sel46, Thm 2] explícito, de Karatsuba–Korolëv [KK05, Thm 1]): para e^16≤x0≤x≤t², |S(t)+(1/π)Σ_{n≤x³}Λ_x(n) sin(t log n)/(n^{σ_{x,t}} log n)| ≤ (σ_{x,t}−1/2)(a1|r(x,t)| + a2(x0) log|t|). Con x0=e^16: a1,a2<15.
- Lemma 3: ∫_T^{2T}(σ_{x,t}−1/2)^ν ξ^{σ_{x,t}−1/2} dt ≤ C(x,T,ξ,ν) T/log^ν x, C = 2^ν ξ^{2/log x} + L a0 2^{4ν+3} ν! (log x/log T)^ν (log T/log x), para x≥2, T≥2T0≥e^{1408}, 1≤ξ≤x^{4k}, x³ξ²≤T^{1/8}.
- Proposition 1: cota explícita general (33) para ∫|S+(1/π)Σ_{p≤x³}|^{2k} con e^16≤x0≤x≤T², log(2T)≤b log x.
- Usa [KK06, Lemma 3] (Karatsuba–Korolëv, Izv. Math. 70 (2006)): momento 2k de polinomio sobre primos ≤ 13(…k)^k T para x=T^{c/(…k)}, T≥exp(max{e²k/c, e³/c}) (explícito).
- **Theorem 6 (I2 explícito para k=1,2):** 0<h≤1, 0<ε≤3/88, 1≤α≤7/(10ε), T≥T1≥max{x0^{6/ε},2T0}:
  |J2(T,h) − (T/π²) log(α+h log T)| ≤ C2 T log^{1/2}(α+h log T),
  |J4(T,h) − (3T/π⁴) log²(α+h log T)| ≤ C3 T log^{3/2}(α+h log T),
  con J_n(T,h)=∫_T^{2T}|S(t+h)−S(t)|^n dt, C2, C3 explícitos vía E1,E2,F1,F2,D1,D2 (fórmulas (48),(49)). Es decir: k=1,2 explícito con T0 explícito; k=4 NO en este paper.
- **(I4) Montgomery–Vaughan/Preissmann explícito usado (44):** |∫_{T1}^{T2}|Σ_{n≤X} a_n n^{−it}|² dt − (T2−T1)Σ|a_n|²| ≤ 3π m0 Σ n|a_n|², m0 = sqrt(1+(2/3)sqrt(6/5)) (de Preissmann, Enseign. Math. 30 (1984) 95–133, usando |log(n/m)|≥2/(3n)). Lemma 4–5: versión bilineal y momento 2k de Im Σ_p a_p p^{it} con error C1(k)(Σ p|a_p|²)^k, C1(k)=(3πm0/4^k)Σ_{m=0}^{2k} binom(2k,m) sqrt(m!(2k−m)!) ≤ 6πm0 k^k.
- **(I5) Lemma 6 (tipo Mertens explícito):** X≥2: si log2/logX≤h≤1, |log(h log X) − Σ_{p≤X}(1−cos(h log p))/p| ≤ 13.88 + 3/log²X; si 0≤h≤log2/logX, Σ_{p≤X}(1−cos(h log p))/p ≤ 2.02+3/log²X. (Usa Rosser–Schoenfeld 1962.)
- Lemma 7: J_{2k}(T,2h(T,η)) ≤ (3ω0 k)^{2k} T para 1≤k≤ log T/(176·10^4), h(T,η)=(2π/η)/log(T/2π), T≥T0 (T0 existencial aquí).
- Cita también Karatsuba–Korolëv [KK06, Lemma 7 p.440]: ∫_T^{T+H}|S+(1/π)Σ_{p<x}|^{2k} ≤ (e^{37}k²/(ε³π²))^k H, 0<ε<10^{−3}, H=T^{27/82+ε}, 1≤k<ε log T/1920, T^{ε/(40k)}<x≤T^{ε/(10k)}, T≥T0 "suficientemente grande" (no explícito). Constantes ≥10^{24} (k=1), ≥10^{49} (k=2).

## Hallazgo 5 — A. Simonič, "Explicit zero density estimate for the Riemann zeta-function near the critical line", J. Math. Anal. Appl. 491(1) (2020) 124303; arXiv:1910.08274 (leído v2). INCONDICIONAL.
- **Theorem 1:** T ≥ H0 = 3.0610046·10^{10}, σ∈[1/2,0.831]:
  N(σ,2T)−N(σ,T) ≤ a T^{1−(σ−1/2)/4} log T + b log²T + c log T log log T + d log T, a=10395.2, b=1.104, c=0.173, d=0.51.
  Corolario: N(σ,T) ≤ 10395.21/(2^{1−(σ−1/2)/4}−1) · T^{1−(σ−1/2)/4} log(T/2), T≥2H0.
- (5): T ≥ 10^{50}, σ∈[1/2,0.569]: N(σ,2T)−N(σ,T) ≤ 5.357 T^{1−(σ−1/2)/4} log T + 1.11 log²T. El método no baja de 3.259 en la constante principal.
- Sólo H=T (diádico). NO da la versión de intervalo corto N(σ,T+H)−N(σ,T) ≪ H(H/√T)^{...} de Selberg/Fujii; Selberg tenía H∈[T^a,T], a∈(1/2,1].
- Menciona: Karatsuba–Korolëv [KK06, Thm 1]: N(σ,T+H)−N(σ,T−H) ≤ 13 H T^{ε(1−2σ)/10} log T, 0<ε<0.001, H=T^{27/82+ε}, T≥T0(ε) NO explícito. (Russian Math. Surveys 61:3 (2006) 389–482.)
- Corollary 5: ∫_0^T|ζ(1/2+it)|²dt = T log T − (1+log2π−2γ)T + E(T), E(T) ≤ 13.803 T^{3/4}sqrt(log(T/2π)) + 83.964 √T log(T/2π) + 2·10³ log T + 3691.24, T≥2π.
- KLN18 (Kadiri–Lumley–Ng, J. Math. Anal. Appl. 465(1) (2018) 22–46, arXiv:1706.?, "Explicit zero density for the Riemann zeta function"): N(σ,T) ≤ A(σ)T^{8(1−σ)/3} log^{5−2σ}T + B(σ) log²T, σ∈[3/5,1), T≥H0; útil sólo σ>5/8 (no cerca de 1/2).

## Hallazgo 6 (I6) — Grafakos & Montgomery-Smith, "Best constants for uncentred maximal functions", arXiv:math/9412218 (leído v2). [Bull. London Math. Soc. 29 (1997) 60–64 — ref. de revista de memoria, no verificada aquí.]
- Theorem: para 1<p<∞, la norma del operador maximal NO centrado M1 en L^p(R) es la única raíz positiva c_p de (p−1)x^p − p x^{p−1} − 1 = 0. Además p/(p−1) < c_p < 2p/(p−1).
- Para el centrado: ‖M_c‖ ≤ ‖M_unc‖ = c_p (cota explícita válida).

## Hallazgo 7 (I4) — Hilbert ponderado de Montgomery–Vaughan con constante explícita. Fuente leída: W. Yangjit, "On the Montgomery–Vaughan weighted generalization of Hilbert's inequality", arXiv:2203.14950 (v1, 2022).
- MV 1974 (J. London Math. Soc. (2) 8 (1974) 73–82): |Σ_{m≠n} z_m z̄_n/(λ_m−λ_n)| ≤ C1 Σ|z_n|²/δ_n, δ_n = min(λ_n−λ_{n−1}, λ_{n+1}−λ_n), con C1 = 3π/2; y no ponderada ≤ (π/δ)Σ|z_n|².
- Preissmann (Enseign. Math. 30 (1984) 95–113): C1 ≤ π sqrt(1+(2/3)sqrt(6/5)) < 4π/3. Selberg (no publicado) 3.2. Conjetura C1 = π. Yangjit: el método no baja de 3.19497.
- Consecuencia estándar (por cuadrado e integración): |∫_{T1}^{T2}|Σ a_n e^{iλ_n t}|²dt − (T2−T1)Σ|a_n|²| ≤ 2C1 Σ|a_n|²/δ_n. STTB22 (44) lo usa en la forma ≤ 3πm0 Σ n|a_n|², m0=sqrt(1+(2/3)sqrt(6/5)) (≈1.3) para a_n n^{−it}.
- También Weber, arXiv:0907.4931 (expositivo): Prop 6 ≤ (4π/δ)Σ|d(n)|² (no ponderado) y Prop 7: momento 2q con linealmente independientes: (1/|J|)∫_J|Σ d(n)e^{itλ_n}|^{2q} ≤ (Σ|d(n)|²)^q (q! + 2min(N^q, πq!)/(|J|ξ)), ξ = espaciado lineal de orden q (explícito).

## Hallazgo 8 — CONDICIONAL (RH): Chirre & Quesada-Herrera, "The second moment of S_n(t) on the Riemann hypothesis", arXiv:2006.08503 (v2 2021). Asintótica de 2º momento de S_n, n≥1, bajo RH; constantes C_n=Σ Λ²(m)/(m log^{2n+2}m) numéricas (Tabla 2). No aplicable (condicional, n≥1).
- Mismo paper cita Selberg 1946 incondicional: ∫_0^T|S(t)|²dt = (T/2π²) log log T + O(T sqrt(log log T)) — sin constantes explícitas.

## Hallazgo 9 (I5) — Mertens explícito. Fuente leída: C. Axler, "New estimates for some functions defined over primes", arXiv:1703.08032 (v2 2017), que cita literalmente:
- Rosser–Schoenfeld [Illinois J. Math. 6:1 (1962) 64–94], Thm 5: log log x + B − 1/(2log²x) < Σ_{p≤x}1/p < log log x + B + 1/(2log²x); izquierda x>1, derecha x≥286. B=0.2614972128...
- RS Thm 6: log x + E − 1/(2log x) < Σ_{p≤x} log p/p < log x + E + 1/(2 log x); izquierda x>1, derecha x≥319. E=−1.33258227573...
- RS Thm 7: (e^{−γ}/log x)(1 − 1/(2log²x)) < Π_{p≤x}(1−1/p) < (e^{−γ}/log x)(1+1/(2log²x)); izq. x≥285, der. x>1.
- RS p.87: −S < 1.02/((x−1)log x), S=Σ_{p>x}(log(1−1/p)+1/p).
- Dusart [Ramanujan J. (2018) "Explicit estimates of some functions over primes", Thm 5.6]: |Σ_{p≤x}1/p − log log x − B| ≤ 1/(5 log³x), x≥2278383. Dusart Thm 5.7: |Σ log p/p − log x − E| < 0.3/log²x, x≥912560.
- Axler Prop 5.1: −1/(20log³x) − 3/(16log⁴x) ≤ Σ1/p − log log x − B ≤ 1/(20log³x)+3/(16log⁴x) (izq. x>1, der. x≥46909074). Prop 5.2: |Σ log p/p − log x − E| ≤ 3/(40log²x)+3/(20log³x) (izq. x>1; der. x≥30972320).
- Dusart general (5.4): |Σ1/p − loglog x − B| ≤ η_k/(k log^k x) + (k+2)η_k/((k+1)log^{k+1}x) si |ϑ(x)−x|<η_k x/log^k x para x≥x0(k).
- Además STTB22 Lemma 6 (ya registrado): versiones para Σ(1−cos(h log p))/p.

## Hallazgo 10 — Chourasiya & Simonič, "An explicit form of Ingham's zero density estimate", arXiv:2507.15184 (2025). INCONDICIONAL.
- Cor 1: T ≥ H_RH = 3·10^{12}: N(σ,T) ≤ B1 T^{3(1−σ)/(2−σ)} log³T + B2 log²T + B3 log T; p.ej. σ∈[0.5,0.625]: 8.604, 9.461, 167.8; σ∈[0.5,0.53125]: B1=5.360. Útil lejos de 1/2 (no sustituye a Selberg en la escala σ−1/2 ≍ 1/log T, porque T^{3(1−σ)/(2−σ)} ≈ T en σ≈1/2).
- Lemma 10 (MV explícito): |∫_{T1}^{T2}|Σ a_n n^{it}|²dt − (T2−T1)Σ|a_n|²| ≤ 2πm0 Σ(n+1/2)|a_n|², m0 = sqrt(1+(2/3)sqrt(6/5)) < 1.31541. [I4 en forma directa y citable.]
- Lemma 5 (de KLN18 Lemma 4.1): ∫_0^T|M_X(1/2+it)|²dt ≤ (C1 T + C2 X) log X, X≥X0≥10^9.
- Thm 2: 4º momento explícito de ζ en [T,2T] con término principal T log⁴T/(2π²).

## Hallazgo 11 — A. Fiori, "Zero density theorems for short intervals", arXiv:2609.22624 (sep 2026). Intervalos cortos [t−h,t+h] pero cerca de σ=1 (α<1/6, Re ρ>1−α). NO cubre σ cerca de 1/2. Irrelevante para la densidad tipo Selberg en intervalos cortos.

## Resultados NEGATIVOS (búsquedas sin versión explícita incondicional)
- Densidad de Selberg/Fujii en intervalo corto N(σ,T+H)−N(σ,T) ≪ H (H/√T)^{...} log T con H=T^a, a<1, explícita: NO encontrada. Única versión con H<T: Karatsuba–Korolëv [KK06, Thm 1] (H=T^{27/82+ε}, constante 13, T0(ε) NO explícito; citado en Simonič 2020). Búsquedas: alphaXiv "zero density short intervals Selberg explicit critical line"; web "explicit zero density estimate near the critical line". Para [T,2T] basta H=T: STTB22 Lemma 1 (L=642.86, T≥e^{1408}/2) o Simonič 2020 (a=10395.2, T≥H0; 5.357 para T≥10^{50}).
- Momentos de Selberg ∫_T^{2T} S(t)^{2k} ≪ T (log log T)^k con constantes explícitas (I3): NO encontrado como enunciado. Ni Chirre–Quesada-Herrera (RH, S_n n≥1) ni Inoue–Kobayashi–Toma (RH) lo dan. Búsquedas: "explicit moments of S(t) Selberg (log log T)^k explicit constants unconditional", alphaXiv "moments S(t) explicit". DERIVABLE inmediatamente: Minkowski + STTB22 Thm 5 (resto ≤ C(ε,k,x0)T) + STTB22 Lemma 5 (momento 2k de Im Σ a_p p^{it} = (T/4^k)binom(2k,k)Σ_p|a_p|²|p| + O*(C1(k)(Σ p|a_p|²)^k)) + Mertens explícito (RS62 Thm 5).
- "explicit Selberg central limit theorem": sólo resultados no explícitos (Arguin–Bailey 2403.19803 grandes desviaciones, no explícito).
- Tsang/Fujii explícito para k=4 (I2): no como enunciado aislado salvo Zhao 2026 Prop 10 (todo v, T suficientemente grande) — ver Hallazgo 3. STTB22 Thm 6 sólo k=1,2 (T0 explícito).
- Advertencia: constantes de STTB22 leídas de arXiv v1 (2020); la versión publicada (TAMS 2022) puede diferir (p.ej. a0 = 1.5453 en v1 vs 1.5435 citado por Zhao 2026). Verificar contra versión publicada antes de usar números.
