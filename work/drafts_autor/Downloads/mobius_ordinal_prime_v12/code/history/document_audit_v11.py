"""Static audit of the Version 11 package and LaTeX source."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
tex = (ROOT / 'mobius_ordinal_prime_transform_S_SS_v11.tex').read_text(encoding='utf-8')

labels = re.findall(r'\\label\{([^}]+)\}', tex)
refs = re.findall(r'\\(?:eqref|ref)\{([^}]+)\}', tex)
print('unique labels:', len(labels) == len(set(labels)), 'count=', len(labels))
missing = sorted(set(refs) - set(labels))
print('missing internal references:', missing)

sections = list(re.finditer(r'\\section\*?\{[^\n]+\}', tex))
unlabelled = []
for m in sections:
    frag = tex[m.end():m.end()+180]
    if '\\section*' not in m.group(0) and not re.search(r'\\label\{sec:[^}]+\}', frag):
        unlabelled.append(m.group(0))
print('unlabelled numbered sections:', unlabelled)

figrefs = re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}', tex)
missing_figs = [f for f in figrefs if not (ROOT / f).exists()]
print('figure references:', len(figrefs), 'missing:', missing_figs)

matlab = sorted(str(p.relative_to(ROOT)) for p in ROOT.rglob('*.m'))
print('MATLAB files in package:', matlab)

spanish_unicode = sorted(set(ch for ch in tex if ch in 'áéíóúÁÉÍÓÚñÑ¿¡'))
print('Spanish-specific Unicode characters in TeX:', spanish_unicode)

# Coordinate consistency checks for the corrected dynamics notation.
required = [
    r'A_j:=s_{\\alpha_j}',
    r'B_j:=s_{\\beta_j}',
    r'\\varphi\^{-1}\(p_j\)=\\{A_j,B_j\\}',
    r'\\Delta_j:=B_j-A_j',
]
for pat in required:
    print('contains', pat, bool(re.search(pat, tex)))

print('audit passed:', not missing and not unlabelled and not missing_figs and not matlab and not spanish_unicode)
