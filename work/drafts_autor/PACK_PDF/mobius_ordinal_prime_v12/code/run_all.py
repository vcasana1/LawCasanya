"""Run the complete Version 12 Python pipeline and capture textual outputs."""
from pathlib import Path
import subprocess, sys
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'outputs'; OUT.mkdir(exist_ok=True)
stages=[
('01_build_data.txt','build_data.py'),
('02_weights_identity.txt','weights_identity.py'),
('03_gap_covariance.txt','gap_covariance.py'),
('04_distribution_tests.txt','distribution_tests.py'),
('05_thinned_ks.txt','thinned_ks.py'),
('06_figures.txt','figures.py'),
('07_ratio_law.txt','ratio_law.py'),
('08_envelope_origin.txt','envelope_origin.py'),
('10_v5_exact_extensions.txt','v5_exact_extensions.py'),
('20_v9_pairing_dynamics_audit.txt','v9_pairing_dynamics_audit.py'),
('21_v9_followup_numerics.txt','v9_followup_numerics.py'),
('22_v11_level_energy_entropy.txt','v11_level_energy_entropy.py'),
('60_v12_alpha_program_audit.txt','v12_alpha_program_audit.py'),
]
for out,script in stages:
    print('running',script,flush=True)
    with (OUT/out).open('w') as fh:
        subprocess.run([sys.executable,str(ROOT/'code'/script)],cwd=ROOT,stdout=fh,stderr=subprocess.STDOUT,check=True)
print('Python pipeline complete')
