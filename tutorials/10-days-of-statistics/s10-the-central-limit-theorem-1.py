# Tutorials > 10 Days of Statistics > Day 6: The Central Limit Theorem I
# Basic problems on the Central Limit Theorem.
#
# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-1/problem
# challenge id: 21224
#

import math

def Φ(x, µ, σ):
    """ Cumulative Probability """
    return 1 / 2 * (1 + math.erf((x - µ) / σ / math.sqrt(2)))

capacity = float(input())       # 9800  maximum load
n = int(input())                # 49    number of boxes
µ = float(input())              # 205   mean
σ = float(input())              # 15    standard deviation

p = Φ(capacity, n * µ, math.sqrt(n) * σ)

print("{:.4f}".format(p))
