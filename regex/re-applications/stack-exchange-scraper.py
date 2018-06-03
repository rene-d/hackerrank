# Regex > Applications > Build a Stack Exchange Scraper
# Use Regular Expression to Scrape Questions from Stack Exchange.
#
# https://www.hackerrank.com/challenges/stack-exchange-scraper/problem
# https://www.hackerrank.com/contests/regex-practice-2/challenges/stack-exchange-scraper
# challenge id: 849
#

import re
import sys

s = sys.stdin.read()

m = re.findall(r'''
href="/questions/(\d+)/.*?class="question-hyperlink">(.+?)</a>
.*?
class="relativetime">(.+?)</span>
''', s, re.MULTILINE | re.VERBOSE | re.DOTALL)

for i in m:
    print(';'.join(i))
