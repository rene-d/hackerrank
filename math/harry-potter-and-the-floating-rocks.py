# Sumar and the Floating Rocks
# Count the number of integral rocks between Harry and Hermoine
#
# https://www.hackerrank.com/challenges/harry-potter-and-the-floating-rocks/problem
#

from math import gcd

for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())

    # y = A* x + B
    # y1 = A * x1 + B
    # y2 = A * x2 + B
    # A = (y2-y1) / (x2-x1)

    f = gcd(y2 - y1, x2 - x1) - 1
    print(f)
