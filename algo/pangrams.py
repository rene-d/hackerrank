# Pangrams
# Check whether a given string is a panagram or not.
#
# https://www.hackerrank.com/challenges/pangrams/problem
#


def pangrams(s):
    # si le set() a 26 éléments, on y a stocké les 26 lettres de l'alphabet
    letters = set()
    for c in s:
        c = c.lower()
        if c.isalpha(): letters.add(c)
    if len(letters) == 26:
        print("pangram")
    else:
        print("not pangram")


if __name__ == '__main__':
    s = input()
    pangrams(s)
