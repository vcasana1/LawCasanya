# casanya_prime_spiral_short v2 (2026-10-23)

Based on `chatgpt/casanya_prime_spiral_short_20261023/casanya_prime_spiral_short.tex` (v1, by ChatGPT, untouched).

Files: `casanya_prime_spiral_short_v2.tex` (= `.txt`, byte-identical), `.pdf` (17 pp., pdflatex x4, no warnings), `.zip` (folder with tex/txt/pdf).
`code/sk_1000055.py` (+ `_py.txt`, `_output.txt`): tau_k = 600299.773701928, s_k = 0.0699082598 for k = 1000055.

SHA-256
- pdf 08d5514026b8ede33a971f74547af732364ff0c45639ecb25302038e0e872d2a
- tex/txt 5029442b1febb37381dd4ed01934a9bfb7eeac5b1853406f19a46a563bf2cac2
- zip 9de3ee9c3f4713ea3b101110785ca861ac29e0d0cda29c5c175de47b286b150c

Changes from v1: canonical v39 TeX/PDF configuration (amsart, boxed links, \CGref/\CGeqref hover tooltips for every label, pagebackref);
bibliography with 14 entries (DOIs checked via Crossref; four books without DOI); every display numbered;
corrections: b_X(1/d) = mu(d)c_X(d)/sqrt(d) (v1 App. A.12 had /d); normalization remark Res_{s=1} zeta_c = 2 Xi_c(i/2);
zeros of E_X on the line = kappa_k, Gonek cell defined; explicit residue chain; |S_a| << sqrt(Q)/log Q, a>0, flow Y_a for 0<a<=2;
Poisson remainder absolutely convergent; convolution proof of c_X(d) and Mertens weight b_X(1); u defined in Cor. 4.x;
uniform IFT in Prop. 5.x; Hankel PSD criterion; notation clashes removed; "Provenance" paragraph replaced by "Data availability".
New Section 6 (from two author-supplied displays): block reality via H >= 0, Theorem of fourth-order accuracy for isolated pairs
(constants checked; corrected to |t_b - t_*| <= 1.01 B h^2/R, relative error 20B(h/R)^3 w.r.t. 2h, K_b <= 520B(h/R)^3, |h_b - h| <= 10B^2h^3/R^2),
computable two-zero certificate h_b M_3/|f''| < 84/125, quartic counterexample, GUE heuristic, regularity hypothesis, adaptive-degree scheme.
