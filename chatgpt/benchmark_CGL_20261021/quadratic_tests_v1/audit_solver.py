"""Replay identical QPs, certify numerical residuals, compare saved roots. No truth."""
import construct as c
import numpy as np,json,time
from scipy.linalg import cholesky_banded,cho_solve_banded
rows=[]
for file in sorted(c.OUT.glob('block_*.npz'),key=lambda p:int(p.stem.split('_')[1])):
    b=np.load(file);meta=json.loads(str(b['metadata']));T=meta['T'];M=meta['nodes']-1;h=meta['h'];L=np.log(T)/(2*np.pi);t=T/2+h*np.arange(M+1);n=c.n0(t);d,_=c.load(t,h,c.primes(np.sqrt(T/2)));lo=L*h/2-np.diff(n);hi=2*L*h-np.diff(n)
    diag=np.full(M+1,2/3);diag[[0,-1]]=1/3;ab=np.zeros((2,M+1));ab[0]=diag+.5*np.r_[1,np.full(M-1,2),1];ab[1,:-1]=-1/3;fac=cholesky_banded(ab,lower=True,check_finite=False)
    y=np.zeros(M+1);z=np.clip(np.diff(y),lo,hi);u=np.zeros(M)
    for it in range(1,meta['iterations']+1):
        y=cho_solve_banded((fac,True),d+.5*c.dt(z-u),check_finite=False);dy=np.diff(y);old=z;z=np.clip(dy+u,lo,hi);u+=dy-z
    lam=.5*u;Ay=diag*y;Ay[:-1]+=y[1:]/6;Ay[1:]+=y[:-1]/6;r=Ay-d+c.dt(lam);bound=np.where(lam>=0,hi,lo)
    # Dual lower bound of J=.5*y'A*y-d'y. At finite primal tolerance
    # this gap is diagnostic, not an exact feasible-primal certificate.
    ab[0]=diag;ab[1,:-1]=1/6;af=cholesky_banded(ab,lower=True,check_finite=False);ar=cho_solve_banded((af,True),r,check_finite=False)
    complement=float(np.sum(lam*(bound-dy)));gap=complement+.5*float(r@ar)
    pred=n+y;q=b['k']-.5;j=np.searchsorted(pred,q)-1;root=t[j]+h*(q-pred[j])/(pred[j+1]-pred[j]);difference=float(np.max(abs(root-b['model'])))
    row=dict(T=T,stationarity_max=float(np.max(abs(r))),primal_violation=max(0.,float(np.max(lo-dy)),float(np.max(dy-hi))),complementarity_sum=complement,dual_gap_at_approximate_primal=gap,saved_root_max_difference=difference,min_nodal_slope=float(np.min(np.diff(pred))/h),max_nodal_slope=float(np.max(np.diff(pred))/h),slope_lower=L/2,slope_upper=2*L)
    assert difference<1e-9 and row['stationarity_max']<2e-10 and row['primal_violation']<2e-10
    rows.append(row);(c.OUT/'solver_audit.partial.json').write_text(json.dumps(rows,indent=2));print(json.dumps(row),flush=True)
(c.OUT/'solver_audit.json').write_text(json.dumps(rows,indent=2))
