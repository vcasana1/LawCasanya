import numpy as np
TWOPI=2*np.pi
g=np.load("g_hp.npy"); N=len(g); T=g[-1]; LT=np.log(T/TWOPI); LTm=np.log(T)
W=120.0; delta=0.0008
nb=int(W/delta)+1; hist=np.zeros(nb)
j=1
while True:
    d=g[j:]-g[:-j]
    m=d<W
    if not m.any(): break
    dd=d[m]; hist+=np.bincount((dd/delta).astype(int),weights=4/(4+dd*dd),minlength=nb)[:nb]
    j+=1
db=(np.arange(nb)+0.5)*delta
print(f"N={N}  T={T:.0f}  L_T=log(T/2pi)={LT:.4f}  ventana W={W}  offsets usados j<={j-1}")
print(f"masa fuera de diagonal sum w = {hist.sum():.1f}   (2/N)*eso = {2*hist.sum()/N:.4f}  ~ L_T = {LT:.3f}\n")
def Off(alpha,L=LT): return 2*np.sum(hist*np.cos(alpha*L*db))/N
# validacion exacta sin binning en unos pocos alpha
def Off_exact(alpha,L=LT):
    c=alpha*L; acc=0.0; jj=1
    while True:
        d=g[jj:]-g[:-jj]; m=d<W
        if not m.any(): break
        dd=d[m]; acc+=np.sum(np.cos(c*dd)*4/(4+dd*dd)); jj+=1
    return 2*acc/N
print("validacion binning vs exacto:")
for a in [0.5,1.4,2.3]: print(f"   alpha={a}:  binned={Off(a):+.5f}   exacto={Off_exact(a):+.5f}")
print("\nF(alpha) = 1 (DIAGONAL) + Off(alpha).   La meseta F->1  <=>  Off->0.")
print("\n  alpha |    Off(alpha) |   F(alpha) | Montgomery F | (F-1)")
print("-"*66)
for a in [0.05,0.2,0.4,0.6,0.8,0.95,1.0,1.1,1.3,1.5,1.8,2.0,2.4,3.0]:
    o=Off(a); mont=(T/TWOPI)**(-2*a)*LT+a if a<=1 else 1.0
    print(f" {a:6.2f} | {o:+13.5f} | {1+o:10.5f} | {mont:12.5f} | {o:+.5f}")
al=np.arange(0.02,4.001,0.005); off=np.array([Off(a) for a in al])
for lo,hi in [(0.02,1.0),(1.0,1.5),(1.5,2.0),(2.0,3.0),(3.0,4.0)]:
    k=(al>=lo)&(al<hi); s=off[k]
    print(f"\n alpha in [{lo:.2f},{hi:.2f}): media Off={s.mean():+.5f}  rms={s.std():.5f}  max|Off|={np.abs(s).max():.5f}")
k=al>=1.0
print(f"\n MESETA alpha>=1 :  media Off = {off[k].mean():+.6f}   rms = {off[k].std():.6f}")
print(f"   1/sqrt(N) = {1/np.sqrt(N):.6f}    L_T/sqrt(N) = {LT/np.sqrt(N):.6f}")
np.savez("corrII.npz",al=al,off=off,N=N,T=T,LT=LT)
