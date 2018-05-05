# Python > Regex and Parsing > Detect Floating Point Number
# Validate a floating point number using the regular expression module for Python.
#
# https://www.hackerrank.com/challenges/introduction-to-regex/problem
#

import re

p = re.compile(r'^[+-]?\d*\.\d+$')
for _ in range(int(input())):
    print(bool(p.match(input())))
