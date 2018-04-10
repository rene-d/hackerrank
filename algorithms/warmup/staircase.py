"""
Staircase

https://www.hackerrank.com/challenges/staircase/problem
"""

import sys

def staircase(n):
    # Complete this function
    for i in range(1, n + 1):
        print(" " * (n - i) + "#" * i)

if __name__ == "__main__":
    n = int(input().strip())
    staircase(n)
