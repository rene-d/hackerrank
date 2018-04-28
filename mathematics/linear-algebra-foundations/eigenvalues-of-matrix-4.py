# Mathematics > Linear Algebra Foundations > Eigenvalue of matrix #4
# Basic problems related to eigenvalues.
#
# https://www.hackerrank.com/challenges/eigenvalues-of-matrix-4/problem
#

import numpy as np

A = np.matrix([[ 2, -1],
               [-1,  2]])

I = np.identity(np.linalg.matrix_rank(A))

print(np.linalg.eigvals(np.linalg.inv(A)))

print(np.linalg.eigvals(A - 4 * I))
