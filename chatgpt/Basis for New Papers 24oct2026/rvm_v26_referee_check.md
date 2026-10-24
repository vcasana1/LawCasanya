# Version 26: independent referee check of the new results

**What the referee was.** A subagent of the same model (Claude), launched inside the working session on
15 October 2026. It is not a human referee or an external system. It is independent of the writing only in the
sense that it had not seen the conversation or the reasoning that produced the proofs. Because it is the same
model, it may share blind spots with the author of the text. It was read-only and modified no file.

**What it was given.**
- `review_new_results.tex`: the new results of version 26.
  - Lemma rb-mass-ms; Theorem rb-uniqueness and Corollaries rb-U, rb-selection, rb-equivalence; Remark
    rb-uniqueness-input.
  - Proposition rb-nonfinitary and Remark rb-nonfinitary.
  - The whole subsection rb-window: Lemma rb-peel, Theorems rb-window-unknown and rb-bernstein, Remark
    rb-window-positivity, Lemma rb-minimizer, Theorem rb-window-equivalence, Remark rb-minimizer-open,
    Heuristic rb-window-zerofree.
- `review_context.tex`: the earlier results these depend on, taken as given.
  - Proposition rung-apriori and Lemma mean-value-ordinates.
  - The section on Cramér's function, with Lemma edge and Proposition cramer-zero-free.
  - Theorem rung-zero-sum.
  - The setting of Route B, Proposition rb-prescribed-uniqueness, and Hamburger's theorem as used.

**Instruction.** Check every new proof line by line, and check that each earlier result is used within its
hypotheses. Report, for each item, either "correct" or a specific error with a fix. Check also that the remarks
and the heuristic claim no more than is proved.

The report is reproduced verbatim below, followed by what was done with each point. The draft numbering in the
report differs from the compiled paper; labels are used throughout.

---

## Report (verbatim)

**Referee report on review_new_results.tex.** All eight proofs are correct; the problems are in the remarks and the heuristic, plus small fixes. Files were read only; nothing was modified.

**Lemma rb-mass-ms: CORRECT.**
- Isolation: $|\log m-\log n|\ge 1/(n+1)\ge 1/(2X+1)\ge 1/(5X)$, so $\varphi_n(\log m)=0$. The formula for $\mathsf c_{\varphi_n}$ is right because $\psi$ is even.
- Term $\mathsf k$: the bound $|\mathsf k|\le 2e^{u/2}$ for $u>\frac12$ holds, because the second term is decreasing and is at most $0.62<e^{1/4}$. $e^{1/10}$ can be $e^{1/20}$; harmless.
- Truncation: $A=\lceil 2/\delta\rceil+1$ and partial summation give $X^{-\delta(A-1)}\log T\le X^{-2}\log T$.
- Sobolev step: the intervals $I_n$ are disjoint for $X>1$. The scalings $|\mathrm b_k|\le1$ are right for both $\mathcal S$ and $\mathcal S'$, using $\kappa_k\le T$. The proof of the mean-value lemma uses only the local count $O(\log t)$, which the tube gives.
- Exponents: $X^{-1}T=X^{\delta}$ and $X^{-2}T^2=X^{2\delta}$, so the total is $X^{3\delta}$. $\delta\le1$ only restricts $\epsilon\le3$, which is trivial.

**Theorem rb-uniqueness: CORRECT.**
- Prop rung-apriori at $\mathsf t=1$: every hypothesis holds. For $1\le X<2$ the lemma does not cover $\mathsf a_2$, but the Prop's constants may depend on the solution, so a single number is absorbed.
- $\mathrm b=0$: since $\kappa_k/\log\kappa_k\to\infty$, $4\mathrm b+o(1)\to0$.
- Extension to $\Re s>1$: the identity theorem applies, since $G$ is zero-free and $\exp\mathsf D$ is holomorphic there.
- Hamburger:
  - (H0): $(s-1)\zeta_{\boldsymbol\kappa}=P\pi^{s/2}/(2\Gamma(1+\frac s2))$, of finite order.
  - (H2): $P/(s(s-1))$ is symmetric under $s\mapsto1-s$.
  - (H3): holds for every $\alpha>0$.

  This matches Titchmarsh §2.13.
- Residue: $P(1)=1$ and $G\sim s-1$ give residue $1$. $C_1=1$, and the identification of the masses is valid.

**Corollaries rb-U, rb-selection, rb-equivalence: CORRECT.**
- In rb-selection, applying Prop rb-compactness to a subsequence needs $\mathscr T_j\subset\mathscr T_{m_j}$ (trivial). The hypothesis B is superfluous.
- In the "direct reading", if $\zeta_{Z1}$ is built from critical-line zeros, state RH first. RH follows from $P_{\boldsymbol\gamma}=c'\xi$ (same zeros).

**Remark rb-uniqueness-input: overclaims.**
- "A list with a linear drift … is not excluded by the identity" reads as if exact drift solutions exist. Nothing proves that. Say "Prop rung-apriori alone does not exclude it."
- "Which every exact solution satisfies" needs the mass hypothesis. In the tube, Lemma rb-mass-ms supplies it.

**Prop rb-nonfinitary: CORRECT.**
- Derivative bounds: $\cosh x-1\le\frac{x^2}2\cosh x$, $|\sinh x|\le|x|\cosh x$, $|d|^j\le d^2 2^{2-j}$. Leibniz gives $d_k^2\mathfrak W_r$, and $d_k^2<\frac14$.
- Partial summation: $r\int N t^{-r-1}$, then $\frac{rH_0^{1-r}}{2\pi(r-1)}(\log H_0+\frac1{r-1})\le\frac r{r-1}H_0^{1-r}\log H_0$.
- I checked the counting bound against arXiv 2107.06506, Cor. 1.2 ($T\ge e$; the constant term is absorbed). At $t=100$ the inequality $\le\frac t{2\pi}\log t$ reads $10.2\le45.2$, and it holds beyond.
- Mollification is valid: for $r\ge2$, $f''\in L^1$, and the $r=2$ bound gives continuity of the right side.
- Minor: $r$ is a free symbol in \eqref{eq:rb-nonfinitary-section}; write $r_{\mathsf f}$ per test.

**Remark rb-nonfinitary.**
- The B-spline inequality is correct, using $\frac r{4(r-1)}\le\frac12$.
- "Finite sections … carry no information on RH" is stated without the qualifier "at precision coarser than the bound"; add it.
- The figure $10^{-57}$ cannot be checked from the supplied files. With $u^*=6.4$, $r=7$, the bound equals $1.3\cdot10^{-68}h^{-6}$, so the figure holds only if every $h\gtrsim0.0153$ and the splines have order $\ge8$.

**Lemma rb-peel: CORRECT.**
- The support argument uses positivity correctly.
- Monotone convergence gives $\mu_j(\{t_j\})$.
- The mean of $|P_j-c|^2$ over $[Y,2Y]$ gives the coefficient argument.
- Subtracting $m_j\delta_{t_j}$ keeps $\mu_{j+1}$ positive, because the atom equals $\mathrm a_{j,0}=m_j$.
- The re-application with $t_{j+1}$ needs no prior support information. $t_j\to\infty$ closes the induction.

**Theorem rb-window-unknown: CORRECT.**
- The proof of Lemma edge needs an integer $m$; use $m=\lceil A\rceil$.
- Boundedness of $\mathscr Z_\xi$ near $J'\times[0,1]$, linearity from real to complex $\mathsf f$, and the identity theorem are all fine.

**Theorem rb-bernstein: CORRECT.** Bernstein on $(0,\infty)$ after the shift by $a$, then $\mu=e^{at}\nu$ with $y_1=a$.

**Remark rb-window-positivity: false claim.**
- "Data from the primes only" is false. $\mathscr V_{\rm b}$ integrates $\xi'/\xi$ over $[-a,1+a]$, which needs $\zeta$ on $[0,1]$ inside the strip, and $g$ brings in $\Gamma$. Replace with "no sum over zeros."
- "No finite computation decides it" needs the same precision qualifier as above.

**Lemma rb-minimizer: CORRECT, with one fix.**
- Fix: the $\varphi_j$ must be real. Otherwise $\langle\mathfrak R,\varphi_j\rangle^2$ is not $\ge0$, so $\mathfrak E=0$ does not force the pairings to vanish, and $\mathscr G$ need not be real.
- Checked: $C^2$ convergence of $\mathscr P$; the order-2 continuity giving $\mathfrak E=\langle\mathfrak R,\mathscr P\rangle$; coordinatewise $C^1$, with uniform convergence of the derivative series from the weights. The product box allows varying one coordinate.
- Jensen: $-m\log 2r\le0$ for $r\ge1$, and the factor $\frac12$ comes from oddness. $c$ depends on $\boldsymbol\kappa^*$.

**Theorem rb-window-equivalence: CORRECT.**
- Compactness and continuity of the pairing are fine.
- The rearrangement needs Lemma rb-matching in its general sorting form: if $x_k\in[\tau_k-C,\tau_k+C]$ for all $k$, the sorted list satisfies the same bounds. That is true by an elementary counting argument.
- Prop rb-prescribed-uniqueness is applied within its hypotheses. The "in particular" follows from (c).

**Remark rb-minimizer-open: gap.**
- "At $\boldsymbol\gamma$ … the gradient does not vanish" (when RH fails) is asserted without proof. It is true, given three facts:
  - $\mathfrak E_U(\boldsymbol\gamma)>0$ for large $U$, by the theorem plus monotonicity in $U$;
  - the identity $\mathfrak E=\langle\mathfrak R,\mathscr P\rangle$ and the gradient formula hold at every $\boldsymbol\kappa$, not only at minimizers;
  - there are $\gg r\log r$ distinct ordinates unconditionally. Cite Conrey here as well, not only under RH; his simple zeros on the line are unconditional.
- The claim "for large $U$ every minimizer is degenerate" is correct by the same monotonicity argument. The Cartwright–Levinson constant $u_2/\pi$ is correct.

**Heuristic rb-window-zerofree.**
- Numbers check: $2\cdot28.73/2\pi=9.15$ and $\operatorname{arccosh}9.15=2.90$, so $U\approx6.8$.
- "Two points are not proved" understates it. The on-line zeros near $\gamma_0$ and the non-resonant $\kappa_k$ contribute kernel terms $\frac12\int\psi\cos((\cdot)u)$ of indefinite sign. With $\psi$ supported near $U$, a translated $\psi$ does not give $\widehat\psi\ge0$.
- The window $(0,U)$ is inconsistent with $(U^{-1},U)$ in the theorem.
- "Interpolate between known zero-free regions and RH" is loose. For fixed $U$ the bound is void once $\log\log\gamma_0\gtrsim U/2$, and classical regions concern the neighbourhood of $\Re s=1$.

Source checked: [Hasanalizadeh–Shen–Wong, arXiv 2107.06506](https://arxiv.org/pdf/2107.06506).

---

## What was done with each point (all in the compiled v26)

**Changed in the text**

| Point | Change |
|---|---|
| Remark rb-uniqueness-input, drift | Now reads: Proposition rung-apriori alone does not exclude an exact solution with a linear drift (whether such solutions exist is not known); the tube excludes it. |
| Remark rb-uniqueness-input, Laplace identity | Now says that a solution in a tube satisfies the identity, with the mass hypothesis supplied by Lemma rb-mass-ms. |
| Proposition rb-nonfinitary, free symbol $r$ | The finite set of tests is taken "with the same $r$". |
| Remark rb-nonfinitary, qualifier | "at a precision coarser than this bound" added. |
| Remark rb-nonfinitary, $10^{-57}$ | The figure is now attributed to the ball-arithmetic evaluation in `certV.py` (column $\epsilon_\zeta$ of Table tab:rb-verified). |
| Remark rb-window-positivity, "primes only" | Replaced by: a representation with no sum over the zeros (the primes, $\xi'/\xi$ on a real segment and $\Gamma$). |
| Remark rb-window-positivity, qualifier | Precision qualifier added. |
| Lemma rb-minimizer | The test functions are now real. |
| Theorem rb-window-unknown | Growth written as $y^{-A}\le y^{-\lceil A\rceil}$, so that Lemma edge applies with an integer exponent. |
| Remark rb-minimizer-open | The non-vanishing of the gradient at $\boldsymbol\gamma$ is now justified by the referee's three facts, with Conrey cited unconditionally. |
| Heuristic rb-window-zerofree | Window $(U^{-1},U)$; a third open point (on-line zeros and nearby $\kappa_k$ give terms of indefinite sign); the "interpolation" sentence replaced by the statement that for fixed $U$ the bound is informative only for $\log(C\log\gamma)<U/2$. |

**Not changed (no error)**

- Corollary rb-selection: the hypothesis B is superfluous but harmless, so it was kept for the logic of the section.
- "Direct reading" in the proof of Corollary rb-selection: RH is already given by Theorem rb-uniqueness in the same proof.
- Lemma rb-mass-ms: $e^{1/10}$ against $e^{1/20}$, and the range $1\le X<2$, are harmless as the report says.
- Theorem rb-window-equivalence: Lemma rb-matching is already stated in the general sorting form.

**On the $10^{-57}$ figure.** `certV.py` computes the bound rigorously for every test of every stage. The largest
value is $7.5\cdot10^{-58}$, at $m=15$ ($h=0.0101$, $u^*\le6.39$, splines of order $8$, $r=7$).

**Independent hand check of that figure.** The constant is $\mathfrak W_7\le(1+u^{*2})\cosh(u^*/2)\,h(1+2/h)^7\approx6.5\cdot10^{16}$. The bound is then
$\tfrac{7}{24}\cdot6.5\cdot10^{16}\cdot(3\cdot10^{12})^{-6}\cdot\log(3\cdot10^{12})\approx7.4\cdot10^{-58}$,
in agreement with the program. The referee's closed form $1.3\cdot10^{-68}h^{-6}$ appears to carry a different
constant: it would give $1.2\cdot10^{-56}$ at $h=0.0101$, whereas both the program and the hand computation give
$\approx7.4\cdot10^{-58}$.
