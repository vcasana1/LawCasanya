"""Assemble paper I (analytic part) from ordinal_prime_cutoff_v17.tex plus new front and back matter.
Usage: python3 assemble_p1.py V17_TEX FRONT BACK OUT_TEX"""
import re, sys
src, front, back, out = sys.argv[1:5]
L = open(src).read().split('\n')
def lines(a, b):
    return '\n'.join(L[a - 1:b])
def must_replace(text, old, new, count=1):
    assert text.count(old) == count, (old[:80], text.count(old))
    return text.replace(old, new)

# ---- preamble
pre_a = lines(1, 52)
assert L[51].startswith('% Tooltip texts')
pre_b = lines(410, 470)
pre_b = re.sub(r'pdftitle=\{[^\n]*\},', 'pdftitle={A computable prime-corrected Riemann-von Mangoldt clock: an exact defect identity, the prime-information threshold, and the location of the zeros of the Riemann zeta function in mean square},', pre_b)
pre_b = re.sub(r'pdfsubject=\{[^\n]*\},', 'pdfsubject={Zeros of the Riemann zeta function, Riemann-von Mangoldt clock, ordinal defect, truncated Euler products, Newton iteration},', pre_b)
pre_b = re.sub(r'pdfkeywords=\{[^\n]*\}', 'pdfkeywords={Riemann zeta function, zeros of the Riemann zeta function, Riemann-von Mangoldt formula, argument of the Riemann zeta function, Euler product, prime cutoff, Newton iteration}', pre_b)
preamble = pre_a + '\n\\makeatletter\n\\makeatother\n' + pre_b

# ---- body pieces
notation = lines(615, 804)
external = lines(805, 950)
theory = lines(951, 1798)
envelope = lines(2013, 2102)

# notation: drop rows of removed material
drop_starts = [r'$\Phi(\theta)$', r'$\omega$, $\omega_0$', r'$R_0$', r'$\iota_1$', r'$K$, $B$', r'$L_T$, $\mathcal N_T$',
               r'$\mathcal A_{T,p}$', r'$\mathcal H_n(t)$', r'$f_T$', r'$\mathfrak K_\theta$',
               r'$\BW(t)$', r'$N^+(\sigma,t)$']
rows = notation.split('\n')
labels_removed = set()
keep_rows = []
for r in rows:
    if any(r.startswith(d) for d in drop_starts):
        continue
    keep_rows.append(r)
notation = '\n'.join(keep_rows)
notation = must_replace(notation, r'$A$, $A_X$, $\PP$ & set of prime powers with $\sum_{n\in A}|a_n|<\infty$; $A_X=\{p^m:p\le X\}$; finite set of primes\\', r'$A$, $A_X$ & set of prime powers with $\sum_{n\in A}|a_n|<\infty$; $A_X=\{p^m:p\le X\}$\\')
notation = must_replace(notation, r'$S_A$, $S_X$, $S_\PP$ & $\sum_{n\in A}a_n\sin(t\log n)$; $S_{A_X}$; $S_{\{p^m:p\in\PP\}}$\\', r'$S_A$, $S_X$ & $\sum_{n\in A}a_n\sin(t\log n)$; $S_{A_X}$\\')
notation = must_replace(notation, r'$v_A$, $v_X$, $v_\PP$ & $\frac12\sum_{n\in A}a_n^2$; $v_{A_X}$; $v_{\{p^m:p\in\PP\}}$\\', r'$v_A$, $v_X$ & $\frac12\sum_{n\in A}a_n^2$; $v_{A_X}$\\')
notation = must_replace(notation, r'$y_0$, $w_T$ & fixed threshold; threshold tending to infinity\\', r'$y_0$, $w_T$ & fixed threshold; threshold tending to infinity (Corollary~\CGref{cor:dichotomy})\\')
notation = must_replace(notation, r'$n_{\mathsf R}(u)$, $C_1,C_2,C_3$ & near-ordinate count and constants of Lemma~\CGref{lem:zero_pairs} and Theorem~\CGref{thm:multiplicity_all}\\',
    r'$n_{\mathsf R}(u)$, $C_1,C_2,C_3$ & number of ordinates of the window within $\mathsf R\mathfrak b_T$ of $u$; constants of Lemma~\CGref{lem:zero_pairs} and Theorem~\CGref{thm:multiplicity_all}\\' + '\n' +
    r'$\mathsf M$, $\mathsf P$, $\mathsf F$, $\mathsf s$, $\mathsf W$, $\mathsf y$ & local names in proofs: $\#\IT$; number of close pairs; $g^{4r}$ (Lemma~\CGref{lem:sampling_rho}); window and scale (Lemma~\CGref{lem:maximal_primes})\\' + '\n' +
    r'$\mathfrak k$, $\mathfrak k_j$ & multiplicity constants: least $\mathfrak k\ge1$ with $\int\tilde n^2\le\mathfrak k\,\mathfrak b_T\#\IT$ (Lemma~\CGref{lem:sampling_rho}, Theorem~\CGref{thm:uniform_iteration})\\' + '\n' +
    r'$y^{(j)}_k$, $\mathfrak r_{j,k}$, $d_{j,k}$ & $\tau_k-x^{(j)}_k$ and the remainder of Lemma~\CGref{lem:second_identity}; gaps $x^{(j)}_{k+1}-x^{(j)}_k$ (Proposition~\CGref{prop:deformation})\\' + '\n' +
    r'$\mathsf g_j$ & $\mathcal M(\varphi_jS_{X_j}\textquoteright)$, maximal function of the derivative of the $j$-th Euler phase (Proposition~\CGref{prop:recursion})\\' + '\n' +
    r'$\mathcal A_p$ & norm of the maximal operator on $L^p$ (Theorem~\CGref{thm:known_maximal})\\' + '\n' +
    r'$\mathscr A$ & van der Corput\textquoteright s $\mathscr A$-process on exponent pairs (Theorem~\CGref{thm:known_exponents})\\' + '\n' +
    r'$\varepsilon_\circ$, $\mathsf q$, $C_{\rm b}$, $C_{\rm d}$ & parameter of the Jensen disc (proof of Theorem~\CGref{thm:envelope}); fixed exponent $\log n=\mathsf q\log T$ (Remark~\CGref{rem:transport}); constants in the proof of Lemma~\CGref{lem:higher_moments}\\')
notation = must_replace(notation, r'$A_j(r)$, $\mathfrak k_j$, $m^*$, $C_\star$, $H^*$ & normalized moments of the errors, multiplicity constants, number of steps and constants of Theorem~\CGref{thm:uniform_iteration}\\', r'$A_j(r)$, $m^*$, $C_\star$, $H^*$, $B_\star$, $C_5$, $C_6$ & normalized moments of the errors, number of steps and constants of Theorem~\CGref{thm:uniform_iteration}\\')


# external results: drop unused blocks (theorem + following explanatory paragraph up to blank line)
def drop_block(text, label):
    i = text.index('\\label{%s}' % label)
    s = text.rfind('\\begin{theorem}', 0, i)
    e = text.index('\\end{theorem}', i) + len('\\end{theorem}')
    rest = text[e:]
    m = re.match(r'\n(?!\n)([^\n]*\n)?', rest)       # one directly following non-blank paragraph line
    if rest.startswith('\n') and len(rest) > 1 and rest[1] not in '\n\\' or (rest.startswith('\n(') ):
        nl = rest.index('\n', 1)
        e += nl
    return text[:s] + text[e:]
for lab in ['thm:known_KL', 'thm:known_stationary', 'thm:known_vdC', 'thm:known_vdC_weighted', 'thm:known_vdC2',
            'thm:known_landau', 'thm:known_density']:
    external = drop_block(external, lab)
external = must_replace(external, r' A limit superior is not a supremum: $|\delta_{34}|=0.993711$.', '')
external = must_replace(external, r'Earlier explicit versions are due to Trudgian \cite{Trudgian2014} and to Hasanalizade, Shen and Wong \cite{HasanalizadeShenWong2022}.',
    r'Earlier explicit versions are due to Trudgian \cite{Trudgian2014} and to Hasanalizade, Shen and Wong \cite{HasanalizadeShenWong2022}. For $T$ sufficiently large, Trudgian \cite[\S5 of the preprint]{Trudgian2010} proved $|S(T)|\le0.1013\log T$ with Huxley\textquoteright s exponent $\frac{32}{205}$ for $\zeta(\frac12+it)$.')

# theory edits
theory = must_replace(theory, r'the transport integral need not be small, and the computed responses do differ (Section~\CGref{sec:heuristic}); no asymptotic statement about this difference is proved.',
    r'and the transport integral need not be small; no asymptotic statement about this difference is proved.')
i = theory.index(r'At $T=2^{19}$ (Table~\CGref{tab:transport})')
j = theory.index(r'\end{remark}', i)
theory = theory[:i] + r'Whether the transport cancels against $u_k(X)$ is open; a proof of such a cancellation would allow a fixed $c$ in Corollary~\CGref{cor:computable_clock} (Question~\CGref{q:fixed_c}). The denominator in \CGeqref{eq:newton_exact} may vanish where $F_X\textquoteright(\tau_k)\le0$.' + '\n' + theory[j:]
i = theory.index(r'Table~\CGref{tab:iteration} illustrates')
j = theory.index(r'\end{table}', i) + len(r'\end{table}')
theory = theory[:i] + theory[j:].lstrip('\n')

# envelope edits
envelope = must_replace(envelope, r'By Theorem~\CGref{thm:known_BW}, $\mathfrak a\le0.10076$; whether $\mathfrak a=0$ is not known.',
    r'By Theorem~\CGref{thm:known_BW}, $\mathfrak a\le0.10076$, and $\mathfrak a\le0.1013$ also follows from \cite{Trudgian2010}; whether $\mathfrak a=0$ is not known.')
i = envelope.index(r'\begin{proposition}[Finite-height envelope]')
j = envelope.index(r'\begin{theorem}[Theorem E]')
envelope = envelope[:i] + envelope[j:]
i = envelope.index(r'\begin{proposition}[An explicit bound valid for all $T\ge e$]')
envelope = envelope[:i].rstrip('\n') + '\n'
old_stmt = envelope[envelope.index(r'For the piecewise linear $\mathfrak e_{\rm B}$'):envelope.index(r'\end{theorem}')]
new_stmt = (r'For $J\ge0$ let $(\mathsf k_0,\mathsf l_0)=(\frac{13}{84},\frac{55}{84})$, $(\mathsf k_j,\mathsf l_j)=A^j(\mathsf k_0,\mathsf l_0)$ with $A(\mathsf k,\mathsf l)=\bigl(\frac{\mathsf k}{2\mathsf k+2},\frac12+\frac{\mathsf l}{2\mathsf k+2}\bigr)$, and let $\mathfrak e_J$ be the piecewise linear function through the points $(\mathsf l_j-\mathsf k_j,\mathsf k_j)$, $0\le j\le J$, and $(1,0)$; the first vertices are $(\frac12,\frac{13}{84})$, $(\frac{139}{194},\frac{13}{194})$, $(\frac{173}{207},\frac{13}{414})$, $(\frac{773}{854},\frac{13}{854})$. Let $C_J$ be the right side of \CGeqref{eq:envelope_formula} for $\mathfrak e=\mathfrak e_J$. Then $\mathfrak a\le C_J$ for every $J$; $C_J$ decreases, $C_7=0.0968160063\ldots$ and $C_{30}=0.0968151142790\ldots$; hence' + '\n'
            r'\begin{equation}' + '\n' + r'\limsup_{k\to\infty}|\tau_k-\gamma_k|=2\pi\mathfrak a\le2\pi C_{30}=0.6083073\ldots<0.60831 .' + '\n' + r'\label{eq:envelope_value}' + '\n' + r'\end{equation}' + '\n')
envelope = envelope.replace(old_stmt, new_stmt)
old_prof = envelope[envelope.index(r'\emph{The profile.}'):envelope.index(r'\end{proof}', envelope.index(r'\emph{The profile.}'))]
new_prof = (r'\emph{The profile.} Let $\varepsilon'+"'"+r'>0$, $(\mathsf k_0,\mathsf l_0)=(\frac{13}{84}+\varepsilon'+"'"+r',\frac{55}{84}+\varepsilon'+"'"+r')$ and $(\mathsf k_j,\mathsf l_j)=A^j(\mathsf k_0,\mathsf l_0)$ for $1\le j\le J$, exponent pairs by Theorem~\CGref{thm:known_exponents}(a),(c), with $\mathsf l_j-\mathsf k_j\ge\frac12$; by (b), $|\zeta(\mathsf l_j-\mathsf k_j+it)|\ll|t|^{\mathsf k_j}\log|t|$, and $|\zeta(1+it)|\ll\log|t|$. The points $(\mathsf l_j-\mathsf k_j,\mathsf k_j)$ and $(1,0)$ have decreasing ordinates, and Theorem~\CGref{thm:known_PL} between consecutive points gives the hypothesis of the theorem for the piecewise linear function through them. For $\varepsilon'+"'"+r'=0$ these are the vertices of $\mathfrak e_J$; the right side of \CGeqref{eq:envelope_formula} depends continuously on $\varepsilon'+"'"+r'$, so $\mathfrak a\le C_J$. On each linear piece $\mathfrak e(\sigma)=\alpha\sigma+\beta$ of $[0,1]$ a primitive of $\mathfrak e(\sigma)/\sqrt{\sigma(2-\sigma)}$ is $-\alpha\sqrt{\sigma(2-\sigma)}+(\alpha+\beta)\arcsin(\sigma-1)$, and the values of $C_J$ at the rational vertices are computed from it at $50$ digits by the program \texttt{opc\_envelope\_iterations\_p1.py} (Data availability); the value $C_7$ agrees with the $40$-digit quadrature of \texttt{opc\_envelope\_coefficient\_v14.py}. Each new vertex lies below the chord from the previous one to $(1,0)$, so $C_J$ decreases. Multiply by $2\pi$ and use Proposition~\CGref{prop:envelope_equivalence}(a).' + '\n')
envelope = envelope.replace(old_prof, new_prof)
old_rem = envelope[envelope.index(r'\begin{remark}\label{rem:envelope_inputs}'):envelope.index(r'\end{remark}', envelope.index(r'\begin{remark}\label{rem:envelope_inputs}')) + len(r'\end{remark}')]
new_rem = (r'\begin{remark}\label{rem:envelope_inputs}' + '\n' +
    r'(a) Trudgian \cite[\S5 of the preprint]{Trudgian2010} obtained $\mathfrak a\le0.1013$ from Huxley\textquoteright s exponent $\frac{32}{205}$ at $\sigma=\frac12$ by the same method; Theorem~\CGref{thm:envelope} replaces the exponents and lets the parameters of the disc tend to their limits. With the explicit exponents used by Bellotti and Wong ($\frac{27}{164}$ at $\sigma=\frac12$, Yang\textquoteright s lines $\sigma_j=1-j/(2^j-2)$ with exponents $1/(2^j-2)$, $4\le j\le9$ \cite{BellottiWong2025}) and linear interpolation between $\sigma=0$ and $\sigma=\frac12$, as in \cite[\S3.1]{BellottiWong2025}, the right side of \CGeqref{eq:envelope_formula} is $0.10074$, the limit of their $C_1=0.10076$ as their parameters tend to $(1,1)$; the same right-hand profile reflected by the functional equation gives $0.09783$. (b) Profiles of $\mu(\sigma)$ below $\mathfrak e_J$ are known: Trudgian and Yang \cite{TrudgianYang2023} close a convex hull of known exponent pairs, Bourgain\textquoteright s among them, under the $A$-, $B$- and $C$-processes and deduce piecewise bounds for $\mu(\sigma)$ on $[\frac12,1]$. Any such profile can be inserted in \CGeqref{eq:envelope_formula}; we do not evaluate it here. (c) For the Lindel\"of profile ($\mathfrak e=0$ on $[\frac12,1]$) the right side is $0.07863$: Backlund\textquoteright s method with a disc cannot give less, whatever the exponents. (d) Theorem~\CGref{thm:envelope} is asymptotic: the explicit constants of the bounds for $\zeta$ do not enter, which is why non-explicit exponents may be used, and it does not replace the explicit bounds of \cite{BellottiWong2025}, valid for all $T\ge e$.' + '\n' + r'\end{remark}')
envelope = envelope.replace(old_rem, new_rem)


# ---------- corrections after the author's review of v1 (2026-10-19)
def sub_block(text, start_marker, end_marker, fn):
    i = text.index(start_marker); j = text.index(end_marker, i) + len(end_marker)
    return text[:i] + fn(text[i:j]) + text[j:]

# (1) Lemma on near pairs: count only l in I_T; exact regimes.
theory = must_replace(theory,
    r"Let $b=\mathfrak b_T$, $M=\#\IT$ and, for $\mathsf R\ge1$, $n_\Lambda(u)=\#\{l:|\gamma_l-u|\le\mathsf R b\}$. There are absolute constants $C_1,C_2$ such that for $T\ge T_0$ and every $\mathsf R\ge1$,",
    r"Let $b=\mathfrak b_T$, $\mathsf M=\#\IT$ and, for $\mathsf R\ge1$ and real $u$, $n_{\mathsf R}(u)=\#\{l\in\IT:|\gamma_l-u|\le\mathsf R b\}$. There are absolute constants $C_1,C_2$ such that for $T\ge T_0$ and every $\mathsf R\ge1$,")
theory = must_replace(theory, r"\le C_1\mathsf R M,\qquad\sum_{k\in\IT}n_\Lambda(\gamma_k)^2\le C_2\mathsf R^2M .",
    r"\le C_1\mathsf R\mathsf M,\qquad\sum_{k\in\IT}n_{\mathsf R}(\gamma_k)^2\le C_2\mathsf R^2\mathsf M .")
theory = must_replace(theory,
    r"If $4\mathsf R b>1$, then $N(u+h)-N(u)\le Ch\log T$ for $h\ge1$ and $u\in[T-1,2T]$, by \CGeqref{eq:N_decomposition} and Theorem~\CGref{thm:known_basic}; hence every $\gamma_k$ has at most $C'\mathsf R$ ordinates within $\mathsf R b$, and both bounds follow.",
    r"If $4\mathsf R b>1$, then $N(u+h)-N(u)\le Ch\log T$ for $1\le h\le T$ and $u\in[T-1,2T]$, by \CGeqref{eq:N_decomposition} and Theorem~\CGref{thm:known_basic}. Since only $l\in\IT$ are counted, $n_{\mathsf R}(\gamma_k)$ is at most the number of ordinates in an interval of length $h=\min(2\mathsf R b,T)$ contained in $[T-1,2T]$, which is $\le Ch\log T\le C'\mathsf R$ (for $h=T$ use $T\log T\le2\mathsf R b\log T\le4\pi\mathsf R$); both bounds follow.")
theory = must_replace(theory, r"hence the number of pairs is at most $\frac1{\mathsf R b}\int_{T-1}^{2T}(N(u+2\mathsf R b)-N(u))^2du\le C\mathsf R T/b\le C_1\mathsf R M$, as $M\asymp T/b$.",
    r"hence the number of pairs is at most $\frac1{\mathsf R b}\int_{T-1}^{2T}(N(u+2\mathsf R b)-N(u))^2du\le C\mathsf R T/b\le C_1\mathsf R\mathsf M$, as $\mathsf M\asymp T/b$.")
theory = must_replace(theory, r"\le\frac{T^{1/4}(C\mathsf R^4T)^{3/4}}{2\mathsf R b}\le C_2\mathsf R^2M$.", r"\le\frac{T^{1/4}(C\mathsf R^4T)^{3/4}}{2\mathsf R b}\le C_2\mathsf R^2\mathsf M$; the triples with $l,l'\in\IT$ are among them.")

# (2) Multiplicity theorem: M -> sans M, P -> sans P, pairs in I_T.
def fix_mult(block):
    block = must_replace(block, r"Write $b=\mathfrak b_T$, $M=\#\IT$,", r"Write $b=\mathfrak b_T$, $\mathsf M=\#\IT$,")
    block = must_replace(block, r"\le b\,P$ with $P=\#\{(k,l)\in\IT^2:|x_k-x_l|<b\}$", r"\le b\,\mathsf P$ with $\mathsf P=\#\{(k,l)\in\IT^2:|x_k-x_l|<b\}$")
    block = must_replace(block, r"number at most $C_1\mathsf R_0M$", r"number at most $C_1\mathsf R_0\mathsf M$")
    block = must_replace(block, r"their number $P_\mathsf R$ satisfies", r"their number $\mathsf P_{\mathsf R}$ satisfies")
    block = must_replace(block, r"P_\mathsf R\le\frac{65}{\mathsf R^2}", r"\mathsf P_{\mathsf R}\le\frac{65}{\mathsf R^2}")
    block = must_replace(block, r"\le\frac{130\sqrt{C_2}\,\mathsf A^2\mathsf H}{\mathsf R}\,M,", r"\le\frac{130\sqrt{C_2}\,\mathsf A^2\mathsf H}{\mathsf R}\,\mathsf M,")
    block = must_replace(block, r"by Cauchy--Schwarz, the hypothesis and \CGeqref{eq:zero_pairs}. Summing over $i\ge0$ gives at most $260\sqrt{C_2}\,\mathsf A^2HM/\mathsf R_0$.",
                          r"by Cauchy--Schwarz, the hypothesis and \CGeqref{eq:zero_pairs} (both $k$ and $l$ lie in $\IT$, so $n_{2\mathsf R}$ counts every $l$ of the block). Summing over $i\ge0$ gives at most $260\sqrt{C_2}\,\mathsf A^2\mathsf H\mathsf M/\mathsf R_0$.")
    block = must_replace(block, r"the two parts are equal and $P\le2\sqrt{260C_1\sqrt{C_2}}\,\mathsf A\sqrt \mathsf H\,M$.", r"the two parts are equal and $\mathsf P\le2\sqrt{260C_1\sqrt{C_2}}\,\mathsf A\sqrt \mathsf H\,\mathsf M$.")
    return block
theory = sub_block(theory, r"\begin{theorem}[Multiplicity of the corrected clock points]", r"\end{proof}", fix_mult)

# (3) Lemma multiplicity (one-step clock): rho typo, M -> sans M.
def fix_lem_mult(block):
    block = must_replace(block, r"Write $b=\mathfrak b_T$ and $M=\#\IT$.", r"Write $b=\mathfrak b_T$ and $\mathsf M=\#\IT$.")
    block = must_replace(block, r"The pairs with $|j-k|\le1$ contribute at most $3bM$.", r"The pairs with $|j-k|\le1$ contribute at most $3b\mathsf M$.")
    block = must_replace(block, r"and $|\rho_{k+m}-x^{(1)}_k|\le b$.", r"and $|x^{(1)}_{k+m}-x^{(1)}_k|\le b$.")
    n0 = len(re.findall(r"(?<![A-Za-z\\_{])M(?![A-Za-z_])", block))
    block = re.sub(r"(?<!\\mathsf )(?<![A-Za-z\\_{])M(?![A-Za-z_])", r"\\mathsf M", block)
    print('lem:multiplicity: bare M replaced', n0)
    return block
theory = sub_block(theory, r"\begin{lemma}[Multiplicity]\label{lem:multiplicity}", r"\end{proof}", fix_lem_mult)

# (4) Sampling lemma: kappa -> frak k, F -> sans F, A_p -> cal A_p, M -> sans M.
def fix_sampling(block):
    block = block.replace(r"\kappa", r"\mathfrak k")
    block = must_replace(block, r"Let $F=g^{4r}$, locally absolutely continuous with $F'=4rg^{4r-1}g'$", r"Let $\mathsf F=g^{4r}$, locally absolutely continuous with $\mathsf F'=4rg^{4r-1}g'$")
    n0 = len(re.findall(r"(?<![A-Za-z\\_{])F(?=[('\\ _^|])", block))
    block = re.sub(r"(?<!\\mathsf )(?<![A-Za-z\\_{])F(?=[('\\ _^|])", r"\\mathsf F", block)
    print('lem:sampling_rho: bare F replaced', n0)
    block = must_replace(block, r"(A_{8r}\|", r"(\mathcal A_{8r}\|")
    block = must_replace(block, r"($p=8r$, $A_p$ bounded)", r"($p=8r$, $\mathcal A_p$ bounded)")
    block = must_replace(block, r"\mathfrak k bM)^{1/2}", r"\mathfrak k b\mathsf M)^{1/2}")
    block = must_replace(block, r"\sqrt\mathfrak k\,M\,", r"\sqrt{\mathfrak k}\,\mathsf M\,")
    block = must_replace(block, r"since $b^{-1}T\asymp M$", r"since $b^{-1}T\asymp\mathsf M=\#\IT$")
    return block
theory = sub_block(theory, r"\begin{lemma}[Sampling at points of bounded multiplicity]", r"\end{proof}", fix_sampling)
external = must_replace(external, r"$A_p$ is bounded for $p\ge2$", r"$\mathcal A_p$ is bounded for $p\ge2$")
external = must_replace(external, r"\|\mathcal Mf\|_p\le A_p\|f\|_p", r"\|\mathcal Mf\|_p\le\mathcal A_p\|f\|_p")

# (5) Uniform iteration: the max in the multiplicity bound; the range of r in the higher-moments lemma.
theory = must_replace(theory, r"\emph{Multiplicities.} Let $\mathfrak k_j$ be the least $\kappa\ge1$ with $\int\tilde n_j^2\le\kappa\mathfrak b_T\#\IT$. Then $\mathfrak k_0=1$ (the $\tau_k$ are separated by at least $\mathfrak b_T$, so only the diagonal contributes), $\mathfrak k_1\le C$ (Lemma~\CGref{lem:multiplicity}) and $\mathfrak k_j\le C_3A_j(2)\sqrt{H_j}$ for $j\ge2$ (Theorem~\CGref{thm:multiplicity_all} with $\mathsf A=\max(A_j(2),1)$ and $\mathsf H=H_j$).",
    r"\emph{Multiplicities.} Let $\mathfrak k_j$ be the least $\mathfrak k\ge1$ with $\int\tilde n_j^2\le\mathfrak k\,\mathfrak b_T\#\IT$. Then $\mathfrak k_0=1$ (the $\tau_k$ are separated by at least $\mathfrak b_T$, so only the diagonal contributes), $\mathfrak k_1\le C$ (Lemma~\CGref{lem:multiplicity}) and $\mathfrak k_j\le C_3\max(A_j(2),1)\sqrt{H_j}$ for $j\ge2$ (Theorem~\CGref{thm:multiplicity_all} with $\mathsf A=\max(A_j(2),1)$ and $\mathsf H=H_j$).")
theory = must_replace(theory, r"for $j\ge3$, $\mathfrak k_{j-1}^{1/8}\sqrt{H_{j-1}}c_j\le(C_3A_{j-1}(2))^{1/8}H_{j-1}^{1/16+1/2-9/16}C_\star=C_\star(C_3A_{j-1}(2))^{1/8}$, and $A_{j-1}(2)\le A_{j-1}(2r)$ (monotonicity of the discrete norms).",
    r"for $j\ge3$, $\mathfrak k_{j-1}^{1/8}\sqrt{H_{j-1}}c_j\le(C_3\max(A_{j-1}(2),1))^{1/8}H_{j-1}^{1/16+1/2-9/16}C_\star=C_\star(C_3\max(A_{j-1}(2),1))^{1/8}$, and $\max(A_{j-1}(2),1)\le\max(A_{j-1}(2r),1)$ (monotonicity of the discrete norms), so that $A_{j-1}(2r)\max(A_{j-1}(2r),1)^{1/8}=\max(A_{j-1}(2r),A_{j-1}(2r)^{9/8})$.")
theory = must_replace(theory, r"with absolute $C,C_5$, provided $X_j\le T^{1/(160r)}$.", r"with absolute $C,C_5$, provided $X_j\le T^{1/(160r)}$ and $r\le\log T/(4\log(2\log T))$ (the range of Lemma~\CGref{lem:higher_moments}).")
theory = must_replace(theory, r"and $X_j\ge2$ because $c_j\ge C_\star(\log\log T)^{-9/16}$. So \CGeqref{eq:induction_claim} holds",
    r"and $X_j\ge2$ because $c_j\ge C_\star(\log\log T)^{-9/16}$. The condition $r\le\log T/(4\log(2\log T))$ holds for all $r\le2^{m^*}$ and $T\ge T_0$, since $m^*=\log^*T+O(1)$ gives $2^{m^*}\ll2^{\log\log\log T}=(\log\log T)^{\log2}$. So \CGeqref{eq:induction_claim} holds")
theory = must_replace(theory, r"There is an absolute constant $C$ such that for every integer $r\ge1$, every $T$ with $T^{1/(160r)}\ge2$ and every $2\le X\le T^{1/(160r)}$,",
    r"There is an absolute constant $C$ such that for every integer $r\ge1$, every $T\ge T_0$ with $T^{1/(160r)}\ge2$ and $r\le\log T/(4\log(2\log T))$, and every $2\le X\le T^{1/(160r)}$,")
theory = must_replace(theory, r"gives $\sum_{k\in\IT}u_k^{2r}\le\int_T^{2T}(|E_X|+T^{-1})^{2r}(\lL+|S_X'|)\,dt+O\bigl(4^rT^{1/100}+(2\log T)^{2r+1}\bigr)$, the last term bounding the boundary terms and the end pieces, since $|u_k(X)|\le\log T+\sqrt X$ (Lemma~\CGref{lem:s_bounds} and \CGeqref{eq:sigma_M_def}) and $X^{r+1/2}\le T^{1/100}$.",
    r"gives $\sum_{k\in\IT}u_k^{2r}\le\int_T^{2T}(|E_X|+T^{-1})^{2r}(\lL+|S_X'|)\,dt+C_{\rm b}\bigl(4^rT^{1/100}+(2\log T)^{2r+1}\bigr)$ with an absolute $C_{\rm b}$, the last term bounding the boundary terms and the end pieces, since $|u_k(X)|\le\log T+\sqrt X$ (Lemma~\CGref{lem:s_bounds} and \CGeqref{eq:sigma_M_def}) and $X^{r+1/2}\le T^{1/100}$. For $r\le\log T/(4\log(2\log T))$ and $T\ge4$ one has $4^rT^{1/100}\le T$ and $(2\log T)^{2r+1}\le T\log T$, so this term is at most $2C_{\rm b}T\log T\le9\pi C_{\rm b}\,\#\IT$ for $T\ge T_0$: it contributes an absolute constant to the mean.")
theory = must_replace(theory, r"\int_T^{2T}E_X^{2r}|S_X'|\le\mathcal E_{4r}^{1/2}C_0T^{1/2}(1+\log X)$; so the integral is at most $(\lL(2T)+C_0(1+\log X))T^{1/2}(\mathcal E_{4r}^{1/2}+T^{-2r+1/2})$. Dividing by $\#\IT\ge\frac12T\lL(T)$ and using $\lL(2T)\le2\lL(T)$ and $1+\log X\le2\pi\lL(T)$, $\langle u_k(X)^{2r}\rangle_{\IT}\le(4+4\pi C_0)T^{-1/2}\mathcal E_{4r}^{1/2}+o(1)$, and the first bound gives the second.",
    r"\int_T^{2T}E_X^{2r}|S_X'|\le\mathcal E_{4r}^{1/2}C_{\rm d}T^{1/2}(1+\log X)$, $C_{\rm d}$ the constant of \CGeqref{eq:SX_derivative}; so the integral is at most $(\lL(2T)+C_{\rm d}(1+\log X))T^{1/2}(\mathcal E_{4r}^{1/2}+T^{-2r+1/2})$. Dividing by $\#\IT\ge\frac12T\lL(T)$ and using $\lL(2T)\le2\lL(T)$ and $1+\log X\le2\pi\lL(T)$, $\langle u_k(X)^{2r}\rangle_{\IT}\le(4+4\pi C_{\rm d})T^{-1/2}\mathcal E_{4r}^{1/2}+9\pi C_{\rm b}+1$, and the first bound gives the second ($C\ge1$ absorbs the constant, as $(Cr^2)^{2r}\ge C^2$).")

# (6) Root proposition: restrict the conclusion to the global monotone regime.
theory = must_replace(theory, r"Thus a root of the corrected equation can be selected only where it gains nothing in order: the error in height of $t_k^X$ has mean square of the same order $\log\log T/\log^2T$ as that of $\tau_k$. Theorem~\CGref{thm:computable_clock} avoids roots and takes one Newton step instead.",
    r"Thus, in the regime $M_X\le\frac12\lL(T)$ where the corrected equation is monotone on the whole window, its root gains nothing in order: the error in height of $t_k^X$ has mean square of the same order $\log\log T/\log^2T$ as that of $\tau_k$. The proposition says nothing about roots at larger cutoffs selected by a local criterion. Theorem~\CGref{thm:computable_clock} avoids roots and takes one Newton step instead.")

# (7) Remark on transport: no theta, no L_T.
theory = must_replace(theory, r"for $\ell_n=\theta L_T$ with fixed $\theta$ the phase change $\delta_k\ell_n$ has mean square $\theta^2L_T^2\langle\delta_k^2\rangle_{\IT}\sim2\theta^2\log\log T$, so it is not small,",
    r"for $\log n=\mathsf q\log T$ with fixed $0<\mathsf q<1$ the phase change $\delta_k\ell_n$ has mean square $\mathsf q^2\log^2T\,\langle\delta_k^2\rangle_{\IT}\sim2\mathsf q^2\log\log T$, so it is not small,")

# (8) Maximal-primes window: psi, W, y_0 are local names that collide with the test function, the Lambert function and the threshold.
def fix_window(block):
    block = block.replace(r"\check\psi", r"\check{\mathsf s}").replace(r"\psi", r"\mathsf s")
    block = re.sub(r"(?<![A-Za-z\\_{])W(?![A-Za-z_0-9])", r"\\mathsf W", block)
    block = block.replace("y_0", r"\mathsf y")
    return block
theory = sub_block(theory, r"\emph{Window.} Fix $\psi\in", r"\emph{At the ordinates.}", fix_window)
assert r"\mathsf s" in theory and r"\mathsf W\ge\frac12" in theory

# (9) Backlund parameter eta -> varepsilon_circ (eta_n are Dirichlet coefficients).
envelope = sub_block(envelope, r"\emph{Backlund's method.} Let $0<\eta<\frac1{100}$", r"\emph{The profile.}", lambda b: b.replace(r"\frac\eta2", r"\frac{\varepsilon_\circ}2").replace(r"\eta", r"\varepsilon_\circ"))
assert r"\varepsilon_\circ\to0" in envelope

# (10) The A-process is written with a script letter (A, A_X are sets of prime powers; cal A_p maximal constants).
external = must_replace(external, r"so is $A(\mathsf k,\mathsf l)=\bigl(", r"so is $\mathscr A(\mathsf k,\mathsf l)=\bigl(")
envelope = must_replace(envelope, r"A^j(\mathsf k_0,\mathsf l_0)$ with $A(\mathsf k,\mathsf l)=", r"\mathscr A^j(\mathsf k_0,\mathsf l_0)$ with $\mathscr A(\mathsf k,\mathsf l)=")
envelope = must_replace(envelope, r"$(\mathsf k_j,\mathsf l_j)=A^j(\mathsf k_0,\mathsf l_0)$ for $1\le j\le J$", r"$(\mathsf k_j,\mathsf l_j)=\mathscr A^j(\mathsf k_0,\mathsf l_0)$ for $1\le j\le J$")
envelope = must_replace(envelope, r"under the $A$-, $B$- and $C$-processes", r"under van der Corput\textquoteright s $\mathscr A$- and $\mathscr B$-processes and the $\mathscr C$-process")

# (11) Fujii part II: corrections to part I.
external = must_replace(external, r"Fujii's statement is an asymptotic formula with main term", r"Part II of Fujii's paper \cite{Fujii1981} carries corrections to Part I; the two statements quoted here are those of Part I, pp.~225 and 232--233. Fujii's statement is an asymptotic formula with main term")



# (12) Signed law: the real parameter eta collides with the Dirichlet coefficients eta_n; use xi (the variable of Theorem A).
def fix_signed(block):
    n = block.count(r"\eta")
    block = block.replace(r"\eta", r"\xi")
    print('cor:signed_law: eta -> xi', n)
    return block
theory = sub_block(theory, r"\begin{corollary}[Signed law", r"\end{proof}", fix_signed)


# (13) Second-level identity: Y^{(j)}_k collides with the polynomial lengths Y, Y_k; R_{j,k} with the radii R.
def fix_second(block):
    n1 = block.count("Y^{("); n2 = block.count("R_{j,k}")
    block = block.replace("Y^{(", "y^{(").replace("R_{j,k}", r"\mathfrak r_{j,k}")
    print('lem:second_identity: Y->y', n1, ' R->frak r', n2)
    return block
theory = sub_block(theory, r"\begin{lemma}[The second-level identity]", r"\end{proof}", fix_second)
assert "Y^{(" not in theory


# (14) Maximal functions g_j of the iteration vs Gram points g_m: sans-serif for the maximal functions; the remainder R_2.
n = len(re.findall(r"(?<![A-Za-z\\_{])g_(?:j|1|2)(?![A-Za-z0-9])", theory))
theory = re.sub(r"(?<![A-Za-z\\_{])g_(j|1|2)(?![A-Za-z0-9])", r"\\mathsf g_\1", theory)
print('maximal functions g_j -> sans g_j:', n)
theory = must_replace(theory, r"-\Delta_k(R_2/\lL(\tau))$, where $\Delta_ka=a_{k+1}-", r"-\Delta_k(\mathfrak r_2/\lL(\tau))$, where $\mathfrak r_2$ is the sequence $\mathfrak r_{2,k}$ of Lemma~\CGref{lem:second_identity}, $\Delta_ka=a_{k+1}-")


# (15) Same local F in the deformation proof.
theory = must_replace(theory, r"with $F=\mathsf g_2^8$: $\|F\|_2=\|\mathsf g_2\|_{16}^8$ and $\|F'\|_2\le8\|\mathsf g_2\|_{16}^7\|\mathsf g_2'\|_{16}$,", r"with $\mathsf F=\mathsf g_2^8$: $\|\mathsf F\|_2=\|\mathsf g_2\|_{16}^8$ and $\|\mathsf F'\|_2\le8\|\mathsf g_2\|_{16}^7\|\mathsf g_2'\|_{16}$,")


# (16) Lemma s_bounds: the local L, U (one-sided values of S) are written S^-, S^+; L is the letter of the clock density.
old = r"\CGeqref{eq:s_bounds} reads $L+\frac12\le x\le U-\frac12$ with $x=s_k-\varpi(\gamma_k)/\pi$, $L=S(\gamma_k^-)$, $U=S(\gamma_k^+)$, and $U-L=\nu(\gamma_k)\ge1$. Put $m=\max(|L|,|U|)$. Then $x\le U-\frac12\le m-\frac12$ and $x\ge L+\frac12\ge-m+\frac12$, which is \CGeqref{eq:s_S_bound}."
new = r"\CGeqref{eq:s_bounds} reads $S^-+\frac12\le x\le S^+-\frac12$ with $x=s_k-\varpi(\gamma_k)/\pi$, $S^-=S(\gamma_k^-)$, $S^+=S(\gamma_k^+)$, and $S^+-S^-=\nu(\gamma_k)\ge1$. Put $\mathsf m=\max(|S^-|,|S^+|)$. Then $x\le S^+-\frac12\le\mathsf m-\frac12$ and $x\ge S^-+\frac12\ge-\mathsf m+\frac12$, which is \CGeqref{eq:s_S_bound}."
notation = must_replace(notation, old, new)

import importlib.util as _ilu, os as _os
_spec=_ilu.spec_from_file_location('edits_v3', _os.path.join(_os.path.dirname(_os.path.abspath(__file__)),'edits_v3.py')); _m=_ilu.module_from_spec(_spec); _spec.loader.exec_module(_m)
_ns={'must_replace':must_replace,'sub_block':sub_block,'theory':theory,'envelope':envelope,'external':external}
_m.apply(_ns); theory=_ns['theory']; envelope=_ns['envelope']; external=_ns['external']

# ---- bibliography: keep cited entries, add new ones
bib_start = next(i for i, l in enumerate(L) if l.startswith(r'\begin{thebibliography}'))
bib_end = next(i for i, l in enumerate(L) if l.startswith(r'\end{thebibliography}'))
entries = re.split(r'\n(?=\\bibitem\{)', '\n'.join(L[bib_start + 1:bib_end]).strip())
new_entries = {
 'Trudgian2010': r'\bibitem{Trudgian2010}' + '\n' + r'T.S. Trudgian, An improved upper bound for the argument of the Riemann zeta-function on the critical line, Math. Comp. 81 (278) (2012) 1053--1061, \href{https://doi.org/10.1090/S0025-5718-2011-02537-8}{https://doi.org/10.1090/S0025-5718-2011-02537-8}; preprint: A modest improvement on the function $S(T)$, arXiv:1010.4596 (2010).',
 'Fujii1981': r'\bibitem{Fujii1981}' + '\n' + r'A. Fujii, On the zeros of Dirichlet $L$-functions. II (with corrections to ``On the zeros of Dirichlet $L$-functions. I\textquotedblright\ and the subsequent papers), Trans. Amer. Math. Soc. 267 (1) (1981) 33--40. % VERIFICAR: volumen, paginas y DOI no comprobados en la fuente',
 'TrudgianYang2023': r'\bibitem{TrudgianYang2023}' + '\n' + r'T.S. Trudgian, A. Yang, Toward optimal exponent pairs, preprint, arXiv:2306.05599 (2023), \href{https://doi.org/10.48550/arXiv.2306.05599}{https://doi.org/10.48550/arXiv.2306.05599}.',
}
pieces = {}
for e in entries:
    m = re.match(r'\\bibitem\{([^}]+)\}', e)
    if m:
        pieces[m.group(1)] = e
pieces.update(new_entries)
body_all = '\n'.join([preamble, open(front).read(), notation, external, theory, envelope, open(back).read()])
cited = []
for m in re.finditer(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}', body_all):
    for k in m.group(1).split(','):
        k = k.strip()
        if k not in cited:
            cited.append(k)
missing = [k for k in cited if k not in pieces]
assert not missing, missing
order = [k for k in pieces if k in cited]          # keep v17 order (alphabetical), new ones appended
def sortkey(k):
    return re.sub(r'[^A-Za-z0-9]', '', k).lower()
order.sort(key=sortkey)
bib = '\\begin{thebibliography}{99}\n\n' + '\n\n'.join(pieces[k].strip() for k in order) + '\n\n\\end{thebibliography}\n'

appendix = '\\end{document}\n'
doc = '\n'.join([preamble, '', open(front).read(), notation, '', external, '', theory, '', '%' + '=' * 70, envelope, '', open(back).read(), bib, appendix])
defined = set(re.findall(r'\\label\{([^}]+)\}', doc))
out_rows = []
for r in doc.split('\n'):
    refs = re.findall(r'\\(?:CGref|CGeqref|ref|eqref)\{([^}]+)\}', r)
    if r.rstrip().endswith('\\\\') and ' & ' in r and refs and any(x not in defined for x in refs):
        continue
    out_rows.append(r)
doc = '\n'.join(out_rows)
doc = re.sub(r'\n{3,}', '\n\n', doc)
undef = sorted(set(x for x in re.findall(r'\\(?:CGref|CGeqref|ref|eqref)\{([^}]+)\}', doc) if x not in defined))
assert not undef, undef
open(out, 'w').write(doc)
print('written', out, len(doc.split('\n')), 'lines; cited', len(order), 'references')
