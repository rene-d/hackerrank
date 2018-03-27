#!/bin/python3

import sys

def aVeryBigSum(n, ar):
    # Complete this function
    return sum(ar)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)

