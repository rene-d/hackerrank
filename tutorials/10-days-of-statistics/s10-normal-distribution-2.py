# Tutorials > 10 Days of Statistics > Day 5: Normal Distribution II
# Problems based on basic statistical distributions.
#
# https://www.hackerrank.com/challenges/s10-normal-distribution-2/problem
# challenge id: 21230
#

import math


def N(x, µ, σ):
    """ Normal Distribution """
    π = math.pi
    return math.exp(- (x - µ) ** 2 / (2 * σ * σ)) / (σ * math.sqrt(2 * π))


def Φ(x, µ, σ):
    """ Cumulative Probability """
    return 1 / 2 * (1 + math.erf((x - µ) / σ / math.sqrt(2)))


µ, σ = map(float, input().split())
q1 = float(input())
q2 = float(input())

# percentage of students having grade > q1
print("{:.2f}".format(100 - Φ(q1, µ, σ) * 100))

# percentage of students having grade ≥ q2
print("{:.2f}".format(100 - Φ(q2, µ, σ) * 100))

# percentage of students having grade < q2
print("{:.2f}".format(Φ(q2, µ, σ) * 100))
