# Day 8: Dictionaries and Maps
# Mapping Keys to Values using a Map or Dictionary.
#
# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem
#

n = int(input())
d = {}

for _ in range(n):
    k, v = input().split()
    d[k] = v

for _ in range(n):
    k = input()
    if k in d:
        print("{}={}".format(k, d[k]))
    else:
        print("Not found")
