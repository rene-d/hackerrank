# Regex > Applications > Find a Word
# Find a given word in a sentence using regex special characters.
#
# https://www.hackerrank.com/challenges/find-a-word/problem
# challenge id: 733
#

import re

s = " ".join(input() for _ in range(int(input())))

for _ in range(int(input())):
    w = input()
    print(len(re.findall(r"(^|(?<=\W))" + w + r"(?=\W)", s, re.I)))
