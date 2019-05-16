# Mathematics > Number Theory > Divisor Exploration
# Find and print the number of divisors for each dataset.
#
# https://www.hackerrank.com/challenges/divisor-exploration/problem
# https://www.hackerrank.com/contests/infinitum16/challenges/divisor-exploration
# challenge id: 11996
#

#!/bin/python3

import os
import sys
# (template_head) ----------------------------------------------------------------------

# p prime
# σ₀(pⁿ) = n+1
# ∑ σ₀(pⁿ) = 1+2+...+(n+1) = (n+1)(n+2)/2 = tri(n+1)
# ∑ σ₀(p₁ⁿ¹ ∙ p₂ⁿ²) = tri(n₁) ∙ tri(n₂)
# ∑ σ₀(∏ pᵢⁿⁱ) = ∏ tri(nᵢ)

# brute force is too long : O(10⁵ ∙ 10⁵)
# precompute P(n) = ∏ tri(i) (i ≤ n) with n ≤ m(max) + a(max) = 2∙10⁵
# answer is P(m+a+1) / P(a+1) = P(m+a+1) * modinv(P(a+1), MOD)

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
    g, x, _ = egcd(a, m)
    assert g == 1
    return x % m


MAX = 100000 + 100000
P = [1] * (MAX + 1)
invP = [0] * (MAX + 1)

for i in range(1, MAX + 1):
    t = i * (i + 1) // 2
    P[i] = (t * P[i - 1]) % MOD
    invP[i] = modinv(P[i], MOD)


# Complete the solve function below.
def solve(m, a):
    """ brute force
    p = 1
    for i in range(a + 2, a + m + 2):
        p *= i * (i + 1) // 2
        p %= MOD
    return p
    """

    return (P[m + a + 1] * invP[a + 1]) % MOD


# (template_tail) ----------------------------------------------------------------------
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    d = int(input())

    for d_itr in range(d):
        ma = input().split()

        m = int(ma[0])

        a = int(ma[1])

        result = solve(m, a)

        fptr.write(str(result) + '\n')

    fptr.close()
