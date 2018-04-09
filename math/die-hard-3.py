# Die Hard 3
# Help Bruce and Samuel save the city by solving their puzzle
#
# https://www.hackerrank.com/challenges/die-hard-3/problem
#

from math import gcd

for _ in range(int(input())):
    a, b, c = map(int, input().split())

    print("YES" if c <= max(a, b) and c % gcd(a, b) == 0 else "NO")
