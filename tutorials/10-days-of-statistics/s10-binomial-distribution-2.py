# Tutorials > 10 Days of Statistics > Day 4: Binomial Distribution II
# Problems based on basic statistical distributions.
#
# https://www.hackerrank.com/challenges/s10-binomial-distribution-2/problem
# challenge id: 21232
#

from math import factorial

# b(x,n,p) = C(n,p) * p^x * (1-p)^(n-x)

# x: number of successes
# n: total number of trials
# p: probability of success of 1 trial

def b(n, x, p):
    return factorial(n) // factorial(n - x) // factorial(x) * (p ** x) * (1 - p) ** (n - x)

p, n = map(int, input().split())

p = p / 100     # proba qu'un piston soit ko

r = b(n, 0, p) + b(n, 1, p) + b(n, 2, p)        # 0 ou 1 ou 2 rejets
print("%.3f" % r)

r = sum(b(n, i, p) for i in range(2, n + 1))    # 2 à 12 rejets
print("%.3f" % r)
