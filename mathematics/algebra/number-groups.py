# Mathematics > Algebra > Number Groups
# Find the sum of consecutive odd number groups.
#
# https://www.hackerrank.com/challenges/number-groups/problem
#

#!/bin/python3

import sys

def sumOfGroup(k):
    # Return the sum of the elements of the k'th group.

    # début de la séquence: n
    # k=1:  1               = 2*0+1
    # k=2:  3,5             = 2*1+1 = 2*k*(k-1)/2+1
    # k=3:  7,9,11          = 2*3+1 = 2*k*(k-1)/2+1
    # k=4:  13,15,17,19     = 2*6+1 = 2*k*(k-1)/2+1
    # n = k * (k - 1) + 1

    # somme des k impairs à partir de n: s
    # n + n+2 + n+4 + n+6 + ... + n+2(k-1)
    # k * n + 2*(0+1+2+...+k-1)
    # k * n + 2*(k * (k-1) / 2)
    # s = k * n + k * (k - 1)

    # et en simplifiant:
    return k ** 3


if __name__ == "__main__":
    k = int(input().strip())
    answer = sumOfGroup(k)
    print(answer)
