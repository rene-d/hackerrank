# Python > Itertools > itertools.permutations()
# Find all permutations of a given size in a given string.
#
# https://www.hackerrank.com/challenges/itertools-permutations/problem
#

from itertools import permutations

s, n = input().split()
for i in permutations(sorted(s), int(n)):
    print("".join(i))
