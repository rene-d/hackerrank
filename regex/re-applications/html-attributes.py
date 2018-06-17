# Regex > Applications > Detect HTML Attributes
# Use Regular Expressions to detect HTML Attributes corresponding to various tags.
#
# https://www.hackerrank.com/challenges/html-attributes/problem
# https://www.hackerrank.com/contests/codesprint-practice/challenges/html-attributes
# challenge id: 724
#

import sys
import re


s = ' '.join(input() for _ in range(int(input())))

tags = {}
for tag, p in re.findall(r'<(\w+)\s?(.*?)>', s):
    attr = set(a for a in re.findall(r'(\w+)=[\'\"]', p))
    if tag not in tags:
        tags[tag] = attr
    else:
        tags[tag] |= attr

for tag in sorted(tags.keys()):
    print(tag + ':' + ','.join(sorted(tags[tag])))
