# Algorithms > Implementation > Larry's Array
# Larry
#
# https://www.hackerrank.com/challenges/larrys-array/problem
#

# Quelques explications:
# - la permutation ABC->BCA->CAB a une signature paire (https://en.wikipedia.org/wiki/Parity_of_a_permutation)
# - la parité d'une permutation ne change pas qq le nombre de cycle
# - la permutation identité est paire
# - donc pour que l'ensemble soit ordonnable avec le permutation donnée, il faut que la parité (i.e. le nombre d'inversions) soit paire
# Lire ici aussi: https://en.wikipedia.org/wiki/Inversion_(discrete_mathematics)

import itertools

for _ in range(int(input())):
    n = input()
    A = list(map(int, input().split()))

    # calcule le nombre d'inversions de A[]
    inversions = 0
    for i in itertools.combinations(A, 2):
        if i[0] > i[1]:
            inversions += 1

    if inversions % 2 == 0:
        print("YES")
    else:
        print("NO")
