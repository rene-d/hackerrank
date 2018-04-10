# Happy Ladybugs
# Determine whether or not all the ladybugs can be made happy.
#
# https://www.hackerrank.com/challenges/happy-ladybugs/problem
#

import itertools


def happyLadybugs(b):
    # y a-t-il une case vide ?
    if b.count('_') == 0:
        # non: il faut alors que le board soit déjà happy
        for k, g in itertools.groupby(b):
            if len(list(g)) < 2: return "NO"
        return "YES"

    # ici, on a une empty cell
    # pour arriver à rendre les ladybugs happy,
    # il faut qu'il y en ait au moins 2 de chaque
    # (on ne calcule pas les mouvements)
    ladybugs = [0] * 26
    for c in b:
        if c != '_':
            ladybugs[ord(c) - ord('A')] += 1

    # une coccinelle d'un seul type: jamais heureuse
    if any(map(lambda x: x == 1, ladybugs)): return "NO"
    return "YES"


if __name__ == '__main__':
    for _ in range(int(input())):
        input()
        b = input()
        print(happyLadybugs(b))
