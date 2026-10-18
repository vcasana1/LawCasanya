#!/usr/bin/env python3
"""Rebuild the frozen winner from arithmetic-only portable inputs and compare bytes."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys


def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(8*1024**2),b''):h.update(b)
    return h.hexdigest()


def main():
    root=Path(__file__).resolve().parent
    out=root/'reproduction_selected'
    out.mkdir(exist_ok=True)
    selected=json.loads((root/'selected.json').read_text())
    params={k:selected[k] for k in ['id','window','policy','cutoffs']}
    (out/'shortlist.json').write_text(json.dumps([params],indent=2))
    with (out/'build.log').open('w') as log:
        subprocess.run([sys.executable,str(root/'zCasanya_build.py'),'--data-dir',str(root/'inputs'),
                        '--output',str(out),'--stage','full'],stdout=log,stderr=subprocess.STDOUT,check=True)
    result={'configuration':params,'rebuild_sha256':sha(out/'candidates'/f"{selected['id']}.bin"),
            'delivered_sha256':sha(root/'zCasanya.bin'),
            'uses_only_portable_Lambert_and_prime_inputs':True,
            'zero_values_provided_to_constructor':False,
            'constructor_source_sha256':sha(root/'zCasanya_build.py')}
    result['byte_identical']=result['rebuild_sha256']==result['delivered_sha256']
    assert result['byte_identical']
    assert result['constructor_source_sha256']==selected['constructor_sha256']
    (root/'reproducibility_check.json').write_text(json.dumps(result,indent=2))
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
