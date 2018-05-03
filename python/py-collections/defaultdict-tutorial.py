# Python > Collections > DefaultDict Tutorial
# Create dictionary value fields with predefined data types.
#
# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
#

from collections import defaultdict

n, m = map(int, input().split())

A = defaultdict(list)
for i in range(1, n + 1):
    A[input()].append(i)

for _ in range(m):
    r = A[input()]
    if len(r) == 0:
        print(-1)
    else:
        print(" ".join(map(str, r)))
