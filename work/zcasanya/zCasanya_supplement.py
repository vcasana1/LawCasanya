#!/usr/bin/env python3
"""Archive unmodified supplied v10 sources/outputs together with our Python sources."""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import zipfile


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source-zip',required=True)
    p.add_argument('--original-dir',required=True)
    p.add_argument('--downloads',required=True)
    a=p.parse_args();root=Path(__file__).resolve().parent
    src=Path(a.source_zip).resolve()
    archive=root.parent/'zCasanya_PY_originales_y_OUTPUTS_v10.zip'
    hashes={}
    with zipfile.ZipFile(src) as original,zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as out:
        for item in original.infolist():
            if item.is_dir():continue
            content=original.read(item.filename)
            out.writestr(item.filename,content)
            hashes[item.filename]=hashlib.sha256(content).hexdigest()
        for f in [*sorted(root.glob('*.py')),root/'requirements.txt',root/'README.md']:
            name='zCasanya_Python/'+f.name;content=f.read_bytes()
            out.writestr(name,content);hashes[name]=hashlib.sha256(content).hexdigest()
        out.write(src,'original_ZIP/ordinal_prime_cutoff_v10.zip')
        out.writestr('ORIGINALS_SHA256.json',json.dumps({
            'original_v10_zip_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
            'files':hashes,'original_v10_files_unchanged':True},indent=2))
        out.writestr('CONTENIDO.txt','Scripts Python de zCasanya y todos los archivos originales de la v10, incluidos code/, outputs/, figures/, data/ y manuscript/. Los originales no se han modificado. Los 836 pilotos y 58 outputs completos nuevos estan en zCasanya_python_20261018_FULL.zip.\n')
    with zipfile.ZipFile(archive) as out,zipfile.ZipFile(src) as original:
        assert out.testzip() is None
        for name in original.namelist():
            if not name.endswith('/'):assert out.read(name)==original.read(name)
        for f in sorted(root.glob('*.py')):
            assert out.read('zCasanya_Python/'+f.name)==f.read_bytes()
    for directory in [Path(a.original_dir),Path(a.downloads)]:
        dest=directory/archive.name
        shutil.copy2(archive,dest)
        assert hashlib.sha256(dest.read_bytes()).digest()==hashlib.sha256(archive.read_bytes()).digest()
    print(archive,archive.stat().st_size,'bytes;',len(hashes),'verified sources')


if __name__=='__main__':main()
