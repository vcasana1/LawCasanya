"""Convergents of the continued fraction e = [2; 1, 2, 1, 1, 4, 1, 1, 6, ...] whose numerator and denominator
are both prime powers, with upsilon = 1 - log(h/q) (the quotient frequency of the pair (q, h)) and the ordinal
period log(T/2pi)/|upsilon| at T = 5e5.  Exact integer arithmetic; upsilon in double precision.
Writes ../outputs/e_convergents_v15.txt (same text as the console)."""
import math, os

HERE = os.path.dirname(os.path.abspath(__file__))
out = open(os.path.join(HERE, '../outputs/e_convergents_v15.txt'), 'w')


def say(s):
    print(s); out.write(s + '\n')


def prime_power(n):
    if n < 2:
        return False
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            return n == 1
        p += 1
    return True


a = [2] + sum(([1, 2 * j, 1] for j in range(1, 12)), [])
h0, h1, q0, q1 = 1, a[0], 0, 1
conv = [(h1, q1)]
for x in a[1:]:
    h0, h1 = h1, x * h1 + h0
    q0, q1 = q1, x * q1 + q0
    conv.append((h1, q1))
say('first 16 convergents h/q of e; * = both prime powers')
for h, q in conv[:16]:
    ups = 1 - math.log(h / q)
    per = math.log(5e5 / (2 * math.pi)) / abs(ups)
    say(f"{'*' if prime_power(h) and prime_power(q) else ' '} {h:>7d}/{q:<7d} upsilon = {ups:+.6e}  period at T=5e5: {per:.4e}")
out.close()
