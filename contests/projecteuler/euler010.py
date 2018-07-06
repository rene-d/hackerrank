# ProjectEuler+ > Project Euler #10: Summation of primes
# More prime number fun.
#
# https://www.hackerrank.com/contests/projecteuler/challenges/euler010
# challenge id: 2636
#

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


N = 1000000
sieve = Crible(N)
primes = sieve.liste()

# precompute the answers
psum = [0] * N
i = 0
k = 0
for p in primes:
    i += 1
    while i < p:
        psum[i] = k
        i += 1
    k += p
    psum[i] = k
while i < N:
    psum[i] = k
    i += 1

for _ in range(int(input())):
    n = int(input())
    print(psum[n])
