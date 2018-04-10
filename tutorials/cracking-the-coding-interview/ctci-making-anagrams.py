# Strings: Making Anagrams
# How many characters should one delete to make two given strings anagrams of each other?
#
# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem
#


def number_needed(a, b):
    a = sorted(a)
    b = sorted(b)
    i, j, n = 0, 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            # on consomme les caractères de a
            i += 1
        elif a[i] > b[j]:
            # on consomme les caractères de b
            j += 1
        else:
            # on a le même caractère: on consomme a et b
            i += 1
            j += 1
            n += 1
    return len(a) + len(b) - n * 2


a = input().strip()
b = input().strip()

print(number_needed(a, b))
