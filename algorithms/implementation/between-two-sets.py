# Between Two Sets
# Find the number of integers that satisfies certain criteria relative to two sets.
# 
# https://www.hackerrank.com/challenges/between-two-sets/problem
# 

import math
import functools


def gcd(*numbers):
    """ greatest common divisor """
    return functools.reduce(math.gcd, numbers)


def lcm(*numbers):
    """ least common multiple """
    return functools.reduce(lambda a, b: (a * b) // gcd(a, b), numbers, 1)


def getTotalX(a, b):
    # Complete this function
    f = lcm(*a)     # ppcm
    k = f
    n = 0
    while k <= max(b):
        if all(i % k == 0 for i in b):
            n += 1  # tous les nombres b sont multiples de k (un multiple de f)
        k += f
    return n
    

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    total = getTotalX(a, b)
    print(total)
