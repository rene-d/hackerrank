# Python > Regex and Parsing > Validating UID
# Validate all the randomly generated user identification numbers according to the constraints.
#
# https://www.hackerrank.com/challenges/validating-uid/problem
#

import re

for _ in range(int(input())):
    s = input()

    ok1 = bool(re.match(r"^[a-zA-Z0-9]{10}$", s))
    ok2 = len(set(s)) == 10
    ok3 = bool(re.match(r"(?=(?:.*[A-Z]){2,})", s))
    ok4 = bool(re.match(r"(?=(?:.*\d){3,})", s))
    if ok1 and ok2 and ok3 and ok4:
        print("Valid")
    else:
        print("Invalid")
