# Mathematics > Combinatorics > Picking Cards
# How many ways can you pick up all the cards from a table?
#
# https://www.hackerrank.com/challenges/picking-cards/problem
# challenge id: 69
#

MOD = 1000000007

for _ in range(int(input())):
    n = int(input())
    cards = list(map(int, input().split()))
    cards.sort(reverse=True)
    res = 1
    for i, c in enumerate(cards):
        val = n - c
        if val <= 0:
            print(0)
            break
        res = (res * (val - i)) % MOD
    else:
        print(res)
