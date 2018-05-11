# Security > Cryptography > Keyword Transposition Cipher
# Given a piece of cipher text and the keyword used to encipher it, write an algorithm to output the original message .
#
# https://www.hackerrank.com/challenges/keyword-transposition-cipher/problem
#

import string
import operator


def get_decoder(key):

    # key2: key avec les caractères en double supprimés
    # n: longueur de key2
    u = set()
    key2 = list()
    for c in key:
        if c not in u:
            u.add(c)
            key2.append(c)
    n = len(key2)

    # letters: tableau des autres caractères de l'alphabet
    letters = list(c for c in string.ascii_uppercase if c not in key2)
    letters += [' '] * ((n - len(letters) % n) % n)
    letters = list(letters[i:i + n] for i in range(0, len(letters), n))

    # complète letters avec key2
    letters.insert(0, key2)

    # trie letters en fonction de l'ordre de key2
    # pour cela, utilise un tuple intermédiaire qui contient l'ordre avant tri
    order = list(map(operator.itemgetter(1), sorted((c, i) for i, c in enumerate(key2))))
    letters = list((list(a[o] for o in order) for a in letters))

    # transpose et met à plat la matrice letters
    letters = list(a[i] for i in range(n) for a in letters if a[i] != ' ')

    # table de décodage
    decoder = dict()
    for a, b in zip(string.ascii_uppercase, letters):
        decoder[b] = a

    return lambda x: decoder.get(x, x)


for _ in range(int(input())):
    key = input()
    decoder = get_decoder(key)
    encoded = input()
    print(''.join(list(map(decoder, encoded))))
