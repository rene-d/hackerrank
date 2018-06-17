# Mathematics > Algebra > Stepping Stones Game
# Can you tell Bob, if he should play Stepping Stones or not ?
#
# https://www.hackerrank.com/challenges/stepping-stones-game/problem
# https://www.hackerrank.com/contests/infinitum-aug14/challenges/stepping-stones-game
#

# il faut vérifier si n est un nombre triangulaire
# 1+2+...+n = n(n+1)/2

from math import sqrt

# n = x * (x + 1) / 2
# x^2 + x - 2 * n = 0
# x = (-1 ± sqrt(1+8n)/2)


for _ in range(int(input())):
    n = int(input())

    d = 1 + 8 * n
    r = int(sqrt(d))
    if r ** 2 == d and (r - 1) % 2 == 0:
        print("Go On Bob", (r - 1) // 2)
    else:
        print("Better Luck Next Time")
