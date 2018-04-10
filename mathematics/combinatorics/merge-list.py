# Merge List
# Help Shashank in merging two list.
#
# https://www.hackerrank.com/challenges/merge-list/problem
#

from math import factorial


def C(n, r):
    return factorial(n) // factorial(r) // factorial(n - r)


for i in range(int(input())):
    n, m = map(int, input().split())
    print(C(n + m, n) % 1000000007)
