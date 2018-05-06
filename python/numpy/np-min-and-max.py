# Python > Numpy > Min and Max
# Use the min and max tools of NumPy on the given 2-D array.
#
# https://www.hackerrank.com/challenges/np-min-and-max/problem
#

import numpy

n, m = map(int, input().split())
A = numpy.array([input().split() for i in range(n)], numpy.int)

print(numpy.max(numpy.min(A, axis=1)))
