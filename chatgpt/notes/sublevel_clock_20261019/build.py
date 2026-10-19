#!/usr/bin/env python3
"""Compile the research note and verify its source and PDF structure.

This program performs document checks only. It never reads zero datasets
and does not select or fit mathematical parameters.
"""
from pathlib import Path
import hashlib
import json
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parent
STEM = "prime_sublevel_clock"
source = ROOT / (STEM + ".tex")
copy = ROOT / (STEM + ".txt")
shutil.copyfile(source, copy)
with (ROOT / "build.log").open("w", encoding="utf-8") as transcript:
    for pass_number in range(1, 4):
        result = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", source.name],
            cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
        )
        transcript.write(f"Compilation pass {pass_number}\n")
        transcript.write(result.stdout)
        transcript.flush()
        if result.returncode:
            raise SystemExit(f"pdflatex failed on pass {pass_number}; see build.log")
log = (ROOT / (STEM + ".log")).read_text(encoding="utf-8", errors="replace")
for pattern in (
    r"LaTeX Warning: (?:Reference|Citation) .* undefined",
    r"There were undefined references",
    r"Label\(s\) may have changed",
    r"Overfull \\[hv]box",
):
    if re.search(pattern, log):
        raise SystemExit(f"Unresolved document check: {pattern}")
if source.read_bytes() != copy.read_bytes():
    raise SystemExit("TEX/TXT mismatch")
metadata = {
    "tex_txt_identical": True,
    "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
    "pdf_sha256": hashlib.sha256((ROOT / (STEM + ".pdf")).read_bytes()).hexdigest(),
    "compilation_passes": 3,
    "unresolved_references": False,
    "overfull_boxes": False,
    "zero_datasets_read": False,
    "numerical_experiments": False,
}
try:
    from pypdf import PdfReader
except ImportError:
    metadata["pdf_structure_check"] = "pypdf unavailable; omitted"
else:
    pdf = PdfReader(ROOT / (STEM + ".pdf"))
    annotations = [item.get_object() for page in pdf.pages for item in page.get("/Annots", [])]
    metadata.update({
        "pdf_pages": len(pdf.pages),
        "hyperlinks": sum(item.get("/Subtype") == "/Link" for item in annotations),
        "tooltip_widgets": sum(item.get("/Subtype") == "/Widget" and bool(item.get("/TU")) for item in annotations),
        "outline_entries": len(pdf.outline),
    })
    if metadata["tooltip_widgets"] < 1 or metadata["hyperlinks"] < 1 or metadata["outline_entries"] < 1:
        raise SystemExit("Missing PDF navigation or tooltip structure")
(ROOT / "build_metadata.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
print(json.dumps(metadata, indent=2))
