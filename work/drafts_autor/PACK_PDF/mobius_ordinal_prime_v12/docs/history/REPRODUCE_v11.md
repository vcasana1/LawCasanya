# Reproduction

Run from the package root.

```bash
python code/build_data.py > outputs/01_build_data.txt
python code/weights_identity.py > outputs/02_weights_identity.txt
python code/gap_covariance.py > outputs/03_gap_covariance.txt
python code/distribution_tests.py > outputs/04_distribution_tests.txt
python code/thinned_ks.py > outputs/05_thinned_ks.txt
python code/figures.py > outputs/06_figures.txt
python code/ratio_law.py > outputs/07_ratio_law.txt
python code/envelope_origin.py > outputs/08_envelope_origin.txt
python code/v5_exact_extensions.py > outputs/10_v5_exact_extensions.txt
python code/v9_pairing_dynamics_audit.py > outputs/20_v9_pairing_dynamics_audit.txt
python code/v9_followup_numerics.py > outputs/21_v9_followup_numerics.txt
python code/v11_level_energy_entropy.py > outputs/22_v11_level_energy_entropy.txt
pdflatex -interaction=nonstopmode -halt-on-error mobius_ordinal_prime_transform_S_SS_v11.tex > outputs/50_v11_pdflatex_pass1.txt
pdflatex -interaction=nonstopmode -halt-on-error mobius_ordinal_prime_transform_S_SS_v11.tex > outputs/51_v11_pdflatex_pass2.txt
```

`figures.py` generates Figures 1-6. `envelope_origin.py` regenerates Figures 7-8. `v11_level_energy_entropy.py` verifies the new exact level-return, excursion-energy, and prime/ordinal identities and prints the separately labelled finite diagnostics. The final package contains no MATLAB computation and does not rely on the previously supplied PNG files.
