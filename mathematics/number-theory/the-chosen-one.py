# Mathematics > Number Theory > The Chosen One
# Given a list of integers, find and print an integer that is a divisor of all but one integer in the list.
#
# https://www.hackerrank.com/challenges/the-chosen-one/problem
#

from math import gcd


n = int(input())
A = list(map(int, input().split()))

if n == 1:
    print(A[0] + 1)

else:
    gauche = [0] * n
    droite = [0] * n

    # calcul du gcd de [A0..Ai] dans gauche[i]
    g = 0
    for i in range(n):
        g = gauche[i] = gcd(g, A[i])

    # calcul du gcd de [Ai..An] dans droite[i]
    g = 0
    for i in range(n - 1, -1, -1):
        g = droite[i] = gcd(g, A[i])

    # avec les deux tablaaux ci-dessus, on peut calculer le gcd de {A} \ A[i]
    # gcd(gauche[i-1]), droite[i+1])
    # si ce gcd ne divise pas A[i] on a trouvé une solution

    for i in range(n):
        if i == 0:
            g = droite[i + 1]
        elif i == n - 1:
            g = gauche[i - 1]
        else:
            g = gcd(gauche[i - 1], droite[i + 1])
        if A[i] % g != 0:
            print(g)
            break
