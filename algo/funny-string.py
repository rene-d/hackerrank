# Funny String
# Is the absolute difference between consecutive characters is the same for a string and the reverse of that string for all indices.
#
# https://www.hackerrank.com/challenges/funny-string/problem
#


def funnyString(s):
    # nota: le demi-parcours suffit, sinon on teste 2 fois la même chose
    for i in range(0, len(s) // 2):
        if abs(ord(s[i]) - ord(s[i + 1])) != abs(ord(s[-1 - i]) - ord(s[-2 - i])):
            print("Not Funny")
            return
    print("Funny")


q = int(input())
for _ in range(q):
    s = input()
    funnyString(s)
