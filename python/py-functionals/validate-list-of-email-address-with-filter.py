"""
Validating Email Addresses With a Filter 

https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem
"""

import re


def fun(s):
    # return True if s is a valid email, else return False
    return bool(re.match(r"^[A-Za-z0-9_\-]+@[a-z0-9]+\.[a-z]{1,3}$", s))


def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
