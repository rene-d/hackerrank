# Regex > Applications > Detect HTML links
# Use Regular Expressions to detect links in a given HTML fragment.
#
# https://www.hackerrank.com/challenges/detect-html-links/problem
# challenge id: 725
#

import re

html = ''.join([input() for _ in range(int(input()))])

find_href = r'<a\s+href="(.*?)".*?>(.*?)</a>'
remove_tags = r'</?(\w+).*?>'
match = re.findall(find_href, html, re.I)
if bool(match):
    for link, title in match:
        title = re.sub(remove_tags, "", title)
        print(link + ',' + title.strip())
