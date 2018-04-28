# Mathematics > Linear Algebra Foundations > Linear Algebra Foundations #10 - Eigenvectors
# Compute the EigenVectors of the following 2x2 matrix.
#
# https://www.hackerrank.com/challenges/linear-algebra-fundamentals-10-eigenvectors/problem
#

import numpy as np

A = np.matrix([[ 0,  1],
               [-2, -3]])
eig, vec = np.linalg.eig(A)

print(eig, vec)

v1 = vec[0].A1
v2 = vec[1].A1

print(v1)
print(v2)

# v1 =  sqrt(1/2) -sqrt(2/5)
# v1 = -sqrt(1/2)  sqrt(4/5)

# réponse
# cf. http://www.wolframalpha.com/input/?i=%7B%7B0,+1%7D,+%7B-2,+-3%7D%7D
# -2 -1
