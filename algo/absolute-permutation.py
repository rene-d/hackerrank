# Absolute Permutation
#  Find lexicographically smallest absolute permutation.
# 
# https://www.hackerrank.com/challenges/absolute-permutation/problem
# 

import sys
import itertools

""" trop lent !
def abs_perm(n, k):
    for p in itertools.permutations(range(1, n + 1)):
        if all(abs(i - pi) == k for i, pi in enumerate(p, 1)):
            return p
    return [-1]
"""    

def abs_perm(n, k):
    if k == 0:
        return [i for i in range(1, n + 1)]
    
    if n % (k * 2) != 0:
        return [-1]

    r = []
    sign = 1
    for i in range(1, n + 1):
        x = i + k * sign
        r.append(x)
        if i % k == 0: sign = -sign

    #assert all(abs(i - v)==k for i, v in enumerate(r, 1)) 
    #assert len(r) == n 
    #assert sorted(r) == [i for i in range(1, n + 1)]

    return r


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    r = abs_perm(n, k)
    print(' '.join(map(str, r)))
