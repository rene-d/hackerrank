# Python > Numpy > Zeros and Ones
# Print an array using the zeros and ones tools in the NumPy module.
#
# https://www.hackerrank.com/challenges/np-zeros-and-ones/problem
#

import numpy

shape = tuple(map(int, input().split()))

print(numpy.zeros(shape, dtype=numpy.int))

print(numpy.ones(shape, dtype=numpy.int))
