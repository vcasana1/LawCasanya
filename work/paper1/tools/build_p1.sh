#!/bin/sh
# Build paper I: assemble from v17, compile, regenerate hover tooltips, recompile, make the .txt copy.
set -e
cd "$(dirname "$0")/.."
python3 tools/assemble_p1.py ../v17/manuscript/ordinal_prime_cutoff_v17.tex manuscript/front_p1.tex manuscript/back_p1.tex manuscript/prime_corrected_clock_v1.tex
cd manuscript
rm -f *.aux *.toc *.out *.brf
for i in 1 2 3; do pdflatex -interaction=nonstopmode prime_corrected_clock_v1.tex > build.log 2>&1 || true; done
python3 ../tools/make_tips.py prime_corrected_clock_v1.tex prime_corrected_clock_v1.aux tips.tex
python3 ../tools/replace_tips.py prime_corrected_clock_v1.tex tips.tex
for i in 1 2; do pdflatex -interaction=nonstopmode prime_corrected_clock_v1.tex > build.log 2>&1 || true; done
cp prime_corrected_clock_v1.tex prime_corrected_clock_v1.txt
grep -E "^!|undefined" prime_corrected_clock_v1.log || true
grep -c Overfull prime_corrected_clock_v1.log || true
tail -2 build.log
