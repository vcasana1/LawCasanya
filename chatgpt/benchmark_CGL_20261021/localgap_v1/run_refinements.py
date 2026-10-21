#!/usr/bin/env python3
"""Resumeable coordinator: wait for verified enumeration, then construct that tier."""
import json,subprocess,sys,time
from pathlib import Path
HERE=Path(__file__).resolve().parent;OUT=HERE/'outputs';pending=[(m,x) for x in [512,2048,8192] for m in ['Gonek','LeClair']]
while pending:
    progressed=False
    for method,tier in pending.copy():
        name=f'{method}_X{tier}';done=OUT/(name+'_final_constructor.json');gate=OUT/'global_index'/(name+'_enumeration.json')
        if done.exists():pending.remove((method,tier));continue
        if not gate.exists():continue
        data=json.loads(gate.read_text())
        if not data.get('complete'):continue
        if not data['numerical_regular_index_gate_passed']:
            print('BLOCKED',name,data,flush=True);pending.remove((method,tier));continue
        with (HERE/(name+'_final_build.log')).open('w') as log:
            subprocess.run([sys.executable,str(HERE/'refine_final.py'),method,str(tier)],stdout=log,stderr=subprocess.STDOUT,check=True)
        pending.remove((method,tier));progressed=True
    if pending and not progressed:time.sleep(5)
print('All available index-gated refinements completed.',flush=True)
