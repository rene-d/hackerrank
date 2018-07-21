# ProjectEuler+ > Project Euler #108: Diophantine reciprocals I
#
# https://www.hackerrank.com/contests/projecteuler/challenges/euler108
# challenge id: 2734
#

# cf. https://github.com/rene-d/math/blob/master/projecteuler/p108.py
# cependant, les testcases 7-11 requièrent une meilleure méthode de factorisation

# version "je triche un peu" et j'économise Eratosthène, Miller-Rabin et Pollard-Brent
# __import__("sys").path.append('/var/ml/python3/lib/python3.5/site-packages')
# from sympy.ntheory import factorint

from math import gcd
import random
from itertools import compress

# https://stackoverflow.com/questions/4643647/fast-prime-factorization-module

# https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/46635266#46635266
def primes_below(n):
    """ Returns a list of primes < n for n > 2 """
    sieve = bytearray([True]) * (n//2+1)
    for i in range(1,int(n**0.5)//2+1):
        if sieve[i]:
            sieve[2*i*(i+1)::2*i+1] = bytearray((n//2-2*i*(i+1))//(2*i+1)+1)
    return [2,*compress(range(3,n,2), sieve[1:])]


small_prime_set_max = 100000
small_prime_set = set(primes_below(small_prime_set_max))


def is_prime(n, precision=7):
    # http://en.wikipedia.org/wiki/Miller-Rabin_primality_test#Algorithm_and_running_time
    if n < 1:
        raise ValueError("Out of bounds, first argument must be > 0")
    elif n <= 3:
        return n >= 2
    elif n % 2 == 0:
        return False
    elif n < small_prime_set_max:
        return n in small_prime_set

    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(precision):
        a = random.randrange(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1: continue

        for r in range(s - 1):
            x = pow(x, 2, n)
            if x == 1: return False
            if x == n - 1: break
        else:return False

    return True


# https://comeoncodeon.wordpress.com/2010/09/18/pollard-rho-brent-integer-factorization/
def pollard_brent(n):
    if n % 2 == 0: return 2
    if n % 3 == 0: return 3

    y, c, m = random.randint(1, n - 1), random.randint(1, n - 1), random.randint(1, n - 1)
    g, r, q = 1, 1, 1
    while g == 1:
        x = y
        for i in range(r):
            y = (pow(y, 2, n) + c) % n

        k = 0
        while k < r and g == 1:
            ys = y
            for i in range(min(m, r - k)):
                y = (pow(y, 2, n) + c) % n
                q = q * abs(x-y) % n
            g = gcd(q, n)
            k += m
        r *= 2

    if g == n:
        while True:
            ys = (pow(ys, 2, n) + c) % n
            g = gcd(abs(x - ys), n)
            if g > 1: break

    return g


small_primes = primes_below(1000) # might seem low, but 1000*1000 = 1000000, so this will fully factor every composite < 1000000


def prime_factors(n):
    factors = []

    for checker in small_primes:
        while n % checker == 0:
            factors.append(checker)
            n //= checker
        if checker > n:
            break

    if n < 2: return factors

    while n > 1:
        if is_prime(n):
            factors.append(n)
            break
        factor = pollard_brent(n) # trial division did not fully factor, switch to pollard-brent
        factors.extend(prime_factors(factor)) # recurse to factor the not necessarily prime factor returned by pollard-brent
        n //= factor

    return factors


def factorint(n):
    factors = {}
    for p in prime_factors(n):
        if p in factors:
            factors[p] += 1
        else:
            factors[p] = 1
    return factors


for _ in range(int(input())):
    n = int(input())
    p = 1
    for _, e in factorint(n).items():
        p *= 2 * e + 1                  # nombre de diviseurs de n²
    print((p + 1) // 2)
