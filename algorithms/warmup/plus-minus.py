"""
Plus Minus

https://www.hackerrank.com/challenges/plus-minus/problem
"""

import sys


def plusMinus(arr):
    # Complete this function
    negatif = positif = zero = 0
    for i in arr:
        if i < 0:
            negatif += 1
        elif i > 0:
            positif += 1
        else:
            zero += 1
    
    print("%.06f" % (positif / len(arr)))      
    print("%.06f" % (negatif / len(arr)))            
    print("%.06f" % (zero / len(arr)))            


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    plusMinus(arr)

