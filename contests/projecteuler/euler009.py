# ProjectEuler+ > Project Euler #9: Special Pythagorean triplet
# A what triplet, you say?
#
# https://www.hackerrank.com/contests/projecteuler/challenges/euler009
# challenge id: 2635
#

from math import sqrt

ok = [-1] * 3001

for a in range(1, 3001):
    for b in range(a + 1, 3001):
        c2 = a * a + b * b
        c = int(sqrt(c2) + 0.5)
        p = a + b + c
        if p > 3000:
            break
        if c * c == c2:
            ok[p] = a * b * c


for _ in range(int(input())):
    n = int(input())
    print(ok[n])
