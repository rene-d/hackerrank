# Tutorials > 10 Days of Statistics > Day 7: Spearman's Rank Correlation Coefficient
# Computing Spearman's rank correlation coefficient.
#
# https://www.hackerrank.com/challenges/s10-spearman-rank-correlation-coefficient/problem
# challenge id: 21707
#

def spearman(n, X, Y):
    """ calcul du coefficient de Spearman pour des échantillons avec des valeurs uniques """

    def rank(X):
        r = [0] * len(X)
        xs = sorted((x, i) for i, x in enumerate(X))
        for j, xi in enumerate(xs):
            r[xi[1]] = j + 1
        return r

    # somme de la différence des ranks au carré
    r = sum((rx - ry) ** 2 for rx, ry in zip(rank(X), rank(Y)))
    r = 1 - 6 * r / n / (n ** 2 - 1)

    return r


n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

c = spearman(n, X, Y)
print('{:.3f}'.format(c))
