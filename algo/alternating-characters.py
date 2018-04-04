# Alternating Characters
# Calculate the minimum number of deletions required to convert a string into a string in which consecutive characters are different.
#
# https://www.hackerrank.com/challenges/alternating-characters/problem
#

import itertools

def alternatingCharacters(s):
    return sum(len(list(g)) - 1 for k, g in itertools.groupby(s))

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = alternatingCharacters(s)
    print(result)
