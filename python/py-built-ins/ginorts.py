# Python > Built-Ins > ginortS
# An uneasy sort.
#
# https://www.hackerrank.com/challenges/ginorts/problem
#

def ordre(c):
    if c.islower(): return ord(c)
    if c.isupper(): return 1000 + ord(c)
    if c.isdigit():
        c = int(c)
        return 2000 + 10 * (1 - c % 2) + c
    return 0

# Solution avec fonction d'ordre
print(*sorted(input(), key=ordre), sep='')

# Solution plus concise
# print(*sorted(input().strip(), key="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468".index), sep='')