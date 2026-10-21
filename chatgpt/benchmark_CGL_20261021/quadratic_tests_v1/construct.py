"""Truth-free quadratic constructor. Atomic resumable block checkpoints."""
import sys,json,hashlib,time,os
from pathlib import Path
import numpy as np
from scipy.linalg import cholesky_banded,cho_solve_banded
from types import SimpleNamespace
HERE=Path(__file__).resolve().parent; OUT=HERE/'outputs';OUT.mkdir(exist_ok=True)
sys.path.insert(0,str(HERE.parent/'localgap_v1'))
from fastphase import evaluate
P=json.loads((HERE/'PROTOCOL.json').read_text()); PH=hashlib.sha256((HERE/'PROTOCOL.json').read_bytes()).hexdigest()
def guard(event,args):
    if event=='open' and 'zeross' in str(args[0]):raise RuntimeError('Truth forbidden in constructor')
sys.addaudithook(guard)
def atomic(path,**arrays):
    tmp=str(path)+'.tmp'
    with open(tmp,'wb') as f:np.savez(f,**arrays)
    os.replace(tmp,path)
def status(**kw):
    p=OUT/'progress.json';t=p.with_suffix('.tmp');t.write_text(json.dumps(dict(protocol_sha256=PH,time=time.time(),**kw),indent=2));t.replace(p)
def n0(t):return t/(2*np.pi)*(np.log(t/(2*np.pi))-1)+.875
def dt(w):return np.r_[-w[0],w[:-1]-w[1:],w[-1]]
def primes(x):
    a=np.ones(int(x)+1,bool);a[:2]=False
    for p in range(2,int(np.sqrt(x))+1):
        if a[p]:a[p*p::p]=False
    return np.flatnonzero(a)
def load(t,h,pp):
    ff=[];aa=[]
    for p in pp:
        r=1/np.sqrt(p);m=1
        while True:
            ff.append(m*np.log(p));aa.append(-r**m/(np.pi*m))
            if r**(m+1)/((m+1)*(1-r))/np.pi<=1e-12/max(1,len(pp)):break
            m+=1
    f=np.array(ff);a=np.array(aa);x=f*h
    d=evaluate(SimpleNamespace(f=f,a=a*np.sinc(x/(2*np.pi))**2,kind='sine'),t) if len(f) else np.zeros_like(t)
    if len(f):
        il=(1+1j*x-np.exp(1j*x))/x**2;ir=(np.exp(1j*x)*(1-1j*x)-1)/x**2
        d[0]=np.sum(a*np.imag(np.exp(1j*f*t[0])*il));d[-1]=np.sum(a*np.imag(np.exp(1j*f*t[-2])*ir))
    a0=t[:-1];r=h/a0;power=r*r;left=np.zeros_like(r);right=np.zeros_like(r);m=2
    while True:
        coef=(-1.)**m/(m*(m-1));left+=a0/(2*np.pi)*coef*power*(1/((m+1)*(m+2))-1/6);right+=a0/(2*np.pi)*coef*power*(1/(m+2)-1/3)
        if h*r.max()**m/(6*np.pi*m*(m+1)*(1-r.max()))<1e-13:break
        power*=r;m+=1
    d[:-1]+=left;d[1:]+=right
    return d,len(f)
def solve(T,k,tau):
    dest=OUT/f'block_{T}.npz'
    if dest.exists():return
    start=time.time();L=np.log(T)/(2*np.pi);M=int(np.ceil(2.5*T*L));h=2.5*T/M;t=T/2+h*np.arange(M+1);smooth=n0(t);pp=primes(np.sqrt(T/2))
    status(stage='loads',T=T,nodes=M+1)
    d,nterms=load(t,h,pp);lo=L*h/2-np.diff(smooth);hi=2*L*h-np.diff(smooth)
    diag=np.full(M+1,2/3);diag[[0,-1]]=1/3;rho=.5
    band=np.zeros((2,M+1));band[0]=diag+rho*np.r_[1,np.full(M-1,2),1];band[1,:-1]=1/6-rho
    chol=cholesky_banded(band,lower=True,check_finite=False)
    cp=OUT/f'checkpoint_{T}.npz';y=np.zeros(M+1);z=np.clip(np.diff(y),lo,hi);u=np.zeros(M);it0=0
    if cp.exists():
        c=np.load(cp);assert str(c['protocol'])==PH;y=c['y'];z=c['z'];u=c['u'];it0=int(c['iteration'])
    pr=du=np.inf
    for it in range(it0+1,3001):
        y=cho_solve_banded((chol,True),d+rho*dt(z-u),check_finite=False);dy=np.diff(y);old=z;z=np.clip(dy+u,lo,hi);u+=dy-z
        if it%10==0:
            pr=float(np.max(np.abs(dy-z)));du=float(np.max(np.abs(rho*dt(z-old))))
            if pr<=1e-10 and du<=1e-10:break
        if it%50==0:
            atomic(cp,y=y,z=z,u=u,iteration=it,protocol=PH);status(stage='solving',T=T,iteration=it,primal=pr,dual=du)
    pred=smooth+y;assert np.all(np.diff(pred)>0)
    q=k-.5;idx=np.searchsorted(pred,q)-1;valid=(idx>=0)&(idx<M);root=np.full(len(k),np.nan);j=idx[valid];root[valid]=t[j]+h*(q[valid]-pred[j])/(pred[j+1]-pred[j])
    meta=dict(T=T,nodes=M+1,h=h,X=float(np.sqrt(T/2)),primes=len(pp),powers=nterms,iterations=it,primal=pr,dual=du,converged=bool(pr<=1e-10 and du<=1e-10),active=int(np.sum((z==lo)|(z==hi))),seconds=time.time()-start)
    atomic(dest,k=k,model=root,metadata=json.dumps(meta),protocol=PH);print(json.dumps(meta),flush=True);status(stage='block_complete',**meta)
    if cp.exists():cp.unlink()
if __name__=='__main__':
    tau=np.fromfile(Path(P['data_directory'])/'zLamb.bin',dtype='<f8');assert len(tau)==P['n'];blocks=2**np.floor(np.log2(tau)).astype(int)
    for T in np.unique(blocks):
        ids=np.flatnonzero(blocks==T);solve(int(T),ids+1,tau[ids])
    x=np.full(len(tau),np.nan)
    for file in OUT.glob('block_*.npz'):
        b=np.load(file);x[b['k']-1]=b['model']
    atomic(OUT/'predictions.npz',k=np.arange(1,len(x)+1),model=x,protocol=PH);status(stage='constructor_complete',n=len(x),missing=int(np.isnan(x).sum()))
