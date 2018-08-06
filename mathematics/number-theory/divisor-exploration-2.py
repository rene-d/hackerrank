# Mathematics > Number Theory > Divisor Exploration II
# Find the product of a sequence and then calculate the summation of its divisors.
#
# https://www.hackerrank.com/challenges/divisor-exploration-2/problem
# https://www.hackerrank.com/contests/infinitum17/challenges/divisor-exploration-2
# challenge id: 12002
#

# à exécuter en Pypy3, trop lent sinon...

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

    def liste(self):
        if self._premiers is None:
            premiers = [2]
            for i in range(1, self.maximum + 1):
                if not self.crible[i - 1]:
                    premiers.append(2 * i + 1)
            self._premiers = premiers
        return self._premiers


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
    _, x, _ = egcd(a, m)
    return x % m


# précalcul des 10^5 premiers nombres premiers
crible = Crible(1299709 + 1)    # le 100000e nombre premier
primes = crible.liste()

MOD = 1000000007


# la "vraie" formule, mais il faut calculer en arithmétique modulaire
def sigma_1(p, a):
    return (pow(p, a + 1) - 1) // (p - 1)

def F(p, a):
    return (p * sigma_1(p, a) - (a + 1)) // (p - 1)


# numérateur et dénominateur de F()
def F_num(p, a):
    return (pow(p, a + 2, MOD) - (p + (p - 1) * (a + 1)) % MOD) % MOD

def F_den(p):
    return (p - 1) ** 2


def solve(m, a):
    n = d = 1
    for i, p in enumerate(primes[:m], 1):
        n *= F_num(p, a + i)
        d *= F_den(p)

        n %= MOD
        d %= MOD

    r = n * modinv(d, MOD)
    r %= MOD
    print(r)


for _ in range(int(input())):
    m, a = map(int, input().split())
    solve(m, a)