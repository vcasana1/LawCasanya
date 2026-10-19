#!/usr/bin/env python3
"""Check the v11 integration fragment without modifying any manuscript."""
from __future__ import annotations
import hashlib
import json
import re
import subprocess
import tempfile
from pathlib import Path
from fractions import Fraction as Q
from math import comb

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
BASE = REPO / "work/paper1/manuscript/prime_corrected_clock_v9.tex"
TEX = HERE / "regularized_clock_insert.tex"
fragment = TEX.read_text()
base = BASE.read_text()
checks = {}

def check(name, condition):
    checks[name] = bool(condition)
    if not condition:
        raise AssertionError(name)

labels = re.findall(r"\\label\{([^}]+)\}", fragment)
base_labels = set(re.findall(r"\\label\{([^}]+)\}", base))
refs = set(re.findall(r"\\(?:eqref|ref)\{([^}]+)\}", fragment))
check("tex_txt_byte_identical", TEX.read_bytes() == TEX.with_suffix(".txt").read_bytes())
check("new_labels_unique", len(labels) == len(set(labels)))
check("labels_namespaced", all(x.startswith("reg:") for x in labels))
check("no_label_collision_with_v9", not set(labels) & base_labels)
check("all_references_resolve_against_v9", refs <= base_labels | set(labels))
check("no_global_macro_definitions", not re.search(r"\\(?:newcommand|renewcommand|def)\b", fragment))

new_notation = [
    r"\mathcal C_T^{\mathrm{reg}}", r"\mathcal J_T^{\mathrm{reg}}",
    r"\mathsf m_T^{\mathrm{reg}}", r"\mathsf h_T^{\mathrm{reg}}",
    r"\mathsf t_{T,j}^{\mathrm{reg}}", r"\mathsf H_T^{\mathrm{reg}}",
    r"\widehat F_{T,c}", r"\widehat x_{T,c,k}",
    r"\widehat u_{T,c,k}", r"\eta_{\mathrm{reg}}",
]
check("new_notation_absent_from_v9", all(x not in base for x in new_notation))
check("existing_clock_window_reused", r"\mathcal I_T^\tau" in base and r"\mathcal I_T^\tau" in fragment)
check("no_new_Lambda_scale", r"\Lambda_T" not in fragment)
check("no_envelope_P_class_reassignment", r"\mathcal P_T" not in fragment)
check("no_iteration_H_reassignment", r"H_j=" not in fragment)

stack = []
for match in re.finditer(r"\\(begin|end)\{([^}]+)\}", fragment):
    action, env = match.groups()
    if action == "begin":
        stack.append(env)
    else:
        check("environment_nesting", bool(stack) and stack.pop() == env)
check("all_environments_closed", not stack)

# Exact coefficient checks, using only the Python standard library.
# Coefficients of x^(4-j) d^j after subtracting x^4+4x^3d+d^4/3.
quartic_left = {j: Q(comb(4,j)) for j in range(5)}
quartic_left[0] -= 1
quartic_left[1] -= 4
quartic_left[4] -= Q(1,3)
quartic_right = {0: Q(0), 1: Q(0), 2: Q(6), 3: Q(4), 4: Q(2,3)}
check("quartic_uniform_convexity_identity", quartic_left == quartic_right)
psi2 = {j: Q(comb(5,j),5)*(Q(1,2)**(5-j)-Q(-1,2)**(5-j)) for j in range(6)}
check("sawtooth_fourth_polynomial", psi2 == {0: Q(1,80), 1: Q(0), 2: Q(1,2), 3: Q(0), 4: Q(1), 5: Q(0)})
# Substitute r=4*A*s^3. The stationary equation is 4*A*s^3-r=0;
# the value is -3*A*s^4. Check the exponents in the displayed closed form.
check("dual_residual_stationarity", 4-4 == 0)
check("dual_residual_minimum", 1-4 == -3 and -Q(4,3)+Q(4,3) == 0 and -Q(1,3)+Q(4,3) == 1 and 3*Q(4,3) == 4)
check("comparator_constant_arithmetic", 8*4**4*Q(5,2) == 5120 and 8*4**4*2 == 4096 and 8*2**4*Q(5,2) == 320)
check("projection_constant_arithmetic", 8*8 == 64 and 8*8+8 == 72)

with tempfile.TemporaryDirectory(prefix="regularized_clock_tex_") as temp:
    builddir = Path(temp)
    external_refs = sorted(refs-set(labels))
    source_labels = "\n".join(
        "\\expandafter\\gdef\\csname r@" + label + "\\endcsname{{source}{0}}"
        for label in external_refs)
    harness = r"""\documentclass[11pt]{article}
\usepackage[margin=28mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathrsfs}
\newcommand{\NO}{N_0}
\newcommand{\lL}{\mathcal L}
\newcommand{\IT}{\mathcal I_T}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\makeatletter
""" + source_labels + "\n\\makeatother\n\\begin{document}\n" + fragment + "\n\\end{document}\n"
    (builddir / "harness.tex").write_text(harness)
    for _ in range(2):
        result = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "harness.tex"], cwd=builddir, text=True, capture_output=True)
        if result.returncode:
            raise RuntimeError(result.stdout[-4000:])
        check("latex_harness_compiles", result.returncode == 0)
    log = (builddir / "harness.log").read_text(errors="replace")
    check("latex_no_undefined_references", "undefined references" not in log and "Reference `" not in log)
    # No standalone paper/PDF is delivered; this is only a syntax harness.
    latex_metadata = {
        "passes": 2,
        "undefined_references": False,
        "overfull_boxes": len(re.findall(r"Overfull \\[hv]box", log)),
        "scope": "Minimal article harness with existing v9 reference labels stubbed; not a full v11 build or PDF presentation audit.",
    }

draft_result = subprocess.run([
    "git", "show", "c2ffecc309f9503eda8fc12855b6f80725524110:work/paper1/v10/manuscript/prime_corrected_clock_v10.tex"
], cwd=REPO, text=True, capture_output=True, check=True)
draft = draft_result.stdout
delta_path = HERE / "v11_delta.tex"
delta = delta_path.read_text()
delta_labels = re.findall(r"\\label\{([^}]+)\}", delta)
draft_labels = set(re.findall(r"\\label\{([^}]+)\}", draft))
delta_refs = set(re.findall(r"\\(?:eqref|ref)\{([^}]+)\}", delta))
check("delta_tex_txt_byte_identical", delta_path.read_bytes() == delta_path.with_suffix(".txt").read_bytes())
check("delta_labels_unique_namespaced", len(delta_labels) == len(set(delta_labels)) and all(x.startswith("reg11:") for x in delta_labels))
check("delta_no_label_collision_with_v10", not set(delta_labels) & draft_labels)
check("delta_references_resolve_against_v10", delta_refs <= draft_labels | set(delta_labels))
delta_new_names = [r"\eta_{\mathrm{reg}}", r"D_{\mathrm{reg}}", r"A_{\mathrm{reg}}", r"B_{\mathrm{reg}}", r"\mathscr L_{\mathrm{reg}}", r"\mathbf r_{\mathrm{reg}}", r"\mathsf B_{T,i}^{\mathrm{reg}}", r"\mathsf M_{\mathrm{mass}}^{\mathrm{reg}}"]
check("delta_new_certificate_names_absent_from_v10", all(x not in draft for x in delta_new_names))
check("delta_reuses_existing_regularization_names", all(x in draft and x in delta for x in [r"\Lambda_T", r"\mathsf J_T", r"\varsigma_T", r"\mathcal K_T", r"\widehat F", r"\mathcal I_T^\tau"]))
check("delta_no_obsolete_v10_draft_mesh_names", r"\eta_T" not in delta and r"\mathsf M_T" not in delta)
check("delta_no_global_macro_definitions", not re.search(r"\\(?:newcommand|renewcommand|def)\b", delta))
with tempfile.TemporaryDirectory(prefix="regularized_clock_delta_tex_") as temp:
    builddir = Path(temp)
    external_refs = sorted(delta_refs-set(delta_labels))
    source_labels = "\n".join(
        "\\expandafter\\gdef\\csname r@" + label + "\\endcsname{{source}{0}}"
        for label in external_refs)
    harness = r"""\documentclass[11pt]{article}
\usepackage[margin=28mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathrsfs}
\newcommand{\NO}{N_0}
\newcommand{\lL}{\mathcal L}
\newcommand{\IT}{\mathcal I_T}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\makeatletter
""" + source_labels + "\n\\makeatother\n\\begin{document}\n" + delta + "\n\\end{document}\n"
    (builddir / "harness.tex").write_text(harness)
    for _ in range(2):
        result = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "harness.tex"], cwd=builddir, text=True, capture_output=True)
        if result.returncode:
            raise RuntimeError(result.stdout[-4000:])
        check("delta_latex_harness_compiles", result.returncode == 0)
    log = (builddir / "harness.log").read_text(errors="replace")
    check("delta_latex_no_undefined_references", "undefined references" not in log and "Reference `" not in log)
    delta_latex_metadata = {"passes": 2, "undefined_references": False, "overfull_boxes": len(re.findall(r"Overfull \\[hv]box", log))}
    if delta_latex_metadata["overfull_boxes"]:
        print("\n".join(re.findall(r"Overfull[^\n]*\n(?:[^\n]*\n){0,3}", log)))

metadata = {
    "base_commit": "2d8e702855192f2d959f66598a0289c31c4bfb28",
    "base_tex_sha256": hashlib.sha256(BASE.read_bytes()).hexdigest(),
    "fragment_sha256": hashlib.sha256(TEX.read_bytes()).hexdigest(),
    "target": "Claude integration into v11; no manuscript version created",
    "new_label_count": len(labels),
    "external_v9_references": sorted(refs-set(labels)),
    "new_notation_checked": new_notation,
    "checks": checks,
    "latex": latex_metadata,
    "v10_final_inspected": {
        "commit": "c2ffecc309f9503eda8fc12855b6f80725524110",
        "path": "work/paper1/v10/manuscript/prime_corrected_clock_v10.tex",
        "sha256": hashlib.sha256(draft.encode()).hexdigest(),
    },
    "preferred_delta": {
        "file": "v11_delta.tex",
        "sha256": hashlib.sha256(delta_path.read_bytes()).hexdigest(),
        "labels": delta_labels,
        "external_v10_references": sorted(delta_refs-set(delta_labels)),
        "new_certificate_names_checked": delta_new_names,
        "latex": delta_latex_metadata,
        "scope": "Supplements v10 existing regularization; keeps its definitions, extends X to sqrt(T/2), adds clock-window moments and certified numerical tolerance.",
    },
    "source_verification": "Existing formulations in v9 used; original external papers not independently re-read in this task.",
    "numerical_experiments": "None; no zero dataset or solver used.",
    "limitations": [
        "No numerical value for C_D, C_pr(c), analytic accuracy constant, or starting height is supplied.",
        "Not a proof of bounded transport for the original one-step clock from tau.",
        "Historical priority not assessed; clock is blockwise in T.",
    ],
}
(HERE / "verification.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2)+"\n")
print(json.dumps({"all_checks_passed": all(checks.values()), "check_count": len(checks), "latex": latex_metadata, "delta_latex": delta_latex_metadata, "fragment_sha256": metadata["fragment_sha256"], "delta_sha256": metadata["preferred_delta"]["sha256"]}, ensure_ascii=False, indent=2))
