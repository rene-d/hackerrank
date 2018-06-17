# Tutorials > 10 Days of Statistics > Day 2: More Dice
# Calculate the probability that two dice will roll two unique values having a sum of 6.
#
# https://www.hackerrank.com/challenges/s10-mcq-2/problem
# challenge id: 21608
#

from fractions import Fraction

n = 0
for i in range(1, 7):
    for j in range(1, 7):
        if i + j == 6 and i != j:
            n += 1

print(Fraction(n, 6 * 6))