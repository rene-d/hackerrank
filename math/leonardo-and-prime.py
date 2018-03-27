# Leonardo's Prime Factors
# Find the maximum number of prime factors for any number in the inclusive range from 1 to n.
#
# https://www.hackerrank.com/challenges/leonardo-and-prime/problem
#

class bitset:
    """
    Implémentation d'un bitset à stockage optimisé
    """

    def __init__(self, taille):
        self.taille = taille
        self.bits = bytearray((taille + 7) // 8)

    def set(self, pos, val):
        """ poitionne le bit `pos` à `val` """
        assert pos >= 0 and pos < self.taille
        if val is True:
            self.bits[pos // 8] = self.bits[pos // 8] | (1 << (pos % 8))
        else:
            self.bits[pos // 8] = self.bits[pos // 8] & ~(1 << (pos % 8))

    def is_set(self, pos):
        """ lit l'état du bit `pos` """
        assert pos >= 0 and pos < self.taille
        return (self.bits[pos // 8] & (1 << (pos % 8))) != 0

    def __getitem__(self, key):
        return self.is_set(key)

    def __setitem__(self, key, value):
        return self.set(key, value)


class Crible:
    """ Crible d'Eratosthène optimisé """

    def __init__(self, n_max):
        self.n_max = n_max

        self.maximum = n = (n_max - 3) // 2 + 1
        self.crible = crible = bitset(n)
        self._premiers = None
        self._phi = None

        i = 0
        while i < n:
            while i < n:
                if not crible.is_set(i):
                    break
                i += 1

            k = 3
            while True:
                j = k * i + 3 * (k - 1) // 2
                if j >= n:
                    break
                crible.set(j, True)
                k += 2

            i += 1

    def liste(self):
        if self._premiers is None:
            premiers = [2]
            for i in range(1, self.maximum + 1):
                if not self.crible.is_set(i - 1):
                    premiers.append(2 * i + 1)
            self._premiers = premiers
        return self._premiers


primes = Crible(1000).liste()

for _ in range(int(input())):
    n = int(input())

    r = 1
    nb = 0
    for p in primes:
        if p * r > n:
            break
        r *= p
        nb += 1
    print(nb)