# Möbius Project — handoff for the next manuscript version

**Current baseline:** `excursion_area_section_v39.tex`  
**Next version to create when explicitly requested:** `excursion_area_section_v40.tex`  
**Do NOT create v40 until the user explicitly orders it.**

This file is the operative handoff for the next chat. The next version must start from **v39**, not from an older version.

---

## 1. Global formatting rules — mandatory

These rules apply not only to this manuscript but to **all papers and projects with the user**.

- **Do not change the document format/layout unless explicitly ordered.**
- **Never remove equation numbers.**
- **Equation numbers must remain on the RIGHT.**
- Preserve the existing equation numbering scheme and all `\label`, `\ref`, `\eqref` machinery.
- Preserve hyperlinks in:
  - table of contents,
  - equations,
  - theorem/proposition/lemma/corollary references,
  - section references,
  - bibliography/citations,
  - URLs.
- The final PDF must preserve **hover previews** for internal references:
  - hovering over an equation reference should display the referenced equation;
  - hovering over a theorem/proposition/section reference should display the referenced content where supported by the current mechanism;
  - clicking must still navigate normally to the target.
- Do not degrade these hover previews to ordinary clickable links only.
- Preserve the internal destinations required for normal PDF navigation/back-history.
- Do not introduce visible “back” buttons unless explicitly requested.
- Do not use a left-equation-number option such as `leqno`.

### Statement classification codes

The manuscript must contain **none** of the old statement-type/novelty codes or equivalent tag system:

- `[N]`
- `[N-el]`
- `[C]`
- `[L]`

Do not reintroduce them in macros, theorem headings, tables, summaries, conclusions, or prose.

Also avoid replacing them with another coded classification system unless explicitly requested.

---

## 2. Editing policy for the next version

The user explicitly requested:

> **Correct only errors or necessary mathematical clarifications. Do not change style merely for stylistic reasons.**

Therefore:

- no global prose polishing;
- no reorganization merely to shorten or “improve flow”;
- no changes to typography, margins, theorem style, title style, section ordering, or visual identity;
- no wholesale notation rewrite;
- no automatic replacement of every `\|...\|`: distinguish scalar absolute values from genuine norms;
- no new version number unless the user explicitly says to create the next version.

---

## 3. Required changes retained from the v39 audit

These are the concrete changes to apply when v40 is ordered.

### 3.1. Replace “Its sharpest instance”

The user explicitly agrees this should change.

Current wording around the conclusions:
> `Its sharpest instance`

Preferred replacement:

> **Its smallest linear instance obtained by the counting comparison**

or an equivalent formulation that makes explicit that the threshold is sharp **only for the counting mechanism used in the paper**, not a universal arithmetic optimum.

Retain the meaning:
\[
\lambda_* = e^{\pi/\gamma_1}
\]
is the threshold of the interval-counting comparison.

Do **not** describe it as the smallest possible horizon for every conceivable method.

---

### 3.2. Correct the grammatical error near the kernel discussion

Current defective text:

> `the direct absolute-value estimate for the full kernel is, in general, can have size comparable...`

Replace by one of:

> **the full absolute kernel can, in general, have size comparable to the window length \(t-u\)**

or

> **the direct absolute-value estimate for the full kernel can, in general, be comparable to the window length \(t-u\)**

The first is preferred if it fits the surrounding sentence without further editing.

---

### 3.3. Correct the relaxed-class statement containing “exactly”

The current statement is too strong because the relaxed class does not encode all internal divisor identities of the Möbius prefix.

Replace the sentence asserting that the conditions are “exactly” the Möbius conditions by:

> **For the genuine Möbius prefix, these conditions reproduce the future-window increment constraint and the excursion-sign constraint coming from \(\mu*1=\delta_1\), but they do not impose the full family of internal divisor identities below \(u\).**

Keep the later observation consistent with this formulation.

---

### 3.4. Triple logarithm domain

For the result involving
\[
\sqrt{\log\log\log X},
\]
separate the domains.

Use the first probability bound for the stated lower range if valid, but state the triple-logarithm conclusion only for:

> **all sufficiently large \(X\)**

Do not state the triple-log expression starting merely at \(X\ge e^e\).

---

### 3.5. Continuous majorant terminology

Where
\[
\mathcal N_\square(X)
=
2+\log_2\!\left(\frac{\log X}{\log 2}\right)
\]
is introduced, describe it as a:

> **continuous increasing majorant**

of the integer counting function.

The symbol `\square` must be kept. It denotes the **square horizon**, i.e. the \(A=2\) case, not a missing glyph.

---

### 3.6. Scalar absolute values versus norms — controlled correction

This is the largest remaining notation cleanup.

For scalar quantities use absolute value:
\[
|M(t)|,\qquad
|C_h|,\qquad
|e_y|,\qquad
|K_y|,\qquad
|S_r-S_{r-1}|.
\]

For cardinalities use:
\[
|\mathcal T|
\quad\text{or}\quad
\#\mathcal T.
\]

Keep genuine vector/function/operator norms as norms, e.g.
\[
\|\mathbf D_{\mathcal T}x\|_2,
\qquad
\|x\|_2,
\qquad
\|\cdot\|_\infty.
\]

**Do not perform a blind global replacement of `\|...\|`.**
Every occurrence must be classified first as scalar absolute value, cardinality, or actual norm.

Known places from the v39 review include:
- notation table;
- excursion definition;
- terminal block;
- identity `|M(t)|=S_{r_I(t)}`;
- kernel/induction discussion;
- signed-correlation section.

---

### 3.7. Landau references must be made exact

The manuscript currently cites a broad chapter for two different counting statements.

For the next version, verify and give an exact theorem/page/equation reference for:

1. the count with
   \[
   \Omega(n)=j
   \]
   where prime factors are counted with multiplicity;

2. the squarefree count with
   \[
   \omega(n)=j
   \]
   where distinct prime factors are counted.

Do not conflate \(\Omega\) and \(\omega\).

If an exact reference cannot be verified from the source, do not invent one; leave a clearly marked citation TODO rather than make a false precise citation.

---

## 4. Recommended clarifications retained for v40

These are useful but secondary to the required corrections above.

### 4.1. Show signed identities before taking absolute values

In the linear-window corollary, explicitly display first:

\[
M(t)
=
-\sum_{d\le 5u/8}
\mu(d)
\left(
\left\lfloor\frac td\right\rfloor-
\left\lfloor\frac ud\right\rfloor
\right),
\]

and

\[
M(t)
=
-\sum_{2\le k\le t}
\left(
M(t/k)-M(u/k)
\right),
\]

before applying absolute values.

This is a clarification, not a new argument.

---

### 4.2. Averaged Chowla citation

The v39 translation is substantially improved, but in v40 give the exact page / numbered hypothesis / paragraph supporting:

- translation parameters;
- the relation between the interval start \(u_j\) and interval length \(X_j\);
- the extension from \(\lambda\) to \(\mu\).

Do not assert more uniformity than the published theorem actually states.

---

### 4.3. Uniform Fourier estimate citation

The v39 statement identifies the relevant theorem and remarks. If possible, add the exact page containing:

- the discussion after equation (1.16);
- the extension from the original logarithmic saving range to every \(0<A<1\);
- the uniformity in \(\xi\);
- the all-interval range
  \[
  x^{3/5+\iota}\le L\le x.
  \]

Again, do not invent a page number if it has not been checked.

---

### 4.4. Replace “the only new ingredient”

Current wording is too absolute.

Replace:

> `the only new ingredient`

by:

> **the additional ingredient specific to the present formulation**

or an equally non-absolute factual formulation.

---

### 4.5. Unify “complete bridge”

Where the text says `complete bridge`, use the terminology already established in the manuscript:

> **completed excursion**

or, where “bridge” is mathematically necessary,

> **completed bridge**

Prefer `completed excursion` when referring to the Möbius excursion object.

---

### 4.6. Explicit checks after the general order-\(k\) identity

After the general identity, add the brief consistency checks:

- \(k=1\): trivial truncation on \(n\le u\);
- \(k=2\): recovers the bilinear square-range truncation proposition;
- support extends to the intended \(u^k\) range.

Do not expand this into a new section.

---

## 5. Numerical section — unresolved reproducibility item

The manuscript now acknowledges that the numerical data are not reproducible from the text alone.

Still missing:

- code;
- census/result file;
- exact excursion-detection algorithm;
- zero-run convention;
- terminal-excursion convention;
- algorithms for height, area, energy and masses;
- environment/compiler version;
- cryptographic hashes;
- small-value checks;
- integer types / overflow controls.

Until those files actually exist and are supplied, **do not fabricate a reproducibility supplement**.

A safe sentence to add if not already present is:

> **The numerical data in this section are observational and are not used in any proof.**

Only add actual code/hash details when the real materials are available.

---

## 6. External results that remain sensitive

Before final submission, verify directly against the cited sources:

### Kaczorowski–Pintz 1986

Reference already identified and checked substantially:

J. Kaczorowski and J. Pintz,  
*Oscillatory properties of arithmetical functions. I*,  
Acta Mathematica Hungarica **48** (1986), no. 1–2, 173–185.  
DOI: 10.1007/BF01949062.

The v39 treatment of `(RL)` is internally coherent. Preserve the explicit chain:

\[
\text{Theorem 1}
\to
\text{Corollary 1}
\to
\text{Corollary 4}.
\]

If revisited, verify literally that the localized combined-oscillation statement transfers to \(M_0=M+2\) exactly as used.

### Pintz 2026

Current manuscript reference:

J. Pintz,  
*Oscillation of partial sums of the Möbius function and zeros of Riemann's zeta function*,  
arXiv:2608.24878v2 [math.NT], 1 September 2026.

Before final submission, check whether v2 remains the latest version and whether theorem numbering is unchanged.

### Matomäki–Radziwiłł–Tao / averaged Chowla

Preserve the distinction between:
- absolute averaged Chowla control;
- Fejér cancellation;
- small-lag contribution to the signed weighted energy identity.

They are not interchangeable.

### Uniform Fourier estimate

Preserve:
- all-interval requirement;
- uniformity in frequency \(\xi\);
- exact \(L\)-range;
- exact logarithmic-saving range justified by the cited theorem/remark.

---

## 7. Mathematical distinctions that must remain explicit

Do not undo these corrections from v39.

### Completed excursion vs open prefix

A completed excursion has integer endpoints \(u,v\) with
\[
M(u)=M(v)=0
\]
and no interior return to zero.

An open/terminal prefix is **not** automatically entitled to completed-bridge identities.

### Real arguments

Keep
\[
M(x)=M(\lfloor x\rfloor)
\]
for real \(x\), while divisor sums and excursion endpoints use integer indices as appropriate.

### Formal determination vs analytic control

Statements saying future values are “determined” by a prefix mean formal/algebraic/computational determination.

They do **not** imply cancellation or a useful analytic bound.

### Omitted prefix block

Use:

> **does not occur as a direct input**

not:

> “plays no role”.

### Deep remainder

Do not call a deep remainder “small”, “lower order”, or an “error term” merely because it depends on smaller scales.

Its size requires an independent estimate.

### No automatic descent iteration

A descended large value need not lie in the admissible localized window of its own excursion.

Any iteration must use a statement valid for arbitrary \(t\), or separately prove window admissibility.

### Signed weighted correlation total

Keep this terminology when discussing
\[
-\sum_h hC_h.
\]

Individual correlation contributions may have either sign even though the complete identity equals a positive energy quantity.

### Three distinct forms of cancellation

Keep distinct:

\[
\sum_{h<R}|C_h|=o(RL),
\]

\[
F_R=o(RL),
\]

and

\[
\sum_{h<R}hC_h=o(Q_I).
\]

One does not automatically imply the others.

---

## 8. Current interpretation of the square symbol

Do **not** replace `\square` by `sq`.

In symbols such as
\[
\mathcal N_\square(X)
\quad\text{and}\quad
Z_{\max,\square}(X),
\]
the subscript \(\square\) denotes the **square horizon**:
\[
x_{1,\nu}>x_{0,\nu}^2
\]
for square-exceptional excursions, i.e. the \(A=2\) case.

The square is intentional mathematical notation.

---

## 9. Current baseline features that must survive v40

The next version must preserve the following v39 features:

- equation numbers on the right;
- current page/layout/style;
- current TOC;
- current theorem numbering;
- all internal hyperlinks;
- bibliography hyperlinks;
- hover previews in the PDF for internal references;
- click-through navigation;
- no `[N]`, `[N-el]`, `[C]`, `[L]` classification tags;
- no reintroduction of a novelty-code legend;
- distinction between external inputs, internal deductions, heuristics and open problems through normal prose, not coded tags.

---

## 10. Output protocol when v40 is requested

When the user explicitly asks for the next version:

1. Start from `excursion_area_section_v39.tex`.
2. Apply the required changes in §3.
3. Apply the recommended clarifications in §4 only where they do not alter style/format.
4. Verify external citations only where needed for the edits.
5. Preserve all formatting rules in §1.
6. Compile repeatedly until references settle.
7. Check:
   - undefined references;
   - duplicate labels;
   - overfull boxes;
   - equation numbers still on the right;
   - TOC hyperlinks;
   - equation/reference/bibliography hyperlinks;
   - hover previews in the final PDF;
   - no `[N]`, `[N-el]`, `[C]`, `[L]` remnants.
8. Produce all three deliverables:
   - `.tex`
   - `.txt`
   - `.pdf`
9. Ensure `.txt` and `.tex` are byte-identical unless there is a deliberate reason not to.
10. Do not announce a new version as finished until the compiled PDF has been checked.

---

## 11. Minimal next-chat instruction

If this file is loaded in a new chat, the intended continuation is:

> **Use `excursion_area_section_v39.tex` as the exact baseline. Do not change its format. Apply the pending corrections in this handoff and produce v40 only when explicitly ordered. Preserve right-hand equation numbering, all hyperlinks, PDF hover previews, and the absence of `[N]/[N-el]/[C]/[L]` classification tags.**

