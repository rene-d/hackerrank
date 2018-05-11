# Ad Infinitum18 > Minimum Height Triangle
# Find the smallest height of a triangle preserving the given constraints.
#
# https://www.hackerrank.com/contests/infinitum18/challenges/lowest-triangle
#

base, area = map(int, input().split())
height = (2 * area - 1) // base + 1
print(height)
