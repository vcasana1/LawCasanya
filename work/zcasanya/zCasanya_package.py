#!/usr/bin/env python3
"""Install the concrete completed results, preserving originals; ZIP and verify.

This delivery step is separate from all numerical construction and validation.
Usage: python3 zCasanya_package.py --original-dir DIR --downloads DIR
"""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import time
import zipfile


def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda:f.read(8*1024**2),b''):h.update(block)
    return h.hexdigest()


def backed_copy(src,dest):
    backup=None
    if dest.exists() and sha(dest)!=sha(src):
        backup=dest.with_name(dest.name+'.backup.'+str(time.time_ns()))
        shutil.copy2(dest,backup)
    if not dest.exists() or sha(dest)!=sha(src):shutil.copy2(src,dest)
    assert sha(src)==sha(dest)
    return {'path':str(dest),'sha256':sha(dest),'bytes':dest.stat().st_size,
            'previous_backup':str(backup) if backup else None}


def main():
    root=Path(__file__).resolve().parent
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--original-dir',required=True);p.add_argument('--downloads',required=True)
    a=p.parse_args();original=Path(a.original_dir).resolve();downloads=Path(a.downloads).resolve()
    assert original.is_dir() and downloads.is_dir()
    s=json.loads((root/'summary.json').read_text())
    selected=json.loads((root/'selected.json').read_text())
    inp=json.loads((root/'input_audit.json').read_text())
    true=json.loads((root/'validation_input_audit.json').read_text())
    assert s['records']==2001052 and s['bytes']==16008416
    assert sha(root/'zCasanya.bin')==s['sha256']==selected['sha256']
    assert json.loads((root/'reproducibility_check.json').read_text())['byte_identical']
    # Original source checksums must still equal the audits made during reading.
    checks={}
    for name,expected in [('zLamb.bin',inp['zLamb']['sha256']),
                          ('primoss.bin',inp['primes']['sha256']),
                          ('zeross.bin',true['sha256'])]:
        actual=sha(original/name);assert actual==expected
        checks[name]={'expected_sha256':expected,'final_sha256':actual,'unchanged':True}
    print('Original inputs unchanged',flush=True)
    names=['zCasanya.bin','zCasanya_build.py','zCasanya_validate.py','zCasanya_numeric_checks.py',
           'zCasanya_report.py','reproduce_selected.py','run_all.py','zCasanya_results.csv',
           'zCasanya_report.txt','zCasanya_summary.tex','zCasanya_summary.pdf','selected.json']
    installed=[backed_copy(root/name,original/name) for name in names]
    print('Final binary, programs and report installed in original directory',flush=True)
    folder=original/root.name
    if folder.exists():folder=original/(root.name+'_'+str(time.time_ns()))
    audit={'original_inputs':checks,'original_directory_outputs':installed,
           'full_results_directory':str(folder),
           'final_binary_first':s['first'],'final_binary_last':s['last'],
           'final_binary_records':s['records'],'final_binary_bytes':s['bytes'],
           'configuration':s['configuration'],'byte_identical_rebuild':True,
           'scripts_and_numerics':'Python; no MATLAB executed',
           'split_protocol':json.loads((root/'split_protocol.json').read_text())}
    (root/'delivery_audit.json').write_text(json.dumps(audit,indent=2))
    files=sorted(f for f in root.rglob('*') if f.is_file() and '__pycache__' not in f.parts
                 and f.name not in ['SHA256SUMS.txt','.DS_Store'])
    hashes={str(f.relative_to(root)):sha(f) for f in files}
    (root/'SHA256SUMS.txt').write_text(''.join(f'{h}  {name}\n' for name,h in hashes.items()))
    shutil.copytree(root,folder,ignore=shutil.ignore_patterns('__pycache__','.DS_Store'))
    for name,h in hashes.items():assert sha(folder/name)==h
    assert sha(root/'SHA256SUMS.txt')==sha(folder/'SHA256SUMS.txt')
    print('All installed results verified by SHA-256',flush=True)
    archive=root.parent/(root.name+'_FULL.zip')
    if archive.exists():
        shutil.copy2(archive,archive.with_name(archive.name+'.backup.'+str(time.time_ns())))
    with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6,allowZip64=True) as z:
        for f in [*files,root/'SHA256SUMS.txt']:
            z.write(f,arcname=str(Path(root.name)/f.relative_to(root)))
    print('ZIP created; checking every member CRC',flush=True)
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None
        member_count=len(z.infolist())
    archive_sha=sha(archive)
    copies=[backed_copy(archive,original/archive.name),backed_copy(archive,downloads/archive.name)]
    for name in ['zCasanya.bin','zCasanya_summary.tex','zCasanya_summary.pdf']:
        copies.append(backed_copy(root/name,downloads/name))
    result={'zip_path':str(archive),'zip_bytes':archive.stat().st_size,
            'zip_sha256':archive_sha,'zip_members':member_count,'zip_crc_check':'passed',
            'installed_directory':str(folder),'verified_copies':copies,
            'original_input_hashes_unchanged':True,
            'all_installed_files_sha256_verified':True}
    (root.parent/(root.name+'_delivery.json')).write_text(json.dumps(result,indent=2))
    (downloads/(archive.name+'.sha256')).write_text(archive_sha+'  '+archive.name+'\n')
    print(json.dumps(result,indent=2),flush=True)


if __name__=='__main__':main()
