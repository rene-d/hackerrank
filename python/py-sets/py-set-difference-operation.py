# Python > Sets > Set .difference() Operation
# Use the .difference() operator to check the differences between  sets.
#
# https://www.hackerrank.com/challenges/py-set-difference-operation/problem
#


n = int(input())
english = set(map(int, input().split()))

n = int(input())
french = set(map(int, input().split()))

print(len(english - french))
