# Mathematics > Number Theory > Fibonacci GCD
# Find gcd for n fibonacci numbers.
#
# https://www.hackerrank.com/challenges/fibonacci-gcd/problem
# https://www.hackerrank.com/contests/infinitum9/challenges/fibonacci-gcd
# challenge id: 4503
#

from math import gcd


MOD = 1000000007


def multm(A, B):
    """ produit matriciel: A * B """
    a00, a10, a01, a11 = A
    b00, b10, b01, b11 = B
    return [(a00 * b00 + a10 * b01) % MOD, (a00 * b10 + a10 * b11) % MOD,
            (a01 * b00 + a11 * b01) % MOD, (a01 * b10 + a11 * b11) % MOD]


def multv(A, V):
    """ produit matrice/vecteur: A * V """
    a00, a10, a01, a11 = A
    b0, b1 = V
    return [(a00 * b0 + a10 * b1) % MOD,
            (a01 * b0 + a11 * b1) % MOD]


def power(M, k):
    """ fast exponentiation M^k """
    P = [1, 0,
         0, 1]

    if k == 0:
        return P
    if k == 1:
        return M

    while k != 0:
        if k % 2 == 1:
            P = multm(P, M)
        M = multm(M, M)
        k //= 2
    return P


# on utilise la propriété suivante:
# gcd(F(a), F(b)) = F(gcd(a, b))

# calcul du gcd(aᵢ)
g = 0
n = int(input())
for i in range(n):
    g = gcd(g, int(input()))

# calcul de F(g) (cf. https://www.hackerrank.com/challenges/fibonacci-finding-easy)
# http://en.wikipedia.org/wiki/Fibonacci_number#Matrix_form
# Fn = A^n * F0
# avec Fn[f(n+1) f(n))
# et A = [[1 1][1 0]]
A = [1, 1, 1, 0]
An = power(A, g)
F0 = [1, 0]
Fn = multv(An, F0)
print(Fn[1])
