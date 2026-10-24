# Audit of the 130 review items against version 25

Status: **done** = incorporated before this audit; **completed** = missing or partial at the audit and
completed in this pass; **kept** = checked and left as is, with the reason.  Places: the manuscript
`rvm_zeta_pi_mertens_v25.tex` (by section, experiment, figure or table) and the programs in `code/`.

| No. | Item | Status | Where / what |
|---|---|---|---|
| 1 | Ordinate table precision | done | Caption of Table tab:clock-1000; appendix intro: differences from unrounded values |
| 2 | Double bars for scalars | done | No double bar used for scalars; all remaining double bars are norms |
| 3 | Automated table checks | completed | `s15` reads each written table back: indices 1..1000 once, rounding consistency; sentence in Appendix A intro |
| 4 | First-crossing definition near the table | done | Caption of Table tab:primes-1000 (inf{x : pi_RVM(x) >= j}, grid step 5.9e-6) |
| 5 | Decimals vs grid accuracy | done | Same caption: first grid point, linear refinement, grid step |
| 6 | Sensitivity of first crossings | completed | `s15` compares with the levels of `s04` (other truncation and grid); median 1.7e-3, 29 of 168 levels > 0.01, 0.85 at j = 148, 118, 106 (near-tangent local maxima); in the caption |
| 7 | Full formula in difference headings | completed | `pi_RVM(n)-pi(n)`, `M_RVM^crit(n)-M(n)` |
| 8 | pi_RVM is real-valued | done/completed | Table caption; notation table now says "real-valued, not an integer count" |
| 9 | Exact vs approximate Mertens columns | done | Caption of Table tab:mertens-1000; differences from unrounded values |
| 10 | Ambiguous "diff" headings | done | Full formulas |
| 11 | Silent truncation of the data files | done | `load_ordinates` raises on different lengths |
| 12 | Finite, ordered, positive data | completed | Positivity and `tau_1 > 2 pi` added to the finiteness/monotonicity checks |
| 13 | Binary layout and size | completed | `read_bin` checks size multiple of 8; little-endian float64 documented |
| 14 | Newton without stopping test | done | `clock_inverse`: relative-step test, RuntimeError on failure |
| 15 | Safeguarded Newton | done | Bracketed Newton with bisection fallback on U > 2 pi |
| 16 | q/tau^2 vs q/(1/4+tau^2) | done | `tail_coefficients` docstring, approximation (iii) and its order |
| 17 | Tail remainder bound | done | Orders of (ii)-(iv) with the bound 1e-10 for the file |
| 18 | Error budget of the product | done | Docstring (i)-(iv); evaluation checks in `s02`; Experiment exp:transition |
| 19 | Principal logarithms | done | Docstrings of `Product` and `logG` |
| 20 | Phase-sensitive use of logarithms | completed | Docstring: logP and logG enter only through exp or real parts (checked: no program reads a phase) |
| 21 | Moebius sieve tests | done | Self-test against mu(0..12) |
| 22 | Empty blocks in s01 | done | Blocks clipped to N |
| 23 | Unstable relative error | done | Balanced metric printed and in the CSV |
| 24 | np.real without check | done | Imaginary residual printed before discarding |
| 25 | "Bounded displacement" title | done | "Observed displacements in the supplied range" |
| 26 | "Distribution" | done | "Empirical distribution of the supplied displacements" |
| 27 | Hard-coded zoom offsets | done | Offsets computed from the file |
| 28 | S(T)+O(1/T) label | done | Label `N_file(T) - N_RVM(T)` and the completeness condition |
| 29 | Richardson model | done | Called empirical; other heights and linear model tested |
| 30 | Imaginary part of the extrapolation | done | Kept complex; tolerance 1e-8 |
| 31 | Computed residual | done/completed | Figure caption and Experiment exp:transition |
| 32 | Manual rows index | done | Dictionary keyed by sigma' |
| 33 | "Stays O(log N)" | done | "observed ... compared with log N" |
| 34 | Maximum over sampled N | done | Maximum over all N (3.58, 3.98, 3.96, 4.53, 10.34) |
| 35 | Landau convention | completed | Experiment exp:expsums cites Theorem thm:known-landau, error O_x(log T), "illustrative" |
| 36 | Height-transform normalisation | done | Comment linked to eq. (MH-RVM) |
| 37 | Exact loop with 300 terms | done | `ke = min(KE, size)` |
| 38 | Assertion on min abs(w) | done | Printed: 377.0 (not 400) |
| 39 | Ei remainder | done | DLMF 6.12(i) bound printed (1e-8) and sample comparison (1.2e-9) |
| 40 | Recurrence drift | done | Measured at every reset (6e-9) |
| 41 | Interpolation in u | completed | `s04` repeats the inversion on the double step: 5.2e-5 (error about 2e-5); sentence in Experiment exp:primes |
| 42 | Sieve size 64 | done | Size from the grid |
| 43 | Fixed 39 exponents | done | Loop while 2^m <= x_max |
| 44 | Monotonicity on the grid | done | "increasing on the sampled grid" |
| 45 | Factor 2.5 | done | Resonance explanation in the code |
| 46 | pi_RVM(1) = 0 | done | Stated in code and console |
| 47 | Sum of cell masses | done | Printed as pi_RVM(1000), separately from pi(1000) |
| 48 | argmax without crossing | done | `first_crossing` raises if not reached |
| 49 | Grid crossing labelled as equality | done | Figure titles "first grid crossings"; linear refinement |
| 50 | Sign (-1)^k | completed | Derivation in the code; unit test: central difference of P/G agrees to 7e-11, k <= 6; in Experiment exp:mertens |
| 51 | Modelled residues | completed | Orange points in Figure fig:explicit; sensitivity to fit range and model form: <= 5.2e-6 |
| 52 | zeta' validation | done | Spot checks across the whole range (<= 2.3e-5) and numerical-differentiation check |
| 53 | Truncated spectral sums | done | Wording in code and paper |
| 54 | Six trivial terms | done | Five and seven terms compared at x = 2 |
| 55 | Exclusion width 0.05 | done | RMS for 0.02, 0.05, 0.10 |
| 56 | Target validation near 1e6 | done | 100 integers <= 1e5 and 34 in [9e5, 1e6] |
| 57 | Target terminology | done | "tapered-and-interpolated target" |
| 58 | "Within +-1 step" | done | Observed maximum 2.62 / 1.65 |
| 59 | Correlation slices | done | [1:] throughout |
| 60 | Errors in the normalised maxima | completed | Values labelled for the target with its error sources; Figure fig:mertens caption |
| 61 | VARPI copied by hand | done | Read from `output/s02_varpi.txt` |
| 62 | K <= N | done | Filtered |
| 63 | Finite-data consistency | done | "internal check of two computations built on the same clock" |
| 64 | Approximate denominator | completed | "auxiliary approximation" in Experiment exp:product-identity |
| 65 | Truncated flow integral | completed | "truncated to k <= N", "truncated flow integral" |
| 66 | Invalid Python in s08 listing | done | All listings are `\lstinputlisting` of the repository files |
| 67 | Bump quadrature | done | Check with half the nodes: 4e-13 / 6e-13 |
| 68 | s08 input length | done | Length validated |
| 69 | k >= k0 slicing | done | Slices corrected |
| 70 | Noise floor | done | Printed note; paper wording |
| 71 | Separate convergence studies | done | Moment order, cumulative k, quadrature nodes in the console |
| 72 | Extended lambda range | done | "numerical prolongation"; positivity and ordering reported |
| 73 | Poisson series not summed | completed | Console note in `s09`; sentence in Experiment exp:clock-defect; `s09` length check |
| 74 | Accepted non-decreasing steps | done | Step accepted only on decrease; band stops otherwise |
| 75 | Normal equations | done | QR/SVD (`scipy.linalg.lstsq`) |
| 76 | Undefined iteration variable | done | Initialised |
| 77 | Von Mangoldt helper | done | Trial division up to sqrt(n) |
| 78 | Reproducibility table | done/completed | Versions and order in Appendix B; `code/requirements.txt` pinned |
| 79 | Data precision | completed | Appendix B: one ulp = 2.3e-10 at the top of the files |
| 80 | Slow vertical limit at sigma' = 0.25 | completed | Experiment exp:transition: 0.143, 0.025, 1.6e-5 at t = 1e4 |
| 81 | Diamond 1970 | done | pp. 12-28, DOI |
| 82 | Uniform bibliography style | completed | One style for all 85 entries (title, journal in italics, DOI link, then arXiv) |
| 83 | DLMF version | done | Release 1.2.8 of 2026-09-15 |
| 84 | Hormander1990 | done | Entry present with DOI |
| 85 | zeros.py precision | completed | Comment: double precision intentional, diagnostics only |
| 86 | Gonek root detection | done/completed | Cells with jumps > 1 level detected and resolved; max level change per cell printed (0.010); comment corrected |
| 87 | Taper clipped at 0 | done | `np.maximum(w, 0)` |
| 88 | Sorting after optimisation | done | Inversions counted (0); monotone matching lemma |
| 89 | Tolerances 1e-15 | kept | Documented; termination status printed (changing them would alter the iterate on which `cert7` depends) |
| 90 | Frozen tail | completed | Code comments in `horizon*.py`; sentence in the receding-horizon paragraph |
| 91 | CERTIFIED | completed | `cert5.py`, `cert6.py` relabelled `FLOAT_PASS` and rerun; paper text updated in two places |
| 92 | np.linalg.inv | completed | LU solve and defect d0 in all three certificate programs; d0 in eq. (rb-num-banach) |
| 93 | Radii at machine precision | completed | Fragility stated; stability measured by the sampled margin (1e-2 to 1e-4) |
| 94 | k(r) = 0.00 | completed | Scientific notation in `cert5`, `cert6` (and `cert7`) |
| 95 | Conditional reuse of C3 | completed | Recomputed for every radius in all three programs |
| 96 | Sampled margin | completed | "sampled margin" in the text, table header and equation |
| 97 | Zeta ordinates in certificate scripts | completed | `cert7` reads none (`diag_cert7_gamma.py`); `cert5`, `cert6` use them only in a final diagnostic block |
| 98 | Hashes and parameters | done | `RESULTS.txt` with SHA-256 of programs and files |
| 99 | Works/fails definitions | done | Status criteria in `RESULTS.txt` |
| 100 | Scaling laws | completed | Slopes with standard errors: 1.81 +- 0.10, 2.10 +- 0.06, -2.08 +- 0.06 |
| 101 | t-independent constant | done | Proposition prop:rung-apriori: uniform over classes with bounded data |
| 102 | sum kappa_k^-2 | done | Explained why it is listed separately |
| 103 | Distributional signs | done | Laplace transform of S_kappa computed with the delta_0' correction |
| 104 | Laplace convention | done | Stated before the proposition |
| 105 | Choice of eps_0 | done | eps_0 = sigma_0 - 3/2 < 2 sigma_0 - 3 |
| 106 | Constant B_2 | done | In terms of the mass constant for the fixed eps_0 |
| 107 | Derivative of n^(1/2-s)/log n | done | Written out |
| 108 | Normalisation of C_t | done | e^(2b(s-2)), all factors at s = 2 |
| 109 | Order at most one | done | "order at most 1" |
| 110 | Right half-strip | done | 2 <= Re s <= 4 |
| 111 | Symmetry and conjugation | done | Both steps written; G is not symmetric, handled by the G-ratio bound |
| 112 | Incomplete PL sentence | done | Removed |
| 113 | Growth u(s) | done | O(abs(s)^(1+eps)) |
| 114 | Compact part of the strip | done | Bottom side bound 5 sum kappa^-2 + c_7; part of the boundary |
| 115 | Zeros on Jensen's circle | done | Rudin Thm 15.18 |
| 116 | Constants T+6, T+8 | done | Stated as coarse bounds |
| 117 | Right continuity | done | T in {kappa_k} by right continuity |
| 118 | Quantile comparison | done | Intermediate inequalities for F_b on x >= x_b |
| 119 | Drift-corrected remainder | done | Intermediate point s_k kept; drift-corrected clock tau_k^(b) |
| 120 | b = 0 separated | done | Corollary cor:rung-apriori-b0 |
| 121 | Initial indices | done | Uniform placement of kappa_k from the count bound |
| 122 | Scope remark | done | "uniform drift-corrected class" |
| 123 | Finite tested linear system | done | Wording |
| 124 | Normalisation and weights | completed | Bump of unit integral, frequency grids, block weights stated |
| 125 | Optimiser data | completed | Tolerances, evaluation limits, numerical rank, condition number, active bounds (printed by `s13`, in the text) |
| 126 | Different initialisations | completed | Three perturbed starts at N = 50: comparable residuals, different near-solutions |
| 127 | Active box constraints in figures | completed | Figure 17 circles masses at the box (none with n <= 15; listed in the legend); Figure 16 legend counts them |
| 128 | Section sizes | completed | Equations, blocks, ordinates, masses in both legends |
| 129 | Boundary masses | completed | Legend and caption: all masses n <= 15 shown; edge masses outside the range |
| 130 | Final status | completed | Status paragraph divided into Proved / Numerical evidence / Open |

Found during the audit and corrected: the stale Richardson value 0.9619415807 in Experiment exp:varpi-bound and in
the list of open points (now 0.9619415789, agreement 2.1e-11 with `s14`); `s14` now reads the Richardson value from
`output/s02_varpi.txt`; the nested section N = 100 does not reach small residuals in the reproducible run (text
rewritten); a stray parenthesis in the `s08` console; the tooltip generator now handles `\texorpdfstring`.
