#!/usr/bin/env python3
"""Reproduce the frozen experiment in a new directory, using only Python for numerics.

python3 run_all.py --output /absolute/path/to/NEW_DIRECTORY
Optional --data-dir uses original binaries; default is the packaged inputs folder.
"""
from pathlib import Path
import argparse
import json
import shutil
import subprocess
import sys


def main():
    source=Path(__file__).resolve().parent
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',required=True)
    p.add_argument('--data-dir',default=str(source/'inputs'))
    a=p.parse_args();out=Path(a.output).resolve();data=Path(a.data_dir).resolve()
    if out.exists():raise FileExistsError('Use a new output directory: '+str(out))
    out.mkdir(parents=True)
    (out/'inputs').mkdir();(out/'source').mkdir()
    for name in ['zLamb.bin','primoss.bin']:
        shutil.copy2(source/'inputs'/name,out/'inputs'/name)
    for f in (source/'source').glob('*'):shutil.copy2(f,out/'source'/f.name)
    for f in source.glob('*.py'):shutil.copy2(f,out/f.name)
    commands=[['zCasanya_numeric_checks.py',str(out)],
              ['zCasanya_build.py','--data-dir',str(data),'--output',str(out),'--stage','pilot'],
              ['zCasanya_validate.py','--data-dir',str(data),'--output',str(out),'--stage','pilot']]
    for i,c in enumerate(commands):
        with (out/f'reproduce_{i:02d}.log').open('w') as log:
            subprocess.run([sys.executable,str(source/c[0]),*c[1:]],stdout=log,stderr=subprocess.STDOUT,check=True)
    # Include the initial coarse-sweep finalists as in the delivered execution.
    frozen=json.loads((source/'shortlist.json').read_text())
    fresh=json.loads((out/'shortlist.json').read_text())
    assert all(c in frozen for c in fresh)
    (out/'shortlist.json').write_text(json.dumps(frozen,indent=2))
    commands=[['zCasanya_build.py','--data-dir',str(data),'--output',str(out),'--stage','full'],
              ['zCasanya_validate.py','--data-dir',str(data),'--output',str(out),'--stage','select'],
              ['zCasanya_validate.py','--data-dir',str(data),'--output',str(out),'--stage','report'],
              ['zCasanya_report.py',str(out)]]
    for i,c in enumerate(commands,3):
        with (out/f'reproduce_{i:02d}.log').open('w') as log:
            subprocess.run([sys.executable,str(source/c[0]),*c[1:]],stdout=log,stderr=subprocess.STDOUT,check=True)
    if shutil.which('pdflatex'):
        for _ in range(2):
            subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error','zCasanya_summary.tex'],cwd=out,check=True,stdout=subprocess.DEVNULL)
    print('Complete:',out)
    print((out/'zCasanya_report.txt').read_text())


if __name__=='__main__':main()
