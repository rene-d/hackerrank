# Minimum Height Triangle
# Find the smallest height of a triangle preserving the given constraints.
#
# https://www.hackerrank.com/challenges/lowest-triangle/problem
#

base, area = map(int, input().split())
height = (2 * area - 1) // base + 1
print(height)
