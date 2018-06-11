# Tutorials > 10 Days of Statistics > Day 2: Compound Event Probability
#
#
# https://www.hackerrank.com/challenges/s10-mcq-3/problem
# challenge id: 21609
#

from fractions import Fraction

n, t = 0, 0
for i in range(1, 8):
    for j in range(1, 10):
        for k in range(1, 9):
            red, black = 0, 0

            if i <= 4:
                red += 1
            else:
                black += 1

            if j <= 5:
                red += 1
            else:
                black += 1

            if k <= 4:
                red += 1
            else:
                black += 1

            if red == 2 and black == 1:
                n += 1
            t += 1

print(Fraction(n, t))
