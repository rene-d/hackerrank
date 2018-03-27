# CamelCase
#    
# 
# https://www.hackerrank.com/challenges/camelcase/problem
# 

import sys

def camelcase(s):
    # Complete this function
    # +1 pour le premier mot, après il suffit de compter les majuscules
    return 1 + sum(1 for c in s if c.upper() == c)

if __name__ == "__main__":
    s = input().strip()
    result = camelcase(s)
    print(result)
