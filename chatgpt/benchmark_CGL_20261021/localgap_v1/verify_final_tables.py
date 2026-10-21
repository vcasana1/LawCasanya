#!/usr/bin/env python3
"""Independent midpoint-cell counts and threshold sensitivity check."""
import csv,json
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent;OUT=HERE/'outputs';N=2001052
DATA=Path('/Users/vcasana/Documents/·.· MATLAB/·.· bin_unicos')
g=np.memmap(DATA/'zeross.bin',dtype='<f8',mode='r')
rows=list(csv.DictReader((OUT/'full_localgap_summary.csv').open()));checks=[]
meta=json.loads((OUT/'baseline_constructor_metadata.json').read_text())
for row in rows:
    if row['region']!='final600316' or '_regional_PAV_' in row['method']:continue
    name=row['method'];p=OUT/(name+'_final_with_halo.npz')
    if p.exists():
        z=np.load(p);k=z['k'];x=z['model']
    else:
        path=Path(meta[name]['path']) if name in meta else DATA/({'c667_original':'zCasanya.bin','zCasanya0_existing':'zCasanya0.bin'}[name])
        k=np.arange(1400736,N+1);x=np.memmap(path,dtype='<f8',mode='r')[k-1]
    left=np.r_[np.nan,np.diff(x)];right=np.r_[np.diff(x),np.nan]
    outer=k==N;right[outer]=np.inf
    main=k>=1400737;struct=main&((left<=0)|(right<=0))
    # Separate calculation: compare the true ordinate to actual midpoint heights.
    lower=np.r_[np.nan,x[:-1]+np.diff(x)/2];upper=np.r_[x[:-1]+np.diff(x)/2,np.inf]
    success=main&~struct&(g[k-1]>lower)&(g[k-1]<upper)
    expected=int(row['directional_pass_count']);assert int(success.sum())==expected
    assert int(struct.sum())==int(row['structural_failure_count'])
    error=x-g[k-1];gap=np.where(error>0,left,right)
    ratio=2*np.abs(error)/gap;valid=main&~struct
    dist=np.abs(ratio[valid]-1);ids=np.flatnonzero(valid);at=ids[np.argmin(dist)]
    check=dict(method=name,covered=int(main.sum()),independent_midpoint_success_count=int(success.sum()),
      matches_summary=True,smallest_distance_from_directional_ratio_one=float(dist.min()),
      nearest_threshold_k=int(k[at]),within_1e_7_of_threshold=int(np.sum(dist<1e-7)))
    checks.append(check)
(OUT/'independent_midpoint_verification.json').write_text(json.dumps(checks,indent=2));print(checks)
