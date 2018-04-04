# The Love-Letter Mystery
# Find the minimum number of operations required to convert a given string into a palindrome under certain conditions
#
# https://www.hackerrank.com/challenges/the-love-letter-mystery/problem
#

def theLoveLetterMystery(s):
    return sum(abs(ord(s[i]) - ord(s[-i - 1])) for i in range(len(s) // 2))

q = int(input())
for a0 in range(q):
    s = input()
    result = theLoveLetterMystery(s)
    print(result)
