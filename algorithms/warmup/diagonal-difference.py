"""
Diagonal Difference

https://www.hackerrank.com/challenges/diagonal-difference/problem
"""

import sys

def diagonalDifference(a):
    # Complete this function
    n = len(a)
    return abs(sum(a[x][x] for x in range(n)) - sum(a[x][n - x - 1] for x in range(n)))

if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
       a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
       a.append(a_t)
    result = diagonalDifference(a)
    print(result)
