# Weekly Challenges - Week 5 > Even Odd Query
# Is the number odd or even?
#
# https://www.hackerrank.com/contests/w5/challenges/even-odd-query
#

input()
A = list(map(int, input().split()))

for _ in range(int(input())):
    x, y = map(int, input().split())
    if A[x - 1] % 2 == 1 or x > y or (x < y and A[x] == 0):
        print("Odd")
    else:
        print("Even")
