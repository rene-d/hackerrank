# Tutorials > 10 Days of Statistics > Day 6: The Central Limit Theorem II
# Basic problems on the Central Limit Theorem.
#
# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-2/problem
# challenge id: 21225
#

import math

def Φ(x, µ, σ):
    """ Cumulative Probability """
    return 1 / 2 * (1 + math.erf((x - µ) / σ / math.sqrt(2)))

tickets = int(input())          # 250
students = int(input())         # 100
µ = float(input())              # 2.4   mean
σ = float(input())              # 2.0   standard deviation

p = Φ(tickets, students * µ, math.sqrt(students) * σ)

print("{:.4f}".format(p))
