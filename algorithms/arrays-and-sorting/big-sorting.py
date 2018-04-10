# Big Sorting
# Sort an array of very long numeric strings.
#
# https://www.hackerrank.com/challenges/big-sorting/problem
#

import functools

def entier(a, b):
    la, lb = len(a), len(b)
    if la < lb: return -1
    if la > lb: return +1
    if a < b: return -1
    if a > b: return +1
    return 0

if __name__ == "__main__":
    n = int(input())
    arr = list(input() for i in range(n))
    for i in sorted(arr, key=functools.cmp_to_key(entier)):
        print(i)
