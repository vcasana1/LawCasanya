"""
Appendix A.1 -- Certified lower bound for theta'(14).
Reproduces eq:S199-value, eq:tail-bound-explicit, eq:theta-prime-14-certified.
"""
import mpmath as mp
mp.mp.dps = 30

gammaE = mp.euler
t = mp.mpf(14)

def term_real(k):
    # Re[1/(k+1) - 1/(k+1/4+7i)]
    denom = (mp.mpf(k) + mp.mpf('0.25'))**2 + mp.mpf('49')
    return mp.mpf(1)/(k+1) - (mp.mpf(k) + mp.mpf('0.25'))/denom

S199 = sum(term_real(k) for k in range(200))
print(f"S_199                 = {S199}")

tail_bound = mp.mpf(3) / (4*199)
print(f"tail bound            = {tail_bound}")

Repsi_center = S199 - gammaE
Repsi_lo = Repsi_center - tail_bound
Repsi_hi = Repsi_center + tail_bound
print(f"Re psi(1/4+7i) in     [{Repsi_lo}, {Repsi_hi}]")

logpi = mp.log(mp.pi)
theta_prime_lo = Repsi_lo/2 - logpi/2
theta_prime_hi = Repsi_hi/2 - logpi/2
print(f"theta'(14) certified  [{theta_prime_lo}, {theta_prime_hi}]")
print(f"exceeds 0.40016?      {theta_prime_lo > mp.mpf('0.40016')}")

# independent cross-check via mpmath's own digamma implementation
ref = mp.re(mp.digamma(mp.mpf('0.25')+7j))/2 - logpi/2
print(f"independent reference theta'(14) = {ref}")
print(f"reference inside certified interval? {theta_prime_lo <= ref <= theta_prime_hi}")
