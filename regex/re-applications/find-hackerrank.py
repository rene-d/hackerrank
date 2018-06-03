# Regex > Applications > Find HackerRank
# Write a regex to find out if conversations start/end or both start and end with hackerrank
#
# https://www.hackerrank.com/challenges/find-hackerrank/problem
# challenge id: 709
#

import re

for _ in range(int(input())):
    s = input().lower()

    a = s.startswith('hackerrank')
    b = s.endswith('hackerrank')
    if a and b:
        print(0)
    elif a:
        print(1)
    elif b:
        print(2)
    else:
        print(-1)
