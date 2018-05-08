# Ad Infinitum18 > Pythagorean Triple
# Find the Pythagorean triple for the given side a.
#
# https://www.hackerrank.com/contests/infinitum18/challenges/pythagorean-triple
#


def pythagoreanTriple(a):
    if a == 4:
        # cas spécial pour la récursion lorsque a est pair
        return 4, 3, 5
    if a % 2 == 1:
        # a impair: on peut utiliser les égalités données dans l'énoncé
        k = (a - 1) // 2
        m = k + 1
        n = k
        assert a == m * m - n * n
        b = 2 * m * n
        c = m * m + n * n
        return (a, b, c)
    else:
        # a pair, il faut "simplifier" jusqu'à 4 au max (sinon on va trouver b=0 et c=a)
        e = 1
        while a % 2 == 0 and a > 4:
            e *= 2
            a //= 2
        return map(lambda x: x * e, pythagoreanTriple(a))


a = int(input().strip())
a, b, c = pythagoreanTriple(a)

print(a, b, c)
