# Specification — final MATLAB for the Möbius energy–entropy model

Target: one MATLAB function, `mobius_final_exact_mc_ldp.m`, producing the numbers and the
LaTeX fragment for a journal submission. Three layers must stay separated in code, in
output, and in the generated LaTeX: **(I) exact/theorem**, **(II) measured/statistical**,
**(III) heuristic**. Nothing from layer III may be presented as a result of layer I.

Input: `moebius.bin`, 455,052,511 `int8` entries; entry `n` is `mu(n)` for
`n = 1 .. 455052511`. No prime tables, no zeta zeros, no fitted spectral data anywhere.

---

## 0. Global invariants (violations must `error()`, not warn)

**0.1 No intermediate product may exceed 2^53 = 9007199254740992.**
At `N = 455052511`: `n^2 = 2.07e17` and `Q(n)^2 = 7.65e16`, both out of exact range.
Every term must be formed by division only. Mandatory rescaled forms, with `qn = Q(n)/n`:

| quantity | forbidden | required |
|---|---|---|
| `M(n)^2/n^2` | `M.*M./(n.*n)` | `(M./n).^2` |
| `Q(n)/n^2` | `Q./(n.*n)` | `qn./n` |
| `Q(n)(Q(n)-1)/n^2` | `Q.*(Q-1)./(n.*n)` | `qn .* ((Q-1)./n)` |
| `phi(Q)/n^2` | — | `qn.^2 - qn./n` |
| `Q^2/n^2` | — | `qn.^2` |
| `phi(Q)/n^4` | — | `(qn.^2 - qn./n)./(n.^2)` → still forms `n^2`; use `((qn.^2 - qn./n)./n)./n` |
| `phi(Q)*Q/n^4` | — | `(qn.^2 - qn./n) .* (qn./n)` |
| `phi(Q)*Q^2/n^4` | — | `(qn.^2 - qn./n) .* (qn.^2)` |

where `phi(Q) = Q*(Q-1)`. Assert at every chunk: `max(abs(M)) < 2^53`, `max(Q) < 2^53`,
`n_max < 2^53`.

**0.2 Parity.** For every cutoff: `mod(Q(N) - M(N), 2) == 0`. This is exact because
`mu(n) ≡ mu(n)^2 (mod 2)`. Abort otherwise — it detects file corruption for free.

**0.3 Lower-tail orientation.** For every cutoff assert `a_N = zeta2 * E_N(M) < 1`
(equivalently `E_N(M) < 1/zeta(2)`). If not, the lower-tail reading inverts and the whole
layer-III section is meaningless; abort with a clear message.

**0.4 LaTeX generation: never use `sprintf` with a backslash in the format string.**
`\r` is a *valid* escape (carriage return) and corrupts the `.tex` silently; MATLAB only
warns about the *first* invalid escape per call, so `\qquad`, `\Om`, `\widehat` degrade
unreported. Build every line by concatenation:
`['$\log_{10}|\Om| = ' sprintf('%.3f', x) '$']`. Concatenation does no escape processing.

**0.5 Reproducibility record**, written to the `.mat` and printed:
MATLAB version, RNG generator name and seed, SHA-256 of `moebius.bin`, file byte count,
`N0`, cutoff list, block size, and wall-clock. For SHA-256 use
`java.security.MessageDigest.getInstance('SHA-256')` streamed over the file, or the OS tool
(`sha256sum` / `certutil -hashfile`). *The exact Java invocation is not verified in this
spec — Codex must test it.*

---

## 1. Definitions

- `N0 = 1000` (fixed throughout; both sides of every comparison use it).
- `M(n) = sum_{k<=n} mu(k)`, `Q(n) = #{k<=n : mu(k) != 0}`.
- `L = log(N/N0)`.
- Logarithmic energy: `E_{N0,N}(R) = (1/L) * sum_{N0 < n <= N} R(n)^2 / n^2`.
- Class `Omega_N^(1)`: fixed zero mask up to `N`, fixed counts of `+1` and `-1`.
  `m = Q(N)`, `S = M(N)`, `p = (m+S)/2`, `q = (m-S)/2`, `|Omega| = nchoosek(m,p)`.
- `xi_j` = sign at the j-th nonzero position; `T_j = sum_{i<=j} xi_i`.
  For any member of the class, `R(n) = T_{Q(n)}`.
- `d = 1/zeta(2) = 6/pi^2 = 0.6079271018540267`.

---

## 2. Layer I — exact closed forms (theorem level)

### 2.1 Moments of the exchangeable sign vector

Let `t = S^2/m` (an O(1) number; `t = 0.1653757` at `N=5e6`, `t = 0.1059512` at the full
file). Then, in numerically safe scaling:

```
mu2 = (t - 1) / (m - 1)
mu4 = ( m * ( t^2 - 6*t + 3 + (8*t - 6)/m ) ) / (m-1) / (m-2) / (m-3)
```

These are algebraically identical to
`mu2 = (S^2 - m)/(m(m-1))` and
`mu4 = (S^4 - 6mS^2 + 8S^2 + 3m^2 - 6m)/(m(m-1)(m-2)(m-3))`,
but the unscaled numerator of `mu4` reaches `3m^2 = 2.3e17` at the full file and is **not**
exactly representable. Use the scaled form. Successive division only; never form
`m*(m-1)*(m-2)*(m-3)`.

`mu2` is `E[xi_a xi_b]` for `a != b`; `mu4` is `E[xi_a xi_b xi_c xi_d]` for four distinct
indices.

### 2.2 Second moment and the exact mean

```
E[T_j^2] = j + mu2 * j * (j-1)
```

Endpoint checks (must hold identically): `E[T_1^2] = 1` and `E[T_m^2] = S^2`.

```
Sigma1 = sum_{N0<n<=N} Q(n)/n^2
Sigma2 = sum_{N0<n<=N} Q(n)(Q(n)-1)/n^2
mu_N   = (Sigma1 + mu2 * Sigma2) / L          % = E_pi[ E_{N0,N}(pi) ]
```

### 2.3 Factorised covariance and the exact variance

For `j <= k`:

```
phi(j)  = j*(j-1)
psi(k)  = 2 + 4*mu2*(k-2) + mu4*(k-2)*(k-3) - mu2^2*k*(k-1)
Cov(T_j^2, T_k^2) = phi(j) * psi(k)
```

`psi(m) = 0` identically (forced by `T_m = S` deterministic).

Expand `psi(k) = c0 + c1*k + c2*k^2` with

```
c2 = mu4 - mu2^2
c1 = 4*mu2 - 5*mu4 + mu2^2
c0 = 2 - 8*mu2 + 6*mu4
```

Because `Q(n)` is non-decreasing, `n1 < n2 ⇒ Q(n1) <= Q(n2)`, so the `j<=k` form applies
directly in the `n`-indexed double sum:

```
Var_pi(E) * L^2 = 2*sum_{n1<n2} phi(Q(n1))*psi(Q(n2))/(n1^2 n2^2)
                +   sum_{n}     phi(Q(n)) *psi(Q(n)) / n^4
```

With the running prefix `Phi(n) = sum_{N0<n1<=n} phi(Q(n1))/n1^2` and six **cutoff-independent**
accumulators

```
G_r = sum_{N0<n<=N} (Q(n)^r / n^2) * Phi(n-1)          r = 0,1,2
H_r = sum_{N0<n<=N} phi(Q(n))*Q(n)^r / n^4             r = 0,1,2
```

the variance at any cutoff is

```
sigma_N^2 = ( 2*(c0*G_0 + c1*G_1 + c2*G_2) + (c0*H_0 + c1*H_1 + c2*H_2) ) / L^2
```

**Conditioning note (important).** Do *not* evaluate `psi(k)` pointwise in the streaming
loop. `psi(m) = 0` arises by cancellation of O(1) terms, so a pointwise evaluation loses all
significant digits near `k = m`. In the accumulator form the cancellation happens once, at
the final combination, where the terms are of size roughly `+8.9, -1.3, +0.29` — a
cancellation factor of about 1.13, harmless.

Expected magnitudes at the full file (sanity only, not assertions):
`c0 ≈ 2`, `c1 ≈ -1.29e-8`, `c2 ≈ 2.06e-17`, `G_0 ≈ 4.45`, `G_1 ≈ 1.02e8`, `G_2 ≈ 1.41e16`,
`H_r` terms ~1e-4 (negligible), `sigma_N ≈ 0.304`.

### 2.4 Derived reported quantities

```
E_N(M)        = Sigma_M / L,  Sigma_M = sum (M(n)/n)^2
Delta_N       = E_N(M) - mu_N
rho_E         = E_N(M) / mu_N
rho_asym      = zeta(2) * E_N(M)                 % the drift-free series
mu_N^asym     = d * ( 1 - (1 - t)/L )            % t = S^2/m
relDiscrepancy= (mu_N^asym - mu_N)/mu_N
endpointTerm  = t / L
sigma_N^asym  = sqrt( 4*d^2*(L - 2.5)/L^2 )
z_N           = (E_N(M) - mu_N)/sigma_N
nu_N          = 2*mu_N^2/sigma_N^2
```

Note the constant is **2.5**, not 1.5. (An earlier draft dropped the term
`-x0 * ∫_{x0}^1 y^{-2} dy = -(1-x0)`, an infinitesimal multiplying a divergent integral.
The 2.5 version reproduces the measured sample SD to 0.09 %; the 1.5 version is wrong by
6.4 standard errors.)

---

## 3. Streaming algorithm

One pass over the file, chunked reads of `2^22` entries, cut at cutoff boundaries.
Maintain running `M`, `Q`, and Kahan accumulators for `Sigma_M, Sigma1, Sigma2, Phi,
G_0..G_2, H_0..H_2`. Snapshot all accumulators plus `m, S, max|M|` at each cutoff.

**Summation rule.** Inside each chunk, sum in sub-blocks of `n_b = 2^16` with `sum`, and
combine sub-block totals with Kahan compensation. This makes the error bound independent of
MATLAB's undocumented internal summation order.

Cutoffs (exact layer): `[1e4 3e4 1e5 3e5 1e6 5e6 5e7 1e8 1.5e8 2e8 2.5e8 3e8 3.5e8 fileEntries]`.

---

## 4. Certified error bound (for `Delta_N` only)

All three sums `Sigma_M, Sigma1, Sigma2` have non-negative terms, so `sum|x_i| = Sigma`.
With `u = 2^-53`, `n_b = 2^16`, `gamma = n_b*u/(1 - n_b*u) = 7.28e-12`:

```
eps_Sigma   = (5*u + gamma) * Sigma          % 3u per term + 2u Kahan + block bound
eps_mu2     = 3*u*abs(mu2)
eps_muL     = eps_Sigma1 + abs(mu2)*eps_Sigma2 + Sigma2*eps_mu2 + 2*u*abs(Sigma1+mu2*Sigma2)
eps_DeltaL  = eps_SigmaM + eps_muL + u*abs(Sigma_M - (Sigma1+mu2*Sigma2))
eps_Delta   = (eps_DeltaL + 3*u*abs(DeltaL))/L + u*abs(Delta)
```

Report `[Delta - eps_Delta, Delta + eps_Delta]` and the margin `|Delta|/eps_Delta`.
**Abort if `0` lies in the interval at any cutoff.** Expected margin at the full file:
about `1e11`.

Declared assumption, to be stated in the paper: IEEE-754 binary64 throughout, no extended
precision, no FMA contraction, no reassociation. This is an *a priori* propagated bound, not
directed-rounding interval arithmetic — say so in the LaTeX, do not write "exact evaluation".

A bound of the same form may be reported for `sigma_N^2` (all `G_r`, `H_r` terms are
non-negative; allow a factor 2 in the relative bound because `Phi` is itself accumulated).
Certification language in the paper is claimed **only** for the sign of `Delta`.

---

## 5. Self-tests — all must pass or the run aborts

### T1 — Exhaustive verification of the covariance formula

For `(m,p)` in `{(6,3), (6,4), (5,3)}` — balanced/even, unbalanced/even, odd `m` —
enumerate all `nchoosek(m,p)` arrangements with equal weight, compute `T_j`, and compare
empirical `Cov(T_j^2, T_k^2)` against `phi(j)*psi(k)` for **all** pairs `j<=k`.
Tolerance: `1e-12` absolute.

Hand-verified values the test must reproduce:

| `(m,p)` | `S` | `t = S^2/m` | `mu2` | `mu4` |
|---|---|---|---|---|
| (6,3) | 0 | 0 | −0.2 | 0.2 |
| (6,4) | 2 | 2/3 | −1/15 | −1/15 |
| (5,3) | 1 | 0.2 | −0.2 | 0.2 |

Also assert: `psi(m) = 0` to `1e-12` in all three; `E[T_1^2] = 1`; `E[T_m^2] = S^2`;
and for `(6,3)`, `Var(T_2^2) = 3.84` exactly (direct check: `T_2 ∈ {−2,0,2}` with
probabilities `0.2, 0.6, 0.2`, so `E T_2^2 = 1.6`, `E T_2^4 = 6.4`).

### T2 — Independent re-implementation of the double sum

At the smallest cutoff (`N = 1e4`, `m ≈ 6079`), compute `sigma_N^2` twice:
(a) from the six accumulators; (b) by an explicit loop over `k` that **recomputes**
`sum_{j<k} v_j*phi(j)` from scratch at each `k` — no running prefix, no `m×m` matrix
(that would be 296 MB at `m=6079`; use a loop with a vectorised inner sum).
Require relative agreement `< 1e-11`. This is the only test that catches an indexing error
in the prefix collapse; a purely algebraic check cannot.

Here `v_j = sum_{n : Q(n)=j, N0<n<=N} 1/n^2`, built with
`accumarray(idx, vals, [m 1], [], 0)` — pass `[]`, **not** `@sum`, to stay on the fast path.

### T3 — Mean reconstructed from plateau weights

`sum_j v_j * E[T_j^2] / L` must equal the streaming `mu_N` to `5e-11` absolute.
Run at every cutoff where `v_j` is built.

### T4 — Regression against the known run

Must reproduce exactly (these are measured, not targets to fit):

| `N` | `Q(N)` | `M(N)` | `E_N(M)` | `mu_N` |
|---|---|---|---|---|
| 5,000,000 | 3,039,633 | −709 | 0.029515 | 0.548482 |
| 50,000,000 | 30,396,344 | −908 | 0.029733 | 0.553360 |
| 100,000,000 | 60,792,694 | 1,928 | 0.029641 | 0.558440 |
| 150,000,000 | 91,189,087 | 1,089 | 0.029536 | 0.557670 |
| 200,000,000 | 121,585,426 | 320 | 0.029772 | 0.558240 |
| 250,000,000 | 151,981,736 | −982 | 0.029944 | 0.559410 |
| 300,000,000 | 182,378,126 | −592 | 0.029662 | 0.559890 |
| 350,000,000 | 212,774,472 | 2,896 | 0.029508 | 0.562260 |
| 455,052,511 | 276,638,778 | −5,414 | 0.029334 | 0.566280 |

Full precision at `N = 5e6`:
`E = 0.0295150019629`, `mu = 0.548481916755`, `rho_E = 0.0538121696655`.

### T5 — Exact variance against the sampled variance

Print `(s - sigma_N) / SE(s)` with

```
SE(s) = (s/2) * sqrt( (kappa_hat - 1) / R ),   kappa_hat = m4 / s^4
```

(delta method: `Var(s) ≈ sigma^2 (kappa-1)/(4R)`).
Reference point: with seed `19092026` and `R = 8200` at `N = 5e6`, the measured
`s = 0.350499677391`. The corrected asymptotic gives `0.350195` (0.07 SE away).
**The exact `sigma_N` must land at least as close.** If `|z| > 4`, abort: the factorisation
is wrong and every variance-derived number in the paper is void.

### T6 — Asymptotic mean check

At the full file, with `m = 276638778`, `S = -5414`, `L = 13.0281681`, `t = 0.1059512`:
`mu^asym = 0.566195`, measured `mu_N = 0.566280`, relative discrepancy `≈ 1.5e-4`.
Print the discrepancy column at every cutoff; it should stay at the `1e-4` level.

---

## 6. Layer II — Monte Carlo ladder (measurement, never proof)

Cutoffs: `1e4, 3e4, 1e5, 3e5, 1e6, 5e6`. Per-cutoff time budget configurable; default
allocate more draws to the cheap small cutoffs (cost per draw scales like `m`, hence like `N`).

Sampler: `baseSigns = [ones(p,1); -ones(q,1)]`, `order = randperm(m)`,
`T = cumsum(baseSigns(order))`, `E = dot(v, T.^2)/L`. This is exactly uniform on the class.

Per cutoff report: `R_N`, `H_N = #{E(pi) <= E_N(M)}`, `Phat = H/R`, two-sided Wilson interval,
and when `H = 0` the exact one-sided bound `1 - alpha^(1/R)`; plus sample mean, sample SD,
minimum, quantiles 1 % / 5 % / 50 %, and the standardised errors against the exact `mu_N`
and `sigma_N`.

Model comparison, using the **exact** `sigma_N` (not the sample SD):

```
nu_N  = 2*mu_N^2 / sigma_N^2
Pchi2 = gammainc( nu_N * E_N(M) / (2*mu_N), nu_N/2 )     % lower regularised; no toolbox
expected hits = R_N * Pchi2
P(H=0)        = (1 - Pchi2)^R_N
```

Control values (verified): `1 - 0.05^(1/2800) = 0.0010693322`;
`1 - 0.05^(1/9500) = 0.0003152905`; `(1 - 0.00428)^2800 = 6.084e-6`; `9500*0.00428 = 40.66`.
At `N = 5e6` with `nu ≈ 4.90`, `Pchi2 ≈ 2.0e-3`, expected hits in 8200 ≈ 16.5,
`P(H=0) ≈ 6.6e-8` — i.e. the two-moment model is rejected. Record that as a **negative
result**: exact mean and variance do not determine this lower tail.

Write all sampled energies to CSV (one row per draw, per cutoff).

Caveat to state in the paper: MT19937 carries 19937 bits of state against
`log2|Omega| = 3.04e6` bits at `N = 5e6`, so the generator cannot reach the whole class.
Irrelevant for a bound at the `1e-4` level — only the marginal law of the statistic matters —
but a referee will ask.

---

## 7. Layer III — OU–LDP heuristic (must be labelled)

Print every line of this section under the literal banner

```
OU_LDP_HEURISTIC — NOT A FINITE-N THEOREM
```

Compute with no hand-entered constants:

```
d   = 6/pi^2
L_N = log(N/N0)
a_N = zeta(2) * E_N(M)                 % = rho_asym
I_N = (a_N - 1)^2 / (8 * a_N)
P_OU= exp( -I_N * L_N )
```

Verified control values:

| `N` | `L_N` | `a_N` | `I(a_N)` | `P_OU` |
|---|---|---|---|---|
| 5,000,000 | 8.5171932 | 0.0485502 | 2.330722 | 2.3918e−9 |
| 350,000,000 | 12.7656884 | 0.0485387 | 2.331322 | 1.1886e−13 |
| 455,052,511 | 13.0281681 | 0.0485250 | 2.346573 | 5.2834e−14 |

### 7.1 Test statistic — residual, not slope

Do **not** make the slope regression the primary test. Report

```
delta_N = log(Phat_N) + I(a_N) * L_N
```

using the exact per-cutoff `a_N` (never a fixed `I = 2.34`). If the heuristic holds with an
O(1) prefactor, `delta_N` is **bounded**; if `delta_N` drifts linearly in `L`, the rate is
wrong. This is a cleaner discriminator than a fitted slope and does not assume `I` constant.

Secondary: binomial maximum likelihood over all ladder cutoffs, including those with `H = 0`
(their likelihood `(1-p_N)^{R_N}` is informative), with `log p_N = b - beta*L_N`.
Report the profile-likelihood interval for `beta`, not just the point estimate, and compare
to `I(a_N)`.

Honest limitation to print and to state in the paper: the LDP is asymptotic in `L`, while
Monte Carlo only has power where `L` is small. At `L = 8.52` the measured local slope between
the 5 % and 1 % sample quantiles was `−10.5` against the predicted `−8.52`, a 23 % bias; at
`L = 2.3` it will be worse. **The ladder tests the form, it does not fix the constant.**

### 7.2 Entropy statement

Report, clearly inside the heuristic banner:

```
Sigma_N^<=( E_N(M) ) - log|Omega_N^(1)| = log P_E(N)  ≈  -I(a_N) * log(N/N0)
```

using the **cumulative** entropy, not the window form. The window version with `delta_N -> 0`
tends to `-inf` trivially and must be retired from the paper.

---

## 8. Outputs

- Console: three clearly banner-separated sections (I, II, III).
- CSV: `exact_layer.csv`, `montecarlo_ladder.csv`, `sampled_energies.csv`, `heuristic.csv`.
- MAT: everything, plus the reproducibility record of §0.5.
- LaTeX fragment written **twice**, as `..._insert.tex` and `..._insert.txt`
  (identical content; the `.txt` copy is a standing project requirement).

### LaTeX fragment contents, by claim status

| environment | content | status |
|---|---|---|
| `theorem` | exact `mu_N` (with `E[T_j^2] = j + mu2 j(j-1)`) | proved |
| `theorem` | exact `sigma_N^2` via `Cov = phi(j) psi(k)` | proved |
| `remark` | verification record: T1 exhaustive enumeration, `psi(m)=0`, `E T_m^2 = S^2`, `E T_m^4 = S^4` | proved |
| `corollary` | `mu_N ~ d(1-(1-t)/L)`, `sigma_N^2 ~ 4d^2(L-2.5)/L^2` | approximation, with measured accuracy |
| `experiment` | certified table of `Delta_N` with `|Delta|/eps` | deterministic + a priori bound |
| `proposition` | `E_N(M) < mu_N` at all listed cutoffs | conditional on IEEE-754 |
| `experiment` | ladder: `R, H, Phat`, intervals | statistical |
| `remark` | **negative result**: two moments do not determine this tail; chi-square model rejected at `6.6e-8` | measured |
| `heuristic` | `I(a) = (a-1)^2/(8a)`, `P_OU` table, residual test | explicitly not a theorem |
| `warning` | a small percentile is **not** a selection principle | required |

### The three required additions to the manuscript

1. **`warning`**: the null is exchangeable, so a typical member has `|T_j| ~ sqrt(m) ≈ 1700`
   at `N=5e6`, while `|M(n)| ≈ 0.17 sqrt(n)`. `P_E` therefore measures amplitude and nothing
   else; any sequence with that amplitude gives the same `P_E`, and the amplitude is already
   known to be `sum_rho |rho zeta'(rho)|^-2`. Without this the strongest-looking number in the
   paper is the easiest to attack.
2. **Weak Mertens identification**: `E_{N0,N}(M) = O(1)` as `N -> infinity` *is*
   `∫_1^X (M(t)/t)^2 dt << log X`, which implies RH and simplicity of all zeros. The
   manuscript's "does the limiting energy exist?" question is that conjecture under another
   name. *Attribution cited from memory — Cramér; Titchmarsh §14.27; Ng (2004), already in the
   bibliography. Verify against the local library before submission.*
3. **Retire** the window form of the entropy-deficit question in favour of the cumulative
   form of §7.2; state explicitly that it supersedes, do not let both stand.

---

## 9. Items this spec does not verify

- The weak-Mertens attribution above (from memory).
- The OU scaled cumulant generating function
  `Lambda(lambda) = (theta - sqrt(theta^2 - 2 lambda sigma^2))/2`, from which
  `I(a) = (a-1)^2/(8a)` follows by Legendre transform at `theta = 1/2, sigma = 1`.
  Only `Lambda'(0) = sigma^2/(2 theta)` was checked.
- The transfer of the LDP from the finite permutation class to the continuous OU limit
  (bridge invariance principle plus an interchange of limits; the bridge adds an O(1)
  boundary correction to the exponent). This is the named unproved step.
- Whether the small ladder cutoffs will produce any hits: that depends on `a_N` at
  `N = 1e4 .. 1e6`, which has never been computed. The script must compute `a_N` first and
  derive the prediction from it — never assume `I = 2.34`.
- The Java SHA-256 invocation.
- Bit-exact reproduction of the Monte Carlo regression numbers requires an identical sequence
  of RNG calls. If the sampler is restructured, downgrade T4's MC part to: sample mean within
  4 SE of `mu_N`, sample SD within 4 SE of `sigma_N`.
