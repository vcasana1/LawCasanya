"""Independent numerical checks of the two exact identities added to the paper."""
import json
from pathlib import Path
import numpy as np
from scipy.integrate import quad


def main():
    checks = {}
    # A repeated ordinate and a nonmonotone model exercise both delicate cases.
    gamma=np.array([1.0,2.0,2.0,3.5,4.2])
    F=lambda t: np.sin(3*t)+0.2*t
    dF=lambda t: 3*np.cos(3*t)+0.2
    u=np.arange(1,len(gamma)+1)-0.5-F(gamma)
    for power in (2,4,6):
        left=sum(quad(lambda t:(k+1-F(t))**power*dF(t),
                      gamma[k],gamma[k+1],epsabs=1e-10)[0]
                 for k in range(len(gamma)-1))
        P=lambda x: ((0.5+x)**(power+1)+(0.5-x)**(power+1))/(power+1)
        right=sum(P(x) for x in u[1:-1]) + (
            (0.5+u[0])**(power+1)+(0.5-u[-1])**(power+1))/(power+1)
        err=abs(left-right)
        if err>1e-8*max(1,abs(right)):
            raise AssertionError(('jump identity',power,left,right))
        checks[f'jump_identity_power_{power}_absolute_error']=float(err)
    # Integrate the positive-part overlap formula, not the antiderivative used
    # in the manuscript, and compare with the closed logarithmic expression.
    for th in (0.1,0.3,0.5,0.8,0.95):
        h=lambda x:max(1-abs(x),0)
        def f(a):
            if th-1 <= a <= 1:
                return 0.0
            kernel=1-h(a)-h(th-a)-h(th)+2*max(1-max(abs(a),abs(th-a),th),0)
            return kernel/(a*(th-a))
        edges=[-np.inf,-1,th-1,1,1+th,np.inf]
        value=sum(quad(f,a,b,epsabs=1e-11)[0] for a,b in zip(edges,edges[1:]))
        exact=-2*((1+th)*np.log1p(th)+(1-th)*np.log1p(-th))/th
        err=abs(value-exact)
        if err>1e-9:
            raise AssertionError(('kernel integral',th,value,exact))
        checks[f'kernel_integral_theta_{th}_absolute_error']=float(err)
    path=Path(__file__).resolve().parents[1]/'outputs'/'identity_checks.json'
    path.write_text(json.dumps(checks,indent=2)+'\n')
    print(json.dumps(checks,indent=2))


if __name__=='__main__':
    main()
