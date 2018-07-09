# ProjectEuler+ > Project Euler #15: Lattice paths
# Walking on grids. And not slipping.
#
# https://www.hackerrank.com/contests/projecteuler/challenges/euler015
# challenge id: 2641
#

import math

"""
Cf. https://en.wikipedia.org/wiki/Lattice_path
"""


def C(n, k):
    """ Coefficient binomial """
    return math.factorial(n) // math.factorial(k) // math.factorial(n - k)


for _ in range(int(input())):
    m, n = map(int, input().split())
    print(C(m + n, n) % 1000000007)
