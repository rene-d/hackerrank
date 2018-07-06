# Mathematics > Number Theory > Prime Sum
# Represent a number as sum of primes.
#
# https://www.hackerrank.com/challenges/prime-sum/problem
# https://www.hackerrank.com/contests/w3/challenges/prime-sum
# challenge id: 2310
#

from random import randrange


def miller_rabin(n, k=10):
    if n == 2:
        return True
    if n & 1 == 0:
        return False

    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1:
            return True
        for i in range(s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1

    s = 0
    d = n - 1

    while d % 2 == 0:
        d >>= 1
        s += 1

    for i in range(k):
        a = randrange(2, n - 1)
        if not check(a, s, d, n):
            return False

    return True


class Crible:
    """ Crible d'Eratosthène optimisé """

    def __init__(self, n_max):
        self.n_max = n_max

        self.maximum = n = (n_max - 3) // 2 + 1
        self.crible = crible = [False] * (n + 1)
        self._premiers = None
        self._phi = None

        i = 0
        while i < n:
            while i < n:
                if not crible[i]:
                    break
                i += 1

            k = 3
            while True:
                j = k * i + 3 * (k - 1) // 2
                if j >= n:
                    break
                crible[j] = True
                k += 2

            i += 1

    def est_premier(self, n):
        if n == 2:
            return True
        elif n % 2 == 0 or n <= 1:
            return False
        else:
            # n est impair et >= 3
            assert n < self.n_max
            return not self.crible[(n - 3) // 2]


N = 1000000
sieve = Crible(N)


def is_prime(n):
    if n < N:
        return sieve.est_premier(n)
    else:
        return miller_rabin(n)


def check(n, k):

    if k == 1:
        # il faut que n soit premier
        print("Yes" if is_prime(n) else "No")

    elif n < 4:
        # aucune solution
        print("No")

    elif k == 2 and n % 2 == 1:
        # n ne peut être la somme que d'un nombre pair et d'un nombre impair
        # et pas la somme de deux nombres impairs.
        # le seul premier pair est 2.
        # donc si n-2 est premier ok, sinon non
        print("Yes" if is_prime(n - 2) else "No")

    elif n % 2 == 0:
        # 2+2+...+2 valeur minimale de la somme,
        # sinon conjecture de Goldbach (on a n > 3 ici)
        print("Yes" if k <= n // 2 else "No")

    else:
        # 3+2+2+...+2 valeur minimale de la somme
        # n-3 est pair, on utilise Goldbach
        print("Yes" if k - 1 <= (n - 3) // 2 else "No")


for _ in range(int(input())):
    n, k = map(int, input().split())
    check(n, k)
