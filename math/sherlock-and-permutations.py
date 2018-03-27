"""
Sherlock and Permutations

https://www.hackerrank.com/challenges/sherlock-and-permutations
"""

import sys
from math import factorial


def C(n, k):
    return factorial(n) // factorial(k) // factorial(n - k)


def solve(m0, m1):
    m1 -= 1

    if m0 == 0 or m1 == 0:
        print(1)
    else:
        print(C(m0 + m1, m0) % 1000000007)


if len(sys.argv) == 3:
    solve(int(sys.argv[1]), int(sys.argv[2]))
else:
    nb = int(input())
    for _ in range(nb):
        m0, m1 = map(int, input().split())
        solve(m0, m1)
