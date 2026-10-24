"""Regenerate Version 9 follow-up measurements in Python.
This replaces previously reported-only and MATLAB-originating follow-ups.
"""
from pathlib import Path
import numpy as np
from scipy import stats
import math
ROOT=Path(__file__).resolve().parents[1]; D=ROOT/'data'
M=np.load(D/'M.npy'); Q=np.load(D/'Q.npy'); SS=np.load(D/'SS.npy'); E=np.load(D/'E_mid.npy')
sd=np.load(D/'sd_corr.npy'); mu=np.load(D/'mu.npy')
N=len(M); n=np.arange(1,N+1); h=np.abs(M)

print('=== cross-coupling tests, regenerated ===')
sel=(n>=10_000)&(h>=12)
Z=E[sel]/sd[sel]; nn=n[sel]; MM=M[sel]
gamma1=14.134725141734693
items=[
 ('corr(Z,sgn M)',np.corrcoef(Z,np.sign(MM))[0,1]),
 ('corr(Z,M/sqrt(n))',np.corrcoef(Z,MM/np.sqrt(nn))[0,1]),
 ('corr(Z,cos(gamma1 log n))',np.corrcoef(Z,np.cos(gamma1*np.log(nn)))[0,1]),
 ('corr(Z,sin(gamma1 log n))',np.corrcoef(Z,np.sin(gamma1*np.log(nn)))[0,1]),
]
for k,v in items: print(f'{k:35s} {v:+.8f}')
diff=Z[MM>0].mean()-Z[MM<0].mean(); print('mean(Z|M>0)-mean(Z|M<0)       %+0.8f'%diff)
# effective sample with positive-sequence Geyer-style cutoff, same method as stage 4
Zc=Z-Z.mean(); vv=Zc.var(); tau=1.0
for lag in range(1,20001):
    r=float(np.dot(Zc[:-lag],Zc[lag:])/((len(Zc)-lag)*vv))
    if r<=0: break
    tau+=2*r
neff=len(Z)/tau
print('integrated autocorrelation time       %.6f'%tau)
print('effective sample size                 %.3f'%neff)
print('1/sqrt(n_eff)                         %.6f'%(1/np.sqrt(neff)))
phase=np.mod(gamma1*np.log(nn),2*np.pi); bins=np.linspace(0,2*np.pi,9)
means=[]; ses=[]
for i in range(8):
    x=Z[(phase>=bins[i])&(phase<bins[i+1])]
    means.append(x.mean()); ses.append(x.std(ddof=1)/np.sqrt(len(x)/tau))
print('8-bin phase mean dispersion           %.6f'%np.std(means))
print('median effective phase-bin SE         %.6f'%np.median(ses))

print('\n=== short-interval prime-count variance, regenerated ===')
# Explicit reproducible protocol: all integer starts x in [3.8e6,4.8e6-H].
MAX=4_800_000
isp=np.ones(MAX+1,dtype=bool); isp[:2]=False
for p in range(2,int(MAX**0.5)+1):
    if isp[p]: isp[p*p:MAX+1:p]=False
pic=np.cumsum(isp.astype(np.int32))
lo,hi=3_800_000,4_800_000; X=4_300_000.0
logX=np.log(X); B=-0.5772156649015329-np.log(2*np.pi)
print('protocol: all integer starts in [3800000, 4800000-H], reference X=4300000')
print('H var_measured ratio_MS ratio_Cramer')
for H in [200,1000,5000,20000]:
    xs=np.arange(lo,hi-H+1,dtype=np.int64)
    cnt=pic[xs+H]-pic[xs]
    vm=float(cnt.var())
    vcr=H/logX
    vms=H*(np.log(X/H)+B)/(logX**2)
    print(f'{H:5d} {vm:12.6f} {vm/vms:9.6f} {vm/vcr:12.6f}')

print('\n=== quadratic-fit regeneration ===')
sf=np.flatnonzero(mu!=0)+1; eps=mu[sf-1]; R=np.cumsum(eps.astype(np.int64))
a=np.flatnonzero(eps==1)+1; b=np.flatnonzero(eps==-1)+1; J=min(len(a),len(b))
d=(b[:J]-a[:J]).astype(float); e2=(a[:J]+b[:J]-4*np.arange(1,J+1)).astype(float)
cD=np.cumsum(d*d); cE=np.cumsum(e2*e2); cM=np.cumsum(R.astype(float)**2)
bal=np.flatnonzero(R==0)+1
qb=bal[(bal//2>=8000)&(bal<=488868)]; jb=qb//2
for name,y in [('D2',cD[jb-1]),('E2',cE[jb-1]),('M2',cM[qb-1])]:
    slope=np.polyfit(np.log(jb),np.log(y),1)[0]
    print(f'{name} log-log slope on balanced prefixes J>=8000 through J=244434: {slope:.6f}')
print('E2/D2 at first selected prefix %.8f'%((cE[jb[0]-1])/(cD[jb[0]-1])))
print('E2/D2 at final selected prefix %.8f'%((cE[jb[-1]-1])/(cD[jb[-1]-1])))
# crude scale fits for |d_j| and |e_j| over logarithmic bins, medians
edges=np.geomspace(1000,J,30).astype(int); mids=[]; md=[]; me=[]
for x,y in zip(edges[:-1],edges[1:]):
    if y<=x: continue
    mids.append(np.sqrt(x*y)); md.append(np.median(np.abs(d[x-1:y-1]))); me.append(np.median(np.abs(e2[x-1:y-1])/2))
for name,arr in [('median |d|',np.array(md)),('median |e|',np.array(me))]:
    mask=arr>0; slope=np.polyfit(np.log(np.array(mids)[mask]),np.log(arr[mask]),1)[0]
    print(f'{name} fitted exponent: {slope:.6f}')

print('\n=== active-lifetime multiset shape, regenerated ===')
Qb=488868; Jb=Qb//2; db=(b[:Jb]-a[:Jb]).astype(np.int64)
def shape_stats(eps0,d0,Qcut):
    R0=np.cumsum(eps0.astype(np.int64)); cuts=np.arange(1,Qcut,dtype=np.int64); rq=R0[cuts-1]
    npv=(cuts+rq)//2; nmv=(cuts-rq)//2; lo0=np.minimum(npv,nmv)+1; hi0=np.maximum(npv,nmv); hh=np.abs(rq)
    pd=np.concatenate(([0],np.cumsum(np.abs(d0),dtype=np.int64))); pd2=np.concatenate(([0.],np.cumsum(d0.astype(float)**2)))
    sa=pd[hi0]-pd[lo0-1]; mean=np.divide(sa,hh,out=np.full(len(hh),np.nan),where=hh>0)
    ss2=pd2[hi0]-pd2[lo0-1]; var=np.divide(ss2,hh,out=np.full(len(hh),np.nan),where=hh>0)-mean*mean
    sd0=np.sqrt(np.maximum(var,0)); cv=np.divide(sd0,mean,out=np.full(len(hh),np.nan),where=mean>0)
    rows=[]
    for low,high in [(8,17),(32,65),(128,401)]:
        s=(hh>=low)&(hh<high)
        rows.append((low,high,int(s.sum()),float(np.nanmean(mean[s]/hh[s])),float(np.nanstd(mean[s]/hh[s])),float(np.nanmean(cv[s]))))
    tails=[]
    for th in [1.5,2.5,3.5]:
        num=den=0
        for L,H,vh in zip(lo0,hi0,hh):
            if vh==0: continue
            vals=np.abs(d0[L-1:H]); num+=int(np.sum(vals>=th*vh)); den+=len(vals)
        tails.append(num/den)
    return rows,tails
rowsM,tailsM=shape_stats(eps[:Qb],db,Qb)
rng=np.random.default_rng(12345); Li=4*Qb; ei=rng.choice([-1,1],size=Li); ai=np.flatnonzero(ei==1)+1; bi=np.flatnonzero(ei==-1)+1; Ji=min(len(ai),len(bi)); di=(bi[:Ji]-ai[:Ji]).astype(np.int64)
rowsI,tailsI=shape_stats(ei,di,Qb)
print('height_bin count_M mean/h_M disp_M cv_M | count_iid mean/h_iid disp_iid cv_iid')
for rm,ri in zip(rowsM,rowsI):
    print(f'{rm[0]}-{rm[1]-1} {rm[2]} {rm[3]:.6f} {rm[4]:.6f} {rm[5]:.6f} | {ri[2]} {ri[3]:.6f} {ri[4]:.6f} {ri[5]:.6f}')
for th,mv,iv in zip([1.5,2.5,3.5],tailsM,tailsI): print(f'P(active |d| >= {th} h): Mobius={mv:.8f} iid={iv:.8f}')
