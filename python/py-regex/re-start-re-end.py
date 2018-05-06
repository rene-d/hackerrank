# Python > Regex and Parsing > Re.start() & Re.end()
# Find the indices of the start and end of the substring matched by the group.
#
# https://www.hackerrank.com/challenges/re-start-re-end/problem
#

import re

s = input()
k = input()


if False:

    p = s.find(k)
    if p == -1:
        print((-1, -1))
    else:
        while p != -1:
            print((p, p + len(k) - 1))
            p = s.find(k, p + 1)

else:

    found = False
    for m in re.finditer(r'(?=(' + re.escape(k) + '))', s):
        print((m.start(1), m.end(1) - 1))
        found = True
    if not found:
        print((-1, -1))
