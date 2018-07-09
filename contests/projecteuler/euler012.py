# ProjectEuler+ > Project Euler #12: Highly divisible triangular number
# Find smallest triangular number with atleast N divisors.
#
# https://www.hackerrank.com/contests/projecteuler/challenges/euler012
# challenge id: 2638
#


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


def solve(n):
    i = 2
    a = decompose(i)
    while True:
        i += 1
        b = decompose(i)

        # fusionne les deux décompositions
        for k, v in b.items():
            a[k] = a.get(k, 0) + v

        # calcule le nombre de diviseurs
        f = 1
        for k, v in a.items():
            if k == 2:
                f *= v
            else:
                f *= v + 1

        # a-t-on un résultat ?
        if f > n:
            return (i * (i - 1) // 2)

        a = b


for _ in range(int(input())):
    n = int(input())
    print(solve(n))
