# Mathematics > Combinatorics > Coinage
# Find the number of ways to pay a given amount, given a set of coins with prescribed denominations.
#
# https://www.hackerrank.com/challenges/coinage/problem
#

import sys

def subcase(t, c1, c2, n1, n2):
    minC2 = (t - c1 * min(n1, t // c1) +c2-1) // c2
    maxC2 = min(t // c2, n2)
    result = max(maxC2 - minC2 + 1, 0)
    return result

def coinage(n, _, q):
    a, b, c, d = q
    result = 0
    for i in range(0, n // 5 + 1):
        result += subcase(5 * i, 5, 10, c, d) * subcase(n - 5 * i, 1, 2, a, b)
    return result

for _ in range(int(input())):
    N = int(input())
    quantite = list(map(int, input().split()))
    print(N, quantite, file=sys.stderr)
    print(coinage(N, 0, quantite))
