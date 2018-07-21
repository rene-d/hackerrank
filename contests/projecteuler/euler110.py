# ProjectEuler+ > Project Euler #110: Diophantine reciprocals II
# euler 110
#
# https://www.hackerrank.com/contests/projecteuler/challenges/euler110
# challenge id: 2736
#

# cf. https://github.com/rene-d/math/blob/master/projecteuler/p110.py

from math import log, ceil

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
          47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
          107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163,
          167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227,
          229, 233, 239, 241, 251, 257, 263, 269, 271]


def hcs(nf, maxe, px):
    if nf <= 1:
        return 1

    if nf <= 3:
        return primes[px]

    ppow = primes[px]

    best = ppow * hcs((nf + 2) // 3, 1, px + 1)
    for e in range(2, maxe + 1):
        ppow *= primes[px]
        if ppow > best:
            break
        test = ppow * hcs((nf + 2 * e) // (2 * e + 1), e, px + 1)
        if test < best:
            best = test

    return best


N = int(input())
assert ceil(log(N * 2) / log(3)) < len(primes)
print(hcs(N * 2 - 1, 10, 0))
