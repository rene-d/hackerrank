# Game of Thrones - I
# Check whether any anagram of a string can be a palindrome or not.
#
# https://www.hackerrank.com/challenges/game-of-thrones/problem
#

# il faut une seule lettre en nombre impair si len(s) est impaire
# sinon toutes les lettres doivent être en nombre pair

def gameOfThrones(s):
    # Complete this function
    a = [0] * 26
    for c in s:
        a[ord(c) - ord('a')] += 1
    b = [0] * 2
    for i in a:
        b[i % 2] += 1
    return "YES" if b[1] <= len(s) % 2 else "NO"

s = input().strip()
result = gameOfThrones(s)
print(result)
