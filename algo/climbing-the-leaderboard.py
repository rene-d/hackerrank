# Climbing the Leaderboard
# Help Alice track her progress toward the top of the leaderboard!
#
# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
#

"""
solution 'à la mano'
on peut aussi utiliser un set() à la place de groupby(),
puis sorted() et bisect.bisect_right() pour faire la dichotomie
ce qui revient +in fine+ à la même chose
"""

import itertools


# dichotomie dans une liste décroissante
def binary_search(a, x):

    first = 0
    last = len(a) - 1

    while first <= last:
        i = (first + last) // 2
        if a[i] == x:
            return i
        elif a[i] < x:
            last = i - 1
        else:
            first = i + 1

    return first


def climbingLeaderboard(scores, alice):
    # Complete this function
    leaderboard = [s for s, _ in itertools.groupby(scores)]

    for a in alice:

        """ version triviale
        rank = 1
        for s in leaderboard:
            if a >= s:
                break
            rank += 1
        """

        # version optimisée avec dichotomie
        # nécessaire pour passer certains testcases
        rank = binary_search(leaderboard, a) + 1

        print(rank)


if __name__ == "__main__":
    n = int(input())
    scores = list(map(int, input().split()))
    m = int(input().strip())
    alice = list(map(int, input().split()))
    climbingLeaderboard(scores, alice)
