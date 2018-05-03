# Python > Sets > Set Mutations
# Using various operations, change the content of a set and output the new sum.
#
# https://www.hackerrank.com/challenges/py-set-mutations/problem
#


n = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    cmd, n = input().split()
    x = set(map(int, input().split()))

    if cmd == "intersection_update":
        s.intersection_update(x)
    elif cmd == "update":
        s.update(x)
    elif cmd == "symmetric_difference_update":
        s.symmetric_difference_update(x)
    elif cmd == "difference_update":
        s.difference_update(x)


print(sum(s))