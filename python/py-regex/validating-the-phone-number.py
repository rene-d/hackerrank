# Python > Regex and Parsing > Validating phone numbers
# Check whether the given phone number is valid or not.
#
# https://www.hackerrank.com/challenges/validating-the-phone-number/problem
#

import re

for _ in range(int(input())):
    s = input()
    print("YES" if re.match(r'^[789]\d{9}$', s) else "NO")
