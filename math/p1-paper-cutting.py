# Cutting Paper Squares
# Determine the number of cuts needed to cut a paper into $1 \times 1$ squares.
#
# https://www.hackerrank.com/challenges/p1-paper-cutting/problem
#

import sys

def solve(n, m):
    # Complete this function
    return n * m - 1


n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
result = solve(n, m)
print(result)
