# Regex > Applications > Building a Smart IDE: Identifying comments
# A Text Processing Challenge. Identify the comments in program source codes.
#
# https://www.hackerrank.com/challenges/ide-identifying-comments/problem
# https://www.hackerrank.com/contests/regex-practice-1/challenges/ide-identifying-comments
# challenge id: 670
#

import re
import sys

s = sys.stdin.read()

p = r'(/\*.*?\*/|//.*?$)'

for i in re.findall(p, s, re.DOTALL | re.MULTILINE):
    for j in re.split(r'\n', i):
        print(j.strip())
