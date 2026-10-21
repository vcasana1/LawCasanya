// Same finite Euler phase and prime-power sine sum; macOS vForce vectors.
#include <Accelerate/Accelerate.h>
#include <vector>
extern "C" void phase_vec(int n,const double*t,int m,const double*f,const double*a,int euler,double*out){
    std::vector<double> arg(n),s(n),c(n),den(n),ang(n);
    for(int i=0;i<n;++i)out[i]=0;
    for(int j=0;j<m;++j){
        for(int i=0;i<n;++i)arg[i]=t[i]*f[j];
        if(euler){
            vvsincos(s.data(),c.data(),arg.data(),&n);
            for(int i=0;i<n;++i){den[i]=1-a[j]*c[i];s[i]*=a[j];}
            vvatan2(ang.data(),s.data(),den.data(),&n);
            for(int i=0;i<n;++i)out[i]-=ang[i]/3.1415926535897932384626433832795;
        }else{
            vvsin(s.data(),arg.data(),&n);
            for(int i=0;i<n;++i)out[i]+=a[j]*s[i];
        }
    }
}
