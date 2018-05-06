# Python > Numpy > Transpose and Flatten
# Use the transpose and flatten tools in the NumPy module to manipulate an array.
#
# https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem
#

import numpy

n, m = map(int, input().split())

M = numpy.array([input().split() for i in range(n)], numpy.int)

print(M.transpose())
print(M.flatten())
