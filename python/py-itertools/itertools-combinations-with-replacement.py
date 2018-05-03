# Python > Itertools > itertools.combinations_with_replacement()
# Find all the combinations of a string with replacements.
#
# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
#

from itertools import combinations_with_replacement

s, n = input().split()
for i in combinations_with_replacement(sorted(s), int(n)):
    print("".join(i))
