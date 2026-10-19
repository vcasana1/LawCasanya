# Prime-corrected clock — complete article, v9 (final)

The manuscript is `manuscript/prime_corrected_clock_v9.tex`; the `.txt` is a
byte-identical copy and the `.pdf` the compiled article (51 pages: numbered
equations, contents, internal links, citation back-references and hover
previews of internal references).

## Compile

Requirements: Python 3 and TeX Live with pdfLaTeX and the usual packages
(Latin Modern, AMS, natbib, hyperref, bookmark, pdfcomment, listings, geometry,
enumitem, longtable, booktabs, microtype). `texmf/` supplies elsarticle,
tracklang and soul with their licence notices.

```sh
python tools/build_v9.py      # 6 pdfLaTeX passes, hover previews, diagnostics, TXT copy
python tools/check_pdf_v9.py  # links, tooltips, labels; writes audit/pdf_checks.json
```

`tools/patch_v9_claude.py` regenerates the v9 source from the v8 source
(`../v8/manuscript/prime_corrected_clock_v8.tex` copied to the v9 file name);
every replacement is asserted to match exactly once. v8 comes from v7 by
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

## Changes from v8 (Claude, 2026-10-19)

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
