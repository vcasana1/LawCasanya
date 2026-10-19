# Prime-corrected clock — complete article, v5

The manuscript is in `manuscript/prime_corrected_clock_v5.tex`. The TXT is a
byte-identical copy of the TEX. The PDF contains the complete article, a
comparison with the cited antecedents, numbered equations, contents, internal
links, citation back-references, and hover previews of internal references.

The isolated mean-square rate is discussed as an observation. No additional
theorem is introduced for the sublevel construction, and no priority claim is
made for the rate alone. The article retains its A–E analytic proof structure.

## Compile

Requirements: Python 3 and a TeX Live installation with pdfLaTeX, Latin Modern,
AMS packages, natbib, hyperref, bookmark, pdfcomment, listings, geometry,
enumitem, longtable, booktabs, microtype, and their usual dependencies.
The archive supplies elsarticle, tracklang, and soul compatibility files in
`texmf/`, with their documented sources and license notices.

From this directory:

```sh
python tools/build_v5.py
```

This compiles the supplied manuscript directly, regenerates the inline hover
texts from its own labels and page numbers, compiles again, checks diagnostics,
and recreates the identical TXT. It does not need another manuscript or data.
Build logs and checks are written in `build/`.

Hover display depends on the PDF viewer supporting annotation tooltips. The
PDF includes the tooltip widgets and the underlying navigation links.

## Reproduce the numerical confirmations

```sh
python -m pip install -r requirements.txt
python code/opc_envelope_coefficient_v14.py outputs
python code/opc_envelope_iterations_p1.py outputs
python code/verify_envelope_intervals_v5.py outputs
```

The first program prints its text summary to stdout; the supplied transcript
is `outputs/envelope_coefficient.txt`. The other programs also save their
text summaries. `audit/numerical_manifest.json` identifies all numerical
parameters, programs, supporting outputs, and hashes. No zero ordinates are
read, and no numerical data select a construction or parameter.

## Source-check status

`audit/source_audit.json` inventories every bibliography entry and distinguishes
the actual PDF passages checked from inherited references not independently
re-read. The originals of Fujii I and II remain unavailable for verification
here; their precise high-moment constants, cutoff exponent, and corrections
are material to the tail and uniform-iteration arguments. These dependencies
are also marked explicitly in TEX comments. This archive does not certify
those outstanding source checks as complete.

Specific unverified comparisons with the individual-zero literature have been
removed. No claim of a finite-height precision guarantee or an exhaustive
historical priority comparison follows from the asymptotic bounds.
