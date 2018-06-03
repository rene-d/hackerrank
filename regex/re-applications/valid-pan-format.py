# Regex > Applications > Valid PAN format
# Use regex to determine the validity of a given set of characters.
#
# https://www.hackerrank.com/challenges/valid-pan-format/problem
# challenge id: 712
#

import re

for _ in range(int(input())):
    s = input()

    # <char><char><char><char><char><digit><digit><digit><digit><char>

    ok = re.match(r'''
^
[A-Z]{5}            # <char><char><char><char><char>
\d{4}               # <digit><digit><digit><digit>
[A-Z]{1}            # <char>
$
''', s, re.VERBOSE)

    print("YES" if ok else "NO")
