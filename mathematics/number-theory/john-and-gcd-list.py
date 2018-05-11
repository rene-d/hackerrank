# Mathematics > Number Theory > John and GCD list
# Help John in making a list from GCD list
#
# https://www.hackerrank.com/challenges/john-and-gcd-list/problem
#

import math
import functools


def gcd(*numbers):
    """ greatest common divisor """
    return functools.reduce(math.gcd, numbers)


def lcm(*numbers):
    """ least common multiple """
    return functools.reduce(lambda a, b: (a * b) // gcd(a, b), numbers, 1)


# la réponse est le ppcm "glissant" des Ai

for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))

    x = A[0]
    B = [x]
    i = 1
    while i < n:
        y = A[i]
        B.append(lcm(x, y))
        x = y
        i += 1
    B.append(A[-1])
    print(*B)
