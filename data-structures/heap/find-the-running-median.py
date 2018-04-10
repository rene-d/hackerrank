# Find the Running Median
# Find the median of the elements after inputting each element.
#
# https://www.hackerrank.com/challenges/find-the-running-median/problem
#

import bisect

a = []
for _ in range(int(input())):
    n = int(input())
    bisect.insort(a, n)
    m = (a[(len(a) - 1) // 2] + a[len(a) // 2]) / 2
    print("%.1f" % m)
