# Python > Built-Ins > Athlete Sort
# Sort the table on the kth attribute.
#
# https://www.hackerrank.com/challenges/python-sort-sort/problem
#

import operator

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

for i in sorted(arr, key=operator.itemgetter(k)):
    print(*i)
