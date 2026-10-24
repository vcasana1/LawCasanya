import os, sys, time, math, json
import numpy as np
from scipy import sparse
from scipy.linalg import eigh
from scipy.special import digamma
from scipy.stats import chi2

os.environ.setdefault('OPENBLAS_NUM_THREADS','16')
os.environ.setdefault('OMP_NUM_THREADS','16')

def build_C(N):
    d=N-1
    rows=[]; cols=[]; data=[]
    # columns col=m-2 for m=2..N; rows r-1 for r=1..N-1
    for m in range(2,N+1):
        col=m-2
        # +1 when m | r+1 => r=km-1, k>=1, r>=1 => m>=2 gives first m-1
        for s in range(m, N+1, m): # s=r+1 <= N
            r=s-1
            if 1 <= r <= N-1:
                rows.append(r-1); cols.append(col); data.append(1.0)
        # -1 when m | r, r<=N-1
        for r in range(m, N, m):
            rows.append(r-1); cols.append(col); data.append(-1.0)
    C=sparse.coo_matrix((data,(rows,cols)),shape=(d,d),dtype=np.float64).tocsr()
    C.sum_duplicates()
    C.eliminate_zeros()
    return C

def metrics(V):
    # columns = eigenvectors
    d,k=V.shape
    p=V*V
    # ensure normalizations
    norms=p.sum(axis=0)
    # Shannon safe
    S=-(np.where(p>0,p*np.log(p),0.0)).sum(axis=0)
    P2=(p*p).sum(axis=0)
    M3=(d**2)*(p**3).sum(axis=0)
    M4=(d**3)*(p**4).sum(axis=0)
    maxI=d*p.max(axis=0)
    D=np.log(d)-S
    Sstr=S+np.log(P2)
    return dict(S=S,P2=P2,M3=M3,M4=M4,maxI=maxI,D=D,Sstr=Sstr,norms=norms)

def exact_bench(d):
    ES=digamma(d/2+1)-digamma(1.5)
    EP2=3/(d+2)
    EM3=15*d*d/((d+2)*(d+4))
    EM4=105*d**3/((d+2)*(d+4)*(d+6))
    cov=-4*(d-1)/((d+2)**2*(d+4))
    varP2=24*(d-1)/((d+2)**2*(d+4)*(d+6))
    varS_as=(1.5*math.pi**2-14)/d
    corr_as=-4/math.sqrt(24*(1.5*math.pi**2-14))
    return dict(ES=ES,D=math.log(d)-ES,dP2=d*EP2,M3=EM3,M4=EM4,covSP2=cov,varP2=varP2,varS_as=varS_as,corr_as=corr_as,Sstr_lim=math.euler_gamma+math.log(6)-2 if hasattr(math,'euler_gamma') else 0.5772156649015329+math.log(6)-2)

def pooled_ks(V, max_sample=1500000):
    d,k=V.shape
    x=(d*(V*V)).ravel()
    if x.size>max_sample:
        # deterministic stride sample
        step=int(math.ceil(x.size/max_sample))
        x=x[::step]
    x=np.sort(x)
    n=x.size
    F=chi2.cdf(x,1)
    # exact one-sample KS distance
    i=np.arange(1,n+1)
    Dplus=np.max(i/n-F)
    Dminus=np.max(F-(i-1)/n)
    return float(max(Dplus,Dminus)), int(n)

def run(N, outdir='/mnt/data/shannon_results'):
    os.makedirs(outdir,exist_ok=True)
    t0=time.time(); C=build_C(N); t1=time.time()
    d=N-1
    # H = C C^T; sparse then dense
    H=(C@C.T).toarray(); t2=time.time()
    L=math.ceil(N/4); U=math.floor(3*N/4)
    # 1-based [L,U]
    vals,Uvec=eigh(H,subset_by_index=[L-1,U-1],driver='evr',check_finite=False,overwrite_a=True)
    t3=time.time()
    sig=np.sqrt(np.maximum(vals,0))
    Vvec=(C.T@Uvec)/sig[np.newaxis,:]
    # renormalize tiny numerical drift
    Vvec=Vvec/np.linalg.norm(Vvec,axis=0,keepdims=True)
    t4=time.time()
    ml=metrics(Uvec); mr=metrics(Vvec)
    b=exact_bench(d)
    corrL=float(np.corrcoef(ml['S'],ml['P2'])[0,1])
    corrR=float(np.corrcoef(mr['S'],mr['P2'])[0,1])
    ksL,nksL=pooled_ks(Uvec); ksR,nksR=pooled_ks(Vvec)
    # paired left-right metrics
    deltaS=ml['S']-mr['S']
    deltaDP2=d*(ml['P2']-mr['P2'])
    corrLR_S=float(np.corrcoef(ml['S'],mr['S'])[0,1])
    corrLR_P2=float(np.corrcoef(ml['P2'],mr['P2'])[0,1])
    def summarize(m):
        return {
            'mean_S':float(np.mean(m['S'])),
            'mean_D':float(np.mean(m['D'])),
            'mean_dP2':float(d*np.mean(m['P2'])),
            'mean_Sstr':float(np.mean(m['Sstr'])),
            'mean_M3':float(np.mean(m['M3'])),
            'mean_M4':float(np.mean(m['M4'])),
            'mean_maxI':float(np.mean(m['maxI'])),
            'median_maxI':float(np.median(m['maxI'])),
            'std_S':float(np.std(m['S'],ddof=1)),
            'std_dP2':float(d*np.std(m['P2'],ddof=1)),
        }
    res={
        'N':N,'d':d,'L':L,'U':U,'k':U-L+1,'nnz_C':int(C.nnz),
        'timing':{'buildC':t1-t0,'H':t2-t1,'eigh':t3-t2,'right':t4-t3},
        'eig_min_window':float(vals[0]),'eig_max_window':float(vals[-1]),
        'orthU':float(np.max(np.abs(Uvec.T@Uvec-np.eye(Uvec.shape[1])))),
        'orthV':float(np.max(np.abs(Vvec.T@Vvec-np.eye(Vvec.shape[1])))),
        'left':summarize(ml),'right':summarize(mr),
        'corr_S_P2_left':corrL,'corr_S_P2_right':corrR,
        'ks_PT_left':ksL,'ks_PT_right':ksR,'ks_n_left':nksL,'ks_n_right':nksR,
        'paired':{
            'mean_deltaS':float(np.mean(deltaS)),
            'rms_deltaS':float(np.sqrt(np.mean(deltaS**2))),
            'mean_delta_dP2':float(np.mean(deltaDP2)),
            'rms_delta_dP2':float(np.sqrt(np.mean(deltaDP2**2))),
            'corr_left_right_S':corrLR_S,
            'corr_left_right_P2':corrLR_P2,
        },
        'benchmark':b,
    }
    with open(f'{outdir}/N{N}.json','w') as f: json.dump(res,f,indent=2)
    print(json.dumps(res,indent=2))
    return res

if __name__=='__main__':
    Ns=[int(x) for x in sys.argv[1:]] or [250]
    for N in Ns:
        print('=== N',N,'===',flush=True)
        run(N)
