# Mathematics > Geometry > Sherlock and Counting
# Help Sherlock count numbers satisfying an inequality.
#
# https://www.hackerrank.com/challenges/sherlock-and-counting/problem
#

from math import sqrt, floor, ceil


for _ in range(int(input())):
    n, k = map(int, input().split())

    # résoud  x*(n-x)=n*k

    # les solutions seront les entiers entre [0, n]
    # qui ne sont pas dans la parabole (sommet vers le haut), i.e dans [r1, r2]
    #              __
    #          r1 /  \ r2
    # +__________/____\________+___
    # 0         /      \       n
    #          /        \

    D = n * n - 4 * k * n
    if D <= 0:
        print(n - 1)
    else:
        r1 = (n - sqrt(D)) / 2
        r2 = (n + sqrt(D)) / 2

        print(floor(r1) + (n - ceil(r2)))
