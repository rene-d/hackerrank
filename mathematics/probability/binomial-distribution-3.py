# Mathematics > Probability > Binomial Distribution #3
# Problems based on basic statistical distributions.
#
# https://www.hackerrank.com/challenges/binomial-distribution-3/problem
# challenge id: 12841
#

from __future__ import print_function
from math import factorial

def b(n, x, p):
    return factorial(n) / factorial(n - x) / factorial(x) * (p ** x) * (1 - p) ** (n - x)

p = 0.12        # proba piston is rejected
n = 10          # number of trials

r = b(n, 0, p) + b(n, 1, p) + b(n, 2, p)        # 0 ou 1 ou 2 rejets
print("%.3f" % r)

r = sum(b(n, i, p) for i in range(2, n + 1))    # 2 à 12 rejets
print("%.3f" % r)
