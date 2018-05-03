# Python > Errors and Exceptions > Incorrect Regex
# Check whether the regex is valid or not.
#
# https://www.hackerrank.com/challenges/incorrect-regex/problem
#

import re

for _ in range(int(input())):
    try:
        re.compile(input())
        print(True)
    except re.error:
        print(False)
