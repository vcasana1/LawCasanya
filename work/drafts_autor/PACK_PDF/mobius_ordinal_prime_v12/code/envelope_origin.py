"""Stage 8: deterministic origin of the packet structure in E_mid(n)."""
import numpy as np, os, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from scipy.signal import find_peaks
D=os.path.join(os.path.dirname(__file__),'..','data'); F=os.path.join(os.path.dirname(__file__),'..','figures')
M=np.load(D+'/M.npy'); E=np.load(D+'/E_mid.npy'); N=len(M); n=np.arange(1,N+1)
h=np.abs(M).astype(float)
gam=np.array([14.1347,21.0220,25.0109,30.4249,32.9351,37.5862,40.9187,43.3271,48.0052,49.7738])
plt.rcParams.update({'font.size':9,'figure.dpi':140})

W=2000
c=np.concatenate([[0.],np.cumsum(E.astype(float)**2)]); env=np.sqrt((c[W:]-c[:-W])/W)
cm=np.concatenate([[0.],np.cumsum(h**1.5*np.log(np.maximum(n,3)))]); pred=(cm[W:]-cm[:-W])/W
mid=n[W//2:W//2+len(env)]
fig,ax=plt.subplots(figsize=(6.6,2.7))
ax.plot(n[::7],E[::7],lw=.25)
k=np.median(env[mid>5e4]/pred[mid>5e4])
ax.plot(mid,k*pred*2.2,lw=1.0,label=r'$\propto |M(n)|^{3/2}\log n$')
ax.plot(mid,-k*pred*2.2,lw=1.0)
ax.set_xlabel('$n$'); ax.set_ylabel('$E_{\\mathrm{mid}}(n)$'); ax.legend(fontsize=8,loc='lower left')
ax.set_title('The packets are the excursions of $|M(n)|$')
fig.tight_layout(); fig.savefig(F+'/fig7_envelope.png'); plt.close(fig)

u=np.linspace(np.log(1000),np.log(10**6),200000); du=u[1]-u[0]
idx=np.clip(np.exp(u).astype(int)-1,0,N-1)
def spec(x):
    y=(x-x.mean())*np.hanning(len(x))
    P=np.abs(np.fft.rfft(y))**2; fr=2*np.pi*np.fft.rfftfreq(len(y),d=du)
    b=(fr>5)&(fr<55); return fr[b],P[b]/P[b].max()
fr,P=spec(M[idx]/np.exp(u/2))
rng=np.random.default_rng(1); Q=np.load(D+'/Q.npy'); mu2=np.diff(np.concatenate([[0],Q]))
fake=np.cumsum(np.where(mu2==1,rng.choice([-1,1],size=N),0))
fr2,P2=spec(fake[idx]/np.exp(u/2))
fig,ax=plt.subplots(figsize=(6.6,2.7))
for g in gam: ax.axvline(g,lw=.8,ls='--')
ax.plot(fr2,P2,lw=.8,label='random-sign surrogate')
ax.plot(fr,P,lw=1.0,label='$M(e^u)e^{-u/2}$')
ax.set_xlabel(r'frequency in $u=\log n$   (dashed: $\gamma_k$, zeta zeros)')
ax.set_ylabel('normalised power'); ax.legend(fontsize=8); ax.set_xlim(5,55)
ax.set_title('Where the packet structure comes from')
fig.tight_layout(); fig.savefig(F+'/fig8_spectrum.png'); plt.close(fig)
print("wrote fig7_envelope.png, fig8_spectrum.png")

print("\ncorr(log RMS-envelope, log |M|^{3/2} log n) over n >= 5e4 : %.4f"
      % np.corrcoef(np.log(env[mid>5e4]),np.log(pred[mid>5e4]))[0,1])
print("control with n log n only (no M)                        : %.4f"
      % np.corrcoef(np.log(env[mid>5e4]),np.log((np.cumsum(np.concatenate([[0.],n*np.log(np.maximum(n,3))]))[W:]-np.cumsum(np.concatenate([[0.],n*np.log(np.maximum(n,3))]))[:-W])[mid>5e4]/W))[0,1])
def pk(fr,P):
    p,_=find_peaks(P,height=.03); o=np.argsort(P[p])[::-1][:8]; return np.sort(fr[p][o])
for nm,(a,b) in [('true M',(fr,P)),('surrogate',(fr2,P2))]:
    t=pk(a,b); print("%-10s peaks %s  mean dist to nearest gamma = %.3f"
                     % (nm,np.round(t,2),np.mean([np.min(np.abs(gam-x)) for x in t])))
