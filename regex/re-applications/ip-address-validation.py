# Regex > Applications > IP Address Validation
# Validate possible IP Addresses with regex.
#
# https://www.hackerrank.com/challenges/ip-address-validation/problem
# https://www.hackerrank.com/contests/programming-interviews-practice-session/challenges/ip-address-validation
# challenge id: 896
#

import re


def check_ip(a):
    m = re.match(r"^(\d+)\.(\d+)\.(\d+).(\d+)$", a)
    if m:
        if all(map(lambda x: 0 <= int(x) <= 255, m.groups())):
            return "IPv4"
    else:
        m = re.match(r"^([a-f0-9]{1,4}:){7}[a-f0-9]{1,4}$", a, re.I)
        if m:
            return "IPv6"
    return "Neither"


for _ in range(int(input())):
    print(check_ip(input()))
