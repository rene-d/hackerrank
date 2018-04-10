# Restaurant
# Help Martha with her interview at Subway
#
# https://www.hackerrank.com/challenges/restaurant/problem
#

from math import gcd

for _ in range(int(input())):
    l, b = map(int, input().split())

    if l == b:
        print(1)
    else:
        print((l * b) // gcd(l, b) ** 2)
