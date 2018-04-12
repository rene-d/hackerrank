# Data Structures > Stacks > Equal Stacks
# Equalize the piles!
#
# https://www.hackerrank.com/challenges/equal-stacks/problem
#

# principe:
# on calcule la hauteur cumulée
# on part de la stack qui contient le moins d'éléments
# et on la dépile jusqu'à ce que la valeur soit présente dans toutes les autres stacks

import itertools

def get_stack():
    s = list(itertools.accumulate(reversed(list(map(int, input().split())))))
    return (len(s), s)

def max_height(oh):
    oh = list(s[1] for s in oh)
    while oh[0]:
        h = oh[0].pop()
        ok = True
        for i in range(1, len(oh)):
            while oh[i] and oh[i][-1] > h:
                oh[i].pop()
            if not oh[i]:
                return 0
            ok = ok and oh[i][-1] == h
        if ok:
            return h
    return 0


n1, n2, n3 = map(int, input().split())
oh = sorted([get_stack() for _ in range(3)])

print(max_height(oh))