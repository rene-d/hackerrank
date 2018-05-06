# Python > Numpy > Shape and Reshape
# Using the shape and reshape tools available in the NumPy module, configure a list according to the guidelines.
#
# https://www.hackerrank.com/challenges/np-shape-reshape/problem
#

import numpy

v = numpy.array(input().split(), numpy.integer)
m = numpy.reshape(v, (3, 3))
print(m)