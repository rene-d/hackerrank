"""
Validating Credit Card Numbers

https://www.hackerrank.com/challenges/validating-credit-card-number/problem
"""

import re


for _ in range(int(input())):
    num = input()

    ok1 = bool(re.match(r"^[456]\d{15}$", num))
    ok2 = bool(re.match(r"^[456]\d{3}\-\d{4}\-\d{4}\-\d{4}$", num))
    num = num.replace("-", "")
    ok3 = bool(re.match(r"(?!.*(\d)(-?\1){3})", num))
    if (ok1 or ok2) and ok3:
        print("Valid")
    else:
        print("Invalid")
