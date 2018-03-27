# Append and Delete
# Can you convert $s$ to $t$ by performing exactly $k$ operations?
#
# https://www.hackerrank.com/challenges/append-and-delete/problem
#

import sys

def appendAndDelete(s, t, k):
    # Complete this function
    if k >= len(s) + len(t): return "Yes"
    i = 0
    while i < min(len(s), len(t)) and s[i] == t[i]:
        i += 1

    k -= len(s) - i # pour supprimer les caractères de fin différents
    k -= len(t) - i # pour ajouter les caractères de fin

    if k < 0: return "No"
    if k == 0: return "Yes"
    if k % 2 == 0: return "Yes"
    if k > len(s) * 2: return "Yes"
    return "No"


if __name__ == "__main__":
    s = input()
    t = input()
    k = int(input())
    print(appendAndDelete(s, t, k))
