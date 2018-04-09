# Matrix Tracing
# How many ways can you trace a given matrix? - 30 Points
#
# https://www.hackerrank.com/challenges/matrix-tracing/problem
#

MOD = 1000000007

def fact(n):
    """ calcule n! mod MOD """
    f = 1
    for i in range(2, n + 1):
        f = (f * i) % MOD
    return f

def pow(a, b):
    """ calcule a^b mod MOD """
    a %= MOD
    # exponentiation rapide
    p = 1
    while b > 0:
        if b % 2 == 1:
            p = (p * a) % MOD
        a = (a * a) % MOD
        b //= 2
    return p

for _ in range(int(input())):
    m, n = map(int, input().split())

    # la solution est C(m+n-2, m-1) ou C(m+n-2, n-1)
    # soit (m+n-2)! / (m-1)! / (n-1)!

    # compte tenu des valeurs de m et n, le calcul direct est impossible

    # on va utiliser le petit théorème de Fermat:
    # a^(p-1) = 1 mod p         si p est premier et gcd(a,p)=1
    # => a^(p-2) = a^(-1) mod p
    # => a^(-1) = a^(p-2) mod p

    # le résultat modulo MOD est donc:
    # (m+n-2)! * [ (m-1)! * (n-1)!) ^ (MOD-2) ]

    r = fact(n + m - 2) * pow(fact(n - 1) * fact(m - 1), MOD - 2)

    print(r % MOD)
