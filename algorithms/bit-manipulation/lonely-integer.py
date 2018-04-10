# Lonely Integer
# Find the unique element in an array of integer pairs.
# 
# https://www.hackerrank.com/challenges/lonely-integer/problem
# 

import functools
import operator

def lonelyinteger(a):
    # Complete this function
    
    # fonctionne car les nombres sont en double sauf un :
    # le xor va annuler les nombres en double (i xor i = 0)
    # et il ne restera que l'unique (i xor 0 = i)
    return functools.reduce(operator.xor, a)
    
    # solution plus triviale, mais fonctionne si les nombres
    # sont en triple, quadruple, etc.
    one = set()
    two_or_more = set()
    for i in a:
        if i in one:
            two_or_more.add(i)
        else:
            one.add(i)
    return (one - two_or_more).pop()
    

n = int(input())
a = list(map(int, input().split()))
result = lonelyinteger(a)
print(result)

