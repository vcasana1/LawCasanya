# Normalized gap s_k for the reported close pair k = 1000055 (Heuristic 6.8, eq. (6.36)).
# gamma_k in log(gamma_k/2pi) is replaced by the RvM clock tau_k, N_0(tau_k) = k - 1/2.
# The separation 0.038304245 is the archived reported value (Appendix B); no zero data are read.
import mpmath as mp
mp.mp.dps = 30
k = 1000055
sep = mp.mpf('0.038304245')
tau = mp.findroot(lambda t: 1 + mp.siegeltheta(t)/mp.pi - (k - mp.mpf(1)/2), 600270)
s = sep * mp.log(tau/(2*mp.pi)) / (2*mp.pi)
print("tau_k =", mp.nstr(tau, 15))
print("s_k   =", mp.nstr(s, 10))
