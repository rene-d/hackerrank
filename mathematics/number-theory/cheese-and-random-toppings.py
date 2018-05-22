# Mathematics > Number Theory > Cheese and Random Toppings
# How many ways are there to choose exactly R toppings from N toppings?
#
# https://www.hackerrank.com/challenges/cheese-and-random-toppings/problem
# https://www.hackerrank.com/contests/infinitum10/challenges/cheese-and-random-toppings
# challenge id: 6061
#


# solution
#   1. décomposer M en facteurs premiers : {pi}
#   2. calculer ai = C(n,r) % pi avec le théorème de Lucas   https://fr.wikipedia.org/wiki/Théorème_de_Lucas
#       on a: ai = C(n,r) % pi
#   3. utiliser Bachet-Bezout puis le théorème des restes chinois   https://fr.wikipedia.org/wiki/Théorème_des_restes_chinois
#       x ≡ ai (mod pi)
#       x = Σ ai∙(m / pi)
#   4. x est notre solution


import math


def nCk(n, k):
    """ coefficient binomial (ou nombre de combinaisons) """
    if n < k:
        return 0
    return math.factorial(n) // math.factorial(k) // math.factorial(n - k)


def decompose(n):
    """ décomposition d'un nombre en facteurs premiers """
    facteurs = {}
    i = 2
    while i * i <= n:
        while n % i == 0:
            n = n // i
            facteurs[i] = facteurs.get(i, 0) + 1
        if i >= 3:
            i += 2
        else:
            i += 1
    if n > 1:
        facteurs[n] = facteurs.get(n, 0) + 1
    return facteurs


def base(x, b):
    """ calcule les chiffres de en base b """
    d = []
    while x != 0:
        x, r = divmod(x, b)
        d.append(r)
    return d


def lucas(m, n, p):
    """ théorème de Lucas """
    M = base(m, p)
    N = base(n, p)

    C = 1
    # nota: si m et n ont un nombre de chiffres différents, pas grave
    # puisque nCr(x,0)=1 : le produit ne change donc pas
    for mi, ni in zip(M, N):
        C *= nCk(mi, ni) % p
        C %= p
    return C


def egcd(b, a):
    """ algortihme d'Euclide étendu: (g, x, y) tel que ax + by = g = gcd(a, b) """
    x0, x1, y0, y1 = 1, 0, 0, 1
    while a != 0:
        q, b, a = b // a, a, b % a
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return b, x0, y0


def nCk_mod(n, r, m):
    """ calcule C(n, r) % m avec m square-free """

    if m < 2:
        return 0

    p = decompose(m)
    assert set(p.values()) == set({1})
    p = list(p.keys())

    x = 0
    for pi in p:
        ai = lucas(n, r, pi)

        _, _, v = egcd(pi, m // pi)
        x += ai * v * (m // pi)

    return x % m


# assert nCk_mod(20, 6, 210) == 120

for _ in range(int(input())):
    n, r, m = map(int, input().split())
    print(nCk_mod(n, r, m))
