# Regex > Applications > Saying Hi
# Use a regex to print all the lines that start with "hi " but are not immediately followed by a 'd' or 'D'.
#
# https://www.hackerrank.com/challenges/saying-hi/problem
# challenge id: 713
#

import re

for _ in range(int(input())):
    s = input()
    if re.match(r"^hi\s[^d]", s, re.I):
        print(s)
