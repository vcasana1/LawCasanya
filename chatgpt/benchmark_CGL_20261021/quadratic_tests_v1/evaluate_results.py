"""Separate reference evaluator; cannot change predictor parameters."""
from pathlib import Path
import numpy as np,json,sys,csv,hashlib
H=Path(__file__).resolve().parent;O=H/'outputs';sys.path.insert(0,str(H.parent/'localgap_v1'))
from localgap_metrics import per_zero,summarize
P=json.loads((H/'PROTOCOL.json').read_text());N=P['n'];prediction=O/'predictions.npz'
# Constructor must have completed before opening reference.
b=np.load(prediction);k=b['k'];x=b['model'];assert len(k)==N
g=np.fromfile(Path(P['data_directory'])/'zeross.bin',dtype='<f8');assert len(g)==N
p=per_zero(k,x,g,N);sets=np.load(H.parent/'localgap_v1/outputs/pilot_index_sets.npz');rows=[]
regions={'first1000':sets['first1000'],'fixed_pilot1000':sets['old_pilot'],'pilot_last300':sets['pilot_last300'],'high_consecutive_last300':sets['high_consecutive_last300'],'final600316':np.arange(1400737,N+1),'all2001052':k}
for name,ids in regions.items():rows.append(summarize(p,np.isin(k,ids),'v14_quadratic_L2',name,'variable dyadic block','fixed protocol; retrospective'))
(O/'metrics.json').write_text(json.dumps(rows,indent=2))
with open(O/'metrics.csv','w') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
np.savez_compressed(O/'evaluation_per_zero.npz',**{name:p[name] for name in ['k','error','left_gap','right_gap','directional_R','directional_passed','structural']})
# Independent direct midpoint test, with unbounded exterior endpoint cells.
left=np.r_[-np.inf,(x[:-1]+x[1:])/2];right=np.r_[(x[:-1]+x[1:])/2,np.inf]
check=(g>left)&(g<right);valid=~p['structural']
assert np.array_equal(check[valid],p['directional_passed'][valid])
seams=[]
for file in sorted(O.glob('block_*.npz')):
    bb=np.load(file);first=int(bb['k'][0]);meta=json.loads(str(bb['metadata']))
    if first>1:seams.append(dict(k=first,gap=float(x[first-1]-x[first-2])))
(O/'seams.json').write_text(json.dumps(seams,indent=2))
(O/'evaluation_audit.json').write_text(json.dumps(dict(prediction_sha256=hashlib.sha256(prediction.read_bytes()).hexdigest(),truth_sha256=hashlib.sha256(g.tobytes()).hexdigest(),midpoint_check_exact=True,nonpositive_pairs=int(np.sum(np.diff(x)<=0)),seam_nonpositive=int(sum(s['gap']<=0 for s in seams))),indent=2))
print(json.dumps(rows,indent=2))
