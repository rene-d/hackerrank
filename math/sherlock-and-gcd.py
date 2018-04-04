# Sherlock and GCD
# Help Sherlock in finding the subset.
#
# https://www.hackerrank.com/challenges/sherlock-and-gcd/problem
#

from math import gcd

def verif(a):
    d = a[0]
    for i in range(1, len(a)):
        d = gcd(d, a[i])

    if d == 1: return "YES"
    return "NO"

for i in range(int(input())):
    input()
    a = list(map(int, input().split()))
    print(verif(a))
