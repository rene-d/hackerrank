"""
Maximize It!

https://www.hackerrank.com/challenges/maximize-it/problem
"""

import itertools

N = []
K, M = map(int, input().split())
for _ in range(K):
    N.append(list(map(lambda x: int(x) ** 2, input().split()))[1:])

Smax = max([sum(i) % M for i in itertools.product(*N)])

print(Smax)
