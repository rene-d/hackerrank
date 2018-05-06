# Python > Regex and Parsing > Validating and Parsing Email Addresses
# Print valid email addresses according to the constraints.
#
# https://www.hackerrank.com/challenges/validating-named-email-addresses/problem
#

import re

for _ in range(int(input())):
    s = input().strip()

    if re.match(r'^.*<[a-z][\w\.\-]*@[a-z]+\.[a-z]{1,3}>$', s, re.I):
        print(s)
