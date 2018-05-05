# Project Euler #16: Power digit sum
#
# https://www.hackerrank.com/contests/projecteuler/challenges/euler016/problem

for _ in range(int(input())):
    print(sum(int(c) for c in str(2 ** int(input()))))
