# Mathematics > Linear Algebra Foundations > Linear Algebra Foundations #7 - The 1000th Power of a Matrix
# Compute the 1000th power of the given matrix.
#
# https://www.hackerrank.com/challenges/linear-algebra-foundations-7-the-1000th-power-of-a-matrix/problem
#

# solution plus aboutie, en calculant l'exponentiation soi-même

def multm(A, B):
    """ produit matriciel: A * B """
    a00, a10, a01, a11 = A
    b00, b10, b01, b11 = B
    return [a00 * b00 + a10 * b01, a00 * b10 + a10 * b11,
            a01 * b00 + a11 * b01, a01 * b10 + a11 * b11]


def multv(A, V):
    """ produit matrice/vecteur: A * V """
    a00, a10, a01, a11 = A
    b0, b1 = V
    return [a00 * b0 + a10 * b1,
            a01 * b0 + a11 * b1]


def power(M, k):
    """ fast exponentiation M^k """
    P = [1, 0,
         0, 1]

    if k == 0:
        return P
    if k == 1:
        return M

    while k != 0:
        if k % 2 == 1:
            P = multm(P, M)
        M = multm(M, M)
        k //= 2
    return P


A = [-2, -9, 1, 4]
B = power(A, 1000)
for x in B:
    print(x)
