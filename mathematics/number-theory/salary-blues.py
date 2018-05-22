# Mathematics > Number Theory > Salary Blues
# Help manager of HackerX company to normalize salaries.
#
# https://www.hackerrank.com/challenges/salary-blues/problem
# https://www.hackerrank.com/contests/infinitum-apr14/challenges/salary-blues
# challenge id: 1833
#

from math import gcd

n, q = map(int, input().split())

A = list(map(int, input().split()))

a0 = A[0]
for i in range(1, len(A)):
    A[i] -= a0

g = A[1]
for i in range(2, len(A)):
    g = gcd(g, A[i])

for _ in range(q):
    k = int(input())
    if len(A) == 1:
        print(a0 + k)
    else:
        print(gcd(g, a0 + k))
