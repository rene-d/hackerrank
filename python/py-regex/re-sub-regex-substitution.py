# Python > Regex and Parsing > Regex Substitution
# Substitute a string using regex tools.
#
# https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem
#

import re

for _ in range(int(input())):
    s = input()
    s = re.sub(r'(?<= )(&&)(?= )', 'and', s)            # (?<= ) et (?= ) pour ne pas consommer les espaces
    s = re.sub(r'(?<= )(\|\|)(?= )', 'or', s)
    print(s)
