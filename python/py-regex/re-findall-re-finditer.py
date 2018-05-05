# Python > Regex and Parsing > Re.findall() & Re.finditer()
# Find all the pattern matches using the expressions re.findall() and re.finditer().
#
# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem
#

import re

found = False
s = input()
for i in re.findall("(?<=[^aeiou])([aeiou]{2,})[^aeiou]", s, flags=re.I):
    print(i)
    found = True
if not found:
    print(-1)
