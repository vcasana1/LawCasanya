#!/usr/bin/env python3
"""v8 = v7 with the external results re-read in Fujii 1974 (page images), Fujii 1981 and Korolev 2016.

Run on a copy of ../v7/manuscript/prime_corrected_clock_v7.tex saved as the v8 file name.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
TEX = ROOT / 'manuscript' / 'prime_corrected_clock_v8.tex'
src = TEX.read_text()
head, sep, body = src.partition('\\begin{document}')
assert sep

def rep(old, new):
    global body
    n = body.count(old)
    if n != 1:
        sys.exit(f'expected 1 match, found {n}:\n{old[:200]}')
    body = body.replace(old, new)

def rep_re(pattern, new):
    global body
    m = list(re.finditer(pattern, body, re.S))
    if len(m) != 1:
        sys.exit(f'regex expected 1 match, found {len(m)}: {pattern[:120]}')
    body = body[:m[0].start()] + new + body[m[0].end():]

rep_re(r'% SOURCECHECK \(v7\):.*?Lemma 12 \(p\. 16\)\.\n',
       '% SOURCECHECK (v8): read in the original at the cited pages: Fujii 1974 (pp. 225, 226, 228--233;\n'
       '% p. 225 read on the page image, the OCR layer misreads the inequalities), Fujii 1975 (p. 140),\n'
       '% Fujii 1981 (pp. 33--34 and Section 5), Korolev 2016 (pp. S13, S123--S126),\n'
       '% Titchmarsh--Heath-Brown (p. 246 and Ch. IX), Korolev Publ. Inst. Math. 2012 (pp. 60, 67, 73),\n'
       '% Bellotti--Wong, Montgomery--Vaughan, Kinnunen, Ivic, Bourgain, Trudgian 2014,\n'
       '% Fazzari--Gerspach--Minelli, Tenenbaum, Di Plinio--Lerner (arXiv version, p. 1).\n')

rep('Fujii \\cite[p.~225]{Fujii1974} quotes Selberg\'s formula for $\\int_T^{T+H}$ with $T^{1/2+a}<H<T$, $0<a<\\frac14$; the form above is the sum of the cases $[T,\\frac32T]$ and $[\\frac32T,2T]$ with $H=\\frac T2$, since $(\\log\\log\\frac32T)^j=(\\log\\log T)^j+O_j((\\log\\log T)^{j-1}/\\log T)$.',
    'Fujii \\cite[p.~225]{Fujii1974} quotes Selberg\'s formula for $\\int_T^{T+H}$ with $T^{1/2+a}\\le H\\le T$; the form above is the case $H=T$.')

NEW = r'''\begin{theorem}[Selberg's formula with Fujii's bounds {\cite[\S3, pp.~232--233]{Fujii1974}}]\label{thm:known_fujii_selberg}
Let $a_2$ be fixed in the range of Fujii's Main Theorem \cite[p.~225]{Fujii1974}, which contains $\frac15$. There are $T_0$ and $C$, depending only on $a_2$, such that for $T\ge T_0$, $T^{1/2+a_2}\le H\le T$ and every integer $k\ge1$ with $x_{\rm F}=T^{a_2/(60k)}\ge2$,
\begin{equation}
\int_T^{T+H}\bigl(S(t)-S^{\rm pr}_{x_{\rm F}^3}(t)\bigr)^{2k}dt\le(Ck^2)^{2k}H .
\label{eq:fujii_selberg}
\end{equation}
\end{theorem}
For the Riemann zeta function (the principal character, $q=1$), \cite[p.~232]{Fujii1974} writes Selberg's formula \cite{Selberg1946b} for $x\ge2$ as $S(t)=S^{\rm pr}_{x^3}(t)+\sum_{i=1}^5O(B_i(t))$, with five explicit functions $B_i$ and absolute implied constants, and uses it with $x=T^{a_2/(60k)}$. On p.~233 it bounds the norms $(\int_T^{T+H}|B_i|^{2k})^{1/2k}$ by $k^{1/2}H^{1/2k}$ for $i=1,4$, by $k^2H^{1/2k}$ for $i=2,3$ and by at most $k^{3/2}H^{1/2k}$ for $i=5$, under the hypotheses of its Main Theorem, which for $q=1$ are $T^{1/2+a_2}\le H\le T$. By the remark on p.~226, the implied constants in that paper do not depend on $q$, $k$ and $h$. Fujii states no range for $k$; $x_{\rm F}\ge2$ is the condition under which he quotes Selberg's formula. Minkowski's inequality gives \CGeqref{eq:fujii_selberg}. Part~II \cite[\S\S1 and 5]{Fujii1981} lists the corrections to Part~I: in the Main Theorem $h$ must be bounded and the exponent of $Ak$ in the error term is $2k$; the remainder terms of Lemma~2 (p.~228) and of the first case of Lemma~3 (p.~230) are to be multiplied by $k^2$, and $k!$ in Lemma~2 replaced by $(Ak)^k$; items (iii) and (iv) of p.~234 are withdrawn. None of them concerns Selberg's formula on p.~232 or the bounds of p.~233 used above.

\begin{lemma}[Selberg's approximation uniformly in the order]\label{lem:selberg_uniform}
Let $\kappa_{\rm F}=1/(300\log2)$ and $Y_k=T^{1/(80k)}$. There are absolute constants $C$ and $T_0$ such that for $T\ge T_0$ and every integer $k$ with $1\le k\le\kappa_{\rm F}\log T$,
\begin{equation}
\int_T^{2T}\bigl(S(t)-S^{\rm pr}_{Y_k}(t)\bigr)^{2k}dt\le(Ck^2)^{2k}\,T .
\label{eq:selberg_uniform}
\end{equation}
In particular $\int_T^{2T}(S-S^{\rm pr}_{Y_0})^4\ll T$ with $Y_0=Y_2=T^{1/160}$.
\end{lemma}

\begin{proof}
Take $a_2=\frac15$ and $H=T$ in Theorem~\CGref{thm:known_fujii_selberg}; its constants are then absolute, and $x_{\rm F}=T^{1/(300k)}\ge2$ because $k\le\kappa_{\rm F}\log T$. It remains to lengthen the prime sum from $x_{\rm F}^3=T^{1/(100k)}\ge8$ to $Y_k=T^{1/(80k)}$. Here $S^{\rm pr}_{x_{\rm F}^3}-S^{\rm pr}_{Y_k}=\frac1\pi\Im\mathcal D$ with $\mathcal D(t)=\sum_{p\in\mathcal J'}p^{-1/2-it}$, $\mathcal J'$ the primes in $[x_{\rm F}^3,Y_k)$. As $\log Y_k/\log x_{\rm F}^3=\frac54$, Theorem~\CGref{thm:known_mertens} gives $\sum_{p\in\mathcal J'}p^{-1}\le\log\frac54+O(1)\le V'$ with an absolute $V'$. Next, $\mathcal D^k=\sum_n\eta_nn^{-it}$ over products of $k$ primes of $\mathcal J'$, so $n\le Y_k^k=T^{1/80}$, and $\sum_n|\eta_n|^2\le k!\,V'^k$, since each $n$ has at most $k!$ ordered factorizations; Theorem~\CGref{thm:known_MV} on $[T,2T]$ gives $\int_T^{2T}|\mathcal D|^{2k}\le k!\,V'^k(T+O(T^{1/80}))\le(C'k)^kT$. Minkowski's inequality in $L^{2k}(T,2T)$ gives $\|S-S^{\rm pr}_{Y_k}\|_{2k}\le(Ck^2+\sqrt{C'k})T^{1/2k}$, which is \CGeqref{eq:selberg_uniform}.
\end{proof}

\begin{remark}[An independent route to the uniformity in the order]\label{rem:korolev_uniform}
Korolev \cite[Lemma~3.13, p.~S126]{Korolev2016} proves, under the conditions of his Lemma~3.11 (p.~S124) and the conventions of pp.~S13 and S123: for fixed $0<\varepsilon_{\rm K}<10^{-3}$, $c_0=2880\varepsilon_{\rm K}^{-1}$, $T_1\ge T_0(\varepsilon_{\rm K})$, $T_1^{27/82+0.9\varepsilon_{\rm K}}\le H\le T_1^{27/82+\varepsilon_{\rm K}}$, $Y_{\rm K}'=T_1^{0.1\varepsilon_{\rm K}}$, integers $1\le k\le c_{\rm K}\log Y_{\rm K}'$ with a sufficiently small absolute constant $c_{\rm K}>0$ not given numerically, and $Y_{\rm K}=(Y_{\rm K}')^{1/(8k+3)}$,
\begin{equation}
\int_{T_1}^{T_1+H}\Bigl|S(t)+\frac1\pi\sum_{p\le Y_{\rm K}}\frac{\sin(t\log p)}{\sqrt p}\Bigr|^{2k}dt<\frac{c_0}{56}\,(c_0k)^{2k}H .
\label{eq:korolev_lemma}
\end{equation}
(The quotation in \cite[Lemma~12, p.~16]{IvicKorolev2018} omits the factor $k^{2k}$.) For a fixed $\varepsilon_{\rm K}$ this gives \CGeqref{eq:selberg_uniform}, even with $(Ck)^{2k}$ in place of $(Ck^2)^{2k}$, for $1\le k\le0.1c_{\rm K}\varepsilon_{\rm K}\log T$, after three adaptations. (i) \emph{Cutoff.} $S+\frac1\pi\sum_{p\le Y_{\rm K}}p^{-1/2}\sin(t\log p)=S-S^{\rm pr}_{Y_k}-\frac1\pi\sum_{Y_{\rm K}<p<Y_k}p^{-1/2}\sin(t\log p)$, and $1<\log Y_k/\log Y_{\rm K}=\frac{(8k+3)\log T}{8k\,\varepsilon_{\rm K}\log T_1}\le\frac{11}{8\varepsilon_{\rm K}}$ for $T\le T_1\le3T$; so the primes between $Y_{\rm K}$ and $Y_k$ have $\sum p^{-1}\le\log\frac{11}{8\varepsilon_{\rm K}}+O(1)$, and Theorem~\CGref{thm:known_MV} on $[T_1,T_1+H]$, applicable since $Y_k^k=T^{1/80}\le H$, bounds their sum in $L^{2k}(T_1,T_1+H)$ by $C_{\varepsilon_{\rm K}}\sqrt k\,H^{1/2k}$, as in the proof of Lemma~\CGref{lem:selberg_uniform}. (ii) \emph{Short intervals.} Cover $[T,2T]$ by consecutive intervals $[T_1,T_1+H]$ with the common length $H=T^{27/82+0.95\varepsilon_{\rm K}}$, which is admissible for every $T_1\in[T,3T]$ once $T\ge T_0(\varepsilon_{\rm K})$. Each interval has its own $Y_{\rm K}=Y_{\rm K}(T_1)$, and (i) is applied on each interval before summing, so that the sum is over the same polynomial $S^{\rm pr}_{Y_k}$. (iii) \emph{Range of orders.} The condition $k\le c_{\rm K}\log Y'_{\rm K}=0.1c_{\rm K}\varepsilon_{\rm K}\log T_1$ follows from $k\le0.1c_{\rm K}\varepsilon_{\rm K}\log T$. Along this route $\kappa_{\rm F}$ is replaced by the unspecified absolute constant $0.1c_{\rm K}\varepsilon_{\rm K}$; Theorems~\CGref{thm:tails} and \CGref{thm:uniform_iteration} below need only some absolute constant in that place, with $300$ replaced by $1/(0.1c_{\rm K}\varepsilon_{\rm K}\log2)$ in the choice of $C_8$. Uniform bounds of the same shape at the Gram points $t_n$, for $\sum_n(S(t_n+0)+\frac1\pi\sum_{p<y}p^{-1/2}\sin(t_n\log p))^{2k}$ and for the moments of $S(t_n+0)-S(t_{n-1}+0)$, are \cite[Lemma~2.4, p.~60, and Thm.~3.2, p.~67]{KorolevPIM2012}; they concern sums over Gram points and are not used here.
\end{remark}

\begin{theorem}[Fujii {\cite[($\alpha'$), p.~33]{Fujii1981}}]\label{thm:known_fujii_difference}
There are absolute constants $A$ and $T_0$ such that for every integer $k\ge1$, $T\ge T_0$ and $h>0$,
\[
\int_T^{2T}\bigl(S(t+h)-S(t)\bigr)^{2k}dt\ll(Ak)^kT\Bigl(\log\bigl(((h\wedge1)\log T+3)\,e^k\bigr)\Bigr)^k,\qquad h\wedge1=\min\{h,1\},
\]
with an absolute implied constant; the interval $(T,2T)$ may be replaced by $(0,T)$ \cite[p.~34, footnote]{Fujii1981}.
\end{theorem}
This is Fujii's corrected form of the moment estimate of \cite[Main Theorem, p.~225]{Fujii1974}, announced in \cite[Lemma, p.~140]{Fujii1975}; for bounded $h$ it is also stated in \cite[(9.25.3), p.~246]{Titchmarsh1986}, there with $0\le h\le\frac12T$, whereas \cite[\S5-1]{Fujii1981} requires $h$ to be bounded in the asymptotic formula. Only $k=1,2$ and $0<h\le1$ are used (Lemma~\CGref{lem:zero_pairs}), in the form
\begin{equation}
\int_{T-1}^{2T}\bigl(S(t+h)-S(t)\bigr)^{2k}dt\le C\,T\bigl(\log(2+h\log T)\bigr)^k\qquad(k=1,2,\ 0<h\le1,\ T\ge T_0),
\label{eq:fujii_difference}
\end{equation}
which follows from the theorem on $(T/2,T)$ and $(T,2T)$, since $\log((h\log T+3)e^k)\le k+\log(3+h\log T)\le(2k+2)\log(2+h\log T)$.'''
rep_re(r"\\begin\{theorem\}\[Selberg's formula with Fujii's bounds.*?since \$\\log\(3\+h\\log2T\)\\le\\log\(4\+h\\log T\)\\le2\\log\(2\+h\\log T\)\$\.", NEW)

for bad in ('not been able to consult', '<H<T', 'have not seen the original', 'C\\sqrt k)^{2k}'):
    assert bad not in body, bad
TEX.write_text(head + sep + body)
print('patched', TEX)
