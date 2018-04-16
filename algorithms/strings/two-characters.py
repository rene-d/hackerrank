# Algorithms > Strings > Two Characters
# Print the length of the longest possible string $t$ you can form.
#
# https://www.hackerrank.com/challenges/two-characters/problem
#

import sys
import re
import itertools

_, s = input(), input()
result = 0
for pair in itertools.combinations("abcdefghijklmnopqrstuvwxyz", 2):
    t = ''.join(c for c in s if c in pair)
    if not re.search(r'(.)\1', t) and len(t) >= 2:
        print(pair, t, file=sys.stderr)
        result = max(result, len(t))
print(result)