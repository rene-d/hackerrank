# Python > Numpy > Dot and Cross
# Use NumPy to find the dot and cross products of arrays.
#
# https://www.hackerrank.com/challenges/np-dot-and-cross/problem
#

import numpy

n = int(input())

A = numpy.array([input().split() for i in range(n)], numpy.int)
B = numpy.array([input().split() for i in range(n)], numpy.int)

print(A.dot(B))
