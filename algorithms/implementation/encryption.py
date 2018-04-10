# Encryption
# Encrypt a string by arranging the characters of a string into a matrix and printing the resulting matrix column wise.
#
# https://www.hackerrank.com/challenges/encryption/problem
#

import math

def encryption(s):
    # Complete this function
    s = s.replace(' ', '')
    L = math.sqrt(len(s))
    row = math.floor(L)
    col = row
    if row * col < len(s): col += 1

    # prend un caractère tous les col, en partant du i-ème
    return " ".join(s[i::col] for i in range(col))

if __name__ == "__main__":
    s = input().strip()
    result = encryption(s)
    print(result)
