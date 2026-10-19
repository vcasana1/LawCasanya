#!/usr/bin/env python3
"""Compile the complete supplied TEX; regenerate internal hover previews."""
from pathlib import Path
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
MAN = ROOT / 'manuscript'
NAME = 'prime_corrected_clock_v5'
TEX = MAN / (NAME + '.tex')
BUILD = ROOT / 'build'
BUILD.mkdir(exist_ok=True)
env = os.environ.copy()
env['TEXINPUTS'] = str(ROOT / 'texmf') + '//:' + env.get('TEXINPUTS', '')

def run(args, log):
    with (BUILD / log).open('w') as out:
        subprocess.run(args, cwd=MAN, env=env, stdout=out,
                       stderr=subprocess.STDOUT, check=True)

def compile_once(number):
    run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
         '-file-line-error', TEX.name], f'pass_{number}.txt')

for number in range(1, 4):
    compile_once(number)
for number in range(4, 7):
    run([sys.executable, str(ROOT/'tools/make_tips.py'), TEX.name,
         NAME+'.aux', 'tips.tex'], 'make_tips.txt')
    run([sys.executable, str(ROOT/'tools/replace_tips.py'), TEX.name,
         'tips.tex'], 'replace_tips.txt')
    compile_once(number)

log = (MAN/(NAME+'.log')).read_text(errors='replace')
bad = re.findall(r'^.*(?:undefined|multiply defined|Overfull \\[hv]box|^!).*$',
                 log, re.M)
if bad:
    raise SystemExit('Unresolved build diagnostics:\n'+'\n'.join(bad))
shutil.copyfile(TEX, MAN/(NAME+'.txt'))
summary = {
    'compiler': subprocess.check_output(['pdflatex','--version'], text=True).splitlines()[0],
    'passes': 6,
    'undefined_references_or_citations': False,
    'multiply_defined_labels': False,
    'overfull_boxes': False,
    'tex_txt_byte_identical': TEX.read_bytes() == (MAN/(NAME+'.txt')).read_bytes(),
    'tex_sha256': hashlib.sha256(TEX.read_bytes()).hexdigest(),
    'pdf_sha256': hashlib.sha256((MAN/(NAME+'.pdf')).read_bytes()).hexdigest(),
    'warnings': re.findall(r'^(?:LaTeX|Package [^ ]+) Warning:.*$',log,re.M),
}
(BUILD/'compile_checks.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
