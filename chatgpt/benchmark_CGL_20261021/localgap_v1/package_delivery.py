#!/usr/bin/env python3
"""Manifest all results, retaining rebuildable intermediate exclusions explicitly."""
import hashlib,json,zipfile
from pathlib import Path
HERE=Path(__file__).resolve().parent
def main():
    files=[];omitted=[]
    for f in sorted(HERE.rglob('*')):
        if not f.is_file() or '__pycache__' in f.parts:continue
        rel=f.relative_to(HERE).as_posix()
        if rel in ['publication_filelist.json','ARTIFACT_MANIFEST.json','CGL_scripts_tables_20261021.zip']:continue
        reason=None
        if f.suffix=='.dylib':reason='platform-specific acceleration, rebuild from fastphase.cpp'
        elif f.name.endswith('_checkpoint.npz'):reason='resume state, rebuild with enumerate_global.py; all final gate results published'
        elif f.suffix=='.bin' and f.name!='c667_PAV_a010.bin':reason='rebuildable constant-cutoff intermediate; full evaluation and all violations published'
        elif f.name.endswith('_final_per_zero.npz') and (f.name.startswith('zCasanya_matlab') or ('Casanya_constant' in f.name and '_PAV_' not in f.name)):reason='redundant per-zero intermediate; constructor, full summaries and all violations published'
        rec=dict(path=rel,bytes=f.stat().st_size,sha256=hashlib.sha256(f.read_bytes()).hexdigest())
        if reason:rec['reason']=reason;omitted.append(rec)
        else:files.append(rec)
    for rec in files:
        f=HERE/rec['path']
        if f.suffix=='.npz':
            with zipfile.ZipFile(f) as z:assert z.testzip() is None
    manifest=dict(published=files,local_reconstructible_intermediates=omitted,original_inputs_excluded=True,
                  original_inputs_unchanged=json.loads((HERE/'outputs/original_inputs_unchanged.json').read_text()))
    (HERE/'ARTIFACT_MANIFEST.json').write_text(json.dumps(manifest,indent=2))
    archive=HERE/'CGL_scripts_tables_20261021.zip'
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
        for rec in files:
            if rec['bytes']<2000000:z.write(HERE/rec['path'],rec['path'])
        z.write(HERE/'ARTIFACT_MANIFEST.json','ARTIFACT_MANIFEST.json')
    with zipfile.ZipFile(archive) as z:assert z.testzip() is None
    names=[r['path'] for r in files]+['ARTIFACT_MANIFEST.json',archive.name]
    (HERE/'publication_filelist.json').write_text(json.dumps(names,indent=2))
    print('files',len(names),'MB',sum(r['bytes'] for r in files)/1e6,'zip_MB',archive.stat().st_size/1e6,
          'zip_sha256',hashlib.sha256(archive.read_bytes()).hexdigest())
if __name__=='__main__':main()
