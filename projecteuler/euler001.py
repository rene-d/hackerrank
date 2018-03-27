"""
Project Euler #1: Multiples of 3 and 5

https://www.hackerrank.com/contests/projecteuler/challenges/euler001
"""

import sys


def t(n):
    """ ∑x = 1+2+..+x = x∗(x+1)/2 """
    return n * (n + 1) // 2


def sum_3_5(n):
    """ somme des multiples de 3, de 5, en enlevant ceux de 3*5 (déjà comptés) """
    return 3 * t(n // 3) + 5 * t(n // 5) - 15 * t(n // 15)


if len(sys.argv) > 1:
    for i in sys.argv[1:]:
        print(i, sum_3_5(int(i) - 1))
else:
    nb = int(input().strip())
    for _ in range(nb):
        n = int(input().strip())
        print(sum_3_5(n - 1))
