# Python > Numpy > Polynomials
# Given the coefficients, use polynomials in NumPy.
#
# https://www.hackerrank.com/challenges/np-polynomials/problem
#

import numpy

p = list(map(float, input().split()))
print(numpy.polyval(p, float(input())))
