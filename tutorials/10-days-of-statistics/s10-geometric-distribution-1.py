# Tutorials > 10 Days of Statistics > Day 4: Geometric Distribution I
# Problems based on basic statistical distributions.
#
# https://www.hackerrank.com/challenges/s10-geometric-distribution-1/problem
# challenge id: 21244
#


def g(n, p):
    return p * (1 - p) ** (n - 1)

ko, total = map(int, input().split())
n = int(input())

r = g(n, ko / total)
print("%.3f" % r)
