# Sock Merchant
# How many pairs of socks John can sell?
# 
# https://www.hackerrank.com/challenges/sock-merchant/problem
# 

#!/bin/python3

import sys
import itertools


def sockMerchant(n, ar):
    # Complete this function

    # - trie le tableau des codes couleur
    # - itertools.groupby retourne les groupes de valeurs identiques
    # - le nombre de paires de valeurs identiques est la moitié
    return sum(len(list(g)) // 2 for k, g in itertools.groupby(sorted(ar)))
        
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)
