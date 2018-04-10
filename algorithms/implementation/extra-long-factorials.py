# Extra Long Factorials
# Calculate a very large factorial that doesn't fit in the conventional numeric data types.
#
# https://www.hackerrank.com/challenges/extra-long-factorials/problem
#

import functools
import operator

def extraLongFactorials(n):
    # Complete this function
    fac = functools.reduce(operator.mul, [i for i in range(1, n + 1)], 1)
    print(fac)
    # ou tout simplement math.factorial(n) !!!

if __name__ == "__main__":
    n = int(input().strip())
    extraLongFactorials(n)
