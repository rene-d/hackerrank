# Sherlock and the Valid String
# Remove some characters from the string such that the new string's characters have the same frequency.
#
# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
#

#!/bin/python3

import sys

def isValid(s):
    # Complete this function
    f = [0] * 26
    for c in s:
        f[ord(c) - ord('a')] += 1

    a = b = max(f)
    for i in f:
        if i > 0 and i < a:
            a = i

    # la fréquence est la même
    if a == b: return "YES"

    if a == 1:
        # une lettre isolée, le reste est sur la même fréquence
        if sum(1 for i in f if i == a) == 1: return "YES"

    if b - a > 1: return "NO"

    if sum(1 for i in f if i == b) == 1: return "YES"


    if sum(1 for i in f if i == a) > 1: return "NO"

    return "YES"


s = input().strip()
result = isValid(s)
print(result)
