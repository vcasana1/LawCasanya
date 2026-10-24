"""Stage 6: figures."""
import numpy as np, os, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import stats
D=os.path.join(os.path.dirname(__file__),'..','data'); F=os.path.join(os.path.dirname(__file__),'..','figures')
M=np.load(D+'/M.npy');Q=np.load(D+'/Q.npy');E_mid=np.load(D+'/E_mid.npy')
sd_i=np.load(D+'/sd_indep.npy');sd_c=np.load(D+'/sd_corr.npy');kappa=np.load(D+'/kappa.npy')
N=len(M);n=np.arange(1,N+1);h=np.abs(M).astype(int)
plt.rcParams.update({'font.size':9,'figure.dpi':140})

# 1  E_mid(n)
fig,ax=plt.subplots(figsize=(6.2,2.6))
ax.plot(n[::7],E_mid[::7],lw=.3); ax.set_xlabel('$n$'); ax.set_ylabel('$E_{\\mathrm{mid}}(n)$')
ax.set_title('Centered ordinal-prime residual'); fig.tight_layout(); fig.savefig(F+'/fig1_Emid.png'); plt.close(fig)

# 2  |E_mid| vs |M| with h^{3/2} envelope
fig,ax=plt.subplots(figsize=(3.4,2.8))
s=(n>=10**3)&(h>0)
ax.plot(h[s][::11],np.abs(E_mid[s])[::11],'.',ms=.4,alpha=.3)
hh=np.arange(1,380); ax.plot(hh,0.155*hh**1.5*np.log(10**6),'-',lw=1.2,label='$0.155\\,h^{3/2}\\log n$')
ax.set_xlabel('$|M(n)|$'); ax.set_ylabel('$|E_{\\mathrm{mid}}(n)|$'); ax.legend(fontsize=7)
ax.set_title('Residual vs Mertens magnitude'); fig.tight_layout(); fig.savefig(F+'/fig2_scaling.png'); plt.close(fig)

# 3  stationarity of Z_{3/2}
Z32=np.where(h>0,E_mid/np.maximum(h,1)**1.5/np.log(np.maximum(n,3)),0.)
fig,ax=plt.subplots(figsize=(3.4,2.8))
ed=np.geomspace(1e3,1e6,25);mid=np.sqrt(ed[:-1]*ed[1:])
med=[np.median(np.abs(Z32[(n>=a)&(n<b)&(h>=8)])) for a,b in zip(ed[:-1],ed[1:])]
rms=[np.sqrt((Z32[(n>=a)&(n<b)&(h>=8)]**2).mean()) for a,b in zip(ed[:-1],ed[1:])]
ax.semilogx(mid,med,'o-',ms=3,label='median $|Z_{3/2}|$'); ax.semilogx(mid,rms,'s-',ms=3,label='RMS $Z_{3/2}$')
ax.set_xlabel('$n$'); ax.set_ylim(0,.32); ax.legend(fontsize=7)
ax.set_title('$Z_{3/2}=E_{\\mathrm{mid}}/(|M|^{3/2}\\log n)$'); fig.tight_layout(); fig.savefig(F+'/fig3_stationarity.png'); plt.close(fig)

# 4  kappa(h) and the two predictions
fig,ax=plt.subplots(figsize=(3.4,2.8))
ax.plot(np.arange(1,369),kappa[1:369],lw=1.2)
ax.axhline(1,ls='--',lw=.9,label='independent gaps')
ax.set_xlabel('$h=|M(n)|$'); ax.set_ylabel('$\\kappa(h)=w^{\\!\\top}\\!Rw/w^{\\!\\top}\\!w$')
ax.legend(fontsize=7); ax.set_title('Gap-correlation correction'); fig.tight_layout()
fig.savefig(F+'/fig4_kappa.png'); plt.close(fig)

# 5  Q-Q of thinned Z
s=(n>=10**4)&(h>=12); Z=(E_mid[s]/sd_c[s])[::51]; Zi=(E_mid[s]/sd_i[s])[::51]
fig,ax=plt.subplots(figsize=(3.4,2.8))
q=np.linspace(.001,.999,600); ax.plot(stats.norm.ppf(q),np.quantile(Zi,q),lw=1.1,label='independent-gap')
ax.plot(stats.norm.ppf(q),np.quantile(Z,q),lw=1.1,label='covariance-corrected')
ax.plot([-3.3,3.3],[-3.3,3.3],'--',lw=.8); ax.set_xlabel('$N(0,1)$ quantile'); ax.set_ylabel('$Z$ quantile')
ax.legend(fontsize=7); ax.set_title('Q-Q plot, thinned sample'); fig.tight_layout()
fig.savefig(F+'/fig5_qq.png'); plt.close(fig)

# 6  autocorrelation of Z
Zf=E_mid[s]/sd_c[s]; Zc=Zf-Zf.mean(); v=Zc.var()
lags=np.unique(np.round(np.geomspace(1,20000,60)).astype(int))
ac=[float(np.dot(Zc[:-d],Zc[d:])/((len(Zc)-d)*v)) for d in lags]
fig,ax=plt.subplots(figsize=(3.4,2.8))
ax.semilogx(lags,ac,'o-',ms=2.5); ax.axhline(0,lw=.6); ax.axhline(.05,ls='--',lw=.8)
ax.set_xlabel('lag in $n$'); ax.set_ylabel('autocorrelation of $Z$')
ax.set_title('Dependence between neighbouring $n$'); fig.tight_layout()
fig.savefig(F+'/fig6_autocorr.png'); plt.close(fig)
print("figures written:", sorted(os.listdir(F)))
