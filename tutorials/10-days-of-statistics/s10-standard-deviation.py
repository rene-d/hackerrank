# Tutorials > 10 Days of Statistics > Day 1: Standard Deviation
# Compute the standard deviation
#
# https://www.hackerrank.com/challenges/s10-standard-deviation/problem
# challenge id: 21237
#

n = int(input())
x = list(map(int, input().split()))

Σ = sum

# moyenne (mean)
µ = Σ(x) / n

# écart-type (standard deviation)
𝜎 = (Σ((i - µ) ** 2 for i in x) / n) ** 0.5

print("{:.1f}".format(𝜎))
