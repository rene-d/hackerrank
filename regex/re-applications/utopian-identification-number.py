# Regex > Applications > Utopian Identification Number
# Can you use regular expressions to check if the Utopian Identification Number is valid or not?
#
# https://www.hackerrank.com/challenges/utopian-identification-number/problem
# challenge id: 721
#

import re

for _ in range(int(input())):
    s = input()
    ok = re.match(r'''
^
[a-z]{0,3}              # The string must begin with between 0-3 (inclusive) lowercase letters
\d{2,8}                 # sequence of digits, length between 2 and 8
[A-Z]{3,}               # 3 uppercase letters or more
$
''', s, re.VERBOSE)
    print("VALID" if ok else "INVALID")
