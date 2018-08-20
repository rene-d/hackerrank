# Mathematics > Number Theory > Devu Vs Police
# Help Devu escape from police
#
# https://www.hackerrank.com/challenges/devu-police/problem
# https://www.hackerrank.com/contests/infinitum-mar14/challenges/devu-police
# challenge id: 1050
#


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


def solve(n1, k1, n2, k2, n):

    if k1 == 0 or (n2 == 0 and k2 != 0):    # exponent is 0
        return pow(n1, 0, n)
    if n2 == 1 or k2 == 0:                  # n2^k2 = 1
        return pow(n1, k1, n)
    if n1 == 0 or n1 % n == 0:              # exponent is not 0
        return 0
    if k2 == 1:                             # other trivial case
        return pow(n1, k1 * n2, n)

    # Euler's theorem
    phi = EulerPhi(n)
    e = pow(n2, k2, phi) + phi
    return pow(pow(n1, k1, n), e, n)


t = int(input())
for _ in range(t):
    n1, k1, n2, k2, n = map(int, input().split())
    print(solve(n1, k1, n2, k2, n))
