"""
Word Order

https://www.hackerrank.com/challenges/word-order/problem
"""

from collections import OrderedDict

dico = OrderedDict()
for _ in range(int(input())):
    word = input()    
    dico[word] = dico.get(word, 0) + 1

print(len(dico))
print(' '.join(map(str, dico.values())))
