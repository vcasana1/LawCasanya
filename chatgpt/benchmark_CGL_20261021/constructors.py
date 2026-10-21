"""Arithmetic-only constructors. No evaluator, true-zero file or zeta calls here.

M1: LeClair 1601.00914v1 eq.49, delta=1e-6 as Table I; prime-by-prime.
M2: Gonek TAMS 2012 eqs.3.4,3.5,5.2,7.4 (exact theta from log Gamma).
M3: frozen c667, sharp prime-POWER support, smooth-clock denominator only.
M4: v17's v15 task3 Stage A / R1 / R2, sampled continuation checks.
"""
import sys
import time
import numpy as np
from scipy.special import loggamma, digamma
from scipy.optimize import brentq

TP = 2*np.pi

def install_guard():
    """Deny access even through np.fromfile/memmap to evaluator inputs."""
    def hook(event, args):
        if event == 'open' and args and isinstance(args[0], (str, bytes)):
            name = str(args[0]).lower()
            if 'zeross' in name or 'zcasanya.bin' in name:
                raise PermissionError('True/frozen ordinates are forbidden to this process')
    sys.addaudithook(hook)

def L(t):
    return np.log(t/TP)/TP

def N0(t):
    return t/TP*(np.log(t/TP)-1)+.875

def clock_diff(t, tau):
    d = t-tau
    u = d/tau
    h = np.empty_like(u)
    small = np.abs(u)<.01
    v = u[small]
    poly = np.full_like(v,1/(14*13))
    for j in range(13,1,-1):
        poly = (-1.)**j/(j*(j-1))+v*poly
    h[small] = v*v*poly
    v = u[~small]
    h[~small] = (1+v)*np.log1p(v)-v
    return L(tau)*d+tau/TP*h

def theta(t):
    return np.imag(loggamma(.25+.5j*t))-.5*t*np.log(np.pi)

def theta_d(t):
    return .5*np.real(digamma(.25+.5j*t))-.5*np.log(np.pi)

def sieve(n):
    a = np.ones(n+1,bool); a[:2] = False
    for p in range(2,int(n**.5)+1):
        if a[p]: a[p*p::p] = False
    return np.flatnonzero(a)

def powers(primes, cutoff):
    out=[]
    for p in primes[primes<=cutoff]:
        q,m=int(p),1
        while q<=cutoff:
            out.append((q,int(p),m)); q*=int(p); m+=1
    out.sort()
    z=np.array(out,dtype=np.int64).reshape(-1,3)
    return z[:,0],z[:,1],z[:,2]

class Phase:
    def __init__(self, primes, support, kind='sharp', formal_X=None, delta=1e-6):
        self.kind=kind; self.support=support; self.formal_X=formal_X
        self.calls=0; self.work=0; self.derivative_work=0; self.raw_work=0; self.max_requested=0
        if kind=='euler':
            self.p=primes[primes<=support].astype(float)
            self.f=np.log(self.p);self.a=self.p**(-.5-delta)
            self.n=self.p;self.m=None
        else:
            self.n,self.p,self.m=powers(primes,support)
            self.f=self.m*np.log(self.p.astype(float))
            w=np.ones(len(self.n))
            if kind=='gonek':
                w=np.minimum(1,2-np.log(self.n.astype(float))/np.log(formal_X))
                w=np.maximum(0,w)
            self.a=-w/(np.pi*self.m*np.sqrt(self.n.astype(float)))

    def __call__(self,t,cut=None,derivative=True):
        t=np.asarray(t,float); s=np.zeros_like(t);ds=np.zeros_like(t)
        self.calls+=t.size
        # Bound temporary arrays. Finite Euler includes all powers analytically.
        cut=np.broadcast_to(self.support if cut is None else cut,t.shape)
        self.max_requested=max(self.max_requested,float(np.max(cut)))
        nt=int(np.searchsorted(self.n,np.max(cut),side='right'))
        for lo in range(0,t.size,128):
            hi=min(lo+128,t.size);tt=t[lo:hi];cc=cut[lo:hi]
            ang=tt[:,None]*self.f[None,:nt]
            mask=self.n[None,:nt]<=cc[:,None]
            sn=np.sin(ang)
            if self.kind=='euler':
                co=np.cos(ang);a=self.a[None,:nt]
                den=1-a*co
                s[lo:hi]=-np.sum(np.where(mask,np.arctan2(a*sn,den),0),axis=1)/np.pi
                if derivative:
                    ds[lo:hi]=-np.sum(np.where(mask,(a*co-a*a)*self.f[None,:nt]/(1-2*a*co+a*a),0),axis=1)/np.pi
            else:
                s[lo:hi]=np.sum(np.where(mask,sn*self.a[None,:nt],0),axis=1)
                if derivative:
                    ds[lo:hi]=np.sum(np.where(mask,np.cos(ang)*(self.a*self.f)[None,:nt],0),axis=1)
            work=int(np.sum(mask));self.work+=work;self.raw_work+=nt*len(tt)
            if derivative:self.derivative_work+=work
        return s,ds

    def budget(self):
        mask=self.n<=self.max_requested
        used=self.p[mask] if self.kind=='euler' else self.p[mask&(self.a!=0)]
        return dict(prime_count=int(len(np.unique(used))),max_prime=int(np.max(used)) if len(used) else 0,
                    support=float(self.support),formal_X=self.formal_X,
                    power_terms='infinite_analytic' if self.kind=='euler' else int(np.count_nonzero(self.a[mask])),
                    phase_point_evaluations=self.calls,term_point_evaluations=self.work,
                    raw_trig_term_point_evaluations=self.raw_work,max_support_evaluated=self.max_requested,
                    derivative_term_point_evaluations=self.derivative_work)

def c667(tau,k,primes):
    x=tau.copy();base=N0(tau)-(k-.5);work=0
    for cutoff in [8,8,512]:
        cut=np.minimum(cutoff,np.maximum(8,np.floor(np.sqrt(np.exp2(np.floor(np.log2(tau)))))))
        s=np.zeros_like(x)
        for cc in np.unique(cut):
            at=cut==cc
            # Match frozen accumulation order exactly: primes, then powers.
            for p in primes[primes<=cc]:
                q,m=int(p),1
                while q<=cc:
                    s[at]+=-1/(np.pi*m*np.sqrt(float(q)))*np.sin((m*np.log(float(p)))*x[at])
                    q*=int(p);m+=1;work+=int(np.sum(at))
        x-=(base+clock_diff(x,tau)+s)/L(x)
    return x,dict(term_point_evaluations=work,phase_point_evaluations=3*len(x),prime_count=97,max_prime=509,
                  support=512,power_terms=len(powers(primes,512)[0]),formal_X=None,derivative_term_point_evaluations=0)

def bracket_fallback(fun,center,spacing):
    """Resolve a failed local Newton solve with positive brackets.
    Do not choose among multiple local roots: report ambiguity instead.
    """
    grid=np.linspace(max(TP+1e-6,center-2*spacing),center+2*spacing,129)
    vals=fun(grid);j=np.flatnonzero(vals[:-1]*vals[1:]<0)
    if len(j)!=1:return np.nan,int(len(j))
    i=j[0]
    root=brentq(lambda t:float(fun(np.array([t]))[0]),grid[i],grid[i+1],xtol=1e-10)
    return root,1

def lc_continuation(tau,k,primes,budgets):
    """Add exactly one prime at a time. Newton solution near preceding root.
    Failure is sticky; no true-zero choice, sorting, or silent recovery.
    """
    x=tau.copy();valid=np.ones(len(x),bool);issues=[];out={};P=Phase(primes,max(budgets),'euler')
    def smooth(t):return N0(t)+1/(48*np.pi*t)
    def smooth_d(t):return L(t)-1/(48*np.pi*t*t)
    # No-prime root with the published Stirling correction.
    for _ in range(4):x-=(smooth(x)-(k-.5))/smooth_d(x)
    start=time.perf_counter()
    for j,p in enumerate(primes[primes<=max(budgets)]):
        cut=float(p)
        previous_x=x.copy()
        for it in range(12):
            ids=np.flatnonzero(valid)
            if not len(ids):break
            xx=x[ids];s,ds=P(xx,np.full(len(ids),cut))
            res=smooth(xx)+s-(k[ids]-.5);der=smooth_d(xx)+ds
            tol=np.maximum(1e-10,16*np.spacing(k[ids].astype(float)))
            done=np.abs(res)<=tol
            if np.all(done):break
            step=res/np.where(np.abs(der)>1e-12,der,np.nan)
            # Trust cap is a numerical safeguard only; max 12 iterations, reported.
            step=np.clip(step,-.25/L(tau[ids]),.25/L(tau[ids]))
            yy=xx-step
            bad=~np.isfinite(yy)|(yy<=TP)
            for z in ids[bad]:issues.append((int(k[z]),'nonreal_or_out_of_domain',int(p)))
            valid[ids[bad]]=False
            x[ids[~bad&~done]]=yy[~bad&~done]
        ids=np.flatnonzero(valid)
        if len(ids):
            s,ds=P(x[ids],np.full(len(ids),cut));res=smooth(x[ids])+s-(k[ids]-.5)
            bad=np.abs(res)>np.maximum(1e-9,32*np.spacing(k[ids].astype(float)))
            for z in ids[bad]:
                fun=lambda t:smooth(t)+P(t,np.full(len(t),cut),False)[0]-(k[z]-.5)
                rt,nroots=bracket_fallback(fun,previous_x[z],1/L(tau[z]))
                if np.isfinite(rt):
                    x[z]=rt;issues.append((int(k[z]),'newton_failure_recovered_unique_bracket',int(p)))
                else:
                    valid[z]=False;issues.append((int(k[z]),f'newton_failure_bracket_root_count_{nroots}',int(p)))
        # Save all budget checkpoints that end at this prime.
        for b in budgets:
            bp=primes[primes<=b]
            if len(bp) and bp[-1]==p:
                y=x.copy();y[~valid]=np.nan
                budget=P.budget();budget.update(prime_count=j+1,max_prime=int(p),support=b)
                out[b]=(y,budget|dict(seconds=time.perf_counter()-start),list(issues))
    return out

def solve_level(tau,k,P,exact_theta=True):
    """Numerical level solver, NOT a claim that levels enumerate model zeros."""
    x=tau.copy();valid=np.ones(len(x),bool);start=time.perf_counter()
    if exact_theta:
        smooth=lambda t:1+theta(t)/np.pi
        smooth_d=lambda t:theta_d(t)/np.pi
    else:
        smooth=N0;smooth_d=L
    for it in range(40):
        s,ds=P(x);res=smooth(x)+s-(k-.5);der=smooth_d(x)+ds
        done=np.abs(res)<=np.maximum(1e-10,16*np.spacing(k.astype(float)))
        if np.all(done):break
        step=np.clip(res/np.where(np.abs(der)>1e-12,der,np.nan),-.25/L(tau),.25/L(tau))
        yy=x-step;bad=~np.isfinite(yy)|(yy<=TP)
        valid&=~bad;x=np.where(bad|done,x,yy)
    s,ds=P(x);res=smooth(x)+s-(k-.5)
    valid&=np.abs(res)<=np.maximum(1e-9,32*np.spacing(k.astype(float)))
    newton_failures=int((~valid).sum());recovered=0;ambiguous=0
    for z in np.flatnonzero(~valid):
        fun=lambda t:smooth(t)+P(t,derivative=False)[0]-(k[z]-.5)
        rt,nroots=bracket_fallback(fun,tau[z],1/L(tau[z]))
        if np.isfinite(rt):x[z]=rt;valid[z]=True;recovered+=1
        else:ambiguous+=int(nroots>1)
    x[~valid]=np.nan
    return x,P.budget()|dict(seconds=time.perf_counter()-start,max_newton_phase_residual=float(np.max(np.abs(res))),
                             newton_failures=newton_failures,bracket_recoveries=recovered,ambiguous_failures=ambiguous)

def stage_a(tau,k,P):
    n=P.n; b=np.cumsum(np.log(P.p)/np.sqrt(n.astype(float)))
    jm=np.searchsorted(b,.9/2*np.log((tau-1)/TP),side='right')-1
    cut=np.where(jm>=0,n[np.maximum(jm,0)],1).astype(float)
    ab=np.cumsum(-P.a)[np.maximum(jm,0)]*(jm>=0)
    bm=b[np.maximum(jm,0)]*(jm>=0)
    base=N0(tau)-(k-.5)
    h=1.1*(ab+np.abs(base))/(L(tau-1)-bm/np.pi)+1e-9
    lo=tau-h;hi=tau+h
    def g(t):return base+clock_diff(t,tau)+P(t,cut,False)[0]
    valid=(lo>TP)&(L(np.maximum(lo,TP+1e-5))-bm/np.pi>0)
    valid&=(g(np.maximum(lo,TP+1e-5))<0)&(g(hi)>0)
    for _ in range(55):
        mid=.5*(lo+hi);neg=g(mid)<0
        lo=np.where(neg,mid,lo);hi=np.where(neg,hi,mid)
    x=.5*(lo+hi);x[~valid]=np.nan
    return x,cut,valid

def v17_continuation(tau,k,P,xA,Xmon,which):
    valid=np.isfinite(xA);x=np.where(valid,xA,tau);cur=Xmon.copy();active=valid.copy()
    w=1/(P.m.astype(float)**2*P.n.astype(float));wc=np.r_[0,np.cumsum(w)]
    it=np.searchsorted(P.n,tau/TP,side='right');ix=np.searchsorted(P.n,Xmon,side='right')
    sigma=np.sqrt((wc[it]-wc[ix])/(2*np.pi**2))
    cphi=np.sqrt(2*np.log(2))/(2*np.pi*sigma)
    ymax=np.sqrt(tau/TP) if which=='R1' else (tau/TP)**np.minimum(cphi,.95)
    base=N0(tau)-(k-.5);rejected=np.zeros(len(x),bool)
    for lev in range(1,7):
        new=np.maximum(np.floor(Xmon*(ymax/Xmon)**(lev/6)),cur)
        ids=np.flatnonzero(active&(new>cur))
        if not len(ids):continue
        ta,ba,xx,yy,prev=tau[ids],base[ids],x[ids].copy(),new[ids],cur[ids]
        good=np.ones(len(ids),bool)
        for _ in range(10):
            s,ds=P(xx,yy);der=L(xx)+ds;bad=der<=.1*L(xx);good&=~bad
            step=np.clip(np.where(bad,0,(ba+clock_diff(xx,ta)+s)/np.where(bad,1,der)),-.25/L(ta),.25/L(ta))
            xx-=step
        s,ds=P(xx,yy);good&=np.abs(ba+clock_diff(xx,ta)+s)<1e-9
        for frac in (0,.25,.5,.75,1):
            pt=x[ids]+frac*(xx-x[ids]);_,d1=P(pt,yy);_,d0=P(pt,prev)
            good&=(L(pt)+d1>.1*L(pt))&(L(pt)+d0>.1*L(pt))
        x[ids[good]]=xx[good];cur[ids[good]]=yy[good]
        active[ids[~good]]=False;rejected[ids[~good]]=True
    x[~valid]=np.nan
    return x,cur,dict(rejected_indices=int(rejected.sum()),target_cutoff_reached=int(np.sum(cur>=np.floor(ymax))),
                       analytic_interval_certification=False,sampled_segment_points=5)
