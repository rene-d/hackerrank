# Tutorials > 10 Days of Statistics > Day 4: Geometric Distribution II
# Problems based on basic statistical distributions.
#
# https://www.hackerrank.com/challenges/s10-geometric-distribution-2/problem
# challenge id: 21245
#

def g(n, p):
    return p * (1 - p) ** (n - 1)

ko, total = map(int, input().split())
n = int(input())

r = sum(g(n, ko / total) for n in range(1, 6))
print("%.3f" % r)
