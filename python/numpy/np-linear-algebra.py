# Python > Numpy > Linear Algebra
# NumPy routines for linear algebra calculations.
#
# https://www.hackerrank.com/challenges/np-linear-algebra/problem
#

import numpy

if numpy.version.version >= '1.14.':
    numpy.set_printoptions(legacy='1.13')

m = numpy.array([input().split() for i in range(int(input()))], numpy.float)
print(numpy.linalg.det(m))
