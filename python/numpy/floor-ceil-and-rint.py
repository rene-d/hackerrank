# Python > Numpy > Floor, Ceil and Rint
# Use the floor, ceil and rint tools of NumPy on the given array.
#
# https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem
#

import numpy

if numpy.version.version >= '1.14.':
    numpy.set_printoptions(legacy='1.13')

a = numpy.array(input().split(), numpy.float)
print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))
