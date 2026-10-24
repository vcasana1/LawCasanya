#!/usr/bin/env bash
set -euo pipefail

project_dir="$(cd "$(dirname "$0")" && pwd)"
export MPLCONFIGDIR="$project_dir/.mplconfig"
mkdir -p "$MPLCONFIGDIR" "$project_dir/outputs" "$project_dir/figures"
cd "$project_dir"

python scripts/export_binary_data.py | tee outputs/export_binary_data_output.txt
python scripts/generate_rvm_binary.py | tee outputs/generate_rvm_binary_output.txt
python scripts/verify_core_theorems.py | tee outputs/core_theorem_compatibility_output.txt
python scripts/centroid_rate_validation.py | tee outputs/centroid_rate_validation_output.txt
python scripts/analyze_unfolded_residual_pair_law.py | tee outputs/unfolded_residual_pair_law_output.txt
python scripts/connected_form_factor.py | tee outputs/connected_form_factor_output.txt
python scripts/carrier_saddle_validation.py | tee outputs/carrier_saddle_validation_output.txt
python scripts/rvm_counterexample_validation.py | tee outputs/rvm_counterexample_validation_output.txt
python scripts/prime_model_validation.py | tee outputs/prime_model_validation_output.txt
python scripts/phase_walks_3d.py | tee outputs/phase_walks_3d_output.txt

