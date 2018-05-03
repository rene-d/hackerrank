# Python > Sets > Check Strict Superset
# Check if A is a strict superset of the other given sets.
#
# https://www.hackerrank.com/challenges/py-check-strict-superset/problem
#

a = set(map(int, input().split()))
strict_superset = True
for _ in range(int(input())):
    x = set(map(int, input().split()))
    if not ((len(x - a) == 0 and len(a - x) > 0)):
        strict_superset = False
        break
print(strict_superset)
