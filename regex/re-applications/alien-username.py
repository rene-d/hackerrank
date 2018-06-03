# Regex > Applications > Alien Username
# Validate the usernames from an alien planet.
#
# https://www.hackerrank.com/challenges/alien-username/problem
# challenge id: 720
#

import re

for _ in range(int(input())):
    s = input()

    ok = re.match(r"^[_\.]\d+[a-z]*_?$", s, re.I)

    print("VALID" if ok else "INVALID")
