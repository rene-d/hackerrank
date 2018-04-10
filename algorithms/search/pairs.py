"""
Pairs

https://www.hackerrank.com/challenges/pairs/problem
"""

import sys
import bisect

def pairs(k, arr):
    # Complete this function
    arr = sorted(arr)
    nb = 0
    length = len(arr)
    for v in arr:
        i = bisect.bisect_left(arr, v + k)
        while i < length and arr[i] == v + k:
            i += 1
            nb += 1
    return nb

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = list(map(int, input().strip().split(' ')))
    result = pairs(k, arr)
    print(result)
