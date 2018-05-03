# Python > Sets > Check Subset
# Verify if set A is a subset of set B.
#
# https://www.hackerrank.com/challenges/py-check-subset/problem
#

for _ in range(int(input())):
    _, a = input(), set(map(int, input().split()))
    _, b = input(), set(map(int, input().split()))
    print(b.intersection(a) == a)
