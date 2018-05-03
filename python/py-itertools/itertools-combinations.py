# Python > Itertools > itertools.combinations()
# Print all the combinations of a string using itertools.
#
# https://www.hackerrank.com/challenges/itertools-combinations/problem
#

from itertools import combinations

s, n = input().split()
for k in range(1, int(n) + 1):
    for i in combinations(sorted(s), k):
        print("".join(i))
