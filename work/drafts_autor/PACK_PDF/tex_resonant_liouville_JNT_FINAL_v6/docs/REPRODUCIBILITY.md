# Reproducibility

Python used for the final audit: 3.13.5.

Install dependencies:

    python3 -m pip install -r requirements.txt

Run the numerical checks from the repository root:

    python3 src/verify_core_results.py
    python3 src/verify_rational_local_profile.py
    python3 src/verify_natural_majority.py
    python3 src/verify_logarithmic_mesoscopic.py

Regenerate PNG figures:

    python3 src/plot_rational_resonances.py
    python3 src/plot_rational_profile.py
    python3 src/plot_logarithmic_mesoscopic.py

Regenerate the Liouville binary independently:

    python3 src/generate_liouville_bin.py --N 21000000 --out data/liouville_int8_N21000000_regenerated.bin

The final audit regenerated all 21,000,000 bytes and verified byte-for-byte equality with the supplied binary.

Compile the manuscript from `submission/`:

    pdflatex tex_resonant_liouville_JNT_FINAL.tex
    pdflatex tex_resonant_liouville_JNT_FINAL.tex
    pdflatex tex_resonant_liouville_JNT_FINAL.tex

The supplied `elsarticle.cls` is the class used for the final compilation. Figures are PNG files only; no standalone figure PDFs are present.
