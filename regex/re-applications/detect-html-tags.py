# Regex > Applications > Detect HTML Tags
# Given N lines of HTML source, print the HTML tags found within it.
#
# https://www.hackerrank.com/challenges/detect-html-tags/problem
# https://www.hackerrank.com/contests/regex-practice-2/challenges/detect-html-tags
# challenge id: 722
#

import re

html = ''.join([input() for _ in range(int(input()))])

find_tags = r'<\s*(\w+).*?>'
match = re.findall(find_tags, html, re.I)
if bool(match):
    print(';'.join(sorted(set(tag for tag in match))))
