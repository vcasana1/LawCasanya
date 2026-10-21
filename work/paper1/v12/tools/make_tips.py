"""Generate the hover texts (\\CGTip@<label>) shown by \\CGref and \\CGeqref in PDF viewers.

usage: python3 make_tips.py main.tex main.aux tips.tex

For every \\label the text is the kind and number of the object, its page and a plain-text
rendering of its statement or equation.  The LaTeX source is converted token by token, as TeX
reads it (a control word is a backslash followed by letters), so that no symbol is lost by the
gluing of a converted macro to the following letters; \\frac, \\sqrt and \\binom are converted
with their arguments; \\CGref and \\CGeqref inside the text are replaced by the numbers they
print; optional arguments and section titles are read with balanced delimiters.
"""
import os
import re
import sys

tex = open(sys.argv[1]).read()
aux = sys.argv[2]
out = sys.argv[3]
nums = {}
if os.path.exists(aux):
    for m in re.finditer(r"\\newlabel\{([^}]*)\}\{\{(\{[^{}]*\}|[^{}]*)\}\{([^}]*)\}", open(aux).read()):
        nums[m.group(1)] = (m.group(2).strip("{}").replace("$", ""), m.group(3))

GREEK = set(("alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa varkappa lambda mu nu xi "
             "pi varpi rho varrho sigma varsigma tau upsilon phi varphi chi psi omega Gamma Delta Theta Lambda Xi "
             "Pi Sigma Upsilon Phi Psi Omega").split())
MAP = {"langle": "<", "rangle": ">", "iff": "<=>", "Rightarrow": "=>", "Leftarrow": "<=", "Longrightarrow": "=>",
       "Leftrightarrow": "<=>", "Longleftrightarrow": "<=>", "setminus": "\\", "subset": "in", "subseteq": "in",
       "Subset": "in", "supset": "contains", "cup": "u", "cap": "n", "le": "<=", "leq": "<=", "ge": ">=", "geq": ">=",
       "ne": "!=", "neq": "!=", "to": "->", "mapsto": "->", "longrightarrow": "->", "rightarrow": "->",
       "downarrow": "decreasing to", "uparrow": "increasing to", "infty": "inf", "cdot": "*", "pm": "+-",
       "mp": "-+", "times": "x", "ll": "<<", "gg": ">>", "lesssim": "<~", "gtrsim": ">~", "asymp": "~", "sim": "~",
       "approx": "~", "simeq": "~", "equiv": "==", "in": "in", "notin": "not in", "mid": "|", "nmid": "does not divide",
       "vert": "|", "Vert": "||", "lvert": "|", "rvert": "|", "lVert": "||", "rVert": "||", "ast": "*", "star": "*",
       "circ": "o", "vee": "v", "wedge": "^", "neg": "not", "forall": "for all", "exists": "exists",
       "emptyset": "empty", "varnothing": "empty", "partial": "d", "nabla": "grad", "prime": "'", "dots": "...",
       "cdots": "...", "ldots": "...", "lfloor": "floor(", "rfloor": ")", "lceil": "ceil(", "rceil": ")",
       "NR": "N_RVM", "RVM": "RVM", "crit": "crit", "vpi": "varpi_RVM", "eps": "eps", "Z": "Z", "C": "C",
       "R": "R", "N": "N", "Q": "Q", "Re": "Re", "Im": "Im", "Log": "Log", "Mell": "*Mel", "hbar": "hbar",
       "ell": "l", "imath": "i", "jmath": "j", "aleph": "aleph", "Pr": "Pr", "pmod": "mod", "bmod": "mod",
       "widehat": "hat", "hat": "hat", "tilde": "tilde", "widetilde": "tilde", "overline": "conj", "bar": "bar",
       "dot": "dot", "ddot": "ddot", "vec": "", "xrightarrow": "->", "overset": "", "underset": "",
       "S": "S", "NO": "N_0", "IT": "I_T", "lL": "L", "sgn": "sgn", "Cr": "Cr", "BW": "BW", "Rg": "R^gamma", "Rt": "R^tau"}
DROP = set(("mathcal mathscr mathfrak mathbf mathrm mathsf mathbb mathit mathtt boldsymbol bm operatorname text "
            "textup textrm textit textbf textsf texttt emph mbox hbox left right bigl bigr Bigl Bigr biggl biggr "
            "Biggl Biggr big Big bigg Bigg middle displaystyle textstyle scriptstyle boxed quad qquad label tag "
            "notag nonumber allowbreak nobreak hfill hfil vfill noindent par limits nolimits phantom hphantom "
            "vphantom smash strut relax protect leavevmode medskip smallskip bigskip centering raggedright "
            "footnotesize small normalsize").split())


def _arg(s, i):
    """one TeX argument at s[i:] (after spaces): braced group, control sequence or single character"""
    while i < len(s) and s[i] in " \n\t":
        i += 1
    if i >= len(s):
        return "", i
    if s[i] == "{":
        depth = 0
        for j in range(i, len(s)):
            if s[j] == "{":
                depth += 1
            elif s[j] == "}":
                depth -= 1
                if depth == 0:
                    return s[i + 1:j], j + 1
        return s[i + 1:], len(s)
    if s[i] == "\\":
        m = re.match(r"\\[a-zA-Z]+|\\.", s[i:])
        return m.group(0), i + len(m.group(0))
    return s[i], i + 1


def _optarg(s, i):
    """optional [ ... ] argument with balanced brackets and braces; returns (content or None, index)"""
    j = i
    while j < len(s) and s[j] in " \n\t":
        j += 1
    if j >= len(s) or s[j] != "[":
        return None, i
    depth_sq, depth_br = 0, 0
    for k in range(j, len(s)):
        c = s[k]
        if c == "{":
            depth_br += 1
        elif c == "}":
            depth_br -= 1
        elif c == "[" and depth_br == 0:
            depth_sq += 1
        elif c == "]" and depth_br == 0:
            depth_sq -= 1
            if depth_sq == 0:
                return s[j + 1:k], k + 1
    return s[j + 1:], len(s)


def _refs(s):
    """\\CGref{lab} -> printed number, \\CGeqref{lab} -> (number); \\cite[..]{..} -> [ref, ..]"""
    s = re.sub(r"\\CGeqref\{([^}]*)\}", lambda m: "(" + nums.get(m.group(1), (m.group(1), ""))[0] + ")", s)
    s = re.sub(r"\\(?:CGref|ref|eqref)\{([^}]*)\}", lambda m: nums.get(m.group(1), (m.group(1), ""))[0], s)
    out_s, i = [], 0
    while True:
        k = s.find("\\cite", i)
        if k < 0:
            out_s.append(s[i:])
            break
        out_s.append(s[i:k])
        j = k + 5
        opt, j = _optarg(s, j)
        _, j = _arg(s, j)
        out_s.append("[ref" + (", " + opt if opt else "") + "]")
        i = j
    return "".join(out_s)


def _structures(s):
    """\\texorpdfstring (its PDF-string argument), \\frac, \\tfrac, \\dfrac, \\sqrt, \\binom, innermost first"""
    s = re.sub(r"\\[td]frac(?![a-zA-Z])", r"\\frac", s)
    for name, fmt, nargs in (("\\texorpdfstring", "{1}", 2), ("\\frac", "({0})/({1})", 2),
                             ("\\binom", "binom({0},{1})", 2), ("\\sqrt", "sqrt({0})", 1)):
        for _ in range(60):
            k = s.rfind(name)
            if k < 0:
                break
            if s[k + len(name):k + len(name) + 1].isalpha():       # a longer control word
                break
            i = k + len(name)
            if name == "\\sqrt":
                _, i = _optarg(s, i)
            args = []
            for _ in range(nargs):
                a, i = _arg(s, i)
                args.append(a)
            s = s[:k] + fmt.format(*args) + s[i:]
    return s


def _macros(s):
    def rep(m):
        name = m.group(1)
        nxt = s_[m.end():m.end() + 1]
        if name in DROP:
            r = ""
        elif name in MAP:
            r = MAP[name]
        else:
            r = name                                   # Greek letters and operator names keep their name
        if r and r[-1].isalnum() and (nxt.isalnum() or nxt in "\\{"):
            r += " "
        return r
    s_ = s
    return re.sub(r"\\([a-zA-Z]+)\*?", rep, s)


def clean(s, limit=320):
    s = re.sub(r"(?<!\\)%.*", "", s)
    s = re.sub(r"\\label\{[^}]*\}", "", s)
    s = re.sub(r"\\begin\{[^}]*\}(\[[^]]*\])?|\\end\{[^}]*\}", " ", s)
    s = s.replace("\\~", "")
    s = re.sub(r"\\c\{([a-zA-Z])\}", r"\1", s)                          # cedilla
    s = re.sub(r"\\[\"'`^]\{?([a-zA-Z])\}?", r"\1", s)                  # accents: \"o -> o
    s = re.sub(r"(?<!\\)~", " ", s)                 # ties
    s = _refs(s)
    s = _structures(s)
    s = re.sub(r"\\[,;:! ]", " ", s)
    s = s.replace("\\{", "{").replace("\\}", "}").replace("\\|", "||").replace("\\#", "#").replace("\\%", "%")
    s = s.replace("\\&", "&").replace("\\_", "_")
    s = _macros(s)
    s = s.replace("&", " ").replace("\\\\", "; ").replace("$", "")
    s = s.replace("{", "").replace("}", "").replace("\\", "")
    s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r"\(\s+", "(", s)
    s = re.sub(r"\s+\)", ")", s)
    if len(s) > limit:
        s = s[:limit - 3].rstrip() + "..."
    s = s.replace("#", "no.").replace("%", " pct")
    s = s.replace("_", r"\_").replace("^", r"\textasciicircum{}").replace("~", r"\textasciitilde{}")
    return s


ENVS = {"theorem": "Theorem", "proposition": "Proposition", "lemma": "Lemma", "corollary": "Corollary",
        "definition": "Definition", "hypothesis": "Hypothesis", "remark": "Remark", "experiment": "Experiment",
        "conjecture": "Conjecture", "heuristic": "Heuristic", "example": "Example", "proof": "Proof"}
tips = {}
for m in re.finditer(r"\\label\{([^}]*)\}", tex):
    lab = m.group(1)
    pos = m.start()
    num, page = nums.get(lab, ("", ""))
    before = tex[:pos]
    if lab.startswith(("sec:", "subsec:", "app:")):
        hs = list(re.finditer(r"\\(section|subsection|subsubsection)\*?(?=[\[{])", before[-2000:]))
        title = lab
        if hs:
            seg = before[-2000:][hs[-1].end():]
            _, i = _optarg(seg, 0)
            t, _ = _arg(seg, i)
            title = clean(t)
        tips[lab] = "Section %s: %s (p. %s)" % (num, title, page)
    elif lab.startswith("eq:"):
        b = max(before.rfind(r"\begin{equation}"), before.rfind(r"\begin{align}"),
                before.rfind(r"\begin{multline}"), before.rfind(r"\begin{gather}"))
        e = tex.find(r"\end{", pos)
        body = tex[b:e]
        body = re.sub(r"\\begin\{(equation|align|multline|gather)\}", "", body)
        if r"\begin{align}" in tex[b:b + 15]:
            for sg in body.split("\\\\"):
                if lab in sg:
                    body = sg
        tg = re.search(r"\\tag\{([^}]*)\}", body)
        if tg and not num:
            num = clean(tg.group(1))
        tips[lab] = "Eq. (%s), p. %s: %s" % (num, page, clean(body))
    elif lab.startswith(("fig:", "tab:")):
        c = tex.rfind(r"\caption{", 0, pos)
        cap, _ = _arg(tex, c + 8)
        tips[lab] = "%s %s (p. %s): %s" % ("Figure" if lab.startswith("fig") else "Table", num, page, clean(cap))
    else:
        mm = list(re.finditer(r"\\begin\{(\w+)\}", before[-3000:]))
        if mm:
            env = mm[-1].group(1)
            seg = before[-3000:][mm[-1].end():]
            title, _ = _optarg(seg, 0)
            e = tex.find(r"\end{" + env + "}", pos)
            body = clean(tex[pos + len(lab) + 8:e])
            tips[lab] = "%s %s%s (p. %s): %s" % (ENVS.get(env, env.capitalize()), num,
                                                 (" (" + clean(title) + ")") if title else "", page, body)
with open(out, "w") as f:
    f.write("\\makeatletter\n")
    for k, v in tips.items():
        f.write("\\expandafter\\gdef\\csname CGTip@%s\\endcsname{%s}\n" % (k, v))
    f.write("\\makeatother\n")
print(len(tips), "tips")
