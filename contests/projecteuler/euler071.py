# ProjectEuler+ > Project Euler #71: Ordered fractions
#
# https://www.hackerrank.com/contests/projecteuler/challenges/euler071
# challenge id: 2697
#

from fractions import Fraction as F


def farey_seq(x, limit):
    l, r = F(0), F(1)
    while l.denominator + r.denominator <= limit:
        m = F(l.numerator + r.numerator, l.denominator + r.denominator)
        if m < x:
            l = m
        else:
            r = m
            if r == x:
                break

    if l.denominator + r.denominator <= limit:
        k = 1 + (limit - (l.denominator + r.denominator)) // r.denominator
        l = F(l.numerator + k * r.numerator, l.denominator + k * r.denominator)

    return l


# ProjectEuler problem:
# print(farey_seq(F(3, 7), 1000000).numerator)

for _ in range(int(input())):
    a, b, n = map(int, input().split())
    r = farey_seq(F(a, b), n)
    print(r.numerator, r.denominator)
