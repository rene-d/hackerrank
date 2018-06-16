# Tutorials > 10 Days of Statistics > Day 6: The Central Limit Theorem III
# Basic problems on the Central Limit Theorem.
#
# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-3/problem
# challenge id: 21226
#

import math

n = int(input())                # 100       sample size
µ = float(input())              # 500       mean
σ = float(input())              # 80        standard deviation
percent = float(input())        # 0.95      distribution percentage we want to cover
z = float(input())              # 1.96      z-score : Φ(1.96) - Φ(-1.96) ≈ 95%

e = z * σ / math.sqrt(n)
print('{:2f}'.format(µ - e))
print('{:2f}'.format(µ + e))
