# Bigger is Greater
# Rearrange the letters of a string to construct another string such that the new string is lexicographically greater than the original.
#
# https://www.hackerrank.com/challenges/bigger-is-greater/problem
#

import sys


def biggerIsGreater(w):
    # Complete this
    w = list(w)
    i = len(w) - 1
    while i > 0 and w[i - 1] >= w[i]:
        i -= 1
    if i == 0: return "no answer"

    # w[i - 1] est le caractère pivot
    j = len(w) - 1
    while w[j] <= w[i - 1]:
        j -= 1
    w[i - 1], w[j] = w[j], w[i - 1]

    # trie le reste (qui est déjà en ordre décroissant)
    w[i:] = w[len(w) - 1:i - 1:-1]
    return ''.join(w)


if __name__ == "__main__":
    T = int(input().strip())
    for a0 in range(T):
        w = input().strip()
        result = biggerIsGreater(w)
        print(result)
