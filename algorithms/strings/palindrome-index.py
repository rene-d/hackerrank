# Palindrome Index
# Determine which character(s) must be removed to make a string a palindrome.
#
# https://www.hackerrank.com/challenges/palindrome-index/problem
#

import sys

def est_palindrome(s):
    return s == s[::-1]

def palindromeIndex(s):
    # Complete this function
    n = len(s)
    i = 0
    j = n - 1
    while i < j:
        if s[i] != s[j]:
            if s[i + 1] == s[j]:
                if est_palindrome(s[:i] +s[i + 1:]):
                    return i
            if s[i] == s[j - 1]:
                if est_palindrome(s[:j] + s[j + 1:]):
                    return j
        i += 1
        j -= 1
    return -1

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = palindromeIndex(s)
    print(result)
