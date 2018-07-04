# ProjectEuler+ > Project Euler #7: 10001st prime
# Finding the Nth prime.
#
# https://www.hackerrank.com/contests/projecteuler/challenges/euler007
# challenge id: 2633
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


c = Crible(104743 + 1)      # 10001e nombre premier
p = c.liste()

for _ in range(int(input())):
    n = int(input())
    print(p[n - 1])
