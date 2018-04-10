# Anagram
# Find the minimum number of characters of the first string that we need to change in order to make it an anagram of the second string.
#
# https://www.hackerrank.com/challenges/anagram/problem
#

def anagram(s):
    n = len(s)
    if n % 2 == 1: return -1
    a = [0] * 26
    b = [0] * 26
    for i in range(n // 2):
        j = ord(s[i]) - ord('a')
        a[j] += 1
    for i in range(n // 2, n):
        j = ord(s[i]) - ord('a')
        b[j] += 1
    return sum(abs(a[i] - b[i]) for i in range(26)) // 2


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = anagram(s)
    print(result)
