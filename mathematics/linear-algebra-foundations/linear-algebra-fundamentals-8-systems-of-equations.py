# Mathematics > Linear Algebra Foundations > Linear Algebra Foundations #8 - Systems of Equations
# A system of equations with no solutions.
#
# https://www.hackerrank.com/challenges/linear-algebra-fundamentals-8-systems-of-equations/problem
#

import numpy as np

for a in range(-10, 11, 1):
    M = np.matrix([[a, 1, 2],
                   [1, 2, 1],
                   [2, 1, a]])
    if abs(np.linalg.det(M)) < 1e-6:
        print(a)

"""
réponse:
-1
2
"""