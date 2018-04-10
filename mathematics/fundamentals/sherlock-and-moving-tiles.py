# Sherlock and Moving Tiles
# Help Sherlock in identifying the overlapping area.
#
# https://www.hackerrank.com/challenges/sherlock-and-moving-tiles/problem
#

L, S1, S2 = map(int, input().split())
if S1 > S2:
    S1, S2 = S2, S1

for _ in range(int(input())):
    q = int(input())

    # le long de la droite 𝓎=𝓍 :
    # coin supérieur du carré lent = S1 * t + √2 * L
    # coin inférieur du carré rapide = S2 * t
    # diagonale du carré de surface q: √(q * 2)

    t  = ((q * 2) ** 0.5 - L * 2 ** 0.5) / (S1 - S2)
    if t <= 0: t = 0
    print("%.20f" % t)