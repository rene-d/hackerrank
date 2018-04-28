# Mathematics > Linear Algebra Foundations > Linear Algebra Foundations #3- Matrix Multiplication
# Matrix Multiplication of 2x2 Matrices
#
# https://www.hackerrank.com/challenges/linear-algebra-foundations-3-matrix-multiplication/problem
#

import numpy as np

a = np.matrix([[1, 2], [2, 3]])
b = np.matrix([[4, 5], [7, 8]])

p = a * b
print(p)
