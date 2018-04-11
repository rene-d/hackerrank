# Tutorials > 30 Days of Code > Day 10: Binary Numbers
# Find the maximum number of consecutive 1's in the base-2 representation of a base-10 number.
#
# https://www.hackerrank.com/challenges/30-binary-numbers/problem
#

n = int(input())

nb = 0
result = 0

while n != 0:
    n, r = divmod(n, 2)
    if r == 1:
        nb += 1
        if nb > result:
            result = nb
    else:
        nb = 0

print(result)
