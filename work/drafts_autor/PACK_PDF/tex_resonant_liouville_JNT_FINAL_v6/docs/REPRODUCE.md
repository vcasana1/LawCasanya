# Reproduction

The manuscript uses only `data/liouville_int8_N21000000.bin`.

1. Install the packages listed in `requirements.txt`.
2. Regenerate numerical checks with:

   `python src/verify_core_results.py`

   `python src/verify_rational_local_profile.py`

   `python src/verify_natural_majority.py`

   `python src/verify_logarithmic_mesoscopic.py`

   Regenerate PNG figures with the three `src/plot_*.py` scripts.
3. The Liouville binary can be regenerated independently with:

   `python src/generate_liouville_bin.py --N 21000000 --out data/liouville_int8_N21000000_regenerated.bin`

   The supplied `outputs/binary_regeneration_audit.txt` records the byte-for-byte comparison performed for the archived version.
4. Compile the paper from `submission/` with the supplied `elsarticle.cls`.

All manuscript figures are PNG files. No figure is supplied as PDF.
