"""
Matrix Script

https://www.hackerrank.com/challenges/matrix-script/problem
"""

import itertools
import re

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
matrix = []
matrix_i = 0
for matrix_i in range(n):
    matrix_t = str(input())
    matrix.append(matrix_t)

message = ''.join(itertools.chain.from_iterable(itertools.zip_longest(*matrix, fillvalue=' ')))

message = re.sub(r"([a-zA-Z0-9])\W+([a-zA-Z0-9])", r"\1 \2", message)
print(message)
