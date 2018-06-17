# Regex > Applications > Detect the Domain Name
# Use Regular Expressions to detect domain names from a chunk of HTML Markup provided to you.
#
# https://www.hackerrank.com/challenges/detect-the-domain-name/problem
# challenge id: 894
#

import re

ad = []
for _ in range(int(input())):
    s = input()
    a = re.findall(r"""https?://(?:ww[w2]\.){0,1}([\w\d\-\.]*\.\w+)[/?"]""", s)
    ad.extend(a)

print(';'.join(sorted(set(ad))))
