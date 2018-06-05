# Regex > Applications > Split the Phone Numbers
# This problem introduces you to the concept of matching groups in regular expressions.
#
# https://www.hackerrank.com/challenges/split-number/problem
# challenge id: 711
#

import re

for _ in range(int(input())):
    s = input()

    m = re.match(r'''
(\d{1,3})[\s\-]
(\d{1,3})[\s\-]
(\d{4,10})
''', s, re.VERBOSE)

    CountryCode, LocalAreaCode, Number = m.group(1), m.group(2), m.group(3)

    print('CountryCode={},LocalAreaCode={},Number={}'.format(CountryCode, LocalAreaCode, Number))
