# HackerRank in a String!
# Determine if a string contains a subsequence of characters that spell "hackerrank".
#
# https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem
#

def hackerrankInString(s):
    # Complete this function
    p = "hackerrank"
    i = 0
    for c in s:
        if c == p[i]:
            i += 1
            if i == len(p):
                return "YES"
    return "NO"

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()
        result = hackerrankInString(s)
        print(result)
