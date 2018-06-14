# Tutorials > 10 Days of Statistics > Day 4: Binomial Distribution I
# Problems based on basic statistical distributions.
#
# https://www.hackerrank.com/challenges/s10-binomial-distribution-1/problem
# challenge id: 21231
#

from math import factorial

# b(x,n,p) = C(n,p) * p^x * (1-p)^(n-x)

# x: number of successes
# n: total number of trials
# p: probability of success of 1 trial

def b(n, x, p):
    return factorial(n) // factorial(n - x) // factorial(x) * (p ** x) * (1 - p) ** (n - x)


boys, girls = map(float, input().split())

p = boys / (boys + girls)

r = b(6, 3, p) + b(6, 4, p) + b(6, 5, p) + b(6, 6, p)

print("%.3f" % r)
