# ProjectEuler+ > Project Euler #18: Maximum path sum I
# Find path with largest sum in a pyramid.
#
# https://www.hackerrank.com/contests/projecteuler/challenges/euler018
# challenge id: 2644
#

def solve(triangle):
    answer = 0

    # algo trivial: calcule les sommes sur tous les chemins possibles
    def cherche(ligne, position, somme):
        nonlocal answer

        if ligne >= len(triangle):
            if somme > answer:
                answer = somme
        else:
            i = triangle[ligne][position]
            cherche(ligne + 1, position, somme + i)

            if ligne > 0:
                i = triangle[ligne][position + 1]
                cherche(ligne + 1, position + 1, somme + i)

        return somme

    cherche(0, 0, 0)
    return answer


for _ in range(int(input())):
    triangle = []
    n = int(input())
    for _ in range(n):
        triangle.append(list(map(int, input().split())))
    print(solve(triangle))
