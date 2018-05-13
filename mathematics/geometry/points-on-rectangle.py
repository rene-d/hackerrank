# Mathematics > Geometry > Points on a Rectangle
#  Determine if a set of points coincides with the edges of a non-degenerate rectangle.
#
# https://www.hackerrank.com/challenges/points-on-rectangle/problem
# https://www.hackerrank.com/contests/101hack42/challenges/points-on-rectangle
#

# le rectangle a ses côtés parralèles aux axes, ça simplifie grandement les choses !
# ces côtés sont définis par les valeurs min et max de x,y

# le rectangle a ses côtés parralèles aux axes, ça simplifie grandement les choses !
# ces côtés sont définis par les valeurs min et max de x,y

for _ in range(int(input())):
    n = int(input())
    x, y = [0] * n, [0] * n

    for i in range(n):
        x[i], y[i] = map(int, input().split())

    x0, y0 = min(x), min(y)
    x1, y1 = max(x), max(y)

    # il faut que tous les points soient sur x0, y0, x1 ou y1
    ok = all((x[i] == x0) or (y[i] == y0) or (x[i] == x1) or (y[i] == y1)
             for i in range(n))
    print(["NO", "YES"][ok])
