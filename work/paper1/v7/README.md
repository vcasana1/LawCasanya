# Prime-corrected clock — complete article, v7

The manuscript is `manuscript/prime_corrected_clock_v7.tex`; the `.txt` is a
byte-identical copy and the `.pdf` the compiled article (47 pages: numbered
equations, contents, internal links, citation back-references and hover
previews of internal references).

## Compile

Requirements: Python 3 and TeX Live with pdfLaTeX and the usual packages
(Latin Modern, AMS, natbib, hyperref, bookmark, pdfcomment, listings, geometry,
enumitem, longtable, booktabs, microtype). `texmf/` supplies elsarticle,
tracklang and soul with their licence notices.

```sh
python tools/build_v7.py      # 6 pdfLaTeX passes, hover previews, diagnostics, TXT copy
python tools/check_pdf_v7.py  # links, tooltips, labels; writes audit/pdf_checks.json
```

`tools/patch_v7_claude.py` regenerates the v7 source from the v6 source
(`../v6/manuscript/prime_corrected_clock_v6.tex` copied to the v7 file name);
every replacement is asserted to match exactly once.

## Numerical confirmations (unchanged from v5/v6)

```sh
python -m pip install -r requirements.txt
python code/opc_envelope_coefficient_v14.py outputs
python code/opc_envelope_iterations_p1.py outputs
python code/verify_envelope_intervals_v5.py outputs
```

`audit/numerical_manifest.json` lists programs, parameters and outputs. No zero
ordinate is read and no numerical value selects a construction or parameter.

## Source checks

`audit/source_audit.json` records, for each reference, what was read and where.
In v7 the cited passages were checked in the author's library (file names
recorded). Not available: Fujii 1981 (Part II, corrections to Part I) and
Korolev 2016 (Lemma 3.13 is cited through Ivić–Korolev 2018, Lemma 12, p. 16).

## Changes from v6 (Claude, 2026-10-19)

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
