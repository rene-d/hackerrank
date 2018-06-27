# Mathematics > Probability > Binomial Distribution #1
# Problems based on basic statistical distributions.
#
# https://www.hackerrank.com/challenges/binomial-distribution-1/problem
# challenge id: 12839
#

from __future__ import print_function
from math import factorial

# b(x,n,p) = C(n,p) * p^x * (1-p)^(n-x)

# x: number of successes
# n: total number of trials
# p: probability of success of 1 trial

def b(n, x, p):
    return factorial(n) / factorial(n - x) / factorial(x) * (p ** x) * (1 - p) ** (n - x)


print("%.3f" % sum(b(4, i, 4. / 5) for i in range(3, 5)))
print("%.3f" % sum(b(4, i, 4. / 5) for i in range(0, 2)))
