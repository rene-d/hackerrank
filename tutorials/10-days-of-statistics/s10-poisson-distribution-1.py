# Tutorials > 10 Days of Statistics > Day 5: Poisson Distribution I
# Basic problem on Poisson Distribution.
#
# https://www.hackerrank.com/challenges/s10-poisson-distribution-1/problem
# challenge id: 21227
#

import math

def poisson(λ, k):
    return λ ** k * math.e ** (-λ) / math.factorial(k)

λ = float(input())
k = int(input())

print("{:.3f}".format(poisson(λ, k)))
