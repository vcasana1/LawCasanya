"""Package per-zero results in bounded GitHub files; keep raw checkpoints local."""
from pathlib import Path
import numpy as np,json,hashlib,csv
H=Path(__file__).resolve().parent;O=H/'outputs';D=O/'per_zero';D.mkdir(exist_ok=True)
p=np.load(O/'predictions.npz');e=np.load(O/'evaluation_per_zero.npz')
for start in range(0,len(p['k']),100000):
    sl=slice(start,start+100000);np.savez_compressed(D/f'indices_{start+1:07d}_{min(start+100000,len(p["k"])):07d}.npz',model=p['model'][sl],**{k:e[k][sl] for k in e.files})
rows=json.loads((O/'metrics.json').read_text());r=next(x for x in rows if x['region']=='final600316')
old=list(csv.DictReader((H.parent/'localgap_v1/outputs/matched_final_directional.csv').open()));cols=['method','prime_count','RMS','MAE','max_abs_error','max_abs_error_k','total_failures','max_directional_ratio','worst_directional_k']
selected=[{k:v[k] for k in cols} for v in old if v['method'].startswith(('Gonek','LeClair')) or 'c667' in v['method']]
selected.append(dict(method='v14_quadratic_L2',prime_count='97/128 variable by dyadic block',RMS=r['rms'],MAE=r['mae'],max_abs_error=r['max_abs'],max_abs_error_k=r['max_abs_k'],total_failures=r['directional_all_failure_count'],max_directional_ratio=r['directional_max_R'],worst_directional_k=r['directional_max_R_k']))
with (O/'comparison_final.csv').open('w') as f:w=csv.DictWriter(f,fieldnames=cols);w.writeheader();w.writerows(selected)
manifest=[]
for f in sorted(H.rglob('*')):
    if f.is_file() and f.name != 'MANIFEST.json' and '__pycache__' not in str(f):manifest.append(dict(path=str(f.relative_to(H)),size=f.stat().st_size,sha256=hashlib.sha256(f.read_bytes()).hexdigest(),publish=not(f.name.startswith('block_') or f.name in ['predictions.npz','evaluation_per_zero.npz','solver_audit.partial.json'])))
(H/'MANIFEST.json').write_text(json.dumps(dict(files=manifest,excluded='Raw block checkpoints and redundant combined arrays remain locally saved; published per_zero chunks contain complete model/error/neighbour outputs.'),indent=2))
