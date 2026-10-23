import mpmath as mp
import sympy as sp
import math,time,sys
mp.iv.dps = 55
iv=mp.iv
CASE = int(sys.argv[1]) if len(sys.argv)>1 else 1290
PARAM = {1283:('1283.159048033','0.164715498','1e433','1e33'),1290:('1290.255802206','0.154422788','1e435','1e25')}
BSTR,HSTR,SCALE,BOUND=PARAM[CASE]
b=iv.mpf(BSTR)
h=iv.mpf(HSTR)
M=256
K=56
N=1024
P=22
lnN=iv.ln(N)
ll=[iv.ln(n) for n in range(1,N)]
bern=[iv.mpf(int(sp.bernoulli(2*k).p))/iv.mpf(int(sp.bernoulli(2*k).q))/iv.mpf(math.factorial(2*k)) for k in range(1,P+1)]
# Strict, analytically established bound on EM remainder on the sampling circle:
# |s+j|<1340, Re s>=-1/2, 2*pi>6, N=1024,
# |R22| < 4*(1340/(6*1024))**44 *1024**1.5/42 < 1e-23.
remainder=iv.mpc(iv.mpf(['-1e-23','1e-23']),iv.mpf(['-1e-23','1e-23']))
logpi=iv.ln(iv.pi)

# Euler--Maclaurin zeta approximation with an explicit complex remainder rectangle.
# Remainder uses periodic Bernoulli integral, bounded for the unit circle by
# 4*(1340/(6*1024))**44 *1024**1.5/42 < 1e-23.
# All summands are evaluated with outward-rounded interval arithmetic.
def zeta_interval(s):
  u=iv.mpc(0)
  for l in ll:
    u+=iv.exp(-s*l)
  u+=iv.exp((1-s)*lnN)/(s-1)+iv.exp(-s*lnN)/2
  poch=iv.mpc(1)
  last=0
  for k in range(1,P+1):
    want=2*k-1
    while last<want:
      poch*=s+last
      last+=1
    u+=bern[k-1]*poch*iv.exp((-s-(2*k)+1)*lnN)
  return u+remainder

def Xi_interval(z):
  s=iv.mpf('0.5')+iv.j*z
  u=zeta_interval(s)
  return (s*(s-1)/2)*iv.exp(-s*logpi/2)*iv.gamma(s/2)*u

def upp(x):
  return float(str(x.b).strip('[]').split(',')[0]) * (1+1e-12)
def low(x):
  return float(str(x.a).strip('[]').split(',')[0]) * (1-1e-12)

def absub(z):
  return upp(abs(z))

def point_range(ivreal):
  return [str(ivreal.a),str(ivreal.b)]

start=time.time()
coeff=[iv.mpc(0) for j in range(K+1)]
for k in range(M):
  w=iv.exp(iv.j*2*iv.pi*k/M)
  f=iv.mpf(SCALE)*Xi_interval(b+w)
  inv=1/w
  cur=iv.mpc(1)
  for j in range(K+1):
    coeff[j] +=f*cur
    cur*=inv
  if k in [0,63,127,191,255]:
    print('node',k,'time',round(time.time()-start,1),flush=True)
coeff=[a/M for a in coeff]
Mout=iv.mpf(BOUND)
for j in range(K+1):
  # DFT alias error bound derived from Cauchy, outer radius=2, inner radius=1
  e=Mout*(iv.mpf('0.5')**(M+j))/(1-iv.mpf('0.5')**M)
  coeff[j] += iv.mpc(iv.mpf([-upp(e),upp(e)]),iv.mpf([-upp(e),upp(e)]))

# a0,a1,a2 enclosures, all coeff numerical enclosures include EM remainder.
for j in range(5):
 print('coef',j, 'RE', point_range(coeff[j].real),'IM',point_range(coeff[j].imag),'abs_up',absub(coeff[j]),flush=True)

# Taylor coefficients are real because Xi(1/2+it) is real for real t; use their real interval enclosures.
a=[x.real for x in coeff]
d2=2*a[2]
rat = a[0] + a[2]*h*h # constant error
# F(z)-Q(z) = rat + a1 x + sum_{n>=3} a_n x^n
H=upp(h)
R=1.5*H
M3_low_series=sum(j*(j-1)*(j-2)*absub(coeff[j])*(R**(j-3)) for j in range(3,K+1))
# tail j>K Cauchy; bound monotonically by formula with q=R/2
q=R/2
m=K+1
M3_tail=float(BOUND)/8 * (m*(m-1)*(m-2)*q**(m-3)/(1-q) + 3*m*(m-1)*q**(m-2)/(1-q)**2 + 6*m*q**(m-1)/(1-q)**3 + 6*q**m/(1-q)**4)  # exact derivative of q^m/(1-q)

# A sharp rigorous maximum-modulus bound for F''' on |x|<=R:
# cover the whole boundary by interval angular arcs and use Horner.
narc=256
M3arc=0
for j in range(narc):
   angle=iv.pi*2*iv.mpf([str(j/narc),str((j+1)/narc)])  # exact dyadic decimals, 256 arcs
   x=iv.mpf(str(R))*iv.exp(iv.j*angle)
   v=iv.mpc(0)
   for n in range(K,2,-1):
      v=v*x + n*(n-1)*(n-2)*a[n]
   M3arc=max(M3arc,absub(v))
print('M3_triangle',M3_low_series,'M3_boundary_arcs',M3arc,'M3_tail',M3_tail)
M3=M3arc+M3_tail

eta=H*M3/low(abs(d2))
constant_error=absub(iv.mpc(rat))
linear_error=absub(iv.mpc(a[1]))
# small circle min |Q| = 7|d2|h^2/32
small_rhs=7*low(abs(d2))*(H/(1+1e-12))**2/32
small_lhs=constant_error+linear_error*(5*H/4)+M3*(5*H/4)**3/6
outer_rhs=5*low(abs(d2))*(H/(1+1e-12))**2/8
outer_lhs=constant_error+linear_error*R+M3*R**3/6
print('VERIFICATION')
for name,num in [('b',float(BSTR)),('h',H),('f2_lower',low(abs(d2))),('M3upper',M3),('eta',eta),('constant_error',constant_error),('linear_error',linear_error),('small_LHS',small_lhs),('small_RHS',small_rhs),('outer_LHS',outer_lhs),('outer_RHS',outer_rhs),('time',time.time()-start)]:print(name,num)
passed=small_lhs<small_rhs and outer_lhs<outer_rhs
print('PASS',passed)
assert passed
assert eta < 84/125
print('PAIR_BRACKETS',float(BSTR)-float(HSTR)*1.25,float(BSTR)-float(HSTR)*.75,float(BSTR)+float(HSTR)*.75,float(BSTR)+float(HSTR)*1.25)
