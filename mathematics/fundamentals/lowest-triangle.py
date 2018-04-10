# Minimum Height Triangle
# Find the smallest height of a triangle preserving the given constraints.
#
# https://www.hackerrank.com/challenges/lowest-triangle/problem
#


def lowestTriangle(base, area):
    # Complete this function
    h = area / base * 2
    if int(h) == h:
        return int(h)
    else:
        return int(h) + 1

base, area = input().strip().split(' ')
base, area = [int(base), int(area)]
height = lowestTriangle(base, area)
print(height)
