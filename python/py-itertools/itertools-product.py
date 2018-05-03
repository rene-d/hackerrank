# Python > Itertools > itertools.product()
# Find the cartesian product of 2 sets. 
# 
# https://www.hackerrank.com/challenges/itertools-product/problem
# 

from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))

P = list(product(A, B))

print(" ".join(str(x) for x in P))
