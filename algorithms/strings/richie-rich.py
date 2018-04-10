# Highest Value Palindrome
# Make a number palindromic in no more than $k$ moves, maximal.
#
# https://www.hackerrank.com/challenges/richie-rich/problem
#
#!/bin/python3

import os
import sys


#
# Complete the highestValuePalindrome function below.
#
def highestValuePalindrome(s, n, k):
    pos = []
    p = []
    for i in range(0, n // 2):
        if s[i] != s[-1 - i]:
            if k == 0: return "-1"
            k -= 1
            # on retient le chiffre le plus grand
            p += max(s[i], s[-1 - i])

            # on mémorise la position du changement
            # pour passer à 9 éventuellement plus tard
            pos.append(i)
        else:
            p += s[i]

    # autant que possible maximise le résultat en mettant des 9
    # i.e. autant qu'on a des crédits k
    i = 0
    while k > 0 and i < len(p):
        if p[i] != '9':
            if i in pos:
                # si c'était un chiffre déjà changé, le coût est 1 au lieu de 2
                p[i] = '9'
                k -= 1
            elif k >= 2:
                p[i] = '9'
                k -= 2
        i += 1

    # ajoute le caractère du milieu isolé si nombre impair
    if n % 2 == 1:
        if k >= 1:
            # il reste un crédit: on maximise
            p += '9'
        else:
            p += s[n // 2]

    # ajoute le p inversé pour faire le palindrome
    if n % 2 == 1:
        p = p + p[-2::-1]
    else:
        p = p + p[::-1]

    return ''.join(p)


if __name__ == '__main__':
    n, k = map(int, input().split())
    s = input()
    result = highestValuePalindrome(s, n, k)
    print(result)
