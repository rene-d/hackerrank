"""
Birthday Cake Candles

https://www.hackerrank.com/challenges/birthday-cake-candles/problem
"""

import sys

def birthdayCakeCandles(n, ar):
    # Complete this function

    # en 1 passage
    nb = 0
    m = 0
    for i in ar:
        if m == i:
            nb += 1
        elif m < i:
            nb = 1
            m = i
    return nb

    # plus lent (2 passages)
    #m = max(ar)
    #return sum(1 for i in ar if i == m)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
