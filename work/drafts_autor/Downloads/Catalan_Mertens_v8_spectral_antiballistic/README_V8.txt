CATALAN MERTENS V8

Main paper:
  paper/Catalan_Mertens_v8_spectral_antiballistic.tex
  paper/Catalan_Mertens_v8_spectral_antiballistic.pdf

Version 8 preserves the complete introduction, Catalan theory, physical
routes, literature discussion, bibliography, prior figures, numerical
outputs, and Python appendices from the earlier versions.

CENTRAL FINITE PHENOMENON

For m = 276638778 compressed squarefree steps, the audited path has
R(m) = 53078 returns.  Hence

  R(m) / sqrt(2m/pi) = 3.9996128947.

The elevated ratio is visible across many finite scales.  It is not declared
to be an asymptotic constant.  Under the iid simple-walk benchmark the
normalized local time has a broad half-normal limit, so this is not a
conventional four-sigma statement.  The exact Catalan relevance is that each
return creates a new primitive-excursion factor, and at a return time the
compatible-sign entropy deficit is at least 2R bits.

NEW EXACT AND UNCONDITIONAL RESULTS

1. Exact spectrum of the occupation kernel K = J*J:

     lambda_k = 1 / [4 sin^2((2k-1)pi/(4H+2))].

2. Exact comparison of quadratic occupation energy with uniform short
   exponential sums.

3. Published twisted short-interval estimates imply unconditionally
   E_1(x,H) = o(H^3) for H >= x^(3/5+epsilon); higher uniformity gives
   arbitrary logarithmic savings for H >= x^(5/8+epsilon).

4. The one-sided Catalan tent inequality

     max_h |M(x+h)-M(x)|^3 <= 3 E_1(x,H)

   converts those energy estimates into genuine bounds for every interior
   peak, not only the terminal chord.

5. Exact shifted-dilation identity, an explicit counterexample to an
   unsigned abstract frame, a low-mode reduction, and the correct Narayana
   distribution for primitive excursions.

LOGICAL BOUNDARY

The all-q dyadic Catalan occupation hierarchy is exactly equivalent to RH.
A uniform Brownian law on every short window is stronger.  The first open
energy frontier is a fixed power saving E_1 << H^(3-delta), but the principal
new empirical problem in V8 is to explain or refute persistence of the
factor-four return local time through the extreme Catalan gap tail.

VERSION 8 AUDIT

  code/jstarj_antiballistic_audit_v8.py
  outputs/jstarj_antiballistic_audit_v8.json
  outputs/jstarj_antiballistic_audit_v8.png
  outputs/catalan_return_factor4_v8.png

The audit verifies finite identities and visualizes the return data.  It does
not test the open arithmetic power-saving estimate or prove an asymptotic
factor four.
