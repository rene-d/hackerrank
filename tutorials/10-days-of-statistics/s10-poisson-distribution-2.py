# Tutorials > 10 Days of Statistics > Day 5: Poisson Distribution II
# Basic problem on Poisson Distribution.
#
# https://www.hackerrank.com/challenges/s10-poisson-distribution-2/problem
# challenge id: 21228
#

import math

def poisson(λ, k):
    return λ ** k * math.e ** (-λ) / math.factorial(k)

def E(λ):
    return λ + λ ** 2

λ1, λ2 = map(float, input().split())

print("{:.3f}".format(160 + 40 * E(λ1)))
print("{:.3f}".format(128 + 40 * E(λ2)))
