# Python > Sets > Set .union() Operation
# Use the .union() operator to determine the number of students.
#
# https://www.hackerrank.com/challenges/py-set-union/problem
#

n = int(input())
english = set(map(int, input().split()))

n = int(input())
french = set(map(int, input().split()))

print(len(english | french))
