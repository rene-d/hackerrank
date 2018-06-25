# Algorithms > Constructive Algorithms > New Year Chaos
# Determine how many bribes took place to get a queue into its current state.
#
# https://www.hackerrank.com/challenges/new-year-chaos/problem
# https://www.hackerrank.com/contests/hourrank-4/challenges/new-year-chaos
# challenge id: 15305
#

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    q.insert(0, 0)
    length = len(q)

    for i, v in enumerate(q):
        if v - i > 2:
            print("Too chaotic")
            return

    swaps = 0
    for i in range(length - 1):
        before = swaps
        for j in range(length - 1):
            if q[j] > q[j + 1]:
                q[j], q[j + 1] = q[j + 1], q[j]
                swaps += 1
                swaped = True
        if swaps == before:
            break

    print(swaps)
    return

    # minimal swaps:
    ref = [0] * (length)
    for i, x in enumerate(q):
        ref[x] = i
    swaps = 0
    for i in range(length):
        k = q[i]
        if k != i:
            q[i], q[ref[i]] = q[ref[i]], q[i]
            ref[i], ref[k] = ref[k], ref[i]
            swaps += 1
    print(swaps)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        q = list(map(int, input().split()))
        minimumBribes(q)
