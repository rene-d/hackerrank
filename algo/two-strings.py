# Two Strings
# Given two strings, you find a common substring of non-zero length.
#
# https://www.hackerrank.com/challenges/two-strings/problem
#

def twoStrings(s1, s2):
    # Complete this function
    return "YES" if len(set.intersection(set(s1), set(s2))) > 0 else "NO"

q = int(input().strip())
for a0 in range(q):
    s1 = input().strip()
    s2 = input().strip()
    result = twoStrings(s1, s2)
    print(result)
