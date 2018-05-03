# Python > Sets > Set .intersection() Operation
# Use the .intersection() operator to determine the number of same students in both sets.
#
# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
#

n = int(input())
english = set(map(int, input().split()))

n = int(input())
french = set(map(int, input().split()))

print(len(english & french))
