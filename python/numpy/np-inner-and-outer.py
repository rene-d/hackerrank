# Python > Numpy > Inner and Outer
# Use NumPy to find the inner and outer product of arrays.
#
# https://www.hackerrank.com/challenges/np-inner-and-outer/problem
#

import numpy

u = numpy.array(input().split(), numpy.int)
v = numpy.array(input().split(), numpy.int)

print(numpy.inner(u, v))
print(numpy.outer(u, v))
