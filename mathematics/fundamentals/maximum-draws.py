# Maximum Draws
# Count the minimum Draws
#
# https://www.hackerrank.com/challenges/maximum-draws/problem
#

for _ in range(int(input())):
    n = int(input())

    # dans le pire des cas, on retire toutes les chaussettes de chaque paire
    # à la suivante, on aura forcément une paire assortie
    print(n + 1)
