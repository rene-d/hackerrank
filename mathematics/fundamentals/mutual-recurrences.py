# Mathematics > Fundamentals > Mutual Recurrences
# Compute terms in a mutual recurrence.
#
# https://www.hackerrank.com/challenges/mutual-recurrences/problem
# https://www.hackerrank.com/contests/infinitum14/challenges/mutual-recurrences
# challenge id: 15898
#

import sys

MOD = 1000000000

#------------------------------------------------------------------------------

a, b, c, d, e, f, g, h = 0, 0, 0, 0, 0, 0, 0, 0
cache_x = None
cache_y = None


def x(n):
    if n < 0:
        return 1
    v =  cache_x[n]
    if v == 0:
        v = x(n - a) + y(n - b) + y(n - c) + n * d ** n
        cache_x[n] = v
    return v


def y(n):
    if n < 0:
        return 1
    v = cache_y[n]
    if v == 0:
        v = y(n - e) + x(n - f) + x(n - g) + n * h ** n
        cache_y[n] = v
    return v

#------------------------------------------------------------------------------

class Matrice:
    def __init__(self, n, v=None):
        self.n = n
        self.v = [0] * (n * n)
        if v is not None:
            if isinstance(v, int) and v == 1:
                for i in range(n):
                    self.v[i + n * i] = 1
            elif isinstance(v, list) and len(v) == n * n:
                self.v = v
            else:
                raise ValueError

    def __setitem__(self, xy, v):
        self.v[xy[0] + self.n * xy[1]] = v

    def __getitem__(self, xy):
        return self.v[xy[0] + self.n * xy[1]]

    def __call__(self, x, y):
        return self.v[x + self.n * y]

    def __str__(self):
        n = self.n
        m = [max(len(str(self.v[x + n * y])) for y in range(n))
             for x in range(n)]
        s = ''
        for i in range(0, n * n, n):
            s += '[' if i == 0 else ' '
            s += '  '.join(str(self.v[j]).rjust(m[j - i]) for j in range(i, i + n))
            s += ']' if i == n * n - n else '\n'
        return s

    def __imod__(self, m):
        """ A %= m """
        for i in range(self.n * self.n):
            self.v[i] %= m
        return self

    def tr(self):
        n = self.n
        Ap = Matrice(n)
        for x in range(n):
            for y in range(n):
                Ap.v[x + n * y] = self.v[y + n * x]
        return Ap


class Vecteur:
    def __init__(self, n, v=None):
        self.n = n
        self.v = [0] * n
        if v is not None:
            if isinstance(v, list) and len(v) == n:
                self.v = v
            else:
                raise ValueError

    def __setitem__(self, x, v):
        self.v[x] = v

    def __getitem__(self, x):
        return self.v[x]

    def __call__(self, x):
        return self.v[x]

    def __str__(self):
        n = self.n
        s = '[' + ' '.join(map(str, self.v)) + ']'
        return s

    def __imod__(self, m):
        """ V %= m """
        for i in range(self.n):
            self.v[i] %= m
        return self


def multm(A, B):
    """ produit matriciel: A * B """
    assert A.n == B.n
    n = A.n
    r = Matrice(n)
    for x in range(n):
        for y in range(n):
            r[(x, y)] = sum(A(i, y) * B(x, i) for i in range(n)) % MOD
    return r


def multv(A, V):
    """ produit matrice/vecteur: A * V """
    assert A.n == V.n
    n = A.n
    r = Vecteur(n)
    for y in range(n):
        r[y] = sum(A(i, y) * V(i) for i in range(n)) % MOD
    return r


def power(M, k):
    """ fast exponentiation M^k """
    P = Matrice(M.n, 1)
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


#------------------------------------------------------------------------------

def fibonacci_easy(a, b, n):
    A = Matrice(2, [1, 1, 1, 0])
    An = power(A, n)
    F0 = Vecteur(2, [b, a])
    Fn = multv(An, F0)
    print(Fn[1])


def solve(a, b, c, d, e, f, g, h, n):

    A = Matrice(24)

    A[(     a - 1, 0)] += 1         # x(n) =  x(n - a)
    A[(10 + b - 1, 0)] += 1         #                  + y(n - b)
    A[(10 + c - 1, 0)] += 1         #                             + y(n - c)
    A[(        22, 0)] += 1         #                                        + n * d ** n

    A[(10 + e - 1, 10)] += 1        # y(n) = y(n - e)
    A[(     f - 1, 10)] += 1        #                 + x(n - f)
    A[(     g - 1, 10)] += 1        #                             + x(n - g)
    A[(        20, 10)] += 1        #                                        + n * h ** n

    for i in range(1, 10):
        A[(i - 1, i)] += 1
        A[(10 + i - 1, 10 + i)] += 1

    A[(20, 20)] = h
    A[(21, 20)] = h
    A[(21, 21)] = h

    A[(22, 22)] = d
    A[(23, 22)] = d
    A[(23, 23)] = d

    V = Vecteur(24, [1] * 24)
    V[20] = 0
    V[22] = 0

    # print(A, file=sys.stderr)

    A = power(A, n + 1)
    r = multv(A, V)
    print(r[0], r[10])


if __name__ == '__main__':
    for _ in range(int(input())):
        a, b, c, d, e, f, g, h, n = map(int, input().split())

        """ naif
        cache_x = [0] * (n + 1)
        cache_y = [0] * (n + 1)
        print(x(n) % MOD, y(n) % MOD)
        """

        solve(a, b, c, d, e, f, g, h, n)
