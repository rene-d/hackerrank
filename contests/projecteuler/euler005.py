# ProjectEuler+ > Project Euler #5: Smallest multiple
# Smallest number which divides all numbers from 1 to N.
#
# https://www.hackerrank.com/contests/projecteuler/challenges/euler005
#

import math
import functools


def gcd(*numbers):
    """ greatest common divisor """
    return functools.reduce(math.gcd, numbers)


def lcm(*numbers):
    """ least common multiple """
    return functools.reduce(lambda a, b: (a * b) // gcd(a, b), numbers, 1)

for _ in range(int(input())):
    n = int(input())
    print(lcm(*range(1, n + 1)))
