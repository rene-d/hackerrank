# Mathematics > Number Theory > Little Panda Power
# Compute A^B mod X
#
# https://www.hackerrank.com/challenges/littlepandapower/problem
#


def egcd(b, a):
    """ return a triple (g, x, y), such that ax + by = g = gcd(a, b) """
    x0, x1, y0, y1 = 1, 0, 0, 1
    while a != 0:
        q, b, a = b // a, a, b % a
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return b, x0, y0


def mulinv(b, m):
    """ modular multiplicative inverse """
    g, x, _ = egcd(b, m)
    if g == 1:
        return x % m


def powmod(x, k, m):
    """ fast exponentiation x^k % m """
    if k < 0:
        x = mulinv(x, m)
        k = -k
    p = 1
    if k == 0:
        return p
    if k == 1:
        return x
    while k != 0:
        if k % 2 == 1:
            p = (p * x) % m
        x = (x * x) % m
        k //= 2
    return p


for _ in range(int(input())):
    a, b, m = map(int, input().split())
    print(powmod(a, b, m))
