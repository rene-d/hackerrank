# Halloween Sale
# How many games can you buy during the Halloween Sale?
#
# https://www.hackerrank.com/challenges/halloween-sale/problem
#


def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    # p = prix d'origine
    # d = ristourne
    # m = prix minimum
    # s = budget

    # plutôt que de trouver la formule exacte, on peut se contenter de boucler
    # il y a 10^4 itérations au max
    nb = 0
    while s >= p:
        s -= p
        p = max(m, p - d)
        nb += 1
    return nb


if __name__ == "__main__":
    p, d, m, s = input().strip().split(' ')
    p, d, m, s = [int(p), int(d), int(m), int(s)]
    answer = howManyGames(p, d, m, s)
    print(answer)


""" ici la solution mathématique:
from math import floor, sqrt
p, d, m, s = map(int, input().split())
x = ((p-m) + (d-1)) // d # after x games, all cost m
cx = x*p - ((x*(x-1))>>1)*d
if s <= cx:
    # solve (-d/2)*n^2 + (p-d/2)*n - s <= 0
    v = 1 + p/d
    print(floor(v - sqrt(v*v - 2*s/d)))
else:
    print(x + (s - cx) // m)
"""
