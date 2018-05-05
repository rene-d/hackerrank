# Project Euler #31: Coin sums
#
# https://www.hackerrank.com/contests/projecteuler/challenges/euler031/problem
#

coins = [1, 2, 5, 10, 20, 50, 100, 200]

cache = []


def r(objectif):

    for i in range(len(cache), objectif + 1):

        arr = [1, 0, 0, 0, 0, 0, 0, 0]

        for j in range(1, 8):
            arr[j] = arr[j - 1]

            if i >= coins[j]:
                arr[j] += cache[i - coins[j]][j]

        cache.append(arr)

    return cache[objectif][7] % 1000000007


for _ in range(int(input())):
    print(r(int(input())))
