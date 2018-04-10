"""
Array Pairs

https://www.hackerrank.com/challenges/array-pairs/problem
"""

n = int(input())
a = list(map(int, input().split()))

#import random
#a = [1,1,2,4,2,1,1,2,4,36,1,2,4,21,1,2,4,2]
#n = len(a)

""" BRUTE FORCE """
nb = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        m = max(a[i:j + 1])
        if a[i] * a[j] <= m:
            nb += 1
print(nb)
