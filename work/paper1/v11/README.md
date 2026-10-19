# Prime-corrected clock — complete article, v11

The manuscript is `manuscript/prime_corrected_clock_v11.tex`; the `.txt` is a
byte-identical copy and the `.pdf` the compiled article (61 pages: numbered
equations, contents, internal links, citation back-references and hover
previews of internal references).

## Compile

Requirements: Python 3 and TeX Live with pdfLaTeX and the usual packages
(Latin Modern, AMS, natbib, hyperref, bookmark, pdfcomment, listings, geometry,
enumitem, longtable, booktabs, microtype). `texmf/` supplies elsarticle,
tracklang and soul with their licence notices.

```sh
python tools/build_v11.py      # 6 pdfLaTeX passes, hover previews, diagnostics, TXT copy
python tools/check_pdf_v11.py  # links, tooltips, labels; writes audit/pdf_checks.json
```

`tools/patch_v11_claude.py` regenerates the v11 source from the v10 source
(`../v10/manuscript/prime_corrected_clock_v10.tex` copied to the v11 file name);
every replacement is asserted to match exactly once. v10 comes from v9 by
`../v10/tools/patch_v10_claude.py`, v9 from v8 by
`../v9/tools/patch_v9_claude.py`, v8 from v7 by
`../v8/tools/patch_v8_claude.py`, v7 from v6 by `../v7/tools/patch_v7_claude.py`.

## Numerical confirmations

```sh
python -m pip install -r requirements.txt   # mpmath; scipy/numpy for the disc scan
python code/envelope_best_profile_v9.py 3000 outputs   # Theorem E hull, interval arithmetic (v9)
python code/envelope_disc_scan_v9.py 3000 outputs      # Backlund disc scan, floating point (v9)
python code/opc_envelope_coefficient_v14.py outputs
python code/opc_envelope_iterations_p1.py outputs
python code/verify_envelope_intervals_v5.py outputs
```

`audit/numerical_manifest.json` lists programs, parameters and outputs. No zero
ordinate is read and no numerical value selects a construction or parameter.

## Source checks

`audit/source_audit.json` records, for each reference, what was read and where.
In v8 and v9 the cited passages were checked in the author's library (file names
recorded). Fujii 1981 and Korolev 2016 were read in the original in v8.

## Changes from v10 (Claude, 2026-10-19)

Applied by `tools/patch_v11_claude.py` to a copy of the v10 source.

- Theorem D'' (`thm:fixed_cutoff_step`, Section 7): for (log log T)^{-1/2} <= c <= 1/2 the one-step
  clock from tau_k has <r_k(T^c)^2>, <t_k(T^c)^2> << 1 + log log log T and height error
  << (1+log log log T)/log^2 T; proof by comparison with the auxiliary cutoff T^{1/sqrt(log log T)}
  (author's argument, 2026-10-19). Remark `rem:fixed_cutoff_heuristic`: O_c(1) not proved; a
  heuristic (independence step flagged as unjustified) suggests the factor is genuine.
- Author's review of v10: Fujii (alpha') stated for 0 < h <= 1 only (the printed h∧1 form cannot be
  uniform in h: with k=1 it would contradict Selberg's second moment); F -> mathsf F in
  `lem:sampling_rho`; t_flat/t_sharp in "two good heights"; mesh step renamed mathsf h_T
  (varsigma_n is already used); notation table completed; disc wording "among the discs examined".
- ChatGPT hand-off (chatgpt/notes/regularized_clock_for_v11_20261019) integrated into the existing
  Section 9: range of Theorem D' widened to 2 <= X <= sqrt(T/2) (Lemma `lem:block_fourth`);
  moments, tails (new eq:regularized_tails) and transport (X <= T^{1/4}) stated on both I_T and the
  clock window I_T^tau; Proposition `prop:tolerance`: approximate minimizers with objective excess
  eta T keep the bounds with (1+log 1/c)^2 + eta, and an explicit primal-dual lower bound B_reg
  (quartic uniform convexity + hat-function mass matrix) certifies the excess without zeros.
- "Open problems" subsection and all Question labels removed; the sentence on uncomputed constants
  kept once (degree of proof).
- Abstract, intro (items D', D''), tables, conclusions updated.
- Independent review (separate agent): no mathematical error; wording corrections applied (sign of the
  m=1 terms, eq:SX_derivative with T∓1, 'better bound for fixed c', tolerance statement, notation
  G and A_reg, duplicated/stale sentences, B, D, D', D'' in the constants sentence).

## Changes from v9 to v10 (Claude, 2026-10-19)

Applied by `tools/patch_v10_claude.py` to a copy of the v9 source.

- New Section `sec:regularized`, Theorem D' (`thm:regularized_clock`): for 2 <= X <= T^{1/3},
  the best L^4 approximation of N_0 + S_X on [T/2, 3T] by piecewise linear functions with slopes
  in [log T/(4 pi), log T/pi] is unique and computed without zeros; its level points are
  increasing with gaps in [pi/log T, 4 pi/log T] and
  <|x_k - gamma_k|^4> << (1 + log(1/c))^2 / log^4 T (one step, fixed cutoff);
  max |x_k - gamma_k| << T^{1/5}; for X <= T^{1/4} the transport S_X(gamma_k) - S_X(x_k) is
  bounded in mean square. Lemmas: Theorem A for Lipschitz models; a slope-constrained model of N
  (Fujii's 8th moment); fourth moment of the prime model on the block.
- Attribution: the clock is the RvM main term inverted by Lambert's W (Corless et al.); the
  corrected equation is no longer called "LeClair's equation"; LeClair solved it numerically.
- Gonek, Trans. AMS 364 (2012): the zeros of zeta_X (on the line, Thm 6.2) solve the corrected
  clock equation with smoothed weights; added to the comparison and to tab:evaluates.
- Abstract, intro (item D'), tables, conclusions, Question q:fixed_c updated.
- Independent review (separate agent): mathematics of D' confirmed; corrections applied —
  shifts h > 1 in Lemma slope_envelope handled by Selberg's moments (Fujii only for h <= 1);
  ranges X <= T^{1/3} (D') stated wherever D' is compared; "without Newton iteration" instead of
  "one step"; Gonek's zeta_X called functions built from finite Euler products; mesh stated in
  the abstract; t_sharp <= 3T - C_g - 1; notation (nodes t_i, L_T, t_flat, t_sharp); constants.

## Changes from v8 to v9 (Claude, 2026-10-19)

Applied by `tools/patch_v9_claude.py` to a copy of the v8 source.

External review of v8 (six points, all checked and accepted)
1. `lem:sampling_rho`: the constant 7 was not uniform in r; now
   4rb(1+log X) <= 2pi(1+1/log 2) log T/log(3T) < 16, factor 8 -> 17.
2. `lem:higher_moments`: the m=2 term is C sqrt(r) T^{1/4r} (from ((2r)!)^{1/4r});
   absorbed by C r^2.
3. `lem:zero_pairs`: case 2Rb >= T separated; otherwise h = max(1,2Rb) <= 4Rb.
4. `prop:deformation`: remainder T^{c_2-1}/log T (not T^{c_1-1}); the o(1) is
   quantified, ||(d_2-d_0)/d_0||_4 << c_2 + c_1 c_2 + T^{-1/2} log^3 T << c_2.
5. `cor:sorted_clock`: construction on J_T = {k : T/2 <= tau_k <= 3T}.
6. Sentence on the "fixed final cutoff" replaced: the limitation concerns the
   one-step clock only.

Theorem E
- Convex hull of published exponent pairs: Bourgain 2017, Heath-Brown 2017 (Thm 2,
  m <= 3000) and their A-images (j <= 25): C_P = 0.0966530245541..., 
  limsup|tau_k - gamma_k| <= 2 pi C_P < 0.6072889 (v8: 0.6083074).
- Remark: with the pairs of the preprints Trudgian-Yang (arXiv:2306.05599, Lemma 1.1)
  0.6061342; with Tao-Trudgian-Yang (arXiv:2501.16779) 0.6060224. Not in the theorem.
- One Backlund disc cannot go below 0.4940172 (Lindelof profile); a scan of the discs
  finds the infimum at the corner used in the proof; on LH S(t) = o(log t)
  (Titchmarsh-Heath-Brown Thm 13.6(A), p. 333), so 0.494 is a floor of the method.

Comparison with França-LeClair and LeClair (read in the originals)
- França-LeClair, CNTP 9 (2015): exact equation (20) p. 11 with arg zeta; Lambert
  formula (63) p. 24 = the clock; numerical solutions evaluate arg zeta (§7.1 p. 28).
- LeClair, Symmetry 13 (2021) 2014 = arXiv:1601.00914v1: equation (49) p. 18 with the
  first N primes is the corrected clock equation with X = p_N up to 1/(48t); accuracy
  estimated against Odlyzko's zeros (Table I p. 19) and argued from S(t) = O(1)
  (Prop. 4 p. 12), incompatible with Selberg's normal law.
- New Table `tab:evaluates` (what each approximation evaluates; what is proved);
  column "evaluates zeta or zeros" in `tab:status`; row in `tab:antecedents`;
  abstract and conclusions state that the constructions and the constant of
  Theorem E use no evaluation of zeta.

Independent review of the v9 draft (separate agent): no mathematical error in the six fixes
or the hull theorem; corrections applied — range p_N <= T^{1/2} when Theorems B, D are said to
concern LeClair's equation (his N(t) < [t^2] is not covered); França-LeClair equation written
with S*(t_n) and the uniqueness assumption attributed correctly; Lindelof value in closed form
(sqrt(3)/2 - pi/6)/log 2, disc optimality labelled numerical (5 starts); Heath-Brown Thm 5
caveat for 1-sigma < 3e-7; A-B-A images computed by the program; M_X instead of sigma_X in
prop:deformation; Bellotti-Wong row and Montgomery-Vaughan wording.

References added: França-LeClair 2015, LeClair 2021, Heath-Brown 2017,
Tao-Trudgian-Yang 2025 (preprint), Platt-Trudgian 2021.

## Changes from v7 to v8 (Claude, 2026-10-19)

Applied by `tools/patch_v8_claude.py` to a copy of the v7 source.

- Fujii 1974, p. 225, read on the page image: the Main Theorem has non-strict
  inequalities, T^{1/2+a_2} <= H <= T. v7 stated (from the OCR layer) that the
  inequalities are strict and that v6's a_2 = 1/4 was outside the range; that
  statement was wrong and is removed. Lemma `lem:selberg_uniform` now uses H = T
  directly (a_2 = 1/5).
- Fujii 1981 (Part II) read: its corrections to Part I (h bounded; error (Ak)^{2k};
  Lemma 2 and Lemma 3 remainders; items (iii), (iv) of p. 234) are listed and do not
  touch Selberg's formula on p. 232 or the bounds on p. 233.
- Difference moments: Theorem `thm:known_fujii_difference` is now Fujii 1981, (alpha'),
  valid for every h > 0 with h ^ 1; Titchmarsh-Heath-Brown (9.25.3) states 0 <= h <= T/2,
  while Fujii 1981 requires h bounded in the asymptotic formula.
- Korolev 2016 read: Lemma 3.13 (p. S126) has the bound (c0/56)(c0 k)^{2k} H; the
  quotation in Ivic-Korolev 2018 omits k^{2k}. Remark `rem:korolev_uniform` corrected:
  the route gives (Ck)^{2k}, not (C sqrt k)^{2k}.

## Changes from v6 to v7 (Claude, 2026-10-19)

Mathematics
- Selberg's approximation uniformly in the order: Theorem `thm:known_fujii_selberg`
  states Fujii's §3 bound literally (0 < a_2 < 1/4 strict; v6 used a_2 = 1/4,
  outside Fujii's range); new Lemma `lem:selberg_uniform` derives the bound with
  Y_k = T^{1/(80k)} on [T,2T] (a_2 = 1/5, two halves with H = T/2, lengthening
  of the prime sum by Montgomery–Vaughan, range 1 <= k <= log T/(300 log 2)).
  Remark `rem:korolev_uniform`: independent route through Korolev's Lemma 3.13,
  with the bridge to the cut T^{1/(80k)}, the short intervals and the range of orders.
- Fujii's difference moments taken from Titchmarsh–Heath-Brown (9.25.3) (after
  Fujii, Bull. AMS 1975), uniform in 0 <= h <= T/2.
- Lemma `lem:higher_moments`, Theorem `thm:tails` (C_8 = max(300,7C),
  lambda_0 = max(4C, C_8(C_9+1)^{2/3})) and Theorem `thm:uniform_iteration`
  carry the range of orders 2r <= kappa_F log T explicitly.
- Lemma `lem:sorted`: only the rearrangement inequality and the multiset are
  claimed; sorting removes strict inversions, not coincidences; no claim about
  continuing the iteration from sorted points (weights attached to the index).
- Remark `rem:newton`, Question `q:fixed_c`: for fixed c the residual is bounded
  in mean square iff the transport is; c^2 log log T is an upper bound, the
  heuristic is labelled as such.
- Theorem `thm:uniform_iteration`, last step: the transport is bounded without
  the factor L(tau_k); statement says the constants C_star, H^* are not computed.
- Second step: L(x^(1)_k) = (log T/2pi)(1 + O(1/log T)).
- Proposition `prop:rounding`: the conclusion is stated for times t, not ordinates.
- BW(t) defined (both bounds of Bellotti–Wong, Thm 1.1).
- Corollary `cor:dichotomy`: "bounded" means sup over T >= T_0.
- Corollary `cor:sorted_clock`: indices outside I_T handled explicitly.
- Notation: forward difference written nabla_k (Delta_k stays the Gram
  displacement); Backlund's variation of the argument written out; erratum
  x^(1)_k = x^(1)_k corrected.

References
- Korolev, Publ. Inst. Math. 2012: Lemma 2.4 (p. 60), Theorem 3.2 (p. 67),
  Theorem 4.2 (p. 73); v6 attributed them to the Izv. paper as "Lemma 4 / Thm 2".
  Keys renamed KorolevPIM2012 / KorolevIzv2012.
- Added Fujii 1975 (Bull. AMS 81, DOI 10.1090/S0002-9904-1975-13674-3);
  Korolev 2016 English DOI 10.1134/S0081543816030019; Lerner 2013 preprint
  replaced by Di Plinio–Lerner, J. Lond. Math. Soc. 90 (2014), DOI 10.1112/jlms/jdu049.
- Removed Radziwiłł 2011 and the attribution to Tsang's thesis p. 60.
- Titchmarsh–Heath-Brown (9.25.4) described as bounding gap moments of every fixed order.
