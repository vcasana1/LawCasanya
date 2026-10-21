#!/usr/bin/env python3
"""Finalize integrity checks and create a delivery ZIP (no original inputs included)."""
import hashlib,json,platform,sys,zipfile
from pathlib import Path
import importlib.metadata as md

HERE=Path(__file__).resolve().parent;OUT=HERE/'results_v2'
def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(8*1024**2),b''):h.update(b)
    return h.hexdigest()

env=dict(python=sys.version,python_executable=sys.executable,platform=platform.platform(),
         packages={n:md.version(n) for n in ['numpy','scipy','mpmath','matplotlib']})
(HERE/'environment.json').write_text(json.dumps(env,indent=2))
# Recheck original input hashes and refresh the hash of each saved source snapshot.
inv=json.loads((OUT/'inventory.json').read_text());source_records=[]
originals=[]
for r in inv:
    p=Path(r['path'])
    if p.name in ['zLamb.bin','zeross.bin','zCasanya.bin','primoss.bin']:
        now=sha(p);assert now==r['sha256'],f'Input changed: {p}'
        originals.append(dict(path=str(p),sha256=now,unchanged=True))
    if p.parent==HERE/'sources':continue
    source_records.append(r)
for p in sorted((HERE/'sources').glob('*')):
    source_records.append(dict(name=p.name,path=str(p),bytes=p.stat().st_size,sha256=sha(p)))
(OUT/'inventory.json').write_text(json.dumps(source_records,indent=2))
(OUT/'originals_unchanged.json').write_text(json.dumps(originals,indent=2))
assert json.loads((OUT/'c667_reproduction.json').read_text())['byte_identical']
assert json.loads((OUT/'high_precision_checks.json').read_text())['pass_checks']
conf=json.loads((OUT/'config_frozen.json').read_text());h=conf.pop('configuration_sha256')
assert hashlib.sha256(json.dumps(conf,sort_keys=True).encode()).hexdigest()==h
for n,s in conf['code_sha256'].items():assert sha(HERE/n)==sha(OUT/'code_at_execution'/n)==s
blob_hashes=json.loads((HERE/'sources'/'github_blob_sha1.json').read_text())
for n,s in blob_hashes.items():
    b=(HERE/'sources'/n).read_bytes();assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==s
files=[p for p in HERE.iterdir() if p.is_file() and p.suffix in ['.py','.md','.json','.txt']]
files+=list((HERE/'sources').rglob('*'))+list(OUT.rglob('*'))
files=sorted(p for p in files if p.is_file() and '__pycache__' not in p.parts and not p.name.endswith('.tmp'))
manifest=HERE/'SHA256SUMS.txt'
manifest.write_text(''.join(f'{sha(p)}  {p.relative_to(HERE)}\n' for p in files if p!=manifest))
files=[p for p in files if p!=manifest]+[manifest]
dest=HERE.parent/'benchmark_CGL_20261021_ENTREGA_INICIAL.zip'
with zipfile.ZipFile(dest,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in files:z.write(p,Path(HERE.name)/p.relative_to(HERE))
with zipfile.ZipFile(dest) as z:
    assert z.testzip() is None
    for p in files:assert hashlib.sha256(z.read(str(Path(HERE.name)/p.relative_to(HERE)))).hexdigest()==sha(p)
result=dict(zip_path=str(dest),zip_sha256=sha(dest),zip_bytes=dest.stat().st_size,file_count=len(files),
            zip_crc_and_member_hashes_verified=True,original_input_hashes_unchanged=True)
(HERE.parent/'benchmark_CGL_20261021_delivery.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
