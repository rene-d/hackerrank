# Tutorials > 10 Days of Statistics > Day 2: Basic Probability
#  Calculate the probability that two dice will have a maximum sum of 9.
#
# https://www.hackerrank.com/challenges/s10-mcq-1/problem
# challenge id: 21607
#

from fractions import Fraction

n = 0
for i in range(1, 7):
    for j in range(1, 7):
        if i + j <= 9:
            n += 1

print(Fraction(n, 6 * 6))
