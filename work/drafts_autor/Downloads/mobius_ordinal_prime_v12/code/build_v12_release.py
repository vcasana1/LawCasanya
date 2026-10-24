"""Produce standalone sources and compile v12 with pdflatex.

The submission TeX and chapter TeX are flattened exports; edit the root
manuscript and chapters/ source instead.
"""
from pathlib import Path
import re
import shutil
import subprocess
from document_audit import expand, audit

ROOT = Path(__file__).resolve().parents[1]
STEM = "mobius_ordinal_prime_transform_S_SS_v12"
CHAPTER = "alpha_research_program_v12"


def generate_sources():
    source = (ROOT / (STEM+".tex")).read_text(encoding="utf-8")
    fragment = (ROOT / "chapters" / (CHAPTER+".tex")).read_text(encoding="utf-8")
    flat = expand(ROOT / (STEM+".tex"))
    (ROOT / "submission" / (STEM+".tex")).write_text(
        flat.replace("{figures/", "{"), encoding="utf-8")
    for figure in (ROOT / "figures").glob("*.png"):
        shutil.copy2(figure, ROOT / "submission" / figure.name)
    preamble = source.split(r"\begin{document}", 1)[0]
    preamble = re.sub(r"\\title\{[^\n]*\}",
                      lambda _: r"\title[Research programme through alpha]"
                      r"{Research Programme through Alpha:"
                      r" Exact Pairing, Energy and Analytic Obligations}", preamble)
    bibliography = source.split(r"\begin{thebibliography}", 1)[1]
    bibliography = bibliography.split(r"\end{thebibliography}", 1)[0]
    items = re.findall(
        r"(\\bibitem\{([^}]+)\}.*?)(?=\\bibitem|\Z)",
        bibliography, re.S)
    cited = {k.strip() for group in re.findall(r"\\cite\{([^}]+)\}", fragment)
             for k in group.split(",")}
    chosen = "\n".join(item.strip() for item, key in items if key in cited)
    doc = (preamble + "\n" + r"\begin{document}" + "\n"
           + r"\maketitle" + "\n"
           + "Independent chapter of Version 12. The results below do not"
             " constitute a proof of RH.\n\n"
           + r"\setcounter{tocdepth}{2}" + "\n"
           + r"\tableofcontents" + "\n" + r"\clearpage" + "\n\n"
           + fragment + "\n"
           + r"\begin{thebibliography}{99}" + "\n" + chosen + "\n"
           + r"\end{thebibliography}" + "\n"
           + r"\end{document}" + "\n")
    (ROOT / (CHAPTER+".tex")).write_text(doc, encoding="utf-8")


def compile_pdf(stem):
    for stage in range(1, 4):
        log = ROOT / "outputs" / ("v12_"+stem+"_pdflatex_pass"+str(stage)+".txt")
        with log.open("w", encoding="utf-8") as fh:
            subprocess.run(
                ["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                 "-file-line-error", stem+".tex"],
                cwd=ROOT, stdout=fh, stderr=subprocess.STDOUT, check=True)
        pdf_bytes = (ROOT / (stem+".pdf")).read_bytes()
        if not pdf_bytes.rstrip().endswith(b"%%EOF"):
            raise RuntimeError("Truncated PDF after pass "+str(stage)+": "+stem)
    print("Compiled", stem+".pdf", flush=True)


def main():
    generate_sources()
    audit()
    compile_pdf(STEM)
    compile_pdf(CHAPTER)
    shutil.copy2(ROOT / (STEM+".pdf"), ROOT / "submission" / (STEM+".pdf"))
    old = ROOT / "submission" / "mobius_ordinal_prime_transform_S_SS_v11.pdf"
    if old.exists():
        target = ROOT / "outputs" / "inherited_v11_submission_reference.pdf"
        if not target.exists():
            shutil.copy2(old, target)
        old.unlink()


if __name__ == "__main__":
    main()
