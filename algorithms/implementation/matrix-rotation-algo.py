# Matrix Layer Rotation 
# Rotate the matrix R times and print the resultant matrix.
# 
# https://www.hackerrank.com/challenges/matrix-rotation-algo/problem
# 

# pour mise au point
verbose = False


def rotate(l, n):
    n = n % len(l)
    return l[n:] + l[:n]


def matrixRotation(matrix, r):
    # Complete this function

    if verbose:
        for row in matrix:     
            print(' '.join("{:2}".format(i) for i in row))

    m = len(matrix[0])      # nombre de colonnes
    n = len(matrix)         # nombre de lignes

    for i in range(0, min(m, n) // 2):

        # crée un tableau qui contient les éléments à tourner
        # nécessaire, sinon certains testcases tombent en timeout
        c = []

        # ligne du haut
        c.extend(matrix[i][i:m-i])

        # colonne à droite
        for j in range(i + 1, n - i - 1):
            c.append(matrix[j][m-i-1])
        
        # ligne du bas
        c.extend(reversed(matrix[n-1-i][i:m-i]))

        # colonne à gauche
        for j in range(n-1-i-1, i, -1):
            c.append(matrix[j][i])
        
        # effectue la rotation
        c = rotate(c, r)

        # remplace dans la matrice les éléments tournés
        k = 0

        # ligne du haut (optimisable...)
        for j in range(i, m - i):
            matrix[i][j] = c[k]
            k += 1
        
        # colonne de droite
        for j in range(i + 1, n - i - 1):
            matrix[j][m - i - 1] = c[k]
            k += 1

        # ligne du bas (optimisable aussi...)
        for j in range(m - 1 - i, i - 1, -1):
            matrix[n - 1 - i][j] = c[k]
            k += 1

        # colonne de gauche
        for j in range(n - i - 2, i, -1):
            matrix[j][i] = c[k]
            k+=1
    
    if verbose:
        print("après {} rotations".format(r))
        for row in matrix:
            print(' '.join("{:2}".format(i) for i in row))
    else:
        for row in matrix:
            print(' '.join(str(i) for i in row))


if __name__ == "__main__":
    m, n, r = map(int, input().split(' '))
    matrix = []
    for matrix_i in range(m):
    	matrix_t = list(map(int, input().split(' ')))
    	matrix.append(matrix_t)
    matrixRotation(matrix, r)

