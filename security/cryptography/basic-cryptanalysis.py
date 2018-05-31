# Security > Cryptography > Basic Cryptanalysis
# Given a piece of text encoded with a simple monoalphabetic substitution cipher, use basic cryptanalytic techniques to attempt to recover the original plain text.
#
# https://www.hackerrank.com/challenges/basic-cryptanalysis/problem
# challenge id: 787
#

# principe: chercher quelle est la bonne permutation de lettres

# le dictionnaire
dictionary = {}
for s in open("dictionary.lst"):
    s = s.strip()
    if len(s) not in dictionary:
        dictionary[len(s)] = list()
    dictionary[len(s)].append(s.lower())

# les mots encryptés
words = [s.strip().lower() for s in input().split()]

# toutes les permutations
total_perms = []
for crypted in sorted(words, key=lambda s:-len(s)):
    perms = []
    for word in dictionary[len(crypted)]:
        perm = ['.'] * 52
        for a, b in zip(crypted, word):
            a = ord(a) - 97
            if perm[a] == '.':
                perm[a] = b
            else:
                if perm[a] != b:
                    break
        else:
            # crypted -> word est une permutation possible

            for a, b in zip(crypted, word):
                b = ord(b) - 97
                perm[b + 26] = a

            perms.append(perm)

    if len(perms) == 0:
        print("pb avec ", crypted)
        exit()
    total_perms.append(perms)

# tri par possibilités croissantes
total_perms.sort(key=lambda x: len(x))


# recherche récursive de la solution: on cherche les permutations de lettres
# qui sont compatibles
def search(step, keys):

    if step == len(total_perms):
        return keys.copy()

    for perm in total_perms[step]:

        for a, b in zip(keys, perm):
            if a == '.' or b == '.':
                continue
            if a != b:
                break

        else:
            keys2 = keys.copy()
            for i, b in enumerate(perm):
                if b != '.':
                    keys2[i] = b

            ok = search(step + 1, keys2)
            if ok:
                return ok
    return False


# on y va
k = search(0, ['.'] * 52)

# affiche le résultat
print(*[''.join(k[ord(c) - 97] for c in word) for word in words])
