# Python > Numpy > Array Mathematics
# Perform basic mathematical operations on arrays in NumPy.
#
# https://www.hackerrank.com/challenges/np-array-mathematics/problem
#

import numpy

n, m = map(int, input().split())

A = numpy.array([input().split() for i in range(n)], numpy.int)
B = numpy.array([input().split() for i in range(n)], numpy.int)

print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)
print(A ** B)
