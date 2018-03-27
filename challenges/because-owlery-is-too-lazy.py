#
# https://www.hackerrank.com/contests/openbracket-2017/challenges/because-owlery-is-too-lazy
#

import re

def isValid(email):
    # Complete this function
    if bool(re.match(r"^[a-z]{5}@hogwarts\.com$", email)):
        return "Yes"
    else:
        return "No"

if __name__ == "__main__":
    s = input().strip()
    result = isValid(s)
    print(result)
