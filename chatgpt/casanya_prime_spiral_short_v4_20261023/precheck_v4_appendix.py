import mpmath as mp
mp.mp.dps = 65
cases = [
 ('1283.159048033','0.164715498','1e433','180.855125215'),
 ('1290.255802206','0.154422788','1e435','63.282575959')]
def F(z):
    s = mp.mpf('0.5') + 1j*z
    return s*(s-1)/2 * mp.pi**(-s/2) * mp.gamma(s/2)*mp.zeta(s)
for bs,hs,scale,M3s in cases:
    b,h,t,M3=map(mp.mpf,(bs,hs,scale,M3s))
    a=t*F(b); a1=t*mp.diff(F,b,1); a2=t*mp.diff(F,b,2)
    err=abs(a+a2*h*h/2)
    sl=err+5*h*abs(a1)/4+mp.mpf(125)/384*M3*h**3
    sr=7*abs(a2)*h*h/32
    bl=err+3*h*abs(a1)/2+mp.mpf(9)/16*M3*h**3
    br=5*abs(a2)*h*h/8
    print(bs, 'small',sl,sr,'outer',bl,br)
