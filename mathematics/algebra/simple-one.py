# Mathematics > Algebra > Simple One
# Calculate the tan function of a given equation.
#
# https://www.hackerrank.com/challenges/simple-one/problem
# https://www.hackerrank.com/contests/infinitum14/challenges/simple-one
# challenge id: 9549
#

from fractions import Fraction


MOD = 1000000007

def egcd(b, a):
    """ algortihme d'Euclide étendu: (g, x, y) tel que ax + by = g = gcd(a, b) """
    # https://fr.wikipedia.org/wiki/Algorithme_d%27Euclide_étendu
    x0, x1, y0, y1 = 1, 0, 0, 1
    while a != 0:
        q, b, a = b // a, a, b % a
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return b, x0, y0


def modinv(a, m):
    """ modular inverse avec Bachet-Bézout """
    # https://fr.wikipedia.org/wiki/Théorème_de_Bachet-Bézout
    _, x, _ = egcd(a, m)
    return x % m


def ntan(a, k):
    # tan(a+b) = (tan(a) + tan(b)) / (1 - tan(a) * tan(b))
    # tan(2a) = 2 * tan(a) / (1 - tan(a)^2)

    b = Fraction(0)

    if k == 0:
        return b
    if k == 1:
        return a

    while k != 0:
        if k % 2 == 1:
            b = (a + b) / (1 - a * b)
            b = Fraction(b.numerator % MOD, b.denominator % MOD)

        a = 2 * a / (1 - a * a)
        a = Fraction(a.numerator % MOD, a.denominator % MOD)

        k //= 2
    return b


for _ in range(int(input())):
    p, q, n = map(int, input().split())
    a = ntan(Fraction(p, q), n)
    print((a.numerator * modinv(a.denominator, MOD)) % MOD)
