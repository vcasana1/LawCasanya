"""In-place corrections of prime_corrected_clock_v5.tex (author's review of v3, points 1, 4 and the secondary
references for the uniformity in k), applied by Claude on the author's order; no new version.
Usage: python3 patch_v5_claude.py TEX   (idempotent: refuses to run twice)."""
import sys
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__file__), '../../tools'))
import importlib.util, os
p = sys.argv[1]
t = open(p).read()
assert 'Korolev2016' not in t, 'already patched'


def rep(old, new):
    global t
    assert t.count(old) == 1, (old[:80], t.count(old))
    t = t.replace(old, new)


def sub_block(text, start, end, fn):
    i = text.index(start); j = text.index(end, i) + len(end)
    return text[:i] + fn(text[i:j]) + text[j:]


spec = importlib.util.spec_from_file_location('e4', os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../tools/edits_v4.py'))
e4 = importlib.util.module_from_spec(spec); spec.loader.exec_module(e4)
# reuse the text edits of edits_v4 except the envelope enclosure (v5 has its own interval verification)
ns = {'must_replace': lambda s, o, n, count=1: (s.replace(o, n) if s.count(o) == count else (_ for _ in ()).throw(AssertionError((o[:80], s.count(o))))),
      'theory': t, 'envelope': '', 'external': t}
src = open(spec.origin).read()
src = src[:src.index('    # ---- Theorem E: certified enclosure.')] + "    ns['theory'] = theory; ns['external'] = external\n"
src = src.replace("theory = ns['theory']; envelope = ns['envelope']; external = ns['external']", "theory = ns['theory']; external = ns['external']")
glb = {}
exec(src, glb)
ns2 = {'must_replace': ns['must_replace'], 'theory': t, 'envelope': '', 'external': t}
# theory edits
def apply_theory(text):
    n = {'must_replace': ns['must_replace'], 'theory': text, 'envelope': '', 'external': text}
    glb['apply'](n)
    return n
# apply on the full text: run once with theory=text, then copy the external replacement
n = apply_theory(t)
t_theory = n['theory']
# the external edit (references) was applied on the 'external' copy; reapply it on t_theory
old_ext = r"For $k=2$ this is the form used in Section~\CGref{sec:main_theorem}; $k=4$, with $Y_4=T^{1/320}$, and the general $k$ are used in Section~\CGref{sec:iteration}."
i = n['external'].index(old_ext); j = n['external'].index('\n', i)
new_ext = n['external'][i:j]
t = t_theory.replace(old_ext, new_ext, 1)
assert 'Korolev2016' in t
# abstract: constants
rep(r"iterated $\log^*T+O(1)$ times, with cutoffs depending only on $T$, locates the ordinates",
    r"iterated $\log^*T+O(1)$ times, with cutoffs depending only on $T$ through absolute constants that are not computed, locates the ordinates")
# bibliography entries, inserted before Korolev2012 / Radziwill alphabetically
rep(r"\bibitem{Korolev2012}", r"""\bibitem{Korolev2016}
M.A. Korolev, Gram\textquoteright s law in the theory of the Riemann zeta-function. Part 1, Sovrem. Probl. Mat. 20 (2015) 3--161; English transl.\ Proc. Steklov Inst. Math. 292, suppl.~2 (2016) S1--S146, \href{https://doi.org/10.4213/spm53}{https://doi.org/10.4213/spm53}. % VERIFICAR: Lema 3.13 citado a traves de Ivic--Korolev 2018

\bibitem{IvicKorolev2018}
A. Ivi\'c, M.A. Korolev, On the distribution of values of the argument of the Riemann zeta-function, preprint, arXiv:1808.10768 (2018), \href{https://doi.org/10.48550/arXiv.1808.10768}{https://doi.org/10.48550/arXiv.1808.10768}.

\bibitem{Radziwill2011}
M. Radziwi\l\l, Large deviations in Selberg\textquoteright s central limit theorem, preprint, arXiv:1108.5092 (2011), \href{https://doi.org/10.48550/arXiv.1108.5092}{https://doi.org/10.48550/arXiv.1108.5092}.

\bibitem{Korolev2012}""")
open(p, 'w').write(t)
print('patched', p)
