"""
Validating Postal Codes

https://www.hackerrank.com/challenges/validating-postalcode/problem
"""

import re

def validate(code):
    ok = bool(re.match(r"^[1-9][0-9]{5}$", code))
    alternative = sum(int(code[i - 1] == code[i + 1]) for i in range(1, len(code) - 1))
    return ok and alternative < 2

print(validate(input()))
