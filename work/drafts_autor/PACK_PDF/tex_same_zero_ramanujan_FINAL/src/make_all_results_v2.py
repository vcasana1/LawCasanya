from pathlib import Path
import json, shutil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parents[1]
FIG, OUT, DATA = BASE/'figures', BASE/'outputs', BASE/'data'
for d in (FIG, OUT, DATA): d.mkdir(parents=True, exist_ok=True)

zeros_txt = DATA/'zeros6.txt'
if not zeros_txt.exists():
    raise FileNotFoundError('Place the official Odlyzko zeros6 text file in data/zeros6.txt')

gamma_txt = np.loadtxt(zeros_txt, dtype=np.float64)
gamma = np.fromfile(DATA/'zeross.bin', dtype=np.float64)
tau = np.fromfile(DATA/'zLamb.bin', dtype=np.float64)
N = len(gamma)
if N != 2_001_052 or len(tau) != N or len(gamma_txt) != N:
    raise ValueError('Expected 2,001,052 ordinates in zeros6.txt, zeross.bin, and zLamb.bin')
if not np.array_equal(gamma_txt, gamma):
    raise ValueError('data/zeross.bin is not the exact float64 encoding of data/zeros6.txt')

(OUT/'data_length_audit.txt').write_text(
    f'zeros6_count={len(gamma_txt)}\n'
    f'zeross_count={len(gamma)}\n'
    f'zLamb_count={len(tau)}\n'
    f'zeross_first={gamma[0]:.15f}\n'
    f'zeross_last={gamma[-1]:.15f}\n'
    f'zLamb_first={tau[0]:.15f}\n'
    f'zLamb_last={tau[-1]:.15f}\n',
    encoding='utf-8'
)

k = np.arange(1, N+1, dtype=np.float64)
clock_residual = tau/(2*np.pi)*np.log(tau/(2*np.pi*np.e)) + 7/8 - (k-1/2)
if np.max(np.abs(clock_residual)) > 1e-8:
    raise ValueError('data/zLamb.bin fails the smooth Riemann--von Mangoldt clock check')

sigma = np.sqrt(2*np.log(np.log(tau))) / np.log(tau/(2*np.pi))
X = (gamma-tau)/sigma

# Adjacent-zero outputs
x0, x1 = X[:-1], X[1:]
loglog = np.log(np.log(tau[:-1]))
D = np.sqrt(loglog)*(x1-x0)
Lclock = np.log(tau[:-1]/(2*np.pi))
gap = (gamma[1:]-gamma[:-1])/(2*np.pi/Lclock)
V_GUE = 3*np.pi/8 - 1
V_GOE = 4/np.pi - 1
rho = float(np.corrcoef(x0,x1)[0,1])
pd.DataFrame([{
    'pairs':len(x0), 'mean_X':np.mean(X), 'mean_X2':np.mean(X**2),
    'rho_adjacent_full_prefix':rho, 'mean_D':np.mean(D), 'var_D':np.var(D),
    'min_D':np.min(D), 'mean_normalized_gap':np.mean(gap),
    'var_normalized_gap':np.var(gap), 'V_GUE_Wigner':V_GUE, 'V_GOE_Wigner':V_GOE,
}]).to_csv(OUT/'adjacent_zero_empirical.csv',index=False)

m=250_000
sl=slice(N-m-1,N-1)
x0t,x1t=x0[sl],x1[sl]
rhot=float(np.corrcoef(x0t,x1t)[0,1])
# Two explicit finite-window conventions are recorded.  The paper reports the
# unweighted mean over the 250,001 distinct zero indices supporting the pairs.
x2_pair_endpoint=float(.5*(np.mean(x0t**2)+np.mean(x1t**2)))
x2_unique=float(np.mean(X[N-m-1:N]**2))
llt=float(np.mean(loglog[sl]))
var_gap_t=float(np.var(gap[sl]))
rho_measured_pair=1-np.pi**2*var_gap_t/(x2_pair_endpoint*llt)
rho_measured_unique=1-np.pi**2*var_gap_t/(x2_unique*llt)
rho_gue_pair=1-np.pi**2*V_GUE/(x2_pair_endpoint*llt)
rho_gue_unique=1-np.pi**2*V_GUE/(x2_unique*llt)
pd.DataFrame([{
    'window_pairs':m, 'zero_support_count':m+1,
    'tau_mid':np.median(tau[:-1][sl]), 'mean_loglog_tau':llt,
    'mean_X2_unique_zero_support':x2_unique,
    'mean_X2_pair_endpoint_average':x2_pair_endpoint,
    'rho_empirical':rhot,
    'var_normalized_gap_empirical':var_gap_t,
    'rho_from_empirical_gap_using_unique_X2':rho_measured_unique,
    'rho_from_empirical_gap_using_pair_endpoint_X2':rho_measured_pair,
    'rho_from_GUE_Wigner_using_unique_X2':rho_gue_unique,
    'rho_from_GUE_Wigner_using_pair_endpoint_X2':rho_gue_pair,
}]).to_csv(OUT/'adjacent_zero_top_window.csv',index=False)

# Four-step reference sample
rng=np.random.default_rng(20260817)
MC=8_000_000
Rsf=np.empty(MC)
chunk=250_000
for pos in range(0,MC,chunk):
    mm=min(chunk,MC-pos)
    th=rng.uniform(0,2*np.pi,size=(mm,4))
    Rsf[pos:pos+mm]=np.abs(np.exp(1j*th).sum(axis=1))

# Fixed-frequency theorem figure
u=np.array([1.,np.sqrt(2),np.sqrt(3),np.sqrt(5)])
Delta=(np.exp(1j*u[0]*gamma)-np.exp(1j*u[1]*gamma)
       -np.exp(1j*u[2]*gamma)+np.exp(1j*u[3]*gamma))
Rfix=np.abs(Delta)
xs,ys=np.sort(Rfix),np.sort(Rsf)
grid=np.sort(np.concatenate([xs[::max(1,len(xs)//300000)],ys[::max(1,len(ys)//300000)]]))
ks_fix=np.max(np.abs(np.searchsorted(xs,grid,'right')/len(xs)-np.searchsorted(ys,grid,'right')/len(ys)))
pd.DataFrame([{
    'sample_count':len(Rfix),'mean_radius_data':np.mean(Rfix),
    'exact_shark_fin_mean':1.799092479842851,
    'mean_deviation':np.mean(Rfix)-1.799092479842851,
    'second_moment_data':np.mean(Rfix**2),'exact_second_moment':4.,
    'second_moment_deviation':np.mean(Rfix**2)-4.,'approx_KS_vs_8m_reference':ks_fix,
}]).to_csv(OUT/'fixed_frequency_sharkfin_stats.csv',index=False)
bins=np.linspace(0,4,220); hf,e=np.histogram(Rfix,bins,density=True); hr,_=np.histogram(Rsf,bins,density=True); c=.5*(e[:-1]+e[1:])
plt.figure(figsize=(9.2,5.8),dpi=220); plt.plot(c,hr,label='Four-step shark-fin reference law'); plt.plot(c,hf,label='Fixed-frequency zeta-zero data'); plt.xlabel(r'$R$'); plt.ylabel('Density'); plt.title('Fixed-frequency zeta-zero observable vs four-step shark-fin law'); plt.legend(); plt.tight_layout(); plt.savefig(FIG/'fixed_frequency_sharkfin_real.png',bbox_inches='tight'); plt.close()

# Lagged two-chord observable
q=k*np.log(k); z=np.exp(1j*gamma*q); w=np.exp(1j*tau*q); start=2
Delta=(z[start+1:]-z[start:-1])-(w[start+1:]-w[start:-1]); Rdata=np.abs(Delta)
Rn=Rdata/np.mean(Rdata); SFn=Rsf/np.mean(Rsf)
xmax=min(2.45,np.quantile(np.concatenate([Rn,SFn[:len(Rn)]]),.9995))
bins=np.linspace(0,xmax,190); hd,e=np.histogram(Rn,bins,density=True); hs,_=np.histogram(SFn,bins,density=True); c=.5*(e[:-1]+e[1:])
xd,yr=np.sort(Rn),np.sort(SFn); grid=np.sort(np.concatenate([xd[::max(1,len(xd)//300000)],yr[::max(1,len(yr)//300000)]])); ks=np.max(np.abs(np.searchsorted(xd,grid,'right')/len(xd)-np.searchsorted(yr,grid,'right')/len(yr)))
pd.DataFrame([{
    'sample_count':len(Rdata),'mean_radius_data':np.mean(Rdata),
    'exact_shark_fin_mean':1.799092479842851,'mean_deviation':np.mean(Rdata)-1.799092479842851,
    'second_moment_data':np.mean(Rdata**2),'exact_second_moment':4.,
    'second_moment_deviation':np.mean(Rdata**2)-4.,'normalized_shape_approx_KS':ks,
}]).to_csv(OUT/'lagged_qk_sharkfin_moments.csv',index=False)
plt.figure(figsize=(9.2,5.8),dpi=220); plt.plot(c,hd,label='Two-chord zeta/RVM data'); plt.plot(c,hs,label='Four-step shark-fin reference law'); plt.xlabel(r'$R/\mathbb{E}R$'); plt.ylabel('Density'); plt.title('Two-chord zeta/RVM observable vs four-step shark-fin law'); plt.legend(); plt.tight_layout(); plt.savefig(FIG/'shark_fin_real_vs_reference.png',bbox_inches='tight'); plt.close()

# Gaussian-phase product outputs: use the complete canonical arrays.
g=gamma; t=tau; sig=sigma; Xc=X
E=np.exp(1j*g)-np.exp(1j*t)+np.exp(1j*np.sqrt(2)*g)-np.exp(1j*np.sqrt(2)*t)
Yobs=np.abs(E)/sig
Wfac=np.abs(1j*(np.exp(1j*t)+np.sqrt(2)*np.exp(1j*np.sqrt(2)*t)))
Ylin=np.abs(Xc)*Wfac
rng2=np.random.default_rng(20260818); MC2=3_000_000; G=np.abs(rng2.standard_normal(MC2)); th=rng2.uniform(0,2*np.pi,size=(MC2,2)); Rph=np.abs(np.exp(1j*th[:,0])+np.sqrt(2)*np.exp(1j*th[:,1])); Ylim=G*Rph
xm=np.quantile(np.concatenate([Yobs,Ylim[:len(Yobs)]]),.995); bins=np.linspace(0,xm,220); h1,e=np.histogram(Yobs,bins,density=True); h2,_=np.histogram(Ylim,bins,density=True); c=.5*(e[:-1]+e[1:])
plt.figure(figsize=(9.2,5.8),dpi=220); plt.plot(c,h1,label='Riemann-zero data'); plt.plot(c,h2,label=r'Gaussian-phase product law $|G|R_u$'); plt.xlabel(r'$|E_k|/\sigma_k$'); plt.ylabel('Density'); plt.title('Finite-data Gaussian-phase product diagnostic'); plt.legend(); plt.tight_layout(); plt.savefig(FIG/'gaussian_phase_product_law.png',bbox_inches='tight'); plt.close()
pd.DataFrame([{'moment':r,'value':np.mean(Xc**r)} for r in range(1,9)]).to_csv(OUT/'X_moments_1_to_8.csv',index=False)
mu=np.mean(Xc); va=np.var(Xc); pd.DataFrame([{'count':len(Xc),'mean':mu,'variance':va,'second_moment':np.mean(Xc**2),'skewness':np.mean((Xc-mu)**3)/np.std(Xc)**3,'kurtosis':np.mean((Xc-mu)**4)/va**2}]).to_csv(OUT/'X_shape_diagnostics.csv',index=False)
pd.DataFrame([{'mean_X2':np.mean(Xc**2),'mean_W2':np.mean(Wfac**2),'product_of_means':np.mean(Xc**2)*np.mean(Wfac**2),'mean_X2W2':np.mean(Xc**2*Wfac**2),'mean_Ylin2':np.mean(Ylin**2),'mean_E2_over_sigma2':np.mean(Yobs**2),'mean_absX':np.mean(np.abs(Xc)),'mean_W':np.mean(Wfac),'mean_Ylin':np.mean(Ylin),'mean_E_over_sigma':np.mean(Yobs),'corr_X2_W2':np.corrcoef(Xc**2,Wfac**2)[0,1],'corr_absX_W':np.corrcoef(np.abs(Xc),Wfac)[0,1]}]).to_csv(OUT/'factor_decomposition.csv',index=False)
pd.DataFrame([{'mean_W_data':np.mean(Wfac),'mean_Ru_MC':np.mean(Rph),'second_moment_W_data':np.mean(Wfac**2),'second_moment_Ru_MC':np.mean(Rph**2),'exact_second_moment':3.}]).to_csv(OUT/'radial_factor_validation.csv',index=False)

# Corrected GUE figures
x=np.linspace(6,30,500); T=10**x; ras=1-np.pi**2*V_GUE/np.log(np.log(T)); rfin=1-np.pi**2*V_GUE/(.848888*np.log(np.log(T)))
plt.figure(figsize=(9,5.5),dpi=220); plt.plot(x,ras,label=r'$\langle X^2\rangle=1$'); plt.plot(x,rfin,label=r'$\langle X^2\rangle=0.848888$'); plt.xlabel(r'$\log_{10}T$'); plt.ylabel(r'$\rho_1$'); plt.title('Corrected adjacent-correlation scale using GUE Wigner variance'); plt.legend(); plt.tight_layout(); plt.savefig(FIG/'corrected_rho1_gue_vs_height.png',bbox_inches='tight'); plt.close()
plt.figure(figsize=(7.5,5.2),dpi=220); vals=[V_GUE,V_GOE]; plt.bar(['GUE Wigner','GOE Wigner'],vals); plt.ylabel('Spacing variance'); plt.title('Corrected Wigner spacing variances'); [plt.text(i,v+.006,f'{v:.6f}',ha='center') for i,v in enumerate(vals)]; plt.tight_layout(); plt.savefig(FIG/'gue_goe_variance_correction.png',bbox_inches='tight'); plt.close()
Dg=np.linspace(-np.pi*np.sqrt(2),7,600); gg=1+Dg/(np.sqrt(2)*np.pi); plt.figure(figsize=(8.5,5.5),dpi=220); plt.plot(Dg,gg); plt.axvline(-np.pi*np.sqrt(2),linewidth=1); plt.axhline(0,linewidth=1); plt.xlabel(r'$D_k=\sqrt{\log\log\tau_k}(X_{k+1}-X_k)$'); plt.ylabel(r'$g_k$'); plt.title(r'Canonical gap dictionary: $g_k=1+D_k/(\sqrt{2}\pi)+o(1)$'); plt.tight_layout(); plt.savefig(FIG/'canonical_D_gap_dictionary.png',bbox_inches='tight'); plt.close()
D_edge=-np.sqrt(2)*np.pi
D_min=float(np.min(D))
plt.figure(figsize=(7.6,5.2),dpi=220)
vals=[D_edge,D_min]
labels=['Leading-order boundary', 'Empirical min D']
plt.bar(labels,vals)
for i,v in enumerate(vals): plt.text(i,v+0.08,f'{v:.6f}',ha='center')
plt.ylabel(r'$D$ value')
plt.title('Empirical minimum vs leading-order gap boundary')
plt.tight_layout()
plt.savefig(FIG/'D_support_consistency.png',bbox_inches='tight')
plt.close()

summary={
    'N':N,
    'clock_max_abs_residual':float(np.max(np.abs(clock_residual))),
    'rho_adjacent_full_prefix':rho,
    'mean_X2_full_prefix':float(np.mean(X**2)),
    'mean_D_full_prefix':float(np.mean(D)),
    'var_D_full_prefix':float(np.var(D)),
    'min_D_full_prefix':float(np.min(D)),
    'mean_gap_full_prefix':float(np.mean(gap)),
    'var_gap_full_prefix':float(np.var(gap)),
    'top250k_pairs':m,
    'top250k_zero_support_count':m+1,
    'tau_median_top250k':float(np.median(tau[:-1][sl])),
    'mean_loglog_tau_top250k':llt,
    'mean_X2_top250k_unique_zero_support':x2_unique,
    'mean_X2_top250k_pair_endpoint_average':x2_pair_endpoint,
    'rho_top250k':rhot,
    'var_gap_top250k':var_gap_t,
    'rho_from_empirical_gap_top250k_unique_X2':rho_measured_unique,
    'rho_from_empirical_gap_top250k_pair_endpoint_X2':rho_measured_pair,
    'rho_from_GUE_Wigner_top250k_unique_X2':rho_gue_unique,
    'rho_from_GUE_Wigner_top250k_pair_endpoint_X2':rho_gue_pair,
    'fixed_mean':float(np.mean(Rfix)),
    'fixed_second_moment':float(np.mean(Rfix**2)),
    'fixed_KS':float(ks_fix),
    'lagged_mean':float(np.mean(Rdata)),
    'lagged_second_moment':float(np.mean(Rdata**2)),
    'lagged_shape_KS':float(ks),
}
(OUT/'numerical_summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
(OUT/'numerical_summary.txt').write_text('\n'.join(f'{a}={b}' for a,b in summary.items())+'\n',encoding='utf-8')
print(json.dumps(summary,indent=2))
