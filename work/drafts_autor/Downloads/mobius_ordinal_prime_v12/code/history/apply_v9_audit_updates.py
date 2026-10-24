from pathlib import Path
import re
p=Path(__file__).resolve().parents[1]/'mobius_ordinal_prime_transform_S_SS_v9.tex'
s=p.read_text()

# Reproducibility statement.
s=s.replace(
"The core numerical pipeline was regenerated for $1\\le n\\le10^{6}$ where stated.\nAdditional follow-up measurements introduced in Versions 5--9 are identified explicitly as\nreported measurements when their originating script was not present in the supplied\npackage; see Sections~\\ref{sec:numeric} and~\\ref{sec:ordinal-pairing}.",
"The complete numerical pipeline used in this version was regenerated in Python for\n$1\\le n\\le10^{6}$ where stated.  The accompanying package contains every Python\nscript used for the numerical tables and figures, the generated numerical arrays, and\nthe corresponding text outputs.  No MATLAB-generated numerical output is used in this\nversion.  Follow-up measurements from earlier versions whose original scripts were not\navailable were either independently regenerated in Python under an explicit protocol or\nremoved rather than retained as unaudited data."
)

# Prime-counting variance table and protocol.
pat=r"\\subsection\{K\. Prime-counting variance comparison\}.*?\\subsection\{L\. Cross-coupling test\}"
rep=r'''\subsection{K. Prime-counting variance comparison}
\label{sec:num-prime-variance}
Proposition~\ref{prop:pi-integral} puts the residual on the prime-counting side.
For reproducibility, Version 9 regenerates this scale comparison using every integer
starting point $x$ in
\begin{equation}
\label{eq:prime-variance-sampling-window}
3.8\times10^6\le x\le4.8\times10^6-H,
\end{equation}
and uses $X=4.3\times10^6$ as the reference scale.  The measured variance of
$\pi(x+H)-\pi(x)$ is compared with
\begin{align}
V_{\rm MS}(H;X)
&:=\frac{H}{(\log X)^2}\left(\log\frac{X}{H}-\gamma-\log(2\pi)\right),
\label{eq:MS-reference-variance}\\
V_{\rm Cr}(H;X)
&:=\frac{H}{\log X}.
\label{eq:Cramer-reference-variance}
\end{align}
The first is a leading reference scale motivated by the Montgomery--Soundararajan
weighted-prime variance, not a theorem for the unweighted prime count
\cite{MontgomerySoundararajan2004}; the second is the elementary Poisson/Cram\'er
reference \cite{Cramer1936}.  The regenerated ratios are
\begin{equation}
\label{eq:short-interval-variance-table}
\begin{array}{lrrrr}
\toprule
H & 200 & 1000 & 5000 & 20000\\
\midrule
\operatorname{Var}_{\rm meas}/V_{\rm MS}
 &1.119&1.179&1.211&1.518\\
\operatorname{Var}_{\rm meas}/V_{\rm Cr}
 &0.554&0.459&0.344&0.294\\
\bottomrule
\end{array}
\end{equation}
These figures are finite-scale diagnostics only; no asymptotic inference is made from
them.  The exact protocol and raw computed variances are in
\texttt{outputs/21\_v9\_followup\_numerics.txt}.

\subsection{L. Cross-coupling test}'''
s,n=re.subn(pat,rep,s,flags=re.S)
assert n==1,n

# Coupling numerical block.
s=re.sub(r"The supplied follow-up tests\nreported\n\\begin\{equation\}.*?specified family\.", r'''The Version 9 Python regeneration gives
\begin{equation}
\label{eq:coupling-table}
\begin{array}{lc}
\toprule
\text{test} & \text{value}\\
\midrule
\operatorname{corr}(Z,\operatorname{sgn}M) & +0.00063\\
\operatorname{corr}(Z,M/\sqrt n) & +0.00117\\
\operatorname{corr}(Z,\cos(\gamma_1\log n)) & -0.00122\\
\operatorname{corr}(Z,\sin(\gamma_1\log n)) & +0.00177\\
\overline Z\,|_{M>0}-\overline Z\,|_{M<0} & +0.00128\\
\bottomrule
\end{array}
\end{equation}
and an eight-bin phase test gives dispersion of the bin means $0.00303$.  Using
the same positive-autocorrelation cutoff as the main residual analysis gives
integrated autocorrelation time $51.30$, effective sample
$n_{\rm eff}\simeq17\,214$, and $1/\sqrt{n_{\rm eff}}\simeq0.00762$.
When that dependence correction is propagated to the eight phase bins, the median
effective standard error of a bin mean is about $0.0213$; the substantially smaller
number quoted in an earlier version was based on an inconsistent independence
normalisation and is not retained.

These are null results only at the tested resolution.  The calculation does not prove
decoupling; it excludes only effects visible to this small specified family and this
finite range.''',s,flags=re.S)

# Quadratic experiments regenerated.
pat=r"\\begin\{experiment\}\[Reported controls for the quadratic decomposition\].*?\\end\{experiment\}"
rep=r'''\begin{experiment}[Regenerated controls for the quadratic decomposition]
\label{exp:v6-quadratic-controls}
Version 9 regenerates these controls directly from the included Python pipeline.  On the
balanced prefix
\begin{equation}
\label{eq:v6-balanced-range}
Q=488868,
\qquad
J=244434,
\end{equation}
the exact energies are
\begin{equation}
\label{eq:v6-energy-values}
\mathcal D_2=10646184520,
\qquad
\mathcal E_2=36823324,
\qquad
2\mathcal M_2=10683007844,
\end{equation}
so
\begin{equation}
\label{eq:v6-energy-fractions}
\frac{\mathcal D_2}{2\mathcal M_2}=0.99655309,
\qquad
\frac{\mathcal E_2}{2\mathcal M_2}=0.00344691.
\end{equation}
The total parallelogram energy is identical for the ordinal, reversed, and a fixed
random pairing, exactly as required by Remark~\ref{rem:pairing-insensitive}.

For a documented finite-range comparison, fitting all balanced prefixes with
$8000\le J\le244434$ gives slopes
\begin{equation}
\label{eq:v6-power-fits}
\mathcal D_2:\ 2.01633,
\qquad
\mathcal E_2:\ 1.46412,
\qquad
\mathcal M_2:\ 2.01198.
\end{equation}
Over the same selected range $\mathcal E_2/\mathcal D_2$ decreases from
$0.01909$ to $0.00346$.  These are finite-range fits under an explicit protocol,
not asymptotic exponents.
\end{experiment}'''
s,n=re.subn(pat,rep,s,flags=re.S); assert n==1,n

pat=r"\\begin\{experiment\}\[Scale of the center displacement\].*?\\end\{experiment\}"
rep=r'''\begin{experiment}[Scale of the center displacement]
\label{exp:v6-center-scale}
Equation~\eqref{eq:e-endpoint-difference} shows exactly that $2e_j$ is the
increment of the same squarefree-time Mertens walk across a window of length
$|d_j|$.  The regenerated conditional values are
\begin{center}
\begin{tabular}{@{}ccccc@{}}
\toprule
$|d|$ bin & $15$--$23$ & $56$--$87$ & $136$--$211$ & $328$--$510$\\
\midrule
$\operatorname{RMS}(2e)/\sqrt{\operatorname{mean}|d|}$
& $1.006$ & $1.023$ & $0.979$ & $0.980$\\
$\operatorname{RMS}(2e)/\operatorname{mean}|d|$
& $0.231$ & $0.121$ & $0.075$ & $0.049$\\
\bottomrule
\end{tabular}
\end{center}
A separate logarithmic-bin fit of medians gives exponents $0.46888$ for
$|d_j|$ and $0.23995$ for $|e_j|$ in the ordinal variable.  The numerical
relation is compatible with a random-walk square-root scale, but no independence
claim is made: both quantities are built from the same walk.
\end{experiment}'''
s,n=re.subn(pat,rep,s,flags=re.S); assert n==1,n

# Local stats values.
s=s.replace('0.5007,\\ 0.2488,\\ 0.1249,\\ 0.0631,\\ 0.0314,\\ 0.0157,',
            '0.500544,\\ 0.249105,\\ 0.124996,\\ 0.062603,\\ 0.031492,\\ 0.015762,')
s=s.replace('was $4.0120$', 'was $4.012027$')
s=s.replace('0.00109,\\ -0.00141,\\ -0.00135,\\ 0.00149,\\ 0.00024,\\ -0.00194.',
            '0.001087,\\ -0.001405,\\ -0.001354,\\ 0.001485,\\ 0.000237,\\ -0.001938.')

# Signed third moment: replace unstable earlier exponent by explicit regeneration.
pat=r"\\begin\{experiment\}\[Signed third moment\].*?\\end\{experiment\}"
rep=r'''\begin{experiment}[Signed third moment]
\label{exp:v7-third-moment}
The Version 9 regeneration uses $28$ logarithmically spaced endpoints between
$Q=2\times10^4$ and $Q=607926$.  Under that explicit protocol the fitted slopes are
\begin{equation}
\label{eq:reported-third-moment-exponents}
\sum_{q\le Q}|R(q)|^3:\ 2.48095,
\qquad
\left|\sum_{q\le Q}R(q)^3\right|:\ 2.56807.
\end{equation}
The ratio $|\sum R^3|/\sum|R|^3$ is $0.1641$ near $Q=4.85\times10^4$ and
$0.2776$ at $Q=607926$.  An earlier fit under a different window gave a much
smaller signed exponent; the change under protocol is itself evidence that no stable
power law should be inferred for the signed sum on this range.  Only finite-range
suppression relative to the absolute third moment is recorded.
\end{experiment}'''
s,n=re.subn(pat,rep,s,flags=re.S); assert n==1,n

# Active lifetime experiment regenerated.
pat=r"\\begin\{experiment\}\[Shape of the active lifetime multiset\].*?\\end\{experiment\}"
rep=r'''\begin{experiment}[Shape of the active lifetime multiset]
\label{exp:active-lifetime-shape}
The full multiset
\begin{equation}
\label{eq:active-lifetime-multiset}
\mathcal L(q):=
\bigl\{\,|\beta_j-\alpha_j|:\ j\in\mathcal W(q)\,\bigr\}
\end{equation}
is not determined by the single height $h=|R(q)|$.  Version 9 regenerates the
comparison on every cut before the balanced prefix $Q=488868$ and compares it with a
fixed-seed iid fair-sign walk.  Each entry below is M\"obius / iid:
\begin{center}
\begin{tabular}{@{}cccc@{}}
\toprule
$h$ bin
& $\langle\operatorname{mean}\mathcal L\rangle/h$
& between-cut dispersion
& $\langle\operatorname{sd}(\mathcal L)/\operatorname{mean}(\mathcal L)\rangle$\\
\midrule
$8$--$16$   & $2.066/2.068$ & $0.364/0.365$ & $0.102/0.102$\\
$32$--$64$  & $2.010/2.025$ & $0.170/0.172$ & $0.055/0.054$\\
$128$--$400$& $1.997/2.000$ & $0.087/0.082$ & $0.028/0.026$\\
\bottomrule
\end{tabular}
\end{center}
Aggregating active pair-cut incidences gives
\begin{equation}
\label{eq:active-lifetime-tail-measured}
\begin{array}{c|ccc}
\text{threshold}&1.5h&2.5h&3.5h\\ \hline
\text{M\"obius}&0.99754&0.00841&0.00037\\
\text{iid}&0.99954&0.00217&0.00007
\end{array}.
\end{equation}
Thus the history-dependent shape that survives the endpoint collapse is closely
reproduced by a conditioned fair-sign walk on this finite range.  This is a measured
statement, not an asymptotic theorem.
\end{experiment}'''
s,n=re.subn(pat,rep,s,flags=re.S); assert n==1,n

# Correct self-dynamics section in full and extend it.
pat=r"\\section\{Self-iteration of the ordinal-prime transform\}.*?\\section\{Collisions and elementary modular rigidity of \\$SS\\\}"
rep=r'''\section{Self-iteration of the ordinal-prime transform}
\label{sec:self-dynamics}

The absolute transform can be iterated on squarefree inputs.  Let
\begin{equation}
\label{eq:phi-definition}
\mathcal S:=\{n\ge1:\mu(n)\ne0\},
\qquad
\varphi:\mathcal S\to\mathbb P,
\qquad
\varphi(n):=|S(n)|,
\end{equation}
where $\mathbb P$ is the set of primes.  Since every prime is squarefree,
$\varphi(\mathcal S)\subset\mathbb P\subset\mathcal S$.

The ordinal variables $\alpha_j,\beta_j$ of Section~\ref{sec:ordinal-pairing}
are positions in the squarefree clock, not natural integers.  To avoid mixing the two
domains, define their natural-coordinate lifts
\begin{equation}
\label{eq:natural-pair-lifts}
A_j:=s_{\alpha_j},
\qquad
B_j:=s_{\beta_j}.
\end{equation}
Thus $A_j$ and $B_j$ are the actual integer positions of the $j$th positive and
negative M\"obius values.

\begin{proposition}[Exact fibres in the natural coordinate]
\label{prop:phi-fibres}
For every $j\ge1$,
\begin{equation}
\label{eq:phi-fibres}
\boxed{\;\varphi^{-1}(p_j)=\{A_j,B_j\}=\{s_{\alpha_j},s_{\beta_j}\}.\;}
\end{equation}
Consequently every prime has indegree $2$, every squarefree composite has indegree
$0$, and every squarefree integer has outdegree $1$ in the functional digraph.
\end{proposition}

\begin{proof}
The $j$th positive and $j$th negative natural occurrences receive $+p_j$ and
$-p_j$, respectively, and no other input receives absolute value $p_j$.
\end{proof}

Define the prime-index map
\begin{equation}
\label{eq:prime-index-map}
f(j):=N_-(p_j).
\end{equation}
Since every prime has M\"obius value $-1$,
\begin{equation}
\label{eq:phi-prime-index-conjugacy}
\boxed{\;\varphi(p_j)=p_{f(j)}.\;}
\end{equation}
If
\begin{equation}
\label{eq:negative-composite-counter}
C_-(x):=\#\{m\le x:m\text{ composite and }\mu(m)=-1\},
\end{equation}
then exactly
\begin{equation}
\label{eq:f-negative-composite}
f(j)=j+C_-(p_j).
\end{equation}
The first negative squarefree composite is $30=2\cdot3\cdot5$.

\begin{theorem}[Complete periodic-orbit classification]
\label{thm:phi-dynamics}
The periodic points of $\varphi$ are exactly
\begin{equation}
\label{eq:phi-fixed-set}
\boxed{\;2,3,5,7,11,13,17,19,23,29.\;}
\end{equation}
All ten are fixed points, and there are no cycles of length greater than one.
Every other squarefree input maps in one step to a prime at least $31$, after which
its orbit is strictly increasing and tends to infinity.
\end{theorem}

\begin{proof}
Before $30$ the negative M\"obius occurrences are precisely the primes.  Hence the
first ten negative natural occurrence positions are
\begin{equation}
\label{eq:first-ten-negative-natural}
B_j=p_j\qquad(1\le j\le10),
\end{equation}
and therefore $\varphi(p_j)=p_j$ for $j\le10$.  For $j\ge11$, the negative
composite $30$ lies below $p_j$, so \eqref{eq:f-negative-composite} gives
$f(j)\ge j+1$ and therefore
\begin{equation}
\label{eq:phi-prime-growth-elementary}
\varphi(p_j)=p_{f(j)}>p_j.
\end{equation}
Every image of $\varphi$ is prime.  Thus an input not mapping to one of the ten fixed
primes reaches a prime at least $31$, and strict growth then persists forever.
\end{proof}

The first ten positive natural occurrence positions are
\begin{equation}
\label{eq:first-ten-positive-natural}
A_1,\ldots,A_{10}=1,6,10,14,15,21,22,26,33,34.
\end{equation}
Thus the basin of the fixed point $p_j$, $j\le10$, is exactly
\begin{equation}
\label{eq:fixed-basin-two-points}
\boxed{\;\{p_j,A_j\}.\;}
\end{equation}
For $j>1$, $A_j$ is necessarily composite because a positive M\"obius value greater
than $1$ has an even positive number of distinct prime factors.

\begin{proposition}[Prime-spine decomposition]
\label{prop:prime-spine-decomposition}
The map $f$ is strictly increasing.  It fixes $1,\ldots,10$, and satisfies
$f(j)>j$ for every $j\ge11$.  Consequently the prime subgraph is the disjoint union
of the ten fixed points and infinite strictly increasing rays beginning at indices
$j$ not in $f(\mathbb N)$.  In the full squarefree graph, every prime vertex has the
positive leaf $A_j$ attached to it; a source prime has in addition the negative
composite leaf $B_j$, while at every later vertex of an escaping prime ray the
negative preimage is exactly the preceding prime on that ray.
\end{proposition}

\begin{proof}
Between consecutive primes $p_j<p_{j+1}$ the negative counter increases at least at
$p_{j+1}$, hence $f(j+1)>f(j)$.  The remaining assertions follow from
Theorem~\ref{thm:phi-dynamics} and the fibre identity
\eqref{eq:phi-fibres}.  If $j=f(k)$, then $p_k$ is the $j$th negative occurrence,
so $B_j=p_k$; conversely a prime $B_j=p_k$ implies $f(k)=j$.  The positive preimage
cannot be prime except for $A_1=1$.
\end{proof}

\begin{proposition}[Growth and density of source primes]
\label{prop:phi-escape-rate}
As $j\to\infty$,
\begin{equation}
\label{eq:f-asymptotic}
f(j)\sim\frac{3}{\pi^2}j\log j.
\end{equation}
Hence, if
\begin{equation}
\label{eq:prime-predecessor-count}
I(J):=\#\{m\le J:m\in f(\mathbb N)\},
\end{equation}
then
\begin{equation}
\label{eq:prime-predecessor-density}
\boxed{\;I(J)\sim\frac{\pi^2}{3}\frac{J}{\log J},\;}
\end{equation}
so a density-one set of prime vertices are sources of escaping prime rays.
For any escaping orbit $x_{k+1}=\varphi(x_k)$,
\begin{align}
x_{k+1}&\sim\frac{3}{\pi^2}x_k\log x_k,
\label{eq:phi-one-step-asymptotic}\\
\log x_k&\sim k\log k,
\label{eq:phi-iterate-log-growth}\\
x_k&=k^{k+o(k)}.
\label{eq:phi-iterate-growth}
\end{align}
\end{proposition}

\begin{proof}
For a prime $p_j$,
\begin{equation}
\label{eq:Nminus-prime-asymptotic}
f(j)=N_-(p_j)=\frac{Q(p_j)-M(p_j)}2\sim\frac{3}{\pi^2}p_j
\sim\frac{3}{\pi^2}j\log j,
\end{equation}
using $Q(x)\sim6x/\pi^2$, $M(x)=o(x)$, and $p_j\sim j\log j$.
Because $f$ is strictly increasing, $I(J)$ is the asymptotic inverse count of $f$,
which gives \eqref{eq:prime-predecessor-density}.  After at most one step an escaping
orbit consists entirely of primes, so \eqref{eq:phi-one-step-asymptotic} follows.
Writing $y_k=\log x_k$ gives
\begin{equation}
\label{eq:phi-log-recurrence}
y_{k+1}=y_k+\log y_k+\log(3/\pi^2)+o(1).
\end{equation}
Standard comparison, followed by Stolz--Ces\`aro, yields
$y_k/(k\log k)\to1$, and exponentiation gives \eqref{eq:phi-iterate-growth}.
\end{proof}

\begin{remark}[Domain correction and graph geometry]
\label{rem:phi-forward-inverse}
The squarefree ordinals $\alpha_j,\beta_j$ must not be confused with the natural
preimages $A_j,B_j$.  An earlier draft did so in the fibre notation; Version 9 uses
\eqref{eq:natural-pair-lifts} throughout this section.  The inverse fibres over primes
are binary, but squarefree composites have no preimages, so the object is not a full
binary tree.  Proposition~\ref{prop:prime-spine-decomposition} gives the exact graph
structure instead.
\end{remark}

\section{Collisions and elementary modular rigidity of $SS$}'''
s,n=re.subn(pat,rep,s,flags=re.S); assert n==1,n

# Correct collision theorem from d to natural-coordinate Delta.
s=s.replace(r'''\boxed{\;SS(n+2)=SS(n)\iff
\text{there exists }j\text{ with }\{\alpha_j,\beta_j\}=\{n+1,n+2\}
\iff |d_j|=1.\;}''',r'''\boxed{\;SS(n+2)=SS(n)\iff
\text{there exists }j\text{ with }\{A_j,B_j\}=\{n+1,n+2\}
\iff |\Delta_j|=1.\;}''')
s=s.replace('same ordinal prime $p_j$, which is equivalent to the stated consecutive\npairing condition.',
            'same ordinal prime $p_j$, which is equivalent to the stated consecutive\nnatural-coordinate pairing condition.  The squarefree-ordinal displacement $d_j$ is\nnot the relevant distance here; the correct quantity is $\\Delta_j=s_{\\beta_j}-s_{\\alpha_j}$.')

# Add cryptographic / stateful-code remark after identification remark.
anchor='''\end{remark}\n\nThe required arithmetic check can nevertheless be restricted to square-root\ndepth.'''
insert='''\end{remark}\n\n\begin{remark}[Coding, error propagation, and cryptography]\n\label{rem:coding-cryptography}\nThe admissible next increment depends on the two preceding occurrence counts, so a\nmodified ternary symbol can desynchronise the ordinal labels of later symbols of the\naffected sign until the counters are restored.  This gives the representation a\nstateful consistency check.  It does not provide confidentiality: by\n\eqref{eq:universal-local-inverse}, differencing $SS_a$ reveals every ternary symbol\nwithout a key.  A keyed replacement of the public prime labels could use the same\nstate architecture, but any cryptographic security would then come from the keyed\nprimitive rather than from the ordinal-prime transform itself.\n\end{remark}\n\nThe required arithmetic check can nevertheless be restricted to square-root\ndepth.'''
assert anchor in s
s=s.replace(anchor,insert)

# Add S/SS-only short-interval transition observation (open, not theorem) before self-dynamics.
anchor='''\section{Self-iteration of the ordinal-prime transform}'''
ins=r'''\begin{remark}[A local $S/SS$ route that remains open]
\label{rem:S-local-transition-open}
Let $S^{\sharp}(n)=S(n)$ when $S(n)\ne1$ and $S^{\sharp}(n)=0$ otherwise; equivalently
$S^{\sharp}$ is obtained from the first difference of $SS$ by removing the distinguished
unit increment.  The local transition energy
\begin{equation}
\label{eq:local-transition-energy}
\mathcal E_H(x):=
\sum_{x<n\le x+H}
\left|S^{\sharp}(n+1)|S^{\sharp}(n)|
-S^{\sharp}(n)|S^{\sharp}(n+1)|\right|
\end{equation}
is positive exactly when the interval contains an adjacent nonzero sign reversal.
A theorem asserting $\mathcal E_{x^\theta}(x)>0$ for every sufficiently large $x$
and some $\theta<1$ would give a genuinely local restriction on the transform, but no
such statement is proved here.  Global positive density or almost-all short-interval
sign-change results do not imply this every-interval adjacent-pattern statement in the
presence of the zero values of $\mu$.  The remark is retained to distinguish a potentially
coercive $S/SS$ observable from the global shifted sums that reduce to ordinary
correlations.
\end{remark}

\section{Self-iteration of the ordinal-prime transform}'''
s=s.replace(anchor,ins,1)

# Status wording: all measurements regenerated, add new prime-spine proposition and crypto/recovery.
s=s.replace('and \\ref{prop:multicut-convexity-collapse}, \\ref{prop:phi-fibres},\n\\ref{prop:phi-escape-rate},',
            'and \\ref{prop:multicut-convexity-collapse}, \\ref{prop:phi-fibres},\n\\ref{prop:prime-spine-decomposition}, \\ref{prop:phi-escape-rate},')
s=s.replace('the exact finite $\\kappa$--$\\rho$ transform (regenerated to double-precision\nroundoff) and the reported finite-dimensional recovery of the first lags of $\\rho$\nfrom $\\kappa$; the short-interval variance ratios;',
            'the exact finite $\\kappa$--$\\rho$ transform (regenerated to double-precision\nroundoff); the explicitly regenerated short-interval variance ratios;')
s=s.replace('and the Version 6\nquadratic-energy and center-displacement measurements',
            'and the regenerated quadratic-energy and center-displacement measurements')

# Novelty section correction/extension.
s=s.replace('Version 9 adds the universal\ncoding theorem, the square-root recovery identity, and the exact dynamical\nclassification of $\\varphi(n)=|S(n)|$.',
            'Version 9 adds the universal coding theorem, the square-root recovery identity,\nand the exact dynamical classification of $\\varphi(n)=|S(n)|$, including the\nprime-index spine decomposition and the density-one source-prime theorem.')

# Summary duplicate heading and corrected collision + graph source density.
s=s.replace('\\section{Summary}\n\\label{sec:summary}\n\\section{Summary}\n\\label{sec:summary}', '\\section{Summary}\n\\label{sec:summary}')
s=s.replace(r'''\boxed{\;SS(n)\equiv n\pmod2\ (n\ge2),
\qquad SS(n+2)=SS(n)\iff |d_j|=1\text{ for the corresponding ordinal pair}.\;}''',
r'''\boxed{\;SS(n)\equiv n\pmod2\ (n\ge2),
\qquad SS(n+2)=SS(n)\iff |\Delta_j|=1\text{ for the corresponding natural pair}.\;}''')
# Add source density after escape summary.
needle=r'''\begin{equation}
\label{eq:summary-phi-escape}
\boxed{\;x_{k+1}=\varphi(x_k),\ x_k\to\infty:
\qquad x_{k+1}\sim\frac{3}{\pi^2}x_k\log x_k,
\qquad x_k=k^{k+o(k)}\;}
\end{equation}'''
add=needle+r'''
\begin{equation}
\label{eq:summary-phi-source-density}
\boxed{\;\#\{m\le J:m\in f(\mathbb N)\}
\sim\frac{\pi^2}{3}\frac{J}{\log J},
\quad\text{so source primes have density }1.\;}
\end{equation}'''
assert needle in s
s=s.replace(needle,add)

# Purpose bullet domain wording.
s=s.replace('the first ten primes\n$2,3,\\ldots,29$ are the only periodic points and are fixed; every other\nsquarefree input reaches a prime at least $31$ after one step and then increases\nstrictly to infinity.  Escaping orbits satisfy an unconditional prime-number-\ntheorem growth law.',
            'the first ten primes $2,3,\\ldots,29$ are the only periodic points and are\nfixed; every other squarefree input reaches a prime at least $31$ after one step and\nthen increases strictly to infinity.  On prime indices the dynamics is conjugate to\nthe strictly increasing map $f(j)=N_-(p_j)$, whose image has zero density; escaping\norbits satisfy an unconditional prime-number-theorem growth law.')

p.write_text(s)
print('patched',p)
