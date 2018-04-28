# Mathematics > Linear Algebra Foundations > Eigenvalue of matrix #2
# Basic problems related to eigenvalues.
#
# https://www.hackerrank.com/challenges/eigenvalue-of-matrix-2/problem
#

import numpy as np

M = np.matrix([[1, 2],
               [2, 4]])

print(np.linalg.eigvals(M))

I = np.identity(np.linalg.matrix_rank(M))

for λ in np.linalg.eigvals(M):
    print(np.linalg.det(M - λ * I))