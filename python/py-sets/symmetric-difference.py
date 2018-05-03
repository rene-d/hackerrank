# Python > Sets > Symmetric Difference
# Learn about sets as a data type.
#
# https://www.hackerrank.com/challenges/symmetric-difference/problem
#

m = int(input())
M = set(map(int, input().split()))

n = int(input())
N = set(map(int, input().split()))

a = (M - N).union(N - M)
for i in sorted(a):
    print(i)
