# Forming a Magic Square
# Find the minimum cost of converting a 3 by 3 matrix into a magic square.
# 
# https://www.hackerrank.com/challenges/magic-square-forming/problem
# 
#!/bin/python3

import sys
import operator

# il n'y a que 8 magic squares 3x3 avec [1..9]
# liste ici par exemple: https://mindyourdecisions.com/blog/2015/11/08/how-many-3x3-magic-squares-are-there-sunday-puzzle/
MAGIC_SQUARES = [
    [8, 1, 6, 3, 5, 7, 4, 9, 2],
    [6, 1, 8, 7, 5, 3, 2, 9, 4],
    [6, 1, 8, 7, 5, 3, 2, 9, 4],
    [4, 9, 2, 3, 5, 7, 8, 1, 6],
    [2, 9, 4, 7, 5, 3, 6, 1, 8], 
    [8, 3, 4, 1, 5, 9, 6, 7, 2],
    [4, 3, 8, 9, 5, 1, 2, 7, 6], 
    [6, 7, 2, 1, 5, 9, 8, 3, 4], 
    [2, 7, 6, 9, 5, 1, 4, 3, 8],
]

def formingMagicSquare(s):        
    return min(sum(map(abs, map(operator.sub, s, m))) for m in MAGIC_SQUARES)

if __name__ == "__main__":
    s = []
    for _ in range(3):
      s.extend(map(int, input().split()))
    result = formingMagicSquare(s)
    print(result)

