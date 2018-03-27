# Connecting Towns
# Find the Number of ways to in which one can travel from one town to another.
#
# https://www.hackerrank.com/challenges/connecting-towns/problem
#

# Python gère nativement les big integers, il suffit de lire l'énoncé

for _ in range(int(input())):
    n = int(input())
    r = list(map(int, input().split()))

    p = 1
    for i in r:
        p = (p * i) % 1234567
    print(p)
