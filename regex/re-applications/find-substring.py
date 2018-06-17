# Regex > Applications > Find A Sub-Word
# Use RegEx  to count the number of times a sub-word appears in a given set of sentences.
#
# https://www.hackerrank.com/challenges/find-substring/problem
# challenge id: 734
#

import re

s = " ".join(input() for _ in range(int(input())))

for _ in range(int(input())):
    sw = input()
    print(len(re.findall(r"\b[\d\w]+" + sw + r"[\d\w]+\b", s)))
