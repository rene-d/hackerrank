# nCr table
# Help Jim calculating nCr values
#
# https://www.hackerrank.com/challenges/ncr-table/problem
#

from math import factorial


def C(n, r):
    return factorial(n) // factorial(r) // factorial(n - r)


for i in range(int(input())):
    n = int(input())
    print(' '.join(str(C(n, r) % 1000000000) for r in range(n + 1)))
