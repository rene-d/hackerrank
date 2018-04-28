# Mathematics > Linear Algebra Foundations > Determinant of the matrix #1
# Basic problems related to determinants.
#
# https://www.hackerrank.com/challenges/determinant-of-the-matrix-1/problem
#

import numpy as np

M = np.matrix([[  3,  0,  0, -2,  4],
               [  0,  2,  0,  0,  0],
               [  0, -1,  0,  5, -3],
               [ -4,  0,  1,  0,  6],
               [  0, -1,  0,  3,  2]])

M = np.matrix([[ a, b, c],
               [ d, e, f],
               [ g, h, h]])

print(round(np.linalg.det(M)))

# réponse: -114
