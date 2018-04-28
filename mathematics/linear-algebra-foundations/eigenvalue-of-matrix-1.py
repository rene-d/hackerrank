# Mathematics > Linear Algebra Foundations > Eigenvalue of a Matrix I
# Basic problems related to eigenvalues.
#
# https://www.hackerrank.com/challenges/eigenvalue-of-matrix-1/problem
#

import numpy as np

M = np.matrix([[1, -3, 3],
               [3, -5, 3],
               [6, -6, 4]])

print(np.linalg.eigvals(M))

I = np.identity(np.linalg.matrix_rank(M))

for λ in np.linalg.eigvals(M):
    print(np.linalg.det(M - λ * I))