# Making Anagrams
# How many characters should one delete to make two given strings anagrams of each other?
#
# https://www.hackerrank.com/challenges/making-anagrams/problem
#


def makingAnagrams(s1, s2):
    # Complete this function
    a = [0] * 26
    b = [0] * 26
    for c in s1:
        j = ord(c) - ord('a')
        a[j] += 1
    for c in s2:
        j = ord(c) - ord('a')
        b[j] += 1
    return sum(abs(a[i] - b[i]) for i in range(26))


s1 = input().strip()
s2 = input().strip()
result = makingAnagrams(s1, s2)
print(result)
