# Mathematics > Linear Algebra Foundations > Eigenvalue of matrix #3
# Basic problems related to eigenvalues.
#
# https://www.hackerrank.com/challenges/eigenvalues-of-matrix-3/problem
#

import numpy as np

a = np.matrix([[2, -1], [-1, 2]])

print(np.linalg.eigvalsh(a))
print(np.linalg.eigvalsh(a * a))

"""
réponse:

1
3
1
9
"""