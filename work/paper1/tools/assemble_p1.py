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
               r'$y_0$, $w_T$', r'$\mathcal A_{T,p}$', r'$\mathcal H_n(t)$', r'$f_T$', r'$\mathfrak K_\theta$',
               r'$\BW(t)$', r'$N^+(\sigma,t)$']
rows = notation.split('\n')
labels_removed = set()
keep_rows = []
for r in rows:
    if any(r.startswith(d) for d in drop_starts):
        continue
    keep_rows.append(r)
notation = '\n'.join(keep_rows)

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
    r'Earlier explicit versions are due to Trudgian \cite{Trudgian2014} and to Hasanalizade, Shen and Wong \cite{HasanalizadeShenWong2022}. For $T$ sufficiently large, Trudgian \cite[Thm.~2 and \S5]{Trudgian2010} proved $|S(T)|\le0.1013\log T$ with Huxley\textquoteright s exponent $\frac{32}{205}$ for $\zeta(\frac12+it)$.')

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
new_prof = (r'\emph{The profile.} Let $\varepsilon'+"'"+r'>0$, $(\mathsf k_0,\mathsf l_0)=(\frac{13}{84}+\varepsilon'+"'"+r',\frac{55}{84}+\varepsilon'+"'"+r')$ and $(\mathsf k_j,\mathsf l_j)=A^j(\mathsf k_0,\mathsf l_0)$ for $1\le j\le J$, exponent pairs by Theorem~\CGref{thm:known_exponents}(a),(c), with $\mathsf l_j-\mathsf k_j\ge\frac12$; by (b), $|\zeta(\mathsf l_j-\mathsf k_j+it)|\ll|t|^{\mathsf k_j}\log|t|$, and $|\zeta(1+it)|\ll\log|t|$. The points $(\mathsf l_j-\mathsf k_j,\mathsf k_j)$ and $(1,0)$ have decreasing ordinates, and Theorem~\CGref{thm:known_PL} between consecutive points gives the hypothesis of the theorem for the piecewise linear function through them. For $\varepsilon'+"'"+r'=0$ these are the vertices of $\mathfrak e_J$; the right side of \CGeqref{eq:envelope_formula} depends continuously on $\varepsilon'+"'"+r'$, so $\mathfrak a\le C_J$. On each linear piece $\mathfrak e(\sigma)=\alpha\sigma+\beta$ of $[0,1]$ a primitive of $\mathfrak e(\sigma)/\sqrt{\sigma(2-\sigma)}$ is $-\alpha\sqrt{\sigma(2-\sigma)}+(\alpha+\beta)\arcsin(\sigma-1)$, and the values of $C_J$ at the rational vertices are computed from it at $50$ digits by \texttt{opc\_envelope\_iterations\_p1.py}; the value $C_7$ agrees with the quadrature of \texttt{opc\_envelope\_coefficient\_v14.py}. Each new vertex lies below the chord from the previous one to $(1,0)$, so $C_J$ decreases. Multiply by $2\pi$ and use Proposition~\CGref{prop:envelope_equivalence}(a).' + '\n')
envelope = envelope.replace(old_prof, new_prof)
old_rem = envelope[envelope.index(r'\begin{remark}\label{rem:envelope_inputs}'):envelope.index(r'\end{remark}', envelope.index(r'\begin{remark}\label{rem:envelope_inputs}')) + len(r'\end{remark}')]
new_rem = (r'\begin{remark}\label{rem:envelope_inputs}' + '\n' +
    r'(a) Trudgian \cite[\S5]{Trudgian2010} obtained $\mathfrak a\le0.1013$ from Huxley\textquoteright s exponent $\frac{32}{205}$ at $\sigma=\frac12$ by the same method; Theorem~\CGref{thm:envelope} replaces the exponents and lets the parameters of the disc tend to their limits. With the explicit exponents used by Bellotti and Wong ($\frac{27}{164}$ at $\sigma=\frac12$, Yang\textquoteright s lines $\sigma_j=1-j/(2^j-2)$ with exponents $1/(2^j-2)$, $4\le j\le9$ \cite{BellottiWong2025}) and linear interpolation between $\sigma=0$ and $\sigma=\frac12$, as in \cite[\S3.1]{BellottiWong2025}, the right side of \CGeqref{eq:envelope_formula} is $0.10074$, the limit of their $C_1=0.10076$ as their parameters tend to $(1,1)$; the same right-hand profile reflected by the functional equation gives $0.09783$. (b) Profiles of $\mu(\sigma)$ below $\mathfrak e_J$ are known: Trudgian and Yang \cite{TrudgianYang2023} close a convex hull of known exponent pairs, Bourgain\textquoteright s among them, under the $A$-, $B$- and $C$-processes and deduce piecewise bounds for $\mu(\sigma)$ on $[\frac12,1]$. Any such profile can be inserted in \CGeqref{eq:envelope_formula}; we do not evaluate it here. (c) For the Lindel\"of profile ($\mathfrak e=0$ on $[\frac12,1]$) the right side is $0.07863$: Backlund\textquoteright s method with a disc cannot give less, whatever the exponents. (d) Theorem~\CGref{thm:envelope} is asymptotic: the explicit constants of the bounds for $\zeta$ do not enter, which is why non-explicit exponents may be used, and it does not replace the explicit bounds of \cite{BellottiWong2025}, valid for all $T\ge e$.' + '\n' + r'\end{remark}')
envelope = envelope.replace(old_rem, new_rem)

# ---- bibliography: keep cited entries, add new ones
bib_start = next(i for i, l in enumerate(L) if l.startswith(r'\begin{thebibliography}'))
bib_end = next(i for i, l in enumerate(L) if l.startswith(r'\end{thebibliography}'))
entries = re.split(r'\n(?=\\bibitem\{)', '\n'.join(L[bib_start + 1:bib_end]).strip())
new_entries = {
 'Trudgian2010': r'\bibitem{Trudgian2010}' + '\n' + r'T.S. Trudgian, A modest improvement on the function $S(T)$, preprint, arXiv:1010.4596 (2010), \href{https://doi.org/10.48550/arXiv.1010.4596}{https://doi.org/10.48550/arXiv.1010.4596}.',
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

appendix = r'''
\appendix
\section{Programs}
\label{app:programs}
The two programs below are in the directory \texttt{work/paper1/code/} of the repository and are reproduced verbatim. They read no data. The first, \texttt{opc\_envelope\_\allowbreak coefficient\_v14.py}, evaluates \CGeqref{eq:envelope_formula} by $40$-digit quadrature for the profiles of Remark~\CGref{rem:envelope_inputs} and for $\mathfrak e_7$; the second, \texttt{opc\_envelope\_\allowbreak iterations\_p1.py}, evaluates it in closed form for $\mathfrak e_J$, $0\le J\le30$. They run under Python 3 with mpmath.

\subsection{\texttt{opc\_envelope\_coefficient\_v14.py}}
\proglisting{opc_envelope_coefficient_v14.py}

\subsection{\texttt{opc\_envelope\_iterations\_p1.py}}
\proglisting{opc_envelope_iterations_p1.py}

\end{document}
'''
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
