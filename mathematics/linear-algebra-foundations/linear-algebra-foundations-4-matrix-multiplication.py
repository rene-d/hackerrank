# Mathematics > Linear Algebra Foundations > Linear Algebra Foundations #4- Matrix Multiplication
# Matrix Multiplication of 2x2 Matrices
#
# https://www.hackerrank.com/challenges/linear-algebra-foundations-4-matrix-multiplication/problem
#

import numpy as np

a = np.matrix([[1,2,3], [2,3,4], [1,1,1]])
b = np.matrix([[4,5,6], [7,8,9], [4,5,7]])
print(a * b)

"""
réponse:

30
36
45
45
54
67
15
18
22
"""