# Mathematics > Geometry > Circle City
# Determine whether Roy's city can be saved or not.
#
# https://www.hackerrank.com/challenges/circle-city/problem
# https://www.hackerrank.com/contests/101aug14/challenges/circle-city
#

# https://fr.wikipedia.org/wiki/Théorème_des_deux_carrés_de_Fermat#Le_cas_général

# le nombre de décompositions d'un entier n en somme de deux carrés est égal
# à 4*(d1 - d3) où d1 (resp. d3) = nombre de diviseurs congrus à 1 mod 4 (resp. 3)

import sys

def diviseurs(n):
    div = [1]
    i = 2
    while i * i <= n:
        q, r = divmod(n, i)
        if r == 0:
            div.append(i)
            if i != q:
                div.append(q)
        i += 1
    if n != 1:
        div.append(n)
    return div


for _ in range(int(input())):
    rr, k = map(int, input().split())

    d = diviseurs(rr)
    d1 = sum(1 for i in d if i % 4 == 1)
    d3 = sum(1 for i in d if i % 4 == 3)
    r2 = 4 * (d1 - d3)
    print("n={} div={} d1={} d3={} r2={}".format(rr, d, d1, d3, r2), file=sys.stderr)
    if k >= r2:
        print("possible")
    else:
        print("impossible")
