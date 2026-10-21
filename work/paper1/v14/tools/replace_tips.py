"""Replace the inlined tooltip block of the paper by a freshly generated one.

Usage: python3 replace_tips.py PAPER.tex TIPS.tex
The block starts at the line after '% Tooltip texts shown when hovering over internal references.'
and ends at the first line '\\makeatother' after it (both lines of the block included)."""
import sys

paper, tips = sys.argv[1], sys.argv[2]
lines = open(paper).read().split("\n")
start = lines.index("% Tooltip texts shown when hovering over internal references.") + 1
end = start + lines[start:].index("\\makeatother")
new = open(tips).read().rstrip("\n").split("\n")
assert lines[start] == "\\makeatletter" and new[0] == "\\makeatletter" and new[-1] == "\\makeatother"
lines[start:end + 1] = new
open(paper, "w").write("\n".join(lines))
print("replaced lines %d-%d with %d lines" % (start + 1, end + 1, len(new)))
