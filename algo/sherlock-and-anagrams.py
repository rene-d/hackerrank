# Sherlock and Anagrams
# Find the number of unordered anagramic pairs of substrings of a string.
#
# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem
#

import sys

def sherlockAndAnagrams(s):
    ana = { }
    nb = 0
    n = len(s)
    for i in range(0, n):
        for j in range(i + 1, n + 1):
            a = ''.join(sorted(s[i:j]))
            if a in ana:
                ana[a] += 1
                nb += ana[a]
            else:
                ana[a] = 0
    return nb

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = sherlockAndAnagrams(s)
    print(result)
