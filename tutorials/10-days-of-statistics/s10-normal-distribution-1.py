# Tutorials > 10 Days of Statistics > Day 5: Normal Distribution I
# Problems based on basic statistical distributions.
#
# https://www.hackerrank.com/challenges/s10-normal-distribution-1/problem
# challenge id: 21229
#

import math

π = math.pi


def N(x, µ, σ):
    """ Normal Distribution """
    return math.exp(- (x - µ) ** 2 / (2 * σ * σ)) / (σ * math.sqrt(2 * π))


def Φ(x, µ, σ):
    """ Cumulative Probability """
    return 1 / 2 * (1 + math.erf((x - µ) / σ / math.sqrt(2)))


µ = 20
σ = 2

print("{:.3f}".format(Φ(19.5, µ, σ)))

print("{:.3f}".format(Φ(22, µ, σ) - Φ(20, µ, σ)))