# Python > Regex and Parsing > Group(), Groups() & Groupdict()
# Using group(), groups(), and groupdict(), find the subgroup(s) of the match.
#
# https://www.hackerrank.com/challenges/re-group-groups/problem
#

import re

s = input()

# \1 (dans la regex) est la référence au premier groupe

m = re.search(r"([0-9a-zA-Z])\1+", s)
if m:
    print(m.group(1))
else:
    print(-1)
