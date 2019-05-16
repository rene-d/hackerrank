# RookieRank > Antiprime Numbers
# For each $a_i$, find the smallest antiprime greater than or equal to $a_i$.
#
# https://www.hackerrank.com/contests/rookierank/challenges/antiprime-numbers
# challenge id: 23016
#

#!/bin/python3

import sys
import math
import bisect


def solve(a):
    pass


def precompute():
    MAX = 1000000 + 10000000
    max_ds = 0
    for n in range(1, MAX + 1):
        cnt = 0
        for d in range(1, int(math.sqrt(n)) + 1):
            q, r = divmod(n, d)
            if r == 0: cnt += 1
            if q != d: cnt += 1

        if cnt > max_ds:
            max_ds = cnt
            #antiprimes.append(n)
            print(n)


if len(sys.argv) == 2:
    precompute()

else:

    for _ in range(int(input())):
        solve(int(input()))
