"""Optional identical-formula vForce backend; pure NumPy remains the default."""
import ctypes,json,time
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
lib=ctypes.CDLL(str(HERE/'fastphase.dylib'))
ptr=np.ctypeslib.ndpointer(dtype=np.float64,ndim=1,flags='C_CONTIGUOUS')
lib.phase_vec.argtypes=[ctypes.c_int,ptr,ctypes.c_int,ptr,ptr,ctypes.c_int,ptr]
def evaluate(P,t):
    t=np.ascontiguousarray(t,dtype=np.float64);s=np.empty_like(t)
    lib.phase_vec(len(t),t,len(P.f),np.ascontiguousarray(P.f),np.ascontiguousarray(P.a),P.kind=='euler',s)
    return s
if __name__=='__main__':
    from pilot_models import Model,OUT
    records=[]
    for method in ['LeClair','Gonek']:
        m=Model(method,8192);t=np.linspace(6.3,1132480.,50000)
        start=time.perf_counter();expected=m.P(t,derivative=False)[0];old=time.perf_counter()-start
        start=time.perf_counter();actual=evaluate(m.P,t);new=time.perf_counter()-start
        record=dict(method=method,n=len(t),numpy_seconds=old,vforce_seconds=new,max_phase_difference=float(np.max(np.abs(actual-expected))),
                    floor_half_level_mismatches=int(np.sum(np.floor(m.smooth(t)+actual+.5)!=np.floor(m.smooth(t)+expected+.5))))
        assert record['max_phase_difference']<1e-12 and record['floor_half_level_mismatches']==0
        records.append(record);print(record,flush=True)
    (OUT/'fastphase_validation.json').write_text(json.dumps(records,indent=2))
