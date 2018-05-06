# Python > Numpy > Sum and Prod
# Perform the sum and prod functions of NumPy on the given 2-D array.
#
# https://www.hackerrank.com/challenges/np-sum-and-prod/problem
#

import numpy

n, m = map(int, input().split())
A = numpy.array([input().split() for i in range(n)], numpy.int)

print(numpy.prod(numpy.sum(A, axis=0)))
