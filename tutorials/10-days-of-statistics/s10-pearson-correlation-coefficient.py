# Tutorials > 10 Days of Statistics > Day 7: Pearson Correlation Coefficient I
# Computing Pearson correlation coefficient.
#
# https://www.hackerrank.com/challenges/s10-pearson-correlation-coefficient/problem
# challenge id: 21178
#

# Pearson: measure of the linear correlation between two variables X and Y

def pearson(n, X, Y):
    mx = sum(X) / n                 # moyenne de la série X
    my = sum(Y) / n

    sx = 0
    sy = 0
    p = 0

    for x, y in zip(X, Y):
        sx += (x - mx) ** 2         # calcule l'écart-type de X
        sy += (y - my) ** 2         # calcule l'écart-type de Y
        p += (x - mx) * (y - my)    # calcule la covariance de (X,Y)

    sx = (sx / n) ** 0.5
    sy = (sy / n) ** 0.5

    p = p / (n * sx * sy)
    return p


n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

print('{:.3f}'.format(pearson(n, X, Y)))
