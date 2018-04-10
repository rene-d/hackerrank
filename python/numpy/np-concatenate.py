# Concatenate
# Use the concatenate function on 2 arrays.
# 
# https://www.hackerrank.com/challenges/np-concatenate/problem
# 

import numpy

n, m, p = map(int, input().split())

N = numpy.array([list(map(int, input().split())) for _ in range(n)])
M = numpy.array([list(map(int, input().split())) for _ in range(m)])

print(numpy.concatenate((N, M), axis = 0))
