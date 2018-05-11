# 101 Hack June 2016 > Easy GCD
# Find the maximum number less than K such that GCD of all numbers is still more than one!
#
# https://www.hackerrank.com/contests/101hack38/challenges/easy-gcd-1
#

import math
import functools


def gcd(*numbers):
    """ greatest common divisor """
    return functools.reduce(math.gcd, numbers)


def diviseur(n):
    """ premier diviseur premier de n """
    i = 2
    while i * i <= n:
        q, r = divmod(n, i)
        if r == 0:
            return i
        i += 1
    return n


n, k = map(int, input().split())
A = list(map(int, input().split()))
g = gcd(*A)

g = diviseur(g)
print((k // g) * g)
