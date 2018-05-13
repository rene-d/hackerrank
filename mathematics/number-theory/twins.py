# Mathematics > Number Theory > Twins
# How many pairs of twins can you find?
#
# https://www.hackerrank.com/challenges/twins/problem
# https://www.hackerrank.com/contests/w26/challenges/twins
#


# algo sans crible segemnté, peu efficace mais suffisant s'il est lancé en pypy3
# timeout en python3 :(


class bitset:
    """
    Implémentation d'un bitset à stockage optimisé
    """

    def __init__(self, taille):
        self.bits = bytearray((taille + 7) // 8)

    def set(self, pos):
        """ poitionne le bit `pos` à `val` """
        self.bits[pos // 8] |= (1 << (pos % 8))

    def is_unset(self, pos):
        """ lit l'état du bit `pos` """
        return (self.bits[pos // 8] & (1 << (pos % 8))) == 0


class Crible:
    """ Crible d'Eratosthène optimisé """

    def __init__(self, n_max):
        self.n_max = n_max

        self.maximum = n = (n_max - 3) // 2 + 1
        self.crible = crible = bitset(n)
        self._premiers = None

        i = 0
        while i < n:
            while i < n:
                if crible.is_unset(i):
                    break
                i += 1

            k = 3
            while True:
                j = k * i + 3 * (k - 1) // 2
                if j >= n:
                    break
                crible.set(j)
                k += 2

            i += 1

        premiers = [2]
        for i in range(1, self.maximum + 1):
            if self.crible.is_unset(i - 1):
                premiers.append(2 * i + 1)
        self._premiers = premiers


    def liste(self):
        return self._premiers


n, m = map(int, input().split())

primes = Crible(int(m ** 0.5) + 2).liste()[1:]
count = 0
last_prime = -3
n = max((n // 2) * 2 + 1, 3)

for i in range(n, m + 1, 2):
    is_prime = True
    for p in primes:
        if i == p:
            break
        if i % p == 0:
            is_prime = False
            break
    if not is_prime:
        continue
    if i - last_prime == 2:
        count += 1
    last_prime = i

print(count)
