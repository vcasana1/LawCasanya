"""Static audit of the v12 source, including its independent chapter."""
from collections import Counter
from pathlib import Path
import re
import json

ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / "mobius_ordinal_prime_transform_S_SS_v12.tex"


def expand(path):
    text = path.read_text(encoding="utf-8")
    def include(match):
        name = match.group(1)
        p = ROOT / (name if name.endswith(".tex") else name+".tex")
        return expand(p)
    return re.sub(r"\\input\{([^}]+)\}", include, text)


def audit():
    tex = expand(MAIN)
    labels = re.findall(r"\\label\{([^}]+)\}", tex)
    refs = re.findall(r"\\(?:eqref|ref)\{([^}]+)\}", tex)
    cites = set(k.strip() for group in
                re.findall(r"\\cite(?:\[[^]]*\])?\{([^}]+)\}", tex)
                for k in group.split(","))
    bib = re.findall(r"\\bibitem(?:\[[^]]*\])?\{([^}]+)\}", tex)
    duplicates = sorted(k for k, v in Counter(labels).items() if v > 1)
    missing = sorted(set(refs) - set(labels))
    sections = list(re.finditer(r"\\section\*?\{[^\n]+\}", tex))
    unlabelled = []
    for m in sections:
        frag = tex[m.end():m.end()+180]
        if r"\section*" not in m.group(0) and not re.search(r"\\label\{sec:[^}]+\}", frag):
            unlabelled.append(m.group(0))
    figs = re.findall(r"\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}", tex)
    missing_figs = [f for f in figs if not (ROOT / f).exists()]
    missing_cites = sorted(cites-set(bib))
    duplicate_bib = sorted(k for k, v in Counter(bib).items() if v > 1)
    matlab = sorted(str(p.relative_to(ROOT)) for p in ROOT.rglob("*.m"))
    result = {
        "version": 12, "labels": len(labels), "duplicate_labels": duplicates,
        "missing_references": missing, "unlabelled_sections": unlabelled,
        "figure_count": len(figs), "missing_figures": missing_figs,
        "bibliography_count": len(bib), "missing_citations": missing_cites,
        "duplicate_bibliography": duplicate_bib, "MATLAB_files": matlab,
    }
    result["passed"] = not any([duplicates, missing, unlabelled, missing_figs,
                               missing_cites, duplicate_bib, matlab])
    print(json.dumps(result, indent=2))
    (ROOT / "outputs" / "v12_document_audit.json").write_text(
        json.dumps(result, indent=2)+"\n", encoding="utf-8")
    assert result["passed"], "Document source audit failed"
    return result


if __name__ == "__main__":
    audit()
