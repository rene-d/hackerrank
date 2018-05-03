# Python > Sets > Set .symmetric_difference() Operation
# Making symmetric difference of sets.
#
# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
#


n = int(input())
english = set(map(int, input().split()))

n = int(input())
french = set(map(int, input().split()))

print(len(english ^ french))
