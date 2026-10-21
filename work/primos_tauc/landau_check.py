import numpy as np
K=17061
g=np.fromfile('/tmp/LawCasanya/data/zeross.bin','<f8')[:K]
tau=np.fromfile('/tmp/LawCasanya/data/zLamb.bin','<f8')[:K]
tc=np.load('best_K17061.npy')[0]
T=g[-1]
def lam(n):
    for p in range(2,n+1):
        if n%p==0:
            m=n
            while m%p==0: m//=p
            return np.log(p) if m==1 else 0.0
print('T = %.1f'%T)
print('%6s %12s %22s %22s %22s'%('n','-(T/2pi)L/sqrt n','sum n^{i gamma}','sum n^{i tau}','sum n^{i tauc}'))
for n in [2,3,4,5,6,7,8,9,10,11,12,13,16,25,30,49,97,101,500,997,1000,2003,5003]:
    u=np.log(n); L=lam(n); main=-(T/(2*np.pi))*L/np.sqrt(n)
    s=[np.sum(np.exp(1j*u*k)) for k in (g,tau,tc)]
    print('%6d %12.2f '%(n,main)+' '.join('%10.2f%+10.2fi'%(z.real,z.imag) for z in s))
