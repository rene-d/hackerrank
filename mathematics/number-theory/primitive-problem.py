# Mathematics > Number Theory > Primitive Problem
# Find the primitive roots of a prime number.
#
# https://www.hackerrank.com/challenges/primitive-problem/problem
# https://www.hackerrank.com/contests/infinitum17/challenges/primitive-problem
#

# https://math.stackexchange.com/questions/124408/finding-a-primitive-root-of-a-prime-number


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


def EulerPhi(n):
    """ calcul de l'Indicatrice d'Euler φ(n) ou totient(n) """
    phi = n
    i = 2
    while i * i <= n:
        if n % i == 0:
            phi -= phi // i
        while n % i == 0:
            n = n // i
        if i != 2:
            i += 2
        else:
            i += 1
    if n > 1:
        phi -= phi // n
    return phi


def powmod(x, k, MOD):
    """ fast exponentiation x^k % MOD """
    p = 1
    if k == 0:
        return p
    if k == 1:
        return x
    while k != 0:
        if k % 2 == 1:
            p = (p * x) % MOD
        x = (x * x) % MOD
        k //= 2
    return p


def primitive_roots(p):
    s = EulerPhi(p)
    f = decompose(s)

    for a in range(2, p):
        ok = all(powmod(a, s // pi, p) != 1 for pi in f.keys())
        if ok:
            break

    if len(decompose(p)) == 1:
        return a, EulerPhi(p - 1)

    # nota: ce cas n'arrive dans les testcases
    return a, "?"


print(*primitive_roots(int(input())))
