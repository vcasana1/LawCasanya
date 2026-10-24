CATALAN MERTENS -- VERSION 9
========================================

Main paper
  paper/Catalan_Mertens_v9_catalan_fusion_program.tex
  paper/Catalan_Mertens_v9_catalan_fusion_program.pdf

Plain-text copy for Copilot
  Catalan_Mertens_v9_catalan_fusion_program.txt

New Version 9 finite certificate
  code/catalan_fusion_v9.py
  outputs/catalan_fusion_v9.json
  outputs/catalan_fusion_v9.png

Run the Version 9 audit from this package directory:
  MPLBACKEND=Agg python3 code/catalan_fusion_v9.py \
    --json outputs/catalan_fusion_v9.json \
    --png outputs/catalan_fusion_v9.png

Compile the paper from the paper directory:
  cd paper
  pdflatex Catalan_Mertens_v9_catalan_fusion_program.tex
  pdflatex Catalan_Mertens_v9_catalan_fusion_program.tex

The package retains all Version 5--8 Python programs and their archived
outputs. The large moebius.bin input is not redistributed.

Logical status
  - Exact: Catalan counts, bounded-height DP, prefix-rank identities,
    layer-deficit telescope, cardinality no-go, and the semilength-6 synergy
    certificate.
  - Open: deriving a quantitative prefix-rank/capacity deficit from partial
    multiplicative information.
  - RH boundary: full revelation or merely declaring the actual Mertens path
    non-exceptional at the square-root scale is the Mertens criterion itself.
