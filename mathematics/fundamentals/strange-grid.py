# Strange Grid Again
# find the integer in c-th column in r-th row of the grid.
#
# https://www.hackerrank.com/challenges/strange-grid/problem
#

r, c = map(int, input().split())

r -= 1
c -= 1
print((r // 2) * 10 + c * 2 + r % 2)
