# Tutorials > 10 Days of Statistics > Day 8: Least Square Regression Line
# Find the line of best fit.
#
# https://www.hackerrank.com/challenges/s10-least-square-regression-line/problem
# challenge id: 21177
#

def pearson(n, X, Y):
    mx = sum(X) / n                 # moyenne de la série X
    my = sum(Y) / n

    sx = 0.
    sy = 0.
    p = 0.

    for x, y in zip(X, Y):
        sx += (x - mx) ** 2         # calcule l'écart-type de X
        sy += (y - my) ** 2         # calcule l'écart-type de Y
        p += (x - mx) * (y - my)    # calcule la covariance de (X,Y)

    sx = (sx / n) ** 0.5
    sy = (sy / n) ** 0.5

    p = p / (n * sx * sy)

    b = p * sy / sx                 # Y = a + b X
    a = my - b * mx

    return p, a, b


X, Y = [0] * 5, [0] * 5
for i in range(5):
    X[i], Y[i] = map(int, input().split())

_, a, b = pearson(5, X, Y)

print("{:.3f}".format(a + b * 80))
