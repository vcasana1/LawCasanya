import numpy as np
TWOPI=2*np.pi
g0=np.load("g_hp.npy")
def offstats(g):
    N=len(g); T=g[-1]; LT=np.log(T/TWOPI); W=120.0
    ds=[];ws=[];j=1
    while True:
        d=g[j:]-g[:-j]; m=d<W
        if not m.any(): break
        dd=d[m]; ds.append(dd); ws.append(4/(4+dd*dd)); j+=1
    d=np.concatenate(ds); w=np.concatenate(ws)
    al=np.arange(1.0,4.001,0.01)
    off=np.array([2*np.sum(w*np.cos(a*LT*d))/N for a in al])
    return N,LT,off.mean(),off.std(),2*w.sum()/N
print("ESCALADO DEL TERMINO FUERA DE DIAGONAL EN LA MESETA (alpha in [1,4])")
print("\n      N |   L_T  | masa |Off| |  media Off |  rms Off  | rms*sqrt(N) | rms*sqrt(N)/L_T")
print("-"*90)
for frac in [1/8,1/4,1/2,1.0]:
    g=g0[:int(len(g0)*frac)]
    N,LT,m,s,mass=offstats(g)
    print(f" {N:6d} | {LT:6.3f} | {mass:9.3f} | {m:+10.5f} | {s:9.5f} | {s*np.sqrt(N):11.3f} | {s*np.sqrt(N)/LT:15.3f}")
print("\n rms*sqrt(N) casi constante  =>  Off(alpha) ~ C/sqrt(N):  cancelacion de RAIZ.")
print(" La masa absoluta del termino fuera de diagonal es ~L_T (crece); el resultado es ~1/sqrt(N).")
