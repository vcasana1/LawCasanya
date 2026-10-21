"""Index-preserving, synthetic-neighbour metrics. No mean spacing in criterion."""
import numpy as np

def per_zero(k,x,g,n_total):
    k=np.asarray(k,np.int64);x=np.asarray(x,float);g=np.asarray(g,float)
    assert k.ndim==1 and len(k)==len(x)==len(g) and np.all(np.diff(k)>0)
    n=len(k);left=np.full(n,np.nan);right=np.full(n,np.nan)
    adjacent=np.diff(k)==1;gap=np.diff(x)
    left[1:]=np.where(adjacent,gap,np.nan);right[:-1]=np.where(adjacent,gap,np.nan)
    d=np.minimum(left,right)
    d[k==1]=right[k==1];d[k==n_total]=left[k==n_total]
    e=x-g;present=np.isfinite(e)&np.isfinite(d)
    structural=present&(d<=0);valid=present&(d>0)
    R=np.full(n,np.nan);R[valid]=2*np.abs(e[valid])/d[valid]
    passed=valid&(R<1);violated=valid&(R>=1)
    # Principal criterion after the user's correction (2026-10-21): the true
    # kth zero belongs to the midpoint cell of its OWN synthetic kth zero.
    # e>0: truth is to the left, so only the left half-gap bounds the error.
    # e<0: truth is to the right, so only the right half-gap bounds the error.
    # Outer cells have no outer boundary; no fictitious endpoint neighbour.
    directional_gap=np.where(e>0,left,right)
    directional_gap[(k==1)&(e>0)]=np.inf
    directional_gap[(k==n_total)&(e<0)]=np.inf
    directional_gap[e==0]=np.inf
    directional_R=np.full(n,np.nan)
    directional_R[valid]=2*np.abs(e[valid])/directional_gap[valid]
    directional_passed=valid&(directional_R<1)
    directional_violated=valid&(directional_R>=1)
    # e=model-truth, so a-diff(e)=diff(truth). This is an evaluation identity.
    margin=gap-np.diff(e);identity_error=np.max(np.abs((margin-np.diff(g))[adjacent])) if np.any(adjacent) else None
    return dict(k=k,model=x,truth=g,error=e,abs_error=np.abs(e),left_gap=left,right_gap=right,d=d,R=R,
                covered=present,structural=structural,passed=passed,violated=violated,
                directional_gap=directional_gap,directional_R=directional_R,
                directional_passed=directional_passed,directional_violated=directional_violated,
                pair_adjacent=adjacent,pair_gap=gap,pair_margin=margin,identity_error=identity_error)

def summarize(data,mask,method,region,prime_count,provenance):
    q=np.asarray(mask,bool);covered=q&data['covered'];valid=covered&~data['structural'];e=data['error'][covered]
    abs_e=np.abs(e);ids=np.flatnonzero(covered);rid=np.flatnonzero(valid)
    imax=ids[np.argmax(abs_e)] if len(ids) else None
    ir=rid[np.argmax(data['R'][rid])] if len(rid) else None
    idir=rid[np.argmax(data['directional_R'][rid])] if len(rid) else None
    # Adjacent pairs with both endpoints in requested subset, never gaps between sparse indices.
    adj=data['pair_adjacent']&q[:-1]&q[1:]
    gaps=data['pair_gap'][adj];finite=gaps[np.isfinite(gaps)]
    r=dict(method=method,region=region,prime_count=prime_count,provenance=provenance,
           requested=int(q.sum()),covered=int(covered.sum()),missing_neighbors_or_outputs=int((q&~data['covered']).sum()),
           rms=float(np.sqrt(np.mean(e*e))) if len(e) else None,mae=float(abs_e.mean()) if len(e) else None,
           max_abs=float(abs_e.max()) if len(e) else None,max_abs_k=int(data['k'][imax]) if imax is not None else None,
           p95_abs=float(np.quantile(abs_e,.95)) if len(e) else None,p99_abs=float(np.quantile(abs_e,.99)) if len(e) else None,
           pass_count=int((q&data['passed']).sum()),ratio_violation_count=int((q&data['violated']).sum()),
           structural_failure_count=int((q&data['structural']).sum()),
           all_failure_count=int((q&(data['violated']|data['structural'])).sum()),
           max_R=float(data['R'][ir]) if ir is not None else None,max_R_k=int(data['k'][ir]) if ir is not None else None,
           consecutive_pairs=int(adj.sum()),nonpositive_gaps=int(np.sum(finite<=0)),
           min_gap=float(finite.min()) if len(finite) else None,max_gap=float(finite.max()) if len(finite) else None,
           pair_margin_identity_error=data['identity_error'])
    r.update(primary_criterion='directional synthetic midpoint cell; outer endpoint cells unbounded',
             legacy_criterion='symmetric min half-gap; sufficient stronger condition; endpoints single neighbour',
             directional_pass_count=int((q&data['directional_passed']).sum()),
             directional_ratio_violation_count=int((q&data['directional_violated']).sum()),
             directional_all_failure_count=int((q&(data['directional_violated']|data['structural'])).sum()),
             directional_max_R=float(data['directional_R'][idir]) if idir is not None else None,
             directional_max_R_k=int(data['k'][idir]) if idir is not None else None,
             symmetric_only_rejections=int((q&data['violated']&data['directional_passed']).sum()))
    assert r['pass_count']+r['ratio_violation_count']+r['structural_failure_count']==r['covered']
    r['violation_percent']=100*r['all_failure_count']/r['covered'] if r['covered'] else None
    assert r['directional_pass_count']+r['directional_ratio_violation_count']+r['structural_failure_count']==r['covered']
    r['directional_violation_percent']=100*r['directional_all_failure_count']/r['covered'] if r['covered'] else None
    return r

def self_check():
    k=np.arange(1,5);x=np.array([0.,2.,3.,5.]);g=x+np.array([.9,.6,.1,1.])
    p=per_zero(k,x,g,4);assert np.array_equal(p['d'],[2,1,1,2])
    assert np.array_equal(p['passed'],[True,False,True,False]) # equality R=1 fails
    # Sparse observations must not create artificial adjacent gaps.
    p=per_zero(np.array([1,3,4]),np.array([0.,3.,5.]),np.array([0.,3.,5.]),4)
    assert not p['covered'][0] and not p['covered'][1] and p['covered'][2]
    p=per_zero(k,np.array([0.,2.,1.,5.]),g,4);assert p['structural'][1] and p['structural'][2]
    # Asymmetric counterexample supplied by the user: left=10,right=1,e=4.
    p=per_zero(np.arange(1,4),np.array([0.,10.,11.]),np.array([0.,6.,11.]),3)
    assert p['violated'][1] and p['directional_passed'][1] and p['directional_R'][1]==.8
    # Reverse direction, strict midpoint tie, and endpoint outer cells.
    p=per_zero(np.arange(1,4),np.array([0.,1.,11.]),np.array([-20.,5.,31.]),3)
    assert np.all(p['directional_passed']) and p['directional_R'][1]==.8
    p=per_zero(np.arange(1,4),np.array([0.,1.,11.]),np.array([0.,6.,11.]),3)
    assert p['directional_violated'][1] and p['directional_R'][1]==1

if __name__=='__main__':self_check();print('Synthetic local-gap checks passed')
