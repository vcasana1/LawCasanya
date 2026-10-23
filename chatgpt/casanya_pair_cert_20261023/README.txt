CASANYA/xi: TWO LOCAL TWO-ZERO CERTIFICATES (2026-10-23)

STATUS: computational interval enclosures using mpmath.iv at 55 decimal digits.
They are reproducible numerical certificates contingent on correctness of the
interval-special-function implementation. Independent certification with
Arb/FLINT, a proof assistant, or independently audited interval gamma bounds
is a remaining publication-grade verification step.

No zeross.bin or true zero ordinates are loaded or supplied to construct
any centers. Both rational centers were proposed by scanning derivative
extrema of xi(1/2+it) near the RvM neighborhood of index 889. The pair
labels 1283 and 1290 designate the approximate HEIGHT, not an ordinal index.

Run:
  python verify_pair.py 1283
  python verify_pair.py 1290

Define f(z) = xi(1/2+iz) and g(z)=A f(z), A=10^433 (case 1283) or
A=10^435 (case 1290). For given rational b, h, set
  Q(z) = g''(b)/2 * [(z-b)^2-h^2].
Using the Taylor formula at b, on |z-b|<=3h/2,
  |g-Q| <= |g(b)+g''(b)h^2/2| + |g'(b)| |z-b|
           + M3 |z-b|^3/6,
  M3=max_{|z-b|<=3h/2} |g'''(z)|.
On the circles |z-(b+-h)|=h/4,
  |Q| >= 7 |g''(b)| h^2/32.
On the outer circle |z-b|=3h/2,
  |Q| = 5 |g''(b)| h^2/8.
Our inequalities pass on ALL THREE circles, so Rouche establishes
exactly one zero in each of the two small disks, and exactly two
zeros in the outer disk, counting multiplicity. Reality of g on the
real axis and uniqueness in each conjugation-invariant small disk
force each zero to be real and simple.

Interval method:
- Evaluate xi at 256th roots of unity translated by b, using a
  1024-term Euler--Maclaurin continuation of zeta with 22 Bernoulli
  corrections and an analytic |remainder| < 1e-23 on the sample circle.
- Use interval arithmetic for the gamma factor and all operations.
- Discrete Fourier coefficients recover Taylor a_0,...,a_56. Their
  alias errors are bounded from Cauchy by an explicit uniform bound
  on |g| in |z-b|<=2: 10^33 (case 1283) or 10^25 (case 1290).
- Cover the ENTIRE circle |z-b|=3h/2 by 256 angular intervals;
  interval Horner evaluation of the polynomial of g''' bounds its
  maximum; add the exact Cauchy tail bound for terms >=57.
- Outward safety inflation of 1e-12 is applied to displayed floating
  upper/lower bounds after interval evaluation.

For the crude global bound, if |z-b|<=2, put s=1/2+iz.
Then -3/2<=Re s<=5/2 and Im s>=b-2>1281.
Euler--Maclaurin with N=1024, m=22 yields |zeta(s)|<10^9.
Using w=s/2, gamma recurrence and Stirling in the right half-plane,
  |Gamma(w)| = |Gamma(w+2)/(w(w+1))|
             <= 500 exp(-pi Im(s)/4)
in this strip. (One can bound |Gamma(w+2)| by
sqrt(2pi)|w+2|^(Re(w)+3/2) exp(-pi Im(w)/2 +1/(6|w+2|)),
with |w+2|<700 and |w(w+1)|>644^2.)
As |s(s-1)|/2<10^6 and |pi^(-s/2)|<3,
  |f(z)| <= 1.5e18 exp(-pi (b-2)/4).
Hence |f|<1e-400 for b=1283.159048033 and
|f|<1e-410 for b=1290.255802206, yielding the scaled bounds above.

OUTPUT (all derivative values refer to the scaled g):
HEIGHT ~1283:
  b=1283.159048033, h=0.164715498.
  |g''(b)| > 52.0346348075; M3 < 180.855125215.
  h*M3/|g''(b)| < 0.572497 < 84/125.
  small-circle |g-Q| < 0.263096 < |Q| lower 0.308822;
  outer-circle |g-Q| < 0.454629 < |Q| lower 0.882351.
  one simple real zero in EACH interval
    (1282.9531536605,1283.0355114095),
    (1283.2825846565,1283.3649424055).

HEIGHT ~1290:
  b=1290.255802206, h=0.154422788.
  |g''(b)| > 18.9905819705; M3 < 63.282575959.
  h*M3/|g''(b)| < 0.514586 < 84/125.
  small-circle |g-Q| < 0.075858 < |Q| lower 0.099062;
  outer-circle |g-Q| < 0.131082 < |Q| lower 0.283035.
  one simple real zero in EACH interval
    (1290.062773721,1290.139985115),
    (1290.371619297,1290.448830691).

LIMITATIONS:
- No claim about which global ordinal indices these four roots carry.
- No global RH claim: other real and non-real zeros may exist elsewhere.
- These are TWO concrete verified PAIRS, not proof of infinite validity
  of the fixed-center quadratic/quartic pair criterion. An independent
  verified arithmetic backend is needed before publication-grade claims.
- A separate abstract theorem gives infinitely many certifiable pairs
  via adaptive ONE-ZERO Rouché disks, assuming the established
  unconditional positive proportion of simple critical-line zeros.
  That theorem does NOT verify the fixed quartic isolation hypothesis.

References: J. B. Conrey, More than two fifths of the zeros of the
Riemann zeta function are on the critical line (1989); exact source
not re-verified for this experiment. No web research performed.