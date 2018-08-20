# Mathematics > Number Theory > Long Permutation
# Determine the n^th element of an infinite permutation!
#
# https://www.hackerrank.com/challenges/long-permutation/problem
# https://www.hackerrank.com/contests/101hack37/challenges/long-permutation
# challenge id: 21494
#

n, m = map(int, input().split())
p = list(map(int, input().split()))

x = 0
while m >= 1:
    m -= 1
    x = p[x]
    if x >= n:
        x += m
        break

print(x)
