# Regex > Applications > Detect the Email Addresses
# Use Regular Expressions to detect the email addresses embedded in a given chunk of text.
#
# https://www.hackerrank.com/challenges/detect-the-email-addresses/problem
# challenge id: 895
#

import re

ad = []
for _ in range(int(input())):
    s = input()

    a = re.findall(r"\b[\w\.]+@(?:\w+\.)+\w+\b", s)

    ad.extend(a)

print(';'.join(sorted(set(ad))))
