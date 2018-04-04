# Building a List
# Generate all possible combinations of a string
#
# https://www.hackerrank.com/challenges/building-a-list/problem
#

import itertools

def combo(s):
    n = len(s)
    def lex():
        for i in range(1, 2 ** n):
            j = i
            w = ''
            k = 0
            while j != 0:
                j, r = divmod(j, 2)
                if r:
                    w += s[k]
                k += 1
            yield w
    for w in sorted(lex()):
        print(w)


for _ in range(int(input())):
    input()
    s = input()
    combo(s)