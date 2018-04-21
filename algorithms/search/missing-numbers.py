# Algorithms > Search > Missing Numbers
# Find the numbers missing from a sequence given a permutation of the original sequence
#
# https://www.hackerrank.com/challenges/missing-numbers/problem
#

# définit un tableau pour compter les nombres
# 200 comme ça pas la peine de chercher le min: on centre sur la première valeur rencontrée

arr = [0] * 200
offset = None

input()     # skip n
for i in map(int, input().split()):
    if offset is None:
        offset = i - 100
    arr[i - offset] += 1

input()     # skip m
for i in map(int, input().split()):
    arr[i - offset] -= 1

print(" ".join(str(k + offset) for k, i in enumerate(arr) if i != 0))
