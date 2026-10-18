# zCasanya: complete Python experiment

The numerics use Python, NumPy and elementary functions. MATLAB is not used.
`source/ordinal_prime_cutoff_v10.tex` is the exact user-supplied manuscript.
The user-supplied iterative task takes precedence over that reference manuscript.

## Reproduce everything

Install the packages in `requirements.txt`, then use a **new** output directory:

```sh
python3 run_all.py --output /absolute/path/to/new_run
```

The default inputs are bundled under `inputs/`. The prime input is the exact
148,933-prime prefix through 1,999,993 plus the next prime (2,000,003) as a sentinel.
This reproduces every tested cutoff without copying the original 3.64 GB file.
`--data-dir /absolute/path/to/original_directory` instead uses the original inputs.
The reproducibility runner includes the initial coarse-sweep finalists and the
extended-sweep finalists, as in the delivered experiment. Estimated coefficients
or true-zero corrections are never passed to the constructor.

The programs save logs and checkpoints. The constructor resumes existing outputs
only after checking matching configuration, index set and SHA-256. It refuses to
overwrite an unmatched binary. The selected binary is backed up before replacement.

## Programs and execution order

1. `zCasanya_numeric_checks.py`: high-precision elementary arithmetic checks.
2. `zCasanya_build.py --data-dir DIR --output OUT --stage pilot`: prime-only pilots.
3. `zCasanya_validate.py --data-dir DIR --output OUT --stage pilot`: parameter tuning.
4. `zCasanya_build.py --data-dir DIR --output OUT --stage full`: all-index construction.
5. `zCasanya_validate.py --data-dir DIR --output OUT --stage select`: freeze winner.
6. `zCasanya_validate.py --data-dir DIR --output OUT --stage report`: untouched-test evaluation.
7. `zCasanya_report.py OUT`: text report, plots and complete TeX source.

`run_all.py` performs these in separate processes, maintaining the constructor's
true-zero-access block. The constructor never imports the validator.
The numerical checks and report accept an optional output-directory argument;
without it they use their own script directory.

If available, `pdflatex` compiles the TeX twice. TeX compilation is the only
non-Python numerical-workflow executable; it does not participate in construction.

## Definitions and evaluation

`euler_v10`: primes p<=X, all powers m>=1, evaluated by a real elementary atan2
local-factor identity. This is not an evaluation of zeta or its argument.
`power_sharp`: prime powers p^m<=X, with the exact weights from the requested task.
There is no smoothing weight in the v10 definition of S_X.

Constant and dyadic policies are separate. Every nondecreasing sequence of
1 through 4 cuts from [8,32,128,512,2048,8192] is piloted, giving 836 arrays.
Parameter search uses only the first 40% of indices. The next 30% chooses the
winner. The final 30% is untouched until selection is frozen. Full-data results
are descriptive and are not presented as independent validation.

Intrinsic eligibility: finite iterates above 2pi, each step below 8 smooth local
spacings. This does not use true zeros. Crossings, steps above 2 spacings and
displacement diagnostics are recorded without sorting, clipping or other repair.

## Main outputs

- `zCasanya.bin`: selected array, little-endian float64, original index order.
- `selected.json`: phase, cuts, steps, selection timing, hash and diagnostics.
- `zCasanya_results.csv`: all metrics by model and evaluation region.
- `final_comparison.csv`, `selection_validation_results.csv`, `pilot_results.csv`.
- `height_windows.csv`, `error_distribution.csv`, `error_and_height.png`.
- `zCasanya_report.txt`, `zCasanya_summary.tex`, `zCasanya_summary.pdf`.
- `pilot/`: every pilot array and its index set; `candidates/`: every full array.
- `*_manifest.json`, input audits, `numeric_checks.json`, execution logs.
- `SHA256SUMS.txt`: artifact checksums; `delivery_audit.json`: original-file
  preservation and delivered-copy verification.

The stable clock difference corrects the sign error in the pasted proposal.
The original source arrays are never altered. Finite computed improvements do
not establish moment or multiplicity bounds at iterated corrected points.

The companion archive `zCasanya_PY_originales_y_OUTPUTS_v10.zip` contains our
Python source files plus every unmodified member of the supplied v10 archive,
including its 11 original Python scripts, outputs, logs, figures and manuscript.
It also includes the original v10 ZIP itself and SHA-256 verification metadata.
`zCasanya_supplement.py` reproduces this companion archive.
